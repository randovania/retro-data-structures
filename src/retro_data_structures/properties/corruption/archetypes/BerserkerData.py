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
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BerserkerDataJson(typing_extensions.TypedDict):
        turn_threshold: float
        unknown_0x76ebc21a: bool
        melee_attack_range: float
        unknown_0xc4db42e3: bool
        ball_slam_damage: json_util.JsonObject
        damage_info_0xbb7977b9: json_util.JsonObject
        ground_pound_damage: json_util.JsonObject
        pirate_as_projectile_damage: json_util.JsonObject
        phazon_cannon_beam_info: json_util.JsonObject
        damage_info_0x97321af1: json_util.JsonObject
        unknown_0xfd5e7062: float
        unknown_0xbd110814: float
        unknown_0x3d947337: float
        unknown_0x1a975a02: float
        launch_projectile_data_0x066bc855: json_util.JsonObject
        unknown_0x67e0e4b4: float
        unknown_0xb7ad7067: float
        unknown_0xf7e20811: float
        unknown_0x4db474b8: float
        unknown_0x68d3daa4: json_util.JsonObject
        unknown_0x1b359207: float
        unknown_0xc12f397a: float
        unknown_0x4bfee56b: float
        unknown_0x8f3be6e1: float
        unknown_0xdd825dc3: float
        unknown_0x869415a3: float
        unknown_0xc6db6dd5: float
        phazon_grapple_time: float
        unknown_0x58e6d9b8: float
        unknown_0xcf111a99: float
        phazon_grapple_damage: json_util.JsonObject
        unknown_0x92f0b2c7: float
        unknown_0xbc2f8f30: float
        unknown_0x910ad1e0: float
        unknown_0x4566b3ef: float
        approach_player_chance: float
        unknown_0x24f779ca: float
        armored_vulnerability: json_util.JsonObject
        armor_health: float
        armor_model1: int
        armor_model2: int
        armor_model3: int
        armor_model4: int
        armor_model5: int
        unknown_0x09e8c7fd: float
        weak_spot_model: int
        provoked_head_vulnerability: json_util.JsonObject
        unknown_0x69d66ec4: float
        unknown_0x299916b2: float
        launch_projectile_data_0xfe51924e: json_util.JsonObject
        launch_projectile_data_0x9b9c702c: json_util.JsonObject
        launch_projectile_data_0x567ba94a: json_util.JsonObject
        launch_projectile_data_0xf4d5150f: json_util.JsonObject
        launch_projectile_data_0x8647c581: json_util.JsonObject
        unknown_0x15d26d26: float
        unknown_0x81eaa9d4: float
        is_gandrayda: bool
        is_chieftain: bool
        shoulder_vulnerability: json_util.JsonObject
        shoulder_health: float
        unknown_0x268e5cb2: float
        left_shoulder_model: int
        right_shoulder_model: int
        weak_spot_armored_vulnerability: json_util.JsonObject
        damage_vulnerability_0x200545bd: json_util.JsonObject
        damage_vulnerability_0xf3ea94dc: json_util.JsonObject
        unknown_0xedf1189f: bool
        minor_shockwave: json_util.JsonObject
        shock_wave_info: json_util.JsonObject
        unknown_0x0c1a5644: float
        unknown_0xc6af2fd0: float


@dataclasses.dataclass()
class BerserkerData(BaseProperty):
    turn_threshold: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC0AC271E, original_name="TurnThreshold"),
        },
    )
    unknown_0x76ebc21a: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x76EBC21A, original_name="Unknown"),
        },
    )
    melee_attack_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3E43D0E, original_name="MeleeAttackRange"),
        },
    )
    unknown_0xc4db42e3: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC4DB42E3, original_name="Unknown"),
        },
    )
    ball_slam_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x74BFFA78,
                original_name="BallSlamDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0xbb7977b9: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xBB7977B9,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    ground_pound_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4738C321,
                original_name="GroundPoundDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    pirate_as_projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xF4E003C1,
                original_name="PirateAsProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    phazon_cannon_beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0xE0DBF22F,
                original_name="PhazonCannonBeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    damage_info_0x97321af1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x97321AF1,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xfd5e7062: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFD5E7062, original_name="Unknown"),
        },
    )
    unknown_0xbd110814: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBD110814, original_name="Unknown"),
        },
    )
    unknown_0x3d947337: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3D947337, original_name="Unknown"),
        },
    )
    unknown_0x1a975a02: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A975A02, original_name="Unknown"),
        },
    )
    launch_projectile_data_0x066bc855: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x066BC855,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    unknown_0x67e0e4b4: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x67E0E4B4, original_name="Unknown"),
        },
    )
    unknown_0xb7ad7067: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB7AD7067, original_name="Unknown"),
        },
    )
    unknown_0xf7e20811: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF7E20811, original_name="Unknown"),
        },
    )
    unknown_0x4db474b8: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4DB474B8, original_name="Unknown"),
        },
    )
    unknown_0x68d3daa4: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x68D3DAA4, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x1b359207: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B359207, original_name="Unknown"),
        },
    )
    unknown_0xc12f397a: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC12F397A, original_name="Unknown"),
        },
    )
    unknown_0x4bfee56b: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4BFEE56B, original_name="Unknown"),
        },
    )
    unknown_0x8f3be6e1: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8F3BE6E1, original_name="Unknown"),
        },
    )
    unknown_0xdd825dc3: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDD825DC3, original_name="Unknown"),
        },
    )
    unknown_0x869415a3: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x869415A3, original_name="Unknown"),
        },
    )
    unknown_0xc6db6dd5: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6DB6DD5, original_name="Unknown"),
        },
    )
    phazon_grapple_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDC8D7887, original_name="PhazonGrappleTime"),
        },
    )
    unknown_0x58e6d9b8: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x58E6D9B8, original_name="Unknown"),
        },
    )
    unknown_0xcf111a99: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF111A99, original_name="Unknown"),
        },
    )
    phazon_grapple_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x719FD06B,
                original_name="PhazonGrappleDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x92f0b2c7: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x92F0B2C7, original_name="Unknown"),
        },
    )
    unknown_0xbc2f8f30: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC2F8F30, original_name="Unknown"),
        },
    )
    unknown_0x910ad1e0: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x910AD1E0, original_name="Unknown"),
        },
    )
    unknown_0x4566b3ef: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4566B3EF, original_name="Unknown"),
        },
    )
    approach_player_chance: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6FE50D32, original_name="ApproachPlayerChance"),
        },
    )
    unknown_0x24f779ca: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0x24F779CA, original_name="Unknown"),
        },
    )
    armored_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xC6BA9753,
                original_name="ArmoredVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    armor_health: float = dataclasses.field(
        default=500.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x83439084, original_name="ArmorHealth"),
        },
    )
    armor_model1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x04547D34, original_name="ArmorModel1"),
        },
    )
    armor_model2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x82C00F9A, original_name="ArmorModel2"),
        },
    )
    armor_model3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x499CDC3F, original_name="ArmorModel3"),
        },
    )
    armor_model4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5499EC87, original_name="ArmorModel4"),
        },
    )
    armor_model5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9FC53F22, original_name="ArmorModel5"),
        },
    )
    unknown_0x09e8c7fd: float = dataclasses.field(
        default=1.399999976158142,
        metadata={
            "reflection": FieldReflection[float](float, id=0x09E8C7FD, original_name="Unknown"),
        },
    )
    weak_spot_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4AE57FEB, original_name="WeakSpotModel"),
        },
    )
    provoked_head_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x4E1D71A1,
                original_name="ProvokedHeadVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0x69d66ec4: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x69D66EC4, original_name="Unknown"),
        },
    )
    unknown_0x299916b2: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x299916B2, original_name="Unknown"),
        },
    )
    launch_projectile_data_0xfe51924e: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0xFE51924E,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    launch_projectile_data_0x9b9c702c: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x9B9C702C,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    launch_projectile_data_0x567ba94a: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x567BA94A,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    launch_projectile_data_0xf4d5150f: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0xF4D5150F,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    launch_projectile_data_0x8647c581: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x8647C581,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    unknown_0x15d26d26: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x15D26D26, original_name="Unknown"),
        },
    )
    unknown_0x81eaa9d4: float = dataclasses.field(
        default=250.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x81EAA9D4, original_name="Unknown"),
        },
    )
    is_gandrayda: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x531A8C85, original_name="IsGandrayda"),
        },
    )
    is_chieftain: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x677BD8AB, original_name="IsChieftain"),
        },
    )
    shoulder_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xC6E6300F,
                original_name="ShoulderVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    shoulder_health: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1520568A, original_name="ShoulderHealth"),
        },
    )
    unknown_0x268e5cb2: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x268E5CB2, original_name="Unknown"),
        },
    )
    left_shoulder_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x650BA238, original_name="LeftShoulderModel"),
        },
    )
    right_shoulder_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x68865410, original_name="RightShoulderModel"),
        },
    )
    weak_spot_armored_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x342DAE7A,
                original_name="WeakSpotArmoredVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    damage_vulnerability_0x200545bd: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x200545BD,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    damage_vulnerability_0xf3ea94dc: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xF3EA94DC,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0xedf1189f: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEDF1189F, original_name="Unknown"),
        },
    )
    minor_shockwave: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x846533CC,
                original_name="MinorShockwave",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x2AF1548B,
                original_name="ShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    unknown_0x0c1a5644: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0C1A5644, original_name="Unknown"),
        },
    )
    unknown_0xc6af2fd0: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6AF2FD0, original_name="Unknown"),
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
        if property_count != 71:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC0AC271E
        turn_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76EBC21A
        unknown_0x76ebc21a = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3E43D0E
        melee_attack_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4DB42E3
        unknown_0xc4db42e3 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74BFFA78
        ball_slam_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB7977B9
        damage_info_0xbb7977b9 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4738C321
        ground_pound_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4E003C1
        pirate_as_projectile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0DBF22F
        phazon_cannon_beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97321AF1
        damage_info_0x97321af1 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFD5E7062
        unknown_0xfd5e7062 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD110814
        unknown_0xbd110814 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D947337
        unknown_0x3d947337 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A975A02
        unknown_0x1a975a02 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x066BC855
        launch_projectile_data_0x066bc855 = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67E0E4B4
        unknown_0x67e0e4b4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7AD7067
        unknown_0xb7ad7067 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF7E20811
        unknown_0xf7e20811 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4DB474B8
        unknown_0x4db474b8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68D3DAA4
        unknown_0x68d3daa4 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B359207
        unknown_0x1b359207 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC12F397A
        unknown_0xc12f397a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4BFEE56B
        unknown_0x4bfee56b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F3BE6E1
        unknown_0x8f3be6e1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD825DC3
        unknown_0xdd825dc3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x869415A3
        unknown_0x869415a3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6DB6DD5
        unknown_0xc6db6dd5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC8D7887
        phazon_grapple_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58E6D9B8
        unknown_0x58e6d9b8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF111A99
        unknown_0xcf111a99 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x719FD06B
        phazon_grapple_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92F0B2C7
        unknown_0x92f0b2c7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC2F8F30
        unknown_0xbc2f8f30 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x910AD1E0
        unknown_0x910ad1e0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4566B3EF
        unknown_0x4566b3ef = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6FE50D32
        approach_player_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24F779CA
        unknown_0x24f779ca = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6BA9753
        armored_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83439084
        armor_health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04547D34
        armor_model1 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82C00F9A
        armor_model2 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x499CDC3F
        armor_model3 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5499EC87
        armor_model4 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9FC53F22
        armor_model5 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09E8C7FD
        unknown_0x09e8c7fd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AE57FEB
        weak_spot_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4E1D71A1
        provoked_head_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69D66EC4
        unknown_0x69d66ec4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x299916B2
        unknown_0x299916b2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE51924E
        launch_projectile_data_0xfe51924e = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B9C702C
        launch_projectile_data_0x9b9c702c = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x567BA94A
        launch_projectile_data_0x567ba94a = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4D5150F
        launch_projectile_data_0xf4d5150f = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8647C581
        launch_projectile_data_0x8647c581 = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15D26D26
        unknown_0x15d26d26 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81EAA9D4
        unknown_0x81eaa9d4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531A8C85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x677BD8AB
        is_chieftain = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6E6300F
        shoulder_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1520568A
        shoulder_health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x268E5CB2
        unknown_0x268e5cb2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x650BA238
        left_shoulder_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68865410
        right_shoulder_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x342DAE7A
        weak_spot_armored_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x200545BD
        damage_vulnerability_0x200545bd = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3EA94DC
        damage_vulnerability_0xf3ea94dc = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDF1189F
        unknown_0xedf1189f = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x846533CC
        minor_shockwave = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2AF1548B
        shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C1A5644
        unknown_0x0c1a5644 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6AF2FD0
        unknown_0xc6af2fd0 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            turn_threshold,
            unknown_0x76ebc21a,
            melee_attack_range,
            unknown_0xc4db42e3,
            ball_slam_damage,
            damage_info_0xbb7977b9,
            ground_pound_damage,
            pirate_as_projectile_damage,
            phazon_cannon_beam_info,
            damage_info_0x97321af1,
            unknown_0xfd5e7062,
            unknown_0xbd110814,
            unknown_0x3d947337,
            unknown_0x1a975a02,
            launch_projectile_data_0x066bc855,
            unknown_0x67e0e4b4,
            unknown_0xb7ad7067,
            unknown_0xf7e20811,
            unknown_0x4db474b8,
            unknown_0x68d3daa4,
            unknown_0x1b359207,
            unknown_0xc12f397a,
            unknown_0x4bfee56b,
            unknown_0x8f3be6e1,
            unknown_0xdd825dc3,
            unknown_0x869415a3,
            unknown_0xc6db6dd5,
            phazon_grapple_time,
            unknown_0x58e6d9b8,
            unknown_0xcf111a99,
            phazon_grapple_damage,
            unknown_0x92f0b2c7,
            unknown_0xbc2f8f30,
            unknown_0x910ad1e0,
            unknown_0x4566b3ef,
            approach_player_chance,
            unknown_0x24f779ca,
            armored_vulnerability,
            armor_health,
            armor_model1,
            armor_model2,
            armor_model3,
            armor_model4,
            armor_model5,
            unknown_0x09e8c7fd,
            weak_spot_model,
            provoked_head_vulnerability,
            unknown_0x69d66ec4,
            unknown_0x299916b2,
            launch_projectile_data_0xfe51924e,
            launch_projectile_data_0x9b9c702c,
            launch_projectile_data_0x567ba94a,
            launch_projectile_data_0xf4d5150f,
            launch_projectile_data_0x8647c581,
            unknown_0x15d26d26,
            unknown_0x81eaa9d4,
            is_gandrayda,
            is_chieftain,
            shoulder_vulnerability,
            shoulder_health,
            unknown_0x268e5cb2,
            left_shoulder_model,
            right_shoulder_model,
            weak_spot_armored_vulnerability,
            damage_vulnerability_0x200545bd,
            damage_vulnerability_0xf3ea94dc,
            unknown_0xedf1189f,
            minor_shockwave,
            shock_wave_info,
            unknown_0x0c1a5644,
            unknown_0xc6af2fd0,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00G")  # 71 properties

        data.write(b"\xc0\xac'\x1e")  # 0xc0ac271e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_threshold))

        data.write(b"v\xeb\xc2\x1a")  # 0x76ebc21a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x76ebc21a))

        data.write(b"\xc3\xe4=\x0e")  # 0xc3e43d0e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_attack_range))

        data.write(b"\xc4\xdbB\xe3")  # 0xc4db42e3
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xc4db42e3))

        data.write(b"t\xbf\xfax")  # 0x74bffa78
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball_slam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbbyw\xb9")  # 0xbb7977b9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0xbb7977b9.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"G8\xc3!")  # 0x4738c321
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ground_pound_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4\xe0\x03\xc1")  # 0xf4e003c1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.pirate_as_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe0\xdb\xf2/")  # 0xe0dbf22f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.phazon_cannon_beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x972\x1a\xf1")  # 0x97321af1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x97321af1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfd^pb")  # 0xfd5e7062
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfd5e7062))

        data.write(b"\xbd\x11\x08\x14")  # 0xbd110814
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbd110814))

        data.write(b"=\x94s7")  # 0x3d947337
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3d947337))

        data.write(b"\x1a\x97Z\x02")  # 0x1a975a02
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1a975a02))

        data.write(b"\x06k\xc8U")  # 0x66bc855
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x066bc855.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"g\xe0\xe4\xb4")  # 0x67e0e4b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x67e0e4b4))

        data.write(b"\xb7\xadpg")  # 0xb7ad7067
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb7ad7067))

        data.write(b"\xf7\xe2\x08\x11")  # 0xf7e20811
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf7e20811))

        data.write(b"M\xb4t\xb8")  # 0x4db474b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4db474b8))

        data.write(b"h\xd3\xda\xa4")  # 0x68d3daa4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x68d3daa4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1b5\x92\x07")  # 0x1b359207
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1b359207))

        data.write(b"\xc1/9z")  # 0xc12f397a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc12f397a))

        data.write(b"K\xfe\xe5k")  # 0x4bfee56b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4bfee56b))

        data.write(b"\x8f;\xe6\xe1")  # 0x8f3be6e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8f3be6e1))

        data.write(b"\xdd\x82]\xc3")  # 0xdd825dc3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdd825dc3))

        data.write(b"\x86\x94\x15\xa3")  # 0x869415a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x869415a3))

        data.write(b"\xc6\xdbm\xd5")  # 0xc6db6dd5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc6db6dd5))

        data.write(b"\xdc\x8dx\x87")  # 0xdc8d7887
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phazon_grapple_time))

        data.write(b"X\xe6\xd9\xb8")  # 0x58e6d9b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x58e6d9b8))

        data.write(b"\xcf\x11\x1a\x99")  # 0xcf111a99
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcf111a99))

        data.write(b"q\x9f\xd0k")  # 0x719fd06b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.phazon_grapple_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x92\xf0\xb2\xc7")  # 0x92f0b2c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x92f0b2c7))

        data.write(b"\xbc/\x8f0")  # 0xbc2f8f30
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbc2f8f30))

        data.write(b"\x91\n\xd1\xe0")  # 0x910ad1e0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x910ad1e0))

        data.write(b"Ef\xb3\xef")  # 0x4566b3ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4566b3ef))

        data.write(b"o\xe5\r2")  # 0x6fe50d32
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.approach_player_chance))

        data.write(b"$\xf7y\xca")  # 0x24f779ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x24f779ca))

        data.write(b"\xc6\xba\x97S")  # 0xc6ba9753
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.armored_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x83C\x90\x84")  # 0x83439084
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.armor_health))

        data.write(b"\x04T}4")  # 0x4547d34
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.armor_model1))

        data.write(b"\x82\xc0\x0f\x9a")  # 0x82c00f9a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.armor_model2))

        data.write(b"I\x9c\xdc?")  # 0x499cdc3f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.armor_model3))

        data.write(b"T\x99\xec\x87")  # 0x5499ec87
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.armor_model4))

        data.write(b'\x9f\xc5?"')  # 0x9fc53f22
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.armor_model5))

        data.write(b"\t\xe8\xc7\xfd")  # 0x9e8c7fd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x09e8c7fd))

        data.write(b"J\xe5\x7f\xeb")  # 0x4ae57feb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.weak_spot_model))

        data.write(b"N\x1dq\xa1")  # 0x4e1d71a1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.provoked_head_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"i\xd6n\xc4")  # 0x69d66ec4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x69d66ec4))

        data.write(b")\x99\x16\xb2")  # 0x299916b2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x299916b2))

        data.write(b"\xfeQ\x92N")  # 0xfe51924e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0xfe51924e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9b\x9cp,")  # 0x9b9c702c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x9b9c702c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"V{\xa9J")  # 0x567ba94a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x567ba94a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4\xd5\x15\x0f")  # 0xf4d5150f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0xf4d5150f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x86G\xc5\x81")  # 0x8647c581
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x8647c581.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x15\xd2m&")  # 0x15d26d26
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x15d26d26))

        data.write(b"\x81\xea\xa9\xd4")  # 0x81eaa9d4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x81eaa9d4))

        data.write(b"S\x1a\x8c\x85")  # 0x531a8c85
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b"g{\xd8\xab")  # 0x677bd8ab
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_chieftain))

        data.write(b"\xc6\xe60\x0f")  # 0xc6e6300f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shoulder_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x15 V\x8a")  # 0x1520568a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shoulder_health))

        data.write(b"&\x8e\\\xb2")  # 0x268e5cb2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x268e5cb2))

        data.write(b"e\x0b\xa28")  # 0x650ba238
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_shoulder_model))

        data.write(b"h\x86T\x10")  # 0x68865410
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_shoulder_model))

        data.write(b"4-\xaez")  # 0x342dae7a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weak_spot_armored_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b" \x05E\xbd")  # 0x200545bd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability_0x200545bd.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3\xea\x94\xdc")  # 0xf3ea94dc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability_0xf3ea94dc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\xf1\x18\x9f")  # 0xedf1189f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xedf1189f))

        data.write(b"\x84e3\xcc")  # 0x846533cc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.minor_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"*\xf1T\x8b")  # 0x2af1548b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0c\x1aVD")  # 0xc1a5644
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0c1a5644))

        data.write(b"\xc6\xaf/\xd0")  # 0xc6af2fd0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc6af2fd0))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BerserkerDataJson", data)
        return cls(
            turn_threshold=json_data["turn_threshold"],
            unknown_0x76ebc21a=json_data["unknown_0x76ebc21a"],
            melee_attack_range=json_data["melee_attack_range"],
            unknown_0xc4db42e3=json_data["unknown_0xc4db42e3"],
            ball_slam_damage=DamageInfo.from_json(json_data["ball_slam_damage"]),
            damage_info_0xbb7977b9=DamageInfo.from_json(json_data["damage_info_0xbb7977b9"]),
            ground_pound_damage=DamageInfo.from_json(json_data["ground_pound_damage"]),
            pirate_as_projectile_damage=DamageInfo.from_json(json_data["pirate_as_projectile_damage"]),
            phazon_cannon_beam_info=PlasmaBeamInfo.from_json(json_data["phazon_cannon_beam_info"]),
            damage_info_0x97321af1=DamageInfo.from_json(json_data["damage_info_0x97321af1"]),
            unknown_0xfd5e7062=json_data["unknown_0xfd5e7062"],
            unknown_0xbd110814=json_data["unknown_0xbd110814"],
            unknown_0x3d947337=json_data["unknown_0x3d947337"],
            unknown_0x1a975a02=json_data["unknown_0x1a975a02"],
            launch_projectile_data_0x066bc855=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x066bc855"]
            ),
            unknown_0x67e0e4b4=json_data["unknown_0x67e0e4b4"],
            unknown_0xb7ad7067=json_data["unknown_0xb7ad7067"],
            unknown_0xf7e20811=json_data["unknown_0xf7e20811"],
            unknown_0x4db474b8=json_data["unknown_0x4db474b8"],
            unknown_0x68d3daa4=Spline.from_json(json_data["unknown_0x68d3daa4"]),
            unknown_0x1b359207=json_data["unknown_0x1b359207"],
            unknown_0xc12f397a=json_data["unknown_0xc12f397a"],
            unknown_0x4bfee56b=json_data["unknown_0x4bfee56b"],
            unknown_0x8f3be6e1=json_data["unknown_0x8f3be6e1"],
            unknown_0xdd825dc3=json_data["unknown_0xdd825dc3"],
            unknown_0x869415a3=json_data["unknown_0x869415a3"],
            unknown_0xc6db6dd5=json_data["unknown_0xc6db6dd5"],
            phazon_grapple_time=json_data["phazon_grapple_time"],
            unknown_0x58e6d9b8=json_data["unknown_0x58e6d9b8"],
            unknown_0xcf111a99=json_data["unknown_0xcf111a99"],
            phazon_grapple_damage=DamageInfo.from_json(json_data["phazon_grapple_damage"]),
            unknown_0x92f0b2c7=json_data["unknown_0x92f0b2c7"],
            unknown_0xbc2f8f30=json_data["unknown_0xbc2f8f30"],
            unknown_0x910ad1e0=json_data["unknown_0x910ad1e0"],
            unknown_0x4566b3ef=json_data["unknown_0x4566b3ef"],
            approach_player_chance=json_data["approach_player_chance"],
            unknown_0x24f779ca=json_data["unknown_0x24f779ca"],
            armored_vulnerability=DamageVulnerability.from_json(json_data["armored_vulnerability"]),
            armor_health=json_data["armor_health"],
            armor_model1=json_data["armor_model1"],
            armor_model2=json_data["armor_model2"],
            armor_model3=json_data["armor_model3"],
            armor_model4=json_data["armor_model4"],
            armor_model5=json_data["armor_model5"],
            unknown_0x09e8c7fd=json_data["unknown_0x09e8c7fd"],
            weak_spot_model=json_data["weak_spot_model"],
            provoked_head_vulnerability=DamageVulnerability.from_json(json_data["provoked_head_vulnerability"]),
            unknown_0x69d66ec4=json_data["unknown_0x69d66ec4"],
            unknown_0x299916b2=json_data["unknown_0x299916b2"],
            launch_projectile_data_0xfe51924e=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0xfe51924e"]
            ),
            launch_projectile_data_0x9b9c702c=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x9b9c702c"]
            ),
            launch_projectile_data_0x567ba94a=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x567ba94a"]
            ),
            launch_projectile_data_0xf4d5150f=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0xf4d5150f"]
            ),
            launch_projectile_data_0x8647c581=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x8647c581"]
            ),
            unknown_0x15d26d26=json_data["unknown_0x15d26d26"],
            unknown_0x81eaa9d4=json_data["unknown_0x81eaa9d4"],
            is_gandrayda=json_data["is_gandrayda"],
            is_chieftain=json_data["is_chieftain"],
            shoulder_vulnerability=DamageVulnerability.from_json(json_data["shoulder_vulnerability"]),
            shoulder_health=json_data["shoulder_health"],
            unknown_0x268e5cb2=json_data["unknown_0x268e5cb2"],
            left_shoulder_model=json_data["left_shoulder_model"],
            right_shoulder_model=json_data["right_shoulder_model"],
            weak_spot_armored_vulnerability=DamageVulnerability.from_json(json_data["weak_spot_armored_vulnerability"]),
            damage_vulnerability_0x200545bd=DamageVulnerability.from_json(json_data["damage_vulnerability_0x200545bd"]),
            damage_vulnerability_0xf3ea94dc=DamageVulnerability.from_json(json_data["damage_vulnerability_0xf3ea94dc"]),
            unknown_0xedf1189f=json_data["unknown_0xedf1189f"],
            minor_shockwave=ShockWaveInfo.from_json(json_data["minor_shockwave"]),
            shock_wave_info=ShockWaveInfo.from_json(json_data["shock_wave_info"]),
            unknown_0x0c1a5644=json_data["unknown_0x0c1a5644"],
            unknown_0xc6af2fd0=json_data["unknown_0xc6af2fd0"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "turn_threshold": self.turn_threshold,
            "unknown_0x76ebc21a": self.unknown_0x76ebc21a,
            "melee_attack_range": self.melee_attack_range,
            "unknown_0xc4db42e3": self.unknown_0xc4db42e3,
            "ball_slam_damage": self.ball_slam_damage.to_json(),
            "damage_info_0xbb7977b9": self.damage_info_0xbb7977b9.to_json(),
            "ground_pound_damage": self.ground_pound_damage.to_json(),
            "pirate_as_projectile_damage": self.pirate_as_projectile_damage.to_json(),
            "phazon_cannon_beam_info": self.phazon_cannon_beam_info.to_json(),
            "damage_info_0x97321af1": self.damage_info_0x97321af1.to_json(),
            "unknown_0xfd5e7062": self.unknown_0xfd5e7062,
            "unknown_0xbd110814": self.unknown_0xbd110814,
            "unknown_0x3d947337": self.unknown_0x3d947337,
            "unknown_0x1a975a02": self.unknown_0x1a975a02,
            "launch_projectile_data_0x066bc855": self.launch_projectile_data_0x066bc855.to_json(),
            "unknown_0x67e0e4b4": self.unknown_0x67e0e4b4,
            "unknown_0xb7ad7067": self.unknown_0xb7ad7067,
            "unknown_0xf7e20811": self.unknown_0xf7e20811,
            "unknown_0x4db474b8": self.unknown_0x4db474b8,
            "unknown_0x68d3daa4": self.unknown_0x68d3daa4.to_json(),
            "unknown_0x1b359207": self.unknown_0x1b359207,
            "unknown_0xc12f397a": self.unknown_0xc12f397a,
            "unknown_0x4bfee56b": self.unknown_0x4bfee56b,
            "unknown_0x8f3be6e1": self.unknown_0x8f3be6e1,
            "unknown_0xdd825dc3": self.unknown_0xdd825dc3,
            "unknown_0x869415a3": self.unknown_0x869415a3,
            "unknown_0xc6db6dd5": self.unknown_0xc6db6dd5,
            "phazon_grapple_time": self.phazon_grapple_time,
            "unknown_0x58e6d9b8": self.unknown_0x58e6d9b8,
            "unknown_0xcf111a99": self.unknown_0xcf111a99,
            "phazon_grapple_damage": self.phazon_grapple_damage.to_json(),
            "unknown_0x92f0b2c7": self.unknown_0x92f0b2c7,
            "unknown_0xbc2f8f30": self.unknown_0xbc2f8f30,
            "unknown_0x910ad1e0": self.unknown_0x910ad1e0,
            "unknown_0x4566b3ef": self.unknown_0x4566b3ef,
            "approach_player_chance": self.approach_player_chance,
            "unknown_0x24f779ca": self.unknown_0x24f779ca,
            "armored_vulnerability": self.armored_vulnerability.to_json(),
            "armor_health": self.armor_health,
            "armor_model1": self.armor_model1,
            "armor_model2": self.armor_model2,
            "armor_model3": self.armor_model3,
            "armor_model4": self.armor_model4,
            "armor_model5": self.armor_model5,
            "unknown_0x09e8c7fd": self.unknown_0x09e8c7fd,
            "weak_spot_model": self.weak_spot_model,
            "provoked_head_vulnerability": self.provoked_head_vulnerability.to_json(),
            "unknown_0x69d66ec4": self.unknown_0x69d66ec4,
            "unknown_0x299916b2": self.unknown_0x299916b2,
            "launch_projectile_data_0xfe51924e": self.launch_projectile_data_0xfe51924e.to_json(),
            "launch_projectile_data_0x9b9c702c": self.launch_projectile_data_0x9b9c702c.to_json(),
            "launch_projectile_data_0x567ba94a": self.launch_projectile_data_0x567ba94a.to_json(),
            "launch_projectile_data_0xf4d5150f": self.launch_projectile_data_0xf4d5150f.to_json(),
            "launch_projectile_data_0x8647c581": self.launch_projectile_data_0x8647c581.to_json(),
            "unknown_0x15d26d26": self.unknown_0x15d26d26,
            "unknown_0x81eaa9d4": self.unknown_0x81eaa9d4,
            "is_gandrayda": self.is_gandrayda,
            "is_chieftain": self.is_chieftain,
            "shoulder_vulnerability": self.shoulder_vulnerability.to_json(),
            "shoulder_health": self.shoulder_health,
            "unknown_0x268e5cb2": self.unknown_0x268e5cb2,
            "left_shoulder_model": self.left_shoulder_model,
            "right_shoulder_model": self.right_shoulder_model,
            "weak_spot_armored_vulnerability": self.weak_spot_armored_vulnerability.to_json(),
            "damage_vulnerability_0x200545bd": self.damage_vulnerability_0x200545bd.to_json(),
            "damage_vulnerability_0xf3ea94dc": self.damage_vulnerability_0xf3ea94dc.to_json(),
            "unknown_0xedf1189f": self.unknown_0xedf1189f,
            "minor_shockwave": self.minor_shockwave.to_json(),
            "shock_wave_info": self.shock_wave_info.to_json(),
            "unknown_0x0c1a5644": self.unknown_0x0c1a5644,
            "unknown_0xc6af2fd0": self.unknown_0xc6af2fd0,
        }


def _decode_ball_slam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0xbb7977b9(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ground_pound_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_pirate_as_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_cannon_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x97321af1(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x066bc855(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_unknown_0x68d3daa4(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_phazon_grapple_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_armored_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_provoked_head_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0xfe51924e(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x9b9c702c(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x567ba94a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0xf4d5150f(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x8647c581(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_shoulder_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_weak_spot_armored_vulnerability(
    data: typing.BinaryIO, game: Game, property_size: int
) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_damage_vulnerability_0x200545bd(
    data: typing.BinaryIO, game: Game, property_size: int
) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_damage_vulnerability_0xf3ea94dc(
    data: typing.BinaryIO, game: Game, property_size: int
) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_minor_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC0AC271E: ("turn_threshold", structs.decode_BIG_f),
    0x76EBC21A: ("unknown_0x76ebc21a", structs.decode_BIG_bool_),
    0xC3E43D0E: ("melee_attack_range", structs.decode_BIG_f),
    0xC4DB42E3: ("unknown_0xc4db42e3", structs.decode_BIG_bool_),
    0x74BFFA78: ("ball_slam_damage", _decode_ball_slam_damage),
    0xBB7977B9: ("damage_info_0xbb7977b9", _decode_damage_info_0xbb7977b9),
    0x4738C321: ("ground_pound_damage", _decode_ground_pound_damage),
    0xF4E003C1: ("pirate_as_projectile_damage", _decode_pirate_as_projectile_damage),
    0xE0DBF22F: ("phazon_cannon_beam_info", _decode_phazon_cannon_beam_info),
    0x97321AF1: ("damage_info_0x97321af1", _decode_damage_info_0x97321af1),
    0xFD5E7062: ("unknown_0xfd5e7062", structs.decode_BIG_f),
    0xBD110814: ("unknown_0xbd110814", structs.decode_BIG_f),
    0x3D947337: ("unknown_0x3d947337", structs.decode_BIG_f),
    0x1A975A02: ("unknown_0x1a975a02", structs.decode_BIG_f),
    0x066BC855: ("launch_projectile_data_0x066bc855", _decode_launch_projectile_data_0x066bc855),
    0x67E0E4B4: ("unknown_0x67e0e4b4", structs.decode_BIG_f),
    0xB7AD7067: ("unknown_0xb7ad7067", structs.decode_BIG_f),
    0xF7E20811: ("unknown_0xf7e20811", structs.decode_BIG_f),
    0x4DB474B8: ("unknown_0x4db474b8", structs.decode_BIG_f),
    0x68D3DAA4: ("unknown_0x68d3daa4", _decode_unknown_0x68d3daa4),
    0x1B359207: ("unknown_0x1b359207", structs.decode_BIG_f),
    0xC12F397A: ("unknown_0xc12f397a", structs.decode_BIG_f),
    0x4BFEE56B: ("unknown_0x4bfee56b", structs.decode_BIG_f),
    0x8F3BE6E1: ("unknown_0x8f3be6e1", structs.decode_BIG_f),
    0xDD825DC3: ("unknown_0xdd825dc3", structs.decode_BIG_f),
    0x869415A3: ("unknown_0x869415a3", structs.decode_BIG_f),
    0xC6DB6DD5: ("unknown_0xc6db6dd5", structs.decode_BIG_f),
    0xDC8D7887: ("phazon_grapple_time", structs.decode_BIG_f),
    0x58E6D9B8: ("unknown_0x58e6d9b8", structs.decode_BIG_f),
    0xCF111A99: ("unknown_0xcf111a99", structs.decode_BIG_f),
    0x719FD06B: ("phazon_grapple_damage", _decode_phazon_grapple_damage),
    0x92F0B2C7: ("unknown_0x92f0b2c7", structs.decode_BIG_f),
    0xBC2F8F30: ("unknown_0xbc2f8f30", structs.decode_BIG_f),
    0x910AD1E0: ("unknown_0x910ad1e0", structs.decode_BIG_f),
    0x4566B3EF: ("unknown_0x4566b3ef", structs.decode_BIG_f),
    0x6FE50D32: ("approach_player_chance", structs.decode_BIG_f),
    0x24F779CA: ("unknown_0x24f779ca", structs.decode_BIG_f),
    0xC6BA9753: ("armored_vulnerability", _decode_armored_vulnerability),
    0x83439084: ("armor_health", structs.decode_BIG_f),
    0x04547D34: ("armor_model1", structs.decode_BIG_Q),
    0x82C00F9A: ("armor_model2", structs.decode_BIG_Q),
    0x499CDC3F: ("armor_model3", structs.decode_BIG_Q),
    0x5499EC87: ("armor_model4", structs.decode_BIG_Q),
    0x9FC53F22: ("armor_model5", structs.decode_BIG_Q),
    0x09E8C7FD: ("unknown_0x09e8c7fd", structs.decode_BIG_f),
    0x4AE57FEB: ("weak_spot_model", structs.decode_BIG_Q),
    0x4E1D71A1: ("provoked_head_vulnerability", _decode_provoked_head_vulnerability),
    0x69D66EC4: ("unknown_0x69d66ec4", structs.decode_BIG_f),
    0x299916B2: ("unknown_0x299916b2", structs.decode_BIG_f),
    0xFE51924E: ("launch_projectile_data_0xfe51924e", _decode_launch_projectile_data_0xfe51924e),
    0x9B9C702C: ("launch_projectile_data_0x9b9c702c", _decode_launch_projectile_data_0x9b9c702c),
    0x567BA94A: ("launch_projectile_data_0x567ba94a", _decode_launch_projectile_data_0x567ba94a),
    0xF4D5150F: ("launch_projectile_data_0xf4d5150f", _decode_launch_projectile_data_0xf4d5150f),
    0x8647C581: ("launch_projectile_data_0x8647c581", _decode_launch_projectile_data_0x8647c581),
    0x15D26D26: ("unknown_0x15d26d26", structs.decode_BIG_f),
    0x81EAA9D4: ("unknown_0x81eaa9d4", structs.decode_BIG_f),
    0x531A8C85: ("is_gandrayda", structs.decode_BIG_bool_),
    0x677BD8AB: ("is_chieftain", structs.decode_BIG_bool_),
    0xC6E6300F: ("shoulder_vulnerability", _decode_shoulder_vulnerability),
    0x1520568A: ("shoulder_health", structs.decode_BIG_f),
    0x268E5CB2: ("unknown_0x268e5cb2", structs.decode_BIG_f),
    0x650BA238: ("left_shoulder_model", structs.decode_BIG_Q),
    0x68865410: ("right_shoulder_model", structs.decode_BIG_Q),
    0x342DAE7A: ("weak_spot_armored_vulnerability", _decode_weak_spot_armored_vulnerability),
    0x200545BD: ("damage_vulnerability_0x200545bd", _decode_damage_vulnerability_0x200545bd),
    0xF3EA94DC: ("damage_vulnerability_0xf3ea94dc", _decode_damage_vulnerability_0xf3ea94dc),
    0xEDF1189F: ("unknown_0xedf1189f", structs.decode_BIG_bool_),
    0x846533CC: ("minor_shockwave", _decode_minor_shockwave),
    0x2AF1548B: ("shock_wave_info", _decode_shock_wave_info),
    0x0C1A5644: ("unknown_0x0c1a5644", structs.decode_BIG_f),
    0xC6AF2FD0: ("unknown_0xc6af2fd0", structs.decode_BIG_f),
}
