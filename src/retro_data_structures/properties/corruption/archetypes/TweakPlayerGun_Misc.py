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

    class TweakPlayerGun_MiscJson(typing_extensions.TypedDict):
        up_look_angle: float
        down_look_angle: float
        vertical_spread: float
        horizontal_spread: float
        high_vertical_spread: float
        high_horizontal_spread: float
        low_vertical_spread: float
        low_horizontal_spread: float
        aim_vertical_speed: float
        aim_horizontal_speed: float
        hologram_display_time: float
        gun_transform_time: float
        unknown_0x83a87042: json_util.JsonValue
        unknown_0x47ea54ce: json_util.JsonValue
        unknown_0x7d061fe0: json_util.JsonValue
        unknown_0x6a880308: json_util.JsonValue
        unknown_0xdcf458b3: json_util.JsonObject
        unknown_0x4b6b499a: json_util.JsonObject
        unknown_0xf8a655db: float


@dataclasses.dataclass()
class TweakPlayerGun_Misc(BaseProperty):
    up_look_angle: float = dataclasses.field(
        default=22.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8BB7E3C, original_name="UpLookAngle"),
        },
    )
    down_look_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5ED7E0BD, original_name="DownLookAngle"),
        },
    )
    vertical_spread: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x842AE0B4, original_name="VerticalSpread"),
        },
    )
    horizontal_spread: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8C29E91C, original_name="HorizontalSpread"),
        },
    )
    high_vertical_spread: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D5A6C93, original_name="HighVerticalSpread"),
        },
    )
    high_horizontal_spread: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB2E26D02, original_name="HighHorizontalSpread"),
        },
    )
    low_vertical_spread: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD81D1450, original_name="LowVerticalSpread"),
        },
    )
    low_horizontal_spread: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0CEBB5C6, original_name="LowHorizontalSpread"),
        },
    )
    aim_vertical_speed: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x904CD49D, original_name="AimVerticalSpeed"),
        },
    )
    aim_horizontal_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFCCDDB00, original_name="AimHorizontalSpeed"),
        },
    )
    hologram_display_time: float = dataclasses.field(
        default=0.0625,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF355D075, original_name="HologramDisplayTime"),
        },
    )
    gun_transform_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9262A722, original_name="GunTransformTime"),
        },
    )
    unknown_0x83a87042: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x83A87042, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x47ea54ce: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x47EA54CE, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x7d061fe0: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x7D061FE0, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x6a880308: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x6A880308, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdcf458b3: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xDCF458B3, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x4b6b499a: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x4B6B499A, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xf8a655db: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8A655DB, original_name="Unknown"),
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
        if property_count != 19:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8BB7E3C
        up_look_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ED7E0BD
        down_look_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x842AE0B4
        vertical_spread = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8C29E91C
        horizontal_spread = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D5A6C93
        high_vertical_spread = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2E26D02
        high_horizontal_spread = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD81D1450
        low_vertical_spread = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0CEBB5C6
        low_horizontal_spread = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x904CD49D
        aim_vertical_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFCCDDB00
        aim_horizontal_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF355D075
        hologram_display_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9262A722
        gun_transform_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83A87042
        unknown_0x83a87042 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47EA54CE
        unknown_0x47ea54ce = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D061FE0
        unknown_0x7d061fe0 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A880308
        unknown_0x6a880308 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCF458B3
        unknown_0xdcf458b3 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B6B499A
        unknown_0x4b6b499a = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8A655DB
        unknown_0xf8a655db = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            up_look_angle,
            down_look_angle,
            vertical_spread,
            horizontal_spread,
            high_vertical_spread,
            high_horizontal_spread,
            low_vertical_spread,
            low_horizontal_spread,
            aim_vertical_speed,
            aim_horizontal_speed,
            hologram_display_time,
            gun_transform_time,
            unknown_0x83a87042,
            unknown_0x47ea54ce,
            unknown_0x7d061fe0,
            unknown_0x6a880308,
            unknown_0xdcf458b3,
            unknown_0x4b6b499a,
            unknown_0xf8a655db,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x13")  # 19 properties

        data.write(b"\xe8\xbb~<")  # 0xe8bb7e3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.up_look_angle))

        data.write(b"^\xd7\xe0\xbd")  # 0x5ed7e0bd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.down_look_angle))

        data.write(b"\x84*\xe0\xb4")  # 0x842ae0b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.vertical_spread))

        data.write(b"\x8c)\xe9\x1c")  # 0x8c29e91c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.horizontal_spread))

        data.write(b"}Zl\x93")  # 0x7d5a6c93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.high_vertical_spread))

        data.write(b"\xb2\xe2m\x02")  # 0xb2e26d02
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.high_horizontal_spread))

        data.write(b"\xd8\x1d\x14P")  # 0xd81d1450
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.low_vertical_spread))

        data.write(b"\x0c\xeb\xb5\xc6")  # 0xcebb5c6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.low_horizontal_spread))

        data.write(b"\x90L\xd4\x9d")  # 0x904cd49d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_vertical_speed))

        data.write(b"\xfc\xcd\xdb\x00")  # 0xfccddb00
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_horizontal_speed))

        data.write(b"\xf3U\xd0u")  # 0xf355d075
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hologram_display_time))

        data.write(b'\x92b\xa7"')  # 0x9262a722
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gun_transform_time))

        data.write(b"\x83\xa8pB")  # 0x83a87042
        data.write(b"\x00\x10")  # size
        self.unknown_0x83a87042.to_stream(data, game)

        data.write(b"G\xeaT\xce")  # 0x47ea54ce
        data.write(b"\x00\x10")  # size
        self.unknown_0x47ea54ce.to_stream(data, game)

        data.write(b"}\x06\x1f\xe0")  # 0x7d061fe0
        data.write(b"\x00\x10")  # size
        self.unknown_0x7d061fe0.to_stream(data, game)

        data.write(b"j\x88\x03\x08")  # 0x6a880308
        data.write(b"\x00\x10")  # size
        self.unknown_0x6a880308.to_stream(data, game)

        data.write(b"\xdc\xf4X\xb3")  # 0xdcf458b3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xdcf458b3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"KkI\x9a")  # 0x4b6b499a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x4b6b499a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf8\xa6U\xdb")  # 0xf8a655db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf8a655db))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_MiscJson", data)
        return cls(
            up_look_angle=json_data["up_look_angle"],
            down_look_angle=json_data["down_look_angle"],
            vertical_spread=json_data["vertical_spread"],
            horizontal_spread=json_data["horizontal_spread"],
            high_vertical_spread=json_data["high_vertical_spread"],
            high_horizontal_spread=json_data["high_horizontal_spread"],
            low_vertical_spread=json_data["low_vertical_spread"],
            low_horizontal_spread=json_data["low_horizontal_spread"],
            aim_vertical_speed=json_data["aim_vertical_speed"],
            aim_horizontal_speed=json_data["aim_horizontal_speed"],
            hologram_display_time=json_data["hologram_display_time"],
            gun_transform_time=json_data["gun_transform_time"],
            unknown_0x83a87042=Color.from_json(json_data["unknown_0x83a87042"]),
            unknown_0x47ea54ce=Color.from_json(json_data["unknown_0x47ea54ce"]),
            unknown_0x7d061fe0=Color.from_json(json_data["unknown_0x7d061fe0"]),
            unknown_0x6a880308=Color.from_json(json_data["unknown_0x6a880308"]),
            unknown_0xdcf458b3=Spline.from_json(json_data["unknown_0xdcf458b3"]),
            unknown_0x4b6b499a=Spline.from_json(json_data["unknown_0x4b6b499a"]),
            unknown_0xf8a655db=json_data["unknown_0xf8a655db"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "up_look_angle": self.up_look_angle,
            "down_look_angle": self.down_look_angle,
            "vertical_spread": self.vertical_spread,
            "horizontal_spread": self.horizontal_spread,
            "high_vertical_spread": self.high_vertical_spread,
            "high_horizontal_spread": self.high_horizontal_spread,
            "low_vertical_spread": self.low_vertical_spread,
            "low_horizontal_spread": self.low_horizontal_spread,
            "aim_vertical_speed": self.aim_vertical_speed,
            "aim_horizontal_speed": self.aim_horizontal_speed,
            "hologram_display_time": self.hologram_display_time,
            "gun_transform_time": self.gun_transform_time,
            "unknown_0x83a87042": self.unknown_0x83a87042.to_json(),
            "unknown_0x47ea54ce": self.unknown_0x47ea54ce.to_json(),
            "unknown_0x7d061fe0": self.unknown_0x7d061fe0.to_json(),
            "unknown_0x6a880308": self.unknown_0x6a880308.to_json(),
            "unknown_0xdcf458b3": self.unknown_0xdcf458b3.to_json(),
            "unknown_0x4b6b499a": self.unknown_0x4b6b499a.to_json(),
            "unknown_0xf8a655db": self.unknown_0xf8a655db,
        }


def _decode_unknown_0x83a87042(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x47ea54ce(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x7d061fe0(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x6a880308(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdcf458b3(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x4b6b499a(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xE8BB7E3C: ("up_look_angle", structs.decode_BIG_f),
    0x5ED7E0BD: ("down_look_angle", structs.decode_BIG_f),
    0x842AE0B4: ("vertical_spread", structs.decode_BIG_f),
    0x8C29E91C: ("horizontal_spread", structs.decode_BIG_f),
    0x7D5A6C93: ("high_vertical_spread", structs.decode_BIG_f),
    0xB2E26D02: ("high_horizontal_spread", structs.decode_BIG_f),
    0xD81D1450: ("low_vertical_spread", structs.decode_BIG_f),
    0x0CEBB5C6: ("low_horizontal_spread", structs.decode_BIG_f),
    0x904CD49D: ("aim_vertical_speed", structs.decode_BIG_f),
    0xFCCDDB00: ("aim_horizontal_speed", structs.decode_BIG_f),
    0xF355D075: ("hologram_display_time", structs.decode_BIG_f),
    0x9262A722: ("gun_transform_time", structs.decode_BIG_f),
    0x83A87042: ("unknown_0x83a87042", _decode_unknown_0x83a87042),
    0x47EA54CE: ("unknown_0x47ea54ce", _decode_unknown_0x47ea54ce),
    0x7D061FE0: ("unknown_0x7d061fe0", _decode_unknown_0x7d061fe0),
    0x6A880308: ("unknown_0x6a880308", _decode_unknown_0x6a880308),
    0xDCF458B3: ("unknown_0xdcf458b3", _decode_unknown_0xdcf458b3),
    0x4B6B499A: ("unknown_0x4b6b499a", _decode_unknown_0x4b6b499a),
    0xF8A655DB: ("unknown_0xf8a655db", structs.decode_BIG_f),
}
