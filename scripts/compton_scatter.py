# script to visualize Klein-Nishina formula for Compton scattering

import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import quad


def P(theta, E):
    return 1 / (1 + E / 511 * (1 - np.cos(theta)))


def diff_cs(theta, E):
    pp = P(theta, E)
    # 1 barn = 100 fm^2
    re = 2.82  # classical electron radius in fm
    return 0.5 * (re**2) * pp**2 * (pp + 1 / pp - np.sin(theta) ** 2)


def cs(theta, E, dtheta):
    res = np.zeros_like(theta)
    f = lambda x: diff_cs(x, E) * np.sin(x)
    for i, t in enumerate(theta):
        res[i] = 2 * np.pi * quad(f, t - 0.5 * dtheta, t + 0.5 * dtheta)[0]

    return res


theta = np.linspace(0.001 * np.pi, 0.999 * np.pi, 200)
cs140 = cs(theta, 140, np.pi / 1000)
cs511 = cs(theta, 511, np.pi / 1000)

fig, ax = plt.subplots(tight_layout=True)
ax.plot(theta * 180 / np.pi, cs140, label=r"$E_\gamma = 140$ keV")
ax.plot(theta * 180 / np.pi, cs511, label=r"$E_\gamma = 511$ keV")
ax.grid(ls=":")
ax.set_xlabel(r"$\theta$ ($^\circ$)")
ax.set_ylabel(r"$\sigma(E_\gamma, \theta, \Delta\theta = 0.001 \cdot \pi)$")
ax.legend()
fig.savefig("../figs/compton_scatter.png", dpi=300)
fig.show()

fig2, ax2 = plt.subplots(tight_layout=True)
ax2.plot(theta * 180 / np.pi, P(theta, 140), label=r"$E_\gamma = 140$ keV")
ax2.plot(theta * 180 / np.pi, P(theta, 511), label=r"$E_\gamma = 511$ keV")
ax2.grid(ls=":")
ax2.legend()
ax2.set_xlabel(r"$\theta$ ($^\circ$)")
ax2.set_ylabel(r"$E_\gamma' \, / \, E_\gamma$")
fig2.savefig("../figs/compton_scatter_energy.png", dpi=300)
fig2.show()
