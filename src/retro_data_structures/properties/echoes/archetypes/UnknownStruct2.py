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

    class UnknownStruct2Json(typing_extensions.TypedDict):
        enabled: bool
        chance: float
        modifier: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x29C77D27, 0x7A7B330E, 0xED2D546F)


@dataclasses.dataclass()
class UnknownStruct2(BaseProperty):
    enabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x29C77D27, original_name="Enabled"),
        },
    )
    chance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7A7B330E, original_name="Chance"),
        },
    )
    modifier: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED2D546F, original_name="Modifier"),
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
            _FAST_FORMAT = struct.Struct(">LH?LHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(27))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b")\xc7}'")  # 0x29c77d27
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.enabled))

        data.write(b"z{3\x0e")  # 0x7a7b330e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.chance))

        data.write(b"\xed-To")  # 0xed2d546f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.modifier))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct2Json", data)
        return cls(
            enabled=json_data["enabled"],
            chance=json_data["chance"],
            modifier=json_data["modifier"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "enabled": self.enabled,
            "chance": self.chance,
            "modifier": self.modifier,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x29C77D27: ("enabled", structs.decode_BIG_bool_),
    0x7A7B330E: ("chance", structs.decode_BIG_f),
    0xED2D546F: ("modifier", structs.decode_BIG_f),
}
