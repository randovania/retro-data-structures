# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.archetypes.UnknownStruct42 import UnknownStruct42
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct43Json(typing_extensions.TypedDict):
        unknown_0xbd80fd94: int
        max_linear_velocity: float
        max_turn_speed: float
        scanning_turn_speed: float
        unknown_0xe32fcae9: float
        unknown_0xc5e0b92c: float
        unknown_0xc17a8806: float
        unknown_0xe75bae9e: int
        laser_pulse_projectile: int
        laser_pulse_damage: json_util.JsonObject
        unknown_0xeda45014: int
        unknown_0x7dd740fe: int
        dodge_chance: float
        reset_shield_time: float
        split_destroyed_priority: float
        laser_sweep_turn_speed: float
        laser_sweep_damage: json_util.JsonObject
        laser_sweep_beam_info: json_util.JsonObject
        unknown_struct42: json_util.JsonObject
        sound_laser_sweep: int
        sound_laser_charge_up: int
        sound_docking: int
        sound_scanning: int
        sound_light_shield: int
        sound_dark_shield: int
        sound_shield_on: int
        ing_possession_data: json_util.JsonObject
        light_shield_vulnerability: json_util.JsonObject
        dark_shield_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct43(BaseProperty):
    unknown_0xbd80fd94: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBD80FD94, original_name="Unknown"),
        },
    )
    max_linear_velocity: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00D74FC3, original_name="MaxLinearVelocity"),
        },
    )
    max_turn_speed: float = dataclasses.field(
        default=720.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0B5C3C1A, original_name="MaxTurnSpeed"),
        },
    )
    scanning_turn_speed: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA0B3E1BE, original_name="ScanningTurnSpeed"),
        },
    )
    unknown_0xe32fcae9: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE32FCAE9, original_name="Unknown"),
        },
    )
    unknown_0xc5e0b92c: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC5E0B92C, original_name="Unknown"),
        },
    )
    unknown_0xc17a8806: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC17A8806, original_name="Unknown"),
        },
    )
    unknown_0xe75bae9e: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE75BAE9E, original_name="Unknown"),
        },
    )
    laser_pulse_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4D77B7AA, original_name="LaserPulseProjectile"),
        },
    )
    laser_pulse_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xB763EB10,
                original_name="LaserPulseDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xeda45014: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEDA45014, original_name="Unknown"),
        },
    )
    unknown_0x7dd740fe: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7DD740FE, original_name="Unknown"),
        },
    )
    dodge_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47BE3298, original_name="DodgeChance"),
        },
    )
    reset_shield_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD3DEC6DC, original_name="ResetShieldTime"),
        },
    )
    split_destroyed_priority: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xECD9D92D, original_name="SplitDestroyedPriority"),
        },
    )
    laser_sweep_turn_speed: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5FF006D1, original_name="LaserSweepTurnSpeed"),
        },
    )
    laser_sweep_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x1BD017CE,
                original_name="LaserSweepDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    laser_sweep_beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x4A37C437,
                original_name="LaserSweepBeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    unknown_struct42: UnknownStruct42 = dataclasses.field(
        default_factory=UnknownStruct42,
        metadata={
            "reflection": FieldReflection[UnknownStruct42](
                UnknownStruct42,
                id=0x9EC51FE4,
                original_name="UnknownStruct42",
                from_json=UnknownStruct42.from_json,
                to_json=UnknownStruct42.to_json,
            ),
        },
    )
    sound_laser_sweep: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xEA307548, original_name="Sound_LaserSweep"),
        },
    )
    sound_laser_charge_up: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x3779BD93, original_name="Sound_LaserChargeUp"),
        },
    )
    sound_docking: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xC90DBDB4, original_name="Sound_Docking"),
        },
    )
    sound_scanning: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE7724802, original_name="Sound_Scanning"),
        },
    )
    sound_light_shield: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD4A06273, original_name="Sound_LightShield"),
        },
    )
    sound_dark_shield: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAFC20631, original_name="Sound_DarkShield"),
        },
    )
    sound_shield_on: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x2FF5A809, original_name="Sound_ShieldOn"),
        },
    )
    ing_possession_data: IngPossessionData = dataclasses.field(
        default_factory=IngPossessionData,
        metadata={
            "reflection": FieldReflection[IngPossessionData](
                IngPossessionData,
                id=0xE61748ED,
                original_name="IngPossessionData",
                from_json=IngPossessionData.from_json,
                to_json=IngPossessionData.to_json,
            ),
        },
    )
    light_shield_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x80A8EF3B,
                original_name="LightShieldVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    dark_shield_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xA21C90EA,
                original_name="DarkShieldVulnerability",
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
        if property_count != 29:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD80FD94
        unknown_0xbd80fd94 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00D74FC3
        max_linear_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B5C3C1A
        max_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA0B3E1BE
        scanning_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE32FCAE9
        unknown_0xe32fcae9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5E0B92C
        unknown_0xc5e0b92c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC17A8806
        unknown_0xc17a8806 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE75BAE9E
        unknown_0xe75bae9e = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D77B7AA
        laser_pulse_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB763EB10
        laser_pulse_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDA45014
        unknown_0xeda45014 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7DD740FE
        unknown_0x7dd740fe = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47BE3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3DEC6DC
        reset_shield_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xECD9D92D
        split_destroyed_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5FF006D1
        laser_sweep_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1BD017CE
        laser_sweep_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A37C437
        laser_sweep_beam_info = PlasmaBeamInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "length": 500.0,
                "expansion_speed": 4.0,
                "life_time": 1.0,
                "pulse_speed": 20.0,
                "shutdown_time": 0.25,
                "pulse_effect_scale": 2.0,
                "inner_color": Color(
                    r=0.49803900718688965, g=0.49803900718688965, b=0.49803900718688965, a=0.49803900718688965
                ),
                "outer_color": Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.49803900718688965),
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9EC51FE4
        unknown_struct42 = UnknownStruct42.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA307548
        sound_laser_sweep = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3779BD93
        sound_laser_charge_up = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC90DBDB4
        sound_docking = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7724802
        sound_scanning = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4A06273
        sound_light_shield = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAFC20631
        sound_dark_shield = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2FF5A809
        sound_shield_on = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE61748ED
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80A8EF3B
        light_shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA21C90EA
        dark_shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            unknown_0xbd80fd94,
            max_linear_velocity,
            max_turn_speed,
            scanning_turn_speed,
            unknown_0xe32fcae9,
            unknown_0xc5e0b92c,
            unknown_0xc17a8806,
            unknown_0xe75bae9e,
            laser_pulse_projectile,
            laser_pulse_damage,
            unknown_0xeda45014,
            unknown_0x7dd740fe,
            dodge_chance,
            reset_shield_time,
            split_destroyed_priority,
            laser_sweep_turn_speed,
            laser_sweep_damage,
            laser_sweep_beam_info,
            unknown_struct42,
            sound_laser_sweep,
            sound_laser_charge_up,
            sound_docking,
            sound_scanning,
            sound_light_shield,
            sound_dark_shield,
            sound_shield_on,
            ing_possession_data,
            light_shield_vulnerability,
            dark_shield_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1d")  # 29 properties

        data.write(b"\xbd\x80\xfd\x94")  # 0xbd80fd94
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xbd80fd94))

        data.write(b"\x00\xd7O\xc3")  # 0xd74fc3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_linear_velocity))

        data.write(b"\x0b\\<\x1a")  # 0xb5c3c1a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed))

        data.write(b"\xa0\xb3\xe1\xbe")  # 0xa0b3e1be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scanning_turn_speed))

        data.write(b"\xe3/\xca\xe9")  # 0xe32fcae9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe32fcae9))

        data.write(b"\xc5\xe0\xb9,")  # 0xc5e0b92c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc5e0b92c))

        data.write(b"\xc1z\x88\x06")  # 0xc17a8806
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc17a8806))

        data.write(b"\xe7[\xae\x9e")  # 0xe75bae9e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe75bae9e))

        data.write(b"Mw\xb7\xaa")  # 0x4d77b7aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.laser_pulse_projectile))

        data.write(b"\xb7c\xeb\x10")  # 0xb763eb10
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.laser_pulse_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\xa4P\x14")  # 0xeda45014
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xeda45014))

        data.write(b"}\xd7@\xfe")  # 0x7dd740fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7dd740fe))

        data.write(b"G\xbe2\x98")  # 0x47be3298
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b"\xd3\xde\xc6\xdc")  # 0xd3dec6dc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reset_shield_time))

        data.write(b"\xec\xd9\xd9-")  # 0xecd9d92d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.split_destroyed_priority))

        data.write(b"_\xf0\x06\xd1")  # 0x5ff006d1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.laser_sweep_turn_speed))

        data.write(b"\x1b\xd0\x17\xce")  # 0x1bd017ce
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.laser_sweep_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"J7\xc47")  # 0x4a37c437
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.laser_sweep_beam_info.to_stream(
            data,
            game,
            default_override={
                "length": 500.0,
                "expansion_speed": 4.0,
                "life_time": 1.0,
                "pulse_speed": 20.0,
                "shutdown_time": 0.25,
                "pulse_effect_scale": 2.0,
                "inner_color": Color(
                    r=0.49803900718688965, g=0.49803900718688965, b=0.49803900718688965, a=0.49803900718688965
                ),
                "outer_color": Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.49803900718688965),
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9e\xc5\x1f\xe4")  # 0x9ec51fe4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct42.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xea0uH")  # 0xea307548
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_laser_sweep))

        data.write(b"7y\xbd\x93")  # 0x3779bd93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_laser_charge_up))

        data.write(b"\xc9\r\xbd\xb4")  # 0xc90dbdb4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_docking))

        data.write(b"\xe7rH\x02")  # 0xe7724802
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_scanning))

        data.write(b"\xd4\xa0bs")  # 0xd4a06273
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_light_shield))

        data.write(b"\xaf\xc2\x061")  # 0xafc20631
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_dark_shield))

        data.write(b"/\xf5\xa8\t")  # 0x2ff5a809
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_shield_on))

        data.write(b"\xe6\x17H\xed")  # 0xe61748ed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x80\xa8\xef;")  # 0x80a8ef3b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.light_shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa2\x1c\x90\xea")  # 0xa21c90ea
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dark_shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct43Json", data)
        return cls(
            unknown_0xbd80fd94=json_data["unknown_0xbd80fd94"],
            max_linear_velocity=json_data["max_linear_velocity"],
            max_turn_speed=json_data["max_turn_speed"],
            scanning_turn_speed=json_data["scanning_turn_speed"],
            unknown_0xe32fcae9=json_data["unknown_0xe32fcae9"],
            unknown_0xc5e0b92c=json_data["unknown_0xc5e0b92c"],
            unknown_0xc17a8806=json_data["unknown_0xc17a8806"],
            unknown_0xe75bae9e=json_data["unknown_0xe75bae9e"],
            laser_pulse_projectile=json_data["laser_pulse_projectile"],
            laser_pulse_damage=DamageInfo.from_json(json_data["laser_pulse_damage"]),
            unknown_0xeda45014=json_data["unknown_0xeda45014"],
            unknown_0x7dd740fe=json_data["unknown_0x7dd740fe"],
            dodge_chance=json_data["dodge_chance"],
            reset_shield_time=json_data["reset_shield_time"],
            split_destroyed_priority=json_data["split_destroyed_priority"],
            laser_sweep_turn_speed=json_data["laser_sweep_turn_speed"],
            laser_sweep_damage=DamageInfo.from_json(json_data["laser_sweep_damage"]),
            laser_sweep_beam_info=PlasmaBeamInfo.from_json(json_data["laser_sweep_beam_info"]),
            unknown_struct42=UnknownStruct42.from_json(json_data["unknown_struct42"]),
            sound_laser_sweep=json_data["sound_laser_sweep"],
            sound_laser_charge_up=json_data["sound_laser_charge_up"],
            sound_docking=json_data["sound_docking"],
            sound_scanning=json_data["sound_scanning"],
            sound_light_shield=json_data["sound_light_shield"],
            sound_dark_shield=json_data["sound_dark_shield"],
            sound_shield_on=json_data["sound_shield_on"],
            ing_possession_data=IngPossessionData.from_json(json_data["ing_possession_data"]),
            light_shield_vulnerability=DamageVulnerability.from_json(json_data["light_shield_vulnerability"]),
            dark_shield_vulnerability=DamageVulnerability.from_json(json_data["dark_shield_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xbd80fd94": self.unknown_0xbd80fd94,
            "max_linear_velocity": self.max_linear_velocity,
            "max_turn_speed": self.max_turn_speed,
            "scanning_turn_speed": self.scanning_turn_speed,
            "unknown_0xe32fcae9": self.unknown_0xe32fcae9,
            "unknown_0xc5e0b92c": self.unknown_0xc5e0b92c,
            "unknown_0xc17a8806": self.unknown_0xc17a8806,
            "unknown_0xe75bae9e": self.unknown_0xe75bae9e,
            "laser_pulse_projectile": self.laser_pulse_projectile,
            "laser_pulse_damage": self.laser_pulse_damage.to_json(),
            "unknown_0xeda45014": self.unknown_0xeda45014,
            "unknown_0x7dd740fe": self.unknown_0x7dd740fe,
            "dodge_chance": self.dodge_chance,
            "reset_shield_time": self.reset_shield_time,
            "split_destroyed_priority": self.split_destroyed_priority,
            "laser_sweep_turn_speed": self.laser_sweep_turn_speed,
            "laser_sweep_damage": self.laser_sweep_damage.to_json(),
            "laser_sweep_beam_info": self.laser_sweep_beam_info.to_json(),
            "unknown_struct42": self.unknown_struct42.to_json(),
            "sound_laser_sweep": self.sound_laser_sweep,
            "sound_laser_charge_up": self.sound_laser_charge_up,
            "sound_docking": self.sound_docking,
            "sound_scanning": self.sound_scanning,
            "sound_light_shield": self.sound_light_shield,
            "sound_dark_shield": self.sound_dark_shield,
            "sound_shield_on": self.sound_shield_on,
            "ing_possession_data": self.ing_possession_data.to_json(),
            "light_shield_vulnerability": self.light_shield_vulnerability.to_json(),
            "dark_shield_vulnerability": self.dark_shield_vulnerability.to_json(),
        }

    def _dependencies_for_laser_pulse_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.laser_pulse_projectile)

    def _dependencies_for_sound_laser_sweep(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_laser_sweep)

    def _dependencies_for_sound_laser_charge_up(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_laser_charge_up)

    def _dependencies_for_sound_docking(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_docking)

    def _dependencies_for_sound_scanning(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_scanning)

    def _dependencies_for_sound_shield_on(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_shield_on)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_laser_pulse_projectile, "laser_pulse_projectile", "AssetId"),
            (self.laser_sweep_beam_info.dependencies_for, "laser_sweep_beam_info", "PlasmaBeamInfo"),
            (self._dependencies_for_sound_laser_sweep, "sound_laser_sweep", "int"),
            (self._dependencies_for_sound_laser_charge_up, "sound_laser_charge_up", "int"),
            (self._dependencies_for_sound_docking, "sound_docking", "int"),
            (self._dependencies_for_sound_scanning, "sound_scanning", "int"),
            (self._dependencies_for_sound_shield_on, "sound_shield_on", "int"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct43.{field_name} ({field_type}): {e}")


def _decode_laser_pulse_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0})


def _decode_laser_sweep_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0})


def _decode_laser_sweep_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "length": 500.0,
            "expansion_speed": 4.0,
            "life_time": 1.0,
            "pulse_speed": 20.0,
            "shutdown_time": 0.25,
            "pulse_effect_scale": 2.0,
            "inner_color": Color(
                r=0.49803900718688965, g=0.49803900718688965, b=0.49803900718688965, a=0.49803900718688965
            ),
            "outer_color": Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.49803900718688965),
        },
    )


def _decode_unknown_struct42(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct42:
    return UnknownStruct42.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


def _decode_light_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_dark_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xBD80FD94: ("unknown_0xbd80fd94", structs.decode_BIG_l),
    0x00D74FC3: ("max_linear_velocity", structs.decode_BIG_f),
    0x0B5C3C1A: ("max_turn_speed", structs.decode_BIG_f),
    0xA0B3E1BE: ("scanning_turn_speed", structs.decode_BIG_f),
    0xE32FCAE9: ("unknown_0xe32fcae9", structs.decode_BIG_f),
    0xC5E0B92C: ("unknown_0xc5e0b92c", structs.decode_BIG_f),
    0xC17A8806: ("unknown_0xc17a8806", structs.decode_BIG_f),
    0xE75BAE9E: ("unknown_0xe75bae9e", structs.decode_BIG_l),
    0x4D77B7AA: ("laser_pulse_projectile", structs.decode_BIG_L),
    0xB763EB10: ("laser_pulse_damage", _decode_laser_pulse_damage),
    0xEDA45014: ("unknown_0xeda45014", structs.decode_BIG_l),
    0x7DD740FE: ("unknown_0x7dd740fe", structs.decode_BIG_l),
    0x47BE3298: ("dodge_chance", structs.decode_BIG_f),
    0xD3DEC6DC: ("reset_shield_time", structs.decode_BIG_f),
    0xECD9D92D: ("split_destroyed_priority", structs.decode_BIG_f),
    0x5FF006D1: ("laser_sweep_turn_speed", structs.decode_BIG_f),
    0x1BD017CE: ("laser_sweep_damage", _decode_laser_sweep_damage),
    0x4A37C437: ("laser_sweep_beam_info", _decode_laser_sweep_beam_info),
    0x9EC51FE4: ("unknown_struct42", _decode_unknown_struct42),
    0xEA307548: ("sound_laser_sweep", structs.decode_BIG_l),
    0x3779BD93: ("sound_laser_charge_up", structs.decode_BIG_l),
    0xC90DBDB4: ("sound_docking", structs.decode_BIG_l),
    0xE7724802: ("sound_scanning", structs.decode_BIG_l),
    0xD4A06273: ("sound_light_shield", structs.decode_BIG_l),
    0xAFC20631: ("sound_dark_shield", structs.decode_BIG_l),
    0x2FF5A809: ("sound_shield_on", structs.decode_BIG_l),
    0xE61748ED: ("ing_possession_data", _decode_ing_possession_data),
    0x80A8EF3B: ("light_shield_vulnerability", _decode_light_shield_vulnerability),
    0xA21C90EA: ("dark_shield_vulnerability", _decode_dark_shield_vulnerability),
}
