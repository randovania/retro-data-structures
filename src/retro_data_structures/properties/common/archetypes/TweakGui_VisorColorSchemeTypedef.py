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

    class TweakGui_VisorColorSchemeTypedefJson(typing_extensions.TypedDict):
        hud_hue: json_util.JsonValue
        unknown: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x59148173, 0x9DA5D1D7)


@dataclasses.dataclass()
class TweakGui_VisorColorSchemeTypedef(BaseProperty):
    hud_hue: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x59148173, original_name="HUDHue", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x9DA5D1D7, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 2:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHffffLHffff")

        dec = _FAST_FORMAT.unpack(data.read(44))
        assert (dec[0], dec[6]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"Y\x14\x81s")  # 0x59148173
        data.write(b"\x00\x10")  # size
        self.hud_hue.to_stream(data, game)

        data.write(b"\x9d\xa5\xd1\xd7")  # 0x9da5d1d7
        data.write(b"\x00\x10")  # size
        self.unknown.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_VisorColorSchemeTypedefJson", data)
        return cls(
            hud_hue=Color.from_json(json_data["hud_hue"]),
            unknown=Color.from_json(json_data["unknown"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hud_hue": self.hud_hue.to_json(),
            "unknown": self.unknown.to_json(),
        }


def _decode_hud_hue(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x59148173: ("hud_hue", _decode_hud_hue),
    0x9DA5D1D7: ("unknown", _decode_unknown),
}
