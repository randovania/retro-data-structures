from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TypeAlias, TypeVar

JsonObject: TypeAlias = Mapping[str, "JsonValue"]
JsonArray: TypeAlias = Sequence["JsonValue"]
JsonValue: TypeAlias = str | int | float | JsonObject | JsonArray | None

JsonValueT = TypeVar("JsonValueT", str, int, float, JsonObject, JsonArray, None)


def identity(obj: JsonValueT) -> JsonValueT:
    """For use when you need a to_json function, but the value is already JsonValue."""
    return obj
