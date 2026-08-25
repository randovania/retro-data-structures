# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PrimeStruct6Json(typing_extensions.TypedDict):
        unnamed: json_util.JsonObject
        unknown_1: json_util.JsonValue
        unknown_2: int
        unknown_3: int


@dataclasses.dataclass()
class PrimeStruct6(BaseProperty):
    unnamed: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00000000,
                original_name="0",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_1: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000001, original_name="Unknown 1", from_json=Color.from_json, to_json=Color.to_json
            ),
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
        unnamed = DamageVulnerability.from_stream(data, game, property_size)
        unknown_1 = Color.from_stream(data, game, property_size)
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(unnamed, unknown_1, unknown_2, unknown_3)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        self.unnamed.to_stream(data, game)
        self.unknown_1.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_l.pack(self.unknown_3))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PrimeStruct6Json", data)
        return cls(
            unnamed=DamageVulnerability.from_json(json_data["unnamed"]),
            unknown_1=Color.from_json(json_data["unknown_1"]),
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unnamed": self.unnamed.to_json(),
            "unknown_1": self.unknown_1.to_json(),
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
        }
