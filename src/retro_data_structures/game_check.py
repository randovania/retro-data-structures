"""
For checking which game is being parsed
"""

from __future__ import annotations

import typing
import uuid
from enum import Enum
from typing import Any

from construct.core import IfThenElse

from retro_data_structures import common_types
from retro_data_structures.base_resource import Dependency
from retro_data_structures.crc import crc32, crc64

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    import construct

    from retro_data_structures.base_resource import AssetId


class Game(Enum):
    PRIME = 1
    ECHOES = 2
    CORRUPTION = 3
    PRIME_REMASTER = 10

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    @property
    def uses_asset_id_32(self):
        return self <= Game.ECHOES

    @property
    def uses_asset_id_64(self):
        return self == Game.CORRUPTION

    @property
    def uses_guid_as_asset_id(self):
        return self == Game.PRIME_REMASTER

    @property
    def uses_lzo(self):
        return self in {Game.ECHOES, Game.CORRUPTION}

    @property
    def invalid_asset_id(self) -> int | uuid.UUID:
        if self.uses_asset_id_32:
            return (1 << 32) - 1
        elif self.uses_asset_id_64:
            return (1 << 64) - 1
        elif self.uses_guid_as_asset_id:
            return uuid.UUID(int=0)
        else:
            raise NotImplementedError

    def hash_asset_id(self, asset_name: str) -> AssetId:
        if self.uses_guid_as_asset_id:
            raise NotImplementedError
        if self.uses_asset_id_64:
            return crc64(asset_name)
        if self.uses_asset_id_32:
            return crc32(asset_name)

    def is_valid_asset_id(self, asset_id: int | uuid.UUID) -> bool:
        if self <= Game.ECHOES and asset_id == 0:
            return False
        return asset_id != self.invalid_asset_id

    @property
    def mlvl_dependencies_to_ignore(self) -> tuple[AssetId]:
        if self == Game.ECHOES:
            # Textures/Misc/VisorSteamQtr.TXTR
            return (0x7B2EA5B1,)
        return ()

    def audio_group_dependencies(self):
        if self == Game.ECHOES:
            # audio_groups_single_player_DGRP
            yield 0x31CB5ADB
            # audio_groups_multi_player_DGRP
            # yield 0xEE0CC360 # FIXME

    def special_ancs_dependencies(self, ancs: AssetId):
        if self == Game.ECHOES:
            if ancs == 0xC043D342:
                # every gun animation needs these i guess
                yield Dependency("TXTR", 0x9E6F9531, False)
                yield Dependency("TXTR", 0xCEA098FE, False)
                yield Dependency("TXTR", 0x607638EA, False)
                yield Dependency("TXTR", 0x578E51B8, False)
                yield Dependency("TXTR", 0x1E7B6C64, False)

            if ancs == 0x2E980BF2:
                # samus ANCS from Hive Chamber A
                yield Dependency("ANIM", 0x711A038F, True)
                yield Dependency("ANIM", 0x1A9CCDD5, True)


def get_current_game(ctx) -> Game:
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


def current_game_at_most(target: Game) -> Callable[[Any], bool]:
    def result(ctx):
        return get_current_game(ctx) <= target

    return result


def current_game_at_least(target: Game) -> Callable[[Any], bool]:
    def result(ctx):
        return get_current_game(ctx) >= target

    return result


class CurrentGameCheck(IfThenElse):
    def __init__(self, target: Game, subcon1, subcon2):
        super().__init__(current_game_at_least(target), subcon1, subcon2)
        self.target_game = target

    def _emitparse(self, code: construct.CodeGen):
        code.append("from retro_data_structures import game_check")
        return (
            f"(({self.thensubcon._compileparse(code)}) "
            f"if (game_check.get_current_game(this) >= game_check.Game.{self.target_game.name}) "
            f"else ({self.elsesubcon._compileparse(code)}))"
        )

    def _emitbuild(self, code: construct.CodeGen):
        code.append("from retro_data_structures import game_check")
        return (
            f"(({self.thensubcon._compilebuild(code)})"
            f" if (game_check.get_current_game(this) >= game_check.Game.{self.target_game.name})"
            f" else ({self.elsesubcon._compilebuild(code)}))"
        )


def current_game_at_least_else(target: Game, subcon1, subcon2) -> IfThenElse:
    return CurrentGameCheck(target, subcon1, subcon2)


def uses_asset_id_32(ctx):
    return get_current_game(ctx).uses_asset_id_32


def uses_lzo(ctx):
    return get_current_game(ctx).uses_lzo


AssetIdCorrect = CurrentGameCheck(Game.CORRUPTION, common_types.AssetId64, common_types.AssetId32)
ObjectTagCorrect = CurrentGameCheck(Game.CORRUPTION, common_types.ObjectTag_64, common_types.ObjectTag_32)
