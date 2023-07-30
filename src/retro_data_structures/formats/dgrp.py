from __future__ import annotations

import typing

import construct
from construct import Int32ub, PrefixedArray, Struct

from retro_data_structures import common_types
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.game_check import CurrentGameCheck, Game


def construct_dep(asset_id_format):
    return Struct("asset_type" / common_types.FourCC, "asset_id" / asset_id_format)


DGRP = CurrentGameCheck(
    Game.CORRUPTION,
    PrefixedArray(Int32ub, construct_dep(common_types.AssetId64)),
    PrefixedArray(Int32ub, construct_dep(common_types.AssetId32)),
).compile()


def legacy_dependencies(obj, target_game: Game):
    for dependency in obj:
        yield dependency.asset_type, dependency.asset_id


class Dgrp(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "DGRP"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return DGRP

    @property
    def direct_dependencies(self) -> typing.Iterator[Dependency]:
        for dep in self.raw:
            yield Dependency(dep.asset_type, dep.asset_id, False)

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        for dependency in self.raw:
            yield from self.asset_manager.get_dependencies_for_asset(dependency.asset_id)
