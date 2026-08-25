# Generated file
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties.base_property import BaseProperty

from .AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game


@dataclasses.dataclass()
class AnimationParameters(BaseProperty):
    ancs: AssetId = dataclasses.field(metadata={"asset_types": ["ANCS"]}, default=default_asset_id)
    character_index: int = 0
    initial_anim: int = 0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        if game.uses_asset_id_32:
            format_specifier = "L"
            known_size = 12
        else:
            format_specifier = "Q"
            known_size = 16

        return cls(*struct.unpack(f"{game.struct_endianness}{format_specifier}LL", data.read(known_size)))

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        if game.uses_asset_id_32:
            format_specifier = "L"
        else:
            format_specifier = "Q"

        data.write(
            struct.pack(
                f"{game.struct_endianness}{format_specifier}LL",
                self.ancs,
                self.character_index,
                self.initial_anim,
            )
        )

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        data_json = typing.cast("dict[str, int]", data)
        return cls(data_json["ancs"], data_json["character_index"], data_json["initial_anim"])

    def to_json(self) -> json_util.JsonObject:
        return {
            "ancs": self.ancs,
            "character_index": self.character_index,
            "initial_anim": self.initial_anim,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
        yield from asset_manager.get_dependencies_for_ancs(self.ancs, self.character_index)
