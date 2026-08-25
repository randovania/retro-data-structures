# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class GunTurretJson(typing_extensions.TypedDict):
        name: str
        type: int
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        collision_extend: json_util.JsonValue
        collision_offset: json_util.JsonValue
        animation_parameters: json_util.JsonObject
        unnamed_0x00000008: json_util.JsonObject
        unnamed_0x00000009: json_util.JsonObject
        unnamed_0x0000000a: json_util.JsonObject
        into_activate_delay: float
        reload_time: float
        reload_time_variance: float
        pan_start_time: float
        pan_hold_time: float
        total_pan_search_time: float
        left_max_angle: float
        right_max_angle: float
        down_max_angle: float
        turn_speed: float
        detection_range: float
        detection_z_range: float
        freeze_duration: float
        freeze_variance: float
        freeze_timeout: bool
        projectile_res: int
        unnamed_0x0000001b: json_util.JsonObject
        idle_light_res: int
        deactivate_light_res: int
        targetting_light_res: int
        frozen_effect_res: int
        charging_effect_res: int
        panning_effect_res: int
        visor_effect_res: int
        tracking_sound_id: int
        lock_on_sound_id: int
        unfreeze_sound_id: int
        stop_clank_sound_id: int
        charging_sound_id: int
        visor_sound_id: int
        extension_model_res_id: int
        extension_drop_down_dist: float
        num_initial_shots: int
        initial_shot_table_index: int
        num_subsequent_shots: int
        frenzy_duration: float
        scripted_start_only: bool


class Type(enum.IntEnum):
    Handle = 0
    Gun = 1

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class GunTurret(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    type: Type = dataclasses.field(
        default=Type.Handle,
        metadata={
            "reflection": FieldReflection[Type](
                Type, id=0x00000001, original_name="Type", from_json=Type.from_json, to_json=Type.to_json
            ),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000003, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_extend: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000005,
                original_name="CollisionExtend",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000006,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000007,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unnamed_0x00000008: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000008,
                original_name="8",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unnamed_0x00000009: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo, id=0x00000009, original_name="9", from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
            ),
        },
    )
    unnamed_0x0000000a: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000A,
                original_name="10",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    into_activate_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="IntoActivateDelay"),
        },
    )
    reload_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="ReloadTime"),
        },
    )
    reload_time_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="ReloadTimeVariance"),
        },
    )
    pan_start_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="PanStartTime"),
        },
    )
    pan_hold_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="PanHoldTime"),
        },
    )
    total_pan_search_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="TotalPanSearchTime"),
        },
    )
    left_max_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="LeftMaxAngle"),
        },
    )
    right_max_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="RightMaxAngle"),
        },
    )
    down_max_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="DownMaxAngle"),
        },
    )
    turn_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="TurnSpeed"),
        },
    )
    detection_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="DetectionRange"),
        },
    )
    detection_z_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="DetectionZRange"),
        },
    )
    freeze_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000017, original_name="FreezeDuration"),
        },
    )
    freeze_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000018, original_name="FreezeVariance"),
        },
    )
    freeze_timeout: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000019, original_name="FreezeTimeout"),
        },
    )
    projectile_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001A, original_name="ProjectileRes"),
        },
    )
    unnamed_0x0000001b: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000001B,
                original_name="27",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    idle_light_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001C, original_name="IdleLightRes"),
        },
    )
    deactivate_light_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001D, original_name="DeactivateLightRes"),
        },
    )
    targetting_light_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001E, original_name="TargettingLightRes"),
        },
    )
    frozen_effect_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001F, original_name="FrozenEffectRes"),
        },
    )
    charging_effect_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000020, original_name="ChargingEffectRes"),
        },
    )
    panning_effect_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000021, original_name="PanningEffectRes"),
        },
    )
    visor_effect_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000022, original_name="VisorEffectRes"),
        },
    )
    tracking_sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000023, original_name="TrackingSoundID"),
        },
    )
    lock_on_sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000024, original_name="LockOnSoundID"),
        },
    )
    unfreeze_sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000025, original_name="UnfreezeSoundID"),
        },
    )
    stop_clank_sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000026, original_name="StopClankSoundID"),
        },
    )
    charging_sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000027, original_name="ChargingSoundID"),
        },
    )
    visor_sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000028, original_name="VisorSoundID"),
        },
    )
    extension_model_res_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000029, original_name="ExtensionModelResID"),
        },
    )
    extension_drop_down_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000002A, original_name="ExtensionDropDownDist"),
        },
    )
    num_initial_shots: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000002B, original_name="NumInitialShots"),
        },
    )
    initial_shot_table_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000002C, original_name="InitialShotTableIndex"),
        },
    )
    num_subsequent_shots: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000002D, original_name="NumSubsequentShots"),
        },
    )
    frenzy_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000002E, original_name="FrenzyDuration"),
        },
    )
    scripted_start_only: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000002F, original_name="ScriptedStartOnly"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x64

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        type = Type.from_stream(data, game)
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        collision_extend = Vector.from_stream(data, game, property_size)
        collision_offset = Vector.from_stream(data, game, property_size)
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed_0x00000008 = ActorParameters.from_stream(data, game, property_size)
        unnamed_0x00000009 = HealthInfo.from_stream(data, game, property_size)
        unnamed_0x0000000a = DamageVulnerability.from_stream(data, game, property_size)
        into_activate_delay = structs.BIG_f.unpack(data.read(4))[0]
        reload_time = structs.BIG_f.unpack(data.read(4))[0]
        reload_time_variance = structs.BIG_f.unpack(data.read(4))[0]
        pan_start_time = structs.BIG_f.unpack(data.read(4))[0]
        pan_hold_time = structs.BIG_f.unpack(data.read(4))[0]
        total_pan_search_time = structs.BIG_f.unpack(data.read(4))[0]
        left_max_angle = structs.BIG_f.unpack(data.read(4))[0]
        right_max_angle = structs.BIG_f.unpack(data.read(4))[0]
        down_max_angle = structs.BIG_f.unpack(data.read(4))[0]
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]
        detection_range = structs.BIG_f.unpack(data.read(4))[0]
        detection_z_range = structs.BIG_f.unpack(data.read(4))[0]
        freeze_duration = structs.BIG_f.unpack(data.read(4))[0]
        freeze_variance = structs.BIG_f.unpack(data.read(4))[0]
        freeze_timeout = structs.BIG_bool_.unpack(data.read(1))[0]
        projectile_res = structs.BIG_L.unpack(data.read(4))[0]
        unnamed_0x0000001b = DamageInfo.from_stream(data, game, property_size)
        idle_light_res = structs.BIG_L.unpack(data.read(4))[0]
        deactivate_light_res = structs.BIG_L.unpack(data.read(4))[0]
        targetting_light_res = structs.BIG_L.unpack(data.read(4))[0]
        frozen_effect_res = structs.BIG_L.unpack(data.read(4))[0]
        charging_effect_res = structs.BIG_L.unpack(data.read(4))[0]
        panning_effect_res = structs.BIG_L.unpack(data.read(4))[0]
        visor_effect_res = structs.BIG_L.unpack(data.read(4))[0]
        tracking_sound_id = structs.BIG_l.unpack(data.read(4))[0]
        lock_on_sound_id = structs.BIG_l.unpack(data.read(4))[0]
        unfreeze_sound_id = structs.BIG_l.unpack(data.read(4))[0]
        stop_clank_sound_id = structs.BIG_l.unpack(data.read(4))[0]
        charging_sound_id = structs.BIG_l.unpack(data.read(4))[0]
        visor_sound_id = structs.BIG_l.unpack(data.read(4))[0]
        extension_model_res_id = structs.BIG_L.unpack(data.read(4))[0]
        extension_drop_down_dist = structs.BIG_f.unpack(data.read(4))[0]
        num_initial_shots = structs.BIG_l.unpack(data.read(4))[0]
        initial_shot_table_index = structs.BIG_l.unpack(data.read(4))[0]
        num_subsequent_shots = structs.BIG_l.unpack(data.read(4))[0]
        frenzy_duration = structs.BIG_f.unpack(data.read(4))[0]
        scripted_start_only = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            type,
            position,
            rotation,
            scale,
            collision_extend,
            collision_offset,
            animation_parameters,
            unnamed_0x00000008,
            unnamed_0x00000009,
            unnamed_0x0000000a,
            into_activate_delay,
            reload_time,
            reload_time_variance,
            pan_start_time,
            pan_hold_time,
            total_pan_search_time,
            left_max_angle,
            right_max_angle,
            down_max_angle,
            turn_speed,
            detection_range,
            detection_z_range,
            freeze_duration,
            freeze_variance,
            freeze_timeout,
            projectile_res,
            unnamed_0x0000001b,
            idle_light_res,
            deactivate_light_res,
            targetting_light_res,
            frozen_effect_res,
            charging_effect_res,
            panning_effect_res,
            visor_effect_res,
            tracking_sound_id,
            lock_on_sound_id,
            unfreeze_sound_id,
            stop_clank_sound_id,
            charging_sound_id,
            visor_sound_id,
            extension_model_res_id,
            extension_drop_down_dist,
            num_initial_shots,
            initial_shot_table_index,
            num_subsequent_shots,
            frenzy_duration,
            scripted_start_only,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x000")  # 48 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.type.to_stream(data, game)
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.collision_extend.to_stream(data, game)
        self.collision_offset.to_stream(data, game)
        self.animation_parameters.to_stream(data, game)
        self.unnamed_0x00000008.to_stream(data, game)
        self.unnamed_0x00000009.to_stream(data, game)
        self.unnamed_0x0000000a.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.into_activate_delay))
        data.write(structs.BIG_f.pack(self.reload_time))
        data.write(structs.BIG_f.pack(self.reload_time_variance))
        data.write(structs.BIG_f.pack(self.pan_start_time))
        data.write(structs.BIG_f.pack(self.pan_hold_time))
        data.write(structs.BIG_f.pack(self.total_pan_search_time))
        data.write(structs.BIG_f.pack(self.left_max_angle))
        data.write(structs.BIG_f.pack(self.right_max_angle))
        data.write(structs.BIG_f.pack(self.down_max_angle))
        data.write(structs.BIG_f.pack(self.turn_speed))
        data.write(structs.BIG_f.pack(self.detection_range))
        data.write(structs.BIG_f.pack(self.detection_z_range))
        data.write(structs.BIG_f.pack(self.freeze_duration))
        data.write(structs.BIG_f.pack(self.freeze_variance))
        data.write(structs.BIG_bool_.pack(self.freeze_timeout))
        data.write(structs.BIG_L.pack(self.projectile_res))
        self.unnamed_0x0000001b.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.idle_light_res))
        data.write(structs.BIG_L.pack(self.deactivate_light_res))
        data.write(structs.BIG_L.pack(self.targetting_light_res))
        data.write(structs.BIG_L.pack(self.frozen_effect_res))
        data.write(structs.BIG_L.pack(self.charging_effect_res))
        data.write(structs.BIG_L.pack(self.panning_effect_res))
        data.write(structs.BIG_L.pack(self.visor_effect_res))
        data.write(structs.BIG_l.pack(self.tracking_sound_id))
        data.write(structs.BIG_l.pack(self.lock_on_sound_id))
        data.write(structs.BIG_l.pack(self.unfreeze_sound_id))
        data.write(structs.BIG_l.pack(self.stop_clank_sound_id))
        data.write(structs.BIG_l.pack(self.charging_sound_id))
        data.write(structs.BIG_l.pack(self.visor_sound_id))
        data.write(structs.BIG_L.pack(self.extension_model_res_id))
        data.write(structs.BIG_f.pack(self.extension_drop_down_dist))
        data.write(structs.BIG_l.pack(self.num_initial_shots))
        data.write(structs.BIG_l.pack(self.initial_shot_table_index))
        data.write(structs.BIG_l.pack(self.num_subsequent_shots))
        data.write(structs.BIG_f.pack(self.frenzy_duration))
        data.write(structs.BIG_bool_.pack(self.scripted_start_only))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GunTurretJson", data)
        return cls(
            name=json_data["name"],
            type=Type.from_json(json_data["type"]),
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            collision_extend=Vector.from_json(json_data["collision_extend"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed_0x00000008=ActorParameters.from_json(json_data["unnamed_0x00000008"]),
            unnamed_0x00000009=HealthInfo.from_json(json_data["unnamed_0x00000009"]),
            unnamed_0x0000000a=DamageVulnerability.from_json(json_data["unnamed_0x0000000a"]),
            into_activate_delay=json_data["into_activate_delay"],
            reload_time=json_data["reload_time"],
            reload_time_variance=json_data["reload_time_variance"],
            pan_start_time=json_data["pan_start_time"],
            pan_hold_time=json_data["pan_hold_time"],
            total_pan_search_time=json_data["total_pan_search_time"],
            left_max_angle=json_data["left_max_angle"],
            right_max_angle=json_data["right_max_angle"],
            down_max_angle=json_data["down_max_angle"],
            turn_speed=json_data["turn_speed"],
            detection_range=json_data["detection_range"],
            detection_z_range=json_data["detection_z_range"],
            freeze_duration=json_data["freeze_duration"],
            freeze_variance=json_data["freeze_variance"],
            freeze_timeout=json_data["freeze_timeout"],
            projectile_res=json_data["projectile_res"],
            unnamed_0x0000001b=DamageInfo.from_json(json_data["unnamed_0x0000001b"]),
            idle_light_res=json_data["idle_light_res"],
            deactivate_light_res=json_data["deactivate_light_res"],
            targetting_light_res=json_data["targetting_light_res"],
            frozen_effect_res=json_data["frozen_effect_res"],
            charging_effect_res=json_data["charging_effect_res"],
            panning_effect_res=json_data["panning_effect_res"],
            visor_effect_res=json_data["visor_effect_res"],
            tracking_sound_id=json_data["tracking_sound_id"],
            lock_on_sound_id=json_data["lock_on_sound_id"],
            unfreeze_sound_id=json_data["unfreeze_sound_id"],
            stop_clank_sound_id=json_data["stop_clank_sound_id"],
            charging_sound_id=json_data["charging_sound_id"],
            visor_sound_id=json_data["visor_sound_id"],
            extension_model_res_id=json_data["extension_model_res_id"],
            extension_drop_down_dist=json_data["extension_drop_down_dist"],
            num_initial_shots=json_data["num_initial_shots"],
            initial_shot_table_index=json_data["initial_shot_table_index"],
            num_subsequent_shots=json_data["num_subsequent_shots"],
            frenzy_duration=json_data["frenzy_duration"],
            scripted_start_only=json_data["scripted_start_only"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "type": self.type.to_json(),
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "collision_extend": self.collision_extend.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed_0x00000008": self.unnamed_0x00000008.to_json(),
            "unnamed_0x00000009": self.unnamed_0x00000009.to_json(),
            "unnamed_0x0000000a": self.unnamed_0x0000000a.to_json(),
            "into_activate_delay": self.into_activate_delay,
            "reload_time": self.reload_time,
            "reload_time_variance": self.reload_time_variance,
            "pan_start_time": self.pan_start_time,
            "pan_hold_time": self.pan_hold_time,
            "total_pan_search_time": self.total_pan_search_time,
            "left_max_angle": self.left_max_angle,
            "right_max_angle": self.right_max_angle,
            "down_max_angle": self.down_max_angle,
            "turn_speed": self.turn_speed,
            "detection_range": self.detection_range,
            "detection_z_range": self.detection_z_range,
            "freeze_duration": self.freeze_duration,
            "freeze_variance": self.freeze_variance,
            "freeze_timeout": self.freeze_timeout,
            "projectile_res": self.projectile_res,
            "unnamed_0x0000001b": self.unnamed_0x0000001b.to_json(),
            "idle_light_res": self.idle_light_res,
            "deactivate_light_res": self.deactivate_light_res,
            "targetting_light_res": self.targetting_light_res,
            "frozen_effect_res": self.frozen_effect_res,
            "charging_effect_res": self.charging_effect_res,
            "panning_effect_res": self.panning_effect_res,
            "visor_effect_res": self.visor_effect_res,
            "tracking_sound_id": self.tracking_sound_id,
            "lock_on_sound_id": self.lock_on_sound_id,
            "unfreeze_sound_id": self.unfreeze_sound_id,
            "stop_clank_sound_id": self.stop_clank_sound_id,
            "charging_sound_id": self.charging_sound_id,
            "visor_sound_id": self.visor_sound_id,
            "extension_model_res_id": self.extension_model_res_id,
            "extension_drop_down_dist": self.extension_drop_down_dist,
            "num_initial_shots": self.num_initial_shots,
            "initial_shot_table_index": self.initial_shot_table_index,
            "num_subsequent_shots": self.num_subsequent_shots,
            "frenzy_duration": self.frenzy_duration,
            "scripted_start_only": self.scripted_start_only,
        }

    def _dependencies_for_projectile_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_res)

    def _dependencies_for_idle_light_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.idle_light_res)

    def _dependencies_for_deactivate_light_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.deactivate_light_res)

    def _dependencies_for_targetting_light_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.targetting_light_res)

    def _dependencies_for_frozen_effect_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.frozen_effect_res)

    def _dependencies_for_charging_effect_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.charging_effect_res)

    def _dependencies_for_panning_effect_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.panning_effect_res)

    def _dependencies_for_visor_effect_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_effect_res)

    def _dependencies_for_tracking_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tracking_sound_id)

    def _dependencies_for_lock_on_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.lock_on_sound_id)

    def _dependencies_for_unfreeze_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unfreeze_sound_id)

    def _dependencies_for_stop_clank_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.stop_clank_sound_id)

    def _dependencies_for_charging_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.charging_sound_id)

    def _dependencies_for_visor_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.visor_sound_id)

    def _dependencies_for_extension_model_res_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.extension_model_res_id)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed_0x00000008.dependencies_for, "unnamed_0x00000008", "ActorParameters"),
            (self._dependencies_for_projectile_res, "projectile_res", "AssetId"),
            (self._dependencies_for_idle_light_res, "idle_light_res", "AssetId"),
            (self._dependencies_for_deactivate_light_res, "deactivate_light_res", "AssetId"),
            (self._dependencies_for_targetting_light_res, "targetting_light_res", "AssetId"),
            (self._dependencies_for_frozen_effect_res, "frozen_effect_res", "AssetId"),
            (self._dependencies_for_charging_effect_res, "charging_effect_res", "AssetId"),
            (self._dependencies_for_panning_effect_res, "panning_effect_res", "AssetId"),
            (self._dependencies_for_visor_effect_res, "visor_effect_res", "AssetId"),
            (self._dependencies_for_tracking_sound_id, "tracking_sound_id", "int"),
            (self._dependencies_for_lock_on_sound_id, "lock_on_sound_id", "int"),
            (self._dependencies_for_unfreeze_sound_id, "unfreeze_sound_id", "int"),
            (self._dependencies_for_stop_clank_sound_id, "stop_clank_sound_id", "int"),
            (self._dependencies_for_charging_sound_id, "charging_sound_id", "int"),
            (self._dependencies_for_visor_sound_id, "visor_sound_id", "int"),
            (self._dependencies_for_extension_model_res_id, "extension_model_res_id", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for GunTurret.{field_name} ({field_type}): {e}")
