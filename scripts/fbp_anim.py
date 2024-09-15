from __future__ import annotations

import array_api_compat.numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import parallelproj

from array_api_compat import to_device
from utils import RadonDisk, RadonObjectSequence

# %%
import numpy as xp

dev = "cpu"

# %%
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
pre_corrected_sino = radon_object.radon_transform(R, THETA)

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

back_projs = np.zeros((num_theta, num_rad, num_rad), device=dev, dtype=xp.float32)
filtered_back_projs = np.zeros(
    (num_theta, num_rad, num_rad), device=dev, dtype=xp.float32
)

for i in range(num_theta):
    tmp = np.zeros_like(pre_corrected_sino)
    tmp[:, i] = pre_corrected_sino[:, i]

    tmp2 = np.zeros_like(filtered_pre_corrected_sino)
    tmp2[:, i] = filtered_pre_corrected_sino[:, i]

    back_projs[i] = proj.adjoint(tmp)
    filtered_back_projs[i] = proj.adjoint(tmp2)

back_proj = back_projs.mean(axis=0)
filtered_back_proj = filtered_back_projs.mean(axis=0)


# %%
def _update_animation(i):
    p1.set_ydata(pre_corrected_sino[:, i])
    p2.set_ydata(np.convolve(pre_corrected_sino[:, i], f, mode="same"))

    img3.set_data(back_projs[i, ...].T)
    img4.set_data(filtered_back_projs[i, ...].T)
    img5.set_data(back_projs[: (i + 1), ...].mean(axis=0).T)
    img6.set_data(filtered_back_projs[: (i + 1), ...].mean(axis=0).T)

    yl = 180 * theta[i] / np.pi
    l0.set_ydata([yl, yl])

    ax1.set_title(
        f"$p_\\theta(s)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
        fontsize="medium",
    )
    ax2.set_title(
        f"$q_\\theta(s) =$ ramp filtered $p_\\theta(s)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
        fontsize="medium",
    )
    ax3.set_title(
        f"$p(\\cos(\\theta)x + \\sin(\\theta) y, \\theta)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
        fontsize="medium",
    )

    ax4.set_title(
        f"$q(\\cos(\\theta)x + \\sin(\\theta) y, \\theta)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
        fontsize="medium",
    )

    ax5.set_title(
        f"$\\int_0^\\theta d\\theta^\\prime \\, p(\\cos(\\theta^\\prime)x + \\sin(\\theta^\\prime) y, \\theta^\\prime)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
        fontsize="medium",
    )

    ax6.set_title(
        f"$\\int_0^\\theta d\\theta^\\prime \\, q(\\cos(\\theta^\\prime)x + \\sin(\\theta^\\prime) y, \\theta^\\prime)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
        fontsize="medium",
    )

    return (p1, p2, img3, img4, img5, img6, l0)


# %%
# animated random transform and sinogram

fig2 = plt.figure(tight_layout=True, figsize=(12, 8))
gs = gridspec.GridSpec(4, 6)

ax0 = fig2.add_subplot(gs[:2, :2])
ax1 = fig2.add_subplot(gs[2, :2])
ax2 = fig2.add_subplot(gs[3, :2])
ax3 = fig2.add_subplot(gs[:2, 2:4])
ax4 = fig2.add_subplot(gs[:2, 4:6])
ax5 = fig2.add_subplot(gs[2:4, 2:4])
ax6 = fig2.add_subplot(gs[2:4, 4:6])

i = 0

ax0.imshow(
    pre_corrected_sino.T,
    cmap="Greys",
    extent=[r.min(), r.max(), 180 * theta.min() / np.pi, 180 * theta.max() / np.pi],
    origin="lower",
    aspect=2 * r.max() / (180 * theta.max() / np.pi),
)

l0 = ax0.axhline(180 * theta[i] / np.pi, color="r", lw=0.5)

p1 = ax1.plot(r, pre_corrected_sino[:, i], color="k")[0]
ax1.set_ylim(pre_corrected_sino.min(), pre_corrected_sino.max())
ax1.grid(ls=":")

p2 = ax2.plot(r, np.convolve(pre_corrected_sino[:, i], f, mode="same"), color="k")[0]
ax2.set_ylim(2 * filtered_back_projs.min(), 2 * filtered_back_projs.max())
ax2.grid(ls=":")


img3 = ax3.imshow(
    back_projs[i, ...].T,
    cmap="Greys",
    extent=[r.min(), r.max(), r.min(), r.max()],
    vmin=0,
    vmax=back_projs.max(),
    origin="lower",
)
img4 = ax4.imshow(
    filtered_back_projs[i, ...].T,
    cmap="Greys",
    extent=[r.min(), r.max(), r.min(), r.max()],
    vmin=filtered_back_projs.min(),
    vmax=filtered_back_projs.max(),
    origin="lower",
)
img5 = ax5.imshow(
    back_projs[: (i + 1), ...].mean(axis=0).T,
    cmap="Greys",
    extent=[r.min(), r.max(), r.min(), r.max()],
    origin="lower",
    vmin=back_proj.min(),
    vmax=1.05 * back_proj.max(),
)
img6 = ax6.imshow(
    filtered_back_projs[: (i + 1), ...].mean(axis=0).T,
    cmap="Greys",
    extent=[r.min(), r.max(), r.min(), r.max()],
    origin="lower",
    vmin=filtered_back_proj.min(),
    vmax=1.05 * filtered_back_proj.max(),
)

ax0.set_xlabel(r"$s$")
ax0.set_ylabel(r"$\theta$ [$^\circ$]")
ax0.set_title(r"$p(s,\theta)$", fontsize="medium")
ax1.set_xlabel(r"$s$")
ax2.set_xlabel(r"$s$")
ax3.set_xlabel(r"$x$")
ax3.set_ylabel(r"$y$")
ax4.set_xlabel(r"$x$")
ax4.set_ylabel(r"$y$")
ax5.set_xlabel(r"$x$")
ax5.set_ylabel(r"$y$")
ax6.set_xlabel(r"$x$")
ax6.set_ylabel(r"$y$")

ax1.set_title(
    f"$p_\\theta(s)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
    fontsize="medium",
)
ax2.set_title(
    f"$q_\\theta(s) =$ ramp filtered $p_\\theta(s)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
    fontsize="medium",
)
ax3.set_title(
    f"$p(\\cos(\\theta)x + \\sin(\\theta) y, \\theta)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
    fontsize="medium",
)

ax4.set_title(
    f"$q(\\cos(\\theta)x + \\sin(\\theta) y, \\theta)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
    fontsize="medium",
)

ax5.set_title(
    f"$\\int_0^\\theta d\\theta^\\prime \\, p(\\cos(\\theta^\\prime)x + \\sin(\\theta^\\prime) y, \\theta^\\prime)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
    fontsize="medium",
)

ax6.set_title(
    f"$\\int_0^\\theta d\\theta^\\prime \\, q(\\cos(\\theta^\\prime)x + \\sin(\\theta^\\prime) y, \\theta^\\prime)$ - $\\theta$ = {180*theta[i]/np.pi:.1f}$^\\circ$",
    fontsize="medium",
)

# create animation
ani = animation.FuncAnimation(
    fig2, _update_animation, num_theta, interval=5, blit=False, repeat=False
)

# save animation to gif
ani.save("fbp_animation.mp4", writer=animation.FFMpegWriter(fps=20))

fig2.show()
