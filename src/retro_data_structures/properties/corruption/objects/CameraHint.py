# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.CameraConstraints import CameraConstraints
from retro_data_structures.properties.corruption.archetypes.CameraFieldOfView import CameraFieldOfView
from retro_data_structures.properties.corruption.archetypes.CameraInterpolation import CameraInterpolation
from retro_data_structures.properties.corruption.archetypes.CameraMotion import CameraMotion
from retro_data_structures.properties.corruption.archetypes.CameraNavigation import CameraNavigation
from retro_data_structures.properties.corruption.archetypes.CameraOrientation import CameraOrientation
from retro_data_structures.properties.corruption.archetypes.CameraPosition import CameraPosition
from retro_data_structures.properties.corruption.archetypes.CameraRotation import CameraRotation
from retro_data_structures.properties.corruption.archetypes.InterpolationMethod import InterpolationMethod
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraHintJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        priority: int
        timer: float
        flags_camera_hint: int
        constraints: json_util.JsonObject
        position_behavior: json_util.JsonObject
        navigation_behavior: json_util.JsonObject
        motion_behavior: json_util.JsonObject
        orientation_behavior: json_util.JsonObject
        rotation_behavior: json_util.JsonObject
        field_of_view_behavior: json_util.JsonObject
        interpolation_behavior: json_util.JsonObject
        control_frame_interpolation: json_util.JsonObject


@dataclasses.dataclass()
class CameraHint(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    priority: int = dataclasses.field(
        default=50,
        metadata={
            "reflection": FieldReflection[int](int, id=0x42087650, original_name="Priority"),
        },
    )
    timer: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8747552E, original_name="Timer"),
        },
    )
    flags_camera_hint: int = dataclasses.field(
        default=30853,
        metadata={
            "reflection": FieldReflection[int](int, id=0x21D720A9, original_name="FlagsCameraHint"),
        },
    )  # Flagset
    constraints: CameraConstraints = dataclasses.field(
        default_factory=CameraConstraints,
        metadata={
            "reflection": FieldReflection[CameraConstraints](
                CameraConstraints,
                id=0x97A93F8F,
                original_name="Constraints",
                from_json=CameraConstraints.from_json,
                to_json=CameraConstraints.to_json,
            ),
        },
    )
    position_behavior: CameraPosition = dataclasses.field(
        default_factory=CameraPosition,
        metadata={
            "reflection": FieldReflection[CameraPosition](
                CameraPosition,
                id=0xD1BD5C40,
                original_name="PositionBehavior",
                from_json=CameraPosition.from_json,
                to_json=CameraPosition.to_json,
            ),
        },
    )
    navigation_behavior: CameraNavigation = dataclasses.field(
        default_factory=CameraNavigation,
        metadata={
            "reflection": FieldReflection[CameraNavigation](
                CameraNavigation,
                id=0x4BE3494B,
                original_name="NavigationBehavior",
                from_json=CameraNavigation.from_json,
                to_json=CameraNavigation.to_json,
            ),
        },
    )
    motion_behavior: CameraMotion = dataclasses.field(
        default_factory=CameraMotion,
        metadata={
            "reflection": FieldReflection[CameraMotion](
                CameraMotion,
                id=0xEBC3E775,
                original_name="MotionBehavior",
                from_json=CameraMotion.from_json,
                to_json=CameraMotion.to_json,
            ),
        },
    )
    orientation_behavior: CameraOrientation = dataclasses.field(
        default_factory=CameraOrientation,
        metadata={
            "reflection": FieldReflection[CameraOrientation](
                CameraOrientation,
                id=0x65FC11FF,
                original_name="OrientationBehavior",
                from_json=CameraOrientation.from_json,
                to_json=CameraOrientation.to_json,
            ),
        },
    )
    rotation_behavior: CameraRotation = dataclasses.field(
        default_factory=CameraRotation,
        metadata={
            "reflection": FieldReflection[CameraRotation](
                CameraRotation,
                id=0x00A7C38D,
                original_name="RotationBehavior",
                from_json=CameraRotation.from_json,
                to_json=CameraRotation.to_json,
            ),
        },
    )
    field_of_view_behavior: CameraFieldOfView = dataclasses.field(
        default_factory=CameraFieldOfView,
        metadata={
            "reflection": FieldReflection[CameraFieldOfView](
                CameraFieldOfView,
                id=0xFC126AD1,
                original_name="FieldOfViewBehavior",
                from_json=CameraFieldOfView.from_json,
                to_json=CameraFieldOfView.to_json,
            ),
        },
    )
    interpolation_behavior: CameraInterpolation = dataclasses.field(
        default_factory=CameraInterpolation,
        metadata={
            "reflection": FieldReflection[CameraInterpolation](
                CameraInterpolation,
                id=0x764827D4,
                original_name="InterpolationBehavior",
                from_json=CameraInterpolation.from_json,
                to_json=CameraInterpolation.to_json,
            ),
        },
    )
    control_frame_interpolation: InterpolationMethod = dataclasses.field(
        default_factory=InterpolationMethod,
        metadata={
            "reflection": FieldReflection[InterpolationMethod](
                InterpolationMethod,
                id=0x95D0D437,
                original_name="ControlFrameInterpolation",
                from_json=InterpolationMethod.from_json,
                to_json=InterpolationMethod.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CAMH"

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42087650
        priority = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8747552E
        timer = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21D720A9
        flags_camera_hint = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97A93F8F
        constraints = CameraConstraints.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1BD5C40
        position_behavior = CameraPosition.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4BE3494B
        navigation_behavior = CameraNavigation.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBC3E775
        motion_behavior = CameraMotion.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65FC11FF
        orientation_behavior = CameraOrientation.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00A7C38D
        rotation_behavior = CameraRotation.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC126AD1
        field_of_view_behavior = CameraFieldOfView.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x764827D4
        interpolation_behavior = CameraInterpolation.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95D0D437
        control_frame_interpolation = InterpolationMethod.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            priority,
            timer,
            flags_camera_hint,
            constraints,
            position_behavior,
            navigation_behavior,
            motion_behavior,
            orientation_behavior,
            rotation_behavior,
            field_of_view_behavior,
            interpolation_behavior,
            control_frame_interpolation,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\r")  # 13 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"B\x08vP")  # 0x42087650
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.priority))

        data.write(b"\x87GU.")  # 0x8747552e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.timer))

        data.write(b"!\xd7 \xa9")  # 0x21d720a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_camera_hint))

        data.write(b"\x97\xa9?\x8f")  # 0x97a93f8f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.constraints.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd1\xbd\\@")  # 0xd1bd5c40
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.position_behavior.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"K\xe3IK")  # 0x4be3494b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.navigation_behavior.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xeb\xc3\xe7u")  # 0xebc3e775
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_behavior.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"e\xfc\x11\xff")  # 0x65fc11ff
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.orientation_behavior.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\xa7\xc3\x8d")  # 0xa7c38d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.rotation_behavior.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfc\x12j\xd1")  # 0xfc126ad1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.field_of_view_behavior.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"vH'\xd4")  # 0x764827d4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.interpolation_behavior.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95\xd0\xd47")  # 0x95d0d437
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.control_frame_interpolation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraHintJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            priority=json_data["priority"],
            timer=json_data["timer"],
            flags_camera_hint=json_data["flags_camera_hint"],
            constraints=CameraConstraints.from_json(json_data["constraints"]),
            position_behavior=CameraPosition.from_json(json_data["position_behavior"]),
            navigation_behavior=CameraNavigation.from_json(json_data["navigation_behavior"]),
            motion_behavior=CameraMotion.from_json(json_data["motion_behavior"]),
            orientation_behavior=CameraOrientation.from_json(json_data["orientation_behavior"]),
            rotation_behavior=CameraRotation.from_json(json_data["rotation_behavior"]),
            field_of_view_behavior=CameraFieldOfView.from_json(json_data["field_of_view_behavior"]),
            interpolation_behavior=CameraInterpolation.from_json(json_data["interpolation_behavior"]),
            control_frame_interpolation=InterpolationMethod.from_json(json_data["control_frame_interpolation"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "priority": self.priority,
            "timer": self.timer,
            "flags_camera_hint": self.flags_camera_hint,
            "constraints": self.constraints.to_json(),
            "position_behavior": self.position_behavior.to_json(),
            "navigation_behavior": self.navigation_behavior.to_json(),
            "motion_behavior": self.motion_behavior.to_json(),
            "orientation_behavior": self.orientation_behavior.to_json(),
            "rotation_behavior": self.rotation_behavior.to_json(),
            "field_of_view_behavior": self.field_of_view_behavior.to_json(),
            "interpolation_behavior": self.interpolation_behavior.to_json(),
            "control_frame_interpolation": self.control_frame_interpolation.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_constraints(data: typing.BinaryIO, game: Game, property_size: int) -> CameraConstraints:
    return CameraConstraints.from_stream(data, game, property_size)


def _decode_position_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraPosition:
    return CameraPosition.from_stream(data, game, property_size)


def _decode_navigation_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraNavigation:
    return CameraNavigation.from_stream(data, game, property_size)


def _decode_motion_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraMotion:
    return CameraMotion.from_stream(data, game, property_size)


def _decode_orientation_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraOrientation:
    return CameraOrientation.from_stream(data, game, property_size)


def _decode_rotation_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraRotation:
    return CameraRotation.from_stream(data, game, property_size)


def _decode_field_of_view_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraFieldOfView:
    return CameraFieldOfView.from_stream(data, game, property_size)


def _decode_interpolation_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraInterpolation:
    return CameraInterpolation.from_stream(data, game, property_size)


def _decode_control_frame_interpolation(data: typing.BinaryIO, game: Game, property_size: int) -> InterpolationMethod:
    return InterpolationMethod.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x42087650: ("priority", structs.decode_BIG_l),
    0x8747552E: ("timer", structs.decode_BIG_f),
    0x21D720A9: ("flags_camera_hint", structs.decode_BIG_L),
    0x97A93F8F: ("constraints", _decode_constraints),
    0xD1BD5C40: ("position_behavior", _decode_position_behavior),
    0x4BE3494B: ("navigation_behavior", _decode_navigation_behavior),
    0xEBC3E775: ("motion_behavior", _decode_motion_behavior),
    0x65FC11FF: ("orientation_behavior", _decode_orientation_behavior),
    0x00A7C38D: ("rotation_behavior", _decode_rotation_behavior),
    0xFC126AD1: ("field_of_view_behavior", _decode_field_of_view_behavior),
    0x764827D4: ("interpolation_behavior", _decode_interpolation_behavior),
    0x95D0D437: ("control_frame_interpolation", _decode_control_frame_interpolation),
}
