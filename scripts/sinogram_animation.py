from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import matplotlib.transforms as mtransforms

from utils import demo_radon_object

# %%
# define an object with known radon transform
radon_object = demo_radon_object()

# %%
# setup r and theta coordinates
r = np.linspace(-30.0, 30.0, 151)
num_theta = int(0.5 * r.shape[0] * np.pi) + 1
theta = np.linspace(0, 1 * np.pi, num_theta, endpoint=False)
THETA, R = np.meshgrid(theta, r, indexing="ij")
x = np.linspace(r.min(), r.max(), 351)
X0, X1 = np.meshgrid(r, r, indexing="ij")
X0hr, X1hr = np.meshgrid(x, x, indexing="ij")

# %%
# analytic calculation of the randon transform
sino = radon_object.radon_transform(R, THETA)


# %%
def _update_animation(i):
    p1.set_ydata(sino[i, :])
    ax1.set_title(
        f"$p_\\theta (s)$ $\\theta =$ {180*theta[i]/np.pi:.1f}$^\\circ$",
    )
    t = mtransforms.Affine2D().rotate_around(0, 0, theta[i])
    for ar in arr:
        ar.set_transform(t + ax0.transData)
    for k, s in enumerate(ss):
        d0 = s * np.cos(theta[i])
        d1 = s * np.sin(theta[i])
        ann[k].set_position(
            (1.2 * R * np.sin(theta[i]) + d0, -1.2 * R * np.cos(theta[i]) + d1)
        )
        ann[k].xy = (1.2 * R * np.sin(theta[i]) + d0, -1.2 * R * np.cos(theta[i]) + d1)

    tmp_sino = sino.copy()
    tmp_sino[(i + 1) :] = 0
    img2.set_data(tmp_sino)

    return (p1, arr, ann)


# %%
# animated random transform and sinogram

fig2 = plt.figure(tight_layout=True, figsize=(12, 4))
gs = gridspec.GridSpec(1, 3)

ax0 = fig2.add_subplot(gs[:, 0])
ax1 = fig2.add_subplot(gs[:, 1])
ax2 = fig2.add_subplot(gs[:, 2])

img0 = ax0.imshow(
    radon_object.values(X0hr, X1hr).T,
    cmap="Greys",
    extent=[r.min(), r.max(), r.min(), r.max()],
    origin="lower",
    aspect=1.0,
)
fig2.colorbar(img0, ax=ax0, location="bottom", fraction=0.03)

i = 0
R = 10.0

arr = []
ann = []

ss = np.linspace(-21.0, 21.0, 7)

p1 = ax1.plot(r, sino[i, :], color="k")[0]
ax1.set_ylim(sino.min(), sino.max())
ax1.grid(ls=":")

for s in ss:
    ax1.axvline(s, color="r", lw=0.5)
    ax2.axvline(s, color="r", lw=0.5)
    d0 = s * np.cos(theta[i])
    d1 = s * np.sin(theta[i])
    arr.append(
        ax0.arrow(
            R * np.sin(theta[i]) + d0,
            -R * np.cos(theta[i]) + d1,
            -2 * R * np.sin(theta[i]),
            2 * R * np.cos(theta[i]),
            color="r",
            width=0.01,
            head_width=1.0,
        )
    )
    ann.append(
        ax0.annotate(
            f"{s:.1f}",
            (1.2 * R * np.sin(theta[i]) + d0, -1.2 * R * np.cos(theta[i]) + d1),
            color="r",
            fontsize="small",
            ha="center",
            va="center",
            annotation_clip=True,
        )
    )

tmp_sino = sino.copy()
tmp_sino[(i + 1) :] = 0

img2 = ax2.imshow(
    tmp_sino,
    cmap="Greys",
    extent=[r.min(), r.max(), 180 * theta.min() / np.pi, 180 * theta.max() / np.pi],
    vmin=0,
    vmax=sino.max(),
    aspect=2 * r.max() / (180 * theta.max() / np.pi),
    origin="lower",
)

fig2.colorbar(img2, ax=ax2, location="bottom", fraction=0.03)

ax0.set_xlabel(r"$x$")
ax0.set_ylabel(r"$y$")
ax0.set_title(r"f(x,y)")
ax1.set_xlabel(r"$s$")
ax2.set_xlabel(r"$s$")
ax2.set_ylabel(r"$\theta$")

ax1.set_title(
    f"$p_\\theta (s)$ $\\theta =$ {180*theta[i]/np.pi:.1f}$^\\circ$",
)
ax2.set_title(
    r"$R[f(x,y)](s,\theta) = p(s,\theta)$",
)

# create animation
ani = animation.FuncAnimation(
    fig2, _update_animation, num_theta, interval=5, blit=False, repeat=False
)

# save animation to gif
ani.save("../figs/sinogram_animation.mp4", writer=animation.FFMpegWriter(fps=20))

fig2.show()
