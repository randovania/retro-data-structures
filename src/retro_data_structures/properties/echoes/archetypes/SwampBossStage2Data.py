# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.echoes.archetypes.SwampBossStage2Struct import SwampBossStage2Struct
from retro_data_structures.properties.echoes.archetypes.UnknownStruct38 import UnknownStruct38
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SwampBossStage2DataJson(typing_extensions.TypedDict):
        hover_speed: float
        upper_left_wing_target: int
        lower_left_wing_target: int
        upper_right_wing_target: int
        lower_right_wing_target: int
        unknown_0xcabe6b96: float
        swamp_boss_stage2_struct_0x7fa9256a: json_util.JsonObject
        swamp_boss_stage2_struct_0x8b884b8e: json_util.JsonObject
        swamp_boss_stage2_struct_0x04b7a789: json_util.JsonObject
        swamp_boss_stage2_struct_0xf096c96d: json_util.JsonObject
        stun_time: float
        unknown_0x96ce7897: int
        spit_projectile: int
        spit_damage: json_util.JsonObject
        spit_visor_effect: int
        sound_spit_visor: int
        spit_projectile_radius: float
        swoop_damage: json_util.JsonObject
        swoop_push: float
        swoop_damage_time: float
        splash: int
        unknown_0x7fc50ac2: float
        unknown_0x13448a4a: float
        unknown_0xf55924da: float
        unknown_0x83bc1de7: float
        unknown_0x5a844633: float
        unknown_0x78e22d1b: float
        unknown_0x9e116385: float
        radar_range: float
        unknown_0xfe97e835: float
        splash_shock_wave: json_util.JsonObject
        unknown_0x9807497c: float
        unknown_0xe57ca27c: float
        scan_info_light: int
        scan_info_dark: int
        bubble_telegraph_effect: int
        wing_damage_effect: int
        unknown_struct38: json_util.JsonObject
        blow_effect: int
        blow_damage: json_util.JsonObject
        unknown_0x6d89649b: float
        blow_push: float
        break_stun_damage: float
        stunned_sound: json_util.JsonObject
        audio_playback_parms_0x427a116a: json_util.JsonObject
        audio_playback_parms_0xc05d5c7a: json_util.JsonObject
        audio_playback_parms_0x2b3c923a: json_util.JsonObject
        unknown_0x8fe0bf01: float
        flinch_sound: json_util.JsonObject
        flinch_sound_chance: float
        stunned_flinch_sound: json_util.JsonObject
        audio_playback_parms_0x878a6522: json_util.JsonObject
        unknown_0x19849710: float
        audio_playback_parms_0x692fa63c: json_util.JsonObject
        audio_playback_parms_0xbe3d39aa: json_util.JsonObject


@dataclasses.dataclass()
class SwampBossStage2Data(BaseProperty):
    hover_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x845EF489, original_name="HoverSpeed"),
        },
    )
    upper_left_wing_target: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x11A273CB, original_name="Upper Left Wing Target"),
        },
    )
    lower_left_wing_target: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8A3331DD, original_name="Lower Left Wing Target"),
        },
    )
    upper_right_wing_target: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x26439458, original_name="Upper Right Wing Target"),
        },
    )
    lower_right_wing_target: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBDD2D64E, original_name="Lower Right Wing Target"),
        },
    )
    unknown_0xcabe6b96: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCABE6B96, original_name="Unknown"),
        },
    )
    swamp_boss_stage2_struct_0x7fa9256a: SwampBossStage2Struct = dataclasses.field(
        default_factory=SwampBossStage2Struct,
        metadata={
            "reflection": FieldReflection[SwampBossStage2Struct](
                SwampBossStage2Struct,
                id=0x7FA9256A,
                original_name="SwampBossStage2Struct",
                from_json=SwampBossStage2Struct.from_json,
                to_json=SwampBossStage2Struct.to_json,
            ),
        },
    )
    swamp_boss_stage2_struct_0x8b884b8e: SwampBossStage2Struct = dataclasses.field(
        default_factory=SwampBossStage2Struct,
        metadata={
            "reflection": FieldReflection[SwampBossStage2Struct](
                SwampBossStage2Struct,
                id=0x8B884B8E,
                original_name="SwampBossStage2Struct",
                from_json=SwampBossStage2Struct.from_json,
                to_json=SwampBossStage2Struct.to_json,
            ),
        },
    )
    swamp_boss_stage2_struct_0x04b7a789: SwampBossStage2Struct = dataclasses.field(
        default_factory=SwampBossStage2Struct,
        metadata={
            "reflection": FieldReflection[SwampBossStage2Struct](
                SwampBossStage2Struct,
                id=0x04B7A789,
                original_name="SwampBossStage2Struct",
                from_json=SwampBossStage2Struct.from_json,
                to_json=SwampBossStage2Struct.to_json,
            ),
        },
    )
    swamp_boss_stage2_struct_0xf096c96d: SwampBossStage2Struct = dataclasses.field(
        default_factory=SwampBossStage2Struct,
        metadata={
            "reflection": FieldReflection[SwampBossStage2Struct](
                SwampBossStage2Struct,
                id=0xF096C96D,
                original_name="SwampBossStage2Struct",
                from_json=SwampBossStage2Struct.from_json,
                to_json=SwampBossStage2Struct.to_json,
            ),
        },
    )
    stun_time: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7E192395, original_name="StunTime"),
        },
    )
    unknown_0x96ce7897: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x96CE7897, original_name="Unknown"),
        },
    )
    spit_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCFE37EBF, original_name="SpitProjectile"),
        },
    )
    spit_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xDA3C9B32,
                original_name="SpitDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    spit_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x008BECAB, original_name="SpitVisorEffect"),
        },
    )
    sound_spit_visor: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xF3AF8417, original_name="Sound_SpitVisor"),
        },
    )
    spit_projectile_radius: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDADC5BC9, original_name="SpitProjectileRadius"),
        },
    )
    swoop_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x294E9516,
                original_name="SwoopDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    swoop_push: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D483636, original_name="SwoopPush"),
        },
    )
    swoop_damage_time: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7B61A42B, original_name="SwoopDamageTime"),
        },
    )
    splash: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD8D148FB, original_name="Splash"),
        },
    )
    unknown_0x7fc50ac2: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FC50AC2, original_name="Unknown"),
        },
    )
    unknown_0x13448a4a: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x13448A4A, original_name="Unknown"),
        },
    )
    unknown_0xf55924da: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF55924DA, original_name="Unknown"),
        },
    )
    unknown_0x83bc1de7: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x83BC1DE7, original_name="Unknown"),
        },
    )
    unknown_0x5a844633: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5A844633, original_name="Unknown"),
        },
    )
    unknown_0x78e22d1b: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78E22D1B, original_name="Unknown"),
        },
    )
    unknown_0x9e116385: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9E116385, original_name="Unknown"),
        },
    )
    radar_range: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEE258868, original_name="RadarRange"),
        },
    )
    unknown_0xfe97e835: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFE97E835, original_name="Unknown"),
        },
    )
    splash_shock_wave: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x6C0F7AA3,
                original_name="SplashShockWave",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    unknown_0x9807497c: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9807497C, original_name="Unknown"),
        },
    )
    unknown_0xe57ca27c: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE57CA27C, original_name="Unknown"),
        },
    )
    scan_info_light: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA3E1608C, original_name="ScanInfoLight"),
        },
    )
    scan_info_dark: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA21792BF, original_name="ScanInfoDark"),
        },
    )
    bubble_telegraph_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x515268E5, original_name="BubbleTelegraphEffect"),
        },
    )
    wing_damage_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB1B55340, original_name="WingDamageEffect"),
        },
    )
    unknown_struct38: UnknownStruct38 = dataclasses.field(
        default_factory=UnknownStruct38,
        metadata={
            "reflection": FieldReflection[UnknownStruct38](
                UnknownStruct38,
                id=0x9347820E,
                original_name="UnknownStruct38",
                from_json=UnknownStruct38.from_json,
                to_json=UnknownStruct38.to_json,
            ),
        },
    )
    blow_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB7DC6C65, original_name="BlowEffect"),
        },
    )
    blow_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xF1F0C73D,
                original_name="BlowDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x6d89649b: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D89649B, original_name="Unknown"),
        },
    )
    blow_push: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x77F97080, original_name="BlowPush"),
        },
    )
    break_stun_damage: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D67C284, original_name="BreakStunDamage"),
        },
    )
    stunned_sound: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x87B30E02,
                original_name="StunnedSound",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x427a116a: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x427A116A,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0xc05d5c7a: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xC05D5C7A,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x2b3c923a: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x2B3C923A,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown_0x8fe0bf01: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8FE0BF01, original_name="Unknown"),
        },
    )
    flinch_sound: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x23087520,
                original_name="FlinchSound",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    flinch_sound_chance: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA3131519, original_name="FlinchSoundChance"),
        },
    )
    stunned_flinch_sound: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xB53087CC,
                original_name="StunnedFlinchSound",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x878a6522: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x878A6522,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown_0x19849710: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x19849710, original_name="Unknown"),
        },
    )
    audio_playback_parms_0x692fa63c: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x692FA63C,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0xbe3d39aa: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xBE3D39AA,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
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
        if property_count != 55:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x845EF489
        hover_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11A273CB
        upper_left_wing_target = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A3331DD
        lower_left_wing_target = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26439458
        upper_right_wing_target = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBDD2D64E
        lower_right_wing_target = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCABE6B96
        unknown_0xcabe6b96 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FA9256A
        swamp_boss_stage2_struct_0x7fa9256a = SwampBossStage2Struct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B884B8E
        swamp_boss_stage2_struct_0x8b884b8e = SwampBossStage2Struct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04B7A789
        swamp_boss_stage2_struct_0x04b7a789 = SwampBossStage2Struct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF096C96D
        swamp_boss_stage2_struct_0xf096c96d = SwampBossStage2Struct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E192395
        stun_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96CE7897
        unknown_0x96ce7897 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCFE37EBF
        spit_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDA3C9B32
        spit_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x008BECAB
        spit_visor_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3AF8417
        sound_spit_visor = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDADC5BC9
        spit_projectile_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x294E9516
        swoop_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 0.5}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D483636
        swoop_push = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B61A42B
        swoop_damage_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8D148FB
        splash = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FC50AC2
        unknown_0x7fc50ac2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13448A4A
        unknown_0x13448a4a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF55924DA
        unknown_0xf55924da = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83BC1DE7
        unknown_0x83bc1de7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5A844633
        unknown_0x5a844633 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78E22D1B
        unknown_0x78e22d1b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9E116385
        unknown_0x9e116385 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEE258868
        radar_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE97E835
        unknown_0xfe97e835 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C0F7AA3
        splash_shock_wave = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9807497C
        unknown_0x9807497c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE57CA27C
        unknown_0xe57ca27c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3E1608C
        scan_info_light = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA21792BF
        scan_info_dark = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x515268E5
        bubble_telegraph_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB1B55340
        wing_damage_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9347820E
        unknown_struct38 = UnknownStruct38.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7DC6C65
        blow_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1F0C73D
        blow_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 0.5}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D89649B
        unknown_0x6d89649b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77F97080
        blow_push = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D67C284
        break_stun_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87B30E02
        stunned_sound = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x427A116A
        audio_playback_parms_0x427a116a = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC05D5C7A
        audio_playback_parms_0xc05d5c7a = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B3C923A
        audio_playback_parms_0x2b3c923a = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8FE0BF01
        unknown_0x8fe0bf01 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23087520
        flinch_sound = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3131519
        flinch_sound_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB53087CC
        stunned_flinch_sound = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x878A6522
        audio_playback_parms_0x878a6522 = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19849710
        unknown_0x19849710 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x692FA63C
        audio_playback_parms_0x692fa63c = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE3D39AA
        audio_playback_parms_0xbe3d39aa = AudioPlaybackParms.from_stream(data, game, property_size)

        return cls(
            hover_speed,
            upper_left_wing_target,
            lower_left_wing_target,
            upper_right_wing_target,
            lower_right_wing_target,
            unknown_0xcabe6b96,
            swamp_boss_stage2_struct_0x7fa9256a,
            swamp_boss_stage2_struct_0x8b884b8e,
            swamp_boss_stage2_struct_0x04b7a789,
            swamp_boss_stage2_struct_0xf096c96d,
            stun_time,
            unknown_0x96ce7897,
            spit_projectile,
            spit_damage,
            spit_visor_effect,
            sound_spit_visor,
            spit_projectile_radius,
            swoop_damage,
            swoop_push,
            swoop_damage_time,
            splash,
            unknown_0x7fc50ac2,
            unknown_0x13448a4a,
            unknown_0xf55924da,
            unknown_0x83bc1de7,
            unknown_0x5a844633,
            unknown_0x78e22d1b,
            unknown_0x9e116385,
            radar_range,
            unknown_0xfe97e835,
            splash_shock_wave,
            unknown_0x9807497c,
            unknown_0xe57ca27c,
            scan_info_light,
            scan_info_dark,
            bubble_telegraph_effect,
            wing_damage_effect,
            unknown_struct38,
            blow_effect,
            blow_damage,
            unknown_0x6d89649b,
            blow_push,
            break_stun_damage,
            stunned_sound,
            audio_playback_parms_0x427a116a,
            audio_playback_parms_0xc05d5c7a,
            audio_playback_parms_0x2b3c923a,
            unknown_0x8fe0bf01,
            flinch_sound,
            flinch_sound_chance,
            stunned_flinch_sound,
            audio_playback_parms_0x878a6522,
            unknown_0x19849710,
            audio_playback_parms_0x692fa63c,
            audio_playback_parms_0xbe3d39aa,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x007")  # 55 properties

        data.write(b"\x84^\xf4\x89")  # 0x845ef489
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hover_speed))

        data.write(b"\x11\xa2s\xcb")  # 0x11a273cb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.upper_left_wing_target))

        data.write(b"\x8a31\xdd")  # 0x8a3331dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.lower_left_wing_target))

        data.write(b"&C\x94X")  # 0x26439458
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.upper_right_wing_target))

        data.write(b"\xbd\xd2\xd6N")  # 0xbdd2d64e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.lower_right_wing_target))

        data.write(b"\xca\xbek\x96")  # 0xcabe6b96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcabe6b96))

        data.write(b"\x7f\xa9%j")  # 0x7fa9256a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swamp_boss_stage2_struct_0x7fa9256a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8b\x88K\x8e")  # 0x8b884b8e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swamp_boss_stage2_struct_0x8b884b8e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x04\xb7\xa7\x89")  # 0x4b7a789
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swamp_boss_stage2_struct_0x04b7a789.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf0\x96\xc9m")  # 0xf096c96d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swamp_boss_stage2_struct_0xf096c96d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~\x19#\x95")  # 0x7e192395
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_time))

        data.write(b"\x96\xcex\x97")  # 0x96ce7897
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x96ce7897))

        data.write(b"\xcf\xe3~\xbf")  # 0xcfe37ebf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.spit_projectile))

        data.write(b"\xda<\x9b2")  # 0xda3c9b32
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spit_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\x8b\xec\xab")  # 0x8becab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.spit_visor_effect))

        data.write(b"\xf3\xaf\x84\x17")  # 0xf3af8417
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_spit_visor))

        data.write(b"\xda\xdc[\xc9")  # 0xdadc5bc9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.spit_projectile_radius))

        data.write(b")N\x95\x16")  # 0x294e9516
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swoop_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 0.5})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"}H66")  # 0x7d483636
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.swoop_push))

        data.write(b"{a\xa4+")  # 0x7b61a42b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.swoop_damage_time))

        data.write(b"\xd8\xd1H\xfb")  # 0xd8d148fb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.splash))

        data.write(b"\x7f\xc5\n\xc2")  # 0x7fc50ac2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7fc50ac2))

        data.write(b"\x13D\x8aJ")  # 0x13448a4a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x13448a4a))

        data.write(b"\xf5Y$\xda")  # 0xf55924da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf55924da))

        data.write(b"\x83\xbc\x1d\xe7")  # 0x83bc1de7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x83bc1de7))

        data.write(b"Z\x84F3")  # 0x5a844633
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5a844633))

        data.write(b"x\xe2-\x1b")  # 0x78e22d1b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x78e22d1b))

        data.write(b"\x9e\x11c\x85")  # 0x9e116385
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9e116385))

        data.write(b"\xee%\x88h")  # 0xee258868
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.radar_range))

        data.write(b"\xfe\x97\xe85")  # 0xfe97e835
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfe97e835))

        data.write(b"l\x0fz\xa3")  # 0x6c0f7aa3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.splash_shock_wave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x98\x07I|")  # 0x9807497c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9807497c))

        data.write(b"\xe5|\xa2|")  # 0xe57ca27c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe57ca27c))

        data.write(b"\xa3\xe1`\x8c")  # 0xa3e1608c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scan_info_light))

        data.write(b"\xa2\x17\x92\xbf")  # 0xa21792bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scan_info_dark))

        data.write(b"QRh\xe5")  # 0x515268e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.bubble_telegraph_effect))

        data.write(b"\xb1\xb5S@")  # 0xb1b55340
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.wing_damage_effect))

        data.write(b"\x93G\x82\x0e")  # 0x9347820e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct38.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb7\xdcle")  # 0xb7dc6c65
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.blow_effect))

        data.write(b"\xf1\xf0\xc7=")  # 0xf1f0c73d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.blow_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 0.5})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"m\x89d\x9b")  # 0x6d89649b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6d89649b))

        data.write(b"w\xf9p\x80")  # 0x77f97080
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.blow_push))

        data.write(b"mg\xc2\x84")  # 0x6d67c284
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.break_stun_damage))

        data.write(b"\x87\xb3\x0e\x02")  # 0x87b30e02
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stunned_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Bz\x11j")  # 0x427a116a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x427a116a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc0]\\z")  # 0xc05d5c7a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0xc05d5c7a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+<\x92:")  # 0x2b3c923a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x2b3c923a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8f\xe0\xbf\x01")  # 0x8fe0bf01
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8fe0bf01))

        data.write(b"#\x08u ")  # 0x23087520
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flinch_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa3\x13\x15\x19")  # 0xa3131519
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flinch_sound_chance))

        data.write(b"\xb50\x87\xcc")  # 0xb53087cc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stunned_flinch_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x87\x8ae"')  # 0x878a6522
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x878a6522.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x19\x84\x97\x10")  # 0x19849710
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x19849710))

        data.write(b"i/\xa6<")  # 0x692fa63c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x692fa63c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbe=9\xaa")  # 0xbe3d39aa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0xbe3d39aa.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwampBossStage2DataJson", data)
        return cls(
            hover_speed=json_data["hover_speed"],
            upper_left_wing_target=json_data["upper_left_wing_target"],
            lower_left_wing_target=json_data["lower_left_wing_target"],
            upper_right_wing_target=json_data["upper_right_wing_target"],
            lower_right_wing_target=json_data["lower_right_wing_target"],
            unknown_0xcabe6b96=json_data["unknown_0xcabe6b96"],
            swamp_boss_stage2_struct_0x7fa9256a=SwampBossStage2Struct.from_json(
                json_data["swamp_boss_stage2_struct_0x7fa9256a"]
            ),
            swamp_boss_stage2_struct_0x8b884b8e=SwampBossStage2Struct.from_json(
                json_data["swamp_boss_stage2_struct_0x8b884b8e"]
            ),
            swamp_boss_stage2_struct_0x04b7a789=SwampBossStage2Struct.from_json(
                json_data["swamp_boss_stage2_struct_0x04b7a789"]
            ),
            swamp_boss_stage2_struct_0xf096c96d=SwampBossStage2Struct.from_json(
                json_data["swamp_boss_stage2_struct_0xf096c96d"]
            ),
            stun_time=json_data["stun_time"],
            unknown_0x96ce7897=json_data["unknown_0x96ce7897"],
            spit_projectile=json_data["spit_projectile"],
            spit_damage=DamageInfo.from_json(json_data["spit_damage"]),
            spit_visor_effect=json_data["spit_visor_effect"],
            sound_spit_visor=json_data["sound_spit_visor"],
            spit_projectile_radius=json_data["spit_projectile_radius"],
            swoop_damage=DamageInfo.from_json(json_data["swoop_damage"]),
            swoop_push=json_data["swoop_push"],
            swoop_damage_time=json_data["swoop_damage_time"],
            splash=json_data["splash"],
            unknown_0x7fc50ac2=json_data["unknown_0x7fc50ac2"],
            unknown_0x13448a4a=json_data["unknown_0x13448a4a"],
            unknown_0xf55924da=json_data["unknown_0xf55924da"],
            unknown_0x83bc1de7=json_data["unknown_0x83bc1de7"],
            unknown_0x5a844633=json_data["unknown_0x5a844633"],
            unknown_0x78e22d1b=json_data["unknown_0x78e22d1b"],
            unknown_0x9e116385=json_data["unknown_0x9e116385"],
            radar_range=json_data["radar_range"],
            unknown_0xfe97e835=json_data["unknown_0xfe97e835"],
            splash_shock_wave=ShockWaveInfo.from_json(json_data["splash_shock_wave"]),
            unknown_0x9807497c=json_data["unknown_0x9807497c"],
            unknown_0xe57ca27c=json_data["unknown_0xe57ca27c"],
            scan_info_light=json_data["scan_info_light"],
            scan_info_dark=json_data["scan_info_dark"],
            bubble_telegraph_effect=json_data["bubble_telegraph_effect"],
            wing_damage_effect=json_data["wing_damage_effect"],
            unknown_struct38=UnknownStruct38.from_json(json_data["unknown_struct38"]),
            blow_effect=json_data["blow_effect"],
            blow_damage=DamageInfo.from_json(json_data["blow_damage"]),
            unknown_0x6d89649b=json_data["unknown_0x6d89649b"],
            blow_push=json_data["blow_push"],
            break_stun_damage=json_data["break_stun_damage"],
            stunned_sound=AudioPlaybackParms.from_json(json_data["stunned_sound"]),
            audio_playback_parms_0x427a116a=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x427a116a"]),
            audio_playback_parms_0xc05d5c7a=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0xc05d5c7a"]),
            audio_playback_parms_0x2b3c923a=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x2b3c923a"]),
            unknown_0x8fe0bf01=json_data["unknown_0x8fe0bf01"],
            flinch_sound=AudioPlaybackParms.from_json(json_data["flinch_sound"]),
            flinch_sound_chance=json_data["flinch_sound_chance"],
            stunned_flinch_sound=AudioPlaybackParms.from_json(json_data["stunned_flinch_sound"]),
            audio_playback_parms_0x878a6522=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x878a6522"]),
            unknown_0x19849710=json_data["unknown_0x19849710"],
            audio_playback_parms_0x692fa63c=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x692fa63c"]),
            audio_playback_parms_0xbe3d39aa=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0xbe3d39aa"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hover_speed": self.hover_speed,
            "upper_left_wing_target": self.upper_left_wing_target,
            "lower_left_wing_target": self.lower_left_wing_target,
            "upper_right_wing_target": self.upper_right_wing_target,
            "lower_right_wing_target": self.lower_right_wing_target,
            "unknown_0xcabe6b96": self.unknown_0xcabe6b96,
            "swamp_boss_stage2_struct_0x7fa9256a": self.swamp_boss_stage2_struct_0x7fa9256a.to_json(),
            "swamp_boss_stage2_struct_0x8b884b8e": self.swamp_boss_stage2_struct_0x8b884b8e.to_json(),
            "swamp_boss_stage2_struct_0x04b7a789": self.swamp_boss_stage2_struct_0x04b7a789.to_json(),
            "swamp_boss_stage2_struct_0xf096c96d": self.swamp_boss_stage2_struct_0xf096c96d.to_json(),
            "stun_time": self.stun_time,
            "unknown_0x96ce7897": self.unknown_0x96ce7897,
            "spit_projectile": self.spit_projectile,
            "spit_damage": self.spit_damage.to_json(),
            "spit_visor_effect": self.spit_visor_effect,
            "sound_spit_visor": self.sound_spit_visor,
            "spit_projectile_radius": self.spit_projectile_radius,
            "swoop_damage": self.swoop_damage.to_json(),
            "swoop_push": self.swoop_push,
            "swoop_damage_time": self.swoop_damage_time,
            "splash": self.splash,
            "unknown_0x7fc50ac2": self.unknown_0x7fc50ac2,
            "unknown_0x13448a4a": self.unknown_0x13448a4a,
            "unknown_0xf55924da": self.unknown_0xf55924da,
            "unknown_0x83bc1de7": self.unknown_0x83bc1de7,
            "unknown_0x5a844633": self.unknown_0x5a844633,
            "unknown_0x78e22d1b": self.unknown_0x78e22d1b,
            "unknown_0x9e116385": self.unknown_0x9e116385,
            "radar_range": self.radar_range,
            "unknown_0xfe97e835": self.unknown_0xfe97e835,
            "splash_shock_wave": self.splash_shock_wave.to_json(),
            "unknown_0x9807497c": self.unknown_0x9807497c,
            "unknown_0xe57ca27c": self.unknown_0xe57ca27c,
            "scan_info_light": self.scan_info_light,
            "scan_info_dark": self.scan_info_dark,
            "bubble_telegraph_effect": self.bubble_telegraph_effect,
            "wing_damage_effect": self.wing_damage_effect,
            "unknown_struct38": self.unknown_struct38.to_json(),
            "blow_effect": self.blow_effect,
            "blow_damage": self.blow_damage.to_json(),
            "unknown_0x6d89649b": self.unknown_0x6d89649b,
            "blow_push": self.blow_push,
            "break_stun_damage": self.break_stun_damage,
            "stunned_sound": self.stunned_sound.to_json(),
            "audio_playback_parms_0x427a116a": self.audio_playback_parms_0x427a116a.to_json(),
            "audio_playback_parms_0xc05d5c7a": self.audio_playback_parms_0xc05d5c7a.to_json(),
            "audio_playback_parms_0x2b3c923a": self.audio_playback_parms_0x2b3c923a.to_json(),
            "unknown_0x8fe0bf01": self.unknown_0x8fe0bf01,
            "flinch_sound": self.flinch_sound.to_json(),
            "flinch_sound_chance": self.flinch_sound_chance,
            "stunned_flinch_sound": self.stunned_flinch_sound.to_json(),
            "audio_playback_parms_0x878a6522": self.audio_playback_parms_0x878a6522.to_json(),
            "unknown_0x19849710": self.unknown_0x19849710,
            "audio_playback_parms_0x692fa63c": self.audio_playback_parms_0x692fa63c.to_json(),
            "audio_playback_parms_0xbe3d39aa": self.audio_playback_parms_0xbe3d39aa.to_json(),
        }

    def _dependencies_for_upper_left_wing_target(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.upper_left_wing_target)

    def _dependencies_for_lower_left_wing_target(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.lower_left_wing_target)

    def _dependencies_for_upper_right_wing_target(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.upper_right_wing_target)

    def _dependencies_for_lower_right_wing_target(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.lower_right_wing_target)

    def _dependencies_for_spit_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spit_projectile)

    def _dependencies_for_spit_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spit_visor_effect)

    def _dependencies_for_sound_spit_visor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_spit_visor)

    def _dependencies_for_splash(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash)

    def _dependencies_for_scan_info_light(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_info_light)

    def _dependencies_for_scan_info_dark(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_info_dark)

    def _dependencies_for_bubble_telegraph_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bubble_telegraph_effect)

    def _dependencies_for_wing_damage_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wing_damage_effect)

    def _dependencies_for_blow_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.blow_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_upper_left_wing_target, "upper_left_wing_target", "AssetId"),
            (self._dependencies_for_lower_left_wing_target, "lower_left_wing_target", "AssetId"),
            (self._dependencies_for_upper_right_wing_target, "upper_right_wing_target", "AssetId"),
            (self._dependencies_for_lower_right_wing_target, "lower_right_wing_target", "AssetId"),
            (self._dependencies_for_spit_projectile, "spit_projectile", "AssetId"),
            (self._dependencies_for_spit_visor_effect, "spit_visor_effect", "AssetId"),
            (self._dependencies_for_sound_spit_visor, "sound_spit_visor", "int"),
            (self._dependencies_for_splash, "splash", "AssetId"),
            (self.splash_shock_wave.dependencies_for, "splash_shock_wave", "ShockWaveInfo"),
            (self._dependencies_for_scan_info_light, "scan_info_light", "AssetId"),
            (self._dependencies_for_scan_info_dark, "scan_info_dark", "AssetId"),
            (self._dependencies_for_bubble_telegraph_effect, "bubble_telegraph_effect", "AssetId"),
            (self._dependencies_for_wing_damage_effect, "wing_damage_effect", "AssetId"),
            (self.unknown_struct38.dependencies_for, "unknown_struct38", "UnknownStruct38"),
            (self._dependencies_for_blow_effect, "blow_effect", "AssetId"),
            (self.stunned_sound.dependencies_for, "stunned_sound", "AudioPlaybackParms"),
            (
                self.audio_playback_parms_0x427a116a.dependencies_for,
                "audio_playback_parms_0x427a116a",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0xc05d5c7a.dependencies_for,
                "audio_playback_parms_0xc05d5c7a",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x2b3c923a.dependencies_for,
                "audio_playback_parms_0x2b3c923a",
                "AudioPlaybackParms",
            ),
            (self.flinch_sound.dependencies_for, "flinch_sound", "AudioPlaybackParms"),
            (self.stunned_flinch_sound.dependencies_for, "stunned_flinch_sound", "AudioPlaybackParms"),
            (
                self.audio_playback_parms_0x878a6522.dependencies_for,
                "audio_playback_parms_0x878a6522",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x692fa63c.dependencies_for,
                "audio_playback_parms_0x692fa63c",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0xbe3d39aa.dependencies_for,
                "audio_playback_parms_0xbe3d39aa",
                "AudioPlaybackParms",
            ),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SwampBossStage2Data.{field_name} ({field_type}): {e}")


def _decode_swamp_boss_stage2_struct_0x7fa9256a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SwampBossStage2Struct:
    return SwampBossStage2Struct.from_stream(data, game, property_size)


def _decode_swamp_boss_stage2_struct_0x8b884b8e(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SwampBossStage2Struct:
    return SwampBossStage2Struct.from_stream(data, game, property_size)


def _decode_swamp_boss_stage2_struct_0x04b7a789(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SwampBossStage2Struct:
    return SwampBossStage2Struct.from_stream(data, game, property_size)


def _decode_swamp_boss_stage2_struct_0xf096c96d(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SwampBossStage2Struct:
    return SwampBossStage2Struct.from_stream(data, game, property_size)


def _decode_spit_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0})


def _decode_swoop_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 0.5})


def _decode_splash_shock_wave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_unknown_struct38(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct38:
    return UnknownStruct38.from_stream(data, game, property_size)


def _decode_blow_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 0.5})


def _decode_stunned_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x427a116a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0xc05d5c7a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x2b3c923a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_flinch_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_stunned_flinch_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x878a6522(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x692fa63c(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0xbe3d39aa(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x845EF489: ("hover_speed", structs.decode_BIG_f),
    0x11A273CB: ("upper_left_wing_target", structs.decode_BIG_L),
    0x8A3331DD: ("lower_left_wing_target", structs.decode_BIG_L),
    0x26439458: ("upper_right_wing_target", structs.decode_BIG_L),
    0xBDD2D64E: ("lower_right_wing_target", structs.decode_BIG_L),
    0xCABE6B96: ("unknown_0xcabe6b96", structs.decode_BIG_f),
    0x7FA9256A: ("swamp_boss_stage2_struct_0x7fa9256a", _decode_swamp_boss_stage2_struct_0x7fa9256a),
    0x8B884B8E: ("swamp_boss_stage2_struct_0x8b884b8e", _decode_swamp_boss_stage2_struct_0x8b884b8e),
    0x04B7A789: ("swamp_boss_stage2_struct_0x04b7a789", _decode_swamp_boss_stage2_struct_0x04b7a789),
    0xF096C96D: ("swamp_boss_stage2_struct_0xf096c96d", _decode_swamp_boss_stage2_struct_0xf096c96d),
    0x7E192395: ("stun_time", structs.decode_BIG_f),
    0x96CE7897: ("unknown_0x96ce7897", structs.decode_BIG_l),
    0xCFE37EBF: ("spit_projectile", structs.decode_BIG_L),
    0xDA3C9B32: ("spit_damage", _decode_spit_damage),
    0x008BECAB: ("spit_visor_effect", structs.decode_BIG_L),
    0xF3AF8417: ("sound_spit_visor", structs.decode_BIG_l),
    0xDADC5BC9: ("spit_projectile_radius", structs.decode_BIG_f),
    0x294E9516: ("swoop_damage", _decode_swoop_damage),
    0x7D483636: ("swoop_push", structs.decode_BIG_f),
    0x7B61A42B: ("swoop_damage_time", structs.decode_BIG_f),
    0xD8D148FB: ("splash", structs.decode_BIG_L),
    0x7FC50AC2: ("unknown_0x7fc50ac2", structs.decode_BIG_f),
    0x13448A4A: ("unknown_0x13448a4a", structs.decode_BIG_f),
    0xF55924DA: ("unknown_0xf55924da", structs.decode_BIG_f),
    0x83BC1DE7: ("unknown_0x83bc1de7", structs.decode_BIG_f),
    0x5A844633: ("unknown_0x5a844633", structs.decode_BIG_f),
    0x78E22D1B: ("unknown_0x78e22d1b", structs.decode_BIG_f),
    0x9E116385: ("unknown_0x9e116385", structs.decode_BIG_f),
    0xEE258868: ("radar_range", structs.decode_BIG_f),
    0xFE97E835: ("unknown_0xfe97e835", structs.decode_BIG_f),
    0x6C0F7AA3: ("splash_shock_wave", _decode_splash_shock_wave),
    0x9807497C: ("unknown_0x9807497c", structs.decode_BIG_f),
    0xE57CA27C: ("unknown_0xe57ca27c", structs.decode_BIG_f),
    0xA3E1608C: ("scan_info_light", structs.decode_BIG_L),
    0xA21792BF: ("scan_info_dark", structs.decode_BIG_L),
    0x515268E5: ("bubble_telegraph_effect", structs.decode_BIG_L),
    0xB1B55340: ("wing_damage_effect", structs.decode_BIG_L),
    0x9347820E: ("unknown_struct38", _decode_unknown_struct38),
    0xB7DC6C65: ("blow_effect", structs.decode_BIG_L),
    0xF1F0C73D: ("blow_damage", _decode_blow_damage),
    0x6D89649B: ("unknown_0x6d89649b", structs.decode_BIG_f),
    0x77F97080: ("blow_push", structs.decode_BIG_f),
    0x6D67C284: ("break_stun_damage", structs.decode_BIG_f),
    0x87B30E02: ("stunned_sound", _decode_stunned_sound),
    0x427A116A: ("audio_playback_parms_0x427a116a", _decode_audio_playback_parms_0x427a116a),
    0xC05D5C7A: ("audio_playback_parms_0xc05d5c7a", _decode_audio_playback_parms_0xc05d5c7a),
    0x2B3C923A: ("audio_playback_parms_0x2b3c923a", _decode_audio_playback_parms_0x2b3c923a),
    0x8FE0BF01: ("unknown_0x8fe0bf01", structs.decode_BIG_f),
    0x23087520: ("flinch_sound", _decode_flinch_sound),
    0xA3131519: ("flinch_sound_chance", structs.decode_BIG_f),
    0xB53087CC: ("stunned_flinch_sound", _decode_stunned_flinch_sound),
    0x878A6522: ("audio_playback_parms_0x878a6522", _decode_audio_playback_parms_0x878a6522),
    0x19849710: ("unknown_0x19849710", structs.decode_BIG_f),
    0x692FA63C: ("audio_playback_parms_0x692fa63c", _decode_audio_playback_parms_0x692fa63c),
    0xBE3D39AA: ("audio_playback_parms_0xbe3d39aa", _decode_audio_playback_parms_0xbe3d39aa),
}
