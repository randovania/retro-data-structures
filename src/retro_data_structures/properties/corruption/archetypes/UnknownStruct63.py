# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct63Json(typing_extensions.TypedDict):
        unknown_0x04131a2a: int
        unknown_0x868cfe92: bool
        unknown_0xf1943b5a: bool
        unknown_0x44bf1dc9: int
        unknown_0x7c538ed3: int
        unknown_0xfcd2a1a0: int
        unknown_0x1aec3e02: int
        unknown_0xe0e4573d: int
        unknown_0x21103ec1: int
        unknown_0xc7c06435: int


class Unknown(enum.IntEnum):
    Unknown1 = 2868300453
    Unknown2 = 881720149
    Unknown3 = 1464639200

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x4131A2A,
    0x868CFE92,
    0xF1943B5A,
    0x44BF1DC9,
    0x7C538ED3,
    0xFCD2A1A0,
    0x1AEC3E02,
    0xE0E4573D,
    0x21103EC1,
    0xC7C06435,
)


@dataclasses.dataclass()
class UnknownStruct63(BaseProperty):
    unknown_0x04131a2a: Unknown = dataclasses.field(
        default=Unknown.Unknown1,
        metadata={
            "reflection": FieldReflection[Unknown](
                Unknown, id=0x04131A2A, original_name="Unknown", from_json=Unknown.from_json, to_json=Unknown.to_json
            ),
        },
    )
    unknown_0x868cfe92: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x868CFE92, original_name="Unknown"),
        },
    )
    unknown_0xf1943b5a: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF1943B5A, original_name="Unknown"),
        },
    )
    unknown_0x44bf1dc9: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x44BF1DC9, original_name="Unknown"),
        },
    )
    unknown_0x7c538ed3: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7C538ED3, original_name="Unknown"),
        },
    )
    unknown_0xfcd2a1a0: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFCD2A1A0, original_name="Unknown"),
        },
    )
    unknown_0x1aec3e02: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1AEC3E02, original_name="Unknown"),
        },
    )
    unknown_0xe0e4573d: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE0E4573D, original_name="Unknown"),
        },
    )
    unknown_0x21103ec1: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x21103EC1, original_name="Unknown"),
        },
    )
    unknown_0xc7c06435: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC7C06435, original_name="Unknown"),
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
        if property_count != 10:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHLLH?LH?LHlLHlLHlLHlLHlLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(94))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27]) == _FAST_IDS
        return cls(
            Unknown(dec[2]),
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"\x04\x13\x1a*")  # 0x4131a2a
        data.write(b"\x00\x04")  # size
        self.unknown_0x04131a2a.to_stream(data, game)

        data.write(b"\x86\x8c\xfe\x92")  # 0x868cfe92
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x868cfe92))

        data.write(b"\xf1\x94;Z")  # 0xf1943b5a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf1943b5a))

        data.write(b"D\xbf\x1d\xc9")  # 0x44bf1dc9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x44bf1dc9))

        data.write(b"|S\x8e\xd3")  # 0x7c538ed3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7c538ed3))

        data.write(b"\xfc\xd2\xa1\xa0")  # 0xfcd2a1a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xfcd2a1a0))

        data.write(b"\x1a\xec>\x02")  # 0x1aec3e02
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x1aec3e02))

        data.write(b"\xe0\xe4W=")  # 0xe0e4573d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe0e4573d))

        data.write(b"!\x10>\xc1")  # 0x21103ec1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x21103ec1))

        data.write(b"\xc7\xc0d5")  # 0xc7c06435
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc7c06435))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct63Json", data)
        return cls(
            unknown_0x04131a2a=Unknown.from_json(json_data["unknown_0x04131a2a"]),
            unknown_0x868cfe92=json_data["unknown_0x868cfe92"],
            unknown_0xf1943b5a=json_data["unknown_0xf1943b5a"],
            unknown_0x44bf1dc9=json_data["unknown_0x44bf1dc9"],
            unknown_0x7c538ed3=json_data["unknown_0x7c538ed3"],
            unknown_0xfcd2a1a0=json_data["unknown_0xfcd2a1a0"],
            unknown_0x1aec3e02=json_data["unknown_0x1aec3e02"],
            unknown_0xe0e4573d=json_data["unknown_0xe0e4573d"],
            unknown_0x21103ec1=json_data["unknown_0x21103ec1"],
            unknown_0xc7c06435=json_data["unknown_0xc7c06435"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x04131a2a": self.unknown_0x04131a2a.to_json(),
            "unknown_0x868cfe92": self.unknown_0x868cfe92,
            "unknown_0xf1943b5a": self.unknown_0xf1943b5a,
            "unknown_0x44bf1dc9": self.unknown_0x44bf1dc9,
            "unknown_0x7c538ed3": self.unknown_0x7c538ed3,
            "unknown_0xfcd2a1a0": self.unknown_0xfcd2a1a0,
            "unknown_0x1aec3e02": self.unknown_0x1aec3e02,
            "unknown_0xe0e4573d": self.unknown_0xe0e4573d,
            "unknown_0x21103ec1": self.unknown_0x21103ec1,
            "unknown_0xc7c06435": self.unknown_0xc7c06435,
        }


def _decode_unknown_0x04131a2a(data: typing.BinaryIO, game: Game, property_size: int) -> Unknown:
    return Unknown.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x04131A2A: ("unknown_0x04131a2a", _decode_unknown_0x04131a2a),
    0x868CFE92: ("unknown_0x868cfe92", structs.decode_BIG_bool_),
    0xF1943B5A: ("unknown_0xf1943b5a", structs.decode_BIG_bool_),
    0x44BF1DC9: ("unknown_0x44bf1dc9", structs.decode_BIG_l),
    0x7C538ED3: ("unknown_0x7c538ed3", structs.decode_BIG_l),
    0xFCD2A1A0: ("unknown_0xfcd2a1a0", structs.decode_BIG_l),
    0x1AEC3E02: ("unknown_0x1aec3e02", structs.decode_BIG_l),
    0xE0E4573D: ("unknown_0xe0e4573d", structs.decode_BIG_l),
    0x21103EC1: ("unknown_0x21103ec1", structs.decode_BIG_l),
    0xC7C06435: ("unknown_0xc7c06435", structs.decode_BIG_l),
}
