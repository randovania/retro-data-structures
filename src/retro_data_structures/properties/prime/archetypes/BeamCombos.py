# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

import retro_data_structures.enums.prime as enums
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BeamCombosJson(typing_extensions.TypedDict):
        super_missile: int
        ice_spreader: int
        wavebuster: int
        flamethrower: int
        phazon_combo: int


@dataclasses.dataclass()
class BeamCombos(BaseProperty):
    super_missile: enums.VulnerabilityTypeEnum = dataclasses.field(
        default=enums.VulnerabilityTypeEnum.DoubleDamage,
        metadata={
            "reflection": FieldReflection[enums.VulnerabilityTypeEnum](
                enums.VulnerabilityTypeEnum,
                id=0x00000000,
                original_name="Super Missile",
                from_json=enums.VulnerabilityTypeEnum.from_json,
                to_json=enums.VulnerabilityTypeEnum.to_json,
            ),
        },
    )
    ice_spreader: enums.VulnerabilityTypeEnum = dataclasses.field(
        default=enums.VulnerabilityTypeEnum.DoubleDamage,
        metadata={
            "reflection": FieldReflection[enums.VulnerabilityTypeEnum](
                enums.VulnerabilityTypeEnum,
                id=0x00000001,
                original_name="Ice Spreader",
                from_json=enums.VulnerabilityTypeEnum.from_json,
                to_json=enums.VulnerabilityTypeEnum.to_json,
            ),
        },
    )
    wavebuster: enums.VulnerabilityTypeEnum = dataclasses.field(
        default=enums.VulnerabilityTypeEnum.DoubleDamage,
        metadata={
            "reflection": FieldReflection[enums.VulnerabilityTypeEnum](
                enums.VulnerabilityTypeEnum,
                id=0x00000002,
                original_name="Wavebuster",
                from_json=enums.VulnerabilityTypeEnum.from_json,
                to_json=enums.VulnerabilityTypeEnum.to_json,
            ),
        },
    )
    flamethrower: enums.VulnerabilityTypeEnum = dataclasses.field(
        default=enums.VulnerabilityTypeEnum.DoubleDamage,
        metadata={
            "reflection": FieldReflection[enums.VulnerabilityTypeEnum](
                enums.VulnerabilityTypeEnum,
                id=0x00000003,
                original_name="Flamethrower",
                from_json=enums.VulnerabilityTypeEnum.from_json,
                to_json=enums.VulnerabilityTypeEnum.to_json,
            ),
        },
    )
    phazon_combo: enums.VulnerabilityTypeEnum = dataclasses.field(
        default=enums.VulnerabilityTypeEnum.DoubleDamage,
        metadata={
            "reflection": FieldReflection[enums.VulnerabilityTypeEnum](
                enums.VulnerabilityTypeEnum,
                id=0x00000004,
                original_name="Phazon Combo",
                from_json=enums.VulnerabilityTypeEnum.from_json,
                to_json=enums.VulnerabilityTypeEnum.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        super_missile = enums.VulnerabilityTypeEnum.from_stream(data, game)
        ice_spreader = enums.VulnerabilityTypeEnum.from_stream(data, game)
        wavebuster = enums.VulnerabilityTypeEnum.from_stream(data, game)
        flamethrower = enums.VulnerabilityTypeEnum.from_stream(data, game)
        phazon_combo = enums.VulnerabilityTypeEnum.from_stream(data, game)
        return cls(super_missile, ice_spreader, wavebuster, flamethrower, phazon_combo)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        self.super_missile.to_stream(data, game)
        self.ice_spreader.to_stream(data, game)
        self.wavebuster.to_stream(data, game)
        self.flamethrower.to_stream(data, game)
        self.phazon_combo.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BeamCombosJson", data)
        return cls(
            super_missile=enums.VulnerabilityTypeEnum.from_json(json_data["super_missile"]),
            ice_spreader=enums.VulnerabilityTypeEnum.from_json(json_data["ice_spreader"]),
            wavebuster=enums.VulnerabilityTypeEnum.from_json(json_data["wavebuster"]),
            flamethrower=enums.VulnerabilityTypeEnum.from_json(json_data["flamethrower"]),
            phazon_combo=enums.VulnerabilityTypeEnum.from_json(json_data["phazon_combo"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "super_missile": self.super_missile.to_json(),
            "ice_spreader": self.ice_spreader.to_json(),
            "wavebuster": self.wavebuster.to_json(),
            "flamethrower": self.flamethrower.to_json(),
            "phazon_combo": self.phazon_combo.to_json(),
        }
