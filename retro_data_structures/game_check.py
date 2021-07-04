"""
For checking which game is being parsed
"""
from enum import Enum

from construct import IfThenElse

from retro_data_structures import common_types


class Game(Enum):
    PRIME = 1
    ECHOES = 2
    CORRUPTION = 3

    @property
    def uses_lzo(self):
        return self in {Game.ECHOES, Game.CORRUPTION}


def get_current_game(ctx):
    result = ctx["_params"]["target_game"]
    if not isinstance(result, Game):
        raise ValueError(f"build/parse didn't set a valid target_game. Expected `Game`, got {result}")

    return result


def is_prime1(ctx):
    return get_current_game(ctx) == Game.PRIME


def is_prime2(ctx):
    return get_current_game(ctx) == Game.ECHOES


def is_prime3(ctx):
    return get_current_game(ctx) == Game.CORRUPTION


def current_game_at_most(target: Game):
    def result(ctx):
        return get_current_game(ctx).value <= target.value

    return result


def current_game_at_least(target: Game):
    def result(ctx):
        return get_current_game(ctx).value >= target.value

    return result


def uses_lzo(ctx):
    return get_current_game(ctx).uses_lzo


uses_asset_id_32 = current_game_at_most(Game.ECHOES)
AssetIdCorrect = IfThenElse(uses_asset_id_32, common_types.AssetId32, common_types.AssetId64)
ObjectTagCorrect = IfThenElse(uses_asset_id_32, common_types.ObjectTag_32, common_types.ObjectTag_64)
