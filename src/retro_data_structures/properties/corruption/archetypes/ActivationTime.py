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

    class ActivationTimeJson(typing_extensions.TypedDict):
        time: float
        unknown_1: int
        unknown_2: int
        unknown_3: int


@dataclasses.dataclass()
class ActivationTime(BaseProperty):
    time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="Time"),
        },
    )
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Unknown 1"),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000002, original_name="Unknown 2"),
        },
    )
    unknown_3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="Unknown 3"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        time = structs.BIG_f.unpack(data.read(4))[0]
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(time, unknown_1, unknown_2, unknown_3)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_f.pack(self.time))
        data.write(structs.BIG_l.pack(self.unknown_1))
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_l.pack(self.unknown_3))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActivationTimeJson", data)
        return cls(
            time=json_data["time"],
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "time": self.time,
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
        }
