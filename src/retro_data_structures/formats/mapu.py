from __future__ import annotations

import typing

from construct import Const, Construct, Int32ub, PrefixedArray, Struct

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AssetId32, Color4f, String, Transform4f
from retro_data_structures.game_check import Game

World = Struct(
    "name" / String,
    "mlvl" / AssetId32,
    "transform" / Transform4f,
    "hexagon_transforms" / PrefixedArray(Int32ub, Transform4f),
    "color" / Color4f,
)

MAPU = Struct(
    "_magic" / Const(0xABCDEF01, Int32ub),
    "_version" / Const(1, Int32ub),
    "hexagon_mapa" / AssetId32,
    "worlds" / PrefixedArray(Int32ub, World),
)


class Mapu(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "MAPU"

    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        if target_game > Game.ECHOES:
            raise ValueError(f"{target_game} does not support MAPU!")
        return MAPU

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from self.asset_manager.get_dependencies_for_asset(self.raw.hexagon_mapa)
