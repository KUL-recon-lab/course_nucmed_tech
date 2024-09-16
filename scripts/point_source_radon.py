# script to visualize the radon transform of a point source

import numpy as np
import matplotlib.pyplot as plt

x0s = [0, 1, 0, -0.4]
y0s = [0, 0, -1, 0.4]

fig, ax = plt.subplots(2, 1, figsize=(4, 8), tight_layout=True)

theta = np.linspace(0, 180.0, 200)
theta_rad = np.deg2rad(theta)

for x0, y0 in zip(x0s, y0s):
    ax[0].plot([x0], [y0], "o")

    s = x0 * np.cos(theta_rad) + y0 * np.sin(theta_rad)

    ax[1].plot(s, theta)

ax[0].set_xlim(-1.1, 1.1)
ax[0].set_ylim(-1.1, 1.1)
ax[1].set_ylim(0, 180)

ax[0].set_aspect("equal")

ax[0].set_xlabel(r"$x$")
ax[0].set_ylabel(r"$y$")

ax[1].set_xlabel(r"$s$")
ax[1].set_ylabel(r"$\theta\,[^\circ]$")

ax[0].grid(ls=":")
ax[1].grid(ls=":")

fig.savefig("../figs/point_source_radon.png")
fig.show()
