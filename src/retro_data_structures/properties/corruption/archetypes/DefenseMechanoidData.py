# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class DefenseMechanoidDataJson(typing_extensions.TypedDict):
        unknown_0xd41f1468: bool
        unknown_0x77259804: bool
        unknown_0xec877653: float
        unknown_0x09555889: float
        unknown_0x5ceca2a6: float
        jammer_antenna_vulnerability: json_util.JsonObject
        command_core_vulnerability: json_util.JsonObject
        unknown_0x6735f19b: float
        unknown_0x0a9689e2: float
        unknown_0xa65f4b32: float
        unknown_0x78871ce9: float
        min_jump_interval: float
        max_jump_interval: float
        min_missile_interval: float
        max_missile_interval: float
        min_taunt_interval: float
        max_taunt_interval: float
        min_distance_adjust_interval: float
        max_distance_adjust_interval: float
        unknown_0xbc801a3e: float
        unknown_0xc060b62b: float
        unknown_0x2766a717: float
        unknown_0x29ea27db: float
        missile_damage: json_util.JsonObject
        huge_missile_damage: json_util.JsonObject
        pulse_shockwave: json_util.JsonObject
        seeker_bomb_damage: json_util.JsonObject


@dataclasses.dataclass()
class DefenseMechanoidData(BaseProperty):
    unknown_0xd41f1468: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xD41F1468, original_name="Unknown"),
        },
    )
    unknown_0x77259804: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x77259804, original_name="Unknown"),
        },
    )
    unknown_0xec877653: float = dataclasses.field(
        default=200.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC877653, original_name="Unknown"),
        },
    )
    unknown_0x09555889: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x09555889, original_name="Unknown"),
        },
    )
    unknown_0x5ceca2a6: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5CECA2A6, original_name="Unknown"),
        },
    )
    jammer_antenna_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xFF8C4056,
                original_name="JammerAntennaVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    command_core_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x99BBC2DE,
                original_name="CommandCoreVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0x6735f19b: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6735F19B, original_name="Unknown"),
        },
    )
    unknown_0x0a9689e2: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0A9689E2, original_name="Unknown"),
        },
    )
    unknown_0xa65f4b32: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA65F4B32, original_name="Unknown"),
        },
    )
    unknown_0x78871ce9: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78871CE9, original_name="Unknown"),
        },
    )
    min_jump_interval: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCDF4D755, original_name="MinJumpInterval"),
        },
    )
    max_jump_interval: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE48A2A4D, original_name="MaxJumpInterval"),
        },
    )
    min_missile_interval: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED223686, original_name="MinMissileInterval"),
        },
    )
    max_missile_interval: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE9B807AC, original_name="MaxMissileInterval"),
        },
    )
    min_taunt_interval: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x33A298CD, original_name="MinTauntInterval"),
        },
    )
    max_taunt_interval: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x20E77E66, original_name="MaxTauntInterval"),
        },
    )
    min_distance_adjust_interval: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAAFE3E43, original_name="MinDistanceAdjustInterval"),
        },
    )
    max_distance_adjust_interval: float = dataclasses.field(
        default=12.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1AC1247F, original_name="MaxDistanceAdjustInterval"),
        },
    )
    unknown_0xbc801a3e: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC801A3E, original_name="Unknown"),
        },
    )
    unknown_0xc060b62b: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC060B62B, original_name="Unknown"),
        },
    )
    unknown_0x2766a717: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2766A717, original_name="Unknown"),
        },
    )
    unknown_0x29ea27db: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x29EA27DB, original_name="Unknown"),
        },
    )
    missile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x258CFB4D,
                original_name="MissileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    huge_missile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xF4D99ABC,
                original_name="HugeMissileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    pulse_shockwave: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0xE17C3B6E,
                original_name="PulseShockwave",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    seeker_bomb_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x59550952,
                original_name="SeekerBombDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
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
        assert property_id == 0xD41F1468
        unknown_0xd41f1468 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77259804
        unknown_0x77259804 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC877653
        unknown_0xec877653 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09555889
        unknown_0x09555889 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5CECA2A6
        unknown_0x5ceca2a6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF8C4056
        jammer_antenna_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x99BBC2DE
        command_core_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6735F19B
        unknown_0x6735f19b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A9689E2
        unknown_0x0a9689e2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA65F4B32
        unknown_0xa65f4b32 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78871CE9
        unknown_0x78871ce9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCDF4D755
        min_jump_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE48A2A4D
        max_jump_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED223686
        min_missile_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9B807AC
        max_missile_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33A298CD
        min_taunt_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20E77E66
        max_taunt_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAAFE3E43
        min_distance_adjust_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AC1247F
        max_distance_adjust_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC801A3E
        unknown_0xbc801a3e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC060B62B
        unknown_0xc060b62b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2766A717
        unknown_0x2766a717 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29EA27DB
        unknown_0x29ea27db = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x258CFB4D
        missile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4D99ABC
        huge_missile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE17C3B6E
        pulse_shockwave = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59550952
        seeker_bomb_damage = DamageInfo.from_stream(data, game, property_size)

        return cls(
            unknown_0xd41f1468,
            unknown_0x77259804,
            unknown_0xec877653,
            unknown_0x09555889,
            unknown_0x5ceca2a6,
            jammer_antenna_vulnerability,
            command_core_vulnerability,
            unknown_0x6735f19b,
            unknown_0x0a9689e2,
            unknown_0xa65f4b32,
            unknown_0x78871ce9,
            min_jump_interval,
            max_jump_interval,
            min_missile_interval,
            max_missile_interval,
            min_taunt_interval,
            max_taunt_interval,
            min_distance_adjust_interval,
            max_distance_adjust_interval,
            unknown_0xbc801a3e,
            unknown_0xc060b62b,
            unknown_0x2766a717,
            unknown_0x29ea27db,
            missile_damage,
            huge_missile_damage,
            pulse_shockwave,
            seeker_bomb_damage,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1b")  # 27 properties

        data.write(b"\xd4\x1f\x14h")  # 0xd41f1468
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xd41f1468))

        data.write(b"w%\x98\x04")  # 0x77259804
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x77259804))

        data.write(b"\xec\x87vS")  # 0xec877653
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xec877653))

        data.write(b"\tUX\x89")  # 0x9555889
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x09555889))

        data.write(b"\\\xec\xa2\xa6")  # 0x5ceca2a6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5ceca2a6))

        data.write(b"\xff\x8c@V")  # 0xff8c4056
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.jammer_antenna_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x99\xbb\xc2\xde")  # 0x99bbc2de
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.command_core_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"g5\xf1\x9b")  # 0x6735f19b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6735f19b))

        data.write(b"\n\x96\x89\xe2")  # 0xa9689e2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0a9689e2))

        data.write(b"\xa6_K2")  # 0xa65f4b32
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa65f4b32))

        data.write(b"x\x87\x1c\xe9")  # 0x78871ce9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x78871ce9))

        data.write(b"\xcd\xf4\xd7U")  # 0xcdf4d755
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_jump_interval))

        data.write(b"\xe4\x8a*M")  # 0xe48a2a4d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_jump_interval))

        data.write(b'\xed"6\x86')  # 0xed223686
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_missile_interval))

        data.write(b"\xe9\xb8\x07\xac")  # 0xe9b807ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_missile_interval))

        data.write(b"3\xa2\x98\xcd")  # 0x33a298cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_taunt_interval))

        data.write(b" \xe7~f")  # 0x20e77e66
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_taunt_interval))

        data.write(b"\xaa\xfe>C")  # 0xaafe3e43
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_distance_adjust_interval))

        data.write(b"\x1a\xc1$\x7f")  # 0x1ac1247f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_distance_adjust_interval))

        data.write(b"\xbc\x80\x1a>")  # 0xbc801a3e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbc801a3e))

        data.write(b"\xc0`\xb6+")  # 0xc060b62b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc060b62b))

        data.write(b"'f\xa7\x17")  # 0x2766a717
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2766a717))

        data.write(b")\xea'\xdb")  # 0x29ea27db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x29ea27db))

        data.write(b"%\x8c\xfbM")  # 0x258cfb4d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4\xd9\x9a\xbc")  # 0xf4d99abc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.huge_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe1|;n")  # 0xe17c3b6e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.pulse_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"YU\tR")  # 0x59550952
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.seeker_bomb_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DefenseMechanoidDataJson", data)
        return cls(
            unknown_0xd41f1468=json_data["unknown_0xd41f1468"],
            unknown_0x77259804=json_data["unknown_0x77259804"],
            unknown_0xec877653=json_data["unknown_0xec877653"],
            unknown_0x09555889=json_data["unknown_0x09555889"],
            unknown_0x5ceca2a6=json_data["unknown_0x5ceca2a6"],
            jammer_antenna_vulnerability=DamageVulnerability.from_json(json_data["jammer_antenna_vulnerability"]),
            command_core_vulnerability=DamageVulnerability.from_json(json_data["command_core_vulnerability"]),
            unknown_0x6735f19b=json_data["unknown_0x6735f19b"],
            unknown_0x0a9689e2=json_data["unknown_0x0a9689e2"],
            unknown_0xa65f4b32=json_data["unknown_0xa65f4b32"],
            unknown_0x78871ce9=json_data["unknown_0x78871ce9"],
            min_jump_interval=json_data["min_jump_interval"],
            max_jump_interval=json_data["max_jump_interval"],
            min_missile_interval=json_data["min_missile_interval"],
            max_missile_interval=json_data["max_missile_interval"],
            min_taunt_interval=json_data["min_taunt_interval"],
            max_taunt_interval=json_data["max_taunt_interval"],
            min_distance_adjust_interval=json_data["min_distance_adjust_interval"],
            max_distance_adjust_interval=json_data["max_distance_adjust_interval"],
            unknown_0xbc801a3e=json_data["unknown_0xbc801a3e"],
            unknown_0xc060b62b=json_data["unknown_0xc060b62b"],
            unknown_0x2766a717=json_data["unknown_0x2766a717"],
            unknown_0x29ea27db=json_data["unknown_0x29ea27db"],
            missile_damage=DamageInfo.from_json(json_data["missile_damage"]),
            huge_missile_damage=DamageInfo.from_json(json_data["huge_missile_damage"]),
            pulse_shockwave=ShockWaveInfo.from_json(json_data["pulse_shockwave"]),
            seeker_bomb_damage=DamageInfo.from_json(json_data["seeker_bomb_damage"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xd41f1468": self.unknown_0xd41f1468,
            "unknown_0x77259804": self.unknown_0x77259804,
            "unknown_0xec877653": self.unknown_0xec877653,
            "unknown_0x09555889": self.unknown_0x09555889,
            "unknown_0x5ceca2a6": self.unknown_0x5ceca2a6,
            "jammer_antenna_vulnerability": self.jammer_antenna_vulnerability.to_json(),
            "command_core_vulnerability": self.command_core_vulnerability.to_json(),
            "unknown_0x6735f19b": self.unknown_0x6735f19b,
            "unknown_0x0a9689e2": self.unknown_0x0a9689e2,
            "unknown_0xa65f4b32": self.unknown_0xa65f4b32,
            "unknown_0x78871ce9": self.unknown_0x78871ce9,
            "min_jump_interval": self.min_jump_interval,
            "max_jump_interval": self.max_jump_interval,
            "min_missile_interval": self.min_missile_interval,
            "max_missile_interval": self.max_missile_interval,
            "min_taunt_interval": self.min_taunt_interval,
            "max_taunt_interval": self.max_taunt_interval,
            "min_distance_adjust_interval": self.min_distance_adjust_interval,
            "max_distance_adjust_interval": self.max_distance_adjust_interval,
            "unknown_0xbc801a3e": self.unknown_0xbc801a3e,
            "unknown_0xc060b62b": self.unknown_0xc060b62b,
            "unknown_0x2766a717": self.unknown_0x2766a717,
            "unknown_0x29ea27db": self.unknown_0x29ea27db,
            "missile_damage": self.missile_damage.to_json(),
            "huge_missile_damage": self.huge_missile_damage.to_json(),
            "pulse_shockwave": self.pulse_shockwave.to_json(),
            "seeker_bomb_damage": self.seeker_bomb_damage.to_json(),
        }


def _decode_jammer_antenna_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_command_core_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_huge_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_pulse_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_seeker_bomb_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD41F1468: ("unknown_0xd41f1468", structs.decode_BIG_bool_),
    0x77259804: ("unknown_0x77259804", structs.decode_BIG_bool_),
    0xEC877653: ("unknown_0xec877653", structs.decode_BIG_f),
    0x09555889: ("unknown_0x09555889", structs.decode_BIG_f),
    0x5CECA2A6: ("unknown_0x5ceca2a6", structs.decode_BIG_f),
    0xFF8C4056: ("jammer_antenna_vulnerability", _decode_jammer_antenna_vulnerability),
    0x99BBC2DE: ("command_core_vulnerability", _decode_command_core_vulnerability),
    0x6735F19B: ("unknown_0x6735f19b", structs.decode_BIG_f),
    0x0A9689E2: ("unknown_0x0a9689e2", structs.decode_BIG_f),
    0xA65F4B32: ("unknown_0xa65f4b32", structs.decode_BIG_f),
    0x78871CE9: ("unknown_0x78871ce9", structs.decode_BIG_f),
    0xCDF4D755: ("min_jump_interval", structs.decode_BIG_f),
    0xE48A2A4D: ("max_jump_interval", structs.decode_BIG_f),
    0xED223686: ("min_missile_interval", structs.decode_BIG_f),
    0xE9B807AC: ("max_missile_interval", structs.decode_BIG_f),
    0x33A298CD: ("min_taunt_interval", structs.decode_BIG_f),
    0x20E77E66: ("max_taunt_interval", structs.decode_BIG_f),
    0xAAFE3E43: ("min_distance_adjust_interval", structs.decode_BIG_f),
    0x1AC1247F: ("max_distance_adjust_interval", structs.decode_BIG_f),
    0xBC801A3E: ("unknown_0xbc801a3e", structs.decode_BIG_f),
    0xC060B62B: ("unknown_0xc060b62b", structs.decode_BIG_f),
    0x2766A717: ("unknown_0x2766a717", structs.decode_BIG_f),
    0x29EA27DB: ("unknown_0x29ea27db", structs.decode_BIG_f),
    0x258CFB4D: ("missile_damage", _decode_missile_damage),
    0xF4D99ABC: ("huge_missile_damage", _decode_huge_missile_damage),
    0xE17C3B6E: ("pulse_shockwave", _decode_pulse_shockwave),
    0x59550952: ("seeker_bomb_damage", _decode_seeker_bomb_damage),
}
