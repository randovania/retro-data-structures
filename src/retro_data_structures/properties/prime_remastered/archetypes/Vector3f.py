# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class Vector3fJson(typing_extensions.TypedDict):
        x: float
        y: float
        z: float


@dataclasses.dataclass()
class Vector3f(BaseProperty):
    x: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="x"),
        },
    )
    y: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="y"),
        },
    )
    z: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="z"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        x = structs.LITTLE_f.unpack(data.read(4))[0]
        y = structs.LITTLE_f.unpack(data.read(4))[0]
        z = structs.LITTLE_f.unpack(data.read(4))[0]
        return cls(x, y, z)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.LITTLE_f.pack(self.x))
        data.write(structs.LITTLE_f.pack(self.y))
        data.write(structs.LITTLE_f.pack(self.z))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("Vector3fJson", data)
        return cls(
            x=json_data["x"],
            y=json_data["y"],
            z=json_data["z"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }
