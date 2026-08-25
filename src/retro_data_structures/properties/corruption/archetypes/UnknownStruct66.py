# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct66Json(typing_extensions.TypedDict):
        world: int
        area: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x31EC14BC, 0xE0C17804)


@dataclasses.dataclass()
class UnknownStruct66(BaseProperty):
    world: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["MLVL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x31EC14BC, original_name="World"),
        },
    )
    area: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["MREA"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE0C17804, original_name="Area"),
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
            _FAST_FORMAT = struct.Struct(">LHQLHQ")

        dec = _FAST_FORMAT.unpack(data.read(28))
        assert (dec[0], dec[3]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"1\xec\x14\xbc")  # 0x31ec14bc
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.world))

        data.write(b"\xe0\xc1x\x04")  # 0xe0c17804
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.area))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct66Json", data)
        return cls(
            world=json_data["world"],
            area=json_data["area"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "world": self.world,
            "area": self.area,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x31EC14BC: ("world", structs.decode_BIG_Q),
    0xE0C17804: ("area", structs.decode_BIG_Q),
}
