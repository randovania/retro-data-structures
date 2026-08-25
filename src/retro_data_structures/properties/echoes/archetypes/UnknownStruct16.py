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

    class UnknownStruct16Json(typing_extensions.TypedDict):
        unknown_0x7ee77018: float
        unknown_0xbfb7ca5c: float
        unknown_0x1e2debc6: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x7EE77018, 0xBFB7CA5C, 0x1E2DEBC6)


@dataclasses.dataclass()
class UnknownStruct16(BaseProperty):
    unknown_0x7ee77018: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7EE77018, original_name="Unknown"),
        },
    )
    unknown_0xbfb7ca5c: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBFB7CA5C, original_name="Unknown"),
        },
    )
    unknown_0x1e2debc6: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E2DEBC6, original_name="Unknown"),
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
        if property_count != 3:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(30))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"~\xe7p\x18")  # 0x7ee77018
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7ee77018))

        data.write(b"\xbf\xb7\xca\\")  # 0xbfb7ca5c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbfb7ca5c))

        data.write(b"\x1e-\xeb\xc6")  # 0x1e2debc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1e2debc6))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct16Json", data)
        return cls(
            unknown_0x7ee77018=json_data["unknown_0x7ee77018"],
            unknown_0xbfb7ca5c=json_data["unknown_0xbfb7ca5c"],
            unknown_0x1e2debc6=json_data["unknown_0x1e2debc6"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x7ee77018": self.unknown_0x7ee77018,
            "unknown_0xbfb7ca5c": self.unknown_0xbfb7ca5c,
            "unknown_0x1e2debc6": self.unknown_0x1e2debc6,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7EE77018: ("unknown_0x7ee77018", structs.decode_BIG_f),
    0xBFB7CA5C: ("unknown_0xbfb7ca5c", structs.decode_BIG_f),
    0x1E2DEBC6: ("unknown_0x1e2debc6", structs.decode_BIG_f),
}
