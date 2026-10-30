"""Sentinels and errors of the merged property classes. See `retro_data_structures.properties.codec`."""

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game


class _Sentinel:
    """A singleton marker. Survives copy, deepcopy and pickle as the very same object."""

    __slots__ = ("_name",)

    def __init__(self, name: str):
        self._name = name

    def __repr__(self) -> str:
        return self._name

    def __copy__(self) -> _Sentinel:
        return self

    def __deepcopy__(self, memo: object) -> _Sentinel:
        return self

    def __reduce__(self) -> str:
        return self._name

    def __bool__(self) -> bool:
        raise TypeError(f"{self._name} has no truth value")


UNSET: typing.Any = _Sentinel("UNSET")
"""The value of a field whose default depends on the game, while the object has no game."""

ABSENT: typing.Any = _Sentinel("ABSENT")
"""The value of a field that the object's game does not have."""


class PropertyError(Exception):
    """Base class of every error raised by the merged property classes."""


class GameNotSet(PropertyError, AttributeError):
    """A field with a game-dependent default was read on an object that has no game."""


class FieldNotInGame(PropertyError, AttributeError):
    """A field was read or written, but the object's game doesn't have it."""


class GameMismatch(PropertyError, ValueError):
    """An object was given a game, but it already has a different one."""


class ClassNotInGame(PropertyError, ValueError):
    """A class that isn't defined in the given game was given that game."""


class MemberNotInGame(PropertyError, ValueError):
    """An enum or flags member was translated to a game that doesn't have it."""

    def __init__(self, enum: type, member: str, game: Game):
        super().__init__(f"{enum.__name__}.{member} does not exist in {game.name}")
        self.enum = enum
        self.member = member
        self.game = game
