import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_I = pd.read_csv("iodine_att.csv", skiprows=1)  # cm^2/g
rho_I = 4.93  # g/cm^3

df_H2O = pd.read_csv("water_att.csv", skiprows=1)  # cm^2/g
rho_H2O = 1.0  # g/cm^3

fig, ax = plt.subplots(1, 2, figsize=(8, 4), tight_layout=True)
ax[0].plot(df_I["E"] * 1000, df_I["mu_tot"] * rho_I, label=r"$I$, $\mu_{tot}$")
ax[0].plot(df_H2O["E"] * 1000, df_H2O["mu_tot"] * rho_H2O, label=r"$H_2O$, $\mu_{tot}$")
ax[1].semilogy(df_I["E"] * 1000, df_I["mu_tot"] * rho_I, label=r"$I$, $\mu_{tot}$")
ax[1].semilogy(
    df_H2O["E"] * 1000, df_H2O["mu_tot"] * rho_H2O, label=r"$H_2O$, $\mu_{tot}$"
)

for axx in ax.ravel():
    axx.set_xlim(100, 600)
    axx.set_ylim(0.07, 5)
    axx.set_xlabel(r"$E_\gamma$ (keV)")
    axx.set_ylabel(r"$\mu$ ($cm^{-1}$)")
    axx.grid(ls=":")
    axx.axvline(140, color="k", ls="--")
    axx.axvline(511, color="k", ls="--")
    axx.legend(ncols=2)

ax[0].set_title("linear scale", fontsize="medium")
ax[1].set_title("log scale", fontsize="medium")

fig.savefig("../figs/lac1.png", dpi=300)
fig.show()

# %%

fig2, ax2 = plt.subplots(1, 2, figsize=(8, 4), tight_layout=True)
ax2[0].plot(df_I["E"] * 1000, df_I["mu_tot"] * rho_I, label=r"$I$, $\mu_{tot}$")
ax2[0].plot(
    df_I["E"] * 1000,
    df_I["pe"] * rho_I,
    label=r"$I$, $\mu_{p.e.}$",
    color=plt.cm.tab10(0),
    ls="--",
)
ax2[0].plot(
    df_I["E"] * 1000,
    df_I["incoh_scat"] * rho_I,
    label=r"$I$, $\mu_{c.s.}$",
    color=plt.cm.tab10(0),
    ls=":",
)

ax2[0].plot(
    df_H2O["E"] * 1000, df_H2O["mu_tot"] * rho_H2O, label=r"$H_2O$, $\mu_{tot}$"
)
ax2[0].plot(
    df_H2O["E"] * 1000,
    df_H2O["pe"] * rho_H2O,
    label=r"$H_2O$, $\mu_{p.e.}$",
    color=plt.cm.tab10(1),
    ls="--",
)
ax2[0].plot(
    df_H2O["E"] * 1000,
    df_H2O["incoh_scat"] * rho_H2O,
    label=r"$H_2O$, $\mu_{c.s.}$",
    color=plt.cm.tab10(1),
    ls=":",
)

ax2[1].semilogy(df_I["E"] * 1000, df_I["mu_tot"] * rho_I, label=r"$I$, $\mu_{tot}$")
ax2[1].semilogy(
    df_I["E"] * 1000,
    df_I["pe"] * rho_I,
    label=r"$I$, $\mu_{p.e.}$",
    color=plt.cm.tab10(0),
    ls="--",
)
ax2[1].semilogy(
    df_I["E"] * 1000,
    df_I["incoh_scat"] * rho_I,
    label=r"$I$, $\mu_{c.s.}$",
    color=plt.cm.tab10(0),
    ls=":",
)
ax2[1].semilogy(
    df_H2O["E"] * 1000, df_H2O["mu_tot"] * rho_H2O, label=r"$H_2O$, $\mu_{tot}$"
)

ax2[1].semilogy(
    df_H2O["E"] * 1000,
    df_H2O["pe"] * rho_H2O,
    label=r"$H_2O$, $\mu_{p.e.}$",
    color=plt.cm.tab10(1),
    ls="--",
)
ax2[1].semilogy(
    df_H2O["E"] * 1000,
    df_H2O["incoh_scat"] * rho_H2O,
    label=r"$H_2O$, $\mu_{c.s.}$",
    color=plt.cm.tab10(1),
    ls=":",
)
for axx in ax2.ravel():
    axx.set_xlim(100, 600)
    axx.set_ylim(0.07, 5)
    axx.set_xlabel(r"$E_\gamma$ (keV)")
    axx.set_ylabel(r"$\mu$ ($cm^{-1}$)")
    axx.grid(ls=":")
    axx.axvline(140, color="k", ls="--")
    axx.axvline(511, color="k", ls="--")
    axx.legend(ncols=2)

ax2[0].set_title("linear scale", fontsize="medium")
ax2[1].set_title("log scale", fontsize="medium")

fig2.savefig("../figs/lac2.png", dpi=300)
fig2.show()
