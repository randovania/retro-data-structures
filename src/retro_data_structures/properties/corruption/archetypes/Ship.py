# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryItem import PlayerInventoryItem
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ShipJson(typing_extensions.TypedDict):
        ship_missile: json_util.JsonObject
        ship_grapple: bool


@dataclasses.dataclass()
class Ship(BaseProperty):
    ship_missile: PlayerInventoryItem = dataclasses.field(
        default_factory=PlayerInventoryItem,
        metadata={
            "reflection": FieldReflection[PlayerInventoryItem](
                PlayerInventoryItem,
                id=0x398A3608,
                original_name="ShipMissile",
                from_json=PlayerInventoryItem.from_json,
                to_json=PlayerInventoryItem.to_json,
            ),
        },
    )
    ship_grapple: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF9AEE109, original_name="ShipGrapple"),
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x398A3608
        ship_missile = PlayerInventoryItem.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9AEE109
        ship_grapple = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(ship_missile, ship_grapple)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"9\x8a6\x08")  # 0x398a3608
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ship_missile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf9\xae\xe1\t")  # 0xf9aee109
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ship_grapple))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShipJson", data)
        return cls(
            ship_missile=PlayerInventoryItem.from_json(json_data["ship_missile"]),
            ship_grapple=json_data["ship_grapple"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "ship_missile": self.ship_missile.to_json(),
            "ship_grapple": self.ship_grapple,
        }


def _decode_ship_missile(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryItem:
    return PlayerInventoryItem.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x398A3608: ("ship_missile", _decode_ship_missile),
    0xF9AEE109: ("ship_grapple", structs.decode_BIG_bool_),
}
