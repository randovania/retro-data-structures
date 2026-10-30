"""Tests of every generated class: it can be created, and round-trips through bytes and JSON in every game it is in."""

from __future__ import annotations

import importlib
import pkgutil
import typing

import pytest

from retro_data_structures.properties import archetypes, objects
from retro_data_structures.properties.base_property import BaseStruct

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game


def _all_classes() -> list[type[BaseStruct]]:
    result: dict[str, type[BaseStruct]] = {}
    for package in (objects, archetypes):
        for info in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{package.__name__}.{info.name}")
            for value in vars(module).values():
                if isinstance(value, type) and issubclass(value, BaseStruct) and value.__module__ == module.__name__:
                    result[value.__name__] = value
    return [result[name] for name in sorted(result)]


ALL_CLASSES = _all_classes()
CASES = [
    pytest.param(cls, game, id=f"{cls.__name__}-{game.name}")
    for cls in ALL_CLASSES
    for game in sorted(cls.games(), key=lambda g: g.value)
]


def test_there_are_classes() -> None:
    assert len(ALL_CLASSES) > 400


def test_object_tables_find_every_object() -> None:
    for cls in ALL_CLASSES:
        if not cls._is_object:
            continue
        for game, object_type in cls._object_types.items():  # type: ignore[attr-defined]
            assert objects.get_object(game, object_type) is cls


@pytest.mark.parametrize(("cls", "game"), CASES)
def test_create_and_round_trip(cls: type[BaseStruct], game: Game) -> None:
    obj = cls(game=game)
    try:
        data = obj.to_bytes(game)
    except NotImplementedError:
        pytest.skip("Stored by the owner of the class in this game")

    decoded = cls.from_bytes(data, game)
    assert decoded == obj
    assert decoded.to_bytes(game) == data

    as_json = typing.cast("typing.Any", decoded).to_json()
    assert cls.from_json(as_json) == decoded


@pytest.mark.parametrize("cls", ALL_CLASSES, ids=lambda c: c.__name__)
def test_create_without_game(cls: type[BaseStruct]) -> None:
    obj = cls()
    assert obj.game is None
