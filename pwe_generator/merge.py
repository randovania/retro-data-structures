"""Merging of the classes of the games into one class for each name, and deciding where each class is written."""

from __future__ import annotations

import collections
import dataclasses
import typing

import inflection

from pwe_generator.enums import MEnum, merge_enums
from pwe_generator.model import GAMES, ID_TAGGED, Codec, EnumKey, GameData, GClass, GField
from retro_data_structures.game_check import Game

KIND_PRIORITY = {"object": 0, "tweak": 1, "struct": 2}
EDITOR_STRUCTS = {"EditorProperties": ("name", "transform", "active"), "Transform": ("position", "rotation", "scale")}


@dataclasses.dataclass
class MField:
    name: str
    layouts: dict[Game, GField]
    split_from: str | None = None
    """For a field split by a type conflict: the name it would have had."""

    @property
    def games(self) -> list[Game]:
        return sorted(self.layouts, key=lambda g: g.value)

    @property
    def type_key(self) -> tuple:
        return next(iter(self.layouts.values())).codec.type_key()


@dataclasses.dataclass
class MClass:
    name: str
    kind: str
    games: list[Game]
    per_game: dict[Game, GClass]
    fields: list[MField]
    order_games: list[Game] = dataclasses.field(default_factory=list)
    """Games whose properties are not written in the order of the fields: every field gets an explicit order."""
    final_name: str = ""
    placement: str = ""
    """"objects" or "archetypes", or the name of the class in whose module this one is written."""
    owners: set[str] = dataclasses.field(default_factory=set)

    @property
    def is_object(self) -> bool:
        return any(c.object_type is not None for c in self.per_game.values())

    @property
    def alias_object_types(self) -> dict[Game, list[str | int]]:
        return {g: c.alias_object_types for g, c in self.per_game.items() if c.alias_object_types}

    @property
    def object_types(self) -> dict[Game, str | int]:
        return {g: c.object_type for g, c in self.per_game.items() if c.object_type is not None}

    def struct_refs(self) -> set[str]:
        return {ref for f in self.fields for lay in f.layouts.values() for ref in lay.codec.struct_refs()}

    def enum_refs(self) -> set[EnumKey]:
        refs: set[EnumKey] = set()
        for f in self.fields:
            for lay in f.layouts.values():
                refs.update(lay.codec.enum_refs())
                if lay.default is not None and lay.default.kind in ("enum", "flags"):
                    refs.add(lay.default.ref)
        return refs


@dataclasses.dataclass
class Merged:
    classes: dict[str, MClass]
    enums: dict[EnumKey, MEnum]
    report: dict[str, list[str]]
    games: dict[Game, GameData]


def _suffix_for(type_key: tuple) -> str:
    match type_key[0]:
        case "list":
            return "list_" + _suffix_for(type_key[1])
        case "enum":
            return inflection.underscore(type_key[1][-1])
        case "struct":
            return inflection.underscore(type_key[1])
        case _:
            return inflection.underscore(str(type_key[0]))


def _add_virtual_editor_games(per_game: dict[str, dict[Game, GClass]]) -> None:
    """EditorProperties and Transform exist in Prime too, but its objects store the values themselves."""
    if not any(
        f.name == "editor_properties"
        for c in (cls for g in per_game.values() for cls in g.values())
        if c.game == Game.PRIME
        for f in c.fields
    ):
        return
    for name, field_names in EDITOR_STRUCTS.items():
        by_game = per_game[name]
        source = by_game[Game.ECHOES]
        fields = [
            dataclasses.replace(f, game=Game.PRIME, locator=None, cook="Always")
            for f in source.fields
            if f.name in field_names
        ]
        assert len(fields) == len(field_names)
        by_game[Game.PRIME] = GClass(Game.PRIME, name, source.kind, fields, atomic=False)


def _split_conflicts(name: str, per_game: dict[Game, GClass]) -> dict[Game, list[tuple[str, GField]]]:
    """Renames the fields that have different Python types in different games. Returns each game's fields in order."""
    by_name: dict[str, dict[Game, GField]] = collections.defaultdict(dict)
    for game, cls in per_game.items():
        for f in cls.fields:
            by_name[f.name][game] = f

    renames: dict[tuple[str, Game], str] = {}
    taken = set(by_name)
    for field_name in sorted(by_name):
        variants: dict[tuple, list[Game]] = collections.defaultdict(list)
        for game, f in by_name[field_name].items():
            variants[f.codec.type_key()].append(game)
        if len(variants) == 1:
            continue
        ordered = sorted(variants.items(), key=lambda kv: (-len(kv[1]), -max(g.value for g in kv[1])))
        for type_key, games in ordered[1:]:
            new_name = f"{field_name}_{_suffix_for(type_key)}"
            while new_name in taken:
                new_name += "_"
            taken.add(new_name)
            for game in games:
                renames[field_name, game] = new_name
    return {game: [(renames.get((f.name, game), f.name), f) for f in cls.fields] for game, cls in per_game.items()}


def _merge_order(per_game_fields: dict[Game, list[str]]) -> list[str]:
    games = sorted(per_game_fields, key=lambda g: (-len(per_game_fields[g]), -g.value))
    result = list(per_game_fields[games[0]])
    for game in games[1:]:
        anchor = -1
        for name in per_game_fields[game]:
            if name in result:
                anchor = result.index(name)
            else:
                anchor += 1
                result.insert(anchor, name)
    return result


def _rename_refs(codec: Codec, aliases: dict[str, str]) -> Codec:
    inner = _rename_refs(codec.inner, aliases) if codec.inner is not None else None
    ref = aliases.get(codec.ref, codec.ref) if codec.kind == "struct" else codec.ref
    return dataclasses.replace(codec, ref=ref, inner=inner)


def _case_aliases(games_data: dict[Game, GameData], report: dict[str, list[str]]) -> dict[str, str]:
    """Names that differ only in case would be the same file. They're the same class: the newest game's spelling wins."""
    spellings: dict[str, dict[str, Game]] = collections.defaultdict(dict)
    for game in GAMES:
        for name in games_data[game].classes:
            spellings[name.lower()][name] = game
    aliases: dict[str, str] = {}
    for names in spellings.values():
        if len(names) == 1:
            continue
        canonical = max(names, key=lambda n: (names[n].value, n))
        for name in names:
            if name != canonical:
                aliases[name] = canonical
                report["case"].append(f"{name} ({names[name].name}) is {canonical}")
    return aliases


def merge_classes(games_data: dict[Game, GameData], report: dict[str, list[str]]) -> dict[str, MClass]:
    aliases = _case_aliases(games_data, report)
    per_game: dict[str, dict[Game, GClass]] = collections.defaultdict(dict)
    for game in GAMES:
        for name, cls in games_data[game].classes.items():
            canonical = aliases.get(name, name)
            cls.name = canonical
            for f in cls.fields:
                f.codec = _rename_refs(f.codec, aliases)
            per_game[canonical][game] = cls
    _add_virtual_editor_games(per_game)

    result: dict[str, MClass] = {}
    for name in sorted(per_game):
        classes = per_game[name]
        kinds = {c.kind for c in classes.values()}
        kind = min(kinds, key=KIND_PRIORITY.__getitem__)
        if len(kinds) > 1:
            report["kind"].append(f"{name}: {', '.join(f'{g.name}={c.kind}' for g, c in classes.items())}")

        split = _split_conflicts(name, classes)
        order_names = {game: [n for n, _ in fields] for game, fields in split.items()}
        merged_order = _merge_order(order_names)

        layouts: dict[str, dict[Game, GField]] = collections.defaultdict(dict)
        original: dict[str, str] = {}
        for game, fields in split.items():
            for field_name, f in fields:
                layouts[field_name][game] = f
                if field_name != f.name:
                    original[field_name] = f.name
        mfields = [MField(n, layouts[n], original.get(n)) for n in merged_order]

        order_games = [
            game
            for game in ID_TAGGED
            if game in order_names and [n for n in merged_order if n in order_names[game]] != order_names[game]
        ]
        result[name] = MClass(name, kind, sorted(classes, key=lambda g: g.value), classes, mfields, order_games)
        for field_name, old_name in original.items():
            report["split"].append(
                f"{name}.{old_name}: {field_name} in "
                + ", ".join(g.name for g in sorted(layouts[field_name], key=lambda g: g.value))
            )
    return result


def compute_owners(classes: dict[str, MClass]) -> None:
    """Sets `owners` of every struct: the objects and tweaks that use it, directly or through other structs."""
    roots = {n for n, c in classes.items() if c.kind != "struct"}
    for name in roots:
        classes[name].owners = {name}
    changed = True
    while changed:
        changed = False
        for cls in classes.values():
            if not cls.owners:
                continue
            for ref in cls.struct_refs():
                target = classes[ref]
                if target.kind == "struct" and not cls.owners <= target.owners:
                    target.owners |= cls.owners
                    changed = True

    for cls in classes.values():
        if cls.kind != "struct":
            cls.placement = "objects"
        elif len(cls.owners) == 1:
            cls.placement = next(iter(cls.owners))
        else:
            cls.placement = "archetypes"


def merge(games_data: dict[Game, GameData]) -> Merged:
    report: dict[str, list[str]] = collections.defaultdict(list)
    enums = merge_enums(games_data)
    classes = merge_classes(games_data, report)
    compute_owners(classes)
    return Merged(classes, enums, report, games_data)


def codec_refs(codec: Codec) -> typing.Iterator[Codec]:
    yield codec
    if codec.inner is not None:
        yield from codec_refs(codec.inner)
