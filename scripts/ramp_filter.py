import numpy as np
import matplotlib.pyplot as plt

n = 15
s = np.linspace(-n, n, 1001)
nu_max = 1 / 2

rf = nu_max * np.sin(2 * np.pi * nu_max * s) / (np.pi * s) - np.sin(
    nu_max * np.pi * s
) ** 2 / (np.pi**2 * s**2)
rf[np.isnan(rf)] = nu_max**2

s2 = np.arange(-n, n + 1)
rf2 = nu_max * np.sin(2 * np.pi * nu_max * s2) / (np.pi * s2) - np.sin(
    nu_max * np.pi * s2
) ** 2 / (np.pi**2 * s2**2)
rf2[np.isnan(rf2)] = nu_max**2

nu = np.linspace(-1.1 * nu_max, 1.1 * nu_max, 1001)
rf_ft = np.zeros(nu.size)
inds = np.where(np.abs(nu) <= nu_max)
rf_ft[inds] = np.abs(nu[inds])

# %%

fig, ax = plt.subplots(1, 2, figsize=(6, 3), tight_layout=True)
ax[0].plot(s, rf)
ax[0].plot(s2, rf2, "rx")
ax[0].set_xlabel(r"$s$")
ax[0].set_ylabel(r"$h(s)$")
ax[0].grid(ls=":")

ax[1].plot(nu, rf_ft)
ax[1].set_aspect("equal")
ax[1].grid(ls=":")
ax[1].set_xlabel(r"$\nu$")
ax[1].set_ylabel(r"$\hat{h}(\nu)$")

fig.show()
fig.savefig("../figs/ramp_filter.png")
