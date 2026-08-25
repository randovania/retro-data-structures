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

    class GrappleParametersJson(typing_extensions.TypedDict):
        grapple_length: float
        grapple_attach_length: float
        grapple_spring_constant: float
        grapple_spring_length: float
        unknown: float
        swing_force: float
        swing_max_force: float
        swing_arc_angle: float
        swing_turn_angle: float
        swing_camera_pitch: float
        swing_camera_max_pitch: float
        lock_swing_turn: bool


@dataclasses.dataclass()
class GrappleParameters(BaseProperty):
    grapple_length: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="GrappleLength"),
        },
    )
    grapple_attach_length: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="GrappleAttachLength"),
        },
    )
    grapple_spring_constant: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="GrappleSpringConstant"),
        },
    )
    grapple_spring_length: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="GrappleSpringLength"),
        },
    )
    unknown: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Unknown"),
        },
    )
    swing_force: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="SwingForce"),
        },
    )
    swing_max_force: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="SwingMaxForce"),
        },
    )
    swing_arc_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="SwingArcAngle"),
        },
    )
    swing_turn_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="SwingTurnAngle"),
        },
    )
    swing_camera_pitch: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="SwingCameraPitch"),
        },
    )
    swing_camera_max_pitch: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="SwingCameraMaxPitch"),
        },
    )
    lock_swing_turn: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="LockSwingTurn"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        grapple_length = structs.BIG_f.unpack(data.read(4))[0]
        grapple_attach_length = structs.BIG_f.unpack(data.read(4))[0]
        grapple_spring_constant = structs.BIG_f.unpack(data.read(4))[0]
        grapple_spring_length = structs.BIG_f.unpack(data.read(4))[0]
        unknown = structs.BIG_f.unpack(data.read(4))[0]
        swing_force = structs.BIG_f.unpack(data.read(4))[0]
        swing_max_force = structs.BIG_f.unpack(data.read(4))[0]
        swing_arc_angle = structs.BIG_f.unpack(data.read(4))[0]
        swing_turn_angle = structs.BIG_f.unpack(data.read(4))[0]
        swing_camera_pitch = structs.BIG_f.unpack(data.read(4))[0]
        swing_camera_max_pitch = structs.BIG_f.unpack(data.read(4))[0]
        lock_swing_turn = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            grapple_length,
            grapple_attach_length,
            grapple_spring_constant,
            grapple_spring_length,
            unknown,
            swing_force,
            swing_max_force,
            swing_arc_angle,
            swing_turn_angle,
            swing_camera_pitch,
            swing_camera_max_pitch,
            lock_swing_turn,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_f.pack(self.grapple_length))
        data.write(structs.BIG_f.pack(self.grapple_attach_length))
        data.write(structs.BIG_f.pack(self.grapple_spring_constant))
        data.write(structs.BIG_f.pack(self.grapple_spring_length))
        data.write(structs.BIG_f.pack(self.unknown))
        data.write(structs.BIG_f.pack(self.swing_force))
        data.write(structs.BIG_f.pack(self.swing_max_force))
        data.write(structs.BIG_f.pack(self.swing_arc_angle))
        data.write(structs.BIG_f.pack(self.swing_turn_angle))
        data.write(structs.BIG_f.pack(self.swing_camera_pitch))
        data.write(structs.BIG_f.pack(self.swing_camera_max_pitch))
        data.write(structs.BIG_bool_.pack(self.lock_swing_turn))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GrappleParametersJson", data)
        return cls(
            grapple_length=json_data["grapple_length"],
            grapple_attach_length=json_data["grapple_attach_length"],
            grapple_spring_constant=json_data["grapple_spring_constant"],
            grapple_spring_length=json_data["grapple_spring_length"],
            unknown=json_data["unknown"],
            swing_force=json_data["swing_force"],
            swing_max_force=json_data["swing_max_force"],
            swing_arc_angle=json_data["swing_arc_angle"],
            swing_turn_angle=json_data["swing_turn_angle"],
            swing_camera_pitch=json_data["swing_camera_pitch"],
            swing_camera_max_pitch=json_data["swing_camera_max_pitch"],
            lock_swing_turn=json_data["lock_swing_turn"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "grapple_length": self.grapple_length,
            "grapple_attach_length": self.grapple_attach_length,
            "grapple_spring_constant": self.grapple_spring_constant,
            "grapple_spring_length": self.grapple_spring_length,
            "unknown": self.unknown,
            "swing_force": self.swing_force,
            "swing_max_force": self.swing_max_force,
            "swing_arc_angle": self.swing_arc_angle,
            "swing_turn_angle": self.swing_turn_angle,
            "swing_camera_pitch": self.swing_camera_pitch,
            "swing_camera_max_pitch": self.swing_camera_max_pitch,
            "lock_swing_turn": self.lock_swing_turn,
        }
