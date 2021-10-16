from construct import Struct, Int32ub, PrefixedArray

from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import AssetIdCorrect, Game

Dependency = Struct("asset_type" / FourCC, "asset_id" / AssetIdCorrect)

DGRP = PrefixedArray(Int32ub, Dependency)


def dependencies_for(obj, target_game: Game):
    for dependency in obj:
        yield dependency.asset_type, dependency.asset_id
