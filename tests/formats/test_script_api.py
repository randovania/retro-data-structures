from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

import retro_data_structures.enums.echoes as _echoes_enums
import retro_data_structures.enums.prime as _prime_enums
from retro_data_structures.formats import script_object
from retro_data_structures.formats.script_object import InstanceId

if TYPE_CHECKING:
    from retro_data_structures.formats.mlvl import Area, Mlvl


@pytest.mark.parametrize(
    ["layer", "area", "instance", "expected"],
    [
        (0, 0, 0, 0x00000000),
        (1, 0, 0, 0x04000000),
        (0, 1, 0, 0x00010000),
        (0, 0, 1, 0x00000001),
        (5, 2, 1, 0x14020001),
    ],
)
def test_instance_id_new(layer, area, instance, expected):
    assert InstanceId.new(layer, area, instance) == expected


@pytest.mark.parametrize(
    ["correct_type", "value", "expected"],
    [
        (_prime_enums.State, _prime_enums.State.Exited, _prime_enums.State.Exited),
        (_prime_enums.State, _echoes_enums.State.Exited, _prime_enums.State.Exited),
        (_echoes_enums.State, _prime_enums.State.Exited, _echoes_enums.State.Exited),
        (_echoes_enums.State, "EXIT", _echoes_enums.State.Exited),
        (_echoes_enums.State, _echoes_enums.State.Exited, _echoes_enums.State.Exited),
    ],
)
def test_resolve_to_enum(correct_type, value, expected):
    assert script_object._resolve_to_enum(correct_type, value) == expected


@pytest.fixture
def prime2_mlvl(prime2_asset_manager) -> Mlvl:
    # Agon Wastes
    return prime2_asset_manager.get_parsed_asset(0x42B935E4)


@pytest.fixture
def prime2_area(prime2_mlvl: Mlvl) -> Area:
    # Storage C
    return prime2_mlvl.get_area(0x5DFA984F)


# Area
@pytest.mark.xfail(reason="This feature had never been tested and does not work")
@pytest.mark.parametrize("active", (False, True))
def test_add_layer(prime2_area: Area, active: bool):
    layer = prime2_area.add_layer("Test", active)
    assert layer.active == active
    assert layer.index == 2


def test_get_instance(prime2_area: Area):
    idx, name = 0x0045006B, "Pickup Object"
    inst = prime2_area.get_instance(idx)
    assert inst.name == name

    inst = prime2_area.get_instance(name)
    assert inst.id == idx


def test_remove_instance(prime2_area: Area):
    old_len = len(list(prime2_area.all_instances))
    prime2_area.remove_instance("Pickup Object")
    assert len(list(prime2_area.all_instances)) == old_len - 1


# Script Layer
def test_add_instance(prime2_area: Area):
    from retro_data_structures.enums import echoes
    from retro_data_structures.properties.echoes.objects.SpecialFunction import SpecialFunction

    inst = prime2_area.get_layer("Default").add_instance_with(
        SpecialFunction(
            function=echoes.Function.Darkworld,
        )
    )
    assert inst.type == SpecialFunction
    assert prime2_area.mrea.build() is not None


def test_add_memory_relay(prime2_area: Area):
    relay = prime2_area.get_layer("Default").add_memory_relay("Test")
    save = prime2_area._parent_mlvl.savw

    assert any(state["instance_id"] == relay.id for state in save.raw.memory_relays)


@pytest.mark.parametrize("name", ("Test1", "Test2"))
@pytest.mark.parametrize("active", (False, True))
def test_edit_layer(prime2_area: Area, name: str, active: bool):
    default = prime2_area.get_layer("Default")

    default.name = name
    default.active = active

    assert default.name == name
    assert default.active == active


# Script Object
def test_edit_properties(prime2_area: Area):
    from retro_data_structures.properties.echoes.objects.Pickup import Pickup

    inst = prime2_area.get_instance("Pickup Object")

    inst.name = "Test"
    assert inst.name == "Test"

    with inst.edit_properties(Pickup) as pickup:
        pickup.amount = 2


def test_edit_connections(prime2_area: Area):
    from retro_data_structures.enums.echoes import Message, State

    pickup = prime2_area.get_instance("Pickup Object")
    relay = prime2_area.get_instance("Post Pickup")

    original_connections = pickup.connections

    pickup.remove_connections_from(relay)
    assert len(pickup.connections) == len(original_connections) - 1

    pickup.add_connection(State.Arrived, Message.SetToZero, relay)
    assert set(pickup.connections) == set(original_connections)
