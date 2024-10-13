"""script for plotting radon brute force inversion"""

from __future__ import annotations

import array_api_compat.numpy as np
import matplotlib.pyplot as plt
import parallelproj

from utils import demo_radon_object

np.random.seed(0)
dev = "cpu"

# %%
# define an object with known radon transform
true_object = demo_radon_object(id=1, amp=1.0)

# %%
# setup r and theta coordinates
num_rad = 201
r = np.linspace(-30.0, 30.0, num_rad)
num_theta = int(0.2 * r.shape[0] * np.pi) + 1
theta = np.linspace(0, 1 * np.pi, num_theta, endpoint=False)
# THETA, R = np.meshgrid(theta, r, indexing="ij")
x = np.linspace(r.min(), r.max(), 351)
X0, X1 = np.meshgrid(r, r, indexing="ij")

# %%
# define a projector and back project the pre-corrected and filtered and pre-corrected sinogram

proj = parallelproj.ParallelViewProjector2D(
    (num_rad, num_rad),
    r,
    -theta,
    2 * float(np.max(r)),
    (float(np.min(r)), float(np.min(r))),
    (float(r[1] - r[0]), float(r[1] - r[0])),
)
# %%
# analytic calculation of the randon transform
sino = proj(true_object.values(X0, X1))
emis_sino = np.random.poisson(sino)

test_objects = [
    demo_radon_object(id=3, amp=1.0),
    demo_radon_object(id=2, amp=2.0),
    demo_radon_object(id=1, amp=0.5),
    true_object,
]

# do a quick MLEM of the emis-sino

x_mlem = np.ones((num_rad, num_rad), dtype=np.float32)
sens_img = proj.adjoint(np.ones_like(emis_sino))

print("running MLEM")
num_iter = 20
for i in range(20):
    print(f"{(i+1):03}/{num_iter:03}", end="\r")
    exp = proj(x_mlem)
    exp2 = np.clip(exp, 1e-6, None)
    ratio = (emis_sino - exp) / exp2
    step = x_mlem / sens_img
    x_mlem += step * proj.adjoint(ratio)
print("")

test_objects.append(x_mlem)

# %%
num_cols = len(test_objects) + 1
fig, ax = plt.subplots(3, num_cols, figsize=(num_cols * 2, 3 * 2.5), tight_layout=True)

for i, test_object in enumerate(test_objects):

    if i < len(test_objects) - 1:
        test_img = test_object.values(X0, X1)
    else:
        test_img = test_object
    test_sino = proj(test_img)

    img0 = ax[0, i].imshow(
        test_img.T,
        cmap="Greys",
        extent=[r.min(), r.max(), r.min(), r.max()],
        origin="lower",
        aspect=1.0,
        vmin=0,
        vmax=2,
    )
    img1 = ax[1, i].imshow(
        test_sino.T,
        cmap="Greys",
        extent=[r.min(), r.max(), 180 * theta.min() / np.pi, 180 * theta.max() / np.pi],
        vmin=0,
        vmax=sino.max(),
        aspect=2 * r.max() / (180 * theta.max() / np.pi),
        origin="lower",
    )
    img2 = ax[2, i].imshow(
        (test_sino - emis_sino).T,
        cmap="seismic",
        extent=[r.min(), r.max(), 180 * theta.min() / np.pi, 180 * theta.max() / np.pi],
        vmin=-sino.max(),
        vmax=sino.max(),
        aspect=2 * r.max() / (180 * theta.max() / np.pi),
        origin="lower",
    )

    sino_mae = np.mean(np.abs(test_sino - emis_sino))

    fig.colorbar(img0, ax=ax[0, i], location="bottom", fraction=0.03)
    fig.colorbar(img1, ax=ax[1, i], location="bottom", fraction=0.03)
    fig.colorbar(img2, ax=ax[2, i], location="bottom", fraction=0.03)

    ax[0, i].set_title(f"Test image {i}", fontsize="small")
    ax[1, i].set_title(f"R[Test image {i}]", fontsize="small")
    ax[2, i].set_title(f"R[Test image {i}] - y, MAE = {sino_mae:.1f}", fontsize="small")

img2 = ax[-1, -1].imshow(
    emis_sino.T,
    cmap="Greys",
    extent=[r.min(), r.max(), 180 * theta.min() / np.pi, 180 * theta.max() / np.pi],
    vmin=0,
    vmax=sino.max(),
    aspect=2 * r.max() / (180 * theta.max() / np.pi),
    origin="lower",
)
fig.colorbar(img2, ax=ax[-1, -1], location="bottom", fraction=0.03)


ax[-1, -1].set_title(f"measured sinogram y", fontsize="small")

for axx in ax.ravel():
    axx.set_xticks([])
    axx.set_yticks([])

for axx in ax[:-1, -1]:
    axx.set_axis_off()

fig.savefig("../figs/brute_force_radon_inversion.png", dpi=300)
fig.show()
