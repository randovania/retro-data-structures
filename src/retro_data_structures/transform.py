from __future__ import annotations

import numbers
import typing
from typing import Any, Self

import construct
import numpy as np

if typing.TYPE_CHECKING:
    from collections.abc import Sequence

    from retro_data_structures.properties.base_vector import BaseVector

type NDTransformMatrix = np.ndarray[tuple[int, int], np.dtype[np.float32]]


class Transform(np.lib.mixins.NDArrayOperatorsMixin):
    _data: NDTransformMatrix

    def __init__(self, data: NDTransformMatrix) -> None:
        from retro_data_structures.properties.base_vector import BaseVector

        self._HANDLED_TYPES = (np.ndarray, numbers.Number, list, BaseVector)

        self._data = data

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)

    @classmethod
    def from_vectors(cls, position: BaseVector, rotation: BaseVector, scale: BaseVector) -> Self:
        pos_xfm = cls.translation(position.x, position.y, position.z)
        rot_xfm = cls.rotation(rotation.x, rotation.y, rotation.z)
        scale_xfm = cls.scale(scale.x, scale.y, scale.z)

        return (pos_xfm @ rot_xfm) @ scale_xfm

    @classmethod
    def unflatten(cls, data: Sequence[float]) -> Self:
        """Creates a Transform from a flat list of 12 floats."""

        if len(data) != 12:
            raise ValueError("Transform requires a list of exactly 12 floats")

        return cls(
            np.array(
                [
                    data[0:4],
                    data[4:8],
                    data[8:12],
                    [0.0, 0.0, 0.0, 1.0],
                ],
                np.float32,
            )
        )

    @classmethod
    def from_rows(cls, row0: Sequence[float], row1: Sequence[float], row2: Sequence[float]) -> Self:
        """Creates a Transform from 3 rows of 4 floats each."""
        if any(len(L) != 4 for L in (row0, row1, row2)):
            raise ValueError("Transform requires three lists of exactly 4 floats each")

        return cls.unflatten([*row0, *row1, *row2])

    def flatten(self) -> Sequence[float]:
        """Returns a flat list of 12 floats representing this Transform."""
        return [
            *self._data[0],
            *self._data[1],
            *self._data[2],
        ]

    @classmethod
    def identity(cls) -> Self:
        """Returns a Transform representing the identity matrix."""
        return Transform.from_rows(
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
        )

    @classmethod
    def translation(cls, x: float, y: float, z: float) -> Self:
        """Returns a Transform representing a translation."""
        return Transform.from_rows(
            [1.0, 0.0, 0.0, x],
            [0.0, 1.0, 0.0, y],
            [0.0, 0.0, 1.0, z],
        )

    @classmethod
    def rotation(cls, x: float, y: float, z: float) -> Self:
        """Returns a Transform representing a rotation (in degrees) around Euler angles."""
        x = np.deg2rad(x)
        y = np.deg2rad(y)
        z = np.deg2rad(z)

        x_rot = Transform.from_rows(
            [1.0, 0.0, 0.0, 0.0],
            [0.0, np.cos(x), np.sin(x), 0.0],
            [0.0, -np.sin(x), np.cos(x), 0.0],
        )
        y_rot = Transform.from_rows(
            [np.cos(y), 0.0, -np.sin(y), 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [np.sin(y), 0.0, np.cos(y), 0.0],
        )
        z_rot = Transform.from_rows(
            [np.cos(z), -np.sin(z), 0.0, 0.0],
            [np.sin(z), np.cos(z), 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
        )
        return y_rot @ x_rot @ z_rot  # order here matters and is correct

    @classmethod
    def scale(cls, x: float, y: float, z: float) -> Self:
        """Returns a Transform representing a scale."""
        return Transform.from_rows(
            [x, 0.0, 0.0, 0.0],
            [0.0, y, 0.0, 0.0],
            [0.0, 0.0, z, 0.0],
        )

    def __array__(self, dtype: np.dtype | None = None, copy: bool | None = None) -> NDTransformMatrix:
        if dtype is not None and dtype != np.float32:
            raise ValueError("Transform only supports float32")
        return np.array(self._data, dtype=np.float32, copy=copy)

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, Transform):
            return np.array_equal(self, other)
        return super().__eq__(other)

    def __ne__(self, other: Any) -> Any:
        return not self == other

    __hash__ = None

    @typing.overload
    def __truediv__(self, other: Transform) -> Transform: ...
    def __truediv__(self, other: object) -> Any:
        if isinstance(other, Transform):
            # matrix multiply by the inverse of the other transform
            return self @ np.linalg.inv(other)
        return super().__truediv__(other)

    @typing.overload
    def __itruediv__(self, other: Transform) -> Transform: ...
    def __itruediv__(self, other: object) -> Any:
        return self.__truediv__(other)

    @typing.overload
    def __matmul__(self, other: Transform) -> Transform: ...
    @typing.overload
    def __matmul__[T: BaseVector](self, other: T) -> T: ...
    def __matmul__(self, other: object) -> Any:
        return super().__matmul__(other)

    @typing.overload
    def __imatmul__(self, other: Transform) -> Transform: ...
    @typing.overload
    def __imatmul__[T: BaseVector](self, other: T) -> T: ...
    def __imatmul__(self, other: object) -> Any:
        return self.__matmul__(other)

    def __array_ufunc__(self, ufunc: np.ufunc, method: str, /, *inputs: Any, **kwargs: Any) -> Any:
        """
        Taken from https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html
        """

        from retro_data_structures.properties.base_vector import BaseVector

        out: tuple = kwargs.get("out", ())

        all_inputs = inputs + out

        for x in all_inputs:
            # Only support operations with instances of
            # _HANDLED_TYPES. Use ArrayLike instead of type(self)
            # for isinstance to allow subclasses that don't
            # override __array_ufunc__ to handle ArrayLike objects.
            if not isinstance(x, self._HANDLED_TYPES + (Transform,)):
                return NotImplemented

        # Defer to the implementation of the ufunc
        # on unwrapped values.
        inputs = tuple(x._data if isinstance(x, Transform) else x for x in inputs)
        if out:
            kwargs["out"] = tuple(x._data if isinstance(x, Transform) else x for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        def _wrap_res(res):
            if isinstance(res, np.ndarray):
                if res.shape == (4, 4):
                    return type(self)(res)
                if res.shape == (4,):
                    if all((x is self) or isinstance(x, BaseVector) for x in all_inputs):
                        restype = type(next(x for x in all_inputs if isinstance(x, BaseVector)))
                        return restype(float(res[0]), float(res[1]), float(res[2]))
            return res

        if type(result) is tuple:
            # multiple return values
            return tuple(_wrap_res(x) for x in result)
        elif method == "at":
            # no return value
            return None
        else:
            # one return value
            return _wrap_res(result)


class _TransformAdapter(construct.Adapter):
    def _decode(self, obj: Sequence[float], context: construct.Container, path: str) -> Transform:
        return Transform.unflatten(obj)

    def _encode(self, obj: Transform, context: construct.Container, path: str) -> Sequence[float]:
        return obj.flatten()


Transform4f = _TransformAdapter(construct.Array(12, construct.Float32b))
