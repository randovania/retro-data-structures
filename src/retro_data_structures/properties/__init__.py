from __future__ import annotations

from typing import TYPE_CHECKING, Literal, overload

from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.properties.base_property import BaseObjectType, BaseProperty


@overload
def get_game_object(game: Literal[Game.PRIME], four_cc: int) -> type[BaseObjectType]: ...
@overload
def get_game_object(game: Literal[Game.ECHOES, Game.CORRUPTION], four_cc: str) -> type[BaseObjectType]: ...
@overload
def get_game_object(game: Literal[Game.PRIME_REMASTER], four_cc: int) -> type[BaseProperty]: ...
@overload
def get_game_object(game: Game, four_cc: str | int) -> type[BaseProperty]: ...


def get_game_object(game: Game, four_cc: str | int) -> type[BaseObjectType] | type[BaseProperty]:
    if game == Game.PRIME:
        from .prime import objects as prime_objects

        return prime_objects.get_object(four_cc)
    elif game == Game.ECHOES:
        from .echoes import objects as echoes_objects

        return echoes_objects.get_object(four_cc)
    elif game == Game.CORRUPTION:
        from .corruption import objects as corruption_objects

        return corruption_objects.get_object(four_cc)
    elif game == Game.PRIME_REMASTER:
        from .prime_remastered import objects as prime_remastered_objects

        return prime_remastered_objects.get_object(four_cc)
    else:
        raise ValueError(f"Unknown Game: {game}")
