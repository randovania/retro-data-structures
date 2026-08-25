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
from retro_data_structures.properties.corruption.archetypes.CameraOrientation import CameraOrientation
from retro_data_structures.properties.corruption.archetypes.CinematicBlend import CinematicBlend
from retro_data_structures.properties.corruption.archetypes.SavedStateID import SavedStateID
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CinematicCameraJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        object_id: json_util.JsonObject
        camera_mode: int
        use_script_object_transform: bool
        animation: json_util.JsonObject
        cinematic_start_type: int
        blend: json_util.JsonObject
        cinematic_ends_type: int
        end_time: float
        flags_cinematic_camera: int
        motion_control_spline: json_util.JsonObject
        target_control_spline: json_util.JsonObject
        orientation_behavior: json_util.JsonObject
        fov_spline: json_util.JsonObject
        roll_spline: json_util.JsonObject
        slowmo_control_spline: json_util.JsonObject
        near_plane_distance_spline: json_util.JsonObject
        far_plane_distance_spline: json_util.JsonObject


class CameraMode(enum.IntEnum):
    Unknown1 = 2247187997
    Unknown2 = 2392533015

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


class CinematicStartType(enum.IntEnum):
    Unknown1 = 3248813110
    Unknown2 = 2415426910
    Unknown3 = 3516177437
    Unknown4 = 2852706775
    Unknown5 = 1552481122

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


class CinematicEndsType(enum.IntEnum):
    Unknown1 = 1671241623
    Unknown2 = 3042939236
    Unknown3 = 1097122971
    Unknown4 = 4076161679

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
class CinematicCamera(BaseObjectType):
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
    object_id: SavedStateID = dataclasses.field(
        default_factory=SavedStateID,
        metadata={
            "reflection": FieldReflection[SavedStateID](
                SavedStateID,
                id=0x16D9A75D,
                original_name="ObjectId",
                from_json=SavedStateID.from_json,
                to_json=SavedStateID.to_json,
            ),
        },
    )
    camera_mode: CameraMode = dataclasses.field(
        default=CameraMode.Unknown1,
        metadata={
            "reflection": FieldReflection[CameraMode](
                CameraMode,
                id=0xCC08EF1B,
                original_name="CameraMode",
                from_json=CameraMode.from_json,
                to_json=CameraMode.to_json,
            ),
        },
    )
    use_script_object_transform: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6387E44B, original_name="UseScriptObjectTransform"),
        },
    )
    animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xA3D63F44,
                original_name="Animation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    cinematic_start_type: CinematicStartType = dataclasses.field(
        default=CinematicStartType.Unknown1,
        metadata={
            "reflection": FieldReflection[CinematicStartType](
                CinematicStartType,
                id=0xB1AC9176,
                original_name="CinematicStartType",
                from_json=CinematicStartType.from_json,
                to_json=CinematicStartType.to_json,
            ),
        },
    )
    blend: CinematicBlend = dataclasses.field(
        default_factory=CinematicBlend,
        metadata={
            "reflection": FieldReflection[CinematicBlend](
                CinematicBlend,
                id=0x9EC65273,
                original_name="Blend",
                from_json=CinematicBlend.from_json,
                to_json=CinematicBlend.to_json,
            ),
        },
    )
    cinematic_ends_type: CinematicEndsType = dataclasses.field(
        default=CinematicEndsType.Unknown1,
        metadata={
            "reflection": FieldReflection[CinematicEndsType](
                CinematicEndsType,
                id=0x974A961F,
                original_name="CinematicEndsType",
                from_json=CinematicEndsType.from_json,
                to_json=CinematicEndsType.to_json,
            ),
        },
    )
    end_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAB8151EA, original_name="EndTime"),
        },
    )
    flags_cinematic_camera: int = dataclasses.field(
        default=2132,
        metadata={
            "reflection": FieldReflection[int](int, id=0x05C5FC6E, original_name="FlagsCinematicCamera"),
        },
    )  # Flagset
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
    near_plane_distance_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x29515802,
                original_name="NearPlaneDistanceSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    far_plane_distance_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xDF1865A6,
                original_name="FarPlaneDistanceSpline",
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
        return "CINE"

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
        if property_count != 18:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16D9A75D
        object_id = SavedStateID.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC08EF1B
        camera_mode = CameraMode.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6387E44B
        use_script_object_transform = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3D63F44
        animation = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB1AC9176
        cinematic_start_type = CinematicStartType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9EC65273
        blend = CinematicBlend.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x974A961F
        cinematic_ends_type = CinematicEndsType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB8151EA
        end_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05C5FC6E
        flags_cinematic_camera = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27E5F874
        motion_control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4DFBFA7
        target_control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65FC11FF
        orientation_behavior = CameraOrientation.from_stream(
            data, game, property_size, default_override={"orientation_type": 648890987, "flags_orientation": 12}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6868D4B3
        fov_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E6D8EFD
        roll_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4F4798E
        slowmo_control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29515802
        near_plane_distance_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF1865A6
        far_plane_distance_spline = Spline.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            object_id,
            camera_mode,
            use_script_object_transform,
            animation,
            cinematic_start_type,
            blend,
            cinematic_ends_type,
            end_time,
            flags_cinematic_camera,
            motion_control_spline,
            target_control_spline,
            orientation_behavior,
            fov_spline,
            roll_spline,
            slowmo_control_spline,
            near_plane_distance_spline,
            far_plane_distance_spline,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x12")  # 18 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x16\xd9\xa7]")  # 0x16d9a75d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.object_id.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcc\x08\xef\x1b")  # 0xcc08ef1b
        data.write(b"\x00\x04")  # size
        self.camera_mode.to_stream(data, game)

        data.write(b"c\x87\xe4K")  # 0x6387e44b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_script_object_transform))

        data.write(b"\xa3\xd6?D")  # 0xa3d63f44
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb1\xac\x91v")  # 0xb1ac9176
        data.write(b"\x00\x04")  # size
        self.cinematic_start_type.to_stream(data, game)

        data.write(b"\x9e\xc6Rs")  # 0x9ec65273
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.blend.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x97J\x96\x1f")  # 0x974a961f
        data.write(b"\x00\x04")  # size
        self.cinematic_ends_type.to_stream(data, game)

        data.write(b"\xab\x81Q\xea")  # 0xab8151ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.end_time))

        data.write(b"\x05\xc5\xfcn")  # 0x5c5fc6e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_cinematic_camera))

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

        data.write(b"e\xfc\x11\xff")  # 0x65fc11ff
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.orientation_behavior.to_stream(
            data, game, default_override={"orientation_type": 648890987, "flags_orientation": 12}
        )
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

        data.write(b")QX\x02")  # 0x29515802
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.near_plane_distance_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdf\x18e\xa6")  # 0xdf1865a6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.far_plane_distance_spline.to_stream(data, game)
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
        json_data = typing.cast("CinematicCameraJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            object_id=SavedStateID.from_json(json_data["object_id"]),
            camera_mode=CameraMode.from_json(json_data["camera_mode"]),
            use_script_object_transform=json_data["use_script_object_transform"],
            animation=AnimationParameters.from_json(json_data["animation"]),
            cinematic_start_type=CinematicStartType.from_json(json_data["cinematic_start_type"]),
            blend=CinematicBlend.from_json(json_data["blend"]),
            cinematic_ends_type=CinematicEndsType.from_json(json_data["cinematic_ends_type"]),
            end_time=json_data["end_time"],
            flags_cinematic_camera=json_data["flags_cinematic_camera"],
            motion_control_spline=Spline.from_json(json_data["motion_control_spline"]),
            target_control_spline=Spline.from_json(json_data["target_control_spline"]),
            orientation_behavior=CameraOrientation.from_json(json_data["orientation_behavior"]),
            fov_spline=Spline.from_json(json_data["fov_spline"]),
            roll_spline=Spline.from_json(json_data["roll_spline"]),
            slowmo_control_spline=Spline.from_json(json_data["slowmo_control_spline"]),
            near_plane_distance_spline=Spline.from_json(json_data["near_plane_distance_spline"]),
            far_plane_distance_spline=Spline.from_json(json_data["far_plane_distance_spline"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "object_id": self.object_id.to_json(),
            "camera_mode": self.camera_mode.to_json(),
            "use_script_object_transform": self.use_script_object_transform,
            "animation": self.animation.to_json(),
            "cinematic_start_type": self.cinematic_start_type.to_json(),
            "blend": self.blend.to_json(),
            "cinematic_ends_type": self.cinematic_ends_type.to_json(),
            "end_time": self.end_time,
            "flags_cinematic_camera": self.flags_cinematic_camera,
            "motion_control_spline": self.motion_control_spline.to_json(),
            "target_control_spline": self.target_control_spline.to_json(),
            "orientation_behavior": self.orientation_behavior.to_json(),
            "fov_spline": self.fov_spline.to_json(),
            "roll_spline": self.roll_spline.to_json(),
            "slowmo_control_spline": self.slowmo_control_spline.to_json(),
            "near_plane_distance_spline": self.near_plane_distance_spline.to_json(),
            "far_plane_distance_spline": self.far_plane_distance_spline.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_object_id(data: typing.BinaryIO, game: Game, property_size: int) -> SavedStateID:
    return SavedStateID.from_stream(data, game, property_size)


def _decode_camera_mode(data: typing.BinaryIO, game: Game, property_size: int) -> CameraMode:
    return CameraMode.from_stream(data, game)


def _decode_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_cinematic_start_type(data: typing.BinaryIO, game: Game, property_size: int) -> CinematicStartType:
    return CinematicStartType.from_stream(data, game)


def _decode_blend(data: typing.BinaryIO, game: Game, property_size: int) -> CinematicBlend:
    return CinematicBlend.from_stream(data, game, property_size)


def _decode_cinematic_ends_type(data: typing.BinaryIO, game: Game, property_size: int) -> CinematicEndsType:
    return CinematicEndsType.from_stream(data, game)


def _decode_motion_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_target_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_orientation_behavior(data: typing.BinaryIO, game: Game, property_size: int) -> CameraOrientation:
    return CameraOrientation.from_stream(
        data, game, property_size, default_override={"orientation_type": 648890987, "flags_orientation": 12}
    )


def _decode_fov_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_roll_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_slowmo_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_near_plane_distance_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_far_plane_distance_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x16D9A75D: ("object_id", _decode_object_id),
    0xCC08EF1B: ("camera_mode", _decode_camera_mode),
    0x6387E44B: ("use_script_object_transform", structs.decode_BIG_bool_),
    0xA3D63F44: ("animation", _decode_animation),
    0xB1AC9176: ("cinematic_start_type", _decode_cinematic_start_type),
    0x9EC65273: ("blend", _decode_blend),
    0x974A961F: ("cinematic_ends_type", _decode_cinematic_ends_type),
    0xAB8151EA: ("end_time", structs.decode_BIG_f),
    0x05C5FC6E: ("flags_cinematic_camera", structs.decode_BIG_L),
    0x27E5F874: ("motion_control_spline", _decode_motion_control_spline),
    0xC4DFBFA7: ("target_control_spline", _decode_target_control_spline),
    0x65FC11FF: ("orientation_behavior", _decode_orientation_behavior),
    0x6868D4B3: ("fov_spline", _decode_fov_spline),
    0x6E6D8EFD: ("roll_spline", _decode_roll_spline),
    0xF4F4798E: ("slowmo_control_spline", _decode_slowmo_control_spline),
    0x29515802: ("near_plane_distance_spline", _decode_near_plane_distance_spline),
    0xDF1865A6: ("far_plane_distance_spline", _decode_far_plane_distance_spline),
}
