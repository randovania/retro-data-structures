from __future__ import annotations

from typing import TYPE_CHECKING, Literal, overload

if TYPE_CHECKING:
    from retro_data_structures.game_check import Game
    from retro_data_structures.properties.base_property import BaseObjectType


@overload
def get_game_object(game: Literal[Game.PRIME], four_cc: int) -> type[BaseObjectType]: ...
@overload
def get_game_object(game: Literal[Game.ECHOES, Game.CORRUPTION], four_cc: str) -> type[BaseObjectType]: ...
@overload
def get_game_object(game: Game, four_cc: str | int) -> type[BaseObjectType]: ...


def get_game_object(game: Game, four_cc: str | int) -> type[BaseObjectType]:
    from retro_data_structures.properties.objects import get_object

    return get_object(game, four_cc)
