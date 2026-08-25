# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class LayerSwitchJson(typing_extensions.TypedDict):
        area_id: int
        index: int


@dataclasses.dataclass()
class LayerSwitch(BaseProperty):
    area_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["MREA"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000000, original_name="AreaID"),
        },
    )
    index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Index"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        area_id = structs.BIG_L.unpack(data.read(4))[0]
        index = structs.BIG_l.unpack(data.read(4))[0]
        return cls(area_id, index)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_L.pack(self.area_id))
        data.write(structs.BIG_l.pack(self.index))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LayerSwitchJson", data)
        return cls(
            area_id=json_data["area_id"],
            index=json_data["index"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "area_id": self.area_id,
            "index": self.index,
        }
