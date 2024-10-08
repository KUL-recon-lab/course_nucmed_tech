"""
Run simple MLEM reconstruction on the brainweb phantom
"""

# %%
from __future__ import annotations

import array_api_compat.numpy as xp

import parallelproj
from array_api_compat import to_device
import array_api_compat.numpy as np
import matplotlib.pyplot as plt

from utils_data import bw_pet_phantom
from utils_functions import NegPoissonLogL, SmoothFunction, QuadraticPrior

from scipy.optimize import fmin_l_bfgs_b

# choose a device (CPU or CUDA GPU)
if "numpy" in xp.__name__:
    # using numpy, device must be cpu
    dev = "cpu"
elif "cupy" in xp.__name__:
    # using cupy, only cuda devices are possible
    dev = xp.cuda.Device(0)
elif "torch" in xp.__name__:
    # using torch valid choices are 'cpu' or 'cuda'
    if parallelproj.cuda_present:
        dev = "cuda"
    else:
        dev = "cpu"

# %%
# Input parameters

num_iter_lbfgs = 100
fwhm_mm_data = 4.5
fwhm_mm_recon = 4.5
counts = 1e6
prior_type = "quadratic"
betas = [0.003, 0.03, 0.3]
seed = 1

# %%
np.random.seed(seed)

# %%
# Setup of the forward model :math:`\bar{y}(x) = A x + s`
# --------------------------------------------------------
#
# We setup a linear forward operator :math:`A` consisting of an
# image-based resolution model, a non-TOF PET projector and an attenuation model
#
# .. note::
#     The MLEM implementation below works with all linear operators that
#     subclass :class:`.LinearOperator` (e.g. the high-level projectors).

num_rings = 1
scanner = parallelproj.RegularPolygonPETScannerGeometry(
    xp,
    dev,
    radius=300.0,
    num_sides=28,
    num_lor_endpoints_per_side=16,
    lor_spacing=4.0,
    ring_positions=xp.asarray([0.0], dtype=np.float32),
    symmetry_axis=2,
)

# %%
# setup a activity and attenuation image based on the brainweb phantom
x_true, x_att = bw_pet_phantom(num_downsample=1)
x_true = to_device(xp.astype(xp.expand_dims(x_true, -1), xp.float32), dev)
x_att = to_device(xp.astype(xp.expand_dims(x_att, -1), xp.float32), dev)

# %%
# setup the LOR descriptor that defines the sinogram

img_shape = x_true.shape
voxel_size = 3 * (0.5 * (512 / x_true.shape[0]),)

lor_desc = parallelproj.RegularPolygonPETLORDescriptor(
    scanner,
    radial_trim=161,
    sinogram_order=parallelproj.SinogramSpatialAxisOrder.RVP,
)

proj = parallelproj.RegularPolygonPETProjector(
    lor_desc, img_shape=img_shape, voxel_size=voxel_size
)


# %%
# Attenuation sinogram setup
# ------------------------------------

# calculate the attenuation sinogram
att_sino = xp.exp(-proj(x_att))

# %%
# Complete PET forward model setup
# --------------------------------
#
# We combine an image-based resolution model,
# a non-TOF or TOF PET projector and an attenuation model
# into a single linear operator.

# enable TOF - comment if you want to run non-TOF
# proj.tof_parameters = parallelproj.TOFParameters(
#    num_tofbins=13, tofbin_width=12.0, sigma_tof=12.0
# )

# setup the attenuation multiplication operator which is different
# for TOF and non-TOF since the attenuation sinogram is always non-TOF
if proj.tof:
    att_op = parallelproj.TOFNonTOFElementwiseMultiplicationOperator(
        proj.out_shape, att_sino
    )
else:
    att_op = parallelproj.ElementwiseMultiplicationOperator(att_sino)

res_model_data = parallelproj.GaussianFilterOperator(
    proj.in_shape, sigma=fwhm_mm_data / (2.35 * proj.voxel_size)
)

# compose all 3 operators into a single linear operator
pet_lin_op_data = parallelproj.CompositeLinearOperator((att_op, proj, res_model_data))


# %%
# Simulation of projection data
# -----------------------------
#
# We setup an arbitrary ground truth :math:`x_{true}` and simulate
# noise-free and noisy data :math:`y` by adding Poisson noise.

# simulated noise-free data
noise_free_data = pet_lin_op_data(x_true)

# scale the total of the noise_free_data such that get the specified
# number of true counts

if counts > 0:
    scale_fac = counts / float(xp.sum(noise_free_data))
    noise_free_data *= scale_fac
    x_true *= scale_fac

# generate a contant contamination sinogram
contamination = xp.full(
    noise_free_data.shape,
    0.5 * float(xp.mean(noise_free_data)),
    device=dev,
    dtype=xp.float32,
)

noise_free_data += contamination

# add Poisson noise
if counts > 0:
    y = xp.asarray(
        np.random.poisson(parallelproj.to_numpy_array(noise_free_data)),
        device=dev,
        dtype=xp.float32,
    )
else:
    y = noise_free_data


# %%
# Run the MLEM iterations
# -----------------------

# setup a separate resolution model for the reconstruction
res_model_recon = parallelproj.GaussianFilterOperator(
    proj.in_shape, sigma=fwhm_mm_recon / (2.35 * proj.voxel_size)
)

# compose all 3 operators into a single linear operator
pet_lin_op_recon = parallelproj.CompositeLinearOperator((att_op, proj, res_model_recon))

# setup the negative poisson logL object
neg_poisson_logl: SmoothFunction = NegPoissonLogL(y, pet_lin_op_recon, contamination)

x_map = []
nrmse = []

if prior_type == "quadratic":
    prior: SmoothFunction = QuadraticPrior(pet_lin_op_recon.in_shape, xp, dev)
else:
    raise ValueError(f"Invalid prior type {prior_type}")

for i, beta in enumerate(betas):
    # setup the prior
    prior.scale = beta

    def cost_fct(z):
        return neg_poisson_logl(z) + prior(z)

    def cost_gradient(z):
        return neg_poisson_logl.gradient(z) + prior.gradient(z)

    # use L-BFGS-B to optimize the negative Poisson logL
    x_init = xp.ones(xp.prod(pet_lin_op_recon.in_shape), dtype=xp.float32, device=dev)

    res = fmin_l_bfgs_b(
        cost_fct,
        x_init,
        fprime=cost_gradient,
        bounds=x_init.size * [[0, None]],
        disp=1,
        maxiter=num_iter_lbfgs,
    )

    x = res[0].reshape(pet_lin_op_recon.in_shape)

    x_map.append(x)

    nrmse.append(float(xp.sqrt(xp.mean((x - x_true) ** 2))) / float(xp.max(x_true)))

# %%
# Visualize the results
# ---------------------


num_rows = 2
num_cols = len(x_map) + 1
vmax = 1.3 * float(x_true.max())

fig, ax = plt.subplots(
    num_rows,
    num_cols,
    figsize=(0.85 * num_cols * 4.5, num_rows * 4.5),
    tight_layout=True,
)
img00 = ax[0, 0].imshow(
    parallelproj.to_numpy_array(x_true[:, :, 0]).T, cmap="Greys", vmin=0, vmax=vmax
)
img10 = ax[1, 0].imshow(
    parallelproj.to_numpy_array(y[:, :, 0]).T, cmap="Greys", aspect="auto"
)
ax[0, 0].set_title(f"true image", fontsize="medium")
ax[1, 0].set_title(f"emission sinogram", fontsize="medium")
fig.colorbar(img00, location="bottom", fraction=0.03)
fig.colorbar(img10, location="bottom", fraction=0.03)

for i, x in enumerate(x_map):
    img01 = ax[0, i + 1].imshow(
        parallelproj.to_numpy_array(x[:, :, 0]).T, cmap="Greys", vmin=0, vmax=vmax
    )
    img11 = ax[1, i + 1].imshow(
        parallelproj.to_numpy_array(x[:, :, 0] - x_true[:, :, 0]).T,
        cmap="seismic",
        vmin=-0.5 * vmax,
        vmax=0.5 * vmax,
    )

    ax[0, i + 1].set_title(
        f"MAP {prior_type} prior $\\beta$ = {betas[i]:.2E}", fontsize="medium"
    )
    ax[1, i + 1].set_title(f"MAP - true image, NRMSE {nrmse[i]:.2f}", fontsize="medium")

    fig.colorbar(img01, location="bottom", fraction=0.03)
    fig.colorbar(img11, location="bottom", fraction=0.03)

fig.show()
plt.show()
