from __future__ import annotations

import typing

import construct

from retro_data_structures.base_resource import AssetId, AssetType, BaseResource, Dependency
from retro_data_structures.game_check import AssetIdCorrect, Game

MAPW = construct.Struct(
    _magic=construct.Const(0xDEADF00D, construct.Int32ub),
    _version=construct.Const(1, construct.Int32ub),
    area_map=construct.PrefixedArray(construct.Int32ub, AssetIdCorrect),
)


def dependencies_for(obj, target_game):
    for item in obj.area_map:
        yield "MAPA", item


class Mapw(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "MAPW"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return MAPW

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        for item in self.raw.area_map:
            yield from self.asset_manager.get_dependencies_for_asset(item)

    def get_mapa_id(self, index: int) -> AssetId:
        return self.raw.area_map[index]

    @property
    def mapa_ids(self) -> typing.Iterator[AssetId]:
        yield from self.raw.area_map
