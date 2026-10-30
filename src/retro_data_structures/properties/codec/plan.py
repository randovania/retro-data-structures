"""
Class information and compiled decoders/encoders of `BaseStruct`.

For each (class, game), a `Plan` is built the first time it's needed: the fields of the game in the order they're
stored, and a decoder and an encoder compiled with `exec`, the way `dataclasses` builds `__init__`. Consecutive
fields with a fixed size share one `struct.Struct`. A plan is cached on the class.

Nothing here is meant to be used directly. See `retro_data_structures.properties.base_property`.
"""

from __future__ import annotations

import copy
import dataclasses
import functools
import struct
import sys
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.codec import codecs
from retro_data_structures.properties.codec.layout import ID_TAGGED_GAMES, Cook, FieldLayout, PrimeEditor
from retro_data_structures.properties.errors import ABSENT, UNSET, FieldNotInGame, GameNotSet

if typing.TYPE_CHECKING:
    from collections.abc import Callable

    from retro_data_structures.properties.codec.codecs import Codec


@dataclasses.dataclass
class FieldInfo:
    """A field of a class, in every game."""

    name: str
    layouts: dict[Game, FieldLayout]
    index: int
    agree: bool
    """True if all the games have the same default. Otherwise the field starts out as UNSET."""

    @property
    def games(self) -> frozenset[Game]:
        return frozenset(self.layouts)

    def make_default(self, game: Game) -> typing.Any:
        """A new default value for the game. Structs in it have the game."""
        layout = self.layouts[game]
        value = layout.default.make()
        if layout.codec.binds:
            layout.codec.bind(value, game)
        return value

    def is_default(self, value: typing.Any) -> bool:
        """True if the value is the default of any game."""
        for layout in self.layouts.values():
            if layout.codec.equal(value, layout.default.make()):
                return True
        return False


@dataclasses.dataclass
class ExtraField:
    """A dataclass field that has no layout. It isn't stored in any game."""

    name: str
    make_default: Callable[[], typing.Any]


@dataclasses.dataclass
class ClassInfo:
    cls: type
    fields: dict[str, FieldInfo]
    extras: list[ExtraField]
    has_unknown_properties: bool
    games: frozenset[Game]
    by_game: dict[Game, list[FieldInfo]]

    @classmethod
    def create(cls, struct_cls: type) -> ClassInfo:
        fields: dict[str, FieldInfo] = {}
        extras: list[ExtraField] = []
        has_unknown = False
        for f in dataclasses.fields(struct_cls):
            if f.name == "game":
                continue
            if f.metadata.get("unknown_properties"):
                has_unknown = True
                continue
            layouts = f.metadata.get("layout")
            if layouts is None:
                if f.default_factory is not dataclasses.MISSING:
                    extras.append(ExtraField(f.name, f.default_factory))
                else:
                    extras.append(ExtraField(f.name, lambda v=f.default: v))  # type: ignore[misc]
                continue
            keys = {layout.default.key for layout in layouts.values()}
            fields[f.name] = FieldInfo(f.name, layouts, len(fields), len(keys) == 1)

        games = set(getattr(struct_cls, "_declared_games", ()))
        for info in fields.values():
            games.update(info.layouts)
        by_game = {
            game: [info for info in fields.values() if game in info.layouts]
            for game in sorted(games, key=lambda g: g.value)
        }
        return cls(struct_cls, fields, extras, has_unknown, frozenset(games), by_game)


def class_info(cls: type) -> ClassInfo:
    info = cls.__dict__.get("_class_info")
    if info is None:
        info = ClassInfo.create(cls)
        cls._class_info = info  # type: ignore[attr-defined]
    return info


# Descriptors


class _BindingField:
    """
    Data descriptor for fields that bind the structs that are assigned to them, and refuse values once the object has a
    game that doesn't have the field. The value lives in the instance's `__dict__`, and reading doesn't go through
    this class, so reading is as fast as for any attribute.
    """

    def __init__(self, name: str, info: FieldInfo, binds: bool):
        self.name = name
        self.games = info.games
        self.info = info
        self.binds = binds

    def __set__(self, obj: typing.Any, value: typing.Any) -> None:
        d = obj.__dict__
        game = d.get("_game")
        if game is not None:
            if game not in self.games:
                if value is not ABSENT:
                    raise FieldNotInGame(f"{type(obj).__name__}.{self.name} does not exist in {game.name}")
            elif value is UNSET:
                value = self.info.make_default(game)
            elif self.binds:
                self.info.layouts[game].codec.bind(value, game)
        d[self.name] = value


class _GuardedField(_BindingField):
    """Like `_BindingField`, but reading also raises for the fields that are UNSET or ABSENT."""

    def __get__(self, obj: typing.Any, owner: type | None = None) -> typing.Any:
        if obj is None:
            return self
        try:
            value = obj.__dict__[self.name]
        except KeyError:
            raise AttributeError(self.name) from None
        if value is UNSET or value is ABSENT:
            # dataclasses.replace and asdict read every field, and have to be able to copy the sentinels.
            if sys._getframe(1).f_globals.get("__name__") == "dataclasses":
                return value
            self._raise(obj, value)
        return value

    def _raise(self, obj: typing.Any, value: typing.Any) -> typing.NoReturn:
        cls_name = type(obj).__name__
        if value is ABSENT:
            game = obj.__dict__["_game"]
            raise FieldNotInGame(f"{cls_name}.{self.name} does not exist in {game.name}")

        games = ", ".join(sorted(g.name for g in self.games))
        raise GameNotSet(
            f"{cls_name}.{self.name} has a default that depends on the game ({games}), and {cls_name} has no game. "
            "Give it a game with set_game(), or assign the field first."
        )


def install_descriptors(cls: type, info: ClassInfo) -> None:
    for name, field in info.fields.items():
        partial = not field.games >= info.games
        can_be_unset = not field.agree
        binds = any(layout.codec.binds for layout in field.layouts.values())
        if partial or can_be_unset:
            setattr(cls, name, _GuardedField(name, field, binds))
        elif binds:
            setattr(cls, name, _BindingField(name, field, binds))


# Plans


@dataclasses.dataclass
class Item:
    """A value stored in the class, in a game."""

    index: int
    field: FieldInfo
    layout: FieldLayout
    codec: Codec
    position: int | None = None
    slot: str | None = None
    """For the properties of Prime's EditorProperties: name, position, rotation, scale or active."""

    @property
    def var(self) -> str:
        return f"x{self.index}"


class _BoundBuilder:
    """Makes instances of a class in a game without going through `__init__` and `set_game`. Same as `Plan.decode`."""

    def __init__(self, cls: type, game: Game):
        cls._info()  # type: ignore[attr-defined]  # prepares the class: descriptors and class info
        info = class_info(cls)
        self.cls = cls
        self.game = game
        self.makers: list[tuple[str, Callable[[], typing.Any] | None]] = []
        for field in info.fields.values():
            layout = field.layouts.get(game)
            self.makers.append((field.name, None if layout is None else _default_maker(layout, game)))
        self.extras = [(extra.name, extra.make_default) for extra in info.extras]
        self.has_unknown = info.has_unknown_properties

    def make(self, values: dict[str, typing.Any]) -> typing.Any:
        result: dict[str, typing.Any] = {}
        for name, maker in self.makers:
            if maker is None:
                result[name] = ABSENT
            elif name in values:
                result[name] = values[name]
            else:
                result[name] = maker()
        for name, make_default in self.extras:
            result[name] = make_default()
        if self.has_unknown:
            result["unknown_properties"] = {}
        result["_game"] = self.game
        obj: typing.Any = object.__new__(self.cls)
        obj.__dict__ = result
        return obj


def _default_maker(layout: FieldLayout, game: Game) -> Callable[[], typing.Any]:
    make = layout.default.make
    codec = layout.codec
    if not codec.binds:
        return make

    def make_bound() -> typing.Any:
        value = make()
        codec.bind(value, game)
        return value

    return make_bound


class EditorHelper:
    """Builds and splits the EditorProperties of a Prime object, which are stored as separate properties."""

    def __init__(self, editor_cls: type, editor: PrimeEditor, game: Game):
        self.editor_cls = editor_cls
        self.editor = editor
        transform_field = class_info(editor_cls).fields["transform"]
        self.transform_cls: type = next(iter(transform_field.layouts.values())).codec.py_type
        self._make_transform = _BoundBuilder(self.transform_cls, game).make
        self._make_editor = _BoundBuilder(editor_cls, game).make

    def build(self, game: Game, name: str, active: bool | None = None, **transform: typing.Any) -> typing.Any:
        """`transform` has the position, rotation and scale that the object has. The others stay at their defaults."""
        values = {"name": name, "transform": self._make_transform(transform)}
        if active is not None:
            values["active"] = active
        return self._make_editor(values)

    def split(self, editor: typing.Any) -> tuple:
        """name, position, rotation, scale and active, in the order of `_SLOT_ORDER`. None for the ones not stored."""
        transform = editor.transform
        return (editor.name, transform.position, transform.rotation, transform.scale, editor.active)


class _BoundDefault:
    """The default of a field in a game, with the structs in it in the game too."""

    def __init__(self, field: FieldInfo, game: Game):
        self.field = field
        self.game = game

    def make(self) -> typing.Any:
        return self.field.make_default(self.game)


def _default_value(defaults: dict | None, name: str, default: typing.Any) -> typing.Any:
    """The default of the field, or the override that the struct that holds this one gives it."""
    if defaults is not None and name in defaults:
        return copy.deepcopy(defaults[name])
    return default.make()


_SLOT_ORDER = ("name", "position", "rotation", "scale", "active")
_SLOT_CODECS: dict[str, Codec] = {
    "name": codecs.string,
    "position": codecs.vector,
    "rotation": codecs.vector,
    "scale": codecs.vector,
    "active": codecs.bool_,
}


class _FullWire:
    """`_wire` of an object that was read with every property its class stores, in the order of the class."""

    def __repr__(self) -> str:
        return "FULL_WIRE"

    def __copy__(self) -> _FullWire:
        return self

    def __deepcopy__(self, memo: dict) -> _FullWire:
        return self


FULL_WIRE = _FullWire()


class Plan:
    """
    The compiled decoder and encoder of a class, in a game.

    In id-tagged games, an object that was decoded remembers which properties it was read with (`__dict__["_wire"]`: a
    tuple of property ids in the order they were read, or `FULL_WIRE` when it had all of them in the order of the
    class). The encoder writes exactly those, plus the ones that were not in the data but have been modified since.
    So decoding and encoding unmodified data gives the same bytes, whatever the cooker of the game left out.
    Objects without `_wire` (new ones) follow the cook preferences of the fields. See `CookMode`.
    """

    def __init__(self, cls: type, game: Game):
        self.cls = cls
        self.game = game
        self.decode: Callable[..., typing.Any]
        """`(data, size, defaults, cooks=None)`: see `struct_` for `defaults` and `cooks`."""
        self.encode: Callable[..., None]
        """`(obj, data, defaults, cooks=None)`"""
        self.table: dict[int, tuple[str, Codec]] = {}
        self.keeps_unknown = False
        self.source = ""
        self.is_object = False
        self._info = class_info(cls)
        self._root_start = 0
        self.items: list[Item] = []
        self._build()

    # General path of id-tagged games: any order, with missing and unknown properties

    def encode_dynamic(
        self, o: typing.Any, data: typing.BinaryIO, defaults: dict | None, cooks: dict[str, Cook]
    ) -> None:
        """Encoder of id-tagged structs used by a field that overrides the cook preference of some of their fields."""
        d = o.__dict__
        game = self.game
        entries: list[tuple[int | None, Codec | None, typing.Any]] = []
        for item in self.items:
            cook = cooks.get(item.field.name, item.layout.cook)
            if cook == Cook.NEVER:
                continue
            value = d[item.field.name]
            if cook == Cook.ONLY_IF_MODIFIED:
                default = _default_value(defaults, item.field.name, _BoundDefault(item.field, game))
                if item.codec.equal(value, default):
                    continue
            entries.append((item.layout.id, item.codec, value))
        if self.keeps_unknown:
            entries.extend((pid, None, blob) for pid, blob in d["unknown_properties"].items())

        self._write_entries(data, entries)

    def encode_wire(self, o: typing.Any, data: typing.BinaryIO, defaults: dict | None, wire: tuple[int, ...]) -> None:
        """Writes the properties that `o` was read with in the order they were read, then the modified others."""
        d = o.__dict__
        game = self.game
        unknown = d["unknown_properties"] if self.keeps_unknown else {}
        entries: list[tuple[int | None, Codec | None, typing.Any]] = []
        seen = set(wire)
        for property_id in wire:
            entry = self.table.get(property_id)
            if entry is None:
                if property_id in unknown:
                    entries.append((property_id, None, unknown[property_id]))
            else:
                entries.append((property_id, entry[1], d[entry[0]]))
        for item in self.items:
            item_id = item.layout.id
            assert item_id is not None
            if item_id in seen or item.layout.cook == Cook.NEVER:
                continue
            value = d[item.field.name]
            default = _default_value(defaults, item.field.name, _BoundDefault(item.field, game))
            if not item.codec.equal(value, default):
                entries.append((item_id, item.codec, value))
        entries.extend((pid, None, blob) for pid, blob in unknown.items() if pid not in seen)
        self._write_entries(data, entries)

    def _write_entries(self, data: typing.BinaryIO, entries: list[tuple[int | None, Codec | None, typing.Any]]) -> None:
        game = self.game
        write = data.write
        if self.is_object:
            root = data.tell() + 4
            write(_get_struct(game, "LHH").pack(0xFFFFFFFF, 0, len(entries)))
        else:
            write(_get_struct(game, "H").pack(len(entries)))
        header = _get_struct(game, "LH")
        size = _get_struct(game, "H")
        for property_id, codec, value in entries:
            write(header.pack(property_id, 0))
            before = data.tell() - 2
            if codec is None:
                write(value)
            else:
                codec.write(data, game, value)
            after = data.tell()
            data.seek(before)
            write(size.pack(after - before - 2))
            data.seek(after)
        if self.is_object:
            end = data.tell()
            data.seek(root)
            write(size.pack(end - root - 2))
            data.seek(end)

    def decode_general(
        self, data: typing.BinaryIO, size: int | None, count: int, root_start: int, defaults: dict | None
    ) -> typing.Any:
        game = self.game
        read = data.read
        header = _get_struct(game, "LH")
        values: dict[str, typing.Any] = {}
        unknown: dict[int, bytes] = {}
        table = self.table
        wire = []
        for _ in range(count):
            property_id, property_size = header.unpack(read(6))
            wire.append(property_id)
            start = data.tell()
            entry = table.get(property_id)
            if entry is None:
                if not self.keeps_unknown:
                    raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
                unknown[property_id] = read(property_size)
            else:
                name, codec = entry
                values[name] = codec.read(data, game, property_size)
            assert data.tell() - start == property_size

        if self.is_object:
            assert data.tell() - root_start == size

        result: dict[str, typing.Any] = {}
        for field in self._info.fields.values():
            name = field.name
            if game not in field.layouts:
                result[name] = ABSENT
            elif name in values:
                result[name] = values[name]
            elif defaults is not None and name in defaults:
                result[name] = copy.deepcopy(defaults[name])
            else:
                result[name] = field.make_default(game)
        for extra in self._info.extras:
            result[extra.name] = extra.make_default()
        if self.keeps_unknown:
            result["unknown_properties"] = unknown
        result["_game"] = game
        result["_wire"] = tuple(wire)
        obj: typing.Any = object.__new__(self.cls)
        obj.__dict__ = result
        return obj

    # Building

    def _make_items(self) -> tuple[str, list[Item], dict[str, EditorHelper]]:
        cls, game, info = self.cls, self.game, self._info
        atomic = game in getattr(cls, "_atomic_games", ())
        kind = "atomic" if atomic else ("id" if game in ID_TAGGED_GAMES else "positional")

        items: list[tuple[tuple, Item]] = []
        editors: dict[str, EditorHelper] = {}
        next_index = 0
        for field in info.by_game[game]:
            layout = field.layouts[game]
            layout.codec.check_game(game)
            if layout.is_virtual:
                continue

            if kind == "id":
                if layout.id is None:
                    raise ValueError(f"{cls.__name__}.{field.name} has no property id in {game.name}")
                sort_key = (layout.order if layout.order is not None else field.index,)
            elif game == Game.PRIME:
                if layout.position is None:
                    raise ValueError(f"{cls.__name__}.{field.name} has no position in {game.name}")
                sort_key = (0,)
            else:  # atomic in an id-tagged game: no positions, only the order
                sort_key = (layout.order if layout.order is not None else field.index,)

            if isinstance(layout.position, PrimeEditor):
                editors[field.name] = EditorHelper(
                    typing.cast("codecs._Struct", layout.codec).cls, layout.position, game
                )
                for position, slot in layout.position.slots():
                    items.append(((position,), Item(next_index, field, layout, _SLOT_CODECS[slot], position, slot)))
                    next_index += 1
                continue

            field_position = layout.position if isinstance(layout.position, int) else None
            if game == Game.PRIME:
                sort_key = (field_position,)  # type: ignore[assignment]
            items.append((sort_key, Item(next_index, field, layout, layout.codec, field_position)))
            next_index += 1

        items.sort(key=lambda it: it[0])
        # Renumber in the final order, to have the generated code read in order
        result = []
        for i, (_, item) in enumerate(items):
            item.index = i
            result.append(item)
        return kind, result, editors

    def _build(self) -> None:
        cls, game, info = self.cls, self.game, self._info
        if info.fields and game not in info.games:
            raise ValueError(f"{cls.__name__} is not defined in {game.name}")
        kind, items, editors = self._make_items()
        self.items = items
        wire_fields = [f for f in info.by_game.get(game, []) if not f.layouts[game].is_virtual]
        if info.by_game.get(game) and not wire_fields:
            raise NotImplementedError(f"{cls.__name__} has no encoding in {game.name}: its owner encodes it")

        self.is_object = bool(getattr(cls, "_is_object", False)) and kind == "id"
        self.keeps_unknown = info.has_unknown_properties and kind == "id"
        gen = _Generator(self, kind, items, editors)
        self.decode, self.encode = gen.compile()
        self.source = gen.source
        if kind == "id":
            for item in items:
                assert item.layout.id is not None
                self.table[item.layout.id] = (item.field.name, item.codec)


def _get_struct(game: Game, fmt: str) -> struct.Struct:
    return codecs.get_struct(game.struct_endianness, fmt)


class _Source:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.indent = 0

    def add(self, line: str) -> None:
        self.lines.append("    " * self.indent + line)

    def __str__(self) -> str:
        return "\n".join(self.lines) + "\n"


class _Generator:
    def __init__(self, plan: Plan, kind: str, items: list[Item], editors: dict[str, EditorHelper]):
        self.plan = plan
        self.cls = plan.cls
        self.game = plan.game
        self.info = plan._info
        self.kind = kind
        self.items = items
        self.editors = editors
        self.endian = plan.game.struct_endianness
        self.ns: dict[str, typing.Any] = {
            "game": plan.game,
            "_cls": plan.cls,
            "_new": object.__new__,
            "_ABSENT": ABSENT,
            "_FULL": FULL_WIRE,
            "_dv": _default_value,
            "_plan": plan,
        }
        self.full = False
        """While generating the encoder of objects that were decoded with all their properties."""
        self._counter = 0
        self._codec_names: dict[int, str] = {}
        self.fixed: dict[int, codecs.Fixed | None] = {it.index: it.codec.fixed(plan.game) for it in items}
        self.parts, self.groups = self.split_optional()
        """The items in the order of the data, as runs of required items and groups of optional ones, and the groups."""

    def split_optional(self) -> tuple[list[tuple[int | None, list[Item]]], list[tuple[int, list[Item]]]]:
        """
        Splits the items of a Prime struct into runs of items that are always in the data and groups of optional ones
        (those with a `min_count`, grouped by `min_count`). Optional properties are present when the property count of
        the struct is large enough. The first part of each pair is the count of a group, None for a run.
        """
        name = f"{self.cls.__name__} in {self.game.name}"
        parts: list[tuple[int | None, list[Item]]] = []
        groups: list[tuple[int, list[Item]]] = []
        for item in self.items:
            count = item.layout.min_count
            if count is not None:
                if self.kind != "positional":
                    raise ValueError(f"{name}: only the properties of positional structs can be optional")
                if item.slot is not None:
                    raise ValueError(f"{name}: editor properties can't be optional")
            if parts and parts[-1][0] == count:
                parts[-1][1].append(item)
                continue
            if count is not None and groups and groups[-1][0] > count:
                raise ValueError(f"{name}: the counts of optional properties must not decrease")
            parts.append((count, [item]))
            if count is not None:
                groups.append((count, parts[-1][1]))
        present = sum(len(run) for count, run in parts if count is None)
        for count, group in groups:
            if present >= count:
                raise ValueError(f"{name}: a count of {present} would read the properties that need {count}")
            present += len(group)
            if present < count:
                raise ValueError(
                    f"{name}: {present} properties are written, too few to be read with a count of {count}"
                )
        return parts, groups

    def const(self, prefix: str, value: typing.Any) -> str:
        name = f"_{prefix}{self._counter}"
        self._counter += 1
        self.ns[name] = value
        return name

    def codec_name(self, item: Item) -> str:
        name = self._codec_names.get(item.index)
        if name is None:
            name = self.const("c", item.codec)
            self._codec_names[item.index] = name
        return name

    def struct_name(self, fmt: str) -> str:
        return self.const("S", codecs.get_struct(self.endian, fmt))

    def unpack_expr(self, item: Item, values: list[str]) -> str:
        fixed = self.fixed[item.index]
        assert fixed is not None
        return fixed.unpack.format(*values, c=self.codec_name(item))

    def pack_args(self, item: Item, value: str) -> str:
        fixed = self.fixed[item.index]
        assert fixed is not None
        return fixed.pack.format(v=value, c=self.codec_name(item))

    # Result dict

    def result_dict(self, values: dict[str, str], unknown: str | None, wire: str | None = None) -> str:
        """Source of the dict with all the attributes of the new instance, in the order of the dataclass."""
        entries = []
        for field in self.info.fields.values():
            name = field.name
            if self.game not in field.layouts:
                expr = "_ABSENT"
            elif name in values:
                expr = values[name]
            else:
                expr = self.const("d", functools.partial(field.make_default, self.game)) + "()"
            entries.append(f"{name!r}: {expr}")
        for extra in self.info.extras:
            entries.append(f"{extra.name!r}: {self.const('d', extra.make_default)}()")
        if unknown is not None:
            entries.append(f"'unknown_properties': {unknown}")
        entries.append("'_game': game")
        if wire is not None:
            entries.append(f"'_wire': {wire}")
        return "{" + ", ".join(entries) + "}"

    def field_values(self) -> dict[str, str]:
        """Expressions of the fields, from the variables of the items."""
        values: dict[str, str] = {}
        slots: dict[str, dict[str, str]] = {}
        for item in self.items:
            if item.slot is not None:
                slots.setdefault(item.field.name, {})[item.slot] = item.var
            else:
                values[item.field.name] = item.var
        for name, slot_vars in slots.items():
            helper = self.const("ed", self.editors[name])
            args = [f"{slot}={var}" for slot, var in slot_vars.items()]
            values[name] = f"{helper}.build(game, {', '.join(args)})"
        return values

    # Decoder

    def gen_decode(self, src: _Source) -> None:
        kind = self.kind
        src.add("def _decode(data, size, defaults, cooks=None):")
        src.indent += 1
        src.add("read = data.read")
        values_in_stream = self.field_values()

        if kind == "id":
            if self.plan.is_object:
                src.add(f"_, size_, count = {self.const('S', _get_struct(self.game, 'LHH'))}.unpack(read(8))")
                src.add("if _ != 0xFFFFFFFF:")
                src.add("    raise AssertionError('Not a struct')")
                src.add("root_start = data.tell() - 2")
                src.add("size = size_")
            else:
                src.add(f"count = {self.const('S', _get_struct(self.game, 'H'))}.unpack(read(2))[0]")
                src.add("root_start = 0")

            fast_items = [it for it in self.items if it.layout.cook != Cook.NEVER]
            src.add(f"if cooks is None and count == {len(fast_items)}:")
            src.indent += 1
            src.add("pos = data.tell()")
            src.add("while True:")
            src.indent += 1
            self.decode_segments(src, fast_items, True)
            unknown = "{}" if self.plan.keeps_unknown else None
            for item in self.items:
                if item.layout.cook == Cook.NEVER:
                    default = functools.partial(item.field.make_default, self.game)
                    src.add(f"{item.var} = {self.const('d', default)}()")
            src.add("o = _new(_cls)")
            src.add(f"o.__dict__ = {self.result_dict(values_in_stream, unknown, '_FULL')}")
            src.add("return o")
            src.indent -= 1
            src.add("data.seek(pos)")
            src.indent -= 1
            src.add("return _plan.decode_general(data, size, count, root_start, defaults)")
        else:
            wire = None
            if self.groups:
                self.gen_decode_optional(src)
                wire = "k"
            else:
                if kind == "positional":
                    src.add("read(4)")
                self.decode_segments(src, self.items, False)
            unknown = "{}" if self.plan.keeps_unknown else None
            src.add("o = _new(_cls)")
            src.add(f"o.__dict__ = {self.result_dict(values_in_stream, unknown, wire)}")
            src.add("return o")
        src.indent -= 1

    def gen_decode_optional(self, src: _Source) -> None:
        """
        Reads the property count, then the properties. `k` is the number of groups of optional properties that were in
        the data, which is what the encoder needs to write the same count.
        """
        src.add(f"count = {self.struct_name('L')}.unpack(read(4))[0]")
        src.add(f"if count >= {self.groups[-1][0]}:")
        src.indent += 1
        self.decode_segments(src, self.items, False)
        src.add(f"k = {len(self.groups)}")
        src.indent -= 1
        src.add("else:")
        src.indent += 1
        src.add("k = 0")
        number = 0
        for count, run in self.parts:
            if count is None:
                self.decode_segments(src, run, False)
                continue
            number += 1
            src.add(f"if count >= {count}:")
            src.indent += 1
            self.decode_segments(src, run, False)
            src.add(f"k = {number}")
            src.indent -= 1
            src.add("else:")
            src.indent += 1
            for item in run:
                default = functools.partial(item.field.make_default, self.game)
                src.add(f"{item.var} = {self.const('d', default)}()")
            src.indent -= 1
        src.indent -= 1

    def decode_segments(self, src: _Source, items: list[Item], tagged: bool) -> None:
        run: list[Item] = []

        def flush() -> None:
            if not run:
                return
            fmt = ""
            for it in run:
                fixed = self.fixed[it.index]
                assert fixed is not None
                fmt += ("LH" if tagged else "") + fixed.fmt
            s = self.struct_name(fmt)
            var = f"v{run[0].index}"
            src.add(f"{var} = {s}.unpack(read({struct.calcsize(self.endian + fmt)}))")
            if tagged:
                checks = []
                column = 0
                for it in run:
                    checks.append(f"{var}[{column}] != {it.layout.id:#x}")
                    column += 2 + self.fixed[it.index].columns  # type: ignore[union-attr]
                src.add(f"if {' or '.join(checks)}:")
                src.add("    break")
            column = 0
            for it in run:
                if tagged:
                    column += 2
                n = self.fixed[it.index].columns  # type: ignore[union-attr]
                refs = [f"{var}[{column + k}]" for k in range(n)]
                src.add(f"{it.var} = {self.unpack_expr(it, refs)}")
                column += n
            run.clear()

        for item in items:
            conditional = item.layout.only_if is not None
            if self.fixed[item.index] is not None and not conditional:
                run.append(item)
                continue
            flush()
            codec_name = self.codec_name(item)
            if tagged:
                header = self.const("S", _get_struct(self.game, "LH"))
                src.add(f"hid, hsz = {header}.unpack(read(6))")
                src.add(f"if hid != {item.layout.id:#x}:")
                src.add("    break")
                src.add(f"{item.var} = {codec_name}.read(data, game, hsz)")
            else:
                read_expr = f"{codec_name}.read(data, game, None)"
                if conditional:
                    cond = self.var_of_field(item.layout.only_if)
                    default = self.const("d", functools.partial(item.field.make_default, self.game))
                    src.add(f"{item.var} = {read_expr} if {cond} else {default}()")
                else:
                    src.add(f"{item.var} = {read_expr}")
        flush()

    def var_of_field(self, name: str | None) -> str:
        for item in self.items:
            if item.field.name == name and item.slot is None:
                return item.var
        raise ValueError(f"{self.cls.__name__}: only_if refers to {name!r}, which is not stored in {self.game.name}")

    # Encoder

    def gen_encode(self, src: _Source) -> None:
        if self.kind != "id":
            self.gen_encode_body(src, "_encode")
            return
        # Objects read from data are written with the properties they were read with. See `Plan`.
        self.full = False
        self.gen_encode_body(src, "_encode_fresh")
        src.add("")
        self.full = True
        self.gen_encode_body(src, "_encode_full")
        src.add("")
        src.add("def _encode(o, data, defaults, cooks=None):")
        src.add("    wire = o.__dict__.get('_wire')")
        src.add("    if wire is None:")
        src.add("        return _encode_fresh(o, data, defaults, cooks)")
        src.add("    if wire is _FULL:")
        src.add("        return _encode_full(o, data, defaults, cooks)")
        src.add("    return _plan.encode_wire(o, data, defaults, wire)")

    def gen_encode_body(self, src: _Source, name: str) -> None:
        kind = self.kind
        src.add(f"def {name}(o, data, defaults, cooks=None):")
        src.indent += 1
        src.add("d = o.__dict__")
        src.add("w = data.write")
        for field_name in self.editors:
            src.add(f"e_{field_name} = {self.const('ed', self.editors[field_name])}.split(d[{field_name!r}])")

        if kind == "id":
            if not self.full:
                src.add("if cooks is not None:")
                src.add("    return _plan.encode_dynamic(o, data, defaults, cooks)")
            self.gen_encode_id(src)
        elif self.groups:
            self.gen_encode_optional(src)
        else:
            if kind == "positional":
                count = len(self.items)
                src.add(f"w({self.const('B', count.to_bytes(4, 'big' if self.endian == '>' else 'little'))})")
            self.encode_segments(src, self.items, False)
        src.indent -= 1

    def gen_encode_optional(self, src: _Source) -> None:
        """
        Writes the required properties, and the optional ones that were in the data (`_wire` is the number of groups of
        them), or have a value other than the default now: the count is the number of properties written.
        """
        src.add("k = d.get('_wire', 0)")
        keyword = "if"
        for number in range(len(self.groups) - 1, -1, -1):
            checks = []
            for item in self.groups[number][1]:
                bound = self.const("D", _BoundDefault(item.field, self.game))
                name = item.field.name
                checks.append(f"not {self.codec_name(item)}.equal(d[{name!r}], _dv(defaults, {name!r}, {bound}))")
            src.add(f"{keyword} k < {number + 1} and ({' or '.join(checks)}):")
            src.add(f"    k = {number + 1}")
            keyword = "elif"
        written = [sum(len(run) for count, run in self.parts if count is None)]
        for _, group in self.groups:
            written.append(written[-1] + len(group))
        src.add(f"w({self.struct_name('L')}.pack({self.const('T', tuple(written))}[k]))")
        number = 0
        for count, run in self.parts:
            if count is None:
                self.encode_segments(src, run, False)
                continue
            src.add(f"if k > {number}:")
            number += 1
            src.indent += 1
            self.encode_segments(src, run, False)
            src.indent -= 1

    def value_expr(self, item: Item) -> str:
        if item.slot is not None:
            return f"e_{item.field.name}[{_SLOT_ORDER.index(item.slot)}]"
        return f"d[{item.field.name!r}]"

    def gen_encode_id(self, src: _Source) -> None:
        items = self.items
        if self.full:
            src.add(f"n = {sum(1 for it in items if it.layout.cook != Cook.NEVER)}")
        else:
            always = sum(1 for it in items if it.layout.cook in (Cook.ALWAYS, Cook.DEFAULT))
            src.add(f"n = {always}")
        for item in items:
            if item.layout.cook == Cook.ONLY_IF_MODIFIED and not self.full:
                bound = self.const("D", _BoundDefault(item.field, self.game))
                src.add(f"dv{item.index} = _dv(defaults, {item.field.name!r}, {bound})")
                src.add(f"m{item.index} = not {self.codec_name(item)}.equal(d[{item.field.name!r}], dv{item.index})")
                src.add(f"if m{item.index}:")
                src.add("    n += 1")
        if self.plan.keeps_unknown:
            src.add("n += len(d['unknown_properties'])")
        if self.plan.is_object:
            src.add("root = data.tell() + 4")
            src.add(f"w({self.const('S', _get_struct(self.game, 'LHH'))}.pack(0xFFFFFFFF, 0, n))")
        else:
            src.add(f"w({self.const('S', _get_struct(self.game, 'H'))}.pack(n))")

        self.encode_segments(src, items, True)

        if self.plan.keeps_unknown:
            header = self.const("S", _get_struct(self.game, "LH"))
            src.add("for pid, blob in d['unknown_properties'].items():")
            src.add(f"    w({header}.pack(pid, len(blob)))")
            src.add("    w(blob)")
        if self.plan.is_object:
            src.add("end = data.tell()")
            src.add("data.seek(root)")
            src.add(f"w({self.const('S', _get_struct(self.game, 'H'))}.pack(end - root - 2))")
            src.add("data.seek(end)")

    def encode_segments(self, src: _Source, items: list[Item], tagged: bool) -> None:
        run: list[tuple[Item, str]] = []

        def flush() -> None:
            if not run:
                return
            fmt = ""
            args = []
            for it, value in run:
                fixed = self.fixed[it.index]
                assert fixed is not None
                if tagged:
                    fmt += "LH"
                    args.append(f"{it.layout.id:#x}")
                    args.append(str(struct.calcsize(self.endian + fixed.fmt)))
                fmt += fixed.fmt
                args.append(self.pack_args(it, value))
            src.add(f"w({self.struct_name(fmt)}.pack({', '.join(args)}))")
            run.clear()

        for item in items:
            cook = item.layout.cook if tagged else Cook.ALWAYS
            if cook == Cook.DEFAULT or (self.full and cook != Cook.NEVER):
                cook = Cook.ALWAYS  # always written, with the value of the object
            if cook == Cook.NEVER:
                continue
            fixed = self.fixed[item.index]
            conditional = item.layout.only_if is not None
            value = self.value_expr(item)

            if cook == Cook.ONLY_IF_MODIFIED:
                flush()
                src.add(f"if m{item.index}:")
                src.indent += 1
                self.encode_single(src, item, value, tagged)
                src.indent -= 1
                continue

            if fixed is not None and not conditional and cook == Cook.ALWAYS:
                local = f"a{item.index}"
                src.add(f"{local} = {value}")
                run.append((item, local))
                continue

            flush()
            if conditional:
                src.add(f"if {self.cond_expr(item.layout.only_if)}:")
                src.indent += 1
                self.encode_single(src, item, value, tagged)
                src.indent -= 1
            else:
                self.encode_single(src, item, value, tagged)
        flush()

    def cond_expr(self, name: str | None) -> str:
        return f"d[{name!r}]"

    def encode_single(self, src: _Source, item: Item, value: str, tagged: bool) -> None:
        fixed = self.fixed[item.index]
        if fixed is not None:
            local = f"s{item.index}"
            src.add(f"{local} = {value}")
            fmt = ("LH" if tagged else "") + fixed.fmt
            args = []
            if tagged:
                args = [f"{item.layout.id:#x}", str(struct.calcsize(self.endian + fixed.fmt))]
            args.append(self.pack_args(item, local))
            src.add(f"w({self.struct_name(fmt)}.pack({', '.join(args)}))")
            return

        codec_name = self.codec_name(item)
        if tagged:
            header = self.const("S", _get_struct(self.game, "LH"))
            src.add(f"w({header}.pack({item.layout.id:#x}, 0))")
            src.add("before = data.tell() - 2")
            src.add(f"{codec_name}.write(data, game, {value})")
            src.add("after = data.tell()")
            src.add("data.seek(before)")
            src.add(f"w({self.const('S', _get_struct(self.game, 'H'))}.pack(after - before - 2))")
            src.add("data.seek(after)")
        else:
            src.add(f"{codec_name}.write(data, game, {value})")

    def compile(self) -> tuple[Callable, Callable]:
        src = _Source()
        self.gen_decode(src)
        src.add("")
        self.gen_encode(src)
        code = str(src)
        filename = f"<{self.cls.__name__} codec for {self.game.name}>"
        exec(compile(code, filename, "exec"), self.ns)  # noqa: S102
        self.source = code
        return self.ns["_decode"], self.ns["_encode"]
