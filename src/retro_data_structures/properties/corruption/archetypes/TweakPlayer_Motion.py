# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayer_MotionJson(typing_extensions.TypedDict):
        forward_accel_normal: float
        forward_accel_air: float
        forward_accel_ice: float
        forward_accel_organic: float
        forward_accel_water: float
        forward_accel_lava: float
        forward_accel_phazon: float
        forward_accel_shrubbery: float
        rotational_accel_normal: float
        rotational_accel_air: float
        rotational_accel_ice: float
        rotational_accel_organic: float
        rotational_accel_water: float
        rotational_accel_lava: float
        rotational_accel_phazon: float
        rotational_accel_shrubbery: float
        advanced_rotational_accel_normal: float
        advanced_rotational_accel_air: float
        advanced_rotational_accel_ice: float
        advanced_rotational_accel_organic: float
        advanced_rotational_accel_water: float
        advanced_rotational_accel_lava: float
        advanced_rotational_accel_phazon: float
        advanced_rotational_accel_shrubbery: float
        unknown_0x600e90ff: float
        unknown_0x81f724a0: float
        unknown_0xe8b15278: float
        unknown_0x1d85f8ca: float
        unknown_0x09b0e377: float
        unknown_0x2ff175f1: float
        unknown_0x8096f89b: float
        unknown_0x90f35da8: float
        movement_friction_normal: float
        movement_friction_air: float
        movement_friction_ice: float
        movement_friction_organic: float
        movement_friction_water: float
        movement_friction_lava: float
        movement_friction_phazon: float
        movement_friction_shrubbery: float
        rotation_friction_normal: float
        rotation_friction_air: float
        rotation_friction_ice: float
        rotation_friction_organic: float
        rotation_friction_water: float
        rotation_friction_lava: float
        rotation_friction_phazon: float
        rotation_friction_shrubbery: float
        rotation_max_speed_normal: float
        rotation_max_speed_air: float
        rotation_max_speed_ice: float
        rotation_max_speed_organic: float
        rotation_max_speed_water: float
        rotation_max_speed_lava: float
        rotation_max_speed_phazon: float
        rotation_max_speed_shrubbery: float
        advanced_rotation_max_speed_normal: float
        advanced_rotation_max_speed_air: float
        advanced_rotation_max_speed_ice: float
        advanced_rotation_max_speed_organic: float
        advanced_rotation_max_speed_water: float
        advanced_rotation_max_speed_lava: float
        advanced_rotation_max_speed_phazon: float
        advanced_rotation_max_speed_shrubbery: float
        unknown_0xd2caa709: float
        unknown_0x320333aa: float
        unknown_0x5b454572: float
        unknown_0x49e96bd4: float
        unknown_0x708c3dce: float
        unknown_0xcf9768f8: float
        unknown_0x3252cf6d: float
        unknown_0x2db4f4e5: float
        forward_max_speed_normal: float
        forward_max_speed_air: float
        forward_max_speed_ice: float
        forward_max_speed_organic: float
        forward_max_speed_water: float
        forward_max_speed_lava: float
        forward_max_speed_phazon: float
        forward_max_speed_shrubbery: float
        gravitational_accel: float
        fluid_gravitational_accel: float
        vertical_jump_accel: float
        horizontal_jump_accel: float
        vertical_double_jump_accel: float
        horizontal_double_jump_accel: float
        water_jump_factor: float
        water_ball_jump_factor: float
        lava_jump_factor: float
        lava_ball_jump_factor: float
        phazon_jump_factor: float
        phazon_ball_jump_factor: float
        allowed_jump_time: float
        allowed_double_jump_time: float
        min_double_jump_window: float
        max_double_jump_window: float
        unknown_0x9bb73a0b: float
        min_jump_time: float
        min_double_jump_time: float
        ledge_fall_time: float
        double_jump_impulse: float
        backwards_force_multiplier: float
        bomb_jump_height: float
        bomb_jump_radius: float
        gravity_boost_time: float
        gravity_boost_force: float
        gravity_boost_cancel_dampening: float
        gravity_boost_multiple_allowed: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x18D0B2DA,
    0x84F61AC5,
    0xEDB06C1D,
    0x56F9F2AF,
    0xD05B643F,
    0x122CE118,
    0xF848DABE,
    0x68AC6028,
    0xCD4EE9FC,
    0x3C461DB2,
    0x55006B6A,
    0x8421E909,
    0x2E41A61D,
    0xDCF5B580,
    0x2DD68198,
    0x1A946073,
    0x800577D0,
    0xFEF7F81D,
    0x97B18EC5,
    0xB6B4CE74,
    0xD7BED27D,
    0x9A5EBA1C,
    0x609D1FB4,
    0x250FE036,
    0x600E90FF,
    0x81F724A0,
    0xE8B15278,
    0x1D85F8CA,
    0x9B0E377,
    0x2FF175F1,
    0x8096F89B,
    0x90F35DA8,
    0xD4A25028,
    0x2B5CB136,
    0x421AC7EE,
    0x586137D,
    0xAECE038B,
    0x3637E815,
    0x343A384C,
    0xCAF4624,
    0x34B2C148,
    0xB917AE8A,
    0xD051D852,
    0x48D462B4,
    0x6BB67D81,
    0xF4725CAD,
    0xD42AA92C,
    0x319526DB,
    0x4B6EB6CA,
    0xC107F3DB,
    0xA8418503,
    0x4B1D5CCF,
    0xDDCC44CD,
    0xE8662D92,
    0xABF6DEAE,
    0x3C3F9884,
    0x79FB91B7,
    0x87ACFC47,
    0xEEEA8A9F,
    0x659BC469,
    0x9087DAE1,
    0x119959F2,
    0x9963F9D3,
    0x3AB6B61B,
    0xD2CAA709,
    0x320333AA,
    0x5B454572,
    0x49E96BD4,
    0x708C3DCE,
    0xCF9768F8,
    0x3252CF6D,
    0x2DB4F4E5,
    0xFFD4A030,
    0x59DFBCB9,
    0x3099CA61,
    0x16C1FDDB,
    0x6C648931,
    0x4B42F5A9,
    0x1F4CC854,
    0xB3408173,
    0x14B78AAF,
    0x2C7620D3,
    0xC2C91F7,
    0x938C77D4,
    0x13C95DFD,
    0x8E41FED2,
    0xB261FA30,
    0x6AE560E9,
    0x3149633,
    0xD7B3F3EA,
    0xAF1450A2,
    0x980D701A,
    0xA805FEAE,
    0x233E3199,
    0x97F30B95,
    0x4C4C5872,
    0x9BB73A0B,
    0x4C8D664C,
    0x1FC20169,
    0xE7A5D759,
    0x7044B295,
    0xD82380A6,
    0x2A2E4100,
    0x905545E6,
    0x229460BE,
    0xE238FD3,
    0xDC92A0AC,
    0xE1FEFD3C,
)


@dataclasses.dataclass()
class TweakPlayer_Motion(BaseProperty):
    forward_accel_normal: float = dataclasses.field(
        default=35000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x18D0B2DA, original_name="ForwardAccelNormal"),
        },
    )
    forward_accel_air: float = dataclasses.field(
        default=8000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x84F61AC5, original_name="ForwardAccelAir"),
        },
    )
    forward_accel_ice: float = dataclasses.field(
        default=35000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEDB06C1D, original_name="ForwardAccelIce"),
        },
    )
    forward_accel_organic: float = dataclasses.field(
        default=35000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x56F9F2AF, original_name="ForwardAccelOrganic"),
        },
    )
    forward_accel_water: float = dataclasses.field(
        default=20000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD05B643F, original_name="ForwardAccelWater"),
        },
    )
    forward_accel_lava: float = dataclasses.field(
        default=20000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x122CE118, original_name="ForwardAccelLava"),
        },
    )
    forward_accel_phazon: float = dataclasses.field(
        default=20000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF848DABE, original_name="ForwardAccelPhazon"),
        },
    )
    forward_accel_shrubbery: float = dataclasses.field(
        default=20000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x68AC6028, original_name="ForwardAccelShrubbery"),
        },
    )
    rotational_accel_normal: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD4EE9FC, original_name="RotationalAccelNormal"),
        },
    )
    rotational_accel_air: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3C461DB2, original_name="RotationalAccelAir"),
        },
    )
    rotational_accel_ice: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x55006B6A, original_name="RotationalAccelIce"),
        },
    )
    rotational_accel_organic: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8421E909, original_name="RotationalAccelOrganic"),
        },
    )
    rotational_accel_water: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2E41A61D, original_name="RotationalAccelWater"),
        },
    )
    rotational_accel_lava: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDCF5B580, original_name="RotationalAccelLava"),
        },
    )
    rotational_accel_phazon: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DD68198, original_name="RotationalAccelPhazon"),
        },
    )
    rotational_accel_shrubbery: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A946073, original_name="RotationalAccelShrubbery"),
        },
    )
    advanced_rotational_accel_normal: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x800577D0, original_name="AdvancedRotationalAccelNormal"),
        },
    )
    advanced_rotational_accel_air: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFEF7F81D, original_name="AdvancedRotationalAccelAir"),
        },
    )
    advanced_rotational_accel_ice: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x97B18EC5, original_name="AdvancedRotationalAccelIce"),
        },
    )
    advanced_rotational_accel_organic: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB6B4CE74, original_name="AdvancedRotationalAccelOrganic"),
        },
    )
    advanced_rotational_accel_water: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD7BED27D, original_name="AdvancedRotationalAccelWater"),
        },
    )
    advanced_rotational_accel_lava: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9A5EBA1C, original_name="AdvancedRotationalAccelLava"),
        },
    )
    advanced_rotational_accel_phazon: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x609D1FB4, original_name="AdvancedRotationalAccelPhazon"),
        },
    )
    advanced_rotational_accel_shrubbery: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0x250FE036, original_name="AdvancedRotationalAccelShrubbery"
            ),
        },
    )
    unknown_0x600e90ff: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x600E90FF, original_name="Unknown"),
        },
    )
    unknown_0x81f724a0: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x81F724A0, original_name="Unknown"),
        },
    )
    unknown_0xe8b15278: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8B15278, original_name="Unknown"),
        },
    )
    unknown_0x1d85f8ca: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1D85F8CA, original_name="Unknown"),
        },
    )
    unknown_0x09b0e377: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x09B0E377, original_name="Unknown"),
        },
    )
    unknown_0x2ff175f1: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2FF175F1, original_name="Unknown"),
        },
    )
    unknown_0x8096f89b: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8096F89B, original_name="Unknown"),
        },
    )
    unknown_0x90f35da8: float = dataclasses.field(
        default=14000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90F35DA8, original_name="Unknown"),
        },
    )
    movement_friction_normal: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4A25028, original_name="MovementFrictionNormal"),
        },
    )
    movement_friction_air: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B5CB136, original_name="MovementFrictionAir"),
        },
    )
    movement_friction_ice: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x421AC7EE, original_name="MovementFrictionIce"),
        },
    )
    movement_friction_organic: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0586137D, original_name="MovementFrictionOrganic"),
        },
    )
    movement_friction_water: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAECE038B, original_name="MovementFrictionWater"),
        },
    )
    movement_friction_lava: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3637E815, original_name="MovementFrictionLava"),
        },
    )
    movement_friction_phazon: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x343A384C, original_name="MovementFrictionPhazon"),
        },
    )
    movement_friction_shrubbery: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0CAF4624, original_name="MovementFrictionShrubbery"),
        },
    )
    rotation_friction_normal: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0x34B2C148, original_name="RotationFrictionNormal"),
        },
    )
    rotation_friction_air: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB917AE8A, original_name="RotationFrictionAir"),
        },
    )
    rotation_friction_ice: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD051D852, original_name="RotationFrictionIce"),
        },
    )
    rotation_friction_organic: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0x48D462B4, original_name="RotationFrictionOrganic"),
        },
    )
    rotation_friction_water: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6BB67D81, original_name="RotationFrictionWater"),
        },
    )
    rotation_friction_lava: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4725CAD, original_name="RotationFrictionLava"),
        },
    )
    rotation_friction_phazon: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD42AA92C, original_name="RotationFrictionPhazon"),
        },
    )
    rotation_friction_shrubbery: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0x319526DB, original_name="RotationFrictionShrubbery"),
        },
    )
    rotation_max_speed_normal: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B6EB6CA, original_name="RotationMaxSpeedNormal"),
        },
    )
    rotation_max_speed_air: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC107F3DB, original_name="RotationMaxSpeedAir"),
        },
    )
    rotation_max_speed_ice: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA8418503, original_name="RotationMaxSpeedIce"),
        },
    )
    rotation_max_speed_organic: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B1D5CCF, original_name="RotationMaxSpeedOrganic"),
        },
    )
    rotation_max_speed_water: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDDCC44CD, original_name="RotationMaxSpeedWater"),
        },
    )
    rotation_max_speed_lava: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8662D92, original_name="RotationMaxSpeedLava"),
        },
    )
    rotation_max_speed_phazon: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xABF6DEAE, original_name="RotationMaxSpeedPhazon"),
        },
    )
    rotation_max_speed_shrubbery: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3C3F9884, original_name="RotationMaxSpeedShrubbery"),
        },
    )
    advanced_rotation_max_speed_normal: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x79FB91B7, original_name="AdvancedRotationMaxSpeedNormal"),
        },
    )
    advanced_rotation_max_speed_air: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x87ACFC47, original_name="AdvancedRotationMaxSpeedAir"),
        },
    )
    advanced_rotation_max_speed_ice: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEEEA8A9F, original_name="AdvancedRotationMaxSpeedIce"),
        },
    )
    advanced_rotation_max_speed_organic: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x659BC469, original_name="AdvancedRotationMaxSpeedOrganic"),
        },
    )
    advanced_rotation_max_speed_water: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9087DAE1, original_name="AdvancedRotationMaxSpeedWater"),
        },
    )
    advanced_rotation_max_speed_lava: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x119959F2, original_name="AdvancedRotationMaxSpeedLava"),
        },
    )
    advanced_rotation_max_speed_phazon: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9963F9D3, original_name="AdvancedRotationMaxSpeedPhazon"),
        },
    )
    advanced_rotation_max_speed_shrubbery: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0x3AB6B61B, original_name="AdvancedRotationMaxSpeedShrubbery"
            ),
        },
    )
    unknown_0xd2caa709: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD2CAA709, original_name="Unknown"),
        },
    )
    unknown_0x320333aa: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x320333AA, original_name="Unknown"),
        },
    )
    unknown_0x5b454572: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5B454572, original_name="Unknown"),
        },
    )
    unknown_0x49e96bd4: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x49E96BD4, original_name="Unknown"),
        },
    )
    unknown_0x708c3dce: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x708C3DCE, original_name="Unknown"),
        },
    )
    unknown_0xcf9768f8: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF9768F8, original_name="Unknown"),
        },
    )
    unknown_0x3252cf6d: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3252CF6D, original_name="Unknown"),
        },
    )
    unknown_0x2db4f4e5: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DB4F4E5, original_name="Unknown"),
        },
    )
    forward_max_speed_normal: float = dataclasses.field(
        default=16.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFFD4A030, original_name="ForwardMaxSpeedNormal"),
        },
    )
    forward_max_speed_air: float = dataclasses.field(
        default=16.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x59DFBCB9, original_name="ForwardMaxSpeedAir"),
        },
    )
    forward_max_speed_ice: float = dataclasses.field(
        default=16.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3099CA61, original_name="ForwardMaxSpeedIce"),
        },
    )
    forward_max_speed_organic: float = dataclasses.field(
        default=16.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16C1FDDB, original_name="ForwardMaxSpeedOrganic"),
        },
    )
    forward_max_speed_water: float = dataclasses.field(
        default=12.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C648931, original_name="ForwardMaxSpeedWater"),
        },
    )
    forward_max_speed_lava: float = dataclasses.field(
        default=12.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B42F5A9, original_name="ForwardMaxSpeedLava"),
        },
    )
    forward_max_speed_phazon: float = dataclasses.field(
        default=12.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1F4CC854, original_name="ForwardMaxSpeedPhazon"),
        },
    )
    forward_max_speed_shrubbery: float = dataclasses.field(
        default=12.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB3408173, original_name="ForwardMaxSpeedShrubbery"),
        },
    )
    gravitational_accel: float = dataclasses.field(
        default=-35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14B78AAF, original_name="GravitationalAccel"),
        },
    )
    fluid_gravitational_accel: float = dataclasses.field(
        default=-10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C7620D3, original_name="FluidGravitationalAccel"),
        },
    )
    vertical_jump_accel: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0C2C91F7, original_name="VerticalJumpAccel"),
        },
    )
    horizontal_jump_accel: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x938C77D4, original_name="HorizontalJumpAccel"),
        },
    )
    vertical_double_jump_accel: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x13C95DFD, original_name="VerticalDoubleJumpAccel"),
        },
    )
    horizontal_double_jump_accel: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E41FED2, original_name="HorizontalDoubleJumpAccel"),
        },
    )
    water_jump_factor: float = dataclasses.field(
        default=0.3700000047683716,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB261FA30, original_name="WaterJumpFactor"),
        },
    )
    water_ball_jump_factor: float = dataclasses.field(
        default=0.3700000047683716,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6AE560E9, original_name="WaterBallJumpFactor"),
        },
    )
    lava_jump_factor: float = dataclasses.field(
        default=0.3700000047683716,
        metadata={
            "reflection": FieldReflection[float](float, id=0x03149633, original_name="LavaJumpFactor"),
        },
    )
    lava_ball_jump_factor: float = dataclasses.field(
        default=0.3700000047683716,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD7B3F3EA, original_name="LavaBallJumpFactor"),
        },
    )
    phazon_jump_factor: float = dataclasses.field(
        default=0.3700000047683716,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAF1450A2, original_name="PhazonJumpFactor"),
        },
    )
    phazon_ball_jump_factor: float = dataclasses.field(
        default=0.3700000047683716,
        metadata={
            "reflection": FieldReflection[float](float, id=0x980D701A, original_name="PhazonBallJumpFactor"),
        },
    )
    allowed_jump_time: float = dataclasses.field(
        default=0.24950000643730164,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA805FEAE, original_name="AllowedJumpTime"),
        },
    )
    allowed_double_jump_time: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x233E3199, original_name="AllowedDoubleJumpTime"),
        },
    )
    min_double_jump_window: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x97F30B95, original_name="MinDoubleJumpWindow"),
        },
    )
    max_double_jump_window: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4C4C5872, original_name="MaxDoubleJumpWindow"),
        },
    )
    unknown_0x9bb73a0b: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9BB73A0B, original_name="Unknown"),
        },
    )
    min_jump_time: float = dataclasses.field(
        default=0.23499999940395355,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4C8D664C, original_name="MinJumpTime"),
        },
    )
    min_double_jump_time: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1FC20169, original_name="MinDoubleJumpTime"),
        },
    )
    ledge_fall_time: float = dataclasses.field(
        default=0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7A5D759, original_name="LedgeFallTime"),
        },
    )
    double_jump_impulse: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7044B295, original_name="DoubleJumpImpulse"),
        },
    )
    backwards_force_multiplier: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD82380A6, original_name="BackwardsForceMultiplier"),
        },
    )
    bomb_jump_height: float = dataclasses.field(
        default=7.900000095367432,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2A2E4100, original_name="BombJumpHeight"),
        },
    )
    bomb_jump_radius: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x905545E6, original_name="BombJumpRadius"),
        },
    )
    gravity_boost_time: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x229460BE, original_name="GravityBoostTime"),
        },
    )
    gravity_boost_force: float = dataclasses.field(
        default=9000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0E238FD3, original_name="GravityBoostForce"),
        },
    )
    gravity_boost_cancel_dampening: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDC92A0AC, original_name="GravityBoostCancelDampening"),
        },
    )
    gravity_boost_multiple_allowed: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE1FEFD3C, original_name="GravityBoostMultipleAllowed"),
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
        if property_count != 108:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?"
            )

        dec = _FAST_FORMAT.unpack(data.read(1077))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
            dec[48],
            dec[51],
            dec[54],
            dec[57],
            dec[60],
            dec[63],
            dec[66],
            dec[69],
            dec[72],
            dec[75],
            dec[78],
            dec[81],
            dec[84],
            dec[87],
            dec[90],
            dec[93],
            dec[96],
            dec[99],
            dec[102],
            dec[105],
            dec[108],
            dec[111],
            dec[114],
            dec[117],
            dec[120],
            dec[123],
            dec[126],
            dec[129],
            dec[132],
            dec[135],
            dec[138],
            dec[141],
            dec[144],
            dec[147],
            dec[150],
            dec[153],
            dec[156],
            dec[159],
            dec[162],
            dec[165],
            dec[168],
            dec[171],
            dec[174],
            dec[177],
            dec[180],
            dec[183],
            dec[186],
            dec[189],
            dec[192],
            dec[195],
            dec[198],
            dec[201],
            dec[204],
            dec[207],
            dec[210],
            dec[213],
            dec[216],
            dec[219],
            dec[222],
            dec[225],
            dec[228],
            dec[231],
            dec[234],
            dec[237],
            dec[240],
            dec[243],
            dec[246],
            dec[249],
            dec[252],
            dec[255],
            dec[258],
            dec[261],
            dec[264],
            dec[267],
            dec[270],
            dec[273],
            dec[276],
            dec[279],
            dec[282],
            dec[285],
            dec[288],
            dec[291],
            dec[294],
            dec[297],
            dec[300],
            dec[303],
            dec[306],
            dec[309],
            dec[312],
            dec[315],
            dec[318],
            dec[321],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            dec[59],
            dec[62],
            dec[65],
            dec[68],
            dec[71],
            dec[74],
            dec[77],
            dec[80],
            dec[83],
            dec[86],
            dec[89],
            dec[92],
            dec[95],
            dec[98],
            dec[101],
            dec[104],
            dec[107],
            dec[110],
            dec[113],
            dec[116],
            dec[119],
            dec[122],
            dec[125],
            dec[128],
            dec[131],
            dec[134],
            dec[137],
            dec[140],
            dec[143],
            dec[146],
            dec[149],
            dec[152],
            dec[155],
            dec[158],
            dec[161],
            dec[164],
            dec[167],
            dec[170],
            dec[173],
            dec[176],
            dec[179],
            dec[182],
            dec[185],
            dec[188],
            dec[191],
            dec[194],
            dec[197],
            dec[200],
            dec[203],
            dec[206],
            dec[209],
            dec[212],
            dec[215],
            dec[218],
            dec[221],
            dec[224],
            dec[227],
            dec[230],
            dec[233],
            dec[236],
            dec[239],
            dec[242],
            dec[245],
            dec[248],
            dec[251],
            dec[254],
            dec[257],
            dec[260],
            dec[263],
            dec[266],
            dec[269],
            dec[272],
            dec[275],
            dec[278],
            dec[281],
            dec[284],
            dec[287],
            dec[290],
            dec[293],
            dec[296],
            dec[299],
            dec[302],
            dec[305],
            dec[308],
            dec[311],
            dec[314],
            dec[317],
            dec[320],
            dec[323],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00l")  # 108 properties

        data.write(b"\x18\xd0\xb2\xda")  # 0x18d0b2da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_normal))

        data.write(b"\x84\xf6\x1a\xc5")  # 0x84f61ac5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_air))

        data.write(b"\xed\xb0l\x1d")  # 0xedb06c1d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_ice))

        data.write(b"V\xf9\xf2\xaf")  # 0x56f9f2af
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_organic))

        data.write(b"\xd0[d?")  # 0xd05b643f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_water))

        data.write(b"\x12,\xe1\x18")  # 0x122ce118
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_lava))

        data.write(b"\xf8H\xda\xbe")  # 0xf848dabe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_phazon))

        data.write(b"h\xac`(")  # 0x68ac6028
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_shrubbery))

        data.write(b"\xcdN\xe9\xfc")  # 0xcd4ee9fc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_normal))

        data.write(b"<F\x1d\xb2")  # 0x3c461db2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_air))

        data.write(b"U\x00kj")  # 0x55006b6a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_ice))

        data.write(b"\x84!\xe9\t")  # 0x8421e909
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_organic))

        data.write(b".A\xa6\x1d")  # 0x2e41a61d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_water))

        data.write(b"\xdc\xf5\xb5\x80")  # 0xdcf5b580
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_lava))

        data.write(b"-\xd6\x81\x98")  # 0x2dd68198
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_phazon))

        data.write(b"\x1a\x94`s")  # 0x1a946073
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_shrubbery))

        data.write(b"\x80\x05w\xd0")  # 0x800577d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_normal))

        data.write(b"\xfe\xf7\xf8\x1d")  # 0xfef7f81d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_air))

        data.write(b"\x97\xb1\x8e\xc5")  # 0x97b18ec5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_ice))

        data.write(b"\xb6\xb4\xcet")  # 0xb6b4ce74
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_organic))

        data.write(b"\xd7\xbe\xd2}")  # 0xd7bed27d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_water))

        data.write(b"\x9a^\xba\x1c")  # 0x9a5eba1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_lava))

        data.write(b"`\x9d\x1f\xb4")  # 0x609d1fb4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_phazon))

        data.write(b"%\x0f\xe06")  # 0x250fe036
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotational_accel_shrubbery))

        data.write(b"`\x0e\x90\xff")  # 0x600e90ff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x600e90ff))

        data.write(b"\x81\xf7$\xa0")  # 0x81f724a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x81f724a0))

        data.write(b"\xe8\xb1Rx")  # 0xe8b15278
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe8b15278))

        data.write(b"\x1d\x85\xf8\xca")  # 0x1d85f8ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1d85f8ca))

        data.write(b"\t\xb0\xe3w")  # 0x9b0e377
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x09b0e377))

        data.write(b"/\xf1u\xf1")  # 0x2ff175f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2ff175f1))

        data.write(b"\x80\x96\xf8\x9b")  # 0x8096f89b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8096f89b))

        data.write(b"\x90\xf3]\xa8")  # 0x90f35da8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x90f35da8))

        data.write(b"\xd4\xa2P(")  # 0xd4a25028
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_normal))

        data.write(b"+\\\xb16")  # 0x2b5cb136
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_air))

        data.write(b"B\x1a\xc7\xee")  # 0x421ac7ee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_ice))

        data.write(b"\x05\x86\x13}")  # 0x586137d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_organic))

        data.write(b"\xae\xce\x03\x8b")  # 0xaece038b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_water))

        data.write(b"67\xe8\x15")  # 0x3637e815
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_lava))

        data.write(b"4:8L")  # 0x343a384c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_phazon))

        data.write(b"\x0c\xafF$")  # 0xcaf4624
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_shrubbery))

        data.write(b"4\xb2\xc1H")  # 0x34b2c148
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_normal))

        data.write(b"\xb9\x17\xae\x8a")  # 0xb917ae8a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_air))

        data.write(b"\xd0Q\xd8R")  # 0xd051d852
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_ice))

        data.write(b"H\xd4b\xb4")  # 0x48d462b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_organic))

        data.write(b"k\xb6}\x81")  # 0x6bb67d81
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_water))

        data.write(b"\xf4r\\\xad")  # 0xf4725cad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_lava))

        data.write(b"\xd4*\xa9,")  # 0xd42aa92c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_phazon))

        data.write(b"1\x95&\xdb")  # 0x319526db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_shrubbery))

        data.write(b"Kn\xb6\xca")  # 0x4b6eb6ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_normal))

        data.write(b"\xc1\x07\xf3\xdb")  # 0xc107f3db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_air))

        data.write(b"\xa8A\x85\x03")  # 0xa8418503
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_ice))

        data.write(b"K\x1d\\\xcf")  # 0x4b1d5ccf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_organic))

        data.write(b"\xdd\xccD\xcd")  # 0xddcc44cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_water))

        data.write(b"\xe8f-\x92")  # 0xe8662d92
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_lava))

        data.write(b"\xab\xf6\xde\xae")  # 0xabf6deae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_phazon))

        data.write(b"<?\x98\x84")  # 0x3c3f9884
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_shrubbery))

        data.write(b"y\xfb\x91\xb7")  # 0x79fb91b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_normal))

        data.write(b"\x87\xac\xfcG")  # 0x87acfc47
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_air))

        data.write(b"\xee\xea\x8a\x9f")  # 0xeeea8a9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_ice))

        data.write(b"e\x9b\xc4i")  # 0x659bc469
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_organic))

        data.write(b"\x90\x87\xda\xe1")  # 0x9087dae1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_water))

        data.write(b"\x11\x99Y\xf2")  # 0x119959f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_lava))

        data.write(b"\x99c\xf9\xd3")  # 0x9963f9d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_phazon))

        data.write(b":\xb6\xb6\x1b")  # 0x3ab6b61b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.advanced_rotation_max_speed_shrubbery))

        data.write(b"\xd2\xca\xa7\t")  # 0xd2caa709
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd2caa709))

        data.write(b"2\x033\xaa")  # 0x320333aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x320333aa))

        data.write(b"[EEr")  # 0x5b454572
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5b454572))

        data.write(b"I\xe9k\xd4")  # 0x49e96bd4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x49e96bd4))

        data.write(b"p\x8c=\xce")  # 0x708c3dce
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x708c3dce))

        data.write(b"\xcf\x97h\xf8")  # 0xcf9768f8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcf9768f8))

        data.write(b"2R\xcfm")  # 0x3252cf6d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3252cf6d))

        data.write(b"-\xb4\xf4\xe5")  # 0x2db4f4e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2db4f4e5))

        data.write(b"\xff\xd4\xa00")  # 0xffd4a030
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_normal))

        data.write(b"Y\xdf\xbc\xb9")  # 0x59dfbcb9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_air))

        data.write(b"0\x99\xcaa")  # 0x3099ca61
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_ice))

        data.write(b"\x16\xc1\xfd\xdb")  # 0x16c1fddb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_organic))

        data.write(b"ld\x891")  # 0x6c648931
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_water))

        data.write(b"KB\xf5\xa9")  # 0x4b42f5a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_lava))

        data.write(b"\x1fL\xc8T")  # 0x1f4cc854
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_phazon))

        data.write(b"\xb3@\x81s")  # 0xb3408173
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_shrubbery))

        data.write(b"\x14\xb7\x8a\xaf")  # 0x14b78aaf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravitational_accel))

        data.write(b",v \xd3")  # 0x2c7620d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fluid_gravitational_accel))

        data.write(b"\x0c,\x91\xf7")  # 0xc2c91f7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.vertical_jump_accel))

        data.write(b"\x93\x8cw\xd4")  # 0x938c77d4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.horizontal_jump_accel))

        data.write(b"\x13\xc9]\xfd")  # 0x13c95dfd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.vertical_double_jump_accel))

        data.write(b"\x8eA\xfe\xd2")  # 0x8e41fed2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.horizontal_double_jump_accel))

        data.write(b"\xb2a\xfa0")  # 0xb261fa30
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.water_jump_factor))

        data.write(b"j\xe5`\xe9")  # 0x6ae560e9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.water_ball_jump_factor))

        data.write(b"\x03\x14\x963")  # 0x3149633
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lava_jump_factor))

        data.write(b"\xd7\xb3\xf3\xea")  # 0xd7b3f3ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lava_ball_jump_factor))

        data.write(b"\xaf\x14P\xa2")  # 0xaf1450a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phazon_jump_factor))

        data.write(b"\x98\rp\x1a")  # 0x980d701a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phazon_ball_jump_factor))

        data.write(b"\xa8\x05\xfe\xae")  # 0xa805feae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.allowed_jump_time))

        data.write(b"#>1\x99")  # 0x233e3199
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.allowed_double_jump_time))

        data.write(b"\x97\xf3\x0b\x95")  # 0x97f30b95
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_double_jump_window))

        data.write(b"LLXr")  # 0x4c4c5872
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_double_jump_window))

        data.write(b"\x9b\xb7:\x0b")  # 0x9bb73a0b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9bb73a0b))

        data.write(b"L\x8dfL")  # 0x4c8d664c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_jump_time))

        data.write(b"\x1f\xc2\x01i")  # 0x1fc20169
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_double_jump_time))

        data.write(b"\xe7\xa5\xd7Y")  # 0xe7a5d759
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ledge_fall_time))

        data.write(b"pD\xb2\x95")  # 0x7044b295
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.double_jump_impulse))

        data.write(b"\xd8#\x80\xa6")  # 0xd82380a6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.backwards_force_multiplier))

        data.write(b"*.A\x00")  # 0x2a2e4100
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bomb_jump_height))

        data.write(b"\x90UE\xe6")  # 0x905545e6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bomb_jump_radius))

        data.write(b'"\x94`\xbe')  # 0x229460be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity_boost_time))

        data.write(b"\x0e#\x8f\xd3")  # 0xe238fd3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity_boost_force))

        data.write(b"\xdc\x92\xa0\xac")  # 0xdc92a0ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity_boost_cancel_dampening))

        data.write(b"\xe1\xfe\xfd<")  # 0xe1fefd3c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.gravity_boost_multiple_allowed))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_MotionJson", data)
        return cls(
            forward_accel_normal=json_data["forward_accel_normal"],
            forward_accel_air=json_data["forward_accel_air"],
            forward_accel_ice=json_data["forward_accel_ice"],
            forward_accel_organic=json_data["forward_accel_organic"],
            forward_accel_water=json_data["forward_accel_water"],
            forward_accel_lava=json_data["forward_accel_lava"],
            forward_accel_phazon=json_data["forward_accel_phazon"],
            forward_accel_shrubbery=json_data["forward_accel_shrubbery"],
            rotational_accel_normal=json_data["rotational_accel_normal"],
            rotational_accel_air=json_data["rotational_accel_air"],
            rotational_accel_ice=json_data["rotational_accel_ice"],
            rotational_accel_organic=json_data["rotational_accel_organic"],
            rotational_accel_water=json_data["rotational_accel_water"],
            rotational_accel_lava=json_data["rotational_accel_lava"],
            rotational_accel_phazon=json_data["rotational_accel_phazon"],
            rotational_accel_shrubbery=json_data["rotational_accel_shrubbery"],
            advanced_rotational_accel_normal=json_data["advanced_rotational_accel_normal"],
            advanced_rotational_accel_air=json_data["advanced_rotational_accel_air"],
            advanced_rotational_accel_ice=json_data["advanced_rotational_accel_ice"],
            advanced_rotational_accel_organic=json_data["advanced_rotational_accel_organic"],
            advanced_rotational_accel_water=json_data["advanced_rotational_accel_water"],
            advanced_rotational_accel_lava=json_data["advanced_rotational_accel_lava"],
            advanced_rotational_accel_phazon=json_data["advanced_rotational_accel_phazon"],
            advanced_rotational_accel_shrubbery=json_data["advanced_rotational_accel_shrubbery"],
            unknown_0x600e90ff=json_data["unknown_0x600e90ff"],
            unknown_0x81f724a0=json_data["unknown_0x81f724a0"],
            unknown_0xe8b15278=json_data["unknown_0xe8b15278"],
            unknown_0x1d85f8ca=json_data["unknown_0x1d85f8ca"],
            unknown_0x09b0e377=json_data["unknown_0x09b0e377"],
            unknown_0x2ff175f1=json_data["unknown_0x2ff175f1"],
            unknown_0x8096f89b=json_data["unknown_0x8096f89b"],
            unknown_0x90f35da8=json_data["unknown_0x90f35da8"],
            movement_friction_normal=json_data["movement_friction_normal"],
            movement_friction_air=json_data["movement_friction_air"],
            movement_friction_ice=json_data["movement_friction_ice"],
            movement_friction_organic=json_data["movement_friction_organic"],
            movement_friction_water=json_data["movement_friction_water"],
            movement_friction_lava=json_data["movement_friction_lava"],
            movement_friction_phazon=json_data["movement_friction_phazon"],
            movement_friction_shrubbery=json_data["movement_friction_shrubbery"],
            rotation_friction_normal=json_data["rotation_friction_normal"],
            rotation_friction_air=json_data["rotation_friction_air"],
            rotation_friction_ice=json_data["rotation_friction_ice"],
            rotation_friction_organic=json_data["rotation_friction_organic"],
            rotation_friction_water=json_data["rotation_friction_water"],
            rotation_friction_lava=json_data["rotation_friction_lava"],
            rotation_friction_phazon=json_data["rotation_friction_phazon"],
            rotation_friction_shrubbery=json_data["rotation_friction_shrubbery"],
            rotation_max_speed_normal=json_data["rotation_max_speed_normal"],
            rotation_max_speed_air=json_data["rotation_max_speed_air"],
            rotation_max_speed_ice=json_data["rotation_max_speed_ice"],
            rotation_max_speed_organic=json_data["rotation_max_speed_organic"],
            rotation_max_speed_water=json_data["rotation_max_speed_water"],
            rotation_max_speed_lava=json_data["rotation_max_speed_lava"],
            rotation_max_speed_phazon=json_data["rotation_max_speed_phazon"],
            rotation_max_speed_shrubbery=json_data["rotation_max_speed_shrubbery"],
            advanced_rotation_max_speed_normal=json_data["advanced_rotation_max_speed_normal"],
            advanced_rotation_max_speed_air=json_data["advanced_rotation_max_speed_air"],
            advanced_rotation_max_speed_ice=json_data["advanced_rotation_max_speed_ice"],
            advanced_rotation_max_speed_organic=json_data["advanced_rotation_max_speed_organic"],
            advanced_rotation_max_speed_water=json_data["advanced_rotation_max_speed_water"],
            advanced_rotation_max_speed_lava=json_data["advanced_rotation_max_speed_lava"],
            advanced_rotation_max_speed_phazon=json_data["advanced_rotation_max_speed_phazon"],
            advanced_rotation_max_speed_shrubbery=json_data["advanced_rotation_max_speed_shrubbery"],
            unknown_0xd2caa709=json_data["unknown_0xd2caa709"],
            unknown_0x320333aa=json_data["unknown_0x320333aa"],
            unknown_0x5b454572=json_data["unknown_0x5b454572"],
            unknown_0x49e96bd4=json_data["unknown_0x49e96bd4"],
            unknown_0x708c3dce=json_data["unknown_0x708c3dce"],
            unknown_0xcf9768f8=json_data["unknown_0xcf9768f8"],
            unknown_0x3252cf6d=json_data["unknown_0x3252cf6d"],
            unknown_0x2db4f4e5=json_data["unknown_0x2db4f4e5"],
            forward_max_speed_normal=json_data["forward_max_speed_normal"],
            forward_max_speed_air=json_data["forward_max_speed_air"],
            forward_max_speed_ice=json_data["forward_max_speed_ice"],
            forward_max_speed_organic=json_data["forward_max_speed_organic"],
            forward_max_speed_water=json_data["forward_max_speed_water"],
            forward_max_speed_lava=json_data["forward_max_speed_lava"],
            forward_max_speed_phazon=json_data["forward_max_speed_phazon"],
            forward_max_speed_shrubbery=json_data["forward_max_speed_shrubbery"],
            gravitational_accel=json_data["gravitational_accel"],
            fluid_gravitational_accel=json_data["fluid_gravitational_accel"],
            vertical_jump_accel=json_data["vertical_jump_accel"],
            horizontal_jump_accel=json_data["horizontal_jump_accel"],
            vertical_double_jump_accel=json_data["vertical_double_jump_accel"],
            horizontal_double_jump_accel=json_data["horizontal_double_jump_accel"],
            water_jump_factor=json_data["water_jump_factor"],
            water_ball_jump_factor=json_data["water_ball_jump_factor"],
            lava_jump_factor=json_data["lava_jump_factor"],
            lava_ball_jump_factor=json_data["lava_ball_jump_factor"],
            phazon_jump_factor=json_data["phazon_jump_factor"],
            phazon_ball_jump_factor=json_data["phazon_ball_jump_factor"],
            allowed_jump_time=json_data["allowed_jump_time"],
            allowed_double_jump_time=json_data["allowed_double_jump_time"],
            min_double_jump_window=json_data["min_double_jump_window"],
            max_double_jump_window=json_data["max_double_jump_window"],
            unknown_0x9bb73a0b=json_data["unknown_0x9bb73a0b"],
            min_jump_time=json_data["min_jump_time"],
            min_double_jump_time=json_data["min_double_jump_time"],
            ledge_fall_time=json_data["ledge_fall_time"],
            double_jump_impulse=json_data["double_jump_impulse"],
            backwards_force_multiplier=json_data["backwards_force_multiplier"],
            bomb_jump_height=json_data["bomb_jump_height"],
            bomb_jump_radius=json_data["bomb_jump_radius"],
            gravity_boost_time=json_data["gravity_boost_time"],
            gravity_boost_force=json_data["gravity_boost_force"],
            gravity_boost_cancel_dampening=json_data["gravity_boost_cancel_dampening"],
            gravity_boost_multiple_allowed=json_data["gravity_boost_multiple_allowed"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "forward_accel_normal": self.forward_accel_normal,
            "forward_accel_air": self.forward_accel_air,
            "forward_accel_ice": self.forward_accel_ice,
            "forward_accel_organic": self.forward_accel_organic,
            "forward_accel_water": self.forward_accel_water,
            "forward_accel_lava": self.forward_accel_lava,
            "forward_accel_phazon": self.forward_accel_phazon,
            "forward_accel_shrubbery": self.forward_accel_shrubbery,
            "rotational_accel_normal": self.rotational_accel_normal,
            "rotational_accel_air": self.rotational_accel_air,
            "rotational_accel_ice": self.rotational_accel_ice,
            "rotational_accel_organic": self.rotational_accel_organic,
            "rotational_accel_water": self.rotational_accel_water,
            "rotational_accel_lava": self.rotational_accel_lava,
            "rotational_accel_phazon": self.rotational_accel_phazon,
            "rotational_accel_shrubbery": self.rotational_accel_shrubbery,
            "advanced_rotational_accel_normal": self.advanced_rotational_accel_normal,
            "advanced_rotational_accel_air": self.advanced_rotational_accel_air,
            "advanced_rotational_accel_ice": self.advanced_rotational_accel_ice,
            "advanced_rotational_accel_organic": self.advanced_rotational_accel_organic,
            "advanced_rotational_accel_water": self.advanced_rotational_accel_water,
            "advanced_rotational_accel_lava": self.advanced_rotational_accel_lava,
            "advanced_rotational_accel_phazon": self.advanced_rotational_accel_phazon,
            "advanced_rotational_accel_shrubbery": self.advanced_rotational_accel_shrubbery,
            "unknown_0x600e90ff": self.unknown_0x600e90ff,
            "unknown_0x81f724a0": self.unknown_0x81f724a0,
            "unknown_0xe8b15278": self.unknown_0xe8b15278,
            "unknown_0x1d85f8ca": self.unknown_0x1d85f8ca,
            "unknown_0x09b0e377": self.unknown_0x09b0e377,
            "unknown_0x2ff175f1": self.unknown_0x2ff175f1,
            "unknown_0x8096f89b": self.unknown_0x8096f89b,
            "unknown_0x90f35da8": self.unknown_0x90f35da8,
            "movement_friction_normal": self.movement_friction_normal,
            "movement_friction_air": self.movement_friction_air,
            "movement_friction_ice": self.movement_friction_ice,
            "movement_friction_organic": self.movement_friction_organic,
            "movement_friction_water": self.movement_friction_water,
            "movement_friction_lava": self.movement_friction_lava,
            "movement_friction_phazon": self.movement_friction_phazon,
            "movement_friction_shrubbery": self.movement_friction_shrubbery,
            "rotation_friction_normal": self.rotation_friction_normal,
            "rotation_friction_air": self.rotation_friction_air,
            "rotation_friction_ice": self.rotation_friction_ice,
            "rotation_friction_organic": self.rotation_friction_organic,
            "rotation_friction_water": self.rotation_friction_water,
            "rotation_friction_lava": self.rotation_friction_lava,
            "rotation_friction_phazon": self.rotation_friction_phazon,
            "rotation_friction_shrubbery": self.rotation_friction_shrubbery,
            "rotation_max_speed_normal": self.rotation_max_speed_normal,
            "rotation_max_speed_air": self.rotation_max_speed_air,
            "rotation_max_speed_ice": self.rotation_max_speed_ice,
            "rotation_max_speed_organic": self.rotation_max_speed_organic,
            "rotation_max_speed_water": self.rotation_max_speed_water,
            "rotation_max_speed_lava": self.rotation_max_speed_lava,
            "rotation_max_speed_phazon": self.rotation_max_speed_phazon,
            "rotation_max_speed_shrubbery": self.rotation_max_speed_shrubbery,
            "advanced_rotation_max_speed_normal": self.advanced_rotation_max_speed_normal,
            "advanced_rotation_max_speed_air": self.advanced_rotation_max_speed_air,
            "advanced_rotation_max_speed_ice": self.advanced_rotation_max_speed_ice,
            "advanced_rotation_max_speed_organic": self.advanced_rotation_max_speed_organic,
            "advanced_rotation_max_speed_water": self.advanced_rotation_max_speed_water,
            "advanced_rotation_max_speed_lava": self.advanced_rotation_max_speed_lava,
            "advanced_rotation_max_speed_phazon": self.advanced_rotation_max_speed_phazon,
            "advanced_rotation_max_speed_shrubbery": self.advanced_rotation_max_speed_shrubbery,
            "unknown_0xd2caa709": self.unknown_0xd2caa709,
            "unknown_0x320333aa": self.unknown_0x320333aa,
            "unknown_0x5b454572": self.unknown_0x5b454572,
            "unknown_0x49e96bd4": self.unknown_0x49e96bd4,
            "unknown_0x708c3dce": self.unknown_0x708c3dce,
            "unknown_0xcf9768f8": self.unknown_0xcf9768f8,
            "unknown_0x3252cf6d": self.unknown_0x3252cf6d,
            "unknown_0x2db4f4e5": self.unknown_0x2db4f4e5,
            "forward_max_speed_normal": self.forward_max_speed_normal,
            "forward_max_speed_air": self.forward_max_speed_air,
            "forward_max_speed_ice": self.forward_max_speed_ice,
            "forward_max_speed_organic": self.forward_max_speed_organic,
            "forward_max_speed_water": self.forward_max_speed_water,
            "forward_max_speed_lava": self.forward_max_speed_lava,
            "forward_max_speed_phazon": self.forward_max_speed_phazon,
            "forward_max_speed_shrubbery": self.forward_max_speed_shrubbery,
            "gravitational_accel": self.gravitational_accel,
            "fluid_gravitational_accel": self.fluid_gravitational_accel,
            "vertical_jump_accel": self.vertical_jump_accel,
            "horizontal_jump_accel": self.horizontal_jump_accel,
            "vertical_double_jump_accel": self.vertical_double_jump_accel,
            "horizontal_double_jump_accel": self.horizontal_double_jump_accel,
            "water_jump_factor": self.water_jump_factor,
            "water_ball_jump_factor": self.water_ball_jump_factor,
            "lava_jump_factor": self.lava_jump_factor,
            "lava_ball_jump_factor": self.lava_ball_jump_factor,
            "phazon_jump_factor": self.phazon_jump_factor,
            "phazon_ball_jump_factor": self.phazon_ball_jump_factor,
            "allowed_jump_time": self.allowed_jump_time,
            "allowed_double_jump_time": self.allowed_double_jump_time,
            "min_double_jump_window": self.min_double_jump_window,
            "max_double_jump_window": self.max_double_jump_window,
            "unknown_0x9bb73a0b": self.unknown_0x9bb73a0b,
            "min_jump_time": self.min_jump_time,
            "min_double_jump_time": self.min_double_jump_time,
            "ledge_fall_time": self.ledge_fall_time,
            "double_jump_impulse": self.double_jump_impulse,
            "backwards_force_multiplier": self.backwards_force_multiplier,
            "bomb_jump_height": self.bomb_jump_height,
            "bomb_jump_radius": self.bomb_jump_radius,
            "gravity_boost_time": self.gravity_boost_time,
            "gravity_boost_force": self.gravity_boost_force,
            "gravity_boost_cancel_dampening": self.gravity_boost_cancel_dampening,
            "gravity_boost_multiple_allowed": self.gravity_boost_multiple_allowed,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x18D0B2DA: ("forward_accel_normal", structs.decode_BIG_f),
    0x84F61AC5: ("forward_accel_air", structs.decode_BIG_f),
    0xEDB06C1D: ("forward_accel_ice", structs.decode_BIG_f),
    0x56F9F2AF: ("forward_accel_organic", structs.decode_BIG_f),
    0xD05B643F: ("forward_accel_water", structs.decode_BIG_f),
    0x122CE118: ("forward_accel_lava", structs.decode_BIG_f),
    0xF848DABE: ("forward_accel_phazon", structs.decode_BIG_f),
    0x68AC6028: ("forward_accel_shrubbery", structs.decode_BIG_f),
    0xCD4EE9FC: ("rotational_accel_normal", structs.decode_BIG_f),
    0x3C461DB2: ("rotational_accel_air", structs.decode_BIG_f),
    0x55006B6A: ("rotational_accel_ice", structs.decode_BIG_f),
    0x8421E909: ("rotational_accel_organic", structs.decode_BIG_f),
    0x2E41A61D: ("rotational_accel_water", structs.decode_BIG_f),
    0xDCF5B580: ("rotational_accel_lava", structs.decode_BIG_f),
    0x2DD68198: ("rotational_accel_phazon", structs.decode_BIG_f),
    0x1A946073: ("rotational_accel_shrubbery", structs.decode_BIG_f),
    0x800577D0: ("advanced_rotational_accel_normal", structs.decode_BIG_f),
    0xFEF7F81D: ("advanced_rotational_accel_air", structs.decode_BIG_f),
    0x97B18EC5: ("advanced_rotational_accel_ice", structs.decode_BIG_f),
    0xB6B4CE74: ("advanced_rotational_accel_organic", structs.decode_BIG_f),
    0xD7BED27D: ("advanced_rotational_accel_water", structs.decode_BIG_f),
    0x9A5EBA1C: ("advanced_rotational_accel_lava", structs.decode_BIG_f),
    0x609D1FB4: ("advanced_rotational_accel_phazon", structs.decode_BIG_f),
    0x250FE036: ("advanced_rotational_accel_shrubbery", structs.decode_BIG_f),
    0x600E90FF: ("unknown_0x600e90ff", structs.decode_BIG_f),
    0x81F724A0: ("unknown_0x81f724a0", structs.decode_BIG_f),
    0xE8B15278: ("unknown_0xe8b15278", structs.decode_BIG_f),
    0x1D85F8CA: ("unknown_0x1d85f8ca", structs.decode_BIG_f),
    0x09B0E377: ("unknown_0x09b0e377", structs.decode_BIG_f),
    0x2FF175F1: ("unknown_0x2ff175f1", structs.decode_BIG_f),
    0x8096F89B: ("unknown_0x8096f89b", structs.decode_BIG_f),
    0x90F35DA8: ("unknown_0x90f35da8", structs.decode_BIG_f),
    0xD4A25028: ("movement_friction_normal", structs.decode_BIG_f),
    0x2B5CB136: ("movement_friction_air", structs.decode_BIG_f),
    0x421AC7EE: ("movement_friction_ice", structs.decode_BIG_f),
    0x0586137D: ("movement_friction_organic", structs.decode_BIG_f),
    0xAECE038B: ("movement_friction_water", structs.decode_BIG_f),
    0x3637E815: ("movement_friction_lava", structs.decode_BIG_f),
    0x343A384C: ("movement_friction_phazon", structs.decode_BIG_f),
    0x0CAF4624: ("movement_friction_shrubbery", structs.decode_BIG_f),
    0x34B2C148: ("rotation_friction_normal", structs.decode_BIG_f),
    0xB917AE8A: ("rotation_friction_air", structs.decode_BIG_f),
    0xD051D852: ("rotation_friction_ice", structs.decode_BIG_f),
    0x48D462B4: ("rotation_friction_organic", structs.decode_BIG_f),
    0x6BB67D81: ("rotation_friction_water", structs.decode_BIG_f),
    0xF4725CAD: ("rotation_friction_lava", structs.decode_BIG_f),
    0xD42AA92C: ("rotation_friction_phazon", structs.decode_BIG_f),
    0x319526DB: ("rotation_friction_shrubbery", structs.decode_BIG_f),
    0x4B6EB6CA: ("rotation_max_speed_normal", structs.decode_BIG_f),
    0xC107F3DB: ("rotation_max_speed_air", structs.decode_BIG_f),
    0xA8418503: ("rotation_max_speed_ice", structs.decode_BIG_f),
    0x4B1D5CCF: ("rotation_max_speed_organic", structs.decode_BIG_f),
    0xDDCC44CD: ("rotation_max_speed_water", structs.decode_BIG_f),
    0xE8662D92: ("rotation_max_speed_lava", structs.decode_BIG_f),
    0xABF6DEAE: ("rotation_max_speed_phazon", structs.decode_BIG_f),
    0x3C3F9884: ("rotation_max_speed_shrubbery", structs.decode_BIG_f),
    0x79FB91B7: ("advanced_rotation_max_speed_normal", structs.decode_BIG_f),
    0x87ACFC47: ("advanced_rotation_max_speed_air", structs.decode_BIG_f),
    0xEEEA8A9F: ("advanced_rotation_max_speed_ice", structs.decode_BIG_f),
    0x659BC469: ("advanced_rotation_max_speed_organic", structs.decode_BIG_f),
    0x9087DAE1: ("advanced_rotation_max_speed_water", structs.decode_BIG_f),
    0x119959F2: ("advanced_rotation_max_speed_lava", structs.decode_BIG_f),
    0x9963F9D3: ("advanced_rotation_max_speed_phazon", structs.decode_BIG_f),
    0x3AB6B61B: ("advanced_rotation_max_speed_shrubbery", structs.decode_BIG_f),
    0xD2CAA709: ("unknown_0xd2caa709", structs.decode_BIG_f),
    0x320333AA: ("unknown_0x320333aa", structs.decode_BIG_f),
    0x5B454572: ("unknown_0x5b454572", structs.decode_BIG_f),
    0x49E96BD4: ("unknown_0x49e96bd4", structs.decode_BIG_f),
    0x708C3DCE: ("unknown_0x708c3dce", structs.decode_BIG_f),
    0xCF9768F8: ("unknown_0xcf9768f8", structs.decode_BIG_f),
    0x3252CF6D: ("unknown_0x3252cf6d", structs.decode_BIG_f),
    0x2DB4F4E5: ("unknown_0x2db4f4e5", structs.decode_BIG_f),
    0xFFD4A030: ("forward_max_speed_normal", structs.decode_BIG_f),
    0x59DFBCB9: ("forward_max_speed_air", structs.decode_BIG_f),
    0x3099CA61: ("forward_max_speed_ice", structs.decode_BIG_f),
    0x16C1FDDB: ("forward_max_speed_organic", structs.decode_BIG_f),
    0x6C648931: ("forward_max_speed_water", structs.decode_BIG_f),
    0x4B42F5A9: ("forward_max_speed_lava", structs.decode_BIG_f),
    0x1F4CC854: ("forward_max_speed_phazon", structs.decode_BIG_f),
    0xB3408173: ("forward_max_speed_shrubbery", structs.decode_BIG_f),
    0x14B78AAF: ("gravitational_accel", structs.decode_BIG_f),
    0x2C7620D3: ("fluid_gravitational_accel", structs.decode_BIG_f),
    0x0C2C91F7: ("vertical_jump_accel", structs.decode_BIG_f),
    0x938C77D4: ("horizontal_jump_accel", structs.decode_BIG_f),
    0x13C95DFD: ("vertical_double_jump_accel", structs.decode_BIG_f),
    0x8E41FED2: ("horizontal_double_jump_accel", structs.decode_BIG_f),
    0xB261FA30: ("water_jump_factor", structs.decode_BIG_f),
    0x6AE560E9: ("water_ball_jump_factor", structs.decode_BIG_f),
    0x03149633: ("lava_jump_factor", structs.decode_BIG_f),
    0xD7B3F3EA: ("lava_ball_jump_factor", structs.decode_BIG_f),
    0xAF1450A2: ("phazon_jump_factor", structs.decode_BIG_f),
    0x980D701A: ("phazon_ball_jump_factor", structs.decode_BIG_f),
    0xA805FEAE: ("allowed_jump_time", structs.decode_BIG_f),
    0x233E3199: ("allowed_double_jump_time", structs.decode_BIG_f),
    0x97F30B95: ("min_double_jump_window", structs.decode_BIG_f),
    0x4C4C5872: ("max_double_jump_window", structs.decode_BIG_f),
    0x9BB73A0B: ("unknown_0x9bb73a0b", structs.decode_BIG_f),
    0x4C8D664C: ("min_jump_time", structs.decode_BIG_f),
    0x1FC20169: ("min_double_jump_time", structs.decode_BIG_f),
    0xE7A5D759: ("ledge_fall_time", structs.decode_BIG_f),
    0x7044B295: ("double_jump_impulse", structs.decode_BIG_f),
    0xD82380A6: ("backwards_force_multiplier", structs.decode_BIG_f),
    0x2A2E4100: ("bomb_jump_height", structs.decode_BIG_f),
    0x905545E6: ("bomb_jump_radius", structs.decode_BIG_f),
    0x229460BE: ("gravity_boost_time", structs.decode_BIG_f),
    0x0E238FD3: ("gravity_boost_force", structs.decode_BIG_f),
    0xDC92A0AC: ("gravity_boost_cancel_dampening", structs.decode_BIG_f),
    0xE1FEFD3C: ("gravity_boost_multiple_allowed", structs.decode_BIG_bool_),
}
