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
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraPitchJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        forwards_pitch: json_util.JsonObject
        backwards_pitch: json_util.JsonObject
        use_player_radius: bool
        max_radius: float
        ease_in: json_util.JsonObject
        ease_out: json_util.JsonObject


@dataclasses.dataclass()
class CameraPitch(BaseObjectType):
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
    forwards_pitch: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x81D093B3, original_name="ForwardsPitch", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    backwards_pitch: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xAD9F8E3E,
                original_name="BackwardsPitch",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    use_player_radius: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3922D9DC, original_name="UsePlayerRadius"),
        },
    )
    max_radius: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC599BCBB, original_name="MaxRadius"),
        },
    )
    ease_in: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xDF5550CC, original_name="EaseIn", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    ease_out: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xCA581334, original_name="EaseOut", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CAMP"

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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81D093B3
        forwards_pitch = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD9F8E3E
        backwards_pitch = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3922D9DC
        use_player_radius = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC599BCBB
        max_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF5550CC
        ease_in = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCA581334
        ease_out = Spline.from_stream(data, game, property_size)

        return cls(editor_properties, forwards_pitch, backwards_pitch, use_player_radius, max_radius, ease_in, ease_out)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x81\xd0\x93\xb3")  # 0x81d093b3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.forwards_pitch.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xad\x9f\x8e>")  # 0xad9f8e3e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.backwards_pitch.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'9"\xd9\xdc')  # 0x3922d9dc
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_player_radius))

        data.write(b"\xc5\x99\xbc\xbb")  # 0xc599bcbb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_radius))

        data.write(b"\xdfUP\xcc")  # 0xdf5550cc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ease_in.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcaX\x134")  # 0xca581334
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ease_out.to_stream(data, game)
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
        json_data = typing.cast("CameraPitchJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            forwards_pitch=Spline.from_json(json_data["forwards_pitch"]),
            backwards_pitch=Spline.from_json(json_data["backwards_pitch"]),
            use_player_radius=json_data["use_player_radius"],
            max_radius=json_data["max_radius"],
            ease_in=Spline.from_json(json_data["ease_in"]),
            ease_out=Spline.from_json(json_data["ease_out"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "forwards_pitch": self.forwards_pitch.to_json(),
            "backwards_pitch": self.backwards_pitch.to_json(),
            "use_player_radius": self.use_player_radius,
            "max_radius": self.max_radius,
            "ease_in": self.ease_in.to_json(),
            "ease_out": self.ease_out.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_forwards_pitch(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_backwards_pitch(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_ease_in(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_ease_out(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x81D093B3: ("forwards_pitch", _decode_forwards_pitch),
    0xAD9F8E3E: ("backwards_pitch", _decode_backwards_pitch),
    0x3922D9DC: ("use_player_radius", structs.decode_BIG_bool_),
    0xC599BCBB: ("max_radius", structs.decode_BIG_f),
    0xDF5550CC: ("ease_in", _decode_ease_in),
    0xCA581334: ("ease_out", _decode_ease_out),
}
