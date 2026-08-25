# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.SandBossStructA import SandBossStructA
from retro_data_structures.properties.echoes.archetypes.UnknownStruct40 import UnknownStruct40
from retro_data_structures.properties.echoes.archetypes.UnknownStruct41 import UnknownStruct41
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SandBossDataJson(typing_extensions.TypedDict):
        scannable_info1: int
        command_index: int
        cracked_sphere1: int
        cracked_sphere2: int
        cracked_sphere3: int
        snap_jaw_damage: json_util.JsonObject
        spit_out_damage: json_util.JsonObject
        unknown_0xbf88fe4f: float
        unknown_0x74c702b3: float
        dark_beam_projectile: int
        dark_beam_damage: json_util.JsonObject
        unknown_0x2b42dddf: float
        unknown_0x1562e0d6: float
        unknown_0xd0db2574: float
        suck_air_time: float
        suck_morphball_range: float
        spit_morphball_time: float
        part: int
        unknown_struct40: json_util.JsonObject
        unknown_struct41: json_util.JsonObject
        sand_boss_struct_a_0x8b452a19: json_util.JsonObject
        sand_boss_struct_a_0x0cf8c54c: json_util.JsonObject
        model_with_tail_armor: int
        skin_for_armored_tail: int
        damage_vulnerability: json_util.JsonObject
        stampede_vulnerability: json_util.JsonObject
        suck_air_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class SandBossData(BaseProperty):
    scannable_info1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x72124842, original_name="ScannableInfo1"),
        },
    )
    command_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE34D7C49, original_name="CommandIndex"),
        },
    )
    cracked_sphere1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE47262F5, original_name="CrackedSphere1"),
        },
    )
    cracked_sphere2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x62E6105B, original_name="CrackedSphere2"),
        },
    )
    cracked_sphere3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA9BAC3FE, original_name="CrackedSphere3"),
        },
    )
    snap_jaw_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x19C91AAA,
                original_name="SnapJawDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    spit_out_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x58889364,
                original_name="SpitOutDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xbf88fe4f: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBF88FE4F, original_name="Unknown"),
        },
    )
    unknown_0x74c702b3: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x74C702B3, original_name="Unknown"),
        },
    )
    dark_beam_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x35EE175D, original_name="DarkBeamProjectile"),
        },
    )
    dark_beam_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x94C2150F,
                original_name="DarkBeamDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x2b42dddf: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B42DDDF, original_name="Unknown"),
        },
    )
    unknown_0x1562e0d6: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1562E0D6, original_name="Unknown"),
        },
    )
    unknown_0xd0db2574: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD0DB2574, original_name="Unknown"),
        },
    )
    suck_air_time: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF1AED43D, original_name="SuckAirTime"),
        },
    )
    suck_morphball_range: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3055DD0E, original_name="SuckMorphballRange"),
        },
    )
    spit_morphball_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6F135965, original_name="SpitMorphballTime"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC49086D9, original_name="PART"),
        },
    )
    unknown_struct40: UnknownStruct40 = dataclasses.field(
        default_factory=UnknownStruct40,
        metadata={
            "reflection": FieldReflection[UnknownStruct40](
                UnknownStruct40,
                id=0x95371A32,
                original_name="UnknownStruct40",
                from_json=UnknownStruct40.from_json,
                to_json=UnknownStruct40.to_json,
            ),
        },
    )
    unknown_struct41: UnknownStruct41 = dataclasses.field(
        default_factory=UnknownStruct41,
        metadata={
            "reflection": FieldReflection[UnknownStruct41](
                UnknownStruct41,
                id=0x7619E561,
                original_name="UnknownStruct41",
                from_json=UnknownStruct41.from_json,
                to_json=UnknownStruct41.to_json,
            ),
        },
    )
    sand_boss_struct_a_0x8b452a19: SandBossStructA = dataclasses.field(
        default_factory=SandBossStructA,
        metadata={
            "reflection": FieldReflection[SandBossStructA](
                SandBossStructA,
                id=0x8B452A19,
                original_name="SandBossStructA",
                from_json=SandBossStructA.from_json,
                to_json=SandBossStructA.to_json,
            ),
        },
    )
    sand_boss_struct_a_0x0cf8c54c: SandBossStructA = dataclasses.field(
        default_factory=SandBossStructA,
        metadata={
            "reflection": FieldReflection[SandBossStructA](
                SandBossStructA,
                id=0x0CF8C54C,
                original_name="SandBossStructA",
                from_json=SandBossStructA.from_json,
                to_json=SandBossStructA.to_json,
            ),
        },
    )
    model_with_tail_armor: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBBD84681, original_name="Model With Tail Armor"),
        },
    )
    skin_for_armored_tail: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDF6DA1A2, original_name="Skin For Armored Tail"),
        },
    )
    damage_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xB7ECDCF9,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    stampede_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x844ED79C,
                original_name="StampedeVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    suck_air_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x77210167,
                original_name="SuckAirVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 27:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72124842
        scannable_info1 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE34D7C49
        command_index = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE47262F5
        cracked_sphere1 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62E6105B
        cracked_sphere2 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9BAC3FE
        cracked_sphere3 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19C91AAA
        snap_jaw_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58889364
        spit_out_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF88FE4F
        unknown_0xbf88fe4f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74C702B3
        unknown_0x74c702b3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35EE175D
        dark_beam_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94C2150F
        dark_beam_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 1, "di_damage": 20.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B42DDDF
        unknown_0x2b42dddf = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1562E0D6
        unknown_0x1562e0d6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD0DB2574
        unknown_0xd0db2574 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1AED43D
        suck_air_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3055DD0E
        suck_morphball_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6F135965
        spit_morphball_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC49086D9
        part = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95371A32
        unknown_struct40 = UnknownStruct40.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7619E561
        unknown_struct41 = UnknownStruct41.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B452A19
        sand_boss_struct_a_0x8b452a19 = SandBossStructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0CF8C54C
        sand_boss_struct_a_0x0cf8c54c = SandBossStructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBBD84681
        model_with_tail_armor = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF6DA1A2
        skin_for_armored_tail = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7ECDCF9
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x844ED79C
        stampede_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77210167
        suck_air_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            scannable_info1,
            command_index,
            cracked_sphere1,
            cracked_sphere2,
            cracked_sphere3,
            snap_jaw_damage,
            spit_out_damage,
            unknown_0xbf88fe4f,
            unknown_0x74c702b3,
            dark_beam_projectile,
            dark_beam_damage,
            unknown_0x2b42dddf,
            unknown_0x1562e0d6,
            unknown_0xd0db2574,
            suck_air_time,
            suck_morphball_range,
            spit_morphball_time,
            part,
            unknown_struct40,
            unknown_struct41,
            sand_boss_struct_a_0x8b452a19,
            sand_boss_struct_a_0x0cf8c54c,
            model_with_tail_armor,
            skin_for_armored_tail,
            damage_vulnerability,
            stampede_vulnerability,
            suck_air_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1b")  # 27 properties

        data.write(b"r\x12HB")  # 0x72124842
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scannable_info1))

        data.write(b"\xe3M|I")  # 0xe34d7c49
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.command_index))

        data.write(b"\xe4rb\xf5")  # 0xe47262f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.cracked_sphere1))

        data.write(b"b\xe6\x10[")  # 0x62e6105b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.cracked_sphere2))

        data.write(b"\xa9\xba\xc3\xfe")  # 0xa9bac3fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.cracked_sphere3))

        data.write(b"\x19\xc9\x1a\xaa")  # 0x19c91aaa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.snap_jaw_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X\x88\x93d")  # 0x58889364
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spit_out_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbf\x88\xfeO")  # 0xbf88fe4f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbf88fe4f))

        data.write(b"t\xc7\x02\xb3")  # 0x74c702b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x74c702b3))

        data.write(b"5\xee\x17]")  # 0x35ee175d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dark_beam_projectile))

        data.write(b"\x94\xc2\x15\x0f")  # 0x94c2150f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dark_beam_damage.to_stream(
            data, game, default_override={"di_weapon_type": 1, "di_damage": 20.0, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+B\xdd\xdf")  # 0x2b42dddf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2b42dddf))

        data.write(b"\x15b\xe0\xd6")  # 0x1562e0d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1562e0d6))

        data.write(b"\xd0\xdb%t")  # 0xd0db2574
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd0db2574))

        data.write(b"\xf1\xae\xd4=")  # 0xf1aed43d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.suck_air_time))

        data.write(b"0U\xdd\x0e")  # 0x3055dd0e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.suck_morphball_range))

        data.write(b"o\x13Ye")  # 0x6f135965
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.spit_morphball_time))

        data.write(b"\xc4\x90\x86\xd9")  # 0xc49086d9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b"\x957\x1a2")  # 0x95371a32
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct40.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"v\x19\xe5a")  # 0x7619e561
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct41.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8bE*\x19")  # 0x8b452a19
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sand_boss_struct_a_0x8b452a19.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0c\xf8\xc5L")  # 0xcf8c54c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sand_boss_struct_a_0x0cf8c54c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbb\xd8F\x81")  # 0xbbd84681
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.model_with_tail_armor))

        data.write(b"\xdfm\xa1\xa2")  # 0xdf6da1a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.skin_for_armored_tail))

        data.write(b"\xb7\xec\xdc\xf9")  # 0xb7ecdcf9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x84N\xd7\x9c")  # 0x844ed79c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stampede_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w!\x01g")  # 0x77210167
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.suck_air_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SandBossDataJson", data)
        return cls(
            scannable_info1=json_data["scannable_info1"],
            command_index=json_data["command_index"],
            cracked_sphere1=json_data["cracked_sphere1"],
            cracked_sphere2=json_data["cracked_sphere2"],
            cracked_sphere3=json_data["cracked_sphere3"],
            snap_jaw_damage=DamageInfo.from_json(json_data["snap_jaw_damage"]),
            spit_out_damage=DamageInfo.from_json(json_data["spit_out_damage"]),
            unknown_0xbf88fe4f=json_data["unknown_0xbf88fe4f"],
            unknown_0x74c702b3=json_data["unknown_0x74c702b3"],
            dark_beam_projectile=json_data["dark_beam_projectile"],
            dark_beam_damage=DamageInfo.from_json(json_data["dark_beam_damage"]),
            unknown_0x2b42dddf=json_data["unknown_0x2b42dddf"],
            unknown_0x1562e0d6=json_data["unknown_0x1562e0d6"],
            unknown_0xd0db2574=json_data["unknown_0xd0db2574"],
            suck_air_time=json_data["suck_air_time"],
            suck_morphball_range=json_data["suck_morphball_range"],
            spit_morphball_time=json_data["spit_morphball_time"],
            part=json_data["part"],
            unknown_struct40=UnknownStruct40.from_json(json_data["unknown_struct40"]),
            unknown_struct41=UnknownStruct41.from_json(json_data["unknown_struct41"]),
            sand_boss_struct_a_0x8b452a19=SandBossStructA.from_json(json_data["sand_boss_struct_a_0x8b452a19"]),
            sand_boss_struct_a_0x0cf8c54c=SandBossStructA.from_json(json_data["sand_boss_struct_a_0x0cf8c54c"]),
            model_with_tail_armor=json_data["model_with_tail_armor"],
            skin_for_armored_tail=json_data["skin_for_armored_tail"],
            damage_vulnerability=DamageVulnerability.from_json(json_data["damage_vulnerability"]),
            stampede_vulnerability=DamageVulnerability.from_json(json_data["stampede_vulnerability"]),
            suck_air_vulnerability=DamageVulnerability.from_json(json_data["suck_air_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scannable_info1": self.scannable_info1,
            "command_index": self.command_index,
            "cracked_sphere1": self.cracked_sphere1,
            "cracked_sphere2": self.cracked_sphere2,
            "cracked_sphere3": self.cracked_sphere3,
            "snap_jaw_damage": self.snap_jaw_damage.to_json(),
            "spit_out_damage": self.spit_out_damage.to_json(),
            "unknown_0xbf88fe4f": self.unknown_0xbf88fe4f,
            "unknown_0x74c702b3": self.unknown_0x74c702b3,
            "dark_beam_projectile": self.dark_beam_projectile,
            "dark_beam_damage": self.dark_beam_damage.to_json(),
            "unknown_0x2b42dddf": self.unknown_0x2b42dddf,
            "unknown_0x1562e0d6": self.unknown_0x1562e0d6,
            "unknown_0xd0db2574": self.unknown_0xd0db2574,
            "suck_air_time": self.suck_air_time,
            "suck_morphball_range": self.suck_morphball_range,
            "spit_morphball_time": self.spit_morphball_time,
            "part": self.part,
            "unknown_struct40": self.unknown_struct40.to_json(),
            "unknown_struct41": self.unknown_struct41.to_json(),
            "sand_boss_struct_a_0x8b452a19": self.sand_boss_struct_a_0x8b452a19.to_json(),
            "sand_boss_struct_a_0x0cf8c54c": self.sand_boss_struct_a_0x0cf8c54c.to_json(),
            "model_with_tail_armor": self.model_with_tail_armor,
            "skin_for_armored_tail": self.skin_for_armored_tail,
            "damage_vulnerability": self.damage_vulnerability.to_json(),
            "stampede_vulnerability": self.stampede_vulnerability.to_json(),
            "suck_air_vulnerability": self.suck_air_vulnerability.to_json(),
        }

    def _dependencies_for_scannable_info1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info1)

    def _dependencies_for_cracked_sphere1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cracked_sphere1)

    def _dependencies_for_cracked_sphere2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cracked_sphere2)

    def _dependencies_for_cracked_sphere3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cracked_sphere3)

    def _dependencies_for_dark_beam_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_beam_projectile)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def _dependencies_for_model_with_tail_armor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model_with_tail_armor)

    def _dependencies_for_skin_for_armored_tail(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.skin_for_armored_tail)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_scannable_info1, "scannable_info1", "AssetId"),
            (self._dependencies_for_cracked_sphere1, "cracked_sphere1", "AssetId"),
            (self._dependencies_for_cracked_sphere2, "cracked_sphere2", "AssetId"),
            (self._dependencies_for_cracked_sphere3, "cracked_sphere3", "AssetId"),
            (self._dependencies_for_dark_beam_projectile, "dark_beam_projectile", "AssetId"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self.unknown_struct40.dependencies_for, "unknown_struct40", "UnknownStruct40"),
            (self.unknown_struct41.dependencies_for, "unknown_struct41", "UnknownStruct41"),
            (self.sand_boss_struct_a_0x8b452a19.dependencies_for, "sand_boss_struct_a_0x8b452a19", "SandBossStructA"),
            (self.sand_boss_struct_a_0x0cf8c54c.dependencies_for, "sand_boss_struct_a_0x0cf8c54c", "SandBossStructA"),
            (self._dependencies_for_model_with_tail_armor, "model_with_tail_armor", "AssetId"),
            (self._dependencies_for_skin_for_armored_tail, "skin_for_armored_tail", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SandBossData.{field_name} ({field_type}): {e}")


def _decode_snap_jaw_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
    )


def _decode_spit_out_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
    )


def _decode_dark_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 1, "di_damage": 20.0, "di_knock_back_power": 10.0},
    )


def _decode_unknown_struct40(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct40:
    return UnknownStruct40.from_stream(data, game, property_size)


def _decode_unknown_struct41(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct41:
    return UnknownStruct41.from_stream(data, game, property_size)


def _decode_sand_boss_struct_a_0x8b452a19(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossStructA:
    return SandBossStructA.from_stream(data, game, property_size)


def _decode_sand_boss_struct_a_0x0cf8c54c(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossStructA:
    return SandBossStructA.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_stampede_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_suck_air_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x72124842: ("scannable_info1", structs.decode_BIG_L),
    0xE34D7C49: ("command_index", structs.decode_BIG_l),
    0xE47262F5: ("cracked_sphere1", structs.decode_BIG_L),
    0x62E6105B: ("cracked_sphere2", structs.decode_BIG_L),
    0xA9BAC3FE: ("cracked_sphere3", structs.decode_BIG_L),
    0x19C91AAA: ("snap_jaw_damage", _decode_snap_jaw_damage),
    0x58889364: ("spit_out_damage", _decode_spit_out_damage),
    0xBF88FE4F: ("unknown_0xbf88fe4f", structs.decode_BIG_f),
    0x74C702B3: ("unknown_0x74c702b3", structs.decode_BIG_f),
    0x35EE175D: ("dark_beam_projectile", structs.decode_BIG_L),
    0x94C2150F: ("dark_beam_damage", _decode_dark_beam_damage),
    0x2B42DDDF: ("unknown_0x2b42dddf", structs.decode_BIG_f),
    0x1562E0D6: ("unknown_0x1562e0d6", structs.decode_BIG_f),
    0xD0DB2574: ("unknown_0xd0db2574", structs.decode_BIG_f),
    0xF1AED43D: ("suck_air_time", structs.decode_BIG_f),
    0x3055DD0E: ("suck_morphball_range", structs.decode_BIG_f),
    0x6F135965: ("spit_morphball_time", structs.decode_BIG_f),
    0xC49086D9: ("part", structs.decode_BIG_L),
    0x95371A32: ("unknown_struct40", _decode_unknown_struct40),
    0x7619E561: ("unknown_struct41", _decode_unknown_struct41),
    0x8B452A19: ("sand_boss_struct_a_0x8b452a19", _decode_sand_boss_struct_a_0x8b452a19),
    0x0CF8C54C: ("sand_boss_struct_a_0x0cf8c54c", _decode_sand_boss_struct_a_0x0cf8c54c),
    0xBBD84681: ("model_with_tail_armor", structs.decode_BIG_L),
    0xDF6DA1A2: ("skin_for_armored_tail", structs.decode_BIG_L),
    0xB7ECDCF9: ("damage_vulnerability", _decode_damage_vulnerability),
    0x844ED79C: ("stampede_vulnerability", _decode_stampede_vulnerability),
    0x77210167: ("suck_air_vulnerability", _decode_suck_air_vulnerability),
}
