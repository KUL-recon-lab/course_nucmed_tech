import abc
import array_api_compat.numpy as np

from array_api_compat import device, get_namespace
from types import ModuleType
from typing import TypeAlias

Array: TypeAlias = np.ndarray


def neighbor_difference(x: Array, xp: ModuleType, padding: str = "edge") -> Array:
    """get differences with nearest neighbors for an n-dimensional array x
    using padding (by default in edge mode)
    a x.ndim*(3,) neighborhood around each element is used
    """
    x_padded = xp.pad(x, 1, mode=padding)

    # number of nearest neighbors
    num_neigh = 3**x.ndim - 1

    # array for differences and sums with nearest neighbors
    d = xp.zeros((num_neigh,) + x.shape, dtype=x.dtype)

    for i, ind in enumerate(xp.ndindex(x.ndim * (3,))):
        if i != (num_neigh // 2):
            sl = []
            for j in ind:
                if j - 2 < 0:
                    sl.append(slice(j, j - 2))
                else:
                    sl.append(slice(j, None))
            sl = tuple(sl)

            if i < num_neigh // 2:
                d[i, ...] = x - x_padded[sl]
            else:
                d[i - 1, ...] = x - x_padded[sl]

    return d


class SmoothFunction(abc.ABC):

    def __init__(self, in_shape, xp, dev, scale: float = 1.0) -> None:

        self._in_shape = in_shape
        self._scale = scale
        self._xp = xp
        self._dev = dev

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, scale: float) -> None:
        self._scale = scale

    @property
    def in_shape(self) -> tuple[int, ...]:
        return self._in_shape

    @property
    def xp(self):
        return self._xp

    @property
    def dev(self):
        return self._dev

    @abc.abstractmethod
    def _call(self, x: Array) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def _gradient(self, x: Array) -> Array:
        raise NotImplementedError

    def __call__(self, x: Array) -> float:
        x = self._xp.asarray(x, device=self._dev)

        flat_input = x.ndim == 1
        if flat_input:
            x = self._xp.reshape(x, self._in_shape)

        if self._scale == 1.0:
            res = self._call(x)
        else:
            res = self._scale * self._call(x)

        return res

    def gradient(self, x: Array) -> Array:
        dev_input = device(x)

        x = self._xp.asarray(x, device=self._dev)

        flat_input = x.ndim == 1
        if flat_input:
            x = self._xp.reshape(x, self._in_shape)

        if self._scale == 1.0:
            res = self._gradient(x)
        else:
            res = self._scale * self._gradient(x)

        if flat_input:
            res = self._xp.reshape(res, (res.size,))

        res = self.xp.to_device(res, dev_input)

        return res


class NegPoissonLogL(SmoothFunction):

    def __init__(self, data, operator, contamination) -> None:
        self._data = data
        self._op = operator
        self._contamination = contamination

        super().__init__(
            self._op.in_shape, get_namespace(self._data), device(self._data)
        )

    def _call(self, x: Array) -> float:
        exp = self._op(x) + self._contamination
        return float(self.xp.sum(exp - self._data * self.xp.log(exp)))

    def _gradient(self, x: Array) -> Array:
        exp = self._op(x) + self._contamination
        return self._op.adjoint(1 - self._data / exp)
