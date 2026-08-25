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

    class HealthInfoJson(typing_extensions.TypedDict):
        health: float
        knockback_resistance: float


@dataclasses.dataclass()
class HealthInfo(BaseProperty):
    health: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="Health"),
        },
    )
    knockback_resistance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="Knockback Resistance"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        health = structs.BIG_f.unpack(data.read(4))[0]
        knockback_resistance = structs.BIG_f.unpack(data.read(4))[0]
        return cls(health, knockback_resistance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_f.pack(self.health))
        data.write(structs.BIG_f.pack(self.knockback_resistance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("HealthInfoJson", data)
        return cls(
            health=json_data["health"],
            knockback_resistance=json_data["knockback_resistance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "health": self.health,
            "knockback_resistance": self.knockback_resistance,
        }
