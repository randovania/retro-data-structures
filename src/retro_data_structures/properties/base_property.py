from __future__ import annotations

import base64
import copy
import dataclasses
import io
import typing
from abc import ABC

from retro_data_structures.game_check import Game
from retro_data_structures.properties.codec.layout import CookMode
from retro_data_structures.properties.codec.plan import ClassInfo, Plan, class_info, install_descriptors
from retro_data_structures.properties.errors import (
    ABSENT,
    UNSET,
    ClassNotInGame,
    FieldNotInGame,
    GameMismatch,
    GameNotSet,
)

if typing.TYPE_CHECKING:
    from collections.abc import Collection, Iterator, Mapping

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.properties.archetypes.EditorProperties import EditorProperties


@dataclasses.dataclass()
class BaseProperty:
    """
    The interface of everything that can be read from and written to a property stream.

    Hand-written, game-neutral types like `Vector`, `Color` and `Spline` extend this and implement the methods.
    The classes generated for the templates extend `BaseStruct`, which implements them.
    """

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing.Self:
        raise NotImplementedError

    @classmethod
    def from_bytes(cls, data: bytes, game: Game) -> typing.Self:
        stream = io.BytesIO(data)
        return cls.from_stream(stream, game, len(data))

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        raise NotImplementedError

    def to_bytes(self, game: Game) -> bytes:
        stream = io.BytesIO()
        self.to_stream(stream, game)
        return stream.getvalue()

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing.Self:
        raise NotImplementedError

    def to_json(self) -> json_util.JsonValue:
        raise NotImplementedError

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return iter(())


def values_equal(a: typing.Any, b: typing.Any) -> bool:
    """Equality that doesn't look at the game of the structs. Used to tell if a value is a default."""
    if isinstance(a, BaseStruct):
        return a._values_equal(b)
    if isinstance(a, list):
        return isinstance(b, list) and len(a) == len(b) and all(values_equal(x, y) for x, y in zip(a, b, strict=True))
    return bool(a == b)


class _GameProperty:
    """`BaseStruct.game`. The game is kept in `__dict__["_game"]`, and only set once the object is initialized."""

    def __get__(self, obj: typing.Any, owner: type | None = None) -> Game | None:
        if obj is None:
            return None
        return obj.__dict__.get("_game")

    def __set__(self, obj: BaseStruct, value: Game | None) -> None:
        d = obj.__dict__
        if "_game" in d:
            obj.set_game(value)
        elif value is not None:
            d["_pending_game"] = value  # dataclass __init__ sets it before the fields. See __post_init__


def _struct_eq(self: BaseStruct, other: object) -> bool:
    if other.__class__ is not self.__class__:
        return NotImplemented
    a, b = self.__dict__, other.__dict__
    if a == b:
        return True
    if "_wire" not in a and "_wire" not in b:
        return False
    # Which properties an object was read with doesn't make it a different value
    return {k: v for k, v in a.items() if k != "_wire"} == {k: v for k, v in b.items() if k != "_wire"}


def _without_presence(value: typing.Any) -> typing.Any:
    """A copy of the value where the structs in it have forgotten which properties they were read with."""
    if isinstance(value, BaseStruct):
        new = object.__new__(type(value))
        new.__dict__ = {k: _without_presence(v) for k, v in value.__dict__.items() if k != "_wire"}
        return new
    if isinstance(value, list):
        return [_without_presence(v) for v in value]
    return value


def _struct_repr(self: BaseStruct) -> str:
    d = self.__dict__
    parts = [f"{k}={v!r}" for k, v in d.items() if k[0] != "_"]
    game = d.get("_game")
    if game is not None:
        parts.append(f"game={game}")
    return f"{type(self).__name__}({', '.join(parts)})"


@dataclasses.dataclass()
class BaseStruct(BaseProperty):
    """
    Base of the classes generated from the templates: one class for all games, with the fields declared by `prop()`.
    See `retro_data_structures.properties.codec` for how a class is written and how it behaves.

    Class keywords:

    - `atomic`: games where the struct is stored without its property count (or ids, outside Prime).
    - `modules`: for each game, the names of the modules a script object needs.
    - `games`: games the class exists in, when no field says so.
    """

    game: Game | None = dataclasses.field(default=None, kw_only=True)

    __hash__: typing.ClassVar[None] = None  # type: ignore[assignment]
    _atomic_games: typing.ClassVar[frozenset[Game]] = frozenset()
    _declared_games: typing.ClassVar[frozenset[Game]] = frozenset()
    _modules: typing.ClassVar[Mapping[Game, list[str]]] = {}
    _is_object: typing.ClassVar[bool] = False

    def __init_subclass__(
        cls,
        *,
        atomic: Collection[Game] = (),
        modules: Mapping[Game, list[str]] | None = None,
        games: Collection[Game] = (),
        **kwargs: typing.Any,
    ) -> None:
        super().__init_subclass__(**kwargs)
        cls._atomic_games = frozenset(atomic)
        cls._declared_games = frozenset(games)
        cls._modules = dict(modules) if modules else {}
        # dataclass() doesn't replace methods that are in the class
        if "__eq__" not in cls.__dict__:
            cls.__eq__ = _struct_eq  # type: ignore[method-assign,assignment]
        if "__repr__" not in cls.__dict__:
            cls.__repr__ = _struct_repr  # type: ignore[assignment]

    # Instances

    def __post_init__(self) -> None:
        cls = type(self)
        if "_class_info" not in cls.__dict__:
            _prepare(cls)
        d = self.__dict__
        pending = d.pop("_pending_game", None)
        d["_game"] = None
        if pending is not None:
            self.set_game(pending)

    __eq__ = _struct_eq
    __repr__ = _struct_repr

    def _values_equal(self, other: object) -> bool:
        if other.__class__ is not self.__class__:
            return False
        b = other.__dict__
        for key, value in self.__dict__.items():
            if key in ("_game", "_wire"):
                continue
            if key not in b or not values_equal(value, b[key]):
                return False
        return True

    # Game

    @classmethod
    def _info(cls) -> ClassInfo:
        if "_class_info" not in cls.__dict__:
            _prepare(cls)
        return class_info(cls)

    @classmethod
    def _plan(cls, game: Game) -> Plan:
        plans = cls.__dict__.get("_plans")
        if plans is None:
            cls._info()
            plans = cls._plans = {}  # type: ignore[attr-defined]
        plan = plans.get(game)
        if plan is None:
            plan = plans[game] = Plan(cls, game)
        return plan

    @classmethod
    def games(cls) -> frozenset[Game]:
        """The games this class exists in."""
        return cls._info().games

    def set_game(self, game: Game | None) -> None:
        """
        Give the object, and the structs in it, a game. Fields with a default that depends on the game get the default
        of the game, and fields that the game doesn't have become ABSENT.

        Does nothing if the object already has that game.

        :raises GameMismatch: if the object has a different game.
        :raises ClassNotInGame: if the class doesn't exist in the game.
        :raises FieldNotInGame: if a field that the game doesn't have has a value that is not a default.
        """
        d = self.__dict__
        current = d["_game"]
        if game is None or current is game:
            return
        if current is not None:
            raise GameMismatch(f"{type(self).__name__} is already in {current.name}, can't be in {game.name}")

        info = self._info()
        if info.fields and game not in info.games:
            raise ClassNotInGame(f"{type(self).__name__} does not exist in {game.name}")

        for field in info.fields.values():
            if game not in field.layouts:
                value = d[field.name]
                if value is not UNSET and value is not ABSENT and not field.is_default(value):
                    raise FieldNotInGame(
                        f"{type(self).__name__}.{field.name} does not exist in {game.name}, "
                        f"but was given the value {value!r}"
                    )

        for field in info.fields.values():
            layout = field.layouts.get(game)
            if layout is None:
                d[field.name] = ABSENT
                continue
            value = d[field.name]
            if value is UNSET or value is ABSENT:
                d[field.name] = field.make_default(game)
            elif layout.codec.binds:
                layout.codec.bind(value, game)
        d["_game"] = game

    def to_game(self, game: Game) -> typing.Self:
        """
        A copy of the object for another game.

        Fields that both games have are copied, and structs are converted too. Fields that only the new game has get
        its defaults. Enum members are kept, if the new game has them.

        :raises FieldNotInGame: if a field that only the current game has holds a value that is not a default.
        :raises MemberNotInGame: if an enum member doesn't exist in the new game.
        """
        info = self._info()
        if info.fields and game not in info.games:
            raise ClassNotInGame(f"{type(self).__name__} does not exist in {game.name}")

        source = self.game
        d = self.__dict__
        result: dict[str, typing.Any] = {}
        for field in info.fields.values():
            value = d[field.name]
            layout = field.layouts.get(game)
            if layout is None:
                if value is not UNSET and value is not ABSENT and not field.is_default(value):
                    raise FieldNotInGame(
                        f"{type(self).__name__}.{field.name} does not exist in {game.name}, but has the value {value!r}"
                    )
                result[field.name] = ABSENT
            elif value is UNSET or value is ABSENT:
                result[field.name] = field.make_default(game)
            else:
                result[field.name] = layout.codec.convert(value, source, game)
        for extra in info.extras:
            result[extra.name] = copy.deepcopy(d[extra.name])
        if info.has_unknown_properties:
            result["unknown_properties"] = copy.deepcopy(d["unknown_properties"])
        result["_game"] = game

        new = object.__new__(type(self))
        new.__dict__ = result
        return new

    def _require_game(self, game: Game | None = None) -> Game:
        """The game of the object, binding it to the given one if it doesn't have one yet."""
        current = self.__dict__["_game"]
        if game is None:
            if current is None:
                raise GameNotSet(f"{type(self).__name__} needs a game: pass one or call set_game()")
            return current
        if current is not game:
            self.set_game(game)
        return game

    # Codec

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing.Self:
        return cls._plan(game).decode(data, size, None)

    def to_stream(self, data: typing.BinaryIO, game: Game | None = None, cook: CookMode = CookMode.PRESERVE) -> None:
        """
        Write the object. If it has no game yet, it gets `game`.

        :param cook: see `CookMode`: whether optional properties that the object was read with are written back.
        """
        game = self._require_game(game)
        obj = self if cook is CookMode.PRESERVE else _without_presence(self)
        self._plan(game).encode(obj, data, None)

    def to_bytes(self, game: Game | None = None, cook: CookMode = CookMode.PRESERVE) -> bytes:
        stream = io.BytesIO()
        self.to_stream(stream, game, cook)
        return stream.getvalue()

    def _to_json_inner(self, game: Game) -> dict[str, typing.Any]:
        info = self._info()
        d = self.__dict__
        result = {
            field.name: field.layouts[game].codec.to_json(d[field.name], game) for field in info.by_game.get(game, [])
        }
        if info.has_unknown_properties:
            result["unknown_properties"] = {
                hex(property_id): base64.b64encode(blob).decode("utf-8")
                for property_id, blob in d["unknown_properties"].items()
            }
        return result

    def to_json(self) -> json_util.JsonObject:
        """JSON of the object, including the game. Needs the object to have a game."""
        game = self._require_game()
        return {"game": game.name, **self._to_json_inner(game)}

    @classmethod
    def _from_json_inner(cls, data: json_util.JsonValue, game: Game) -> typing.Self:
        info = cls._info()
        json_data = typing.cast("dict[str, typing.Any]", data)
        result: dict[str, typing.Any] = {}
        for field in info.fields.values():
            layout = field.layouts.get(game)
            if layout is None:
                result[field.name] = ABSENT
            elif field.name in json_data:
                result[field.name] = layout.codec.from_json(json_data[field.name], game)
            else:
                result[field.name] = field.make_default(game)
        for extra in info.extras:
            result[extra.name] = extra.make_default()
        if info.has_unknown_properties:
            result["unknown_properties"] = {
                int(property_id, 16): base64.b64decode(blob)
                for property_id, blob in json_data.get("unknown_properties", {}).items()
            }
        result["_game"] = game
        obj = object.__new__(cls)
        obj.__dict__ = result
        return obj

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing.Self:
        """Create an object from the JSON of `to_json`. The JSON has the game."""
        game = Game[typing.cast("dict[str, str]", data)["game"]]
        return cls._from_json_inner(data, game)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        game = self._require_game()
        info = self._info()
        if info.has_unknown_properties:
            return
        d = self.__dict__
        for field in info.by_game.get(game, []):
            layout = field.layouts[game]
            try:
                yield from layout.codec.dependencies(d[field.name], game, asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for {type(self).__name__}.{field.name} "
                    f"({getattr(layout.codec.py_type, '__name__', layout.codec.py_type)}): {e}"
                ) from e


# `game` is a property, that the dataclass doesn't know about
BaseStruct.game = _GameProperty()  # type: ignore[assignment]


def _prepare(cls: type[BaseStruct]) -> None:
    """Called when the first instance of a class is created, after the dataclass is complete."""
    info = class_info(cls)
    install_descriptors(cls, info)


class BaseObjectType(BaseStruct, ABC):
    """
    Base of the script objects, tweaks and scans.

    Class keywords: `object_types`, the type of the object in each game: an int in Prime, and a four character string
    in Echoes and Corruption. Plus those of `BaseStruct`.
    """

    _is_object: typing.ClassVar[bool] = True
    _object_types: typing.ClassVar[Mapping[Game, str | int]] = {}

    def __init_subclass__(cls, *, object_types: Mapping[Game, str | int] | None = None, **kwargs: typing.Any) -> None:
        games = set(kwargs.pop("games", ()))
        if object_types:
            games.update(object_types)
        super().__init_subclass__(games=games, **kwargs)
        cls._object_types = dict(object_types) if object_types else {}

    @classmethod
    def object_type(cls, game: Game) -> str | int:
        try:
            return cls._object_types[game]
        except KeyError:
            raise ClassNotInGame(f"{cls.__name__} does not exist in {game.name}") from None

    @classmethod
    def modules(cls, game: Game) -> list[str]:
        return list(cls._modules.get(game, []))

    def get_name(self) -> str:
        info = self._info()
        if "editor_properties" in info.fields:
            return self.editor_properties.name  # type: ignore[attr-defined]
        if "name" in info.fields:
            return self.name
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        info = self._info()
        if "editor_properties" in info.fields:
            self.editor_properties.name = name  # type: ignore[attr-defined]
        elif "name" in info.fields:
            self.name = name
        else:
            raise RuntimeError(f"{self.__class__.__name__} does not have name")


@typing.runtime_checkable
class ObjectWithEditorProperties(typing.Protocol):
    editor_properties: EditorProperties
