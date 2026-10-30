"""
Codecs and the declarative layout of merged property classes.

Generated class format
======================

A property class exists once for all games it appears in. Every field is declared with `prop()`, which says how the
field is stored in each game. The class does not contain any encode/decode code: `BaseStruct`/`BaseObjectType` compile
(per class and game, on first use) a decoder and an encoder from the layouts.

Example::

    @dataclasses.dataclass()
    class Transform(BaseStruct, games=ALL_GAMES):
        # In every game, but Prime stores these values in the owner (see `PrimeEditor`): "virtual" there.
        position: Vector = prop(vector, id=0x504F5321, games=ALL_GAMES)
        rotation: Vector = prop(vector, id=0x524F5421, games=ALL_GAMES)
        scale: Vector = prop(vector, id=0x53434C21, games=ALL_GAMES, default_factory=lambda: Vector(1.0, 1.0, 1.0))


    @dataclasses.dataclass()
    class EditorProperties(BaseStruct, games=ALL_GAMES):
        name: str = prop(string, id=0x494E414D, games=ALL_GAMES)
        transform: Transform = prop(struct(Transform), id=0x5846524D, games=ALL_GAMES)
        active: bool = prop(bool_, id=0x41435456, games=ALL_GAMES, default=True)


    class Weakness(enum.IntFlag):
        Beam = 1
        Seeker = 4  # canonical value, the one of the last game that has it

        __game_values__ = {
            Game.PRIME: {"Beam": 1},
            Game.ECHOES: {"Beam": 1, "Seeker": 8},
            Game.CORRUPTION: {"Beam": 1, "Seeker": 4},
        }


    @dataclasses.dataclass()
    class Door(BaseObjectType, object_types={PRIME: 0x03, ECHOES: "DOOR", CORRUPTION: "DOOR"}):
        # `prime=PrimeEditor(active=7)`: in Prime, the 4 editor values (and the optional active flag) are positional
        # properties of the owner, which become the fields of this `EditorProperties`.
        editor_properties: EditorProperties = prop(
            struct(EditorProperties), id=0x255A4580, prime=PrimeEditor(active=7), games=ALL_GAMES
        )
        collision_box: Vector = prop(vector, id=0xF344C0B0, prime=4)  # id for Echoes/Corruption, position for Prime
        animation: AnimationParameters = prop(animation_parameters, id=0xE25FB08C, prime=6)
        shell_model: int = prop(asset("CMDL"), id=0xB20CC271, games=ECHOES | CORRUPTION)  # not in Prime
        is_open: bool = prop(bool_, id=0xA1DFFAD2, prime=8, default=True, defaults={CORRUPTION: False})
        weak_to: Weakness = prop(flags_(Weakness), id=0xAAAA0003, prime=11, default=Weakness(0))
        count: int = prop(s32, id=0xAAAA0004, prime=12, codecs={PRIME: u16})
        tags: list[int] = prop(array(u32), id=0xAAAA0006, prime=14)
        unknown_properties: dict[int, bytes] = unknown_properties()  # only for classes with incomplete templates

Rules:

- `prop(codec, id=, prime=, echoes=, corruption=, games=, default=, default_factory=, defaults=, codecs=, cook=,
  cooks=, order=, only_if=, asset_types=, original_name=)`. `id` is the id in Echoes and Corruption; `echoes=` and
  `corruption=` override it. `prime` is the position (Prime has no ids). `games` defaults to the games that have an id
  or position; a game listed in `games` with neither is virtual: the field exists, but its owner encodes it.
- The dataclass default is the default of the field if all games agree, otherwise `UNSET`, which is replaced by the
  default of the game when the object gets one. Asset defaults depend on the game (invalid id width), so they are
  `UNSET` until the game is known.
- Class kwargs: `BaseStruct(atomic=, modules=, games=)` (`atomic` structs have no count in Prime) and
  `BaseObjectType(object_types={game: type})`.
- Id-tagged games write the fields in dataclass order unless `order={game: n}`. Prime writes in position order.
  `only_if="field"` omits the property in Prime unless that bool field is true (Water-like conditionals).
  `prime=(position, min_count)` makes a Prime property optional: it is only in the data when the struct's property
  count is at least `min_count`. A decoded object remembers how many groups of optional properties it had (`_wire`)
  and writes them back; `CookMode.MINIMAL` and new objects drop the trailing ones that equal their default.
- Cook preferences (`Cook.NEVER`, `DEFAULT`, `ONLY_IF_MODIFIED`) only affect id-tagged games, and by default only
  objects that weren't decoded: a decoded object remembers the property ids it was read with (`_wire`, ignored by
  `==` and `to_json`) and writes those back. `to_bytes(game, cook=CookMode.MINIMAL)` ignores that and applies the
  preferences only. The memory is dropped by `to_game`, `dataclasses.replace` and `from_json`, kept by `deepcopy`.
- Enums define `__game_values__`; see `retro_data_structures.enums.merged`. A member that doesn't exist in a game
  raises `MemberNotInGame` when encoded.
- Prime `EditorProperties.active` defaults to True, but a Prime Door's own Active flag defaults to False in the
  game's data: the decoded value always wins.

Game binding
============

Objects are created without a game (`game=` is the last, keyword argument) and bound by `set_game()`, by the first
`to_bytes`/`to_stream` call with a game, by `from_bytes(data, game)`, or by being assigned to a field of a bound
object (children are bound recursively; assigning a differently-bound one raises `GameMismatch`). Reading a field that
is `UNSET` for lack of a game raises `GameNotSet`; reading one that the game doesn't have raises `FieldNotInGame`
(both are also `AttributeError`). `to_game(other)` returns a converted copy and raises
`FieldNotInGame`/`MemberNotInGame`
for non-default values that don't exist in the target. `ClassNotInGame` is raised for classes used in an
unsupported game.
`dataclasses.replace` and `copy.deepcopy` work.
"""

from __future__ import annotations

from retro_data_structures.game_check import Game
from retro_data_structures.properties.codec.codecs import (
    Codec,
    animation_parameters,
    array,
    asset,
    bool_,
    bytes_,
    color,
    enum_,
    f32,
    flags_,
    guid,
    s8,
    s16,
    s32,
    sound,
    spline,
    string,
    u8,
    u16,
    u32,
    vector,
)
from retro_data_structures.properties.codec.codecs import struct_ as struct
from retro_data_structures.properties.codec.layout import (
    EDITOR_PROPERTIES,
    Cook,
    CookMode,
    FieldLayout,
    PrimeEditor,
    prop,
    unknown_properties,
)
from retro_data_structures.properties.errors import UNSET

PRIME = Game.PRIME
ECHOES = Game.ECHOES
CORRUPTION = Game.CORRUPTION
ALL_GAMES = PRIME | ECHOES | CORRUPTION

__all__ = [
    "ALL_GAMES",
    "CORRUPTION",
    "ECHOES",
    "EDITOR_PROPERTIES",
    "PRIME",
    "UNSET",
    "Codec",
    "Cook",
    "CookMode",
    "FieldLayout",
    "PrimeEditor",
    "animation_parameters",
    "array",
    "asset",
    "bool_",
    "bytes_",
    "color",
    "enum_",
    "f32",
    "flags_",
    "guid",
    "prop",
    "s8",
    "s16",
    "s32",
    "sound",
    "spline",
    "string",
    "struct",
    "u8",
    "u16",
    "u32",
    "unknown_properties",
    "vector",
]
