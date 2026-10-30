from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

from retro_data_structures import json_util

if TYPE_CHECKING:
    from collections.abc import Callable

    from retro_data_structures.game_check import Game
    from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass(frozen=True)
class FieldReflection[T]:
    """
    How a field looks in one game.

    - `type`: the Python type of the value: a class for structs and enums, `list` for arrays, `int` for assets.
    - `id`: the property id, or the position in Prime.
    - `original_name`: the name in the template, if it's different from the name of the field.
    - `from_json`, `to_json`: JSON conversion of the value, for the game.
    """

    type: type[T]
    id: int
    original_name: str | None
    from_json: Callable[[json_util.JsonValue], T] = json_util.identity  # type: ignore[assignment]
    to_json: Callable[[T], json_util.JsonValue] = json_util.identity  # type: ignore[assignment]


def get_reflection(cls: type[BaseProperty], game: Game) -> dict[str, FieldReflection]:
    """
    Get the FieldReflection of every field that exists in the game.
    The `asset_types` of a field, if it has them, are in `dataclasses.fields(cls)[i].metadata["asset_types"]`.

    :param cls: A class with fields declared by `prop()`, or a hand-written one with a `FieldReflection` in the
        "reflection" metadata of its fields (which is used as is, for every game).
    :param game: The game.
    :return: A dict of field name, to a FieldReflection
    """
    result: dict[str, FieldReflection] = {}
    for field in dataclasses.fields(cls):
        layouts = field.metadata.get("layout")
        if layouts is not None:
            layout = layouts.get(game)
            if layout is None:
                continue
            codec = layout.codec
            locator = layout.id if layout.id is not None else layout.position
            if not isinstance(locator, int):
                locator = locator.name if locator is not None else 0
            result[field.name] = FieldReflection(
                type=codec.py_type,
                id=locator,
                original_name=layout.original_name,
                from_json=lambda data, codec=codec: codec.from_json(data, game),  # type: ignore[misc]
                to_json=lambda value, codec=codec: codec.to_json(value, game),  # type: ignore[misc]
            )
        elif "reflection" in field.metadata:
            result[field.name] = field.metadata["reflection"]
    return result
