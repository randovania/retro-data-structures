# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.archetypes.PrimeStruct2 import PrimeStruct2
from retro_data_structures.properties.prime.archetypes.PrimeStruct4 import PrimeStruct4
from retro_data_structures.properties.prime.archetypes.PrimeStruct6 import PrimeStruct6
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class MassivePrimeStructJson(typing_extensions.TypedDict):
        unknown_1: int
        unnamed_0x00000001: json_util.JsonObject
        unnamed_0x00000002: json_util.JsonObject
        unknown_2: int
        prime_struct2_1: json_util.JsonObject
        prime_struct2_2: json_util.JsonObject
        prime_struct2_3: json_util.JsonObject
        unknown_3: int
        particle_1: int
        particle_2: int
        particle_3: int
        damage_info_1: json_util.JsonObject
        unknown_4: float
        unknown_5: float
        texture_1: int
        unknown_6: int
        unknown_7: int
        particle_4: int
        prime_struct4_1: json_util.JsonObject
        prime_struct4_2: json_util.JsonObject
        prime_struct4_3: json_util.JsonObject
        prime_struct4_4: json_util.JsonObject
        wpsc_1: int
        damage_info_2: json_util.JsonObject
        prime_struct2_4: json_util.JsonObject
        wpsc_2: int
        damage_info_3: json_util.JsonObject
        prime_struct2_5: json_util.JsonObject
        unknown_8: int
        particle_5: int
        damage_info_4: json_util.JsonObject
        unknown_9: float
        unknown_10: float
        unknown_11: float
        texture_2: int
        unknown_12: bool
        unknown_13: bool
        unknown_14: bool
        unknown_15: bool
        damage_info_5: json_util.JsonObject
        prime_struct2_6: json_util.JsonObject
        particle_6: int
        swhc: int
        particle_7: int
        particle_8: int
        prime_struct6_1: json_util.JsonObject
        prime_struct6_2: json_util.JsonObject
        prime_struct6_3: json_util.JsonObject
        prime_struct6_4: json_util.JsonObject


@dataclasses.dataclass()
class MassivePrimeStruct(BaseProperty):
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000000, original_name="Unknown 1"),
        },
    )
    unnamed_0x00000001: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x00000001,
                original_name="1",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    unnamed_0x00000002: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000002,
                original_name="2",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="Unknown 2"),
        },
    )
    prime_struct2_1: PrimeStruct2 = dataclasses.field(
        default_factory=PrimeStruct2,
        metadata={
            "reflection": FieldReflection[PrimeStruct2](
                PrimeStruct2,
                id=0x00000004,
                original_name="PrimeStruct2 1",
                from_json=PrimeStruct2.from_json,
                to_json=PrimeStruct2.to_json,
            ),
        },
    )
    prime_struct2_2: PrimeStruct2 = dataclasses.field(
        default_factory=PrimeStruct2,
        metadata={
            "reflection": FieldReflection[PrimeStruct2](
                PrimeStruct2,
                id=0x00000005,
                original_name="PrimeStruct2 2",
                from_json=PrimeStruct2.from_json,
                to_json=PrimeStruct2.to_json,
            ),
        },
    )
    prime_struct2_3: PrimeStruct2 = dataclasses.field(
        default_factory=PrimeStruct2,
        metadata={
            "reflection": FieldReflection[PrimeStruct2](
                PrimeStruct2,
                id=0x00000006,
                original_name="PrimeStruct2 3",
                from_json=PrimeStruct2.from_json,
                to_json=PrimeStruct2.to_json,
            ),
        },
    )
    unknown_3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000007, original_name="Unknown 3"),
        },
    )
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="Particle 1"),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="Particle 2"),
        },
    )
    particle_3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="Particle 3"),
        },
    )
    damage_info_1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000B,
                original_name="DamageInfo 1",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="Unknown 5"),
        },
    )
    texture_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000E, original_name="Texture 1"),
        },
    )
    unknown_6: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000F, original_name="Unknown 6"),
        },
    )
    unknown_7: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000010, original_name="Unknown 7"),
        },
    )
    particle_4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000011, original_name="Particle 4"),
        },
    )
    prime_struct4_1: PrimeStruct4 = dataclasses.field(
        default_factory=PrimeStruct4,
        metadata={
            "reflection": FieldReflection[PrimeStruct4](
                PrimeStruct4,
                id=0x00000012,
                original_name="PrimeStruct4 1",
                from_json=PrimeStruct4.from_json,
                to_json=PrimeStruct4.to_json,
            ),
        },
    )
    prime_struct4_2: PrimeStruct4 = dataclasses.field(
        default_factory=PrimeStruct4,
        metadata={
            "reflection": FieldReflection[PrimeStruct4](
                PrimeStruct4,
                id=0x00000013,
                original_name="PrimeStruct4 2",
                from_json=PrimeStruct4.from_json,
                to_json=PrimeStruct4.to_json,
            ),
        },
    )
    prime_struct4_3: PrimeStruct4 = dataclasses.field(
        default_factory=PrimeStruct4,
        metadata={
            "reflection": FieldReflection[PrimeStruct4](
                PrimeStruct4,
                id=0x00000014,
                original_name="PrimeStruct4 3",
                from_json=PrimeStruct4.from_json,
                to_json=PrimeStruct4.to_json,
            ),
        },
    )
    prime_struct4_4: PrimeStruct4 = dataclasses.field(
        default_factory=PrimeStruct4,
        metadata={
            "reflection": FieldReflection[PrimeStruct4](
                PrimeStruct4,
                id=0x00000015,
                original_name="PrimeStruct4 4",
                from_json=PrimeStruct4.from_json,
                to_json=PrimeStruct4.to_json,
            ),
        },
    )
    wpsc_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000016, original_name="WPSC 1"),
        },
    )
    damage_info_2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000017,
                original_name="DamageInfo 2",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    prime_struct2_4: PrimeStruct2 = dataclasses.field(
        default_factory=PrimeStruct2,
        metadata={
            "reflection": FieldReflection[PrimeStruct2](
                PrimeStruct2,
                id=0x00000018,
                original_name="PrimeStruct2 4",
                from_json=PrimeStruct2.from_json,
                to_json=PrimeStruct2.to_json,
            ),
        },
    )
    wpsc_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000019, original_name="WPSC 2"),
        },
    )
    damage_info_3: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000001A,
                original_name="DamageInfo 3",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    prime_struct2_5: PrimeStruct2 = dataclasses.field(
        default_factory=PrimeStruct2,
        metadata={
            "reflection": FieldReflection[PrimeStruct2](
                PrimeStruct2,
                id=0x0000001B,
                original_name="PrimeStruct2 5",
                from_json=PrimeStruct2.from_json,
                to_json=PrimeStruct2.to_json,
            ),
        },
    )
    unknown_8: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001C, original_name="Unknown 8"),
        },
    )
    particle_5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001D, original_name="Particle 5"),
        },
    )
    damage_info_4: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000001E,
                original_name="DamageInfo 4",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001F, original_name="Unknown 9"),
        },
    )
    unknown_10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000020, original_name="Unknown 10"),
        },
    )
    unknown_11: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000021, original_name="Unknown 11"),
        },
    )
    texture_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000022, original_name="Texture 2"),
        },
    )
    unknown_12: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000023, original_name="Unknown 12"),
        },
    )
    unknown_13: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000024, original_name="Unknown 13"),
        },
    )
    unknown_14: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000025, original_name="Unknown 14"),
        },
    )
    unknown_15: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000026, original_name="Unknown 15"),
        },
    )
    damage_info_5: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000027,
                original_name="DamageInfo 5",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    prime_struct2_6: PrimeStruct2 = dataclasses.field(
        default_factory=PrimeStruct2,
        metadata={
            "reflection": FieldReflection[PrimeStruct2](
                PrimeStruct2,
                id=0x00000028,
                original_name="PrimeStruct2 6",
                from_json=PrimeStruct2.from_json,
                to_json=PrimeStruct2.to_json,
            ),
        },
    )
    particle_6: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000029, original_name="Particle 6"),
        },
    )
    swhc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SWHC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000002A, original_name="SWHC"),
        },
    )
    particle_7: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000002B, original_name="Particle 7"),
        },
    )
    particle_8: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000002C, original_name="Particle 8"),
        },
    )
    prime_struct6_1: PrimeStruct6 = dataclasses.field(
        default_factory=PrimeStruct6,
        metadata={
            "reflection": FieldReflection[PrimeStruct6](
                PrimeStruct6,
                id=0x0000002D,
                original_name="PrimeStruct6 1",
                from_json=PrimeStruct6.from_json,
                to_json=PrimeStruct6.to_json,
            ),
        },
    )
    prime_struct6_2: PrimeStruct6 = dataclasses.field(
        default_factory=PrimeStruct6,
        metadata={
            "reflection": FieldReflection[PrimeStruct6](
                PrimeStruct6,
                id=0x0000002E,
                original_name="PrimeStruct6 2",
                from_json=PrimeStruct6.from_json,
                to_json=PrimeStruct6.to_json,
            ),
        },
    )
    prime_struct6_3: PrimeStruct6 = dataclasses.field(
        default_factory=PrimeStruct6,
        metadata={
            "reflection": FieldReflection[PrimeStruct6](
                PrimeStruct6,
                id=0x0000002F,
                original_name="PrimeStruct6 3",
                from_json=PrimeStruct6.from_json,
                to_json=PrimeStruct6.to_json,
            ),
        },
    )
    prime_struct6_4: PrimeStruct6 = dataclasses.field(
        default_factory=PrimeStruct6,
        metadata={
            "reflection": FieldReflection[PrimeStruct6](
                PrimeStruct6,
                id=0x00000030,
                original_name="PrimeStruct6 4",
                from_json=PrimeStruct6.from_json,
                to_json=PrimeStruct6.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        unnamed_0x00000001 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000002 = ActorParameters.from_stream(data, game, property_size)
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        prime_struct2_1 = PrimeStruct2.from_stream(data, game, property_size)
        prime_struct2_2 = PrimeStruct2.from_stream(data, game, property_size)
        prime_struct2_3 = PrimeStruct2.from_stream(data, game, property_size)
        unknown_3 = structs.BIG_l.unpack(data.read(4))[0]
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        particle_3 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        texture_1 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_l.unpack(data.read(4))[0]
        particle_4 = structs.BIG_L.unpack(data.read(4))[0]
        prime_struct4_1 = PrimeStruct4.from_stream(data, game, property_size)
        prime_struct4_2 = PrimeStruct4.from_stream(data, game, property_size)
        prime_struct4_3 = PrimeStruct4.from_stream(data, game, property_size)
        prime_struct4_4 = PrimeStruct4.from_stream(data, game, property_size)
        wpsc_1 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_2 = DamageInfo.from_stream(data, game, property_size)
        prime_struct2_4 = PrimeStruct2.from_stream(data, game, property_size)
        wpsc_2 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_3 = DamageInfo.from_stream(data, game, property_size)
        prime_struct2_5 = PrimeStruct2.from_stream(data, game, property_size)
        unknown_8 = structs.BIG_l.unpack(data.read(4))[0]
        particle_5 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_4 = DamageInfo.from_stream(data, game, property_size)
        unknown_9 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_11 = structs.BIG_f.unpack(data.read(4))[0]
        texture_2 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_12 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_13 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_14 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_15 = structs.BIG_bool_.unpack(data.read(1))[0]
        damage_info_5 = DamageInfo.from_stream(data, game, property_size)
        prime_struct2_6 = PrimeStruct2.from_stream(data, game, property_size)
        particle_6 = structs.BIG_L.unpack(data.read(4))[0]
        swhc = structs.BIG_L.unpack(data.read(4))[0]
        particle_7 = structs.BIG_L.unpack(data.read(4))[0]
        particle_8 = structs.BIG_L.unpack(data.read(4))[0]
        prime_struct6_1 = PrimeStruct6.from_stream(data, game, property_size)
        prime_struct6_2 = PrimeStruct6.from_stream(data, game, property_size)
        prime_struct6_3 = PrimeStruct6.from_stream(data, game, property_size)
        prime_struct6_4 = PrimeStruct6.from_stream(data, game, property_size)
        return cls(
            unknown_1,
            unnamed_0x00000001,
            unnamed_0x00000002,
            unknown_2,
            prime_struct2_1,
            prime_struct2_2,
            prime_struct2_3,
            unknown_3,
            particle_1,
            particle_2,
            particle_3,
            damage_info_1,
            unknown_4,
            unknown_5,
            texture_1,
            unknown_6,
            unknown_7,
            particle_4,
            prime_struct4_1,
            prime_struct4_2,
            prime_struct4_3,
            prime_struct4_4,
            wpsc_1,
            damage_info_2,
            prime_struct2_4,
            wpsc_2,
            damage_info_3,
            prime_struct2_5,
            unknown_8,
            particle_5,
            damage_info_4,
            unknown_9,
            unknown_10,
            unknown_11,
            texture_2,
            unknown_12,
            unknown_13,
            unknown_14,
            unknown_15,
            damage_info_5,
            prime_struct2_6,
            particle_6,
            swhc,
            particle_7,
            particle_8,
            prime_struct6_1,
            prime_struct6_2,
            prime_struct6_3,
            prime_struct6_4,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_l.pack(self.unknown_1))
        self.unnamed_0x00000001.to_stream(data, game)
        self.unnamed_0x00000002.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.unknown_2))
        self.prime_struct2_1.to_stream(data, game)
        self.prime_struct2_2.to_stream(data, game)
        self.prime_struct2_3.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.unknown_3))
        data.write(structs.BIG_L.pack(self.particle_1))
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_L.pack(self.particle_3))
        self.damage_info_1.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_L.pack(self.texture_1))
        data.write(structs.BIG_l.pack(self.unknown_6))
        data.write(structs.BIG_l.pack(self.unknown_7))
        data.write(structs.BIG_L.pack(self.particle_4))
        self.prime_struct4_1.to_stream(data, game)
        self.prime_struct4_2.to_stream(data, game)
        self.prime_struct4_3.to_stream(data, game)
        self.prime_struct4_4.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.wpsc_1))
        self.damage_info_2.to_stream(data, game)
        self.prime_struct2_4.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.wpsc_2))
        self.damage_info_3.to_stream(data, game)
        self.prime_struct2_5.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.unknown_8))
        data.write(structs.BIG_L.pack(self.particle_5))
        self.damage_info_4.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_9))
        data.write(structs.BIG_f.pack(self.unknown_10))
        data.write(structs.BIG_f.pack(self.unknown_11))
        data.write(structs.BIG_L.pack(self.texture_2))
        data.write(structs.BIG_bool_.pack(self.unknown_12))
        data.write(structs.BIG_bool_.pack(self.unknown_13))
        data.write(structs.BIG_bool_.pack(self.unknown_14))
        data.write(structs.BIG_bool_.pack(self.unknown_15))
        self.damage_info_5.to_stream(data, game)
        self.prime_struct2_6.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle_6))
        data.write(structs.BIG_L.pack(self.swhc))
        data.write(structs.BIG_L.pack(self.particle_7))
        data.write(structs.BIG_L.pack(self.particle_8))
        self.prime_struct6_1.to_stream(data, game)
        self.prime_struct6_2.to_stream(data, game)
        self.prime_struct6_3.to_stream(data, game)
        self.prime_struct6_4.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MassivePrimeStructJson", data)
        return cls(
            unknown_1=json_data["unknown_1"],
            unnamed_0x00000001=PatternedAITypedef.from_json(json_data["unnamed_0x00000001"]),
            unnamed_0x00000002=ActorParameters.from_json(json_data["unnamed_0x00000002"]),
            unknown_2=json_data["unknown_2"],
            prime_struct2_1=PrimeStruct2.from_json(json_data["prime_struct2_1"]),
            prime_struct2_2=PrimeStruct2.from_json(json_data["prime_struct2_2"]),
            prime_struct2_3=PrimeStruct2.from_json(json_data["prime_struct2_3"]),
            unknown_3=json_data["unknown_3"],
            particle_1=json_data["particle_1"],
            particle_2=json_data["particle_2"],
            particle_3=json_data["particle_3"],
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            texture_1=json_data["texture_1"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            particle_4=json_data["particle_4"],
            prime_struct4_1=PrimeStruct4.from_json(json_data["prime_struct4_1"]),
            prime_struct4_2=PrimeStruct4.from_json(json_data["prime_struct4_2"]),
            prime_struct4_3=PrimeStruct4.from_json(json_data["prime_struct4_3"]),
            prime_struct4_4=PrimeStruct4.from_json(json_data["prime_struct4_4"]),
            wpsc_1=json_data["wpsc_1"],
            damage_info_2=DamageInfo.from_json(json_data["damage_info_2"]),
            prime_struct2_4=PrimeStruct2.from_json(json_data["prime_struct2_4"]),
            wpsc_2=json_data["wpsc_2"],
            damage_info_3=DamageInfo.from_json(json_data["damage_info_3"]),
            prime_struct2_5=PrimeStruct2.from_json(json_data["prime_struct2_5"]),
            unknown_8=json_data["unknown_8"],
            particle_5=json_data["particle_5"],
            damage_info_4=DamageInfo.from_json(json_data["damage_info_4"]),
            unknown_9=json_data["unknown_9"],
            unknown_10=json_data["unknown_10"],
            unknown_11=json_data["unknown_11"],
            texture_2=json_data["texture_2"],
            unknown_12=json_data["unknown_12"],
            unknown_13=json_data["unknown_13"],
            unknown_14=json_data["unknown_14"],
            unknown_15=json_data["unknown_15"],
            damage_info_5=DamageInfo.from_json(json_data["damage_info_5"]),
            prime_struct2_6=PrimeStruct2.from_json(json_data["prime_struct2_6"]),
            particle_6=json_data["particle_6"],
            swhc=json_data["swhc"],
            particle_7=json_data["particle_7"],
            particle_8=json_data["particle_8"],
            prime_struct6_1=PrimeStruct6.from_json(json_data["prime_struct6_1"]),
            prime_struct6_2=PrimeStruct6.from_json(json_data["prime_struct6_2"]),
            prime_struct6_3=PrimeStruct6.from_json(json_data["prime_struct6_3"]),
            prime_struct6_4=PrimeStruct6.from_json(json_data["prime_struct6_4"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_1": self.unknown_1,
            "unnamed_0x00000001": self.unnamed_0x00000001.to_json(),
            "unnamed_0x00000002": self.unnamed_0x00000002.to_json(),
            "unknown_2": self.unknown_2,
            "prime_struct2_1": self.prime_struct2_1.to_json(),
            "prime_struct2_2": self.prime_struct2_2.to_json(),
            "prime_struct2_3": self.prime_struct2_3.to_json(),
            "unknown_3": self.unknown_3,
            "particle_1": self.particle_1,
            "particle_2": self.particle_2,
            "particle_3": self.particle_3,
            "damage_info_1": self.damage_info_1.to_json(),
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "texture_1": self.texture_1,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "particle_4": self.particle_4,
            "prime_struct4_1": self.prime_struct4_1.to_json(),
            "prime_struct4_2": self.prime_struct4_2.to_json(),
            "prime_struct4_3": self.prime_struct4_3.to_json(),
            "prime_struct4_4": self.prime_struct4_4.to_json(),
            "wpsc_1": self.wpsc_1,
            "damage_info_2": self.damage_info_2.to_json(),
            "prime_struct2_4": self.prime_struct2_4.to_json(),
            "wpsc_2": self.wpsc_2,
            "damage_info_3": self.damage_info_3.to_json(),
            "prime_struct2_5": self.prime_struct2_5.to_json(),
            "unknown_8": self.unknown_8,
            "particle_5": self.particle_5,
            "damage_info_4": self.damage_info_4.to_json(),
            "unknown_9": self.unknown_9,
            "unknown_10": self.unknown_10,
            "unknown_11": self.unknown_11,
            "texture_2": self.texture_2,
            "unknown_12": self.unknown_12,
            "unknown_13": self.unknown_13,
            "unknown_14": self.unknown_14,
            "unknown_15": self.unknown_15,
            "damage_info_5": self.damage_info_5.to_json(),
            "prime_struct2_6": self.prime_struct2_6.to_json(),
            "particle_6": self.particle_6,
            "swhc": self.swhc,
            "particle_7": self.particle_7,
            "particle_8": self.particle_8,
            "prime_struct6_1": self.prime_struct6_1.to_json(),
            "prime_struct6_2": self.prime_struct6_2.to_json(),
            "prime_struct6_3": self.prime_struct6_3.to_json(),
            "prime_struct6_4": self.prime_struct6_4.to_json(),
        }

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def _dependencies_for_particle_3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_3)

    def _dependencies_for_texture_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture_1)

    def _dependencies_for_unknown_7(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_7)

    def _dependencies_for_particle_4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_4)

    def _dependencies_for_wpsc_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_1)

    def _dependencies_for_wpsc_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_2)

    def _dependencies_for_particle_5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_5)

    def _dependencies_for_texture_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture_2)

    def _dependencies_for_particle_6(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_6)

    def _dependencies_for_swhc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.swhc)

    def _dependencies_for_particle_7(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_7)

    def _dependencies_for_particle_8(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_8)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000001.dependencies_for, "unnamed_0x00000001", "PatternedAITypedef"),
            (self.unnamed_0x00000002.dependencies_for, "unnamed_0x00000002", "ActorParameters"),
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
            (self._dependencies_for_particle_3, "particle_3", "AssetId"),
            (self._dependencies_for_texture_1, "texture_1", "AssetId"),
            (self._dependencies_for_unknown_7, "unknown_7", "int"),
            (self._dependencies_for_particle_4, "particle_4", "AssetId"),
            (self.prime_struct4_1.dependencies_for, "prime_struct4_1", "PrimeStruct4"),
            (self.prime_struct4_2.dependencies_for, "prime_struct4_2", "PrimeStruct4"),
            (self.prime_struct4_3.dependencies_for, "prime_struct4_3", "PrimeStruct4"),
            (self.prime_struct4_4.dependencies_for, "prime_struct4_4", "PrimeStruct4"),
            (self._dependencies_for_wpsc_1, "wpsc_1", "AssetId"),
            (self._dependencies_for_wpsc_2, "wpsc_2", "AssetId"),
            (self._dependencies_for_particle_5, "particle_5", "AssetId"),
            (self._dependencies_for_texture_2, "texture_2", "AssetId"),
            (self._dependencies_for_particle_6, "particle_6", "AssetId"),
            (self._dependencies_for_swhc, "swhc", "AssetId"),
            (self._dependencies_for_particle_7, "particle_7", "AssetId"),
            (self._dependencies_for_particle_8, "particle_8", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for MassivePrimeStruct.{field_name} ({field_type}): {e}")
