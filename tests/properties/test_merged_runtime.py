"""
Tests of the runtime of the merged property classes, with small hand-written classes that look like what the
generator emits. The expected bytes are built by hand in the format of the games.
"""

from __future__ import annotations

import copy
import dataclasses
import enum
import io
import os
import struct
import typing

import pytest

from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseObjectType, BaseStruct
from retro_data_structures.properties.codec import (
    ALL_GAMES,
    CORRUPTION,
    ECHOES,
    PRIME,
    Cook,
    CookMode,
    PrimeEditor,
    animation_parameters,
    array,
    asset,
    bool_,
    color,
    enum_,
    f32,
    flags_,
    guid,
    prop,
    s16,
    s32,
    sound,
    spline,
    string,
    u8,
    u16,
    u32,
    unknown_properties,
    vector,
)
from retro_data_structures.properties.codec import (
    struct as struct_codec,
)
from retro_data_structures.properties.codec.plan import FULL_WIRE
from retro_data_structures.properties.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.core.color import Color
from retro_data_structures.properties.core.spline import Spline
from retro_data_structures.properties.core.vector import Vector
from retro_data_structures.properties.errors import (
    ABSENT,
    UNSET,
    ClassNotInGame,
    FieldNotInGame,
    GameMismatch,
    GameNotSet,
    MemberNotInGame,
)
from retro_data_structures.properties.field_reflection import get_reflection

# Enums


class Effect(enum.IntEnum):
    Normal = 0
    Fire = 1
    Ice = 2  # canonical value: the one in Corruption

    __game_values__ = {  # noqa: RUF012
        Game.PRIME: {"Normal": 0, "Fire": 1},
        Game.ECHOES: {"Normal": 0, "Fire": 1, "Ice": 5},
        Game.CORRUPTION: {"Normal": 0, "Fire": 1, "Ice": 2},
    }


class Weakness(enum.IntFlag):
    Beam = 1
    Missile = 2
    Seeker = 4  # canonical bit: the one in Corruption

    __game_values__ = {  # noqa: RUF012
        Game.PRIME: {"Beam": 1, "Missile": 2},
        Game.ECHOES: {"Beam": 1, "Missile": 2, "Seeker": 8},
        Game.CORRUPTION: {"Beam": 1, "Missile": 2, "Seeker": 4},
    }


class Same(enum.IntEnum):
    A = 0
    B = 7


# Classes


@dataclasses.dataclass()
class Transform(BaseStruct, games=ALL_GAMES):
    # Present in every game, but only stored by Echoes and Corruption: in Prime, the owner stores the values
    position: Vector = prop(vector, id=0x504F5321, games=ALL_GAMES)
    rotation: Vector = prop(vector, id=0x524F5421, games=ALL_GAMES)
    scale: Vector = prop(vector, id=0x53434C21, games=ALL_GAMES, default_factory=lambda: Vector(1.0, 1.0, 1.0))


@dataclasses.dataclass()
class EditorProperties(BaseStruct, games=ALL_GAMES):
    name: str = prop(string, id=0x494E414D, games=ALL_GAMES)
    transform: Transform = prop(struct_codec(Transform), id=0x5846524D, games=ALL_GAMES)
    active: bool = prop(bool_, id=0x41435456, games=ALL_GAMES, default=True)
    unknown: int = prop(u32, id=0x5D298A43, default=3)  # Echoes and Corruption only


@dataclasses.dataclass()
class Part(BaseStruct):
    weight: float = prop(f32, id=0x1, prime=0, default=1.0)
    model: int = prop(asset("CMDL"), id=0x2, prime=1, default=UNSET)


@dataclasses.dataclass()
class ActorParameters(BaseStruct):
    fade_in_time: float = prop(f32, id=0x10, prime=0, default=1.0)
    visible: bool = prop(bool_, id=0x11, prime=1, default=True)
    max_volume: int = prop(s32, id=0x12, prime=2, default=127)
    parts: list[Part] = prop(array(struct_codec(Part)), id=0x13, prime=3)


@dataclasses.dataclass()
class Door(BaseObjectType, object_types={PRIME: 0x03, ECHOES: "DOOR", CORRUPTION: "DOOR"}):
    editor_properties: EditorProperties = prop(
        struct_codec(EditorProperties), id=0x255A4580, prime=PrimeEditor(active=7), games=ALL_GAMES
    )
    collision_box: Vector = prop(vector, id=0xF344C0B0, prime=4)
    actor_information: ActorParameters = prop(struct_codec(ActorParameters), id=0x7E397FED, prime=5)
    animation: AnimationParameters = prop(animation_parameters, id=0xE25FB08C, prime=6)
    shell_model: int = prop(asset("CMDL"), id=0xB20CC271, games=ECHOES | CORRUPTION, default=UNSET)
    is_open: bool = prop(
        bool_, id=0xA1DFFAD2, prime=8, default=UNSET, defaults={PRIME: True, ECHOES: True, CORRUPTION: False}
    )
    is_shield_down: bool = prop(bool_, id=0xAAAA0001, games=CORRUPTION)
    open_time: float = prop(f32, id=0x2007B71D, prime=9, default=0.5)
    effect: Effect = prop(enum_(Effect), id=0xAAAA0002, prime=10, default=Effect.Normal)
    weak_to: Weakness = prop(flags_(Weakness), id=0xAAAA0003, prime=11, default=Weakness(0))
    count: int = prop(s32, id=0xAAAA0004, prime=12, codecs={PRIME: u16})
    label: str = prop(string, id=0xAAAA0005, prime=13)
    tags: list[int] = prop(array(u32), id=0xAAAA0006, prime=14)
    ping: int = prop(sound, id=0xAAAA0007, prime=15)


# Helpers to write bytes


def prop_bytes(property_id: int, payload: bytes) -> bytes:
    return struct.pack(">LH", property_id, len(payload)) + payload


def id_struct(*props: bytes) -> bytes:
    return struct.pack(">H", len(props)) + b"".join(props)


def id_object(*props: bytes) -> bytes:
    payload = id_struct(*props)
    return b"\xff\xff\xff\xff" + struct.pack(">H", len(payload)) + payload


def prime_struct(count: int, *values: bytes) -> bytes:
    return struct.pack(">L", count) + b"".join(values)


def vec(x: float, y: float, z: float) -> bytes:
    return struct.pack(">fff", x, y, z)


def cstr(text: str) -> bytes:
    return text.encode() + b"\x00"


def echoes_transform(position: Vector, rotation: Vector, scale: Vector) -> bytes:
    return id_struct(
        prop_bytes(0x504F5321, vec(*position)),
        prop_bytes(0x524F5421, vec(*rotation)),
        prop_bytes(0x53434C21, vec(*scale)),
    )


def echoes_editor(name: str, active: bool, flags: int = 3) -> bytes:
    return id_struct(
        prop_bytes(0x494E414D, cstr(name)),
        prop_bytes(0x5846524D, echoes_transform(Vector(1, 2, 3), Vector(0, 0, 90), Vector(1, 1, 1))),
        prop_bytes(0x41435456, struct.pack(">?", active)),
        prop_bytes(0x5D298A43, struct.pack(">L", flags)),
    )


def make_editor(game: Game) -> EditorProperties:
    return EditorProperties(
        name="Door 1",
        transform=Transform(position=Vector(1, 2, 3), rotation=Vector(0, 0, 90)),
        active=False,
        game=game,
    )


def make_door(game: Game) -> Door:
    door = Door(
        editor_properties=make_editor(game),
        collision_box=Vector(4, 5, 6),
        actor_information=ActorParameters(fade_in_time=2.0, parts=[Part(weight=3.0, model=0x1234)]),
        animation=AnimationParameters(0xAABBCCDD, 2, 0 if game == Game.CORRUPTION else 3),
        open_time=0.25,
        effect=Effect.Ice if game != Game.PRIME else Effect.Fire,
        weak_to=Weakness.Beam | Weakness.Seeker if game != Game.PRIME else Weakness.Beam,
        count=300,
        label="hello",
        tags=[1, 2, 3],
        ping=77,
        game=game,
    )
    if game != Game.PRIME:
        door.shell_model = 0xB0B0B0B0
    if game == Game.CORRUPTION:
        door.is_shield_down = True
    return door


def prime_door_bytes() -> bytes:
    actor = prime_struct(
        4,
        struct.pack(">f?l", 2.0, True, 127),
        struct.pack(">L", 1),
        prime_struct(2, struct.pack(">fL", 3.0, 0x1234)),
    )
    return prime_struct(
        16,
        cstr("Door 1"),
        vec(1, 2, 3),
        vec(0, 0, 90),
        vec(1, 1, 1),
        vec(4, 5, 6),
        actor,
        struct.pack(">LLL", 0xAABBCCDD, 2, 3),
        struct.pack(">?", False),  # active, in the editor properties
        struct.pack(">?", True),  # is_open, the Prime default
        struct.pack(">f", 0.25),
        struct.pack(">L", 1),  # Fire
        struct.pack(">L", 1),  # Beam
        struct.pack(">H", 300),
        cstr("hello"),
        struct.pack(">L3L", 3, 1, 2, 3),
        struct.pack(">l", 77),
    )


def echoes_actor() -> bytes:
    return id_struct(
        prop_bytes(0x10, struct.pack(">f", 2.0)),
        prop_bytes(0x11, struct.pack(">?", True)),
        prop_bytes(0x12, struct.pack(">l", 127)),
        prop_bytes(
            0x13,
            struct.pack(">L", 1)
            + id_struct(prop_bytes(0x1, struct.pack(">f", 3.0)), prop_bytes(0x2, struct.pack(">L", 0x1234))),
        ),
    )


def echoes_door_bytes() -> bytes:
    return id_object(
        prop_bytes(0x255A4580, echoes_editor("Door 1", False)),
        prop_bytes(0xF344C0B0, vec(4, 5, 6)),
        prop_bytes(0x7E397FED, echoes_actor()),
        prop_bytes(0xE25FB08C, struct.pack(">LLL", 0xAABBCCDD, 2, 3)),
        prop_bytes(0xB20CC271, struct.pack(">L", 0xB0B0B0B0)),
        prop_bytes(0xA1DFFAD2, struct.pack(">?", True)),
        prop_bytes(0x2007B71D, struct.pack(">f", 0.25)),
        prop_bytes(0xAAAA0002, struct.pack(">L", 5)),  # Ice in Echoes
        prop_bytes(0xAAAA0003, struct.pack(">L", 1 | 8)),  # Seeker is 8 in Echoes
        prop_bytes(0xAAAA0004, struct.pack(">l", 300)),
        prop_bytes(0xAAAA0005, cstr("hello")),
        prop_bytes(0xAAAA0006, struct.pack(">L3L", 3, 1, 2, 3)),
        prop_bytes(0xAAAA0007, struct.pack(">l", 77)),
    )


def corruption_door_bytes() -> bytes:
    return id_object(
        prop_bytes(0x255A4580, echoes_editor("Door 1", False)),
        prop_bytes(0xF344C0B0, vec(4, 5, 6)),
        prop_bytes(
            0x7E397FED,
            id_struct(
                prop_bytes(0x10, struct.pack(">f", 2.0)),
                prop_bytes(0x11, struct.pack(">?", True)),
                prop_bytes(0x12, struct.pack(">l", 127)),
                prop_bytes(
                    0x13,
                    struct.pack(">L", 1)
                    + id_struct(prop_bytes(0x1, struct.pack(">f", 3.0)), prop_bytes(0x2, struct.pack(">Q", 0x1234))),
                ),
            ),
        ),
        prop_bytes(0xE25FB08C, struct.pack(">QL", 0xAABBCCDD, 2)),  # Corruption has no initial_anim
        prop_bytes(0xB20CC271, struct.pack(">Q", 0xB0B0B0B0)),
        prop_bytes(0xA1DFFAD2, struct.pack(">?", False)),
        prop_bytes(0xAAAA0001, struct.pack(">?", True)),
        prop_bytes(0x2007B71D, struct.pack(">f", 0.25)),
        prop_bytes(0xAAAA0002, struct.pack(">L", 2)),
        prop_bytes(0xAAAA0003, struct.pack(">L", 1 | 4)),
        prop_bytes(0xAAAA0004, struct.pack(">l", 300)),
        prop_bytes(0xAAAA0005, cstr("hello")),
        prop_bytes(0xAAAA0006, struct.pack(">L3L", 3, 1, 2, 3)),
        prop_bytes(0xAAAA0007, struct.pack(">l", 77)),
    )


DOOR_BYTES = {
    Game.PRIME: prime_door_bytes,
    Game.ECHOES: echoes_door_bytes,
    Game.CORRUPTION: corruption_door_bytes,
}
GAMES = [Game.PRIME, Game.ECHOES, Game.CORRUPTION]


# Defaults and the optional game


def test_no_game_yet():
    door = Door()
    assert door.game is None
    assert door.open_time == 0.5  # all games agree
    assert door.effect is Effect.Normal
    assert door.collision_box == Vector(0, 0, 0)
    assert door.tags == []
    # nested structs start out as structs without a game
    assert door.editor_properties.game is None
    assert door.editor_properties.active is True
    door.editor_properties.active = False
    assert door.editor_properties.active is False


def test_default_that_depends_on_game_is_unset():
    door = Door()
    with pytest.raises(GameNotSet, match=r"Door\.is_open.*CORRUPTION"):
        _ = door.is_open
    assert door.__dict__["is_open"] is UNSET

    # Writing is always fine
    door.is_open = False
    assert door.is_open is False


def test_asset_default_depends_on_game():
    door = Door()
    with pytest.raises(GameNotSet):
        _ = door.shell_model
    door.set_game(ECHOES)
    assert door.shell_model == 0xFFFFFFFF
    assert Door(game=CORRUPTION).shell_model == 0xFFFFFFFFFFFFFFFF


def test_unset_receives_the_default_of_the_game():
    assert Door(game=ECHOES).is_open is True
    assert Door(game=PRIME).is_open is True
    assert Door(game=CORRUPTION).is_open is False
    assert Door(is_open=False, game=ECHOES).is_open is False


def test_field_not_in_game_is_absent():
    door = Door(game=ECHOES)
    assert door.__dict__["is_shield_down"] is ABSENT
    with pytest.raises(FieldNotInGame, match="is_shield_down.*ECHOES"):
        _ = door.is_shield_down
    with pytest.raises(FieldNotInGame):
        door.is_shield_down = True
    assert not hasattr(door, "is_shield_down")

    # Writing the other games' fields before there is a game works, if the value isn't there when the game is set
    other = Door()
    other.is_shield_down = True
    with pytest.raises(FieldNotInGame, match="is_shield_down"):
        other.set_game(ECHOES)
    assert other.game is None
    other.set_game(CORRUPTION)
    assert other.is_shield_down is True


def test_field_given_with_the_default_value_is_not_an_error():
    door = Door(is_shield_down=False, shell_model=0xFFFFFFFF)
    door.set_game(PRIME)
    assert door.__dict__["is_shield_down"] is ABSENT
    assert door.__dict__["shell_model"] is ABSENT


def test_field_in_other_game_with_value_raises_on_set_game():
    door = Door(shell_model=0x1234)
    with pytest.raises(FieldNotInGame, match="shell_model"):
        door.set_game(PRIME)


def test_game_is_set_by_the_constructor_and_cannot_change():
    door = Door(game=ECHOES)
    assert door.game is ECHOES
    door.set_game(ECHOES)  # same game: nothing happens
    with pytest.raises(GameMismatch):
        door.set_game(CORRUPTION)
    with pytest.raises(GameMismatch):
        door.game = PRIME
    assert door.game is ECHOES


def test_class_not_in_game():
    @dataclasses.dataclass()
    class OnlyEchoes(BaseStruct):
        a: int = prop(u32, id=1)

    with pytest.raises(ClassNotInGame):
        OnlyEchoes(game=PRIME)
    assert OnlyEchoes.games() == {ECHOES, CORRUPTION}


def test_set_game_binds_nested_structs():
    door = Door(
        actor_information=ActorParameters(parts=[Part(model=5), Part()]),
        editor_properties=EditorProperties(transform=Transform()),
    )
    door.set_game(CORRUPTION)
    assert door.actor_information.game is CORRUPTION
    assert door.editor_properties.transform.game is CORRUPTION
    assert all(part.game is CORRUPTION for part in door.actor_information.parts)
    assert door.actor_information.parts[1].model == 0xFFFFFFFFFFFFFFFF


def test_assign_nested_struct_binds_it_in_place():
    door = Door(game=ECHOES)
    actor = ActorParameters(parts=[Part()])
    door.actor_information = actor
    assert actor.game is ECHOES
    assert door.actor_information is actor

    other = ActorParameters(game=CORRUPTION)
    with pytest.raises(GameMismatch):
        door.actor_information = other

    # The game of a struct that is not in a game yet doesn't change when it's assigned to an object without one
    free = ActorParameters()
    unbound = Door(actor_information=free)
    assert free.game is None
    assert unbound.actor_information is free


def test_shared_struct_gets_the_game_of_the_first_use():
    shared = ActorParameters()
    Door(actor_information=shared, game=ECHOES)
    assert shared.game is ECHOES
    with pytest.raises(GameMismatch):
        Door(actor_information=shared, game=CORRUPTION)


def test_to_bytes_sets_the_game():
    door = Door(count=1, label="x")
    door.shell_model = 5
    data = door.to_bytes(ECHOES)
    assert door.game is ECHOES
    assert data == door.to_bytes()
    with pytest.raises(GameMismatch):
        door.to_bytes(CORRUPTION)

    with pytest.raises(GameNotSet):
        Door().to_bytes()

    stream = io.BytesIO()
    Door(game=PRIME).to_stream(stream)
    assert stream.getvalue() == Door(game=PRIME).to_bytes()


# Encoding and decoding


@pytest.mark.parametrize("game", GAMES)
def test_encode(game: Game):
    assert make_door(game).to_bytes() == DOOR_BYTES[game]()


@pytest.mark.parametrize("game", GAMES)
def test_decode(game: Game):
    decoded = Door.from_bytes(DOOR_BYTES[game](), game)
    assert decoded.game is game
    expected = make_door(game)
    if game == Game.PRIME:
        # Prime stores the Active flag in the object, and keeps the defaults of everything it doesn't have
        pass
    assert decoded == expected
    assert type(decoded.editor_properties) is EditorProperties
    assert decoded.editor_properties.game is game
    assert decoded.actor_information.parts[0].game is game


@pytest.mark.parametrize("game", GAMES)
def test_round_trip(game: Game):
    data = DOOR_BYTES[game]()
    assert Door.from_bytes(data, game).to_bytes() == data


def test_decoded_object_has_absent_fields_marked():
    door = Door.from_bytes(prime_door_bytes(), Game.PRIME)
    assert door.__dict__["shell_model"] is ABSENT
    assert door.__dict__["is_shield_down"] is ABSENT
    assert door.editor_properties.name == "Door 1"
    assert door.editor_properties.active is False
    assert door.editor_properties.transform.rotation == Vector(0, 0, 90)
    assert door.get_name() == "Door 1"
    door.set_name("Other")
    assert door.editor_properties.name == "Other"
    assert door.to_bytes().startswith(prime_struct(16, cstr("Other")))


def test_prime_editor_properties_are_stored_in_the_object():
    door = Door(game=PRIME)
    door.editor_properties.name = "N"
    door.editor_properties.transform.position = Vector(9, 8, 7)
    door.editor_properties.active = False
    data = door.to_bytes()
    assert data[:4] == struct.pack(">L", 16)
    assert data[4:6] == b"N\x00"
    assert data[6:18] == vec(9, 8, 7)
    # the other fields are in the order of the positions, so the Active flag comes after the animation
    decoded = Door.from_bytes(data, Game.PRIME)
    assert decoded.editor_properties.active is False
    assert decoded.editor_properties.transform.position == Vector(9, 8, 7)


def test_virtual_fields_cannot_be_encoded_standalone():
    with pytest.raises(NotImplementedError):
        EditorProperties(game=PRIME).to_bytes()
    with pytest.raises(NotImplementedError):
        Transform.from_bytes(b"", Game.PRIME)


def test_fields_only_in_some_games_are_not_written():
    assert b"\xaa\xaa\x00\x01" not in echoes_door_bytes()
    # Corruption has one more property than Echoes
    assert struct.unpack(">H", Door(game=ECHOES).to_bytes()[6:8])[0] == 13
    assert struct.unpack(">H", Door(game=CORRUPTION).to_bytes()[6:8])[0] == 14


def test_decode_out_of_order_and_missing_properties():
    data = id_object(
        prop_bytes(0xA1DFFAD2, struct.pack(">?", False)),
        prop_bytes(0x2007B71D, struct.pack(">f", 0.75)),
        prop_bytes(0xAAAA0005, cstr("x")),
    )
    door = Door.from_bytes(data, Game.ECHOES)
    assert door.is_open is False
    assert door.open_time == 0.75
    assert door.label == "x"
    # Missing: the defaults of the game
    assert door.collision_box == Vector()
    assert door.shell_model == 0xFFFFFFFF
    assert door.editor_properties == EditorProperties(game=ECHOES)


def test_decode_unknown_property_fails():
    data = id_object(prop_bytes(0x12345678, b"\x00"))
    with pytest.raises(RuntimeError, match="Unknown property: 0x12345678"):
        Door.from_bytes(data, Game.ECHOES)


def test_struct_header_is_checked():
    with pytest.raises(AssertionError):
        Door.from_bytes(bytes(8), Game.ECHOES)


# Cook preferences, defaults of structs


@dataclasses.dataclass()
class Cooked(BaseStruct):
    always: int = prop(u32, id=0x1, default=1)
    never: int = prop(u32, id=0x2, default=2, cook=Cook.NEVER)
    default: int = prop(u32, id=0x3, default=3, cook=Cook.DEFAULT)
    only_if_modified: int = prop(u32, id=0x4, default=4, cook=Cook.ONLY_IF_MODIFIED)
    only_if_modified_struct: Part = prop(struct_codec(Part), id=0x5, cook="OnlyIfModified")
    text: str = prop(string, id=0x6, default="abc", cooks={ECHOES: Cook.ONLY_IF_MODIFIED})


@dataclasses.dataclass()
class CookedOwner(BaseStruct):
    plain: Cooked = prop(struct_codec(Cooked), id=0x1)
    overridden: Cooked = prop(
        struct_codec(Cooked, defaults={"default": 30, "only_if_modified": 40, "always": 10}), id=0x2
    )


def cooked_bytes(game: Game, **present: int | str) -> bytes:
    props = []
    for name, property_id, fmt in (
        ("always", 1, ">L"),
        ("default", 3, ">L"),
        ("only_if_modified", 4, ">L"),
    ):
        if name in present:
            props.append(prop_bytes(property_id, struct.pack(fmt, present[name])))
    if "text" in present:
        props.append(prop_bytes(6, cstr(str(present["text"]))))
    return id_struct(*props)


@pytest.mark.parametrize("game", [ECHOES, CORRUPTION])
def test_cook_preferences(game: Game):
    cooked = Cooked(always=11, never=22, default=33, only_if_modified=44, game=game)
    # never is not written, default is always written, only_if_modified and text have their value
    expected = [prop_bytes(1, struct.pack(">L", 11)), prop_bytes(3, struct.pack(">L", 33))]
    expected.append(prop_bytes(4, struct.pack(">L", 44)))
    if game == ECHOES:
        text = None
    else:
        text = prop_bytes(6, cstr("abc"))
    expected_data = id_struct(*expected, *([text] if text else []))
    assert cooked.to_bytes() == expected_data

    # OnlyIfModified skips what is equal to the default
    cooked = Cooked(always=11, only_if_modified=4, game=game)
    expected = [prop_bytes(1, struct.pack(">L", 11)), prop_bytes(3, struct.pack(">L", 3))]
    expected_data = id_struct(*expected, *([prop_bytes(6, cstr("abc"))] if game == CORRUPTION else []))
    assert cooked.to_bytes() == expected_data

    # and a struct that equals the default doesn't count as modified, even though it has a game
    cooked.only_if_modified_struct = Part()
    assert cooked.to_bytes() == expected_data
    cooked.only_if_modified_struct = Part(weight=2.0)
    assert cooked.to_bytes() != expected_data
    assert struct.unpack(">H", cooked.to_bytes()[:2])[0] == len(expected) + 1 + (game == CORRUPTION)


def test_decoding_cooked_uses_the_defaults_of_the_class():
    data = cooked_bytes(ECHOES, always=5)
    cooked = Cooked.from_bytes(data, Game.ECHOES)
    assert cooked == Cooked(always=5, game=ECHOES)


def test_default_override_of_a_struct_property():
    owner = CookedOwner(
        plain=Cooked(always=11, default=33, only_if_modified=44),
        overridden=Cooked(always=11, default=33, only_if_modified=40),
        game=ECHOES,
    )
    data = owner.to_bytes()
    plain = prop_bytes(0x1, cooked_bytes(ECHOES, always=11, default=33, only_if_modified=44))
    # With the override, only_if_modified=40 is not modified
    overridden = prop_bytes(0x2, cooked_bytes(ECHOES, always=11, default=33))
    assert data == id_struct(plain, overridden)

    # When reading, the override is the value of what is missing
    decoded = CookedOwner.from_bytes(data, Game.ECHOES)
    assert decoded.plain == Cooked(always=11, default=33, only_if_modified=44, game=ECHOES)
    assert decoded.overridden == Cooked(always=11, default=33, only_if_modified=40, game=ECHOES)


@dataclasses.dataclass()
class CookOverrideOwner(BaseStruct):
    # Same struct, the cook preference is changed by the field that holds it
    overridden: Cooked = prop(
        struct_codec(Cooked, cooks={"always": "OnlyIfModified", "only_if_modified": "Always", "never": "Always"}),
        id=0x2,
    )


def test_cook_override_of_a_struct_property():
    # `always` is omitted while it has its default (1), `only_if_modified` is always written, `never` too
    owner = CookOverrideOwner(overridden=Cooked(always=1, never=9, only_if_modified=4), game=ECHOES)
    inner = id_struct(
        prop_bytes(2, struct.pack(">L", 9)), prop_bytes(3, struct.pack(">L", 3)), prop_bytes(4, struct.pack(">L", 4))
    )
    assert owner.to_bytes() == id_struct(prop_bytes(0x2, inner))
    decoded = CookOverrideOwner.from_bytes(owner.to_bytes(), Game.ECHOES)
    assert decoded == owner

    owner.overridden.always = 5
    assert owner.to_bytes().count(struct.pack(">LH", 1, 4)) == 1


# Presence of optionally cooked properties: CookMode


def test_decoded_object_writes_back_what_it_was_read_with():
    # only_if_modified is in the data with its default value (4), which the template rules would leave out
    data = cooked_bytes(ECHOES, always=5, default=3, only_if_modified=4)
    decoded = Cooked.from_bytes(data, Game.ECHOES)
    assert decoded.to_bytes() == data
    assert decoded.to_bytes(cook=CookMode.PRESERVE) == data

    minimal = decoded.to_bytes(cook=CookMode.MINIMAL)
    assert minimal == cooked_bytes(ECHOES, always=5, default=3)
    # Preserve still works afterwards: MINIMAL doesn't forget anything
    assert decoded.to_bytes() == data

    # Written in the order of the data, which is not the order of the class
    swapped = id_struct(
        prop_bytes(4, struct.pack(">L", 4)), prop_bytes(3, struct.pack(">L", 3)), prop_bytes(1, struct.pack(">L", 5))
    )
    assert Cooked.from_bytes(swapped, Game.ECHOES).to_bytes() == swapped


def test_decoded_object_with_every_property_has_full_wire():
    part = prop_bytes(0x5, id_struct(prop_bytes(1, struct.pack(">f", 1.0)), prop_bytes(2, struct.pack(">L", 7))))
    data = id_struct(
        prop_bytes(1, struct.pack(">L", 5)),
        prop_bytes(3, struct.pack(">L", 3)),
        prop_bytes(4, struct.pack(">L", 4)),
        part,
        prop_bytes(6, cstr("abc")),
    )
    decoded = Cooked.from_bytes(data, Game.ECHOES)
    assert decoded.__dict__["_wire"] is FULL_WIRE
    assert copy.deepcopy(decoded).__dict__["_wire"] is FULL_WIRE
    assert decoded.to_bytes() == data
    assert copy.deepcopy(decoded).to_bytes() == data

    # The struct is not default, so only the optional integer and the string go away
    minimal = decoded.to_bytes(cook=CookMode.MINIMAL)
    assert minimal == id_struct(prop_bytes(1, struct.pack(">L", 5)), prop_bytes(3, struct.pack(">L", 3)), part)

    decoded.only_if_modified_struct = Part()
    assert decoded.to_bytes(cook=CookMode.MINIMAL) == id_struct(
        prop_bytes(1, struct.pack(">L", 5)), prop_bytes(3, struct.pack(">L", 3))
    )


def test_modified_after_decoding_is_written():
    data = cooked_bytes(ECHOES, always=5, default=3)
    decoded = Cooked.from_bytes(data, Game.ECHOES)
    decoded.only_if_modified = 8
    assert decoded.to_bytes() == id_struct(
        prop_bytes(1, struct.pack(">L", 5)),
        prop_bytes(3, struct.pack(">L", 3)),
        prop_bytes(4, struct.pack(">L", 8)),
    )
    decoded.only_if_modified = 4  # back to the default: it was not in the data
    assert decoded.to_bytes() == data


def test_presence_is_not_part_of_the_value():
    with_default = Cooked.from_bytes(cooked_bytes(ECHOES, always=5, default=3, only_if_modified=4), Game.ECHOES)
    without = Cooked.from_bytes(cooked_bytes(ECHOES, always=5, default=3), Game.ECHOES)
    assert with_default == without
    assert with_default == Cooked(always=5, game=ECHOES)
    assert with_default.to_json() == without.to_json()


def test_presence_with_copy_replace_and_to_game():
    data = cooked_bytes(ECHOES, always=5, default=3, only_if_modified=4)
    decoded = Cooked.from_bytes(data, Game.ECHOES)

    assert copy.deepcopy(decoded).to_bytes() == data  # copies keep it
    assert copy.copy(decoded).to_bytes() == data
    # new objects have no presence: template rules
    replaced = dataclasses.replace(decoded, always=6)
    assert replaced.to_bytes() == cooked_bytes(ECHOES, always=6, default=3)
    assert "_wire" not in decoded.to_game(CORRUPTION).__dict__
    assert "_wire" not in Cooked.from_json(decoded.to_json()).__dict__


def test_nested_presence_and_minimal():
    inner = cooked_bytes(ECHOES, always=5, default=3, only_if_modified=4)
    data = id_struct(prop_bytes(0x1, inner))
    owner = CookedOwner.from_bytes(data, Game.ECHOES)
    assert owner.to_bytes() == data
    minimal = owner.to_bytes(cook=CookMode.MINIMAL)
    expected = CookedOwner(plain=Cooked(always=5, default=3), game=ECHOES).to_bytes(cook=CookMode.MINIMAL)
    assert minimal == expected
    assert owner.to_bytes() == data


# Prime: counts, atomic structs, conditional properties, orders


@dataclasses.dataclass()
class WaterLike(BaseStruct):
    enabled: bool = prop(bool_, prime=0, id=0x1)
    extra: int = prop(u32, prime=1, only_if="enabled", id=0x2)
    always: float = prop(f32, prime=2, id=0x3)


def test_prime_conditional_property():
    on = WaterLike(enabled=True, extra=5, always=1.0, game=PRIME)
    assert on.to_bytes() == prime_struct(3, b"\x01", struct.pack(">L", 5), struct.pack(">f", 1.0))
    off = WaterLike(enabled=False, extra=5, always=1.0, game=PRIME)
    # the count is the same
    assert off.to_bytes() == prime_struct(3, b"\x00", struct.pack(">f", 1.0))

    decoded = WaterLike.from_bytes(off.to_bytes(), Game.PRIME)
    assert decoded.extra == 0
    assert WaterLike.from_bytes(on.to_bytes(), Game.PRIME) == on


@dataclasses.dataclass()
class Trailing(BaseStruct):
    """Prime struct with two required properties, and optional ones: one with a count of 4, two with a count of 6."""

    a: int = prop(u32, prime=0, id=0x1)
    b: int = prop(u32, prime=1, id=0x2)
    c: int = prop(u32, prime=(2, 3), id=0x3, default=7)
    d: float = prop(f32, prime=(3, 5), id=0x4)
    e: bool = prop(bool_, prime=(4, 5), id=0x5)


def trailing_bytes(count: int) -> bytes:
    values = [struct.pack(">L", 1), struct.pack(">L", 2), struct.pack(">L", 3), struct.pack(">f", 4.0), b"\x01"]
    return prime_struct(count, *values[:count])


def test_optional_properties_are_read_when_the_count_allows():
    short = Trailing.from_bytes(trailing_bytes(2), Game.PRIME)
    assert (short.a, short.b, short.c, short.d, short.e) == (1, 2, 7, 0.0, False)

    middle = Trailing.from_bytes(trailing_bytes(3), Game.PRIME)
    assert (middle.c, middle.d, middle.e) == (3, 0.0, False)

    # the two last properties come together: a count of 4 reads only the first optional property
    four = Trailing.from_bytes(trailing_bytes(4), Game.PRIME)
    assert (four.c, four.d, four.e) == (3, 0.0, False)

    full = Trailing.from_bytes(trailing_bytes(5), Game.PRIME)
    assert (full.c, full.d, full.e) == (3, 4.0, True)


def test_preserve_writes_the_properties_that_were_read():
    for count in (2, 3, 5):
        data = trailing_bytes(count)
        obj = Trailing.from_bytes(data, Game.PRIME)
        assert obj.to_bytes() == data
        assert Trailing.from_bytes(obj.to_bytes(), Game.PRIME) == obj

    # presence is not part of equality
    assert Trailing.from_bytes(trailing_bytes(2), Game.PRIME) == Trailing(a=1, b=2, game=PRIME)

    # a copy remembers it too
    assert copy.deepcopy(Trailing.from_bytes(trailing_bytes(3), Game.PRIME)).to_bytes() == trailing_bytes(3)


def test_minimal_drops_trailing_defaults():
    full_defaults = Trailing(a=1, b=2, c=7, d=0.0, e=False, game=PRIME)
    assert full_defaults.to_bytes() == prime_struct(2, struct.pack(">L", 1), struct.pack(">L", 2))

    obj = Trailing.from_bytes(trailing_bytes(5), Game.PRIME)
    obj.c = 7
    obj.d = 0.0
    obj.e = False
    # PRESERVE keeps them
    assert obj.to_bytes() == prime_struct(
        5, struct.pack(">L", 1), struct.pack(">L", 2), struct.pack(">L", 7), struct.pack(">f", 0.0), b"\x00"
    )
    assert obj.to_bytes(cook=CookMode.MINIMAL) == prime_struct(2, struct.pack(">L", 1), struct.pack(">L", 2))

    # a default in the middle is written when something after it is not
    obj = Trailing(a=1, b=2, e=True, game=PRIME)
    assert obj.to_bytes(cook=CookMode.MINIMAL) == prime_struct(
        5, struct.pack(">L", 1), struct.pack(">L", 2), struct.pack(">L", 7), struct.pack(">f", 0.0), b"\x01"
    )


def test_modifying_an_optional_property_of_a_short_object_writes_it():
    obj = Trailing.from_bytes(trailing_bytes(2), Game.PRIME)
    obj.c = 9
    assert obj.to_bytes() == prime_struct(3, struct.pack(">L", 1), struct.pack(">L", 2), struct.pack(">L", 9))

    obj = Trailing.from_bytes(trailing_bytes(3), Game.PRIME)
    obj.d = 2.0
    assert obj.to_bytes() == prime_struct(
        5, struct.pack(">L", 1), struct.pack(">L", 2), struct.pack(">L", 3), struct.pack(">f", 2.0), b"\x00"
    )
    assert Trailing.from_bytes(obj.to_bytes(), Game.PRIME) == obj


def test_optional_properties_do_not_change_other_games():
    obj = Trailing(a=1, b=2, game=ECHOES)
    assert Trailing.from_bytes(obj.to_bytes(), Game.ECHOES) == obj
    assert obj.to_game(Game.PRIME).to_bytes() == prime_struct(2, struct.pack(">L", 1), struct.pack(">L", 2))


@dataclasses.dataclass()
class Interleaved(BaseStruct):
    """The last property is always there, after the optional one."""

    a: int = prop(u32, prime=0)
    b: int = prop(u32, prime=(1, 3), default=5)
    c: int = prop(u32, prime=2)


def test_required_property_after_an_optional_one():
    short = Interleaved.from_bytes(prime_struct(2, struct.pack(">L", 1), struct.pack(">L", 3)), Game.PRIME)
    assert (short.a, short.b, short.c) == (1, 5, 3)
    assert short.to_bytes() == prime_struct(2, struct.pack(">L", 1), struct.pack(">L", 3))

    full_data = prime_struct(3, struct.pack(">L", 1), struct.pack(">L", 2), struct.pack(">L", 3))
    full = Interleaved.from_bytes(full_data, Game.PRIME)
    assert (full.a, full.b, full.c) == (1, 2, 3)
    assert full.to_bytes() == full_data


def test_optional_properties_must_have_consistent_counts():
    @dataclasses.dataclass()
    class Wrong(BaseStruct):
        a: int = prop(u32, prime=0)
        b: int = prop(u32, prime=(1, 5))  # 2 properties can never be read with a count of 5

    with pytest.raises(ValueError, match="too few"):
        Wrong.from_bytes(prime_struct(1, struct.pack(">L", 1)), Game.PRIME)


@dataclasses.dataclass()
class Pair(BaseStruct, atomic=[PRIME, ECHOES]):
    first: float = prop(f32, id=0x1, prime=1)
    second: float = prop(f32, id=0x2, prime=0, order={ECHOES: 5})
    third: int = prop(u8, id=0x3, prime=2, order={ECHOES: 1})


def test_atomic_struct_has_no_count_and_follows_the_order_of_each_game():
    pair = Pair(first=1.0, second=2.0, third=3, game=PRIME)
    assert pair.to_bytes() == struct.pack(">ffB", 2.0, 1.0, 3)  # by position
    assert Pair.from_bytes(pair.to_bytes(), Game.PRIME) == pair

    pair = Pair(first=1.0, second=2.0, third=3, game=ECHOES)
    assert pair.to_bytes() == struct.pack(">fBf", 1.0, 3, 2.0)  # by order, then declaration
    assert Pair.from_bytes(pair.to_bytes(), Game.ECHOES) == pair

    # Corruption is not atomic
    pair = Pair(first=1.0, second=2.0, third=3, game=CORRUPTION)
    assert pair.to_bytes() == id_struct(
        prop_bytes(0x1, struct.pack(">f", 1.0)), prop_bytes(0x2, struct.pack(">f", 2.0)), prop_bytes(0x3, b"")
    )


@dataclasses.dataclass()
class Reordered(BaseStruct):
    a: int = prop(u32, id=0xA, prime=0)
    b: int = prop(u32, id=0xB, prime=2, order={CORRUPTION: 10})
    c: int = prop(u32, id=0xC, prime=1, order={CORRUPTION: -1})


def test_games_can_write_in_different_orders():
    obj = Reordered(a=1, b=2, c=3, game=ECHOES)
    assert obj.to_bytes() == id_struct(
        *(prop_bytes(i, struct.pack(">L", v)) for i, v in ((0xA, 1), (0xB, 2), (0xC, 3)))
    )
    obj = Reordered(a=1, b=2, c=3, game=CORRUPTION)
    assert obj.to_bytes() == id_struct(
        *(prop_bytes(i, struct.pack(">L", v)) for i, v in ((0xC, 3), (0xA, 1), (0xB, 2)))
    )
    obj = Reordered(a=1, b=2, c=3, game=PRIME)
    assert obj.to_bytes() == prime_struct(3, *(struct.pack(">L", v) for v in (1, 3, 2)))
    for game in GAMES:
        original = Reordered(a=1, b=2, c=3, game=game)
        assert Reordered.from_bytes(original.to_bytes(), game) == original


@dataclasses.dataclass()
class Incomplete(BaseStruct):
    known: int = prop(u32, id=0x1)
    unknown_properties: dict[int, bytes] = unknown_properties()


def test_unknown_properties_are_kept():
    data = id_struct(prop_bytes(0x1, struct.pack(">L", 7)), prop_bytes(0x99, b"\x01\x02\x03"), prop_bytes(0x98, b""))
    obj = Incomplete.from_bytes(data, Game.ECHOES)
    assert obj.known == 7
    assert obj.unknown_properties == {0x99: b"\x01\x02\x03", 0x98: b""}
    # the count is the known properties plus the unknown ones, which are written after
    assert obj.to_bytes() == data
    assert Incomplete.from_json(obj.to_json()) == obj
    assert obj.to_json()["unknown_properties"] == {"0x99": "AQID", "0x98": ""}
    assert list(obj.dependencies_for(None)) == []  # type: ignore[arg-type]
    assert Incomplete(known=1, game=ECHOES).to_bytes() == id_struct(prop_bytes(0x1, struct.pack(">L", 1)))


# JSON


@pytest.mark.parametrize("game", GAMES)
def test_json_round_trip(game: Game):
    door = make_door(game)
    data = typing.cast("dict[str, typing.Any]", door.to_json())
    assert data["game"] == game.name
    assert "game" not in data["actor_information"]
    assert data["collision_box"] == {"x": 4, "y": 5, "z": 6}
    expected_effect = {Game.PRIME: 1, Game.ECHOES: 5, Game.CORRUPTION: 2}[game]
    assert data["effect"] == expected_effect
    assert ("shell_model" in data) == (game != Game.PRIME)

    decoded = Door.from_json(data)
    assert decoded == door
    assert decoded.to_bytes() == DOOR_BYTES[game]()


def test_json_requires_a_game():
    with pytest.raises(GameNotSet):
        Door().to_json()


# to_game


def test_to_game_keeps_shared_fields_and_converts_enums():
    door = make_door(Game.ECHOES)
    door.shell_model = 0x1234
    converted = door.to_game(CORRUPTION)
    assert converted is not door
    assert converted.game is CORRUPTION
    assert door.game is ECHOES
    assert converted.effect is Effect.Ice
    assert converted.weak_to == Weakness.Beam | Weakness.Seeker
    assert converted.is_shield_down is False  # default of the target
    assert converted.is_open is True  # copied from the source, not the default of the target
    assert converted.shell_model == 0x1234
    assert converted.actor_information.game is CORRUPTION
    assert converted.actor_information.parts[0].game is CORRUPTION
    assert converted.actor_information.parts[0].model == 0x1234
    assert converted.actor_information is not door.actor_information
    assert converted.to_bytes() != door.to_bytes()
    converted.animation.initial_anim = 0  # Corruption doesn't store it
    assert Door.from_bytes(converted.to_bytes(), Game.CORRUPTION) == converted


def test_to_game_raises_for_non_default_values_of_missing_fields():
    door = make_door(Game.CORRUPTION)
    with pytest.raises(FieldNotInGame, match="is_shield_down"):
        door.to_game(ECHOES)
    door.is_shield_down = False
    assert door.to_game(ECHOES).game is ECHOES


def test_to_game_to_prime_requires_defaults():
    door = Door(game=ECHOES)
    prime = door.to_game(PRIME)
    assert prime.game is PRIME
    assert prime.__dict__["shell_model"] is ABSENT
    door.shell_model = 3
    with pytest.raises(FieldNotInGame):
        door.to_game(PRIME)


def test_to_game_from_a_door_without_game():
    door = Door(count=7)
    converted = door.to_game(ECHOES)
    assert converted.game is ECHOES
    assert converted.count == 7
    assert converted.is_open is True
    assert door.game is None


def test_enum_member_that_the_game_does_not_have():
    door = make_door(Game.ECHOES)
    door.shell_model = 0xFFFFFFFF
    assert door.effect is Effect.Ice
    with pytest.raises(MemberNotInGame, match=r"Effect.Ice.*PRIME"):
        door.to_game(PRIME)
    door.effect = Effect.Fire
    door.weak_to = Weakness.Seeker
    with pytest.raises(MemberNotInGame, match="Seeker"):
        door.to_game(PRIME)
    door.weak_to = Weakness.Beam
    assert door.to_game(PRIME).effect is Effect.Fire

    # and when writing
    with pytest.raises(MemberNotInGame):
        Door(effect=Effect.Ice, game=PRIME).to_bytes()


def test_flags_are_translated_bit_by_bit_and_keep_unknown_bits():
    door = Door(weak_to=Weakness(Weakness.Beam | 0x100), game=ECHOES)
    data = door.to_bytes()
    decoded = Door.from_bytes(data, Game.ECHOES)
    assert decoded.weak_to == Weakness.Beam | 0x100

    door = Door(weak_to=Weakness.Seeker | Weakness.Missile, game=ECHOES)
    assert door.to_json()["weak_to"] == 8 | 2
    assert Door.from_json(door.to_json()).weak_to == Weakness.Seeker | Weakness.Missile


def test_enums_with_the_same_values_in_every_game_need_nothing():
    @dataclasses.dataclass()
    class WithEnum(BaseStruct):
        value: Same = prop(enum_(Same), id=1, default=Same.B)

    obj = WithEnum(game=ECHOES)
    assert obj.to_bytes() == id_struct(prop_bytes(1, struct.pack(">L", 7)))
    assert WithEnum.from_bytes(obj.to_bytes(), Game.CORRUPTION).value is Same.B
    with pytest.raises(ValueError, match="9"):
        WithEnum.from_bytes(id_struct(prop_bytes(1, struct.pack(">L", 9))), Game.ECHOES)


def test_enum_value_not_in_the_game():
    data = id_object(prop_bytes(0xAAAA0002, struct.pack(">L", 2)))
    with pytest.raises(ValueError, match="2"):
        Door.from_bytes(data, Game.ECHOES)  # Ice is 5 in Echoes
    assert Door.from_bytes(data, Game.CORRUPTION).effect is Effect.Ice


# dataclasses


@pytest.mark.parametrize("game", GAMES)
def test_dataclasses_replace(game: Game):
    door = make_door(game)
    other = dataclasses.replace(door, open_time=9.0)
    assert other.game is game
    assert other.open_time == 9.0
    assert other.collision_box == door.collision_box
    assert other.__dict__["is_shield_down"] == door.__dict__["is_shield_down"]
    assert other is not door
    assert dataclasses.replace(other, open_time=0.25) == door


def test_dataclasses_replace_without_game():
    door = Door(open_time=3.0)
    other = dataclasses.replace(door, label="x")
    assert other.game is None
    assert other.__dict__["is_open"] is UNSET
    assert other.label == "x"
    assert other.open_time == 3.0


def test_replace_cannot_write_missing_fields():
    door = make_door(Game.ECHOES)
    with pytest.raises(FieldNotInGame):
        dataclasses.replace(door, is_shield_down=True)


@pytest.mark.parametrize("game", [None, *GAMES])
def test_deepcopy(game: Game | None):
    door = make_door(game) if game is not None else Door(label="x")
    clone = copy.deepcopy(door)
    assert clone == door
    assert clone is not door
    assert clone.game is door.game
    assert clone.actor_information is not door.actor_information
    assert clone.collision_box is not door.collision_box
    assert copy.deepcopy(door.__dict__["is_open"]) is door.__dict__["is_open"]
    if game is not None:
        assert clone.to_bytes() == door.to_bytes()
    clone.tags.append(5)
    assert door.tags != clone.tags
    assert copy.copy(door) == door


def test_equality_and_repr():
    assert Door(label="x") == Door(label="x")
    assert Door(label="x") != Door(label="y")
    assert Door(game=ECHOES) != Door(game=CORRUPTION)
    assert Door(game=ECHOES) != Door()
    assert "game=Game.ECHOES" in repr(Door(game=ECHOES))
    assert repr(Door(label="x")).startswith("Door(editor_properties=EditorProperties(")
    assert "is_open=UNSET" in repr(Door())
    assert dataclasses.asdict(Door())["is_open"] is UNSET


def test_object_class_data():
    assert Door.object_type(Game.PRIME) == 3
    assert Door.object_type(Game.ECHOES) == "DOOR"
    assert Door.games() == {PRIME, ECHOES, CORRUPTION}
    assert make_door(Game.PRIME).get_name() == "Door 1"

    @dataclasses.dataclass()
    class NoName(BaseObjectType, object_types={ECHOES: "NONE"}):
        pass

    with pytest.raises(ClassNotInGame):
        NoName.object_type(PRIME)
    with pytest.raises(RuntimeError, match="does not have name"):
        NoName().get_name()


# Reflection


def test_reflection_for_a_game():
    echoes = get_reflection(Door, ECHOES)
    assert "shell_model" in echoes
    assert "is_shield_down" not in echoes
    assert echoes["shell_model"].id == 0xB20CC271
    assert echoes["shell_model"].type is int
    assert echoes["actor_information"].type is ActorParameters
    assert echoes["tags"].type is list
    assert echoes["effect"].type is Effect
    assert echoes["effect"].to_json(Effect.Ice) == 5
    assert echoes["effect"].from_json(5) is Effect.Ice

    corruption = get_reflection(Door, CORRUPTION)
    assert "is_shield_down" in corruption
    assert corruption["effect"].to_json(Effect.Ice) == 2
    assert corruption["collision_box"].to_json(Vector(1, 2, 3)) == {"x": 1, "y": 2, "z": 3}

    prime = get_reflection(Door, PRIME)
    assert "shell_model" not in prime
    assert prime["collision_box"].id == 4
    assert prime["count"].id == 12

    names = [f.name for f in dataclasses.fields(Door)]
    assert names[1:4] == ["editor_properties", "collision_box", "actor_information"]
    assert "shell_model" in names and "is_shield_down" in names  # fields of every game


def test_asset_types_in_metadata():
    by_name = {f.name: f for f in dataclasses.fields(Door)}
    assert by_name["shell_model"].metadata["asset_types"] == ["CMDL"]
    assert by_name["ping"].metadata["sound"] is True
    assert "asset_types" not in by_name["count"].metadata


def test_reflection_of_handwritten_classes():
    reflection = get_reflection(Spline, ECHOES)
    assert reflection["knots"].id == 2


# Other codecs


@dataclasses.dataclass()
class Misc(BaseStruct):
    color: Color = prop(color, id=0x1, prime=0)
    spline: Spline = prop(spline, id=0x2, prime=1)
    guid: bytes = prop(guid, id=0x3, prime=2)
    small: int = prop(s16, id=0x4, prime=3, default=-2)
    wide: int = prop(u8, id=0x5, prime=4, default=250)


@pytest.mark.parametrize("game", GAMES)
def test_misc_codecs(game: Game):
    obj = Misc(
        color=Color(1.0, 0.5, 0.25, 0.0),
        spline=Spline(knots=[], minimum_amplitude=-1.0, maximum_amplitude=1.0),
        guid=bytes(range(16)),
        game=game,
    )
    data = obj.to_bytes()
    spline_bytes = struct.pack(">BBL", 0, 0, 0) + struct.pack(">Bff", 0, -1.0, 1.0)
    values = [
        struct.pack(">ffff", 1.0, 0.5, 0.25, 0.0),
        spline_bytes,
        bytes(range(16)),
        struct.pack(">h", -2),
        struct.pack(">B", 250),
    ]
    if game == Game.PRIME:
        assert data == prime_struct(5, *values)
    else:
        ids = [1, 2, 3, 4, 5]
        assert data == id_struct(*(prop_bytes(i, v) for i, v in zip(ids, values, strict=True)))
    decoded = Misc.from_bytes(data, game)
    assert decoded == obj
    assert Misc.from_json(obj.to_json()) == obj
    assert obj.to_json()["guid"] == bytes(range(16)).hex()


def test_animation_parameters_default_is_written_as_the_invalid_asset_of_the_game():
    door = Door()
    door.shell_model = 1
    assert door.to_game(CORRUPTION).animation == AnimationParameters(0xFFFFFFFF, 0, 0)
    data = Door(game=CORRUPTION).to_bytes()
    assert prop_bytes(0xE25FB08C, struct.pack(">QL", 0xFFFFFFFFFFFFFFFF, 0)) in data


def test_empty_array_and_array_of_structs_decode():
    door = Door(game=ECHOES)
    decoded = Door.from_bytes(door.to_bytes(), Game.ECHOES)
    assert decoded.tags == []
    assert decoded.actor_information.parts == []
    decoded.actor_information.parts.append(Part(weight=2.0))
    assert Door.from_bytes(decoded.to_bytes(), Game.ECHOES).actor_information.parts[0].weight == 2.0


def test_array_elements_are_bound_when_written():
    door = Door(game=ECHOES)
    part = Part()
    door.actor_information.parts.append(part)
    assert part.game is None
    door.to_bytes()
    assert part.game is ECHOES


# Dependencies


class FakeAssetManager:
    def __init__(self):
        self.requested = []

    def get_dependencies_for_asset(self, asset_id, **kwargs):
        from retro_data_structures.base_resource import Dependency

        self.requested.append(("asset", asset_id))
        yield Dependency("CMDL", asset_id, False)

    def get_audio_group_dependency(self, sound_id):
        from retro_data_structures.base_resource import Dependency

        self.requested.append(("sound", sound_id))
        yield Dependency("AGSC", sound_id, False)

    def get_dependencies_for_ancs(self, asset_id, char_index=None):
        from retro_data_structures.base_resource import Dependency

        self.requested.append(("ancs", asset_id, char_index))
        yield Dependency("ANCS", asset_id, False)


def test_dependencies():
    door = make_door(Game.ECHOES)
    manager = FakeAssetManager()
    deps = list(door.dependencies_for(manager))  # type: ignore[arg-type]
    assert manager.requested == [
        ("asset", 0x1234),  # in the array of structs, in actor_information
        ("ancs", 0xAABBCCDD, 2),
        ("asset", 0xB0B0B0B0),
        ("sound", 77),
    ]
    assert [d.type for d in deps] == ["CMDL", "ANCS", "CMDL", "AGSC"]


def test_dependencies_error_names_the_field():
    class Broken(FakeAssetManager):
        def get_dependencies_for_asset(self, asset_id, **kwargs):
            raise KeyError(asset_id)

    door = make_door(Game.ECHOES)
    with pytest.raises(Exception, match=r"Error finding dependencies for Door\.actor_information"):
        list(door.dependencies_for(Broken()))  # type: ignore[arg-type]


def test_mlvl_and_mrea_assets_have_no_dependencies():
    @dataclasses.dataclass()
    class Level(BaseStruct):
        world: int = prop(asset("MLVL"), id=1, default=UNSET)
        weird: int = prop(asset("TXTR", ignore_dependencies_mlvl=True), id=2, default=UNSET)

    manager = FakeAssetManager()
    deps = list(Level(world=5, weird=6, game=ECHOES).dependencies_for(manager))  # type: ignore[arg-type]
    assert manager.requested == [("asset", 6)]
    assert [(d.id, d.exclude_for_mlvl) for d in deps] == [(6, True)]


# Micro-benchmark. Skipped by default: RDS_BENCHMARK=1 pytest tests/properties/test_merged_runtime.py -k benchmark -s


@dataclasses.dataclass()
class Flat(BaseStruct, games=ECHOES | CORRUPTION):
    a: float = prop(f32, id=0x10000001, default=1.0)
    b: int = prop(u32, id=0x10000002)
    c: bool = prop(bool_, id=0x10000003)
    d: float = prop(f32, id=0x10000004)
    e: int = prop(s32, id=0x10000005)


_FLAT_NAIVE = {
    0x10000001: ("a", ">f"),
    0x10000002: ("b", ">L"),
    0x10000003: ("c", ">?"),
    0x10000004: ("d", ">f"),
    0x10000005: ("e", ">l"),
}


def _naive_decode(data: bytes) -> Flat:
    (count,) = struct.unpack_from(">H", data, 0)
    offset = 2
    values = {}
    for _ in range(count):
        prop_id, size = struct.unpack_from(">LH", data, offset)
        offset += 6
        name, fmt = _FLAT_NAIVE[prop_id]
        (values[name],) = struct.unpack_from(fmt, data, offset)
        offset += size
    return Flat(**values, game=ECHOES)


def _naive_encode(flat: Flat) -> bytes:
    out = [struct.pack(">H", len(_FLAT_NAIVE))]
    for prop_id, (name, fmt) in _FLAT_NAIVE.items():
        payload = struct.pack(fmt, getattr(flat, name))
        out.append(struct.pack(">LH", prop_id, len(payload)) + payload)
    return b"".join(out)


@pytest.mark.skipif(not os.environ.get("RDS_BENCHMARK"), reason="set RDS_BENCHMARK=1 to run the benchmark")
def test_benchmark_compiled_vs_naive():
    import timeit

    flat = Flat(a=1.5, b=2, c=True, d=4.0, e=-5, game=ECHOES)
    data = flat.to_bytes()
    assert _naive_encode(flat) == data
    assert _naive_decode(data) == flat

    n = 20000
    results = {
        "decode compiled": timeit.timeit(lambda: Flat.from_bytes(data, ECHOES), number=n),
        "decode naive loop": timeit.timeit(lambda: _naive_decode(data), number=n),
        "encode compiled": timeit.timeit(flat.to_bytes, number=n),
        "encode naive loop": timeit.timeit(lambda: _naive_encode(flat), number=n),
    }
    plain = dataclasses.make_dataclass("Plain", ["a", "b", "c", "d", "e"])(1.5, 2, True, 4.0, -5)
    results["field read (guarded)"] = timeit.timeit(lambda: flat.a, number=n * 10)
    results["field read (plain dataclass)"] = timeit.timeit(lambda: plain.a, number=n * 10)
    for name, seconds in results.items():
        count = n * 10 if name.startswith("field") else n
        print(f"{name:32} {seconds / count * 1e6:8.3f} us")


def test_string_with_invalid_utf8_round_trips():
    data = id_struct(prop_bytes(6, b"\xff\x99ab\x00"))
    cooked = Cooked.from_bytes(data, Game.CORRUPTION)
    assert prop_bytes(6, b"\xff\x99ab\x00") in cooked.to_bytes()


def test_defaults_that_differ_between_games_need_unset():
    with pytest.raises(TypeError, match="needs `default=UNSET`"):
        prop(bool_, id=0x1, prime=0, default=True, defaults={CORRUPTION: False})
    with pytest.raises(TypeError, match="needs `default=UNSET`"):
        prop(bool_, id=0x1, prime=0, defaults={CORRUPTION: True})
    with pytest.raises(ValueError, match="different defaults"):
        prop(asset("CMDL"), id=0x1)  # The invalid asset id is 32 bits in Echoes and 64 in Corruption
    with pytest.raises(ValueError, match="same default"):
        prop(bool_, id=0x1, prime=0, default=UNSET, defaults={PRIME: True, ECHOES: True, CORRUPTION: True})

    field = prop(bool_, id=0x1, prime=0, default=UNSET, defaults={PRIME: True, CORRUPTION: True})
    assert field.default is UNSET
    assert {g: lay.default.value for g, lay in field.metadata["layout"].items()} == {
        PRIME: True,
        ECHOES: False,
        CORRUPTION: True,
    }
