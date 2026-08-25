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
from retro_data_structures.properties.common.archetypes.DynamicLightFalloff import DynamicLightFalloff
from retro_data_structures.properties.common.archetypes.DynamicLightIntensity import DynamicLightIntensity
from retro_data_structures.properties.common.archetypes.DynamicLightMotionSpline import DynamicLightMotionSpline
from retro_data_structures.properties.common.archetypes.DynamicLightParent import DynamicLightParent
from retro_data_structures.properties.common.archetypes.DynamicLightSpotlight import DynamicLightSpotlight
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class DynamicLightJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        light_type: int
        unknown_0xe42bab04: bool
        unknown_0x364a7b36: bool
        unknown_0x4ea02861: bool
        unknown_0xa502605d: bool
        unknown_0xa19817f0: bool
        color: json_util.JsonValue
        intensity: json_util.JsonObject
        falloff: json_util.JsonObject
        spotlight: json_util.JsonObject
        motion_spline: json_util.JsonObject
        parent: json_util.JsonObject


@dataclasses.dataclass()
class DynamicLight(BaseObjectType):
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
    light_type: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7FC4E336, original_name="LightType"),
        },
    )
    unknown_0xe42bab04: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE42BAB04, original_name="Unknown"),
        },
    )
    unknown_0x364a7b36: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x364A7B36, original_name="Unknown"),
        },
    )
    unknown_0x4ea02861: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4EA02861, original_name="Unknown"),
        },
    )
    unknown_0xa502605d: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA502605D, original_name="Unknown"),
        },
    )
    unknown_0xa19817f0: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA19817F0, original_name="Unknown"),
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
    intensity: DynamicLightIntensity = dataclasses.field(
        default_factory=DynamicLightIntensity,
        metadata={
            "reflection": FieldReflection[DynamicLightIntensity](
                DynamicLightIntensity,
                id=0x72531EDE,
                original_name="Intensity",
                from_json=DynamicLightIntensity.from_json,
                to_json=DynamicLightIntensity.to_json,
            ),
        },
    )
    falloff: DynamicLightFalloff = dataclasses.field(
        default_factory=DynamicLightFalloff,
        metadata={
            "reflection": FieldReflection[DynamicLightFalloff](
                DynamicLightFalloff,
                id=0x219B52DA,
                original_name="Falloff",
                from_json=DynamicLightFalloff.from_json,
                to_json=DynamicLightFalloff.to_json,
            ),
        },
    )
    spotlight: DynamicLightSpotlight = dataclasses.field(
        default_factory=DynamicLightSpotlight,
        metadata={
            "reflection": FieldReflection[DynamicLightSpotlight](
                DynamicLightSpotlight,
                id=0x9546F449,
                original_name="Spotlight",
                from_json=DynamicLightSpotlight.from_json,
                to_json=DynamicLightSpotlight.to_json,
            ),
        },
    )
    motion_spline: DynamicLightMotionSpline = dataclasses.field(
        default_factory=DynamicLightMotionSpline,
        metadata={
            "reflection": FieldReflection[DynamicLightMotionSpline](
                DynamicLightMotionSpline,
                id=0x14322138,
                original_name="MotionSpline",
                from_json=DynamicLightMotionSpline.from_json,
                to_json=DynamicLightMotionSpline.to_json,
            ),
        },
    )
    parent: DynamicLightParent = dataclasses.field(
        default_factory=DynamicLightParent,
        metadata={
            "reflection": FieldReflection[DynamicLightParent](
                DynamicLightParent,
                id=0xF734DF8C,
                original_name="Parent",
                from_json=DynamicLightParent.from_json,
                to_json=DynamicLightParent.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DLHT"

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
        assert property_id == 0x7FC4E336
        light_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE42BAB04
        unknown_0xe42bab04 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x364A7B36
        unknown_0x364a7b36 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4EA02861
        unknown_0x4ea02861 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA502605D
        unknown_0xa502605d = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA19817F0
        unknown_0xa19817f0 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37C7D09D
        color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72531EDE
        intensity = DynamicLightIntensity.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x219B52DA
        falloff = DynamicLightFalloff.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9546F449
        spotlight = DynamicLightSpotlight.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14322138
        motion_spline = DynamicLightMotionSpline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF734DF8C
        parent = DynamicLightParent.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            light_type,
            unknown_0xe42bab04,
            unknown_0x364a7b36,
            unknown_0x4ea02861,
            unknown_0xa502605d,
            unknown_0xa19817f0,
            color,
            intensity,
            falloff,
            spotlight,
            motion_spline,
            parent,
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

        data.write(b"\x7f\xc4\xe36")  # 0x7fc4e336
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_type))

        data.write(b"\xe4+\xab\x04")  # 0xe42bab04
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xe42bab04))

        data.write(b"6J{6")  # 0x364a7b36
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x364a7b36))

        data.write(b"N\xa0(a")  # 0x4ea02861
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4ea02861))

        data.write(b"\xa5\x02`]")  # 0xa502605d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa502605d))

        data.write(b"\xa1\x98\x17\xf0")  # 0xa19817f0
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa19817f0))

        data.write(b"7\xc7\xd0\x9d")  # 0x37c7d09d
        data.write(b"\x00\x10")  # size
        self.color.to_stream(data, game)

        data.write(b"rS\x1e\xde")  # 0x72531ede
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.intensity.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"!\x9bR\xda")  # 0x219b52da
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.falloff.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95F\xf4I")  # 0x9546f449
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spotlight.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x142!8")  # 0x14322138
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf74\xdf\x8c")  # 0xf734df8c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.parent.to_stream(data, game)
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
        json_data = typing.cast("DynamicLightJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            light_type=json_data["light_type"],
            unknown_0xe42bab04=json_data["unknown_0xe42bab04"],
            unknown_0x364a7b36=json_data["unknown_0x364a7b36"],
            unknown_0x4ea02861=json_data["unknown_0x4ea02861"],
            unknown_0xa502605d=json_data["unknown_0xa502605d"],
            unknown_0xa19817f0=json_data["unknown_0xa19817f0"],
            color=Color.from_json(json_data["color"]),
            intensity=DynamicLightIntensity.from_json(json_data["intensity"]),
            falloff=DynamicLightFalloff.from_json(json_data["falloff"]),
            spotlight=DynamicLightSpotlight.from_json(json_data["spotlight"]),
            motion_spline=DynamicLightMotionSpline.from_json(json_data["motion_spline"]),
            parent=DynamicLightParent.from_json(json_data["parent"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "light_type": self.light_type,
            "unknown_0xe42bab04": self.unknown_0xe42bab04,
            "unknown_0x364a7b36": self.unknown_0x364a7b36,
            "unknown_0x4ea02861": self.unknown_0x4ea02861,
            "unknown_0xa502605d": self.unknown_0xa502605d,
            "unknown_0xa19817f0": self.unknown_0xa19817f0,
            "color": self.color.to_json(),
            "intensity": self.intensity.to_json(),
            "falloff": self.falloff.to_json(),
            "spotlight": self.spotlight.to_json(),
            "motion_spline": self.motion_spline.to_json(),
            "parent": self.parent.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_intensity(data: typing.BinaryIO, game: Game, property_size: int) -> DynamicLightIntensity:
    return DynamicLightIntensity.from_stream(data, game, property_size)


def _decode_falloff(data: typing.BinaryIO, game: Game, property_size: int) -> DynamicLightFalloff:
    return DynamicLightFalloff.from_stream(data, game, property_size)


def _decode_spotlight(data: typing.BinaryIO, game: Game, property_size: int) -> DynamicLightSpotlight:
    return DynamicLightSpotlight.from_stream(data, game, property_size)


def _decode_motion_spline(data: typing.BinaryIO, game: Game, property_size: int) -> DynamicLightMotionSpline:
    return DynamicLightMotionSpline.from_stream(data, game, property_size)


def _decode_parent(data: typing.BinaryIO, game: Game, property_size: int) -> DynamicLightParent:
    return DynamicLightParent.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7FC4E336: ("light_type", structs.decode_BIG_l),
    0xE42BAB04: ("unknown_0xe42bab04", structs.decode_BIG_bool_),
    0x364A7B36: ("unknown_0x364a7b36", structs.decode_BIG_bool_),
    0x4EA02861: ("unknown_0x4ea02861", structs.decode_BIG_bool_),
    0xA502605D: ("unknown_0xa502605d", structs.decode_BIG_bool_),
    0xA19817F0: ("unknown_0xa19817f0", structs.decode_BIG_bool_),
    0x37C7D09D: ("color", _decode_color),
    0x72531EDE: ("intensity", _decode_intensity),
    0x219B52DA: ("falloff", _decode_falloff),
    0x9546F449: ("spotlight", _decode_spotlight),
    0x14322138: ("motion_spline", _decode_motion_spline),
    0xF734DF8C: ("parent", _decode_parent),
}
