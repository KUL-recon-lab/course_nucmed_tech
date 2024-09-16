# script to visualize the radon transform of a point source

import numpy as np
import matplotlib.pyplot as plt

x0 = 0
y0 = 0

theta = np.linspace(0, 180.0, 100)
theta_rad = np.deg2rad(theta)

x = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, x, indexing="ij")
R = np.sqrt((X - x0) ** 2 + (Y - y0) ** 2)

fwd_back = 1 / R

fig, ax = plt.subplots(2, 2, figsize=(6, 6), tight_layout=True)

ax[0, 1].plot([x0], [y0], "k.")
s = x0 * np.cos(theta_rad) + y0 * np.sin(theta_rad)
ax[1, 0].plot(s, theta, "k")
ax[1, 1].imshow(np.log(fwd_back), extent=(-1, 1, -1, 1), origin="lower", cmap="Greys")

ax[0, 1].set_xlim(-1.1, 1.1)
ax[0, 1].set_ylim(-1.1, 1.1)
ax[1, 1].set_xlim(-1.1, 1.1)
ax[1, 1].set_ylim(-1.1, 1.1)

ax[1, 0].set_ylim(0, 180)
ax[1, 0].set_xlim(-1.1, 1.1)

ax[0, 1].set_aspect("equal")

ax[0, 1].set_xlabel(r"$x$")
ax[0, 1].set_ylabel(r"$y$")
ax[1, 1].set_xlabel(r"$x$")
ax[1, 1].set_ylabel(r"$y$")

ax[1, 0].set_xlabel(r"$s$")
ax[1, 0].set_ylabel(r"$\theta\,[^\circ]$")
ax[1, 0].grid(ls=":")

ax[0, 1].set_title(r"$f(x,y) = \delta(x) \delta(y)$")
ax[1, 0].set_title(r"$R[\delta(x) \delta(y)]$")
ax[1, 1].set_title(r"$R^H[R[\delta(x) \delta(y)]]$")

ax[0, 0].set_axis_off()

fig.savefig("../figs/fwd_back.png")
fig.show()
