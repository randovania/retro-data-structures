# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GhorStructAJson(typing_extensions.TypedDict):
        undamaged: int
        damaged: int
        locator: str
        damage_effect: str


@dataclasses.dataclass()
class GhorStructA(BaseProperty):
    undamaged: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF8BEDB63, original_name="Undamaged"),
        },
    )
    damaged: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1D5CCC2D, original_name="Damaged"),
        },
    )
    locator: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x8A660FE5, original_name="Locator"),
        },
    )
    damage_effect: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x5F137AC5, original_name="DamageEffect"),
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
        if property_count != 4:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8BEDB63
        undamaged = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D5CCC2D
        damaged = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A660FE5
        locator = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F137AC5
        damage_effect = data.read(property_size)[:-1].decode("utf-8")

        return cls(undamaged, damaged, locator, damage_effect)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\xf8\xbe\xdbc")  # 0xf8bedb63
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.undamaged))

        data.write(b"\x1d\\\xcc-")  # 0x1d5ccc2d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.damaged))

        data.write(b"\x8af\x0f\xe5")  # 0x8a660fe5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.locator.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"_\x13z\xc5")  # 0x5f137ac5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.damage_effect.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorStructAJson", data)
        return cls(
            undamaged=json_data["undamaged"],
            damaged=json_data["damaged"],
            locator=json_data["locator"],
            damage_effect=json_data["damage_effect"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "undamaged": self.undamaged,
            "damaged": self.damaged,
            "locator": self.locator,
            "damage_effect": self.damage_effect,
        }


def _decode_locator(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_damage_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF8BEDB63: ("undamaged", structs.decode_BIG_Q),
    0x1D5CCC2D: ("damaged", structs.decode_BIG_Q),
    0x8A660FE5: ("locator", _decode_locator),
    0x5F137AC5: ("damage_effect", _decode_damage_effect),
}
