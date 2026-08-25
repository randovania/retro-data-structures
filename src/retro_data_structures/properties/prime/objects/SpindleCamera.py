# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.PlayerHintStruct import PlayerHintStruct
from retro_data_structures.properties.prime.archetypes.SpindleCameraStruct import SpindleCameraStruct
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SpindleCameraJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        active: bool
        unnamed: json_util.JsonObject
        hint_to_cam_dist_min_: float
        hint_to_cam_dist_max: float
        hint_to_cam_v_off_min: float
        hint_to_cam_v_off_max: float
        target_hint_to_cam_delta_angle_vel: json_util.JsonObject
        delta_angle_scale_with_cam_dist: json_util.JsonObject
        hint_to_cam_dist: json_util.JsonObject
        dist_offset_from_ball_dist: json_util.JsonObject
        hint_ball_to_cam_azimuth: json_util.JsonObject
        unused: json_util.JsonObject
        max_hint_ball_to_cam_azimuth: json_util.JsonObject
        cam_look_rel_azimuth: json_util.JsonObject
        look_pos_z_offset: json_util.JsonObject
        cam_pos_z_offset: json_util.JsonObject
        clamped_azimuth_from_hint_dir: json_util.JsonObject
        damping_azimuth_speed: json_util.JsonObject
        target_hint_to_cam_delta_angle_vel_range: json_util.JsonObject
        delete_hint_ball_dist: json_util.JsonObject
        recover_clamped_azimuth_from_hint_dir: json_util.JsonObject


@dataclasses.dataclass()
class SpindleCamera(BaseObjectType):
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
    unnamed: PlayerHintStruct = dataclasses.field(
        default_factory=PlayerHintStruct,
        metadata={
            "reflection": FieldReflection[PlayerHintStruct](
                PlayerHintStruct,
                id=0x00000004,
                original_name="4",
                from_json=PlayerHintStruct.from_json,
                to_json=PlayerHintStruct.to_json,
            ),
        },
    )
    hint_to_cam_dist_min_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="HintToCamDistMin "),
        },
    )
    hint_to_cam_dist_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="HintToCamDistMax"),
        },
    )
    hint_to_cam_v_off_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="HintToCamVOffMin"),
        },
    )
    hint_to_cam_v_off_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="HintToCamVOffMax"),
        },
    )
    target_hint_to_cam_delta_angle_vel: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000009,
                original_name="TargetHintToCamDeltaAngleVel",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    delta_angle_scale_with_cam_dist: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x0000000A,
                original_name="DeltaAngleScaleWithCamDist",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    hint_to_cam_dist: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x0000000B,
                original_name="HintToCamDist",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    dist_offset_from_ball_dist: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x0000000C,
                original_name="DistOffsetFromBallDist",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    hint_ball_to_cam_azimuth: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x0000000D,
                original_name="HintBallToCamAzimuth",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    unused: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x0000000E,
                original_name="unused",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    max_hint_ball_to_cam_azimuth: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x0000000F,
                original_name="MaxHintBallToCamAzimuth",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    cam_look_rel_azimuth: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000010,
                original_name="CamLookRelAzimuth",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    look_pos_z_offset: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000011,
                original_name="LookPosZOffset",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    cam_pos_z_offset: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000012,
                original_name="CamPosZOffset",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    clamped_azimuth_from_hint_dir: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000013,
                original_name="ClampedAzimuthFromHintDir",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    damping_azimuth_speed: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000014,
                original_name="DampingAzimuthSpeed",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    target_hint_to_cam_delta_angle_vel_range: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000015,
                original_name="TargetHintToCamDeltaAngleVelRange",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    delete_hint_ball_dist: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000016,
                original_name="DeleteHintBallDist",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    recover_clamped_azimuth_from_hint_dir: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x00000017,
                original_name="RecoverClampedAzimuthFromHintDir",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x71

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
        unnamed = PlayerHintStruct.from_stream(data, game, property_size)
        hint_to_cam_dist_min_ = structs.BIG_f.unpack(data.read(4))[0]
        hint_to_cam_dist_max = structs.BIG_f.unpack(data.read(4))[0]
        hint_to_cam_v_off_min = structs.BIG_f.unpack(data.read(4))[0]
        hint_to_cam_v_off_max = structs.BIG_f.unpack(data.read(4))[0]
        target_hint_to_cam_delta_angle_vel = SpindleCameraStruct.from_stream(data, game, property_size)
        delta_angle_scale_with_cam_dist = SpindleCameraStruct.from_stream(data, game, property_size)
        hint_to_cam_dist = SpindleCameraStruct.from_stream(data, game, property_size)
        dist_offset_from_ball_dist = SpindleCameraStruct.from_stream(data, game, property_size)
        hint_ball_to_cam_azimuth = SpindleCameraStruct.from_stream(data, game, property_size)
        unused = SpindleCameraStruct.from_stream(data, game, property_size)
        max_hint_ball_to_cam_azimuth = SpindleCameraStruct.from_stream(data, game, property_size)
        cam_look_rel_azimuth = SpindleCameraStruct.from_stream(data, game, property_size)
        look_pos_z_offset = SpindleCameraStruct.from_stream(data, game, property_size)
        cam_pos_z_offset = SpindleCameraStruct.from_stream(data, game, property_size)
        clamped_azimuth_from_hint_dir = SpindleCameraStruct.from_stream(data, game, property_size)
        damping_azimuth_speed = SpindleCameraStruct.from_stream(data, game, property_size)
        target_hint_to_cam_delta_angle_vel_range = SpindleCameraStruct.from_stream(data, game, property_size)
        delete_hint_ball_dist = SpindleCameraStruct.from_stream(data, game, property_size)
        recover_clamped_azimuth_from_hint_dir = SpindleCameraStruct.from_stream(data, game, property_size)
        return cls(
            name,
            position,
            rotation,
            active,
            unnamed,
            hint_to_cam_dist_min_,
            hint_to_cam_dist_max,
            hint_to_cam_v_off_min,
            hint_to_cam_v_off_max,
            target_hint_to_cam_delta_angle_vel,
            delta_angle_scale_with_cam_dist,
            hint_to_cam_dist,
            dist_offset_from_ball_dist,
            hint_ball_to_cam_azimuth,
            unused,
            max_hint_ball_to_cam_azimuth,
            cam_look_rel_azimuth,
            look_pos_z_offset,
            cam_pos_z_offset,
            clamped_azimuth_from_hint_dir,
            damping_azimuth_speed,
            target_hint_to_cam_delta_angle_vel_range,
            delete_hint_ball_dist,
            recover_clamped_azimuth_from_hint_dir,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x18")  # 24 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        self.unnamed.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.hint_to_cam_dist_min_))
        data.write(structs.BIG_f.pack(self.hint_to_cam_dist_max))
        data.write(structs.BIG_f.pack(self.hint_to_cam_v_off_min))
        data.write(structs.BIG_f.pack(self.hint_to_cam_v_off_max))
        self.target_hint_to_cam_delta_angle_vel.to_stream(data, game)
        self.delta_angle_scale_with_cam_dist.to_stream(data, game)
        self.hint_to_cam_dist.to_stream(data, game)
        self.dist_offset_from_ball_dist.to_stream(data, game)
        self.hint_ball_to_cam_azimuth.to_stream(data, game)
        self.unused.to_stream(data, game)
        self.max_hint_ball_to_cam_azimuth.to_stream(data, game)
        self.cam_look_rel_azimuth.to_stream(data, game)
        self.look_pos_z_offset.to_stream(data, game)
        self.cam_pos_z_offset.to_stream(data, game)
        self.clamped_azimuth_from_hint_dir.to_stream(data, game)
        self.damping_azimuth_speed.to_stream(data, game)
        self.target_hint_to_cam_delta_angle_vel_range.to_stream(data, game)
        self.delete_hint_ball_dist.to_stream(data, game)
        self.recover_clamped_azimuth_from_hint_dir.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpindleCameraJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            active=json_data["active"],
            unnamed=PlayerHintStruct.from_json(json_data["unnamed"]),
            hint_to_cam_dist_min_=json_data["hint_to_cam_dist_min_"],
            hint_to_cam_dist_max=json_data["hint_to_cam_dist_max"],
            hint_to_cam_v_off_min=json_data["hint_to_cam_v_off_min"],
            hint_to_cam_v_off_max=json_data["hint_to_cam_v_off_max"],
            target_hint_to_cam_delta_angle_vel=SpindleCameraStruct.from_json(
                json_data["target_hint_to_cam_delta_angle_vel"]
            ),
            delta_angle_scale_with_cam_dist=SpindleCameraStruct.from_json(json_data["delta_angle_scale_with_cam_dist"]),
            hint_to_cam_dist=SpindleCameraStruct.from_json(json_data["hint_to_cam_dist"]),
            dist_offset_from_ball_dist=SpindleCameraStruct.from_json(json_data["dist_offset_from_ball_dist"]),
            hint_ball_to_cam_azimuth=SpindleCameraStruct.from_json(json_data["hint_ball_to_cam_azimuth"]),
            unused=SpindleCameraStruct.from_json(json_data["unused"]),
            max_hint_ball_to_cam_azimuth=SpindleCameraStruct.from_json(json_data["max_hint_ball_to_cam_azimuth"]),
            cam_look_rel_azimuth=SpindleCameraStruct.from_json(json_data["cam_look_rel_azimuth"]),
            look_pos_z_offset=SpindleCameraStruct.from_json(json_data["look_pos_z_offset"]),
            cam_pos_z_offset=SpindleCameraStruct.from_json(json_data["cam_pos_z_offset"]),
            clamped_azimuth_from_hint_dir=SpindleCameraStruct.from_json(json_data["clamped_azimuth_from_hint_dir"]),
            damping_azimuth_speed=SpindleCameraStruct.from_json(json_data["damping_azimuth_speed"]),
            target_hint_to_cam_delta_angle_vel_range=SpindleCameraStruct.from_json(
                json_data["target_hint_to_cam_delta_angle_vel_range"]
            ),
            delete_hint_ball_dist=SpindleCameraStruct.from_json(json_data["delete_hint_ball_dist"]),
            recover_clamped_azimuth_from_hint_dir=SpindleCameraStruct.from_json(
                json_data["recover_clamped_azimuth_from_hint_dir"]
            ),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "active": self.active,
            "unnamed": self.unnamed.to_json(),
            "hint_to_cam_dist_min_": self.hint_to_cam_dist_min_,
            "hint_to_cam_dist_max": self.hint_to_cam_dist_max,
            "hint_to_cam_v_off_min": self.hint_to_cam_v_off_min,
            "hint_to_cam_v_off_max": self.hint_to_cam_v_off_max,
            "target_hint_to_cam_delta_angle_vel": self.target_hint_to_cam_delta_angle_vel.to_json(),
            "delta_angle_scale_with_cam_dist": self.delta_angle_scale_with_cam_dist.to_json(),
            "hint_to_cam_dist": self.hint_to_cam_dist.to_json(),
            "dist_offset_from_ball_dist": self.dist_offset_from_ball_dist.to_json(),
            "hint_ball_to_cam_azimuth": self.hint_ball_to_cam_azimuth.to_json(),
            "unused": self.unused.to_json(),
            "max_hint_ball_to_cam_azimuth": self.max_hint_ball_to_cam_azimuth.to_json(),
            "cam_look_rel_azimuth": self.cam_look_rel_azimuth.to_json(),
            "look_pos_z_offset": self.look_pos_z_offset.to_json(),
            "cam_pos_z_offset": self.cam_pos_z_offset.to_json(),
            "clamped_azimuth_from_hint_dir": self.clamped_azimuth_from_hint_dir.to_json(),
            "damping_azimuth_speed": self.damping_azimuth_speed.to_json(),
            "target_hint_to_cam_delta_angle_vel_range": self.target_hint_to_cam_delta_angle_vel_range.to_json(),
            "delete_hint_ball_dist": self.delete_hint_ball_dist.to_json(),
            "recover_clamped_azimuth_from_hint_dir": self.recover_clamped_azimuth_from_hint_dir.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
