from __future__ import annotations

from typing import TypeAlias

JsonObject: TypeAlias = dict[str, "JsonValue"]
JsonArray: TypeAlias = list["JsonValue"]
JsonValue: TypeAlias = str | int | float | JsonObject | JsonArray | None


def identity(obj: JsonValue) -> JsonValue:
    """For use when you need a to_json function, but the value is already JsonValue."""
    return obj
