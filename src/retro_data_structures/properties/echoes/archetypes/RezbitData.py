# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class RezbitDataJson(typing_extensions.TypedDict):
        hearing_radius: float
        unknown_0x4a6c4b40: float
        unknown_0x30d11671: float
        model_no_holos: int
        skin_no_holos: int
        shield_down_time: float
        unknown_0xffb37b81: float
        shield_up_time: float
        unknown_0x0d1d1648: float
        shield_explode_effect: int
        sound_shield_explode: json_util.JsonObject
        sound_shield_on: json_util.JsonObject
        sound_shield_off: json_util.JsonObject
        sound_flinch: json_util.JsonObject
        unknown_0xad120ad7: float
        unknown_0xe70ef8a3: float
        audio_playback_parms: json_util.JsonObject
        unknown_0x70e597d4: float
        unknown_0x94980a67: float
        unknown_0xd02f08b0: float
        unknown_0x53e84718: float
        unknown_0x6fbc1bf9: float
        energy_bolt_chance: float
        cutting_laser_chance: float
        unknown_0x075491ca: float
        unknown_0x54f2892e: float
        energy_bolt_damage: json_util.JsonObject
        energy_bolt_projectile: int
        energy_bolt_attack_duration: float
        unknown_0x28944183: float
        unknown_0xc7a69a59: float
        sound_energy_bolt: json_util.JsonObject
        unknown_0x9ede657f: float
        unknown_0xcd787d9b: float
        virus_attack_time: float
        virus_damage: json_util.JsonObject
        sound_always_ff: int
        sound_0xbb3f8a7b: int
        sound_0x601f846d: int
        unknown_0x64c7990d: float
        unknown_0x376181e9: float
        cutting_laser_damage: json_util.JsonObject
        sound_cutting_laser: json_util.JsonObject
        cutting_laser_beam_info: json_util.JsonObject
        shield_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class RezbitData(BaseProperty):
    hearing_radius: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED69488F, original_name="HearingRadius"),
        },
    )
    unknown_0x4a6c4b40: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4A6C4B40, original_name="Unknown"),
        },
    )
    unknown_0x30d11671: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x30D11671, original_name="Unknown"),
        },
    )
    model_no_holos: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC80BB6E4, original_name="Model (No Holos)"),
        },
    )
    skin_no_holos: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x05486319, original_name="Skin (No Holos)"),
        },
    )
    shield_down_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8980A469, original_name="ShieldDownTime"),
        },
    )
    unknown_0xffb37b81: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFFB37B81, original_name="Unknown"),
        },
    )
    shield_up_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x448579CD, original_name="ShieldUpTime"),
        },
    )
    unknown_0x0d1d1648: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D1D1648, original_name="Unknown"),
        },
    )
    shield_explode_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA41F75EF, original_name="ShieldExplodeEffect"),
        },
    )
    sound_shield_explode: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xA34E2D84,
                original_name="Sound_ShieldExplode",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_shield_on: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x8C598E41,
                original_name="Sound_ShieldOn",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_shield_off: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xF4491ED5,
                original_name="Sound_ShieldOff",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_flinch: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x7D832158,
                original_name="Sound_Flinch",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown_0xad120ad7: float = dataclasses.field(
        default=12.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD120AD7, original_name="Unknown"),
        },
    )
    unknown_0xe70ef8a3: float = dataclasses.field(
        default=1.2000000476837158,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE70EF8A3, original_name="Unknown"),
        },
    )
    audio_playback_parms: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x6BF2FF60,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown_0x70e597d4: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x70E597D4, original_name="Unknown"),
        },
    )
    unknown_0x94980a67: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x94980A67, original_name="Unknown"),
        },
    )
    unknown_0xd02f08b0: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD02F08B0, original_name="Unknown"),
        },
    )
    unknown_0x53e84718: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x53E84718, original_name="Unknown"),
        },
    )
    unknown_0x6fbc1bf9: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6FBC1BF9, original_name="Unknown"),
        },
    )
    energy_bolt_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDC276015, original_name="EnergyBoltChance"),
        },
    )
    cutting_laser_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2CA3E9CD, original_name="CuttingLaserChance"),
        },
    )
    unknown_0x075491ca: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x075491CA, original_name="Unknown"),
        },
    )
    unknown_0x54f2892e: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54F2892E, original_name="Unknown"),
        },
    )
    energy_bolt_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x600C5F40,
                original_name="EnergyBoltDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    energy_bolt_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2F11094B, original_name="EnergyBoltProjectile"),
        },
    )
    energy_bolt_attack_duration: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA1F350F5, original_name="EnergyBoltAttackDuration"),
        },
    )
    unknown_0x28944183: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x28944183, original_name="Unknown"),
        },
    )
    unknown_0xc7a69a59: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC7A69A59, original_name="Unknown"),
        },
    )
    sound_energy_bolt: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xBD3EB001,
                original_name="Sound_EnergyBolt",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown_0x9ede657f: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9EDE657F, original_name="Unknown"),
        },
    )
    unknown_0xcd787d9b: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD787D9B, original_name="Unknown"),
        },
    )
    virus_attack_time: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4A7D3B04, original_name="VirusAttackTime"),
        },
    )
    virus_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x16869B57,
                original_name="VirusDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_always_ff: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x973D7CC3, original_name="Sound? (Always FF)"),
        },
    )
    sound_0xbb3f8a7b: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xBB3F8A7B, original_name="Sound"),
        },
    )
    sound_0x601f846d: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x601F846D, original_name="Sound"),
        },
    )
    unknown_0x64c7990d: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x64C7990D, original_name="Unknown"),
        },
    )
    unknown_0x376181e9: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x376181E9, original_name="Unknown"),
        },
    )
    cutting_laser_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xBB58C088,
                original_name="CuttingLaserDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_cutting_laser: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x7864CA32,
                original_name="Sound_CuttingLaser",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    cutting_laser_beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x59764DBB,
                original_name="CuttingLaserBeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    shield_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xD34F1323,
                original_name="ShieldVulnerability",
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
        if property_count != 45:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED69488F
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A6C4B40
        unknown_0x4a6c4b40 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30D11671
        unknown_0x30d11671 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC80BB6E4
        model_no_holos = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05486319
        skin_no_holos = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8980A469
        shield_down_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFFB37B81
        unknown_0xffb37b81 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x448579CD
        shield_up_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D1D1648
        unknown_0x0d1d1648 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA41F75EF
        shield_explode_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA34E2D84
        sound_shield_explode = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8C598E41
        sound_shield_on = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4491ED5
        sound_shield_off = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D832158
        sound_flinch = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD120AD7
        unknown_0xad120ad7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE70EF8A3
        unknown_0xe70ef8a3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BF2FF60
        audio_playback_parms = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70E597D4
        unknown_0x70e597d4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94980A67
        unknown_0x94980a67 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD02F08B0
        unknown_0xd02f08b0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53E84718
        unknown_0x53e84718 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6FBC1BF9
        unknown_0x6fbc1bf9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC276015
        energy_bolt_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CA3E9CD
        cutting_laser_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x075491CA
        unknown_0x075491ca = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54F2892E
        unknown_0x54f2892e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x600C5F40
        energy_bolt_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F11094B
        energy_bolt_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1F350F5
        energy_bolt_attack_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28944183
        unknown_0x28944183 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7A69A59
        unknown_0xc7a69a59 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD3EB001
        sound_energy_bolt = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9EDE657F
        unknown_0x9ede657f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD787D9B
        unknown_0xcd787d9b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A7D3B04
        virus_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16869B57
        virus_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x973D7CC3
        sound_always_ff = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB3F8A7B
        sound_0xbb3f8a7b = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x601F846D
        sound_0x601f846d = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64C7990D
        unknown_0x64c7990d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x376181E9
        unknown_0x376181e9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB58C088
        cutting_laser_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7864CA32
        sound_cutting_laser = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59764DBB
        cutting_laser_beam_info = PlasmaBeamInfo.from_stream(
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
        assert property_id == 0xD34F1323
        shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            hearing_radius,
            unknown_0x4a6c4b40,
            unknown_0x30d11671,
            model_no_holos,
            skin_no_holos,
            shield_down_time,
            unknown_0xffb37b81,
            shield_up_time,
            unknown_0x0d1d1648,
            shield_explode_effect,
            sound_shield_explode,
            sound_shield_on,
            sound_shield_off,
            sound_flinch,
            unknown_0xad120ad7,
            unknown_0xe70ef8a3,
            audio_playback_parms,
            unknown_0x70e597d4,
            unknown_0x94980a67,
            unknown_0xd02f08b0,
            unknown_0x53e84718,
            unknown_0x6fbc1bf9,
            energy_bolt_chance,
            cutting_laser_chance,
            unknown_0x075491ca,
            unknown_0x54f2892e,
            energy_bolt_damage,
            energy_bolt_projectile,
            energy_bolt_attack_duration,
            unknown_0x28944183,
            unknown_0xc7a69a59,
            sound_energy_bolt,
            unknown_0x9ede657f,
            unknown_0xcd787d9b,
            virus_attack_time,
            virus_damage,
            sound_always_ff,
            sound_0xbb3f8a7b,
            sound_0x601f846d,
            unknown_0x64c7990d,
            unknown_0x376181e9,
            cutting_laser_damage,
            sound_cutting_laser,
            cutting_laser_beam_info,
            shield_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00-")  # 45 properties

        data.write(b"\xediH\x8f")  # 0xed69488f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b"JlK@")  # 0x4a6c4b40
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4a6c4b40))

        data.write(b"0\xd1\x16q")  # 0x30d11671
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x30d11671))

        data.write(b"\xc8\x0b\xb6\xe4")  # 0xc80bb6e4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.model_no_holos))

        data.write(b"\x05Hc\x19")  # 0x5486319
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.skin_no_holos))

        data.write(b"\x89\x80\xa4i")  # 0x8980a469
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shield_down_time))

        data.write(b"\xff\xb3{\x81")  # 0xffb37b81
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xffb37b81))

        data.write(b"D\x85y\xcd")  # 0x448579cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shield_up_time))

        data.write(b"\r\x1d\x16H")  # 0xd1d1648
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0d1d1648))

        data.write(b"\xa4\x1fu\xef")  # 0xa41f75ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shield_explode_effect))

        data.write(b"\xa3N-\x84")  # 0xa34e2d84
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_shield_explode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8cY\x8eA")  # 0x8c598e41
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_shield_on.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4I\x1e\xd5")  # 0xf4491ed5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_shield_off.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"}\x83!X")  # 0x7d832158
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_flinch.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xad\x12\n\xd7")  # 0xad120ad7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xad120ad7))

        data.write(b"\xe7\x0e\xf8\xa3")  # 0xe70ef8a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe70ef8a3))

        data.write(b"k\xf2\xff`")  # 0x6bf2ff60
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"p\xe5\x97\xd4")  # 0x70e597d4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x70e597d4))

        data.write(b"\x94\x98\ng")  # 0x94980a67
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x94980a67))

        data.write(b"\xd0/\x08\xb0")  # 0xd02f08b0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd02f08b0))

        data.write(b"S\xe8G\x18")  # 0x53e84718
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x53e84718))

        data.write(b"o\xbc\x1b\xf9")  # 0x6fbc1bf9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6fbc1bf9))

        data.write(b"\xdc'`\x15")  # 0xdc276015
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_chance))

        data.write(b",\xa3\xe9\xcd")  # 0x2ca3e9cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cutting_laser_chance))

        data.write(b"\x07T\x91\xca")  # 0x75491ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x075491ca))

        data.write(b"T\xf2\x89.")  # 0x54f2892e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x54f2892e))

        data.write(b"`\x0c_@")  # 0x600c5f40
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.energy_bolt_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"/\x11\tK")  # 0x2f11094b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.energy_bolt_projectile))

        data.write(b"\xa1\xf3P\xf5")  # 0xa1f350f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_attack_duration))

        data.write(b"(\x94A\x83")  # 0x28944183
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x28944183))

        data.write(b"\xc7\xa6\x9aY")  # 0xc7a69a59
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc7a69a59))

        data.write(b"\xbd>\xb0\x01")  # 0xbd3eb001
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_energy_bolt.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9e\xdee\x7f")  # 0x9ede657f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9ede657f))

        data.write(b"\xcdx}\x9b")  # 0xcd787d9b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd787d9b))

        data.write(b"J};\x04")  # 0x4a7d3b04
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.virus_attack_time))

        data.write(b"\x16\x86\x9bW")  # 0x16869b57
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.virus_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x97=|\xc3")  # 0x973d7cc3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_always_ff))

        data.write(b"\xbb?\x8a{")  # 0xbb3f8a7b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0xbb3f8a7b))

        data.write(b"`\x1f\x84m")  # 0x601f846d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0x601f846d))

        data.write(b"d\xc7\x99\r")  # 0x64c7990d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x64c7990d))

        data.write(b"7a\x81\xe9")  # 0x376181e9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x376181e9))

        data.write(b"\xbbX\xc0\x88")  # 0xbb58c088
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.cutting_laser_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"xd\xca2")  # 0x7864ca32
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_cutting_laser.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"YvM\xbb")  # 0x59764dbb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.cutting_laser_beam_info.to_stream(
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

        data.write(b"\xd3O\x13#")  # 0xd34f1323
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RezbitDataJson", data)
        return cls(
            hearing_radius=json_data["hearing_radius"],
            unknown_0x4a6c4b40=json_data["unknown_0x4a6c4b40"],
            unknown_0x30d11671=json_data["unknown_0x30d11671"],
            model_no_holos=json_data["model_no_holos"],
            skin_no_holos=json_data["skin_no_holos"],
            shield_down_time=json_data["shield_down_time"],
            unknown_0xffb37b81=json_data["unknown_0xffb37b81"],
            shield_up_time=json_data["shield_up_time"],
            unknown_0x0d1d1648=json_data["unknown_0x0d1d1648"],
            shield_explode_effect=json_data["shield_explode_effect"],
            sound_shield_explode=AudioPlaybackParms.from_json(json_data["sound_shield_explode"]),
            sound_shield_on=AudioPlaybackParms.from_json(json_data["sound_shield_on"]),
            sound_shield_off=AudioPlaybackParms.from_json(json_data["sound_shield_off"]),
            sound_flinch=AudioPlaybackParms.from_json(json_data["sound_flinch"]),
            unknown_0xad120ad7=json_data["unknown_0xad120ad7"],
            unknown_0xe70ef8a3=json_data["unknown_0xe70ef8a3"],
            audio_playback_parms=AudioPlaybackParms.from_json(json_data["audio_playback_parms"]),
            unknown_0x70e597d4=json_data["unknown_0x70e597d4"],
            unknown_0x94980a67=json_data["unknown_0x94980a67"],
            unknown_0xd02f08b0=json_data["unknown_0xd02f08b0"],
            unknown_0x53e84718=json_data["unknown_0x53e84718"],
            unknown_0x6fbc1bf9=json_data["unknown_0x6fbc1bf9"],
            energy_bolt_chance=json_data["energy_bolt_chance"],
            cutting_laser_chance=json_data["cutting_laser_chance"],
            unknown_0x075491ca=json_data["unknown_0x075491ca"],
            unknown_0x54f2892e=json_data["unknown_0x54f2892e"],
            energy_bolt_damage=DamageInfo.from_json(json_data["energy_bolt_damage"]),
            energy_bolt_projectile=json_data["energy_bolt_projectile"],
            energy_bolt_attack_duration=json_data["energy_bolt_attack_duration"],
            unknown_0x28944183=json_data["unknown_0x28944183"],
            unknown_0xc7a69a59=json_data["unknown_0xc7a69a59"],
            sound_energy_bolt=AudioPlaybackParms.from_json(json_data["sound_energy_bolt"]),
            unknown_0x9ede657f=json_data["unknown_0x9ede657f"],
            unknown_0xcd787d9b=json_data["unknown_0xcd787d9b"],
            virus_attack_time=json_data["virus_attack_time"],
            virus_damage=DamageInfo.from_json(json_data["virus_damage"]),
            sound_always_ff=json_data["sound_always_ff"],
            sound_0xbb3f8a7b=json_data["sound_0xbb3f8a7b"],
            sound_0x601f846d=json_data["sound_0x601f846d"],
            unknown_0x64c7990d=json_data["unknown_0x64c7990d"],
            unknown_0x376181e9=json_data["unknown_0x376181e9"],
            cutting_laser_damage=DamageInfo.from_json(json_data["cutting_laser_damage"]),
            sound_cutting_laser=AudioPlaybackParms.from_json(json_data["sound_cutting_laser"]),
            cutting_laser_beam_info=PlasmaBeamInfo.from_json(json_data["cutting_laser_beam_info"]),
            shield_vulnerability=DamageVulnerability.from_json(json_data["shield_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hearing_radius": self.hearing_radius,
            "unknown_0x4a6c4b40": self.unknown_0x4a6c4b40,
            "unknown_0x30d11671": self.unknown_0x30d11671,
            "model_no_holos": self.model_no_holos,
            "skin_no_holos": self.skin_no_holos,
            "shield_down_time": self.shield_down_time,
            "unknown_0xffb37b81": self.unknown_0xffb37b81,
            "shield_up_time": self.shield_up_time,
            "unknown_0x0d1d1648": self.unknown_0x0d1d1648,
            "shield_explode_effect": self.shield_explode_effect,
            "sound_shield_explode": self.sound_shield_explode.to_json(),
            "sound_shield_on": self.sound_shield_on.to_json(),
            "sound_shield_off": self.sound_shield_off.to_json(),
            "sound_flinch": self.sound_flinch.to_json(),
            "unknown_0xad120ad7": self.unknown_0xad120ad7,
            "unknown_0xe70ef8a3": self.unknown_0xe70ef8a3,
            "audio_playback_parms": self.audio_playback_parms.to_json(),
            "unknown_0x70e597d4": self.unknown_0x70e597d4,
            "unknown_0x94980a67": self.unknown_0x94980a67,
            "unknown_0xd02f08b0": self.unknown_0xd02f08b0,
            "unknown_0x53e84718": self.unknown_0x53e84718,
            "unknown_0x6fbc1bf9": self.unknown_0x6fbc1bf9,
            "energy_bolt_chance": self.energy_bolt_chance,
            "cutting_laser_chance": self.cutting_laser_chance,
            "unknown_0x075491ca": self.unknown_0x075491ca,
            "unknown_0x54f2892e": self.unknown_0x54f2892e,
            "energy_bolt_damage": self.energy_bolt_damage.to_json(),
            "energy_bolt_projectile": self.energy_bolt_projectile,
            "energy_bolt_attack_duration": self.energy_bolt_attack_duration,
            "unknown_0x28944183": self.unknown_0x28944183,
            "unknown_0xc7a69a59": self.unknown_0xc7a69a59,
            "sound_energy_bolt": self.sound_energy_bolt.to_json(),
            "unknown_0x9ede657f": self.unknown_0x9ede657f,
            "unknown_0xcd787d9b": self.unknown_0xcd787d9b,
            "virus_attack_time": self.virus_attack_time,
            "virus_damage": self.virus_damage.to_json(),
            "sound_always_ff": self.sound_always_ff,
            "sound_0xbb3f8a7b": self.sound_0xbb3f8a7b,
            "sound_0x601f846d": self.sound_0x601f846d,
            "unknown_0x64c7990d": self.unknown_0x64c7990d,
            "unknown_0x376181e9": self.unknown_0x376181e9,
            "cutting_laser_damage": self.cutting_laser_damage.to_json(),
            "sound_cutting_laser": self.sound_cutting_laser.to_json(),
            "cutting_laser_beam_info": self.cutting_laser_beam_info.to_json(),
            "shield_vulnerability": self.shield_vulnerability.to_json(),
        }

    def _dependencies_for_model_no_holos(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model_no_holos)

    def _dependencies_for_skin_no_holos(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.skin_no_holos)

    def _dependencies_for_shield_explode_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_explode_effect)

    def _dependencies_for_energy_bolt_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.energy_bolt_projectile)

    def _dependencies_for_sound_0xbb3f8a7b(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0xbb3f8a7b)

    def _dependencies_for_sound_0x601f846d(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0x601f846d)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model_no_holos, "model_no_holos", "AssetId"),
            (self._dependencies_for_skin_no_holos, "skin_no_holos", "AssetId"),
            (self._dependencies_for_shield_explode_effect, "shield_explode_effect", "AssetId"),
            (self.sound_shield_explode.dependencies_for, "sound_shield_explode", "AudioPlaybackParms"),
            (self.sound_shield_on.dependencies_for, "sound_shield_on", "AudioPlaybackParms"),
            (self.sound_shield_off.dependencies_for, "sound_shield_off", "AudioPlaybackParms"),
            (self.sound_flinch.dependencies_for, "sound_flinch", "AudioPlaybackParms"),
            (self.audio_playback_parms.dependencies_for, "audio_playback_parms", "AudioPlaybackParms"),
            (self._dependencies_for_energy_bolt_projectile, "energy_bolt_projectile", "AssetId"),
            (self.sound_energy_bolt.dependencies_for, "sound_energy_bolt", "AudioPlaybackParms"),
            (self._dependencies_for_sound_0xbb3f8a7b, "sound_0xbb3f8a7b", "int"),
            (self._dependencies_for_sound_0x601f846d, "sound_0x601f846d", "int"),
            (self.sound_cutting_laser.dependencies_for, "sound_cutting_laser", "AudioPlaybackParms"),
            (self.cutting_laser_beam_info.dependencies_for, "cutting_laser_beam_info", "PlasmaBeamInfo"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for RezbitData.{field_name} ({field_type}): {e}")


def _decode_sound_shield_explode(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_shield_on(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_shield_off(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_flinch(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_energy_bolt_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0},
    )


def _decode_sound_energy_bolt(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_virus_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0},
    )


def _decode_cutting_laser_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 5.0},
    )


def _decode_sound_cutting_laser(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_cutting_laser_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
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


def _decode_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xED69488F: ("hearing_radius", structs.decode_BIG_f),
    0x4A6C4B40: ("unknown_0x4a6c4b40", structs.decode_BIG_f),
    0x30D11671: ("unknown_0x30d11671", structs.decode_BIG_f),
    0xC80BB6E4: ("model_no_holos", structs.decode_BIG_L),
    0x05486319: ("skin_no_holos", structs.decode_BIG_L),
    0x8980A469: ("shield_down_time", structs.decode_BIG_f),
    0xFFB37B81: ("unknown_0xffb37b81", structs.decode_BIG_f),
    0x448579CD: ("shield_up_time", structs.decode_BIG_f),
    0x0D1D1648: ("unknown_0x0d1d1648", structs.decode_BIG_f),
    0xA41F75EF: ("shield_explode_effect", structs.decode_BIG_L),
    0xA34E2D84: ("sound_shield_explode", _decode_sound_shield_explode),
    0x8C598E41: ("sound_shield_on", _decode_sound_shield_on),
    0xF4491ED5: ("sound_shield_off", _decode_sound_shield_off),
    0x7D832158: ("sound_flinch", _decode_sound_flinch),
    0xAD120AD7: ("unknown_0xad120ad7", structs.decode_BIG_f),
    0xE70EF8A3: ("unknown_0xe70ef8a3", structs.decode_BIG_f),
    0x6BF2FF60: ("audio_playback_parms", _decode_audio_playback_parms),
    0x70E597D4: ("unknown_0x70e597d4", structs.decode_BIG_f),
    0x94980A67: ("unknown_0x94980a67", structs.decode_BIG_f),
    0xD02F08B0: ("unknown_0xd02f08b0", structs.decode_BIG_f),
    0x53E84718: ("unknown_0x53e84718", structs.decode_BIG_f),
    0x6FBC1BF9: ("unknown_0x6fbc1bf9", structs.decode_BIG_f),
    0xDC276015: ("energy_bolt_chance", structs.decode_BIG_f),
    0x2CA3E9CD: ("cutting_laser_chance", structs.decode_BIG_f),
    0x075491CA: ("unknown_0x075491ca", structs.decode_BIG_f),
    0x54F2892E: ("unknown_0x54f2892e", structs.decode_BIG_f),
    0x600C5F40: ("energy_bolt_damage", _decode_energy_bolt_damage),
    0x2F11094B: ("energy_bolt_projectile", structs.decode_BIG_L),
    0xA1F350F5: ("energy_bolt_attack_duration", structs.decode_BIG_f),
    0x28944183: ("unknown_0x28944183", structs.decode_BIG_f),
    0xC7A69A59: ("unknown_0xc7a69a59", structs.decode_BIG_f),
    0xBD3EB001: ("sound_energy_bolt", _decode_sound_energy_bolt),
    0x9EDE657F: ("unknown_0x9ede657f", structs.decode_BIG_f),
    0xCD787D9B: ("unknown_0xcd787d9b", structs.decode_BIG_f),
    0x4A7D3B04: ("virus_attack_time", structs.decode_BIG_f),
    0x16869B57: ("virus_damage", _decode_virus_damage),
    0x973D7CC3: ("sound_always_ff", structs.decode_BIG_l),
    0xBB3F8A7B: ("sound_0xbb3f8a7b", structs.decode_BIG_l),
    0x601F846D: ("sound_0x601f846d", structs.decode_BIG_l),
    0x64C7990D: ("unknown_0x64c7990d", structs.decode_BIG_f),
    0x376181E9: ("unknown_0x376181e9", structs.decode_BIG_f),
    0xBB58C088: ("cutting_laser_damage", _decode_cutting_laser_damage),
    0x7864CA32: ("sound_cutting_laser", _decode_sound_cutting_laser),
    0x59764DBB: ("cutting_laser_beam_info", _decode_cutting_laser_beam_info),
    0xD34F1323: ("shield_vulnerability", _decode_shield_vulnerability),
}
