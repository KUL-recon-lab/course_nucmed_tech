"""script showing different estimator of activity detection for a source in front of 2 detectors"""

import numpy as np
import matplotlib.pyplot as plt

A = 50  # activity of the source in Bq
T = 25  # measurement time in seconds
n = 4000000  # number of repeated measurements

# efficiencies of the two detectors
eps1 = 1 / 10
eps2 = 1 / 50

# expected counts in the two detectors
exp1 = A * T * eps1
exp2 = A * T * eps2

# number of counts in the two detectors
x = np.random.poisson(exp1, n)
y = np.random.poisson(exp2, n)

# 1st estimator: taking results of first detector only
A1 = x / (eps1 * T)
# 2nd estimator: taking results of second detector only
A2 = y / (eps2 * T)
# 3rd estimator: taking average of A1 and A2
A_avg = (A1 + A2) / 2
# 4th estimator: Poisson ML solution
A_poiss = (x + y) / ((eps1 + eps2) * T)
# 5th estimator: unweighted LS estimator
A_lsq = (eps1 * x + eps2 * y) / ((eps1**2 + eps2**2) * T)

# %% plot histograms of the estimators

fig, ax = plt.subplots(1, 1, figsize=(14, 5), tight_layout=True)
ax.boxplot(
    [A1, A2, A_avg, A_poiss, A_lsq],
    showmeans=True,
    patch_artist=True,
    boxprops=dict(facecolor="lightgray"),
    flierprops=dict(marker="x", markersize=1),
    meanprops=dict(marker="o", markersize=5),
    tick_labels=[
        f"$A_1$, $\\mu$ = {A1.mean():.2f} Bq, $\\sigma$ = {A1.std():.2f} Bq",
        f"$A_2$, $\\mu$ = {A2.mean():.2f} Bq, $\\sigma$ = {A2.std():.2f} Bq",
        f"$A_{{avg}}$, $\\mu$ = {A_avg.mean():.2f} Bq, $\\sigma$ = {A_avg.std():.2f} Bq",
        f"$A_{{ML,Poisson}}$, $\\mu$ = {A_poiss.mean():.2f} Bq, $\\sigma$ = {A_poiss.std():.2f} Bq",
        f"$A_{{lsq}}$, $\\mu$ = {A_lsq.mean():.2f} Bq, $\\sigma$ = {A_lsq.std():.2f} Bq",
    ],
)
ax.grid(ls=":")
ax.set_title(
    f"$A_{{true}}$ = {A} Bq, $T$ = {T} s, $\\epsilon_1$ = {eps1}, $\\epsilon_2$ = {eps2}, {n:.1E} measurements"
)
fig.savefig("../figs/two_dect_act_estimate.png", dpi=300)
fig.show()
