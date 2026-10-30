"""Merging of the enums and flags of the games."""

from __future__ import annotations

import dataclasses
import keyword
import typing

from pwe_generator.model import GAMES, EnumKey, GameData
from pwe_generator.parse import ENUMS_THAT_ALLOW_UNKNOWN_VALUES, scrub_enum

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game


def member_name(name: str) -> str:
    result = scrub_enum(name)
    return result + "_" if keyword.iskeyword(result) else result


@dataclasses.dataclass
class MEnum:
    """An enum or flags class for all the games that have it."""

    key: EnumKey
    name: str
    kind: str
    """"enum" or "flags"."""
    base: str
    """The enum class it extends, without `enum.`."""
    members: list[str]
    """In declaration order."""
    canonical: dict[str, typing.Any]
    game_values: dict[Game, dict[str, typing.Any]]
    plain: bool
    """True if every game has the same members with the same values: no `__game_values__`."""
    allow_unknown: bool = False
    renumbered: list[str] = dataclasses.field(default_factory=list)
    final_name: str = ""
    owner: str | None = None

    def game_member(self, game: Game, raw: int) -> str | None:
        """The member that has the value in the game."""
        for name, value in self.game_values[game].items():
            if value == raw:
                return name
        return None

    def canonical_flags(self, game: Game, mask: int) -> int:
        """Canonical value of flags of the game. Bits that no member has are kept."""
        if self.plain:
            return mask
        result = 0
        remaining = mask
        for name, game_bits in self.game_values[game].items():
            canonical = self.canonical[name]
            if canonical != 0 and canonical & (canonical - 1) == 0 and game_bits and mask & game_bits == game_bits:
                result |= canonical
                remaining &= ~game_bits
        return result | remaining


def merge_enums(games: dict[Game, GameData]) -> dict[EnumKey, MEnum]:
    keys: dict[EnumKey, dict[Game, typing.Any]] = {}
    for game in GAMES:
        for key, definition in games[game].enums.items():
            keys.setdefault(key, {})[game] = definition

    result: dict[EnumKey, MEnum] = {}
    for key in sorted(keys):
        defs = keys[key]
        newest_first = sorted(defs, key=lambda g: -g.value)
        kind = next(iter(defs.values())).kind
        assert all(d.kind == kind for d in defs.values()), key

        per_game: dict[Game, dict[str, typing.Any]] = {}
        for game, definition in defs.items():
            values: dict[str, typing.Any] = {}
            for raw_name, value in definition.values.items():
                name = member_name(raw_name)
                while name in values:
                    name += "_"
                values[name] = value
            per_game[game] = values

        members: list[str] = []
        for game in newest_first:
            members.extend(n for n in per_game[game] if n not in members)
        source = {n: next(g for g in newest_first if n in per_game[g]) for n in members}
        canonical = {n: per_game[source[n]][n] for n in members}

        base = next(iter(defs.values())).base
        if kind == "flags":
            base = "IntFlag"
        renumbered: list[str] = []
        # Members that have the same value, but not in the same game, are different members.
        # Members that have the same value in the game they get it from are aliases, like in the game's own enum.
        owner_of: dict[tuple[type, typing.Any], str] = {}
        for n in members:
            value = canonical[n]
            other = owner_of.get((type(value), value))
            if (
                other is not None
                and source[other] != source[n]
                and not (kind == "flags" and (value == 0 or value & (value - 1)))
            ):
                renumbered.append(n)
                if kind == "flags":
                    taken = set(canonical.values())
                    value = next(1 << i for i in range(32) if (1 << i) not in taken)
                else:
                    value = max(v for v in canonical.values() if isinstance(v, int)) + 1
                canonical[n] = value
            owner_of.setdefault((type(value), value), n)

        plain = all(per_game[g] == canonical for g in defs) and all(set(per_game[g]) == set(members) for g in defs)
        name = key[-1]
        owner = key[1] if key[0] == "local" else None
        enum = MEnum(
            key,
            name,
            kind,
            base,
            members,
            canonical,
            per_game,
            plain,
            name in ENUMS_THAT_ALLOW_UNKNOWN_VALUES,
            renumbered,
        )
        enum.owner = owner
        if enum.allow_unknown:
            assert plain, f"{name} must have the same values in every game"
        result[key] = enum
    return result
