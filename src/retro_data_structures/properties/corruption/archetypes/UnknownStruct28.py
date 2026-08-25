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

    class UnknownStruct28Json(typing_extensions.TypedDict):
        common_vertical_scale: float
        unknown_0x8ed32be8: float
        unknown_0xcfc4146e: float
        unknown_0x0479c95b: float
        unknown_0xdfc69abc: float
        unknown_0x9c27ea0d: float
        unknown_0xe8c00bb1: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x50AF31E, 0x8ED32BE8, 0xCFC4146E, 0x479C95B, 0xDFC69ABC, 0x9C27EA0D, 0xE8C00BB1)


@dataclasses.dataclass()
class UnknownStruct28(BaseProperty):
    common_vertical_scale: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x050AF31E, original_name="CommonVerticalScale"),
        },
    )
    unknown_0x8ed32be8: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8ED32BE8, original_name="Unknown"),
        },
    )
    unknown_0xcfc4146e: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCFC4146E, original_name="Unknown"),
        },
    )
    unknown_0x0479c95b: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0479C95B, original_name="Unknown"),
        },
    )
    unknown_0xdfc69abc: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDFC69ABC, original_name="Unknown"),
        },
    )
    unknown_0x9c27ea0d: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9C27EA0D, original_name="Unknown"),
        },
    )
    unknown_0xe8c00bb1: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8C00BB1, original_name="Unknown"),
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
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(70))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\x05\n\xf3\x1e")  # 0x50af31e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.common_vertical_scale))

        data.write(b"\x8e\xd3+\xe8")  # 0x8ed32be8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8ed32be8))

        data.write(b"\xcf\xc4\x14n")  # 0xcfc4146e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcfc4146e))

        data.write(b"\x04y\xc9[")  # 0x479c95b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0479c95b))

        data.write(b"\xdf\xc6\x9a\xbc")  # 0xdfc69abc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdfc69abc))

        data.write(b"\x9c'\xea\r")  # 0x9c27ea0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9c27ea0d))

        data.write(b"\xe8\xc0\x0b\xb1")  # 0xe8c00bb1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe8c00bb1))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct28Json", data)
        return cls(
            common_vertical_scale=json_data["common_vertical_scale"],
            unknown_0x8ed32be8=json_data["unknown_0x8ed32be8"],
            unknown_0xcfc4146e=json_data["unknown_0xcfc4146e"],
            unknown_0x0479c95b=json_data["unknown_0x0479c95b"],
            unknown_0xdfc69abc=json_data["unknown_0xdfc69abc"],
            unknown_0x9c27ea0d=json_data["unknown_0x9c27ea0d"],
            unknown_0xe8c00bb1=json_data["unknown_0xe8c00bb1"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "common_vertical_scale": self.common_vertical_scale,
            "unknown_0x8ed32be8": self.unknown_0x8ed32be8,
            "unknown_0xcfc4146e": self.unknown_0xcfc4146e,
            "unknown_0x0479c95b": self.unknown_0x0479c95b,
            "unknown_0xdfc69abc": self.unknown_0xdfc69abc,
            "unknown_0x9c27ea0d": self.unknown_0x9c27ea0d,
            "unknown_0xe8c00bb1": self.unknown_0xe8c00bb1,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x050AF31E: ("common_vertical_scale", structs.decode_BIG_f),
    0x8ED32BE8: ("unknown_0x8ed32be8", structs.decode_BIG_f),
    0xCFC4146E: ("unknown_0xcfc4146e", structs.decode_BIG_f),
    0x0479C95B: ("unknown_0x0479c95b", structs.decode_BIG_f),
    0xDFC69ABC: ("unknown_0xdfc69abc", structs.decode_BIG_f),
    0x9C27EA0D: ("unknown_0x9c27ea0d", structs.decode_BIG_f),
    0xE8C00BB1: ("unknown_0xe8c00bb1", structs.decode_BIG_f),
}
