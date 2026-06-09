from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar

import construct

if TYPE_CHECKING:
    from collections.abc import Callable

    from construct import Container


class FieldsMixin:
    _raw: Container
    _fields: ClassVar[tuple[tuple[str, Field], ...]] = ()

    def __init__(self, raw: Container):
        self._raw = raw

    def __init_subclass__(cls, default_field_location: FieldLocation = (), **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

        for name, field in cls._fields:
            if field.location is None:
                field.location = default_field_location

    def __repr__(self) -> str:
        field_reprs = [f"{name}={getattr(self, name)}" for name, field in self.__class__._fields]
        return f"<{self.__class__.__qualname__} {' '.join(field_reprs)}>"

    def __str__(self) -> str:
        field_strs = [f"    {name} = {str(getattr(self, name))}" for name, field in self.__class__._fields]
        lines = [f"{self.__class__.__qualname__}:", *field_strs]
        return "\n".join(lines)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False

        for field_name, field in self.__class__._fields:
            if getattr(self, field_name, None) != getattr(other, field_name, None):
                return False

        return True

    __hash__ = None  # type: ignore[assignment]


type FieldLocation = tuple[str, ...]


class Field[T]:
    """
    Descriptor class to use to quickly define fields that take from `_raw`
    """

    def __init__(
        self,
        location: FieldLocation | None = None,
        factory: Callable[[Any], T] | None = None,
    ):
        self.location = location
        self.factory = factory

    def __set_name__(self, owner: type[FieldsMixin], name: str) -> None:
        self.name = name

        owner._fields += ((name, self),)

    def _data(self, obj: FieldsMixin) -> Container:
        data = obj._raw
        assert self.location is not None
        for loc in self.location:
            data = getattr(data, loc)
        return data

    def __get__(self, obj: FieldsMixin | None, owner: type[FieldsMixin] | None = None) -> T:
        if obj is None:
            raise AttributeError(
                f"Cannot access field '{self.name}' on class {owner.__name__} (must be accessed on an instance)"
            )
        result = getattr(self._data(obj), self.name)
        if self.factory is not None:
            result = self.factory(result)
        return result

    def __set__(self, obj: FieldsMixin, value: T) -> None:
        setattr(self._data(obj), self.name, value)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} location='{self.location}' factory='{self.factory}'>"


def field[T](
    type_hint: type[T],
    *,
    location: FieldLocation | None = None,
    factory: Callable[[Any], T] | None = None,
) -> Field[T]:
    return Field[T](location, factory)


class WrapperClassAdapter[T: FieldsMixin](construct.Adapter):
    def __init__(self, subcon: construct.Construct, wrapper_cls: type[T]):
        super().__init__(subcon)
        self.wrapper_cls = wrapper_cls

    def _decode(self, obj: construct.Container, context: construct.Container, path: str) -> T:
        return self.wrapper_cls(obj)

    def _encode(self, obj: T, context: construct.Container, path: str) -> construct.Container:
        return obj._raw
