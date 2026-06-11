from __future__ import annotations

import copy
import dataclasses
import math
import struct
import typing

import numpy as np

from retro_data_structures.properties.base_property import BaseProperty

if typing.TYPE_CHECKING:
    import typing_extensions

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game


@dataclasses.dataclass()
class Vector(BaseProperty):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(*struct.unpack(game.struct_endianness + "fff", data.read(12)))

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(struct.pack(game.struct_endianness + "fff", self.x, self.y, self.z))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("dict[str, float]", data)
        return cls(json_data["x"], json_data["y"], json_data["z"])

    def to_json(self) -> json_util.JsonObject:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
        yield from []

    def __array__(
        self, dtype: np.dtype | None = None, copy: bool | None = None
    ) -> np.ndarray[tuple[int], np.dtype[np.float32]]:
        if dtype is not None and dtype != np.float32:
            raise ValueError("Vector only supports float32")
        return np.array([self.x, self.y, self.z, 1.0], dtype=np.float32, copy=copy)

    def __iter__(self) -> typing.Iterator[float]:
        return iter((self.x, self.y, self.z))

    def __add__(self, other: Vector) -> typing_extensions.Self:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector) -> typing_extensions.Self:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: int | float | Vector) -> typing_extensions.Self:
        if isinstance(other, Vector):
            return self.__class__(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, int | float):
            return self.__class__(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __rmul__(self, other: int | float | Vector) -> typing_extensions.Self:
        return self.__mul__(other)  # commutative property

    def __truediv__(self, other: int | float | Vector) -> typing_extensions.Self:
        if isinstance(other, Vector):
            return self.__class__(self.x / other.x, self.y / other.y, self.z / other.z)
        if isinstance(other, int | float):
            return self.__class__(self.x / other, self.y / other, self.z / other)
        return NotImplemented

    def __floordiv__(self, other: int | float | Vector) -> typing_extensions.Self:
        if isinstance(other, Vector):
            return self.__class__(self.x // other.x, self.y // other.y, self.z // other.z)
        if isinstance(other, int | float):
            return self.__class__(self.x // other, self.y // other, self.z // other)
        return NotImplemented

    def truncated(self) -> typing_extensions.Self:
        """
        Truncates the values of each component to be representable
        with single-precision floats. Since the values are single-precision
        in-game, this better reflects the actual value of this vector.

        :returns: A new vector with truncated components
        """

        def truncate(val: float) -> float:
            return struct.unpack(">f", struct.pack(">f", val))[0]

        return self.__class__(truncate(self.x), truncate(self.y), truncate(self.z))

    def rotate(self, rotation: Vector, center: Vector | None = None) -> typing_extensions.Self:
        """
        Rotates the vector on all three axes, around a center point.

        :param rotation: The angle (in degrees) to rotate around each axis
        :param center: The point around which to revolve
        :returns: A new vector with the rotation applied
        """

        if center is None:
            center = Vector()

        pos = [self.x - center.x, self.y - center.y, self.z - center.z]
        rot = [rotation.x, rotation.y, rotation.z]

        for i in range(3):
            theta = rot[i] * math.pi / 180.0
            sin = math.sin(theta)
            cos = math.cos(theta)

            old_pos = copy.copy(pos)

            comp1 = (i + 1) % 3
            comp2 = (i + 2) % 3
            pos[comp1] = old_pos[comp1] * cos - old_pos[comp2] * sin
            pos[comp2] = old_pos[comp1] * sin + old_pos[comp2] * cos

        return self.__class__(pos[0], pos[1], pos[2]) + center
