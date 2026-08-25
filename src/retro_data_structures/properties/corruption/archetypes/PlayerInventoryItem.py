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

    class PlayerInventoryItemJson(typing_extensions.TypedDict):
        amount: int
        capacity: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x94AF1445, 0x6DC59F13)


@dataclasses.dataclass()
class PlayerInventoryItem(BaseProperty):
    amount: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x94AF1445, original_name="Amount"),
        },
    )
    capacity: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6DC59F13, original_name="Capacity"),
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
            _FAST_FORMAT = struct.Struct(">LHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(20))
        assert (dec[0], dec[3]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\x94\xaf\x14E")  # 0x94af1445
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.amount))

        data.write(b"m\xc5\x9f\x13")  # 0x6dc59f13
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.capacity))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerInventoryItemJson", data)
        return cls(
            amount=json_data["amount"],
            capacity=json_data["capacity"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "amount": self.amount,
            "capacity": self.capacity,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x94AF1445: ("amount", structs.decode_BIG_l),
    0x6DC59F13: ("capacity", structs.decode_BIG_l),
}
