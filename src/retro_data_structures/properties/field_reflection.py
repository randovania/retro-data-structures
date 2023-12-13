from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, Generic, TypeVar

from retro_data_structures import json_util

if TYPE_CHECKING:
    from collections.abc import Callable

    from retro_data_structures.properties.base_property import BaseProperty

T = TypeVar("T")


@dataclasses.dataclass(frozen=True)
class FieldReflection(Generic[T]):
    type: type[T]
    id: int
    original_name: str | None
    from_json: Callable[[json_util.JsonValue], T] = json_util.identity
    to_json: Callable[[T], json_util.JsonValue] = json_util.identity


def get_reflection(cls: type[BaseProperty]) -> dict[str, FieldReflection]:
    """
    Get all FieldReflection objects for a given property.
    :param cls:
    :return: A dict of field name, to a FieldDetails
    """
    return {
        field.name: field.metadata["reflection"] for field in dataclasses.fields(cls) if "reflection" in field.metadata
    }
