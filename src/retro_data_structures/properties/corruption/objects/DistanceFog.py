# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.Vector2f import Vector2f
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class DistanceFogJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_0x88e8d530: int
        mode: int
        color: json_util.JsonValue
        near_far_plane: json_util.JsonObject
        color_rate: float
        distance_rate: json_util.JsonObject
        force_settings: bool
        is_two_sided: bool
        unknown_0xb7246843: json_util.JsonValue
        vector2f_0x520d1dd5: json_util.JsonObject
        unknown_0xbc86052a: float
        vector2f_0xfba31a97: json_util.JsonObject


@dataclasses.dataclass()
class DistanceFog(BaseObjectType):
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
    unknown_0x88e8d530: int = dataclasses.field(
        default=3630416747,
        metadata={
            "reflection": FieldReflection[int](int, id=0x88E8D530, original_name="Unknown"),
        },
    )  # Choice
    mode: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x09AD63DE, original_name="Mode"),
        },
    )
    color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x37C7D09D, original_name="Color", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    near_far_plane: Vector2f = dataclasses.field(
        default_factory=Vector2f,
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0x652008DA,
                original_name="NearFarPlane",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
            ),
        },
    )
    color_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x29AB4727, original_name="ColorRate"),
        },
    )
    distance_rate: Vector2f = dataclasses.field(
        default_factory=Vector2f,
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0xCC8E0F98,
                original_name="DistanceRate",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
            ),
        },
    )
    force_settings: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC5935B67, original_name="ForceSettings"),
        },
    )
    is_two_sided: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB5D1EF02, original_name="IsTwoSided"),
        },
    )
    unknown_0xb7246843: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xB7246843, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    vector2f_0x520d1dd5: Vector2f = dataclasses.field(
        default_factory=Vector2f,
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0x520D1DD5,
                original_name="Vector2f",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
            ),
        },
    )
    unknown_0xbc86052a: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC86052A, original_name="Unknown"),
        },
    )
    vector2f_0xfba31a97: Vector2f = dataclasses.field(
        default_factory=Vector2f,
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0xFBA31A97,
                original_name="Vector2f",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DFOG"

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
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={"active": False})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88E8D530
        unknown_0x88e8d530 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09AD63DE
        mode = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37C7D09D
        color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x652008DA
        near_far_plane = Vector2f.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29AB4727
        color_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC8E0F98
        distance_rate = Vector2f.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5935B67
        force_settings = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5D1EF02
        is_two_sided = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7246843
        unknown_0xb7246843 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x520D1DD5
        vector2f_0x520d1dd5 = Vector2f.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC86052A
        unknown_0xbc86052a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBA31A97
        vector2f_0xfba31a97 = Vector2f.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            unknown_0x88e8d530,
            mode,
            color,
            near_far_plane,
            color_rate,
            distance_rate,
            force_settings,
            is_two_sided,
            unknown_0xb7246843,
            vector2f_0x520d1dd5,
            unknown_0xbc86052a,
            vector2f_0xfba31a97,
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
        self.editor_properties.to_stream(data, game, default_override={"active": False})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x88\xe8\xd50")  # 0x88e8d530
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x88e8d530))

        data.write(b"\t\xadc\xde")  # 0x9ad63de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.mode))

        data.write(b"7\xc7\xd0\x9d")  # 0x37c7d09d
        data.write(b"\x00\x10")  # size
        self.color.to_stream(data, game)

        data.write(b"e \x08\xda")  # 0x652008da
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.near_far_plane.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b")\xabG'")  # 0x29ab4727
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.color_rate))

        data.write(b"\xcc\x8e\x0f\x98")  # 0xcc8e0f98
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.distance_rate.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc5\x93[g")  # 0xc5935b67
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.force_settings))

        data.write(b"\xb5\xd1\xef\x02")  # 0xb5d1ef02
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_two_sided))

        data.write(b"\xb7$hC")  # 0xb7246843
        data.write(b"\x00\x10")  # size
        self.unknown_0xb7246843.to_stream(data, game)

        data.write(b"R\r\x1d\xd5")  # 0x520d1dd5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vector2f_0x520d1dd5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbc\x86\x05*")  # 0xbc86052a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbc86052a))

        data.write(b"\xfb\xa3\x1a\x97")  # 0xfba31a97
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vector2f_0xfba31a97.to_stream(data, game)
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
        json_data = typing.cast("DistanceFogJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            unknown_0x88e8d530=json_data["unknown_0x88e8d530"],
            mode=json_data["mode"],
            color=Color.from_json(json_data["color"]),
            near_far_plane=Vector2f.from_json(json_data["near_far_plane"]),
            color_rate=json_data["color_rate"],
            distance_rate=Vector2f.from_json(json_data["distance_rate"]),
            force_settings=json_data["force_settings"],
            is_two_sided=json_data["is_two_sided"],
            unknown_0xb7246843=Color.from_json(json_data["unknown_0xb7246843"]),
            vector2f_0x520d1dd5=Vector2f.from_json(json_data["vector2f_0x520d1dd5"]),
            unknown_0xbc86052a=json_data["unknown_0xbc86052a"],
            vector2f_0xfba31a97=Vector2f.from_json(json_data["vector2f_0xfba31a97"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "unknown_0x88e8d530": self.unknown_0x88e8d530,
            "mode": self.mode,
            "color": self.color.to_json(),
            "near_far_plane": self.near_far_plane.to_json(),
            "color_rate": self.color_rate,
            "distance_rate": self.distance_rate.to_json(),
            "force_settings": self.force_settings,
            "is_two_sided": self.is_two_sided,
            "unknown_0xb7246843": self.unknown_0xb7246843.to_json(),
            "vector2f_0x520d1dd5": self.vector2f_0x520d1dd5.to_json(),
            "unknown_0xbc86052a": self.unknown_0xbc86052a,
            "vector2f_0xfba31a97": self.vector2f_0xfba31a97.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={"active": False})


def _decode_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_near_far_plane(data: typing.BinaryIO, game: Game, property_size: int) -> Vector2f:
    return Vector2f.from_stream(data, game, property_size)


def _decode_distance_rate(data: typing.BinaryIO, game: Game, property_size: int) -> Vector2f:
    return Vector2f.from_stream(data, game, property_size)


def _decode_unknown_0xb7246843(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_vector2f_0x520d1dd5(data: typing.BinaryIO, game: Game, property_size: int) -> Vector2f:
    return Vector2f.from_stream(data, game, property_size)


def _decode_vector2f_0xfba31a97(data: typing.BinaryIO, game: Game, property_size: int) -> Vector2f:
    return Vector2f.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x88E8D530: ("unknown_0x88e8d530", structs.decode_BIG_L),
    0x09AD63DE: ("mode", structs.decode_BIG_l),
    0x37C7D09D: ("color", _decode_color),
    0x652008DA: ("near_far_plane", _decode_near_far_plane),
    0x29AB4727: ("color_rate", structs.decode_BIG_f),
    0xCC8E0F98: ("distance_rate", _decode_distance_rate),
    0xC5935B67: ("force_settings", structs.decode_BIG_bool_),
    0xB5D1EF02: ("is_two_sided", structs.decode_BIG_bool_),
    0xB7246843: ("unknown_0xb7246843", _decode_unknown_0xb7246843),
    0x520D1DD5: ("vector2f_0x520d1dd5", _decode_vector2f_0x520d1dd5),
    0xBC86052A: ("unknown_0xbc86052a", structs.decode_BIG_f),
    0xFBA31A97: ("vector2f_0xfba31a97", _decode_vector2f_0xfba31a97),
}
