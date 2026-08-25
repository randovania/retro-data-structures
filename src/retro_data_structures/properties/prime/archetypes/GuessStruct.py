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

    class GuessStructJson(typing_extensions.TypedDict):
        duration: float
        sfx_dist: float


@dataclasses.dataclass()
class GuessStruct(BaseProperty):
    duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="Duration"),
        },
    )
    sfx_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="SfxDist"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        duration = structs.BIG_f.unpack(data.read(4))[0]
        sfx_dist = structs.BIG_f.unpack(data.read(4))[0]
        return cls(duration, sfx_dist)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_f.pack(self.duration))
        data.write(structs.BIG_f.pack(self.sfx_dist))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GuessStructJson", data)
        return cls(
            duration=json_data["duration"],
            sfx_dist=json_data["sfx_dist"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "duration": self.duration,
            "sfx_dist": self.sfx_dist,
        }
