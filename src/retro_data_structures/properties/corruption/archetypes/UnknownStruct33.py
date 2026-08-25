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

    class UnknownStruct33Json(typing_extensions.TypedDict):
        initial_morph_time: float
        unknown_0x41ed6a42: float
        unknown_0x420da002: float
        unknown_0xa2675081: float
        unknown_0x413aee5b: float
        unknown_0x9fe347b5: float
        unknown_0xc8ed17f6: float
        cloak_time: float
        decloak_time: float
        unknown_0x587fa387: float
        unknown_0x3e9ac5f3: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x45161109,
    0x41ED6A42,
    0x420DA002,
    0xA2675081,
    0x413AEE5B,
    0x9FE347B5,
    0xC8ED17F6,
    0x388BC31F,
    0x4319C840,
    0x587FA387,
    0x3E9AC5F3,
)


@dataclasses.dataclass()
class UnknownStruct33(BaseProperty):
    initial_morph_time: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x45161109, original_name="InitialMorphTime"),
        },
    )
    unknown_0x41ed6a42: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x41ED6A42, original_name="Unknown"),
        },
    )
    unknown_0x420da002: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x420DA002, original_name="Unknown"),
        },
    )
    unknown_0xa2675081: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA2675081, original_name="Unknown"),
        },
    )
    unknown_0x413aee5b: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x413AEE5B, original_name="Unknown"),
        },
    )
    unknown_0x9fe347b5: float = dataclasses.field(
        default=9.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9FE347B5, original_name="Unknown"),
        },
    )
    unknown_0xc8ed17f6: float = dataclasses.field(
        default=11.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC8ED17F6, original_name="Unknown"),
        },
    )
    cloak_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x388BC31F, original_name="CloakTime"),
        },
    )
    decloak_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4319C840, original_name="DecloakTime"),
        },
    )
    unknown_0x587fa387: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x587FA387, original_name="Unknown"),
        },
    )
    unknown_0x3e9ac5f3: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3E9AC5F3, original_name="Unknown"),
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
        if property_count != 11:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(110))
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"E\x16\x11\t")  # 0x45161109
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_morph_time))

        data.write(b"A\xedjB")  # 0x41ed6a42
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x41ed6a42))

        data.write(b"B\r\xa0\x02")  # 0x420da002
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x420da002))

        data.write(b"\xa2gP\x81")  # 0xa2675081
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa2675081))

        data.write(b"A:\xee[")  # 0x413aee5b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x413aee5b))

        data.write(b"\x9f\xe3G\xb5")  # 0x9fe347b5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9fe347b5))

        data.write(b"\xc8\xed\x17\xf6")  # 0xc8ed17f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc8ed17f6))

        data.write(b"8\x8b\xc3\x1f")  # 0x388bc31f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cloak_time))

        data.write(b"C\x19\xc8@")  # 0x4319c840
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.decloak_time))

        data.write(b"X\x7f\xa3\x87")  # 0x587fa387
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x587fa387))

        data.write(b">\x9a\xc5\xf3")  # 0x3e9ac5f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3e9ac5f3))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct33Json", data)
        return cls(
            initial_morph_time=json_data["initial_morph_time"],
            unknown_0x41ed6a42=json_data["unknown_0x41ed6a42"],
            unknown_0x420da002=json_data["unknown_0x420da002"],
            unknown_0xa2675081=json_data["unknown_0xa2675081"],
            unknown_0x413aee5b=json_data["unknown_0x413aee5b"],
            unknown_0x9fe347b5=json_data["unknown_0x9fe347b5"],
            unknown_0xc8ed17f6=json_data["unknown_0xc8ed17f6"],
            cloak_time=json_data["cloak_time"],
            decloak_time=json_data["decloak_time"],
            unknown_0x587fa387=json_data["unknown_0x587fa387"],
            unknown_0x3e9ac5f3=json_data["unknown_0x3e9ac5f3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "initial_morph_time": self.initial_morph_time,
            "unknown_0x41ed6a42": self.unknown_0x41ed6a42,
            "unknown_0x420da002": self.unknown_0x420da002,
            "unknown_0xa2675081": self.unknown_0xa2675081,
            "unknown_0x413aee5b": self.unknown_0x413aee5b,
            "unknown_0x9fe347b5": self.unknown_0x9fe347b5,
            "unknown_0xc8ed17f6": self.unknown_0xc8ed17f6,
            "cloak_time": self.cloak_time,
            "decloak_time": self.decloak_time,
            "unknown_0x587fa387": self.unknown_0x587fa387,
            "unknown_0x3e9ac5f3": self.unknown_0x3e9ac5f3,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x45161109: ("initial_morph_time", structs.decode_BIG_f),
    0x41ED6A42: ("unknown_0x41ed6a42", structs.decode_BIG_f),
    0x420DA002: ("unknown_0x420da002", structs.decode_BIG_f),
    0xA2675081: ("unknown_0xa2675081", structs.decode_BIG_f),
    0x413AEE5B: ("unknown_0x413aee5b", structs.decode_BIG_f),
    0x9FE347B5: ("unknown_0x9fe347b5", structs.decode_BIG_f),
    0xC8ED17F6: ("unknown_0xc8ed17f6", structs.decode_BIG_f),
    0x388BC31F: ("cloak_time", structs.decode_BIG_f),
    0x4319C840: ("decloak_time", structs.decode_BIG_f),
    0x587FA387: ("unknown_0x587fa387", structs.decode_BIG_f),
    0x3E9AC5F3: ("unknown_0x3e9ac5f3", structs.decode_BIG_f),
}
