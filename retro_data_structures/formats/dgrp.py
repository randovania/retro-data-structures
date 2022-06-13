import typing

import construct
from construct import Struct, PrefixedArray, Int32ub

from retro_data_structures.base_resource import AssetId, BaseResource, AssetType, Dependency
from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import AssetIdCorrect
from retro_data_structures.game_check import Game

ConstructDependency = Struct("asset_type" / FourCC, "asset_id" / AssetIdCorrect)

DGRP = PrefixedArray(Int32ub, ConstructDependency)


def dependencies_for(obj, target_game: Game):
    for dependency in obj:
        yield dependency.asset_type, dependency.asset_id


class Dgrp(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "DGRP"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return DGRP

    def dependencies_for(self) -> typing.Iterator[AssetId]:
        yield from self.dependencies_to_asset_ids(dependencies_for(self.raw, self.target_game))

    def mlvl_dependencies_for(self, dep_manager) -> typing.Iterator[AssetId]:
        yield from []
