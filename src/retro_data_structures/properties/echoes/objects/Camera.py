# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.common.archetypes.SplineType import SplineType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CameraJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        animation_time: float
        flags_cinematic_camera: int
        unknown: int
        motion_spline_type: json_util.JsonObject
        target_spline_type: json_util.JsonObject
        motion_control_spline: json_util.JsonObject
        target_control_spline: json_util.JsonObject
        fov_spline: json_util.JsonObject
        roll_spline: json_util.JsonObject
        slowmo_control_spline: json_util.JsonObject


class FlagsCinematicCamera(enum.IntFlag):
    LookAtPlayer = 1
    OutOfPlayerEye = 2
    IntoPlayerEye = 4
    CinematicSkip = 8
    FinishCineSkip = 16
    DisableInput = 32
    DrawPlayer = 64
    CheckFailsafe = 128
    CinematicPause = 256
    DisableOutOfInto = 512
    Sinusoidal = 1024
    IgnoreWatchedCheck = 2048
    HintToCamDir = 4096
    SkipBallCameraCinematic = 8192
    HintToBallDir = 16384

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
class Camera(BaseObjectType):
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
    animation_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2A53245A, original_name="AnimationTime"),
        },
    )
    flags_cinematic_camera: FlagsCinematicCamera = dataclasses.field(
        default=FlagsCinematicCamera(168),
        metadata={
            "reflection": FieldReflection[FlagsCinematicCamera](
                FlagsCinematicCamera,
                id=0x05C5FC6E,
                original_name="FlagsCinematicCamera",
                from_json=FlagsCinematicCamera.from_json,
                to_json=FlagsCinematicCamera.to_json,
            ),
        },
    )
    unknown: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD4B29446, original_name="Unknown"),
        },
    )
    motion_spline_type: SplineType = dataclasses.field(
        default_factory=SplineType,
        metadata={
            "reflection": FieldReflection[SplineType](
                SplineType,
                id=0x493D6A2D,
                original_name="MotionSplineType",
                from_json=SplineType.from_json,
                to_json=SplineType.to_json,
            ),
        },
    )
    target_spline_type: SplineType = dataclasses.field(
        default_factory=SplineType,
        metadata={
            "reflection": FieldReflection[SplineType](
                SplineType,
                id=0x5604D304,
                original_name="TargetSplineType",
                from_json=SplineType.from_json,
                to_json=SplineType.to_json,
            ),
        },
    )
    motion_control_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x27E5F874,
                original_name="MotionControlSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    target_control_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xC4DFBFA7,
                original_name="TargetControlSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    fov_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x6868D4B3, original_name="FOVSpline", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    roll_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x6E6D8EFD, original_name="RollSpline", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    slowmo_control_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xF4F4798E,
                original_name="SlowmoControlSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CAMR"

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
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={"active": False})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2A53245A
        animation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05C5FC6E
        flags_cinematic_camera = FlagsCinematicCamera.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4B29446
        unknown = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x493D6A2D
        motion_spline_type = SplineType.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5604D304
        target_spline_type = SplineType.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27E5F874
        motion_control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4DFBFA7
        target_control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6868D4B3
        fov_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E6D8EFD
        roll_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4F4798E
        slowmo_control_spline = Spline.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            animation_time,
            flags_cinematic_camera,
            unknown,
            motion_spline_type,
            target_spline_type,
            motion_control_spline,
            target_control_spline,
            fov_spline,
            roll_spline,
            slowmo_control_spline,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={"active": False})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"*S$Z")  # 0x2a53245a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.animation_time))

        data.write(b"\x05\xc5\xfcn")  # 0x5c5fc6e
        data.write(b"\x00\x04")  # size
        self.flags_cinematic_camera.to_stream(data, game)

        data.write(b"\xd4\xb2\x94F")  # 0xd4b29446
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown))

        data.write(b"I=j-")  # 0x493d6a2d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"V\x04\xd3\x04")  # 0x5604d304
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.target_spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"'\xe5\xf8t")  # 0x27e5f874
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc4\xdf\xbf\xa7")  # 0xc4dfbfa7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.target_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"hh\xd4\xb3")  # 0x6868d4b3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.fov_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"nm\x8e\xfd")  # 0x6e6d8efd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.roll_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4\xf4y\x8e")  # 0xf4f4798e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.slowmo_control_spline.to_stream(data, game)
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
        json_data = typing.cast("CameraJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            animation_time=json_data["animation_time"],
            flags_cinematic_camera=FlagsCinematicCamera.from_json(json_data["flags_cinematic_camera"]),
            unknown=json_data["unknown"],
            motion_spline_type=SplineType.from_json(json_data["motion_spline_type"]),
            target_spline_type=SplineType.from_json(json_data["target_spline_type"]),
            motion_control_spline=Spline.from_json(json_data["motion_control_spline"]),
            target_control_spline=Spline.from_json(json_data["target_control_spline"]),
            fov_spline=Spline.from_json(json_data["fov_spline"]),
            roll_spline=Spline.from_json(json_data["roll_spline"]),
            slowmo_control_spline=Spline.from_json(json_data["slowmo_control_spline"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "animation_time": self.animation_time,
            "flags_cinematic_camera": self.flags_cinematic_camera.to_json(),
            "unknown": self.unknown,
            "motion_spline_type": self.motion_spline_type.to_json(),
            "target_spline_type": self.target_spline_type.to_json(),
            "motion_control_spline": self.motion_control_spline.to_json(),
            "target_control_spline": self.target_control_spline.to_json(),
            "fov_spline": self.fov_spline.to_json(),
            "roll_spline": self.roll_spline.to_json(),
            "slowmo_control_spline": self.slowmo_control_spline.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={"active": False})


def _decode_flags_cinematic_camera(data: typing.BinaryIO, game: Game, property_size: int) -> FlagsCinematicCamera:
    return FlagsCinematicCamera.from_stream(data, game)


def _decode_motion_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_target_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_motion_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_target_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fov_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_roll_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_slowmo_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x2A53245A: ("animation_time", structs.decode_BIG_f),
    0x05C5FC6E: ("flags_cinematic_camera", _decode_flags_cinematic_camera),
    0xD4B29446: ("unknown", structs.decode_BIG_l),
    0x493D6A2D: ("motion_spline_type", _decode_motion_spline_type),
    0x5604D304: ("target_spline_type", _decode_target_spline_type),
    0x27E5F874: ("motion_control_spline", _decode_motion_control_spline),
    0xC4DFBFA7: ("target_control_spline", _decode_target_control_spline),
    0x6868D4B3: ("fov_spline", _decode_fov_spline),
    0x6E6D8EFD: ("roll_spline", _decode_roll_spline),
    0xF4F4798E: ("slowmo_control_spline", _decode_slowmo_control_spline),
}
