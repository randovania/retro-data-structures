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
from retro_data_structures.properties.prime.archetypes.BoolFloat import BoolFloat
from retro_data_structures.properties.prime.archetypes.BoolVec3f import BoolVec3f
from retro_data_structures.properties.prime.archetypes.CameraHintStruct import CameraHintStruct
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CameraHintJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        active: bool
        priority: int
        ball_camera_behavior: int
        ball_camera_hints: json_util.JsonObject
        min_distance: json_util.JsonObject
        max_distance: json_util.JsonObject
        backwards_distance: json_util.JsonObject
        look_at_offset: json_util.JsonObject
        chase_look_at_offset: json_util.JsonObject
        ball_to_camera: json_util.JsonValue
        field_of_view: json_util.JsonObject
        attitude_range: json_util.JsonObject
        azimuth_range: json_util.JsonObject
        angle_per_second: json_util.JsonObject
        clamp_velocity_range: float
        clamp_rotation_range: float
        elevation: json_util.JsonObject
        interpolate_time: float
        clamp_velocity_time: float
        control_interpolation_duration: float


class BallCameraBehavior(enum.IntEnum):
    Default = 0
    FreezeLookPosition = 1
    HintBallToCamera = 2
    HintInitializePosition = 3
    HintFixedPosition = 4
    HintFixedTransform = 5
    PathCameraDesiredPosition = 6
    PathCamera = 7
    SpindleCamera = 8

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
class CameraHint(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000001, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Active"),
        },
    )
    priority: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="Priority"),
        },
    )
    ball_camera_behavior: BallCameraBehavior = dataclasses.field(
        default=BallCameraBehavior.Default,
        metadata={
            "reflection": FieldReflection[BallCameraBehavior](
                BallCameraBehavior,
                id=0x00000005,
                original_name="BallCameraBehavior",
                from_json=BallCameraBehavior.from_json,
                to_json=BallCameraBehavior.to_json,
            ),
        },
    )
    ball_camera_hints: CameraHintStruct = dataclasses.field(
        default_factory=CameraHintStruct,
        metadata={
            "reflection": FieldReflection[CameraHintStruct](
                CameraHintStruct,
                id=0x00000006,
                original_name="BallCameraHints",
                from_json=CameraHintStruct.from_json,
                to_json=CameraHintStruct.to_json,
            ),
        },
    )
    min_distance: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x00000007,
                original_name="MinDistance",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    max_distance: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x00000008,
                original_name="MaxDistance",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    backwards_distance: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x00000009,
                original_name="BackwardsDistance",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    look_at_offset: BoolVec3f = dataclasses.field(
        default_factory=BoolVec3f,
        metadata={
            "reflection": FieldReflection[BoolVec3f](
                BoolVec3f,
                id=0x0000000A,
                original_name="LookAtOffset",
                from_json=BoolVec3f.from_json,
                to_json=BoolVec3f.to_json,
            ),
        },
    )
    chase_look_at_offset: BoolVec3f = dataclasses.field(
        default_factory=BoolVec3f,
        metadata={
            "reflection": FieldReflection[BoolVec3f](
                BoolVec3f,
                id=0x0000000B,
                original_name="ChaseLookAtOffset",
                from_json=BoolVec3f.from_json,
                to_json=BoolVec3f.to_json,
            ),
        },
    )
    ball_to_camera: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x0000000C, original_name="BallToCamera", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    field_of_view: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x0000000D,
                original_name="FieldOfView",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    attitude_range: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x0000000E,
                original_name="AttitudeRange",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    azimuth_range: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x0000000F,
                original_name="AzimuthRange",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    angle_per_second: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x00000010,
                original_name="AnglePerSecond",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    clamp_velocity_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="ClampVelocityRange"),
        },
    )
    clamp_rotation_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="ClampRotationRange"),
        },
    )
    elevation: BoolFloat = dataclasses.field(
        default_factory=BoolFloat,
        metadata={
            "reflection": FieldReflection[BoolFloat](
                BoolFloat,
                id=0x00000013,
                original_name="Elevation",
                from_json=BoolFloat.from_json,
                to_json=BoolFloat.to_json,
            ),
        },
    )
    interpolate_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="InterpolateTime"),
        },
    )
    clamp_velocity_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="ClampVelocityTime"),
        },
    )
    control_interpolation_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="ControlInterpolationDuration"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x10

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        priority = structs.BIG_l.unpack(data.read(4))[0]
        ball_camera_behavior = BallCameraBehavior.from_stream(data, game)
        ball_camera_hints = CameraHintStruct.from_stream(data, game, property_size)
        min_distance = BoolFloat.from_stream(data, game, property_size)
        max_distance = BoolFloat.from_stream(data, game, property_size)
        backwards_distance = BoolFloat.from_stream(data, game, property_size)
        look_at_offset = BoolVec3f.from_stream(data, game, property_size)
        chase_look_at_offset = BoolVec3f.from_stream(data, game, property_size)
        ball_to_camera = Vector.from_stream(data, game, property_size)
        field_of_view = BoolFloat.from_stream(data, game, property_size)
        attitude_range = BoolFloat.from_stream(data, game, property_size)
        azimuth_range = BoolFloat.from_stream(data, game, property_size)
        angle_per_second = BoolFloat.from_stream(data, game, property_size)
        clamp_velocity_range = structs.BIG_f.unpack(data.read(4))[0]
        clamp_rotation_range = structs.BIG_f.unpack(data.read(4))[0]
        elevation = BoolFloat.from_stream(data, game, property_size)
        interpolate_time = structs.BIG_f.unpack(data.read(4))[0]
        clamp_velocity_time = structs.BIG_f.unpack(data.read(4))[0]
        control_interpolation_duration = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            active,
            priority,
            ball_camera_behavior,
            ball_camera_hints,
            min_distance,
            max_distance,
            backwards_distance,
            look_at_offset,
            chase_look_at_offset,
            ball_to_camera,
            field_of_view,
            attitude_range,
            azimuth_range,
            angle_per_second,
            clamp_velocity_range,
            clamp_rotation_range,
            elevation,
            interpolate_time,
            clamp_velocity_time,
            control_interpolation_duration,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x17")  # 23 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_l.pack(self.priority))
        self.ball_camera_behavior.to_stream(data, game)
        self.ball_camera_hints.to_stream(data, game)
        self.min_distance.to_stream(data, game)
        self.max_distance.to_stream(data, game)
        self.backwards_distance.to_stream(data, game)
        self.look_at_offset.to_stream(data, game)
        self.chase_look_at_offset.to_stream(data, game)
        self.ball_to_camera.to_stream(data, game)
        self.field_of_view.to_stream(data, game)
        self.attitude_range.to_stream(data, game)
        self.azimuth_range.to_stream(data, game)
        self.angle_per_second.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.clamp_velocity_range))
        data.write(structs.BIG_f.pack(self.clamp_rotation_range))
        self.elevation.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.interpolate_time))
        data.write(structs.BIG_f.pack(self.clamp_velocity_time))
        data.write(structs.BIG_f.pack(self.control_interpolation_duration))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraHintJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            active=json_data["active"],
            priority=json_data["priority"],
            ball_camera_behavior=BallCameraBehavior.from_json(json_data["ball_camera_behavior"]),
            ball_camera_hints=CameraHintStruct.from_json(json_data["ball_camera_hints"]),
            min_distance=BoolFloat.from_json(json_data["min_distance"]),
            max_distance=BoolFloat.from_json(json_data["max_distance"]),
            backwards_distance=BoolFloat.from_json(json_data["backwards_distance"]),
            look_at_offset=BoolVec3f.from_json(json_data["look_at_offset"]),
            chase_look_at_offset=BoolVec3f.from_json(json_data["chase_look_at_offset"]),
            ball_to_camera=Vector.from_json(json_data["ball_to_camera"]),
            field_of_view=BoolFloat.from_json(json_data["field_of_view"]),
            attitude_range=BoolFloat.from_json(json_data["attitude_range"]),
            azimuth_range=BoolFloat.from_json(json_data["azimuth_range"]),
            angle_per_second=BoolFloat.from_json(json_data["angle_per_second"]),
            clamp_velocity_range=json_data["clamp_velocity_range"],
            clamp_rotation_range=json_data["clamp_rotation_range"],
            elevation=BoolFloat.from_json(json_data["elevation"]),
            interpolate_time=json_data["interpolate_time"],
            clamp_velocity_time=json_data["clamp_velocity_time"],
            control_interpolation_duration=json_data["control_interpolation_duration"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "active": self.active,
            "priority": self.priority,
            "ball_camera_behavior": self.ball_camera_behavior.to_json(),
            "ball_camera_hints": self.ball_camera_hints.to_json(),
            "min_distance": self.min_distance.to_json(),
            "max_distance": self.max_distance.to_json(),
            "backwards_distance": self.backwards_distance.to_json(),
            "look_at_offset": self.look_at_offset.to_json(),
            "chase_look_at_offset": self.chase_look_at_offset.to_json(),
            "ball_to_camera": self.ball_to_camera.to_json(),
            "field_of_view": self.field_of_view.to_json(),
            "attitude_range": self.attitude_range.to_json(),
            "azimuth_range": self.azimuth_range.to_json(),
            "angle_per_second": self.angle_per_second.to_json(),
            "clamp_velocity_range": self.clamp_velocity_range,
            "clamp_rotation_range": self.clamp_rotation_range,
            "elevation": self.elevation.to_json(),
            "interpolate_time": self.interpolate_time,
            "clamp_velocity_time": self.clamp_velocity_time,
            "control_interpolation_duration": self.control_interpolation_duration,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
