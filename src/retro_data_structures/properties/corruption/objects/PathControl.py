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
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PathControlJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        path_flags: int
        path_curve_type: int
        radius_control: json_util.JsonObject
        height_control: json_util.JsonObject


class PathCurveType(enum.IntEnum):
    Unknown1 = 4117718896
    Unknown2 = 2494257178

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
class PathControl(BaseObjectType):
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
    path_flags: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB0B97F9F, original_name="PathFlags"),
        },
    )  # Flagset
    path_curve_type: PathCurveType = dataclasses.field(
        default=PathCurveType.Unknown1,
        metadata={
            "reflection": FieldReflection[PathCurveType](
                PathCurveType,
                id=0xF25FFDFF,
                original_name="PathCurveType",
                from_json=PathCurveType.from_json,
                to_json=PathCurveType.to_json,
            ),
        },
    )
    radius_control: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xF8AF858C, original_name="RadiusControl", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    height_control: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x72CD60CE, original_name="HeightControl", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PCTL"

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
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB0B97F9F
        path_flags = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF25FFDFF
        path_curve_type = PathCurveType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8AF858C
        radius_control = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72CD60CE
        height_control = Spline.from_stream(data, game, property_size)

        return cls(editor_properties, path_flags, path_curve_type, radius_control, height_control)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb0\xb9\x7f\x9f")  # 0xb0b97f9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.path_flags))

        data.write(b"\xf2_\xfd\xff")  # 0xf25ffdff
        data.write(b"\x00\x04")  # size
        self.path_curve_type.to_stream(data, game)

        data.write(b"\xf8\xaf\x85\x8c")  # 0xf8af858c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.radius_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"r\xcd`\xce")  # 0x72cd60ce
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.height_control.to_stream(data, game)
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
        json_data = typing.cast("PathControlJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            path_flags=json_data["path_flags"],
            path_curve_type=PathCurveType.from_json(json_data["path_curve_type"]),
            radius_control=Spline.from_json(json_data["radius_control"]),
            height_control=Spline.from_json(json_data["height_control"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "path_flags": self.path_flags,
            "path_curve_type": self.path_curve_type.to_json(),
            "radius_control": self.radius_control.to_json(),
            "height_control": self.height_control.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_path_curve_type(data: typing.BinaryIO, game: Game, property_size: int) -> PathCurveType:
    return PathCurveType.from_stream(data, game)


def _decode_radius_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_height_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB0B97F9F: ("path_flags", structs.decode_BIG_L),
    0xF25FFDFF: ("path_curve_type", _decode_path_curve_type),
    0xF8AF858C: ("radius_control", _decode_radius_control),
    0x72CD60CE: ("height_control", _decode_height_control),
}
