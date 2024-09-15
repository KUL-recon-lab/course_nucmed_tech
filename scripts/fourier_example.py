import abc
import numpy as np
import matplotlib.pyplot as plt


class FourierFunction(abc.ABC):
    def __init__(self):
        self._a = 1.0
        self._amp = 1.0

    @abc.abstractmethod
    def _value(self, x: np.ndarray) -> np.ndarray:
        pass

    @abc.abstractmethod
    def _fourier_transform(self, nu: np.ndarray) -> np.ndarray:
        pass

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def amp(self) -> float:
        return self._amp

    @amp.setter
    def amp(self, value):
        self._amp = value

    def __call__(self, x):
        return self._amp * self._value(self._a * x)

    def fourier_transform(self, nu):
        return self._amp * (1 / np.abs(self._a)) * self._fourier_transform(nu / self._a)


class Rectangular(FourierFunction):
    def _value(self, x):
        return np.where(np.abs(x) < 0.5, 1, 0)

    def _fourier_transform(self, nu):
        return np.sinc(nu)


class Gaussian(FourierFunction):
    def _value(self, x):
        return np.exp(-(x**2))

    def _fourier_transform(self, nu):
        return np.sqrt(np.pi) * np.exp(-np.pi**2 * nu**2)


# %%

n = 1001

f = Rectangular()
f.a = 1.0
f.amp = 1.0

f2 = Rectangular()
f2.a = 5
f2.amp = 5

x = np.linspace(-1, 1, n)
nu = np.linspace(-30, 30, n)

fig, ax = plt.subplots(1, 2, figsize=(8, 3), tight_layout=True)
ax[0].plot(x, f(x), label="rect(x)")
ax[0].plot(x, f2(x), "--", label=f"{f2.amp}rect({f2.a}x)")
ax[1].plot(nu, f.fourier_transform(nu))
ax[1].plot(nu, f2.fourier_transform(nu), "--")

ax[0].set_xlabel("x")
ax[0].set_ylabel("f(x)")
ax[1].set_xlabel(r"$\nu$")
ax[1].set_ylabel(r"$\hat{f}(\nu)$")

ax[0].legend()

ax[0].grid(ls=":")
ax[1].grid(ls=":")

fig.show()
fig.savefig("../figs/fourier_rect.png")


# %%

f = Gaussian()
f.a = 1.0
f.amp = 1.0

f2 = Gaussian()
f2.a = 5
f2.amp = 5

x = np.linspace(-2, 2, n)
nu = np.linspace(-5, 5, n)

fig, ax = plt.subplots(1, 2, figsize=(8, 3), tight_layout=True)
ax[0].plot(x, f(x), label="exp(-x**2)")
ax[0].plot(x, f2(x), "--", label=f"{f2.amp}exp(-({f2.a}x)**2)")
ax[1].plot(nu, f.fourier_transform(nu))
ax[1].plot(nu, f2.fourier_transform(nu), "--")

ax[0].set_xlabel("x")
ax[0].set_ylabel("f(x)")
ax[1].set_xlabel(r"$\nu$")
ax[1].set_ylabel(r"$\hat{f}(\nu)$")

ax[0].legend()

ax[0].grid(ls=":")
ax[1].grid(ls=":")

fig.show()
fig.savefig("../figs/fourier_gauss.png")
