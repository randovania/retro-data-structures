from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TypeVar

JsonObject = Mapping[str, "JsonValue"]
JsonArray = Sequence["JsonValue"]
JsonValue = str | int | float | JsonObject | JsonArray | None

JsonValueT = TypeVar("JsonValueT", str, int, float, JsonObject, JsonArray, None)


def identity[T: (str, int, float, JsonObject, JsonArray, None)](obj: T) -> T:
    """For use when you need a to_json function, but the value is already JsonValue."""
    return obj
