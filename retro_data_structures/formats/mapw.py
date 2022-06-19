import typing

import construct

from retro_data_structures.base_resource import BaseResource, AssetType, Dependency, AssetId
from retro_data_structures.game_check import Game, AssetIdCorrect

MAPW = construct.Struct(
    _magic=construct.Const(0xDEADF00D, construct.Int32ub),
    _version=construct.Const(1, construct.Int32ub),
    area_map=construct.PrefixedArray(construct.Int32ub, AssetIdCorrect)
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
        yield from dependencies_for(self.raw, self.target_game)

    def get_mapa_id(self, index: int) -> AssetId:
        return self.raw.area_map[index]
