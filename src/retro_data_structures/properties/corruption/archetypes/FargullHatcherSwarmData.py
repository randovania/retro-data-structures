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

    class FargullHatcherSwarmDataJson(typing_extensions.TypedDict):
        unknown_0x3109e1c7: float
        unknown_0xf73a8baa: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x3109E1C7, 0xF73A8BAA)


@dataclasses.dataclass()
class FargullHatcherSwarmData(BaseProperty):
    unknown_0x3109e1c7: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3109E1C7, original_name="Unknown"),
        },
    )
    unknown_0xf73a8baa: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF73A8BAA, original_name="Unknown"),
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
            _FAST_FORMAT = struct.Struct(">LHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(20))
        assert (dec[0], dec[3]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"1\t\xe1\xc7")  # 0x3109e1c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3109e1c7))

        data.write(b"\xf7:\x8b\xaa")  # 0xf73a8baa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf73a8baa))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FargullHatcherSwarmDataJson", data)
        return cls(
            unknown_0x3109e1c7=json_data["unknown_0x3109e1c7"],
            unknown_0xf73a8baa=json_data["unknown_0xf73a8baa"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x3109e1c7": self.unknown_0x3109e1c7,
            "unknown_0xf73a8baa": self.unknown_0xf73a8baa,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x3109E1C7: ("unknown_0x3109e1c7", structs.decode_BIG_f),
    0xF73A8BAA: ("unknown_0xf73a8baa", structs.decode_BIG_f),
}
