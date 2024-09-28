# script to plot binomial distribution for radioactive decay example

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

plot_poisson = False

# initial number of nuclei
N0 = 16

# half life in minutes
T12 = 109

# array for possible outcomes 0, 1, 2, ..., N0
n = np.arange(0, N0 + 1)

# create figure
fig, ax = plt.subplots(tight_layout=True, figsize=(6, 4))

# measured time in minutes
T_fracs = np.array([0.1])
ps = 1 - 0.5 ** (T_fracs)

for i, T_frac in enumerate(T_fracs):
    P = binom.pmf(n, N0, ps[i])
    ax.plot(
        n,
        P,
        "o",
        label=f"binomial, $T = {T_frac:.1f} T_{{1/2}}, \\ p = {ps[i]:.2f}, \\ N_0 = {N0}$",
    )

if plot_poisson:
    for i, T_frac in enumerate(T_fracs):
        P2 = poisson.pmf(n, N0 * ps[i])
        ax.plot(
            n,
            P2,
            "x",
            label=f"Poisson, $\\lambda = {N0}*{ps[i]:0.2f} =  {N0*ps[i]:.1f}$",
        )

ax.set_xlabel(r"$n$")
ax.set_ylabel(r"$P(n)$")
ax.grid(ls=":")
ax.legend()
fig.savefig(f"../figs/binom_decay_poisson_{plot_poisson}.png", dpi=300)
fig.show()
