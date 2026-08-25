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

    class UnknownStruct29Json(typing_extensions.TypedDict):
        blinking_enabled: bool
        unknown_0x9b131110: float
        unknown_0xa5a6d998: float
        unknown_0xd9f6253b: int
        unknown_0x0896fde0: float
        unknown_0x5f98ada3: float
        unknown_0xc3230652: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x47C836C5, 0x9B131110, 0xA5A6D998, 0xD9F6253B, 0x896FDE0, 0x5F98ADA3, 0xC3230652)


@dataclasses.dataclass()
class UnknownStruct29(BaseProperty):
    blinking_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x47C836C5, original_name="BlinkingEnabled"),
        },
    )
    unknown_0x9b131110: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9B131110, original_name="Unknown"),
        },
    )
    unknown_0xa5a6d998: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA5A6D998, original_name="Unknown"),
        },
    )
    unknown_0xd9f6253b: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD9F6253B, original_name="Unknown"),
        },
    )
    unknown_0x0896fde0: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0896FDE0, original_name="Unknown"),
        },
    )
    unknown_0x5f98ada3: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5F98ADA3, original_name="Unknown"),
        },
    )
    unknown_0xc3230652: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3230652, original_name="Unknown"),
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
            _FAST_FORMAT = struct.Struct(">LH?LHfLHfLHlLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(67))
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

        data.write(b"G\xc86\xc5")  # 0x47c836c5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.blinking_enabled))

        data.write(b"\x9b\x13\x11\x10")  # 0x9b131110
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9b131110))

        data.write(b"\xa5\xa6\xd9\x98")  # 0xa5a6d998
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa5a6d998))

        data.write(b"\xd9\xf6%;")  # 0xd9f6253b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd9f6253b))

        data.write(b"\x08\x96\xfd\xe0")  # 0x896fde0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0896fde0))

        data.write(b"_\x98\xad\xa3")  # 0x5f98ada3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5f98ada3))

        data.write(b"\xc3#\x06R")  # 0xc3230652
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc3230652))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct29Json", data)
        return cls(
            blinking_enabled=json_data["blinking_enabled"],
            unknown_0x9b131110=json_data["unknown_0x9b131110"],
            unknown_0xa5a6d998=json_data["unknown_0xa5a6d998"],
            unknown_0xd9f6253b=json_data["unknown_0xd9f6253b"],
            unknown_0x0896fde0=json_data["unknown_0x0896fde0"],
            unknown_0x5f98ada3=json_data["unknown_0x5f98ada3"],
            unknown_0xc3230652=json_data["unknown_0xc3230652"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "blinking_enabled": self.blinking_enabled,
            "unknown_0x9b131110": self.unknown_0x9b131110,
            "unknown_0xa5a6d998": self.unknown_0xa5a6d998,
            "unknown_0xd9f6253b": self.unknown_0xd9f6253b,
            "unknown_0x0896fde0": self.unknown_0x0896fde0,
            "unknown_0x5f98ada3": self.unknown_0x5f98ada3,
            "unknown_0xc3230652": self.unknown_0xc3230652,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x47C836C5: ("blinking_enabled", structs.decode_BIG_bool_),
    0x9B131110: ("unknown_0x9b131110", structs.decode_BIG_f),
    0xA5A6D998: ("unknown_0xa5a6d998", structs.decode_BIG_f),
    0xD9F6253B: ("unknown_0xd9f6253b", structs.decode_BIG_l),
    0x0896FDE0: ("unknown_0x0896fde0", structs.decode_BIG_f),
    0x5F98ADA3: ("unknown_0x5f98ada3", structs.decode_BIG_f),
    0xC3230652: ("unknown_0xc3230652", structs.decode_BIG_f),
}
