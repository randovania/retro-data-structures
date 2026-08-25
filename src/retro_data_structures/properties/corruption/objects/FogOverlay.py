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
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FogOverlayJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        full_alpha: float
        fade_down_time: float
        fade_up_time: float
        start_faded_out: bool
        color: json_util.JsonValue
        ambient_radius_x: float
        ambient_radius_y: float
        ambient_speed: float
        ambient_speed_target: float
        unknown_0x6a111b96: float
        unknown_0xff226ea3: float
        unknown_0x2190ab0a: json_util.JsonValue
        unknown_0x9f19f0af: float
        unknown_0x90c10fe7: float
        unknown_0xd8daff1d: float


@dataclasses.dataclass()
class FogOverlay(BaseObjectType):
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
    full_alpha: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x547B28D5, original_name="FullAlpha"),
        },
    )
    fade_down_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF977CB35, original_name="FadeDownTime"),
        },
    )
    fade_up_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D21D348, original_name="FadeUpTime"),
        },
    )
    start_faded_out: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEB250A0B, original_name="StartFadedOut"),
        },
    )
    color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x37C7D09D, original_name="Color", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    ambient_radius_x: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B9046D6, original_name="AmbientRadiusX"),
        },
    )
    ambient_radius_y: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD0CC9573, original_name="AmbientRadiusY"),
        },
    )
    ambient_speed: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF76BCBDD, original_name="AmbientSpeed"),
        },
    )
    ambient_speed_target: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C4C6785, original_name="AmbientSpeedTarget"),
        },
    )
    unknown_0x6a111b96: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6A111B96, original_name="Unknown"),
        },
    )
    unknown_0xff226ea3: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFF226EA3, original_name="Unknown"),
        },
    )
    unknown_0x2190ab0a: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x2190AB0A, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0x9f19f0af: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F19F0AF, original_name="Unknown"),
        },
    )
    unknown_0x90c10fe7: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90C10FE7, original_name="Unknown"),
        },
    )
    unknown_0xd8daff1d: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD8DAFF1D, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "FOGO"

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
        if property_count != 16:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x547B28D5
        full_alpha = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF977CB35
        fade_down_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D21D348
        fade_up_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB250A0B
        start_faded_out = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37C7D09D
        color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B9046D6
        ambient_radius_x = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD0CC9573
        ambient_radius_y = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF76BCBDD
        ambient_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C4C6785
        ambient_speed_target = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A111B96
        unknown_0x6a111b96 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF226EA3
        unknown_0xff226ea3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2190AB0A
        unknown_0x2190ab0a = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F19F0AF
        unknown_0x9f19f0af = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90C10FE7
        unknown_0x90c10fe7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8DAFF1D
        unknown_0xd8daff1d = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            full_alpha,
            fade_down_time,
            fade_up_time,
            start_faded_out,
            color,
            ambient_radius_x,
            ambient_radius_y,
            ambient_speed,
            ambient_speed_target,
            unknown_0x6a111b96,
            unknown_0xff226ea3,
            unknown_0x2190ab0a,
            unknown_0x9f19f0af,
            unknown_0x90c10fe7,
            unknown_0xd8daff1d,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x10")  # 16 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"T{(\xd5")  # 0x547b28d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.full_alpha))

        data.write(b"\xf9w\xcb5")  # 0xf977cb35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_down_time))

        data.write(b"\r!\xd3H")  # 0xd21d348
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_up_time))

        data.write(b"\xeb%\n\x0b")  # 0xeb250a0b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.start_faded_out))

        data.write(b"7\xc7\xd0\x9d")  # 0x37c7d09d
        data.write(b"\x00\x10")  # size
        self.color.to_stream(data, game)

        data.write(b"\x1b\x90F\xd6")  # 0x1b9046d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ambient_radius_x))

        data.write(b"\xd0\xcc\x95s")  # 0xd0cc9573
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ambient_radius_y))

        data.write(b"\xf7k\xcb\xdd")  # 0xf76bcbdd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ambient_speed))

        data.write(b",Lg\x85")  # 0x2c4c6785
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ambient_speed_target))

        data.write(b"j\x11\x1b\x96")  # 0x6a111b96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6a111b96))

        data.write(b'\xff"n\xa3')  # 0xff226ea3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xff226ea3))

        data.write(b"!\x90\xab\n")  # 0x2190ab0a
        data.write(b"\x00\x0c")  # size
        self.unknown_0x2190ab0a.to_stream(data, game)

        data.write(b"\x9f\x19\xf0\xaf")  # 0x9f19f0af
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9f19f0af))

        data.write(b"\x90\xc1\x0f\xe7")  # 0x90c10fe7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x90c10fe7))

        data.write(b"\xd8\xda\xff\x1d")  # 0xd8daff1d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd8daff1d))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FogOverlayJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            full_alpha=json_data["full_alpha"],
            fade_down_time=json_data["fade_down_time"],
            fade_up_time=json_data["fade_up_time"],
            start_faded_out=json_data["start_faded_out"],
            color=Color.from_json(json_data["color"]),
            ambient_radius_x=json_data["ambient_radius_x"],
            ambient_radius_y=json_data["ambient_radius_y"],
            ambient_speed=json_data["ambient_speed"],
            ambient_speed_target=json_data["ambient_speed_target"],
            unknown_0x6a111b96=json_data["unknown_0x6a111b96"],
            unknown_0xff226ea3=json_data["unknown_0xff226ea3"],
            unknown_0x2190ab0a=Vector.from_json(json_data["unknown_0x2190ab0a"]),
            unknown_0x9f19f0af=json_data["unknown_0x9f19f0af"],
            unknown_0x90c10fe7=json_data["unknown_0x90c10fe7"],
            unknown_0xd8daff1d=json_data["unknown_0xd8daff1d"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "full_alpha": self.full_alpha,
            "fade_down_time": self.fade_down_time,
            "fade_up_time": self.fade_up_time,
            "start_faded_out": self.start_faded_out,
            "color": self.color.to_json(),
            "ambient_radius_x": self.ambient_radius_x,
            "ambient_radius_y": self.ambient_radius_y,
            "ambient_speed": self.ambient_speed,
            "ambient_speed_target": self.ambient_speed_target,
            "unknown_0x6a111b96": self.unknown_0x6a111b96,
            "unknown_0xff226ea3": self.unknown_0xff226ea3,
            "unknown_0x2190ab0a": self.unknown_0x2190ab0a.to_json(),
            "unknown_0x9f19f0af": self.unknown_0x9f19f0af,
            "unknown_0x90c10fe7": self.unknown_0x90c10fe7,
            "unknown_0xd8daff1d": self.unknown_0xd8daff1d,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x2190ab0a(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x547B28D5: ("full_alpha", structs.decode_BIG_f),
    0xF977CB35: ("fade_down_time", structs.decode_BIG_f),
    0x0D21D348: ("fade_up_time", structs.decode_BIG_f),
    0xEB250A0B: ("start_faded_out", structs.decode_BIG_bool_),
    0x37C7D09D: ("color", _decode_color),
    0x1B9046D6: ("ambient_radius_x", structs.decode_BIG_f),
    0xD0CC9573: ("ambient_radius_y", structs.decode_BIG_f),
    0xF76BCBDD: ("ambient_speed", structs.decode_BIG_f),
    0x2C4C6785: ("ambient_speed_target", structs.decode_BIG_f),
    0x6A111B96: ("unknown_0x6a111b96", structs.decode_BIG_f),
    0xFF226EA3: ("unknown_0xff226ea3", structs.decode_BIG_f),
    0x2190AB0A: ("unknown_0x2190ab0a", _decode_unknown_0x2190ab0a),
    0x9F19F0AF: ("unknown_0x9f19f0af", structs.decode_BIG_f),
    0x90C10FE7: ("unknown_0x90c10fe7", structs.decode_BIG_f),
    0xD8DAFF1D: ("unknown_0xd8daff1d", structs.decode_BIG_f),
}
