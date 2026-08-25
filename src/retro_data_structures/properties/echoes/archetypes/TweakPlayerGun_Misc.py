# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

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


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xE8BB7E3C,
    0x5ED7E0BD,
    0x842AE0B4,
    0x8C29E91C,
    0x7D5A6C93,
    0xB2E26D02,
    0xD81D1450,
    0xCEBB5C6,
    0x904CD49D,
    0xFCCDDB00,
    0xF355D075,
    0x9262A722,
)


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
        if property_count != 12:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(120))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0c")  # 12 properties

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
        }


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
}
