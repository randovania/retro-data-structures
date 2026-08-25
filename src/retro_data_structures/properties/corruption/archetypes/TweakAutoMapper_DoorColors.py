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
        power_beam_door_color: json_util.JsonValue
        nova_beam_door_color: json_util.JsonValue
        plasma_beam_door_color: json_util.JsonValue
        missile_door_color: json_util.JsonValue
        ice_missile_door_color: json_util.JsonValue
        seeker_missile_door_color: json_util.JsonValue
        grapple_voltage_door_color: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xE9D5359D, 0x393E8990, 0x96F5253A, 0x9620D4A0, 0x79831276, 0x5AC17B63, 0x69E23CF3)


@dataclasses.dataclass()
class TweakAutoMapper_DoorColors(BaseProperty):
    power_beam_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xE9D5359D,
                original_name="PowerBeamDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    nova_beam_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x393E8990,
                original_name="NovaBeamDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    plasma_beam_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x96F5253A,
                original_name="PlasmaBeamDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
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
    ice_missile_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x79831276,
                original_name="IceMissileDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    seeker_missile_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x5AC17B63,
                original_name="SeekerMissileDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    grapple_voltage_door_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x69E23CF3,
                original_name="GrappleVoltageDoorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
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
        if property_count != 7:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHffffLHffffLHffffLHffffLHffffLHffffLHffff")

        dec = _FAST_FORMAT.unpack(data.read(154))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[30], dec[36]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            Color(*dec[26:30]),
            Color(*dec[32:36]),
            Color(*dec[38:42]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\xe9\xd55\x9d")  # 0xe9d5359d
        data.write(b"\x00\x10")  # size
        self.power_beam_door_color.to_stream(data, game)

        data.write(b"9>\x89\x90")  # 0x393e8990
        data.write(b"\x00\x10")  # size
        self.nova_beam_door_color.to_stream(data, game)

        data.write(b"\x96\xf5%:")  # 0x96f5253a
        data.write(b"\x00\x10")  # size
        self.plasma_beam_door_color.to_stream(data, game)

        data.write(b"\x96 \xd4\xa0")  # 0x9620d4a0
        data.write(b"\x00\x10")  # size
        self.missile_door_color.to_stream(data, game)

        data.write(b"y\x83\x12v")  # 0x79831276
        data.write(b"\x00\x10")  # size
        self.ice_missile_door_color.to_stream(data, game)

        data.write(b"Z\xc1{c")  # 0x5ac17b63
        data.write(b"\x00\x10")  # size
        self.seeker_missile_door_color.to_stream(data, game)

        data.write(b"i\xe2<\xf3")  # 0x69e23cf3
        data.write(b"\x00\x10")  # size
        self.grapple_voltage_door_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakAutoMapper_DoorColorsJson", data)
        return cls(
            power_beam_door_color=Color.from_json(json_data["power_beam_door_color"]),
            nova_beam_door_color=Color.from_json(json_data["nova_beam_door_color"]),
            plasma_beam_door_color=Color.from_json(json_data["plasma_beam_door_color"]),
            missile_door_color=Color.from_json(json_data["missile_door_color"]),
            ice_missile_door_color=Color.from_json(json_data["ice_missile_door_color"]),
            seeker_missile_door_color=Color.from_json(json_data["seeker_missile_door_color"]),
            grapple_voltage_door_color=Color.from_json(json_data["grapple_voltage_door_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "power_beam_door_color": self.power_beam_door_color.to_json(),
            "nova_beam_door_color": self.nova_beam_door_color.to_json(),
            "plasma_beam_door_color": self.plasma_beam_door_color.to_json(),
            "missile_door_color": self.missile_door_color.to_json(),
            "ice_missile_door_color": self.ice_missile_door_color.to_json(),
            "seeker_missile_door_color": self.seeker_missile_door_color.to_json(),
            "grapple_voltage_door_color": self.grapple_voltage_door_color.to_json(),
        }


def _decode_power_beam_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_nova_beam_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_plasma_beam_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ice_missile_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_seeker_missile_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_grapple_voltage_door_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xE9D5359D: ("power_beam_door_color", _decode_power_beam_door_color),
    0x393E8990: ("nova_beam_door_color", _decode_nova_beam_door_color),
    0x96F5253A: ("plasma_beam_door_color", _decode_plasma_beam_door_color),
    0x9620D4A0: ("missile_door_color", _decode_missile_door_color),
    0x79831276: ("ice_missile_door_color", _decode_ice_missile_door_color),
    0x5AC17B63: ("seeker_missile_door_color", _decode_seeker_missile_door_color),
    0x69E23CF3: ("grapple_voltage_door_color", _decode_grapple_voltage_door_color),
}
