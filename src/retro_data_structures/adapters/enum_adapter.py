from __future__ import annotations

import enum
import typing

import construct

E = typing.TypeVar("E", bound=enum.IntEnum)


class EnumAdapter[T: enum.IntEnum](construct.Adapter):
    def __init__(
        self,
        enum_class: type[T],
        subcon: construct.Construct = construct.Int32ub,
        *,
        strict: bool = False,
    ):
        super().__init__(construct.Enum(subcon, enum_class))
        self._enum_class = enum_class
        self.strict = strict

    def _handle_invalid[InvalidT](self, obj: InvalidT) -> InvalidT:
        if self.strict:
            raise ValueError(f"Invalid value for {self._enum_class.__name__}: {obj}")
        else:
            return obj

    def _decode(self, obj: str | int, context: construct.Container, path: str) -> T | int:
        try:
            return self._enum_class[obj]
        except KeyError:
            return self._handle_invalid(obj)

    def _encode(self, obj: T | int, context: construct.Container, path: str) -> str | int:
        try:
            return self._enum_class(obj).name
        except ValueError:
            return self._handle_invalid(obj)
