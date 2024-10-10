import numpy as np
import matplotlib.pyplot as plt

gamma = 2.0
eps = 1e-3
delta = 1e-2


fig, ax = plt.subplots(2, 1, figsize=(4, 8), tight_layout=True)

for i, xj in enumerate([1.0, 5.0]):

    xk = np.linspace(xj - 1, xj + 1, 1000)

    phi1 = (xj - xk) ** 2
    phi2 = 3 * (xj - xk) ** 2 / ((xj + xk) + gamma * np.abs(xj - xk) + eps)
    phi3 = np.abs(xj - xk)
    phi4 = delta * np.log(np.cosh((xj - xk) / delta))

    ax[i].plot(xk, phi1, label=r"$(x_j - x_k)^2$")
    ax[i].plot(
        xk, phi2, label=r"$\frac{3(x_j - x_k)^2}{(x_j + x_k) + 2|x_j - x_k|}$", ls="--"
    )
    ax[i].plot(xk, phi3, label=r"$|x_j - x_k|$")
    ax[i].plot(xk, phi4, label=r"$\delta \, \log(\cosh((x_j - x_k)/\delta))$", ls=":")
    ax[i].grid(ls=":")
    ax[i].set_xlabel(r"$x_k$")
    ax[i].set_ylabel(f"$\\phi(x_j={xj}, x_k)$")

ax[0].legend()
fig.savefig("../figs/penalty_fcts.png", dpi=300)
fig.show()
