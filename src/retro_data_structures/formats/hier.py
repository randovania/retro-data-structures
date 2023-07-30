from __future__ import annotations

import typing

from construct import Byte, Const, Construct, GreedyRange, Int32ub, PrefixedArray, Struct

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AssetId32, String

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game

HIER = Struct(
    magic=Const(b"HIER"),
    entries=PrefixedArray(
        Int32ub,
        Struct(
            string_table_id=AssetId32,
            name=String,
            scan_id=AssetId32,
            parent_id=Int32ub,
        ),
    ),
    junk=GreedyRange(Byte),
)


class Hier(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return HIER

    @classmethod
    def resource_type(cls) -> AssetType:
        return "DUMB"

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        for entry in self.raw.entries:
            yield from self.asset_manager.get_dependencies_for_asset(entry.string_table_id)
