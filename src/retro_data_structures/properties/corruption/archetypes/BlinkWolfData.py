# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BlinkWolfDataJson(typing_extensions.TypedDict):
        unknown_0x2b3109a6: bool
        start_invisible: bool
        unknown_0x7fdee42c: float
        turn_prediction: float
        spit_prediction: float
        approach_dist: float
        unknown_0x6d6c84cb: float
        jump_apex: float
        min_spit_range: float
        max_spit_range: float
        unknown_0xb6055f35: int
        spit_starting: json_util.JsonObject
        spit_full_speed: json_util.JsonObject
        launch_projectile_data_0x76b1b8e0: json_util.JsonObject
        launch_projectile_data_0xfe3b5965: json_util.JsonObject
        caud: int
        sound_teleport_end: int
        max_head_rotation: float
        head_rotation_speed: float
        unknown_0x0f5a3164: float
        unknown_0x190d9fc8: float
        unknown_0xfcae3411: float
        unknown_0x7ecb92ca: float
        burn_damage: float
        burn_damage_duration: float
        shockwave_range: float
        shockwave_damage: json_util.JsonObject
        shockwave_intensity: float
        unknown_0xb39833c0: float
        unknown_0x96bd6426: float
        unknown_0xd7aa5ba0: float
        blink_out: int
        blink_bubble: int
        min_bubble_time: float
        max_bubble_time: float
        min_blink_range: float
        unknown_0x8e5f1638: float
        warp_increase_intensity: float
        warp_intensity_max: float
        unknown_0x22794c6d: float
        unknown_0x5b9cc474: float
        warp_duration_max: float
        frozen_gib_time: float
        avoidance_range: float
        hearing_radius: float
        recheck_path_time: float
        recheck_path_distance: float
        pain_threshold: float
        unknown_0xa6c1631d: float
        unknown_0x312e194a: float
        unknown_0xc6f92e2f: float
        player_scan_delay: float
        unknown_0x108e8ed8: float
        max_fall_time: float
        unknown_0xc34bffca: float
        unknown_0xf5aa6363: float
        unknown_0xd40c2b10: float
        unknown_0x6bbf9cdc: float
        unknown_0xb2dd7c06: float


@dataclasses.dataclass()
class BlinkWolfData(BaseProperty):
    unknown_0x2b3109a6: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2B3109A6, original_name="Unknown"),
        },
    )
    start_invisible: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBB5C37E0, original_name="StartInvisible"),
        },
    )
    unknown_0x7fdee42c: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FDEE42C, original_name="Unknown"),
        },
    )
    turn_prediction: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x983954AE, original_name="TurnPrediction"),
        },
    )
    spit_prediction: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x86B2B7D7, original_name="SpitPrediction"),
        },
    )
    approach_dist: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA1D7E06B, original_name="ApproachDist"),
        },
    )
    unknown_0x6d6c84cb: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D6C84CB, original_name="Unknown"),
        },
    )
    jump_apex: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF2782501, original_name="JumpApex"),
        },
    )
    min_spit_range: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0236C750, original_name="MinSpitRange"),
        },
    )
    max_spit_range: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x17BD13A2, original_name="MaxSpitRange"),
        },
    )
    unknown_0xb6055f35: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB6055F35, original_name="Unknown"),
        },
    )
    spit_starting: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x6DAC116A,
                original_name="SpitStarting",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    spit_full_speed: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x9AAB30F1,
                original_name="SpitFullSpeed",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    launch_projectile_data_0x76b1b8e0: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x76B1B8E0,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    launch_projectile_data_0xfe3b5965: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0xFE3B5965,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    caud: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x95EAAACB, original_name="CAUD"),
        },
    )
    sound_teleport_end: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD4C88DD1, original_name="Sound_TeleportEnd"),
        },
    )
    max_head_rotation: float = dataclasses.field(
        default=70.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE68CEBB0, original_name="MaxHeadRotation"),
        },
    )
    head_rotation_speed: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B7FCF8C, original_name="HeadRotationSpeed"),
        },
    )
    unknown_0x0f5a3164: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0F5A3164, original_name="Unknown"),
        },
    )
    unknown_0x190d9fc8: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x190D9FC8, original_name="Unknown"),
        },
    )
    unknown_0xfcae3411: float = dataclasses.field(
        default=24.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFCAE3411, original_name="Unknown"),
        },
    )
    unknown_0x7ecb92ca: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7ECB92CA, original_name="Unknown"),
        },
    )
    burn_damage: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF201BFA, original_name="BurnDamage"),
        },
    )
    burn_damage_duration: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF495AAB, original_name="BurnDamageDuration"),
        },
    )
    shockwave_range: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D518FD5, original_name="ShockwaveRange"),
        },
    )
    shockwave_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0F2FA713,
                original_name="ShockwaveDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    shockwave_intensity: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA42DBD9E, original_name="ShockwaveIntensity"),
        },
    )
    unknown_0xb39833c0: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB39833C0, original_name="Unknown"),
        },
    )
    unknown_0x96bd6426: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x96BD6426, original_name="Unknown"),
        },
    )
    unknown_0xd7aa5ba0: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD7AA5BA0, original_name="Unknown"),
        },
    )
    blink_out: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2050F248, original_name="BlinkOut"),
        },
    )
    blink_bubble: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9CB2109A, original_name="BlinkBubble"),
        },
    )
    min_bubble_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4CE0D7E5, original_name="MinBubbleTime"),
        },
    )
    max_bubble_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1F46CF01, original_name="MaxBubbleTime"),
        },
    )
    min_blink_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0FC0B9E3, original_name="MinBlinkRange"),
        },
    )
    unknown_0x8e5f1638: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E5F1638, original_name="Unknown"),
        },
    )
    warp_increase_intensity: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF7BA9E21, original_name="WarpIncreaseIntensity"),
        },
    )
    warp_intensity_max: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E501419, original_name="WarpIntensityMax"),
        },
    )
    unknown_0x22794c6d: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x22794C6D, original_name="Unknown"),
        },
    )
    unknown_0x5b9cc474: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5B9CC474, original_name="Unknown"),
        },
    )
    warp_duration_max: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08F1E9D3, original_name="WarpDurationMax"),
        },
    )
    frozen_gib_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x51BB4B6F, original_name="FrozenGibTime"),
        },
    )
    avoidance_range: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50A9BD0D, original_name="AvoidanceRange"),
        },
    )
    hearing_radius: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED69488F, original_name="HearingRadius"),
        },
    )
    recheck_path_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9AA90B6B, original_name="RecheckPathTime"),
        },
    )
    recheck_path_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7626EC89, original_name="RecheckPathDistance"),
        },
    )
    pain_threshold: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x13A15B89, original_name="PainThreshold"),
        },
    )
    unknown_0xa6c1631d: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA6C1631D, original_name="Unknown"),
        },
    )
    unknown_0x312e194a: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x312E194A, original_name="Unknown"),
        },
    )
    unknown_0xc6f92e2f: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6F92E2F, original_name="Unknown"),
        },
    )
    player_scan_delay: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1F844B33, original_name="PlayerScanDelay"),
        },
    )
    unknown_0x108e8ed8: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x108E8ED8, original_name="Unknown"),
        },
    )
    max_fall_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x74CC0CCF, original_name="MaxFallTime"),
        },
    )
    unknown_0xc34bffca: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC34BFFCA, original_name="Unknown"),
        },
    )
    unknown_0xf5aa6363: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF5AA6363, original_name="Unknown"),
        },
    )
    unknown_0xd40c2b10: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD40C2B10, original_name="Unknown"),
        },
    )
    unknown_0x6bbf9cdc: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6BBF9CDC, original_name="Unknown"),
        },
    )
    unknown_0xb2dd7c06: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB2DD7C06, original_name="Unknown"),
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
        if property_count != 59:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B3109A6
        unknown_0x2b3109a6 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB5C37E0
        start_invisible = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FDEE42C
        unknown_0x7fdee42c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x983954AE
        turn_prediction = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86B2B7D7
        spit_prediction = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1D7E06B
        approach_dist = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D6C84CB
        unknown_0x6d6c84cb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF2782501
        jump_apex = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0236C750
        min_spit_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17BD13A2
        max_spit_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6055F35
        unknown_0xb6055f35 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DAC116A
        spit_starting = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AAB30F1
        spit_full_speed = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76B1B8E0
        launch_projectile_data_0x76b1b8e0 = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE3B5965
        launch_projectile_data_0xfe3b5965 = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95EAAACB
        caud = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4C88DD1
        sound_teleport_end = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE68CEBB0
        max_head_rotation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B7FCF8C
        head_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F5A3164
        unknown_0x0f5a3164 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x190D9FC8
        unknown_0x190d9fc8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFCAE3411
        unknown_0xfcae3411 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ECB92CA
        unknown_0x7ecb92ca = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF201BFA
        burn_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF495AAB
        burn_damage_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D518FD5
        shockwave_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F2FA713
        shockwave_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA42DBD9E
        shockwave_intensity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB39833C0
        unknown_0xb39833c0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96BD6426
        unknown_0x96bd6426 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD7AA5BA0
        unknown_0xd7aa5ba0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2050F248
        blink_out = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9CB2109A
        blink_bubble = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4CE0D7E5
        min_bubble_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F46CF01
        max_bubble_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FC0B9E3
        min_blink_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E5F1638
        unknown_0x8e5f1638 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF7BA9E21
        warp_increase_intensity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E501419
        warp_intensity_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22794C6D
        unknown_0x22794c6d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B9CC474
        unknown_0x5b9cc474 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08F1E9D3
        warp_duration_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51BB4B6F
        frozen_gib_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50A9BD0D
        avoidance_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED69488F
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AA90B6B
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626EC89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13A15B89
        pain_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6C1631D
        unknown_0xa6c1631d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x312E194A
        unknown_0x312e194a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6F92E2F
        unknown_0xc6f92e2f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F844B33
        player_scan_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x108E8ED8
        unknown_0x108e8ed8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74CC0CCF
        max_fall_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC34BFFCA
        unknown_0xc34bffca = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5AA6363
        unknown_0xf5aa6363 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD40C2B10
        unknown_0xd40c2b10 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BBF9CDC
        unknown_0x6bbf9cdc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2DD7C06
        unknown_0xb2dd7c06 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            unknown_0x2b3109a6,
            start_invisible,
            unknown_0x7fdee42c,
            turn_prediction,
            spit_prediction,
            approach_dist,
            unknown_0x6d6c84cb,
            jump_apex,
            min_spit_range,
            max_spit_range,
            unknown_0xb6055f35,
            spit_starting,
            spit_full_speed,
            launch_projectile_data_0x76b1b8e0,
            launch_projectile_data_0xfe3b5965,
            caud,
            sound_teleport_end,
            max_head_rotation,
            head_rotation_speed,
            unknown_0x0f5a3164,
            unknown_0x190d9fc8,
            unknown_0xfcae3411,
            unknown_0x7ecb92ca,
            burn_damage,
            burn_damage_duration,
            shockwave_range,
            shockwave_damage,
            shockwave_intensity,
            unknown_0xb39833c0,
            unknown_0x96bd6426,
            unknown_0xd7aa5ba0,
            blink_out,
            blink_bubble,
            min_bubble_time,
            max_bubble_time,
            min_blink_range,
            unknown_0x8e5f1638,
            warp_increase_intensity,
            warp_intensity_max,
            unknown_0x22794c6d,
            unknown_0x5b9cc474,
            warp_duration_max,
            frozen_gib_time,
            avoidance_range,
            hearing_radius,
            recheck_path_time,
            recheck_path_distance,
            pain_threshold,
            unknown_0xa6c1631d,
            unknown_0x312e194a,
            unknown_0xc6f92e2f,
            player_scan_delay,
            unknown_0x108e8ed8,
            max_fall_time,
            unknown_0xc34bffca,
            unknown_0xf5aa6363,
            unknown_0xd40c2b10,
            unknown_0x6bbf9cdc,
            unknown_0xb2dd7c06,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00;")  # 59 properties

        data.write(b"+1\t\xa6")  # 0x2b3109a6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2b3109a6))

        data.write(b"\xbb\\7\xe0")  # 0xbb5c37e0
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.start_invisible))

        data.write(b"\x7f\xde\xe4,")  # 0x7fdee42c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7fdee42c))

        data.write(b"\x989T\xae")  # 0x983954ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_prediction))

        data.write(b"\x86\xb2\xb7\xd7")  # 0x86b2b7d7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.spit_prediction))

        data.write(b"\xa1\xd7\xe0k")  # 0xa1d7e06b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.approach_dist))

        data.write(b"ml\x84\xcb")  # 0x6d6c84cb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6d6c84cb))

        data.write(b"\xf2x%\x01")  # 0xf2782501
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.jump_apex))

        data.write(b"\x026\xc7P")  # 0x236c750
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_spit_range))

        data.write(b"\x17\xbd\x13\xa2")  # 0x17bd13a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_spit_range))

        data.write(b"\xb6\x05_5")  # 0xb6055f35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb6055f35))

        data.write(b"m\xac\x11j")  # 0x6dac116a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spit_starting.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9a\xab0\xf1")  # 0x9aab30f1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spit_full_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"v\xb1\xb8\xe0")  # 0x76b1b8e0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x76b1b8e0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfe;Ye")  # 0xfe3b5965
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0xfe3b5965.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95\xea\xaa\xcb")  # 0x95eaaacb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud))

        data.write(b"\xd4\xc8\x8d\xd1")  # 0xd4c88dd1
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_teleport_end))

        data.write(b"\xe6\x8c\xeb\xb0")  # 0xe68cebb0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_head_rotation))

        data.write(b"\x8b\x7f\xcf\x8c")  # 0x8b7fcf8c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.head_rotation_speed))

        data.write(b"\x0fZ1d")  # 0xf5a3164
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0f5a3164))

        data.write(b"\x19\r\x9f\xc8")  # 0x190d9fc8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x190d9fc8))

        data.write(b"\xfc\xae4\x11")  # 0xfcae3411
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfcae3411))

        data.write(b"~\xcb\x92\xca")  # 0x7ecb92ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7ecb92ca))

        data.write(b"\xcf \x1b\xfa")  # 0xcf201bfa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.burn_damage))

        data.write(b"\xcfIZ\xab")  # 0xcf495aab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.burn_damage_duration))

        data.write(b"\x8dQ\x8f\xd5")  # 0x8d518fd5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shockwave_range))

        data.write(b"\x0f/\xa7\x13")  # 0xf2fa713
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shockwave_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa4-\xbd\x9e")  # 0xa42dbd9e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shockwave_intensity))

        data.write(b"\xb3\x983\xc0")  # 0xb39833c0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb39833c0))

        data.write(b"\x96\xbdd&")  # 0x96bd6426
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x96bd6426))

        data.write(b"\xd7\xaa[\xa0")  # 0xd7aa5ba0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd7aa5ba0))

        data.write(b" P\xf2H")  # 0x2050f248
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.blink_out))

        data.write(b"\x9c\xb2\x10\x9a")  # 0x9cb2109a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.blink_bubble))

        data.write(b"L\xe0\xd7\xe5")  # 0x4ce0d7e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_bubble_time))

        data.write(b"\x1fF\xcf\x01")  # 0x1f46cf01
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_bubble_time))

        data.write(b"\x0f\xc0\xb9\xe3")  # 0xfc0b9e3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_blink_range))

        data.write(b"\x8e_\x168")  # 0x8e5f1638
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8e5f1638))

        data.write(b"\xf7\xba\x9e!")  # 0xf7ba9e21
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.warp_increase_intensity))

        data.write(b"\x1eP\x14\x19")  # 0x1e501419
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.warp_intensity_max))

        data.write(b'"yLm')  # 0x22794c6d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x22794c6d))

        data.write(b"[\x9c\xc4t")  # 0x5b9cc474
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5b9cc474))

        data.write(b"\x08\xf1\xe9\xd3")  # 0x8f1e9d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.warp_duration_max))

        data.write(b"Q\xbbKo")  # 0x51bb4b6f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.frozen_gib_time))

        data.write(b"P\xa9\xbd\r")  # 0x50a9bd0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.avoidance_range))

        data.write(b"\xediH\x8f")  # 0xed69488f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b"\x9a\xa9\x0bk")  # 0x9aa90b6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b"v&\xec\x89")  # 0x7626ec89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b"\x13\xa1[\x89")  # 0x13a15b89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pain_threshold))

        data.write(b"\xa6\xc1c\x1d")  # 0xa6c1631d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa6c1631d))

        data.write(b"1.\x19J")  # 0x312e194a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x312e194a))

        data.write(b"\xc6\xf9./")  # 0xc6f92e2f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc6f92e2f))

        data.write(b"\x1f\x84K3")  # 0x1f844b33
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_scan_delay))

        data.write(b"\x10\x8e\x8e\xd8")  # 0x108e8ed8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x108e8ed8))

        data.write(b"t\xcc\x0c\xcf")  # 0x74cc0ccf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_fall_time))

        data.write(b"\xc3K\xff\xca")  # 0xc34bffca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc34bffca))

        data.write(b"\xf5\xaacc")  # 0xf5aa6363
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf5aa6363))

        data.write(b"\xd4\x0c+\x10")  # 0xd40c2b10
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd40c2b10))

        data.write(b"k\xbf\x9c\xdc")  # 0x6bbf9cdc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6bbf9cdc))

        data.write(b"\xb2\xdd|\x06")  # 0xb2dd7c06
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb2dd7c06))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BlinkWolfDataJson", data)
        return cls(
            unknown_0x2b3109a6=json_data["unknown_0x2b3109a6"],
            start_invisible=json_data["start_invisible"],
            unknown_0x7fdee42c=json_data["unknown_0x7fdee42c"],
            turn_prediction=json_data["turn_prediction"],
            spit_prediction=json_data["spit_prediction"],
            approach_dist=json_data["approach_dist"],
            unknown_0x6d6c84cb=json_data["unknown_0x6d6c84cb"],
            jump_apex=json_data["jump_apex"],
            min_spit_range=json_data["min_spit_range"],
            max_spit_range=json_data["max_spit_range"],
            unknown_0xb6055f35=json_data["unknown_0xb6055f35"],
            spit_starting=LaunchProjectileData.from_json(json_data["spit_starting"]),
            spit_full_speed=LaunchProjectileData.from_json(json_data["spit_full_speed"]),
            launch_projectile_data_0x76b1b8e0=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x76b1b8e0"]
            ),
            launch_projectile_data_0xfe3b5965=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0xfe3b5965"]
            ),
            caud=json_data["caud"],
            sound_teleport_end=json_data["sound_teleport_end"],
            max_head_rotation=json_data["max_head_rotation"],
            head_rotation_speed=json_data["head_rotation_speed"],
            unknown_0x0f5a3164=json_data["unknown_0x0f5a3164"],
            unknown_0x190d9fc8=json_data["unknown_0x190d9fc8"],
            unknown_0xfcae3411=json_data["unknown_0xfcae3411"],
            unknown_0x7ecb92ca=json_data["unknown_0x7ecb92ca"],
            burn_damage=json_data["burn_damage"],
            burn_damage_duration=json_data["burn_damage_duration"],
            shockwave_range=json_data["shockwave_range"],
            shockwave_damage=DamageInfo.from_json(json_data["shockwave_damage"]),
            shockwave_intensity=json_data["shockwave_intensity"],
            unknown_0xb39833c0=json_data["unknown_0xb39833c0"],
            unknown_0x96bd6426=json_data["unknown_0x96bd6426"],
            unknown_0xd7aa5ba0=json_data["unknown_0xd7aa5ba0"],
            blink_out=json_data["blink_out"],
            blink_bubble=json_data["blink_bubble"],
            min_bubble_time=json_data["min_bubble_time"],
            max_bubble_time=json_data["max_bubble_time"],
            min_blink_range=json_data["min_blink_range"],
            unknown_0x8e5f1638=json_data["unknown_0x8e5f1638"],
            warp_increase_intensity=json_data["warp_increase_intensity"],
            warp_intensity_max=json_data["warp_intensity_max"],
            unknown_0x22794c6d=json_data["unknown_0x22794c6d"],
            unknown_0x5b9cc474=json_data["unknown_0x5b9cc474"],
            warp_duration_max=json_data["warp_duration_max"],
            frozen_gib_time=json_data["frozen_gib_time"],
            avoidance_range=json_data["avoidance_range"],
            hearing_radius=json_data["hearing_radius"],
            recheck_path_time=json_data["recheck_path_time"],
            recheck_path_distance=json_data["recheck_path_distance"],
            pain_threshold=json_data["pain_threshold"],
            unknown_0xa6c1631d=json_data["unknown_0xa6c1631d"],
            unknown_0x312e194a=json_data["unknown_0x312e194a"],
            unknown_0xc6f92e2f=json_data["unknown_0xc6f92e2f"],
            player_scan_delay=json_data["player_scan_delay"],
            unknown_0x108e8ed8=json_data["unknown_0x108e8ed8"],
            max_fall_time=json_data["max_fall_time"],
            unknown_0xc34bffca=json_data["unknown_0xc34bffca"],
            unknown_0xf5aa6363=json_data["unknown_0xf5aa6363"],
            unknown_0xd40c2b10=json_data["unknown_0xd40c2b10"],
            unknown_0x6bbf9cdc=json_data["unknown_0x6bbf9cdc"],
            unknown_0xb2dd7c06=json_data["unknown_0xb2dd7c06"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x2b3109a6": self.unknown_0x2b3109a6,
            "start_invisible": self.start_invisible,
            "unknown_0x7fdee42c": self.unknown_0x7fdee42c,
            "turn_prediction": self.turn_prediction,
            "spit_prediction": self.spit_prediction,
            "approach_dist": self.approach_dist,
            "unknown_0x6d6c84cb": self.unknown_0x6d6c84cb,
            "jump_apex": self.jump_apex,
            "min_spit_range": self.min_spit_range,
            "max_spit_range": self.max_spit_range,
            "unknown_0xb6055f35": self.unknown_0xb6055f35,
            "spit_starting": self.spit_starting.to_json(),
            "spit_full_speed": self.spit_full_speed.to_json(),
            "launch_projectile_data_0x76b1b8e0": self.launch_projectile_data_0x76b1b8e0.to_json(),
            "launch_projectile_data_0xfe3b5965": self.launch_projectile_data_0xfe3b5965.to_json(),
            "caud": self.caud,
            "sound_teleport_end": self.sound_teleport_end,
            "max_head_rotation": self.max_head_rotation,
            "head_rotation_speed": self.head_rotation_speed,
            "unknown_0x0f5a3164": self.unknown_0x0f5a3164,
            "unknown_0x190d9fc8": self.unknown_0x190d9fc8,
            "unknown_0xfcae3411": self.unknown_0xfcae3411,
            "unknown_0x7ecb92ca": self.unknown_0x7ecb92ca,
            "burn_damage": self.burn_damage,
            "burn_damage_duration": self.burn_damage_duration,
            "shockwave_range": self.shockwave_range,
            "shockwave_damage": self.shockwave_damage.to_json(),
            "shockwave_intensity": self.shockwave_intensity,
            "unknown_0xb39833c0": self.unknown_0xb39833c0,
            "unknown_0x96bd6426": self.unknown_0x96bd6426,
            "unknown_0xd7aa5ba0": self.unknown_0xd7aa5ba0,
            "blink_out": self.blink_out,
            "blink_bubble": self.blink_bubble,
            "min_bubble_time": self.min_bubble_time,
            "max_bubble_time": self.max_bubble_time,
            "min_blink_range": self.min_blink_range,
            "unknown_0x8e5f1638": self.unknown_0x8e5f1638,
            "warp_increase_intensity": self.warp_increase_intensity,
            "warp_intensity_max": self.warp_intensity_max,
            "unknown_0x22794c6d": self.unknown_0x22794c6d,
            "unknown_0x5b9cc474": self.unknown_0x5b9cc474,
            "warp_duration_max": self.warp_duration_max,
            "frozen_gib_time": self.frozen_gib_time,
            "avoidance_range": self.avoidance_range,
            "hearing_radius": self.hearing_radius,
            "recheck_path_time": self.recheck_path_time,
            "recheck_path_distance": self.recheck_path_distance,
            "pain_threshold": self.pain_threshold,
            "unknown_0xa6c1631d": self.unknown_0xa6c1631d,
            "unknown_0x312e194a": self.unknown_0x312e194a,
            "unknown_0xc6f92e2f": self.unknown_0xc6f92e2f,
            "player_scan_delay": self.player_scan_delay,
            "unknown_0x108e8ed8": self.unknown_0x108e8ed8,
            "max_fall_time": self.max_fall_time,
            "unknown_0xc34bffca": self.unknown_0xc34bffca,
            "unknown_0xf5aa6363": self.unknown_0xf5aa6363,
            "unknown_0xd40c2b10": self.unknown_0xd40c2b10,
            "unknown_0x6bbf9cdc": self.unknown_0x6bbf9cdc,
            "unknown_0xb2dd7c06": self.unknown_0xb2dd7c06,
        }


def _decode_spit_starting(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_spit_full_speed(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x76b1b8e0(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0xfe3b5965(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_shockwave_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2B3109A6: ("unknown_0x2b3109a6", structs.decode_BIG_bool_),
    0xBB5C37E0: ("start_invisible", structs.decode_BIG_bool_),
    0x7FDEE42C: ("unknown_0x7fdee42c", structs.decode_BIG_f),
    0x983954AE: ("turn_prediction", structs.decode_BIG_f),
    0x86B2B7D7: ("spit_prediction", structs.decode_BIG_f),
    0xA1D7E06B: ("approach_dist", structs.decode_BIG_f),
    0x6D6C84CB: ("unknown_0x6d6c84cb", structs.decode_BIG_f),
    0xF2782501: ("jump_apex", structs.decode_BIG_f),
    0x0236C750: ("min_spit_range", structs.decode_BIG_f),
    0x17BD13A2: ("max_spit_range", structs.decode_BIG_f),
    0xB6055F35: ("unknown_0xb6055f35", structs.decode_BIG_l),
    0x6DAC116A: ("spit_starting", _decode_spit_starting),
    0x9AAB30F1: ("spit_full_speed", _decode_spit_full_speed),
    0x76B1B8E0: ("launch_projectile_data_0x76b1b8e0", _decode_launch_projectile_data_0x76b1b8e0),
    0xFE3B5965: ("launch_projectile_data_0xfe3b5965", _decode_launch_projectile_data_0xfe3b5965),
    0x95EAAACB: ("caud", structs.decode_BIG_Q),
    0xD4C88DD1: ("sound_teleport_end", structs.decode_BIG_Q),
    0xE68CEBB0: ("max_head_rotation", structs.decode_BIG_f),
    0x8B7FCF8C: ("head_rotation_speed", structs.decode_BIG_f),
    0x0F5A3164: ("unknown_0x0f5a3164", structs.decode_BIG_f),
    0x190D9FC8: ("unknown_0x190d9fc8", structs.decode_BIG_f),
    0xFCAE3411: ("unknown_0xfcae3411", structs.decode_BIG_f),
    0x7ECB92CA: ("unknown_0x7ecb92ca", structs.decode_BIG_f),
    0xCF201BFA: ("burn_damage", structs.decode_BIG_f),
    0xCF495AAB: ("burn_damage_duration", structs.decode_BIG_f),
    0x8D518FD5: ("shockwave_range", structs.decode_BIG_f),
    0x0F2FA713: ("shockwave_damage", _decode_shockwave_damage),
    0xA42DBD9E: ("shockwave_intensity", structs.decode_BIG_f),
    0xB39833C0: ("unknown_0xb39833c0", structs.decode_BIG_f),
    0x96BD6426: ("unknown_0x96bd6426", structs.decode_BIG_f),
    0xD7AA5BA0: ("unknown_0xd7aa5ba0", structs.decode_BIG_f),
    0x2050F248: ("blink_out", structs.decode_BIG_Q),
    0x9CB2109A: ("blink_bubble", structs.decode_BIG_Q),
    0x4CE0D7E5: ("min_bubble_time", structs.decode_BIG_f),
    0x1F46CF01: ("max_bubble_time", structs.decode_BIG_f),
    0x0FC0B9E3: ("min_blink_range", structs.decode_BIG_f),
    0x8E5F1638: ("unknown_0x8e5f1638", structs.decode_BIG_f),
    0xF7BA9E21: ("warp_increase_intensity", structs.decode_BIG_f),
    0x1E501419: ("warp_intensity_max", structs.decode_BIG_f),
    0x22794C6D: ("unknown_0x22794c6d", structs.decode_BIG_f),
    0x5B9CC474: ("unknown_0x5b9cc474", structs.decode_BIG_f),
    0x08F1E9D3: ("warp_duration_max", structs.decode_BIG_f),
    0x51BB4B6F: ("frozen_gib_time", structs.decode_BIG_f),
    0x50A9BD0D: ("avoidance_range", structs.decode_BIG_f),
    0xED69488F: ("hearing_radius", structs.decode_BIG_f),
    0x9AA90B6B: ("recheck_path_time", structs.decode_BIG_f),
    0x7626EC89: ("recheck_path_distance", structs.decode_BIG_f),
    0x13A15B89: ("pain_threshold", structs.decode_BIG_f),
    0xA6C1631D: ("unknown_0xa6c1631d", structs.decode_BIG_f),
    0x312E194A: ("unknown_0x312e194a", structs.decode_BIG_f),
    0xC6F92E2F: ("unknown_0xc6f92e2f", structs.decode_BIG_f),
    0x1F844B33: ("player_scan_delay", structs.decode_BIG_f),
    0x108E8ED8: ("unknown_0x108e8ed8", structs.decode_BIG_f),
    0x74CC0CCF: ("max_fall_time", structs.decode_BIG_f),
    0xC34BFFCA: ("unknown_0xc34bffca", structs.decode_BIG_f),
    0xF5AA6363: ("unknown_0xf5aa6363", structs.decode_BIG_f),
    0xD40C2B10: ("unknown_0xd40c2b10", structs.decode_BIG_f),
    0x6BBF9CDC: ("unknown_0x6bbf9cdc", structs.decode_BIG_f),
    0xB2DD7C06: ("unknown_0xb2dd7c06", structs.decode_BIG_f),
}
