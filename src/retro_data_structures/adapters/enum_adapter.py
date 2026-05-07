from __future__ import annotations

import enum
import typing

import construct

E = typing.TypeVar("E", bound=enum.IntEnum)


class EnumAdapter[T: enum.IntEnum](construct.Adapter):
    def __init__(self, enum_class: type[T], subcon=construct.Int32ub):
        super().__init__(construct.Enum(subcon, enum_class))
        self._enum_class = enum_class

    def _decode(self, obj: str, context, path) -> T:
        return self._enum_class[obj]

    def _encode(self, obj: T, context, path) -> str:
        return obj.name
