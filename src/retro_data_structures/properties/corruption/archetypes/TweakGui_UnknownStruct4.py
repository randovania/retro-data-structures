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

    class TweakGui_UnknownStruct4Json(typing_extensions.TypedDict):
        outline_color: json_util.JsonValue
        stripe_color: json_util.JsonValue
        stripe_scale: float
        min_random_stripe_wipe_speed: float
        max_random_stripe_wipe_speed: float
        unknown_0x8c9a8472: float
        unknown_0x3ca59e4e: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x60D78569, 0xD2E92C37, 0xC97F5ADC, 0x38DB0D63, 0xD7591319, 0x8C9A8472, 0x3CA59E4E)


@dataclasses.dataclass()
class TweakGui_UnknownStruct4(BaseProperty):
    outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x60D78569, original_name="OutlineColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    stripe_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD2E92C37, original_name="StripeColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    stripe_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC97F5ADC, original_name="StripeScale"),
        },
    )
    min_random_stripe_wipe_speed: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x38DB0D63, original_name="MinRandomStripeWipeSpeed"),
        },
    )
    max_random_stripe_wipe_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD7591319, original_name="MaxRandomStripeWipeSpeed"),
        },
    )
    unknown_0x8c9a8472: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8C9A8472, original_name="Unknown"),
        },
    )
    unknown_0x3ca59e4e: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3CA59E4E, original_name="Unknown"),
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
            _FAST_FORMAT = struct.Struct(">LHffffLHffffLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(94))
        assert (dec[0], dec[6], dec[12], dec[15], dec[18], dec[21], dec[24]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"`\xd7\x85i")  # 0x60d78569
        data.write(b"\x00\x10")  # size
        self.outline_color.to_stream(data, game)

        data.write(b"\xd2\xe9,7")  # 0xd2e92c37
        data.write(b"\x00\x10")  # size
        self.stripe_color.to_stream(data, game)

        data.write(b"\xc9\x7fZ\xdc")  # 0xc97f5adc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stripe_scale))

        data.write(b"8\xdb\rc")  # 0x38db0d63
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_random_stripe_wipe_speed))

        data.write(b"\xd7Y\x13\x19")  # 0xd7591319
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_random_stripe_wipe_speed))

        data.write(b"\x8c\x9a\x84r")  # 0x8c9a8472
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8c9a8472))

        data.write(b"<\xa5\x9eN")  # 0x3ca59e4e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3ca59e4e))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_UnknownStruct4Json", data)
        return cls(
            outline_color=Color.from_json(json_data["outline_color"]),
            stripe_color=Color.from_json(json_data["stripe_color"]),
            stripe_scale=json_data["stripe_scale"],
            min_random_stripe_wipe_speed=json_data["min_random_stripe_wipe_speed"],
            max_random_stripe_wipe_speed=json_data["max_random_stripe_wipe_speed"],
            unknown_0x8c9a8472=json_data["unknown_0x8c9a8472"],
            unknown_0x3ca59e4e=json_data["unknown_0x3ca59e4e"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "outline_color": self.outline_color.to_json(),
            "stripe_color": self.stripe_color.to_json(),
            "stripe_scale": self.stripe_scale,
            "min_random_stripe_wipe_speed": self.min_random_stripe_wipe_speed,
            "max_random_stripe_wipe_speed": self.max_random_stripe_wipe_speed,
            "unknown_0x8c9a8472": self.unknown_0x8c9a8472,
            "unknown_0x3ca59e4e": self.unknown_0x3ca59e4e,
        }


def _decode_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_stripe_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x60D78569: ("outline_color", _decode_outline_color),
    0xD2E92C37: ("stripe_color", _decode_stripe_color),
    0xC97F5ADC: ("stripe_scale", structs.decode_BIG_f),
    0x38DB0D63: ("min_random_stripe_wipe_speed", structs.decode_BIG_f),
    0xD7591319: ("max_random_stripe_wipe_speed", structs.decode_BIG_f),
    0x8C9A8472: ("unknown_0x8c9a8472", structs.decode_BIG_f),
    0x3CA59E4E: ("unknown_0x3ca59e4e", structs.decode_BIG_f),
}
