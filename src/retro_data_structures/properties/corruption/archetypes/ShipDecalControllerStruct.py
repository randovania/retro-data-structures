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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ShipDecalControllerStructJson(typing_extensions.TypedDict):
        save_game: int
        texture_asset: int


class SaveGame(enum.IntEnum):
    Unknown1 = 718950382
    Unknown2 = 769513116
    Unknown3 = 3263590420
    Unknown4 = 57119807
    Unknown5 = 3218965678
    Unknown6 = 634958821
    Unknown7 = 3878045253
    Unknown8 = 17817487
    Unknown9 = 1589020689

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
_FAST_IDS = (0x77EDD0F1, 0x2F11C14F)


@dataclasses.dataclass()
class ShipDecalControllerStruct(BaseProperty):
    save_game: SaveGame = dataclasses.field(
        default=SaveGame.Unknown1,
        metadata={
            "reflection": FieldReflection[SaveGame](
                SaveGame,
                id=0x77EDD0F1,
                original_name="SaveGame",
                from_json=SaveGame.from_json,
                to_json=SaveGame.to_json,
            ),
        },
    )
    texture_asset: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2F11C14F, original_name="TextureAsset"),
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
            _FAST_FORMAT = struct.Struct(">LHLLHQ")

        dec = _FAST_FORMAT.unpack(data.read(24))
        assert (dec[0], dec[3]) == _FAST_IDS
        return cls(
            SaveGame(dec[2]),
            dec[5],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"w\xed\xd0\xf1")  # 0x77edd0f1
        data.write(b"\x00\x04")  # size
        self.save_game.to_stream(data, game)

        data.write(b"/\x11\xc1O")  # 0x2f11c14f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.texture_asset))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShipDecalControllerStructJson", data)
        return cls(
            save_game=SaveGame.from_json(json_data["save_game"]),
            texture_asset=json_data["texture_asset"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "save_game": self.save_game.to_json(),
            "texture_asset": self.texture_asset,
        }


def _decode_save_game(data: typing.BinaryIO, game: Game, property_size: int) -> SaveGame:
    return SaveGame.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x77EDD0F1: ("save_game", _decode_save_game),
    0x2F11C14F: ("texture_asset", structs.decode_BIG_Q),
}
