import array_api_compat.numpy as np
import parallelproj
from parallelproj import Array

import abc
from collections.abc import Sequence
from parallelproj import Array

from types import ModuleType
from array_api_compat import get_namespace, device

from scipy.ndimage import gaussian_filter


class DiscreteRadonTransform(parallelproj.LinearOperator):
    def __init__(self):

        smax = 30.0
        num_s = 201
        theta_max = np.pi
        num_theta = int(0.5 * num_s * np.pi * (theta_max / np.pi)) + 1

        s, ds = np.linspace(-smax, smax, num_s, dtype=np.float32, retstep=True)
        ds = float(ds)

        theta, dtheta = np.linspace(
            0,
            theta_max,
            num_theta,
            endpoint=False,
            dtype=np.float32,
            retstep=True,
        )
        dtheta = float(dtheta)

        self._smax = smax
        self._num_s = num_s

        self._theta_max = theta_max
        self._num_theta = num_theta

        self._s = s
        self._ds = ds

        self._theta = theta
        self._dtheta = dtheta

        self._proj = parallelproj.ParallelViewProjector2D(
            (self._num_s, self._num_s),
            self._s,
            -self._theta,
            2 * self._smax,
            (-self._smax, -self._smax),
            (self._ds, self._ds),
        )

        super().__init__()

    @property
    def in_shape(self) -> tuple[int, int]:
        return self._proj.in_shape

    @property
    def out_shape(self) -> tuple[int, int]:
        return self._proj.out_shape

    @property
    def s(self) -> np.ndarray:
        return self._s

    @property
    def theta(self) -> np.ndarray:
        return self._theta

    @property
    def dtheta(self) -> float:
        return self._dtheta

    @property
    def pixel_size(self) -> tuple[float, float]:
        return (self._ds, self._ds)

    @property
    def sinogram_axis_labels(self):
        return (r"$s$ [mm]", r"$\theta$ [rad]")

    @property
    def sinogram_extent(self):
        return (-self._smax, self._smax, 0, self._theta_max)

    @property
    def image_axis_labels(self):
        return (r"$x$ [mm]", r"$y$ [mm]")

    @property
    def image_shape(self):
        return self.in_shape

    @property
    def image_extent(self):
        return (-self._smax, self._smax, -self._smax, self._smax)

    @property
    def sinogram_shape(self):
        return self.out_shape

    @property
    def pixel_x_coordinates(self):
        return self.s

    @property
    def pixel_y_coordinates(self):
        return self.s

    def _apply(self, x: np.ndarray) -> np.ndarray:
        return self._proj._apply(x)

    def _adjoint(self, y: np.ndarray) -> np.ndarray:
        return self._proj.adjoint(y)


class RadonObject(abc.ABC):
    """abstract base class for objects with known radon transform"""

    def __init__(self, xp: ModuleType, dev: str) -> None:
        self._xp = xp
        self._dev = dev

        self._x0_offset: float = 0.0
        self._x1_offset: float = 0.0
        self._s0: float = 1.0
        self._s1: float = 1.0
        self._amplitude: float = 1.0

    @abc.abstractmethod
    def _centered_radon_transform(self, r: Array, phi: Array) -> Array:
        pass

    @abc.abstractmethod
    def _centered_values(self, x0: Array, x1: Array) -> Array:
        pass

    @property
    def xp(self) -> ModuleType:
        return self._xp

    @property
    def dev(self) -> str:
        return self._dev

    @property
    def x0_offset(self) -> float:
        return self._x0_offset

    @x0_offset.setter
    def x0_offset(self, value: float) -> None:
        self._x0_offset = value

    @property
    def x1_offset(self) -> float:
        return self._x1_offset

    @x1_offset.setter
    def x1_offset(self, value: float) -> None:
        self._x1_offset = value

    @property
    def s0(self) -> float:
        return self._s0

    @s0.setter
    def s0(self, value: float) -> None:
        self._s0 = value

    @property
    def s1(self) -> float:
        return self._s1

    @s1.setter
    def s1(self, value: float) -> None:
        self._s1 = value

    @property
    def amplitude(self) -> float:
        return self._amplitude

    @amplitude.setter
    def amplitude(self, value: float) -> None:
        self._amplitude = value

    def radon_transform(self, s: Array, phi: Array) -> Array:
        s_prime = s / self.xp.sqrt(
            self._s0**2 * self.xp.cos(phi) ** 2 + self._s1**2 * self.xp.sin(phi) ** 2
        )
        phi_prime = self.xp.atan2(
            self._s0 * self.xp.sin(phi), self._s1 * self.xp.cos(phi)
        )

        fac = (
            self._s0
            * self._s1
            / self.xp.sqrt(
                self._s0**2 * self.xp.cos(phi) ** 2
                + self._s1**2 * self.xp.sin(phi) ** 2
            )
        )

        return (
            self._amplitude
            * fac
            * self._centered_radon_transform(
                s_prime
                - self._x0_offset * self.xp.cos(phi_prime)
                - self._x1_offset * self.xp.sin(phi_prime),
                phi_prime,
            )
        )

    def values(self, x0: Array, x1: Array) -> Array:
        return self._amplitude * self._centered_values(
            x0 / self._s0 - self._x0_offset, x1 / self._s1 - self._x1_offset
        )


class RadonObjectSequence(Sequence[RadonObject]):
    def __init__(self, objects: Sequence[RadonObject]) -> None:
        super().__init__()
        self._objects: Sequence[RadonObject] = objects

    def __len__(self) -> int:
        return len(self._objects)

    def __getitem__(self, i: int) -> RadonObject:
        return self._objects[i]

    def radon_transform(self, r, phi) -> float:
        return sum([x.radon_transform(r, phi) for x in self])

    def values(self, x0: Array, x1: Array) -> Array:
        return sum([x.values(x0, x1) for x in self])


class RadonDisk(RadonObject):
    """2D disk with known radon transform"""

    def __init__(self, xp: ModuleType, dev: str, radius: float) -> None:
        super().__init__(xp, dev)
        self._radius: float = radius

    def _centered_radon_transform(self, r: Array, phi: Array) -> Array:
        rt = self.xp.zeros_like(r)
        rt[self.xp.abs(r) <= self._radius] = 2 * self.xp.sqrt(
            self._radius**2 - r[self.xp.abs(r) <= self._radius] ** 2
        )

        return rt

    def _centered_values(self, x0: Array, x1: Array) -> Array:
        return self.xp.where(
            x0**2 + x1**2 <= self._radius**2,
            self.xp.ones_like(x0),
            self.xp.zeros_like(x0),
        )

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value


def demo_radon_object(xp, dev, image_id=1):
    if image_id == 0:
        disk0 = RadonDisk(xp, dev, 12.0)
        disk0.amplitude = 1.0
        disk0.s0 = 2.0
        disk0.x1_offset = 1
        disk0.x0_offset = -1.5

        disk1 = RadonDisk(xp, dev, 3.0)
        disk1.amplitude = 1.0
        disk1.x1_offset = -3
        disk1.x0_offset = 8
        disk1.s1 = 1.5

        disk2 = RadonDisk(xp, dev, 2.0)
        disk2.amplitude = -0.75
        disk2.x0_offset = -4

        radon_object = RadonObjectSequence([disk0, disk1, disk2])

    elif image_id == 1:
        disk0 = RadonDisk(xp, dev, 8.0)
        disk0.amplitude = 1.0
        disk0.s0 = 3.0

        disk1 = RadonDisk(xp, dev, 2.0)
        disk1.amplitude = 0.5
        disk1.x1_offset = 4.67

        disk2 = RadonDisk(xp, dev, 1.4)
        disk2.amplitude = -0.5
        disk2.x0_offset = -10.0

        disk3 = RadonDisk(xp, dev, 0.93)
        disk3.amplitude = -0.5
        disk3.x1_offset = -4.67

        disk4 = RadonDisk(xp, dev, 0.67)
        disk4.amplitude = 1.0
        disk4.x1_offset = -4.67

        radon_object = RadonObjectSequence([disk0, disk1, disk2, disk3, disk4])
    else:
        raise ValueError(f"Unknown image id: {image_id}")

    return radon_object


def demo_image(x, y, **kwargs):
    xp = get_namespace(x)
    dev = device(x)
    X, Y = xp.meshgrid(x, y, indexing="ij")

    radon_object = demo_radon_object(xp, dev, **kwargs)

    return radon_object.values(X, Y)


def demo_sinogram(
    s: Array, theta: Array, sig=1.0, gamma=0.0, seed=1, **kwargs
) -> Array:
    xp = get_namespace(s)
    dev = device(s)

    radon_object = demo_radon_object(xp, dev, **kwargs)

    S, THETA = xp.meshgrid(s, theta, indexing="ij")

    discrete_sinogram = radon_object.radon_transform(S, THETA)

    # add sinogram blurring in radial direction
    discrete_sinogram = gaussian_filter(discrete_sinogram, sigma=sig, axes=(0,))

    if gamma > 0:
        current_rng_state = np.random.get_state()
        np.random.seed(seed)
        discrete_sinogram = np.random.poisson(discrete_sinogram / gamma) * gamma
        np.random.set_state(current_rng_state)

    return discrete_sinogram
