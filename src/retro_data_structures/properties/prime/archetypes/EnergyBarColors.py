# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class EnergyBarColorsJson(typing_extensions.TypedDict):
        energy_bar_filled: json_util.JsonValue
        energy_bar_empty: json_util.JsonValue
        energy_bar_shadow: json_util.JsonValue
        energy_tank_filled: json_util.JsonValue
        energy_tank_empty: json_util.JsonValue
        energy_digits_font: json_util.JsonValue
        energy_digits_outline: json_util.JsonValue


@dataclasses.dataclass()
class EnergyBarColors(BaseProperty):
    energy_bar_filled: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000000, original_name="EnergyBarFilled", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_bar_empty: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000000, original_name="EnergyBarEmpty", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_bar_shadow: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000000, original_name="EnergyBarShadow", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_tank_filled: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000000, original_name="EnergyTankFilled", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_tank_empty: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000000, original_name="EnergyTankEmpty", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_digits_font: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000000, original_name="EnergyDigitsFont", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_digits_outline: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x00000000,
                original_name="EnergyDigitsOutline",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        energy_bar_filled = Color.from_stream(data, game, property_size)
        energy_bar_empty = Color.from_stream(data, game, property_size)
        energy_bar_shadow = Color.from_stream(data, game, property_size)
        energy_tank_filled = Color.from_stream(data, game, property_size)
        energy_tank_empty = Color.from_stream(data, game, property_size)
        energy_digits_font = Color.from_stream(data, game, property_size)
        energy_digits_outline = Color.from_stream(data, game, property_size)
        return cls(
            energy_bar_filled,
            energy_bar_empty,
            energy_bar_shadow,
            energy_tank_filled,
            energy_tank_empty,
            energy_digits_font,
            energy_digits_outline,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        self.energy_bar_filled.to_stream(data, game)
        self.energy_bar_empty.to_stream(data, game)
        self.energy_bar_shadow.to_stream(data, game)
        self.energy_tank_filled.to_stream(data, game)
        self.energy_tank_empty.to_stream(data, game)
        self.energy_digits_font.to_stream(data, game)
        self.energy_digits_outline.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EnergyBarColorsJson", data)
        return cls(
            energy_bar_filled=Color.from_json(json_data["energy_bar_filled"]),
            energy_bar_empty=Color.from_json(json_data["energy_bar_empty"]),
            energy_bar_shadow=Color.from_json(json_data["energy_bar_shadow"]),
            energy_tank_filled=Color.from_json(json_data["energy_tank_filled"]),
            energy_tank_empty=Color.from_json(json_data["energy_tank_empty"]),
            energy_digits_font=Color.from_json(json_data["energy_digits_font"]),
            energy_digits_outline=Color.from_json(json_data["energy_digits_outline"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "energy_bar_filled": self.energy_bar_filled.to_json(),
            "energy_bar_empty": self.energy_bar_empty.to_json(),
            "energy_bar_shadow": self.energy_bar_shadow.to_json(),
            "energy_tank_filled": self.energy_tank_filled.to_json(),
            "energy_tank_empty": self.energy_tank_empty.to_json(),
            "energy_digits_font": self.energy_digits_font.to_json(),
            "energy_digits_outline": self.energy_digits_outline.to_json(),
        }
