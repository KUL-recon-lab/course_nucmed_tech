from __future__ import annotations

import array_api_compat.numpy as np
import matplotlib.pyplot as plt
import parallelproj

from array_api_compat import to_device
from utils import RadonDisk, RadonObjectSequence

# %%
import numpy as xp

dev = "cpu"

# %%
counts = 0

# choose number of radial elements, number of views and angular coverage
num_rad = 301
theta_max = xp.pi
num_theta = int(0.5 * num_rad * xp.pi * (theta_max / xp.pi)) + 1
num_theta = num_theta // 1

r = xp.linspace(-30, 30, num_rad, device=dev, dtype=xp.float32)
theta = xp.linspace(
    0, theta_max, num_theta, endpoint=False, device=dev, dtype=xp.float32
)
R, THETA = xp.meshgrid(r, theta, indexing="ij")
# X0, X1 = xp.meshgrid(r, r, indexing="ij")
# x = xp.linspace(float(xp.min(r)), float(xp.max(r)), 1001, device=dev, dtype=xp.float32)
# X0hr, X1hr = xp.meshgrid(x, x, indexing="ij")

print(f"num rad:   {num_rad}")
print(f"theta max:   {180*theta_max/xp.pi:.2f} deg")
print(f"delta theta: {180*float(theta[1]-theta[0])/xp.pi:.2f} deg")


# %%
# define an object with known radon transform
disk0 = RadonDisk(xp, dev, 8.0)
disk0.amplitude = 1.0
disk0.s0 = 3.0

disk1 = RadonDisk(xp, dev, 2.0)
disk1.amplitude = 0.5
disk1.x1_offset = 4.67

disk2 = RadonDisk(xp, dev, 1.4)
disk2.amplitude = -0.5
disk2.x0_offset = -10.0

disk3 = RadonDisk(xp, dev, 0.93)
disk3.amplitude = -0.5
disk3.x1_offset = -4.67

disk4 = RadonDisk(xp, dev, 0.67)
disk4.amplitude = 1.0
disk4.x1_offset = -4.67

radon_object = RadonObjectSequence([disk0, disk1, disk2, disk3, disk4])

# %%
# analytic calculation of the randon transform
img_radon = radon_object.radon_transform(R, THETA)

# %%
# add attenuation and Poisson noise

attn_img_fwd = disk0.radon_transform(R, THETA)
attn_img_fwd /= 0.3 * attn_img_fwd.max()
# attn_sino = xp.exp(-attn_img_fwd)
attn_sino = 1.0

noise_free_emis_sino = img_radon * attn_sino

if counts > 0:
    scale_face = counts / noise_free_emis_sino.sum()
    noise_free_emis_sino *= scale_face
    emis_sino = xp.random.poisson(noise_free_emis_sino).astype(float)
else:
    scale_face = 1.0
    emis_sino = noise_free_emis_sino

pre_corrected_sino = emis_sino / attn_sino

# %%
# filtered back projection

# setup a discrete ramp filter
n_filter = r.shape[0]
r_shift = xp.arange(n_filter, device=dev, dtype=xp.float64) - n_filter // 2
f = xp.zeros(n_filter, device=dev, dtype=xp.float64)
f[r_shift != 0] = -1 / (xp.pi**2 * r_shift[r_shift != 0] ** 2)
f[(r_shift % 2) == 0] = 0
f[r_shift == 0] = 0.25

# %%
# ramp filter the sinogram in the radial direction
filtered_pre_corrected_sino = 1.0 * pre_corrected_sino

for i in range(num_theta):
    filtered_pre_corrected_sino[:, i] = xp.asarray(
        np.convolve(
            np.asarray(to_device(filtered_pre_corrected_sino[:, i], "cpu")),
            f,
            mode="same",
        ),
        device=dev,
    )

# %%
# define a projector and back project the pre-corrected and filtered and pre-corrected sinogram

proj = parallelproj.ParallelViewProjector2D(
    (num_rad, num_rad),
    r,
    -theta,
    2 * float(xp.max(r)),
    (float(xp.min(r)), float(xp.min(r))),
    (float(r[1] - r[0]), float(r[1] - r[0])),
)

# %%
# perform a back projection and filtered back projection
# back_proj = proj.adjoint(pre_corrected_sino)
# filtered_back_proj = proj.adjoint(filtered_pre_corrected_sino)

back_proj = proj.adjoint(pre_corrected_sino)
filtered_back_proj = proj.adjoint(filtered_pre_corrected_sino)

# %%

fig, ax = plt.subplots(2, 1, figsize=(3, 6), tight_layout=True)
ax[0].imshow(
    pre_corrected_sino.T,
    cmap="Greys",
    extent=[r.min(), r.max(), 180 * theta.min() / np.pi, 180 * theta.max() / np.pi],
    origin="lower",
    aspect=2 * r.max() / (180 * theta.max() / np.pi),
)
ax[1].imshow(
    filtered_back_proj.T,
    cmap="Greys",
    extent=[r.min(), r.max(), r.min(), r.max()],
    origin="lower",
)

# ax[0].set_xlabel(r"$s$")
# ax[0].set_ylabel(r"$\theta$")
# ax[1].set_xlabel(r"$x$")
# ax[1].set_ylabel(r"$y$")

fig.savefig(f"../figs/fbp_counts_{counts:.2E}.png")
fig.show()
