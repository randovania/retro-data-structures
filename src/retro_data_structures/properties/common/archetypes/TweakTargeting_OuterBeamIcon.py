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

    class TweakTargeting_OuterBeamIconJson(typing_extensions.TypedDict):
        unknown_0x383e2b2d: float
        unknown_0xeaac42d0: float
        but_settings_color: float
        but_settings_scale: json_util.JsonValue
        unknown_0xe7d57d6a: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x383E2B2D, 0xEAAC42D0, 0x4967A63C, 0x52F1D0D7, 0xE7D57D6A)


@dataclasses.dataclass()
class TweakTargeting_OuterBeamIcon(BaseProperty):
    unknown_0x383e2b2d: float = dataclasses.field(
        default=1.100000023841858,
        metadata={
            "reflection": FieldReflection[float](float, id=0x383E2B2D, original_name="Unknown"),
        },
    )
    unknown_0xeaac42d0: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEAAC42D0, original_name="Unknown"),
        },
    )
    but_settings_color: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4967A63C, original_name="But_Settings_Color"),
        },
    )
    but_settings_scale: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x52F1D0D7,
                original_name="But_Settings_Scale",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xe7d57d6a: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE7D57D6A, original_name="Unknown"),
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
        if property_count != 5:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHffffLHl")

        dec = _FAST_FORMAT.unpack(data.read(62))
        assert (dec[0], dec[3], dec[6], dec[9], dec[15]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            Color(*dec[11:15]),
            dec[17],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"8>+-")  # 0x383e2b2d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x383e2b2d))

        data.write(b"\xea\xacB\xd0")  # 0xeaac42d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xeaac42d0))

        data.write(b"Ig\xa6<")  # 0x4967a63c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.but_settings_color))

        data.write(b"R\xf1\xd0\xd7")  # 0x52f1d0d7
        data.write(b"\x00\x10")  # size
        self.but_settings_scale.to_stream(data, game)

        data.write(b"\xe7\xd5}j")  # 0xe7d57d6a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe7d57d6a))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_OuterBeamIconJson", data)
        return cls(
            unknown_0x383e2b2d=json_data["unknown_0x383e2b2d"],
            unknown_0xeaac42d0=json_data["unknown_0xeaac42d0"],
            but_settings_color=json_data["but_settings_color"],
            but_settings_scale=Color.from_json(json_data["but_settings_scale"]),
            unknown_0xe7d57d6a=json_data["unknown_0xe7d57d6a"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x383e2b2d": self.unknown_0x383e2b2d,
            "unknown_0xeaac42d0": self.unknown_0xeaac42d0,
            "but_settings_color": self.but_settings_color,
            "but_settings_scale": self.but_settings_scale.to_json(),
            "unknown_0xe7d57d6a": self.unknown_0xe7d57d6a,
        }


def _decode_but_settings_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x383E2B2D: ("unknown_0x383e2b2d", structs.decode_BIG_f),
    0xEAAC42D0: ("unknown_0xeaac42d0", structs.decode_BIG_f),
    0x4967A63C: ("but_settings_color", structs.decode_BIG_f),
    0x52F1D0D7: ("but_settings_scale", _decode_but_settings_scale),
    0xE7D57D6A: ("unknown_0xe7d57d6a", structs.decode_BIG_l),
}
