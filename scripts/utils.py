from collections.abc import Sequence
import abc
import numpy as np

from types import ModuleType
from typing import TypeAlias

Array: TypeAlias = np.ndarray


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

    def radon_transform(self, s, phi) -> float:
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


def demo_radon_object(
    xp: ModuleType = np, dev: str = "cpu", amp: float = 1.0, id: int = 1
) -> RadonObjectSequence:

    if id == 1:
        disk0 = RadonDisk(xp, dev, 8.0)
        disk0.amplitude = 1.0 * amp
        disk0.s0 = 3.0

        disk1 = RadonDisk(xp, dev, 2.0)
        disk1.amplitude = 0.5 * amp
        disk1.x1_offset = 4.67

        disk2 = RadonDisk(xp, dev, 1.4)
        disk2.amplitude = -0.5 * amp
        disk2.x0_offset = -10.0

        disk3 = RadonDisk(xp, dev, 0.93)
        disk3.amplitude = -0.5 * amp
        disk3.x1_offset = -4.67

        disk4 = RadonDisk(xp, dev, 0.67)
        disk4.amplitude = 1.0 * amp
        disk4.x1_offset = -4.67

        res = RadonObjectSequence([disk0, disk1, disk2, disk3, disk4])
    elif id == 2:
        disk0 = RadonDisk(xp, dev, 8.0)
        disk0.amplitude = 1.0 * amp
        res = RadonObjectSequence([disk0])
    elif id == 3:
        disk0 = RadonDisk(xp, dev, 8.0)
        disk0.amplitude = 1.0 * amp
        disk0.s1 = 2.0
        disk1 = RadonDisk(xp, dev, 2.0)
        disk1.amplitude = 1.5 * amp
        disk1.x1_offset = -3
        res = RadonObjectSequence([disk0, disk1])
    else:
        raise ValueError(f"unknown id: {id}")

    return res
