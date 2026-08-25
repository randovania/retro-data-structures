# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakGui_ScanVisorJson(typing_extensions.TypedDict):
        unknown_0x5d750eef: json_util.JsonValue
        inactive_color: json_util.JsonValue
        inactive_external_color: json_util.JsonValue
        non_critical_color: json_util.JsonValue
        critical_color: json_util.JsonValue
        burn_in_color: json_util.JsonValue
        highlight_color: json_util.JsonValue
        unknown_0x84badf82: json_util.JsonValue
        critical_highlight_color: json_util.JsonValue
        unknown_0xe8f5018b: json_util.JsonValue
        unknown_0xba1ae1e5: json_util.JsonValue
        unknown_0xb39d450e: json_util.JsonValue
        unknown_0x1042455b: json_util.JsonValue
        unknown_0xd72435ad: json_util.JsonValue
        unknown_0x75cdc913: json_util.JsonValue
        sweep_bar_color: json_util.JsonValue
        burn_in_time: float
        fade_out_time: float
        unknown_0xee169779: float
        unknown_0x58bc9d5d: float
        unknown_0xf4f19c8b: json_util.JsonObject
        unknown_0x5286973f: json_util.JsonObject
        unknown_0x636e8da2: json_util.JsonObject
        unknown_0xc5198616: json_util.JsonObject
        unknown_0x00beb898: json_util.JsonObject
        unknown_0xa6c9b32c: json_util.JsonObject


@dataclasses.dataclass()
class TweakGui_ScanVisor(BaseProperty):
    unknown_0x5d750eef: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5D750EEF, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    inactive_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x972271B9, original_name="InactiveColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    inactive_external_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xA908C775,
                original_name="InactiveExternalColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    non_critical_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xEE1F1DF6, original_name="NonCriticalColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    critical_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x43445AE7, original_name="CriticalColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    burn_in_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF48FD559, original_name="BurnInColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    highlight_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x7A6412F6, original_name="HighlightColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x84badf82: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x84BADF82, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    critical_highlight_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xF45F7D17,
                original_name="CriticalHighlightColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xe8f5018b: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE8F5018B, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xba1ae1e5: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xBA1AE1E5, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xb39d450e: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xB39D450E, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x1042455b: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1042455B, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xd72435ad: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD72435AD, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x75cdc913: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x75CDC913, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    sweep_bar_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x997EC38D, original_name="SweepBarColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    burn_in_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00B83F02, original_name="BurnInTime"),
        },
    )
    fade_out_time: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7C269EBC, original_name="FadeOutTime"),
        },
    )
    unknown_0xee169779: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEE169779, original_name="Unknown"),
        },
    )
    unknown_0x58bc9d5d: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x58BC9D5D, original_name="Unknown"),
        },
    )
    unknown_0xf4f19c8b: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xF4F19C8B, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x5286973f: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x5286973F, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x636e8da2: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x636E8DA2, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xc5198616: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xC5198616, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x00beb898: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x00BEB898, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xa6c9b32c: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xA6C9B32C, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 26:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D750EEF
        unknown_0x5d750eef = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x972271B9
        inactive_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA908C775
        inactive_external_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEE1F1DF6
        non_critical_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43445AE7
        critical_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF48FD559
        burn_in_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A6412F6
        highlight_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84BADF82
        unknown_0x84badf82 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF45F7D17
        critical_highlight_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8F5018B
        unknown_0xe8f5018b = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA1AE1E5
        unknown_0xba1ae1e5 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB39D450E
        unknown_0xb39d450e = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1042455B
        unknown_0x1042455b = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD72435AD
        unknown_0xd72435ad = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75CDC913
        unknown_0x75cdc913 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x997EC38D
        sweep_bar_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00B83F02
        burn_in_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C269EBC
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEE169779
        unknown_0xee169779 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58BC9D5D
        unknown_0x58bc9d5d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4F19C8B
        unknown_0xf4f19c8b = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5286973F
        unknown_0x5286973f = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x636E8DA2
        unknown_0x636e8da2 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5198616
        unknown_0xc5198616 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00BEB898
        unknown_0x00beb898 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6C9B32C
        unknown_0xa6c9b32c = Spline.from_stream(data, game, property_size)

        return cls(
            unknown_0x5d750eef,
            inactive_color,
            inactive_external_color,
            non_critical_color,
            critical_color,
            burn_in_color,
            highlight_color,
            unknown_0x84badf82,
            critical_highlight_color,
            unknown_0xe8f5018b,
            unknown_0xba1ae1e5,
            unknown_0xb39d450e,
            unknown_0x1042455b,
            unknown_0xd72435ad,
            unknown_0x75cdc913,
            sweep_bar_color,
            burn_in_time,
            fade_out_time,
            unknown_0xee169779,
            unknown_0x58bc9d5d,
            unknown_0xf4f19c8b,
            unknown_0x5286973f,
            unknown_0x636e8da2,
            unknown_0xc5198616,
            unknown_0x00beb898,
            unknown_0xa6c9b32c,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1a")  # 26 properties

        data.write(b"]u\x0e\xef")  # 0x5d750eef
        data.write(b"\x00\x10")  # size
        self.unknown_0x5d750eef.to_stream(data, game)

        data.write(b'\x97"q\xb9')  # 0x972271b9
        data.write(b"\x00\x10")  # size
        self.inactive_color.to_stream(data, game)

        data.write(b"\xa9\x08\xc7u")  # 0xa908c775
        data.write(b"\x00\x10")  # size
        self.inactive_external_color.to_stream(data, game)

        data.write(b"\xee\x1f\x1d\xf6")  # 0xee1f1df6
        data.write(b"\x00\x10")  # size
        self.non_critical_color.to_stream(data, game)

        data.write(b"CDZ\xe7")  # 0x43445ae7
        data.write(b"\x00\x10")  # size
        self.critical_color.to_stream(data, game)

        data.write(b"\xf4\x8f\xd5Y")  # 0xf48fd559
        data.write(b"\x00\x10")  # size
        self.burn_in_color.to_stream(data, game)

        data.write(b"zd\x12\xf6")  # 0x7a6412f6
        data.write(b"\x00\x10")  # size
        self.highlight_color.to_stream(data, game)

        data.write(b"\x84\xba\xdf\x82")  # 0x84badf82
        data.write(b"\x00\x10")  # size
        self.unknown_0x84badf82.to_stream(data, game)

        data.write(b"\xf4_}\x17")  # 0xf45f7d17
        data.write(b"\x00\x10")  # size
        self.critical_highlight_color.to_stream(data, game)

        data.write(b"\xe8\xf5\x01\x8b")  # 0xe8f5018b
        data.write(b"\x00\x10")  # size
        self.unknown_0xe8f5018b.to_stream(data, game)

        data.write(b"\xba\x1a\xe1\xe5")  # 0xba1ae1e5
        data.write(b"\x00\x10")  # size
        self.unknown_0xba1ae1e5.to_stream(data, game)

        data.write(b"\xb3\x9dE\x0e")  # 0xb39d450e
        data.write(b"\x00\x10")  # size
        self.unknown_0xb39d450e.to_stream(data, game)

        data.write(b"\x10BE[")  # 0x1042455b
        data.write(b"\x00\x10")  # size
        self.unknown_0x1042455b.to_stream(data, game)

        data.write(b"\xd7$5\xad")  # 0xd72435ad
        data.write(b"\x00\x10")  # size
        self.unknown_0xd72435ad.to_stream(data, game)

        data.write(b"u\xcd\xc9\x13")  # 0x75cdc913
        data.write(b"\x00\x10")  # size
        self.unknown_0x75cdc913.to_stream(data, game)

        data.write(b"\x99~\xc3\x8d")  # 0x997ec38d
        data.write(b"\x00\x10")  # size
        self.sweep_bar_color.to_stream(data, game)

        data.write(b"\x00\xb8?\x02")  # 0xb83f02
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.burn_in_time))

        data.write(b"|&\x9e\xbc")  # 0x7c269ebc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

        data.write(b"\xee\x16\x97y")  # 0xee169779
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xee169779))

        data.write(b"X\xbc\x9d]")  # 0x58bc9d5d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x58bc9d5d))

        data.write(b"\xf4\xf1\x9c\x8b")  # 0xf4f19c8b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xf4f19c8b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"R\x86\x97?")  # 0x5286973f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x5286973f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"cn\x8d\xa2")  # 0x636e8da2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x636e8da2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc5\x19\x86\x16")  # 0xc5198616
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xc5198616.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\xbe\xb8\x98")  # 0xbeb898
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x00beb898.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa6\xc9\xb3,")  # 0xa6c9b32c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xa6c9b32c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_ScanVisorJson", data)
        return cls(
            unknown_0x5d750eef=Color.from_json(json_data["unknown_0x5d750eef"]),
            inactive_color=Color.from_json(json_data["inactive_color"]),
            inactive_external_color=Color.from_json(json_data["inactive_external_color"]),
            non_critical_color=Color.from_json(json_data["non_critical_color"]),
            critical_color=Color.from_json(json_data["critical_color"]),
            burn_in_color=Color.from_json(json_data["burn_in_color"]),
            highlight_color=Color.from_json(json_data["highlight_color"]),
            unknown_0x84badf82=Color.from_json(json_data["unknown_0x84badf82"]),
            critical_highlight_color=Color.from_json(json_data["critical_highlight_color"]),
            unknown_0xe8f5018b=Color.from_json(json_data["unknown_0xe8f5018b"]),
            unknown_0xba1ae1e5=Color.from_json(json_data["unknown_0xba1ae1e5"]),
            unknown_0xb39d450e=Color.from_json(json_data["unknown_0xb39d450e"]),
            unknown_0x1042455b=Color.from_json(json_data["unknown_0x1042455b"]),
            unknown_0xd72435ad=Color.from_json(json_data["unknown_0xd72435ad"]),
            unknown_0x75cdc913=Color.from_json(json_data["unknown_0x75cdc913"]),
            sweep_bar_color=Color.from_json(json_data["sweep_bar_color"]),
            burn_in_time=json_data["burn_in_time"],
            fade_out_time=json_data["fade_out_time"],
            unknown_0xee169779=json_data["unknown_0xee169779"],
            unknown_0x58bc9d5d=json_data["unknown_0x58bc9d5d"],
            unknown_0xf4f19c8b=Spline.from_json(json_data["unknown_0xf4f19c8b"]),
            unknown_0x5286973f=Spline.from_json(json_data["unknown_0x5286973f"]),
            unknown_0x636e8da2=Spline.from_json(json_data["unknown_0x636e8da2"]),
            unknown_0xc5198616=Spline.from_json(json_data["unknown_0xc5198616"]),
            unknown_0x00beb898=Spline.from_json(json_data["unknown_0x00beb898"]),
            unknown_0xa6c9b32c=Spline.from_json(json_data["unknown_0xa6c9b32c"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x5d750eef": self.unknown_0x5d750eef.to_json(),
            "inactive_color": self.inactive_color.to_json(),
            "inactive_external_color": self.inactive_external_color.to_json(),
            "non_critical_color": self.non_critical_color.to_json(),
            "critical_color": self.critical_color.to_json(),
            "burn_in_color": self.burn_in_color.to_json(),
            "highlight_color": self.highlight_color.to_json(),
            "unknown_0x84badf82": self.unknown_0x84badf82.to_json(),
            "critical_highlight_color": self.critical_highlight_color.to_json(),
            "unknown_0xe8f5018b": self.unknown_0xe8f5018b.to_json(),
            "unknown_0xba1ae1e5": self.unknown_0xba1ae1e5.to_json(),
            "unknown_0xb39d450e": self.unknown_0xb39d450e.to_json(),
            "unknown_0x1042455b": self.unknown_0x1042455b.to_json(),
            "unknown_0xd72435ad": self.unknown_0xd72435ad.to_json(),
            "unknown_0x75cdc913": self.unknown_0x75cdc913.to_json(),
            "sweep_bar_color": self.sweep_bar_color.to_json(),
            "burn_in_time": self.burn_in_time,
            "fade_out_time": self.fade_out_time,
            "unknown_0xee169779": self.unknown_0xee169779,
            "unknown_0x58bc9d5d": self.unknown_0x58bc9d5d,
            "unknown_0xf4f19c8b": self.unknown_0xf4f19c8b.to_json(),
            "unknown_0x5286973f": self.unknown_0x5286973f.to_json(),
            "unknown_0x636e8da2": self.unknown_0x636e8da2.to_json(),
            "unknown_0xc5198616": self.unknown_0xc5198616.to_json(),
            "unknown_0x00beb898": self.unknown_0x00beb898.to_json(),
            "unknown_0xa6c9b32c": self.unknown_0xa6c9b32c.to_json(),
        }


def _decode_unknown_0x5d750eef(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inactive_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inactive_external_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_non_critical_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_burn_in_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x84badf82(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xe8f5018b(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xba1ae1e5(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xb39d450e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x1042455b(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xd72435ad(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x75cdc913(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_sweep_bar_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xf4f19c8b(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x5286973f(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x636e8da2(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0xc5198616(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x00beb898(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0xa6c9b32c(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5D750EEF: ("unknown_0x5d750eef", _decode_unknown_0x5d750eef),
    0x972271B9: ("inactive_color", _decode_inactive_color),
    0xA908C775: ("inactive_external_color", _decode_inactive_external_color),
    0xEE1F1DF6: ("non_critical_color", _decode_non_critical_color),
    0x43445AE7: ("critical_color", _decode_critical_color),
    0xF48FD559: ("burn_in_color", _decode_burn_in_color),
    0x7A6412F6: ("highlight_color", _decode_highlight_color),
    0x84BADF82: ("unknown_0x84badf82", _decode_unknown_0x84badf82),
    0xF45F7D17: ("critical_highlight_color", _decode_critical_highlight_color),
    0xE8F5018B: ("unknown_0xe8f5018b", _decode_unknown_0xe8f5018b),
    0xBA1AE1E5: ("unknown_0xba1ae1e5", _decode_unknown_0xba1ae1e5),
    0xB39D450E: ("unknown_0xb39d450e", _decode_unknown_0xb39d450e),
    0x1042455B: ("unknown_0x1042455b", _decode_unknown_0x1042455b),
    0xD72435AD: ("unknown_0xd72435ad", _decode_unknown_0xd72435ad),
    0x75CDC913: ("unknown_0x75cdc913", _decode_unknown_0x75cdc913),
    0x997EC38D: ("sweep_bar_color", _decode_sweep_bar_color),
    0x00B83F02: ("burn_in_time", structs.decode_BIG_f),
    0x7C269EBC: ("fade_out_time", structs.decode_BIG_f),
    0xEE169779: ("unknown_0xee169779", structs.decode_BIG_f),
    0x58BC9D5D: ("unknown_0x58bc9d5d", structs.decode_BIG_f),
    0xF4F19C8B: ("unknown_0xf4f19c8b", _decode_unknown_0xf4f19c8b),
    0x5286973F: ("unknown_0x5286973f", _decode_unknown_0x5286973f),
    0x636E8DA2: ("unknown_0x636e8da2", _decode_unknown_0x636e8da2),
    0xC5198616: ("unknown_0xc5198616", _decode_unknown_0xc5198616),
    0x00BEB898: ("unknown_0x00beb898", _decode_unknown_0x00beb898),
    0xA6C9B32C: ("unknown_0xa6c9b32c", _decode_unknown_0xa6c9b32c),
}
