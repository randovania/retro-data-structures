# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.SavedStateID import SavedStateID
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class LayerIDJson(typing_extensions.TypedDict):
        area_id: int
        layer_id: json_util.JsonObject


@dataclasses.dataclass()
class LayerID(BaseProperty):
    area_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000000, original_name="AreaId"),
        },
    )
    layer_id: SavedStateID = dataclasses.field(
        default_factory=SavedStateID,
        metadata={
            "reflection": FieldReflection[SavedStateID](
                SavedStateID,
                id=0x00000001,
                original_name="LayerId",
                from_json=SavedStateID.from_json,
                to_json=SavedStateID.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        area_id = structs.BIG_Q.unpack(data.read(8))[0]
        layer_id = SavedStateID.from_stream(data, game, property_size)
        return cls(area_id, layer_id)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_Q.pack(self.area_id))
        self.layer_id.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LayerIDJson", data)
        return cls(
            area_id=json_data["area_id"],
            layer_id=SavedStateID.from_json(json_data["layer_id"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "area_id": self.area_id,
            "layer_id": self.layer_id.to_json(),
        }
