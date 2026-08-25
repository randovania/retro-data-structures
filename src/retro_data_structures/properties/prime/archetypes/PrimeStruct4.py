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
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.PrimeStruct5 import PrimeStruct5
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PrimeStruct4Json(typing_extensions.TypedDict):
        unknown_1: int
        unknown_2: int
        particle_1: int
        particle_2: int
        texture_1: int
        texture_2: int
        unknown_3: float
        unknown_4: float
        unknown_5: float
        unknown_6: float
        unknown_7: float
        unknown_8: float
        unknown_9: float
        unknown_10: float
        unknown_11: float
        unknown_12: json_util.JsonValue
        unknown_13: json_util.JsonValue
        wpsc: int
        damage_info_1: json_util.JsonObject
        unnamed: json_util.JsonObject
        unknown_22: float
        damage_info_2: json_util.JsonObject


@dataclasses.dataclass()
class PrimeStruct4(BaseProperty):
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000000, original_name="Unknown 1"),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Unknown 2"),
        },
    )
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000002, original_name="Particle 1"),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000003, original_name="Particle 2"),
        },
    )
    texture_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000004, original_name="Texture 1"),
        },
    )
    texture_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000005, original_name="Texture 2"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Unknown 3"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unknown 6"),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="Unknown 7"),
        },
    )
    unknown_8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="Unknown 8"),
        },
    )
    unknown_9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="Unknown 9"),
        },
    )
    unknown_10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="Unknown 10"),
        },
    )
    unknown_11: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="Unknown 11"),
        },
    )
    unknown_12: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0000000F, original_name="Unknown 12", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_13: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000010, original_name="Unknown 13", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000011, original_name="WPSC"),
        },
    )
    damage_info_1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000012,
                original_name="DamageInfo 1",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unnamed: PrimeStruct5 = dataclasses.field(
        default_factory=PrimeStruct5,
        metadata={
            "reflection": FieldReflection[PrimeStruct5](
                PrimeStruct5,
                id=0x00000013,
                original_name="19",
                from_json=PrimeStruct5.from_json,
                to_json=PrimeStruct5.to_json,
            ),
        },
    )
    unknown_22: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="Unknown 22"),
        },
    )
    damage_info_2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000015,
                original_name="DamageInfo 2",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        texture_1 = structs.BIG_L.unpack(data.read(4))[0]
        texture_2 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_9 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_11 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_12 = Color.from_stream(data, game, property_size)
        unknown_13 = Color.from_stream(data, game, property_size)
        wpsc = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        unnamed = PrimeStruct5.from_stream(data, game, property_size)
        unknown_22 = structs.BIG_f.unpack(data.read(4))[0]
        damage_info_2 = DamageInfo.from_stream(data, game, property_size)
        return cls(
            unknown_1,
            unknown_2,
            particle_1,
            particle_2,
            texture_1,
            texture_2,
            unknown_3,
            unknown_4,
            unknown_5,
            unknown_6,
            unknown_7,
            unknown_8,
            unknown_9,
            unknown_10,
            unknown_11,
            unknown_12,
            unknown_13,
            wpsc,
            damage_info_1,
            unnamed,
            unknown_22,
            damage_info_2,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_l.pack(self.unknown_1))
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_L.pack(self.particle_1))
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_L.pack(self.texture_1))
        data.write(structs.BIG_L.pack(self.texture_2))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_f.pack(self.unknown_7))
        data.write(structs.BIG_f.pack(self.unknown_8))
        data.write(structs.BIG_f.pack(self.unknown_9))
        data.write(structs.BIG_f.pack(self.unknown_10))
        data.write(structs.BIG_f.pack(self.unknown_11))
        self.unknown_12.to_stream(data, game)
        self.unknown_13.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.wpsc))
        self.damage_info_1.to_stream(data, game)
        self.unnamed.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_22))
        self.damage_info_2.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PrimeStruct4Json", data)
        return cls(
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            particle_1=json_data["particle_1"],
            particle_2=json_data["particle_2"],
            texture_1=json_data["texture_1"],
            texture_2=json_data["texture_2"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
            unknown_9=json_data["unknown_9"],
            unknown_10=json_data["unknown_10"],
            unknown_11=json_data["unknown_11"],
            unknown_12=Color.from_json(json_data["unknown_12"]),
            unknown_13=Color.from_json(json_data["unknown_13"]),
            wpsc=json_data["wpsc"],
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            unnamed=PrimeStruct5.from_json(json_data["unnamed"]),
            unknown_22=json_data["unknown_22"],
            damage_info_2=DamageInfo.from_json(json_data["damage_info_2"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "particle_1": self.particle_1,
            "particle_2": self.particle_2,
            "texture_1": self.texture_1,
            "texture_2": self.texture_2,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
            "unknown_9": self.unknown_9,
            "unknown_10": self.unknown_10,
            "unknown_11": self.unknown_11,
            "unknown_12": self.unknown_12.to_json(),
            "unknown_13": self.unknown_13.to_json(),
            "wpsc": self.wpsc,
            "damage_info_1": self.damage_info_1.to_json(),
            "unnamed": self.unnamed.to_json(),
            "unknown_22": self.unknown_22,
            "damage_info_2": self.damage_info_2.to_json(),
        }

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def _dependencies_for_texture_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture_1)

    def _dependencies_for_texture_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture_2)

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
            (self._dependencies_for_texture_1, "texture_1", "AssetId"),
            (self._dependencies_for_texture_2, "texture_2", "AssetId"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self.unnamed.dependencies_for, "unnamed", "PrimeStruct5"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PrimeStruct4.{field_name} ({field_type}): {e}")
