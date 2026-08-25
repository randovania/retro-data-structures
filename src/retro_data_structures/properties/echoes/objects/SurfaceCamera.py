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
from retro_data_structures.properties.common.archetypes.SplineType import SplineType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SurfaceCameraJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flags_surface_camera: int
        surface_type: int
        spline: json_util.JsonObject
        player_offset: json_util.JsonValue
        spline_type: json_util.JsonObject
        unknown_0x431769c6: bool
        target_spline_type: json_util.JsonObject
        unknown_0x33b4f106: bool
        target_control_spline: json_util.JsonObject
        fov_spline: json_util.JsonObject


@dataclasses.dataclass()
class SurfaceCamera(BaseObjectType):
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
    flags_surface_camera: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1FFC65D8, original_name="FlagsSurfaceCamera"),
        },
    )
    surface_type: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1405B5E4, original_name="SurfaceType"),
        },
    )
    spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x922D151F, original_name="Spline", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    player_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x1D8B933F, original_name="PlayerOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    spline_type: SplineType = dataclasses.field(
        default_factory=SplineType,
        metadata={
            "reflection": FieldReflection[SplineType](
                SplineType,
                id=0x33E4685B,
                original_name="SplineType",
                from_json=SplineType.from_json,
                to_json=SplineType.to_json,
            ),
        },
    )
    unknown_0x431769c6: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x431769C6, original_name="Unknown"),
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
    unknown_0x33b4f106: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x33B4F106, original_name="Unknown"),
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

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SURC"

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
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1FFC65D8
        flags_surface_camera = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1405B5E4
        surface_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x922D151F
        spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D8B933F
        player_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33E4685B
        spline_type = SplineType.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x431769C6
        unknown_0x431769c6 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5604D304
        target_spline_type = SplineType.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33B4F106
        unknown_0x33b4f106 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4DFBFA7
        target_control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6868D4B3
        fov_spline = Spline.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            flags_surface_camera,
            surface_type,
            spline,
            player_offset,
            spline_type,
            unknown_0x431769c6,
            target_spline_type,
            unknown_0x33b4f106,
            target_control_spline,
            fov_spline,
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
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1f\xfce\xd8")  # 0x1ffc65d8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.flags_surface_camera))

        data.write(b"\x14\x05\xb5\xe4")  # 0x1405b5e4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.surface_type))

        data.write(b"\x92-\x15\x1f")  # 0x922d151f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1d\x8b\x93?")  # 0x1d8b933f
        data.write(b"\x00\x0c")  # size
        self.player_offset.to_stream(data, game)

        data.write(b"3\xe4h[")  # 0x33e4685b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"C\x17i\xc6")  # 0x431769c6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x431769c6))

        data.write(b"V\x04\xd3\x04")  # 0x5604d304
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.target_spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\xb4\xf1\x06")  # 0x33b4f106
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x33b4f106))

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

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SurfaceCameraJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            flags_surface_camera=json_data["flags_surface_camera"],
            surface_type=json_data["surface_type"],
            spline=Spline.from_json(json_data["spline"]),
            player_offset=Vector.from_json(json_data["player_offset"]),
            spline_type=SplineType.from_json(json_data["spline_type"]),
            unknown_0x431769c6=json_data["unknown_0x431769c6"],
            target_spline_type=SplineType.from_json(json_data["target_spline_type"]),
            unknown_0x33b4f106=json_data["unknown_0x33b4f106"],
            target_control_spline=Spline.from_json(json_data["target_control_spline"]),
            fov_spline=Spline.from_json(json_data["fov_spline"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "flags_surface_camera": self.flags_surface_camera,
            "surface_type": self.surface_type,
            "spline": self.spline.to_json(),
            "player_offset": self.player_offset.to_json(),
            "spline_type": self.spline_type.to_json(),
            "unknown_0x431769c6": self.unknown_0x431769c6,
            "target_spline_type": self.target_spline_type.to_json(),
            "unknown_0x33b4f106": self.unknown_0x33b4f106,
            "target_control_spline": self.target_control_spline.to_json(),
            "fov_spline": self.fov_spline.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_player_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_target_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_target_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fov_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x1FFC65D8: ("flags_surface_camera", structs.decode_BIG_l),
    0x1405B5E4: ("surface_type", structs.decode_BIG_l),
    0x922D151F: ("spline", _decode_spline),
    0x1D8B933F: ("player_offset", _decode_player_offset),
    0x33E4685B: ("spline_type", _decode_spline_type),
    0x431769C6: ("unknown_0x431769c6", structs.decode_BIG_bool_),
    0x5604D304: ("target_spline_type", _decode_target_spline_type),
    0x33B4F106: ("unknown_0x33b4f106", structs.decode_BIG_bool_),
    0xC4DFBFA7: ("target_control_spline", _decode_target_control_spline),
    0x6868D4B3: ("fov_spline", _decode_fov_spline),
}
