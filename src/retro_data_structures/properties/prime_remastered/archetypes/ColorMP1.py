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

    class ColorMP1Json(typing_extensions.TypedDict):
        r: float
        g: float
        b: float
        a: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x110889D1, 0x8A7AFF22, 0x2A5349E9, 0xE364C93A)


@dataclasses.dataclass()
class ColorMP1(BaseProperty):
    r: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x110889D1, original_name="R"),
        },
    )
    g: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A7AFF22, original_name="G"),
        },
    )
    b: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2A5349E9, original_name="B"),
        },
    )
    a: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE364C93A, original_name="A"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.LITTLE_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
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
        if property_count != 4:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct("<LHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(40))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x04\x00")  # 4 properties

        data.write(b"\xd1\x89\x08\x11")  # 0x110889d1
        data.write(b"\x04\x00")  # size
        data.write(structs.LITTLE_f.pack(self.r))

        data.write(b'"\xffz\x8a')  # 0x8a7aff22
        data.write(b"\x04\x00")  # size
        data.write(structs.LITTLE_f.pack(self.g))

        data.write(b"\xe9IS*")  # 0x2a5349e9
        data.write(b"\x04\x00")  # size
        data.write(structs.LITTLE_f.pack(self.b))

        data.write(b":\xc9d\xe3")  # 0xe364c93a
        data.write(b"\x04\x00")  # size
        data.write(structs.LITTLE_f.pack(self.a))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ColorMP1Json", data)
        return cls(
            r=json_data["r"],
            g=json_data["g"],
            b=json_data["b"],
            a=json_data["a"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "r": self.r,
            "g": self.g,
            "b": self.b,
            "a": self.a,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x110889D1: ("r", structs.decode_LITTLE_f),
    0x8A7AFF22: ("g", structs.decode_LITTLE_f),
    0x2A5349E9: ("b", structs.decode_LITTLE_f),
    0xE364C93A: ("a", structs.decode_LITTLE_f),
}
