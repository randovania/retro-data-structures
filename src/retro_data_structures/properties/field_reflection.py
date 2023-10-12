from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, Generic, TypeVar

from retro_data_structures import json_util

if TYPE_CHECKING:
    from collections.abc import Callable

T = TypeVar("T")


@dataclasses.dataclass(frozen=True)
class FieldReflection(Generic[T]):
    id: int
    original_name: str | None
    from_json: Callable[[json_util.JsonValue], T] = json_util.identity
    to_json: Callable[[T], json_util.JsonValue] = json_util.identity
