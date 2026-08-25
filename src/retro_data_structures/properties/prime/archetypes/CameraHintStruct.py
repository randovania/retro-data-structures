# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraHintStructJson(typing_extensions.TypedDict):
        calculate_cam_pos: bool
        chase_allowed: bool
        boost_allowed: bool
        obscure_avoidance: bool
        volume_collider: bool
        apply_immediately: bool
        look_at_ball: bool
        hint_distance_selection: bool
        hint_distance_self_pos: bool
        control_interpolation: bool
        sinusoidal_interpolation: bool
        sinusoidal_interpolation_hintless: bool
        clamp_velocity: bool
        skip_cinematic: bool
        no_elevation_interp: bool
        direct_elevation: bool
        override_look_dir: bool
        no_elevation_vel_clamp: bool
        calculate_transform_from_prev_cam: bool
        no_spline: bool
        unknown_0x00000014: bool
        unknown_0x00000015: bool


@dataclasses.dataclass()
class CameraHintStruct(BaseProperty):
    calculate_cam_pos: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="CalculateCamPos"),
        },
    )
    chase_allowed: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="ChaseAllowed"),
        },
    )
    boost_allowed: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="BoostAllowed"),
        },
    )
    obscure_avoidance: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="ObscureAvoidance"),
        },
    )
    volume_collider: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="VolumeCollider"),
        },
    )
    apply_immediately: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000005, original_name="ApplyImmediately"),
        },
    )
    look_at_ball: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="LookAtBall"),
        },
    )
    hint_distance_selection: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="HintDistanceSelection"),
        },
    )
    hint_distance_self_pos: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="HintDistanceSelfPos"),
        },
    )
    control_interpolation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000009, original_name="ControlInterpolation"),
        },
    )
    sinusoidal_interpolation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="SinusoidalInterpolation"),
        },
    )
    sinusoidal_interpolation_hintless: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="SinusoidalInterpolationHintless"),
        },
    )
    clamp_velocity: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000C, original_name="ClampVelocity"),
        },
    )
    skip_cinematic: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="SkipCinematic"),
        },
    )
    no_elevation_interp: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="NoElevationInterp"),
        },
    )
    direct_elevation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="DirectElevation"),
        },
    )
    override_look_dir: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="OverrideLookDir"),
        },
    )
    no_elevation_vel_clamp: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000011, original_name="NoElevationVelClamp"),
        },
    )
    calculate_transform_from_prev_cam: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000012, original_name="CalculateTransformFromPrevCam"),
        },
    )
    no_spline: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000013, original_name="NoSpline"),
        },
    )
    unknown_0x00000014: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000014, original_name="Unknown"),
        },
    )
    unknown_0x00000015: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000015, original_name="Unknown"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        calculate_cam_pos = structs.BIG_bool_.unpack(data.read(1))[0]
        chase_allowed = structs.BIG_bool_.unpack(data.read(1))[0]
        boost_allowed = structs.BIG_bool_.unpack(data.read(1))[0]
        obscure_avoidance = structs.BIG_bool_.unpack(data.read(1))[0]
        volume_collider = structs.BIG_bool_.unpack(data.read(1))[0]
        apply_immediately = structs.BIG_bool_.unpack(data.read(1))[0]
        look_at_ball = structs.BIG_bool_.unpack(data.read(1))[0]
        hint_distance_selection = structs.BIG_bool_.unpack(data.read(1))[0]
        hint_distance_self_pos = structs.BIG_bool_.unpack(data.read(1))[0]
        control_interpolation = structs.BIG_bool_.unpack(data.read(1))[0]
        sinusoidal_interpolation = structs.BIG_bool_.unpack(data.read(1))[0]
        sinusoidal_interpolation_hintless = structs.BIG_bool_.unpack(data.read(1))[0]
        clamp_velocity = structs.BIG_bool_.unpack(data.read(1))[0]
        skip_cinematic = structs.BIG_bool_.unpack(data.read(1))[0]
        no_elevation_interp = structs.BIG_bool_.unpack(data.read(1))[0]
        direct_elevation = structs.BIG_bool_.unpack(data.read(1))[0]
        override_look_dir = structs.BIG_bool_.unpack(data.read(1))[0]
        no_elevation_vel_clamp = structs.BIG_bool_.unpack(data.read(1))[0]
        calculate_transform_from_prev_cam = structs.BIG_bool_.unpack(data.read(1))[0]
        no_spline = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_0x00000014 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_0x00000015 = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            calculate_cam_pos,
            chase_allowed,
            boost_allowed,
            obscure_avoidance,
            volume_collider,
            apply_immediately,
            look_at_ball,
            hint_distance_selection,
            hint_distance_self_pos,
            control_interpolation,
            sinusoidal_interpolation,
            sinusoidal_interpolation_hintless,
            clamp_velocity,
            skip_cinematic,
            no_elevation_interp,
            direct_elevation,
            override_look_dir,
            no_elevation_vel_clamp,
            calculate_transform_from_prev_cam,
            no_spline,
            unknown_0x00000014,
            unknown_0x00000015,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_bool_.pack(self.calculate_cam_pos))
        data.write(structs.BIG_bool_.pack(self.chase_allowed))
        data.write(structs.BIG_bool_.pack(self.boost_allowed))
        data.write(structs.BIG_bool_.pack(self.obscure_avoidance))
        data.write(structs.BIG_bool_.pack(self.volume_collider))
        data.write(structs.BIG_bool_.pack(self.apply_immediately))
        data.write(structs.BIG_bool_.pack(self.look_at_ball))
        data.write(structs.BIG_bool_.pack(self.hint_distance_selection))
        data.write(structs.BIG_bool_.pack(self.hint_distance_self_pos))
        data.write(structs.BIG_bool_.pack(self.control_interpolation))
        data.write(structs.BIG_bool_.pack(self.sinusoidal_interpolation))
        data.write(structs.BIG_bool_.pack(self.sinusoidal_interpolation_hintless))
        data.write(structs.BIG_bool_.pack(self.clamp_velocity))
        data.write(structs.BIG_bool_.pack(self.skip_cinematic))
        data.write(structs.BIG_bool_.pack(self.no_elevation_interp))
        data.write(structs.BIG_bool_.pack(self.direct_elevation))
        data.write(structs.BIG_bool_.pack(self.override_look_dir))
        data.write(structs.BIG_bool_.pack(self.no_elevation_vel_clamp))
        data.write(structs.BIG_bool_.pack(self.calculate_transform_from_prev_cam))
        data.write(structs.BIG_bool_.pack(self.no_spline))
        data.write(structs.BIG_bool_.pack(self.unknown_0x00000014))
        data.write(structs.BIG_bool_.pack(self.unknown_0x00000015))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraHintStructJson", data)
        return cls(
            calculate_cam_pos=json_data["calculate_cam_pos"],
            chase_allowed=json_data["chase_allowed"],
            boost_allowed=json_data["boost_allowed"],
            obscure_avoidance=json_data["obscure_avoidance"],
            volume_collider=json_data["volume_collider"],
            apply_immediately=json_data["apply_immediately"],
            look_at_ball=json_data["look_at_ball"],
            hint_distance_selection=json_data["hint_distance_selection"],
            hint_distance_self_pos=json_data["hint_distance_self_pos"],
            control_interpolation=json_data["control_interpolation"],
            sinusoidal_interpolation=json_data["sinusoidal_interpolation"],
            sinusoidal_interpolation_hintless=json_data["sinusoidal_interpolation_hintless"],
            clamp_velocity=json_data["clamp_velocity"],
            skip_cinematic=json_data["skip_cinematic"],
            no_elevation_interp=json_data["no_elevation_interp"],
            direct_elevation=json_data["direct_elevation"],
            override_look_dir=json_data["override_look_dir"],
            no_elevation_vel_clamp=json_data["no_elevation_vel_clamp"],
            calculate_transform_from_prev_cam=json_data["calculate_transform_from_prev_cam"],
            no_spline=json_data["no_spline"],
            unknown_0x00000014=json_data["unknown_0x00000014"],
            unknown_0x00000015=json_data["unknown_0x00000015"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "calculate_cam_pos": self.calculate_cam_pos,
            "chase_allowed": self.chase_allowed,
            "boost_allowed": self.boost_allowed,
            "obscure_avoidance": self.obscure_avoidance,
            "volume_collider": self.volume_collider,
            "apply_immediately": self.apply_immediately,
            "look_at_ball": self.look_at_ball,
            "hint_distance_selection": self.hint_distance_selection,
            "hint_distance_self_pos": self.hint_distance_self_pos,
            "control_interpolation": self.control_interpolation,
            "sinusoidal_interpolation": self.sinusoidal_interpolation,
            "sinusoidal_interpolation_hintless": self.sinusoidal_interpolation_hintless,
            "clamp_velocity": self.clamp_velocity,
            "skip_cinematic": self.skip_cinematic,
            "no_elevation_interp": self.no_elevation_interp,
            "direct_elevation": self.direct_elevation,
            "override_look_dir": self.override_look_dir,
            "no_elevation_vel_clamp": self.no_elevation_vel_clamp,
            "calculate_transform_from_prev_cam": self.calculate_transform_from_prev_cam,
            "no_spline": self.no_spline,
            "unknown_0x00000014": self.unknown_0x00000014,
            "unknown_0x00000015": self.unknown_0x00000015,
        }
