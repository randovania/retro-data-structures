# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakAutoMapper_DoorColorsJson(typing_extensions.TypedDict):
        num_door_colors: int
        blue_door_color: json_util.JsonValue
        missile_door_color: json_util.JsonValue
        dark_beam_door_color: json_util.JsonValue
        unknown: json_util.JsonValue
        annihilator_beam_door_color: json_util.JsonValue
        light_beam_door_color: json_util.JsonValue
        super_missile_door_color: json_util.JsonValue
        seeker_door_color: json_util.JsonValue
        power_bomb_door_color: json_util.JsonValue
        grey_door_color: json_util.JsonValue
        white_door_color: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x4FCEB904,
    0xB36AA9B7,
    0x9620D4A0,
    0x4E1A9A8D,
    0xCE986453,
    0x70F36F9,
    0xFADA14B6,
    0x172241DC,
    0x518BCCDC,
    0x2853FA91,
    0xE655A18E,
    0xF08F35E,
)


@dataclasses.dataclass()
class TweakAutoMapper_DoorColors(BaseProperty):
    num_door_colors: int = dataclasses.field(
        default=8,
        metadata={
            "reflection": FieldReflection[int](int, id=0x4FCEB904, original_name="NumDoorColors"),
        },
    )
    blue_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xB36AA9B7, original_name="BlueDoorColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    missile_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x9620D4A0, original_name="MissileDoorColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    dark_beam_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x4E1A9A8D,
                original_name="DarkBeamDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xCE986453, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    annihilator_beam_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x070F36F9,
                original_name="AnnihilatorBeamDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    light_beam_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xFADA14B6,
                original_name="LightBeamDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    super_missile_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x172241DC,
                original_name="SuperMissileDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    seeker_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x518BCCDC, original_name="SeekerDoorColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    power_bomb_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x2853FA91,
                original_name="PowerBombDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    grey_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE655A18E, original_name="GreyDoorColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    white_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0F08F35E, original_name="WhiteDoorColor", from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 12:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffff")

        dec = _FAST_FORMAT.unpack(data.read(252))
        assert (
            dec[0],
            dec[3],
            dec[9],
            dec[15],
            dec[21],
            dec[27],
            dec[33],
            dec[39],
            dec[45],
            dec[51],
            dec[57],
            dec[63],
        ) == _FAST_IDS
        return cls(
            dec[2],
            Color(*dec[5:9]),
            Color(*dec[11:15]),
            Color(*dec[17:21]),
            Color(*dec[23:27]),
            Color(*dec[29:33]),
            Color(*dec[35:39]),
            Color(*dec[41:45]),
            Color(*dec[47:51]),
            Color(*dec[53:57]),
            Color(*dec[59:63]),
            Color(*dec[65:69]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0c")  # 12 properties

        data.write(b"O\xce\xb9\x04")  # 0x4fceb904
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.num_door_colors))

        data.write(b"\xb3j\xa9\xb7")  # 0xb36aa9b7
        data.write(b"\x00\x10")  # size
        self.blue_door_color.to_stream(data, game)

        data.write(b"\x96 \xd4\xa0")  # 0x9620d4a0
        data.write(b"\x00\x10")  # size
        self.missile_door_color.to_stream(data, game)

        data.write(b"N\x1a\x9a\x8d")  # 0x4e1a9a8d
        data.write(b"\x00\x10")  # size
        self.dark_beam_door_color.to_stream(data, game)

        data.write(b"\xce\x98dS")  # 0xce986453
        data.write(b"\x00\x10")  # size
        self.unknown.to_stream(data, game)

        data.write(b"\x07\x0f6\xf9")  # 0x70f36f9
        data.write(b"\x00\x10")  # size
        self.annihilator_beam_door_color.to_stream(data, game)

        data.write(b"\xfa\xda\x14\xb6")  # 0xfada14b6
        data.write(b"\x00\x10")  # size
        self.light_beam_door_color.to_stream(data, game)

        data.write(b'\x17"A\xdc')  # 0x172241dc
        data.write(b"\x00\x10")  # size
        self.super_missile_door_color.to_stream(data, game)

        data.write(b"Q\x8b\xcc\xdc")  # 0x518bccdc
        data.write(b"\x00\x10")  # size
        self.seeker_door_color.to_stream(data, game)

        data.write(b"(S\xfa\x91")  # 0x2853fa91
        data.write(b"\x00\x10")  # size
        self.power_bomb_door_color.to_stream(data, game)

        data.write(b"\xe6U\xa1\x8e")  # 0xe655a18e
        data.write(b"\x00\x10")  # size
        self.grey_door_color.to_stream(data, game)

        data.write(b"\x0f\x08\xf3^")  # 0xf08f35e
        data.write(b"\x00\x10")  # size
        self.white_door_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakAutoMapper_DoorColorsJson", data)
        return cls(
            num_door_colors=json_data["num_door_colors"],
            blue_door_color=Color.from_json(json_data["blue_door_color"]),
            missile_door_color=Color.from_json(json_data["missile_door_color"]),
            dark_beam_door_color=Color.from_json(json_data["dark_beam_door_color"]),
            unknown=Color.from_json(json_data["unknown"]),
            annihilator_beam_door_color=Color.from_json(json_data["annihilator_beam_door_color"]),
            light_beam_door_color=Color.from_json(json_data["light_beam_door_color"]),
            super_missile_door_color=Color.from_json(json_data["super_missile_door_color"]),
            seeker_door_color=Color.from_json(json_data["seeker_door_color"]),
            power_bomb_door_color=Color.from_json(json_data["power_bomb_door_color"]),
            grey_door_color=Color.from_json(json_data["grey_door_color"]),
            white_door_color=Color.from_json(json_data["white_door_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "num_door_colors": self.num_door_colors,
            "blue_door_color": self.blue_door_color.to_json(),
            "missile_door_color": self.missile_door_color.to_json(),
            "dark_beam_door_color": self.dark_beam_door_color.to_json(),
            "unknown": self.unknown.to_json(),
            "annihilator_beam_door_color": self.annihilator_beam_door_color.to_json(),
            "light_beam_door_color": self.light_beam_door_color.to_json(),
            "super_missile_door_color": self.super_missile_door_color.to_json(),
            "seeker_door_color": self.seeker_door_color.to_json(),
            "power_bomb_door_color": self.power_bomb_door_color.to_json(),
            "grey_door_color": self.grey_door_color.to_json(),
            "white_door_color": self.white_door_color.to_json(),
        }


def _decode_blue_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_beam_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_annihilator_beam_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_beam_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_super_missile_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_seeker_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_power_bomb_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_grey_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_white_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4FCEB904: ("num_door_colors", structs.decode_BIG_l),
    0xB36AA9B7: ("blue_door_color", _decode_blue_door_color),
    0x9620D4A0: ("missile_door_color", _decode_missile_door_color),
    0x4E1A9A8D: ("dark_beam_door_color", _decode_dark_beam_door_color),
    0xCE986453: ("unknown", _decode_unknown),
    0x070F36F9: ("annihilator_beam_door_color", _decode_annihilator_beam_door_color),
    0xFADA14B6: ("light_beam_door_color", _decode_light_beam_door_color),
    0x172241DC: ("super_missile_door_color", _decode_super_missile_door_color),
    0x518BCCDC: ("seeker_door_color", _decode_seeker_door_color),
    0x2853FA91: ("power_bomb_door_color", _decode_power_bomb_door_color),
    0xE655A18E: ("grey_door_color", _decode_grey_door_color),
    0x0F08F35E: ("white_door_color", _decode_white_door_color),
}
