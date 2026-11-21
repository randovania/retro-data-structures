from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

import construct
import pytest
from construct import Container, ListContainer
from tests import test_lib

from retro_data_structures.base_resource import Dependency
from retro_data_structures.formats.fsm2 import FSM2, Fsm2, ReferenceKind
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetId


def _ref(kind: ReferenceKind, index: int, name: str = "") -> Container:
    return Container(name=name, kind=kind, index=index)


def _machine(version: int, sub_machine_id: int) -> Container:
    def guid(n: int) -> uuid.UUID | None:
        return uuid.UUID(int=n) if version >= 2 else None

    return Container(
        version=version,
        states=ListContainer(
            [
                Container(
                    name="Start",
                    guid=guid(1),
                    transitions=ListContainer([_ref(ReferenceKind.TRIGGER, 0), _ref(ReferenceKind.STATE, 1)]),
                ),
                Container(name="Dead", guid=guid(2), transitions=ListContainer()),
            ]
        ),
        triggers=ListContainer(
            [
                Container(
                    name="Delay",
                    guid=guid(3),
                    parameter=1.5,
                    targets=ListContainer([_ref(ReferenceKind.ACTION, 0)]),
                    unknown=0,
                ),
            ]
        ),
        actions=ListContainer(
            [Container(name="Explode", guid=guid(4), targets=ListContainer([_ref(ReferenceKind.STATE, 1)]))]
        ),
        sub_machines=ListContainer(
            [
                Container(
                    name="Main",
                    guid=guid(5),
                    entries=ListContainer([_ref(ReferenceKind.SUB_MACHINE, 0, "ExitPortal")]),
                    state_machine=sub_machine_id,
                )
            ]
        ),
    )


@pytest.mark.parametrize(
    ("game", "version", "sub_machine_id", "alignment"),
    [
        (Game.ECHOES, 1, 0x79E9EAA2, 32),
        (Game.CORRUPTION, 1, 0x0123456789ABCDEF, 64),
        (Game.CORRUPTION, 2, 0x0123456789ABCDEF, 64),
    ],
)
def test_build_parse_synthetic(game: Game, version: int, sub_machine_id: int, alignment: int):
    encoded = FSM2.build(_machine(version, sub_machine_id), target_game=game)

    assert encoded[:4] == b"FSM2"
    assert encoded[4:24] == construct.Int32ub[5].build([version, 2, 1, 1, 1])
    assert len(encoded) % alignment == 0
    assert encoded.rstrip(b"\xff") != encoded

    decoded = FSM2.parse(encoded, target_game=game)
    assert [state.name for state in decoded.states] == ["Start", "Dead"]
    assert decoded.states[0].transitions[1].kind is ReferenceKind.STATE
    assert decoded.triggers[0].parameter == 1.5
    assert decoded.sub_machines[0].state_machine == sub_machine_id
    assert decoded.sub_machines[0].entries[0].name == "ExitPortal"
    assert (decoded.states[0].guid is not None) == (version >= 2)
    assert FSM2.build(decoded, target_game=game) == encoded


def test_reference_packing():
    # Kind in the high byte, index in the low 24 bits, after the (usually empty) name.
    encoded = FSM2.build(_machine(1, 0x79E9EAA2), target_game=Game.ECHOES)
    start = encoded.index(b"Start\x00") + len(b"Start\x00")
    assert encoded[start : start + 14] == bytes.fromhex("00000002 00 00000000 00 01000001")


def test_invalid_reference_kind():
    data = bytearray(FSM2.build(_machine(1, 0x79E9EAA2), target_game=Game.ECHOES))
    start = data.index(b"Start\x00") + len(b"Start\x00")
    data[start + 5] = 4  # first transition's kind byte
    with pytest.raises(ValueError, match="Invalid value for ReferenceKind: 4"):
        FSM2.parse(bytes(data), target_game=Game.ECHOES)


def test_resolve():
    fsm = Fsm2(
        FSM2.parse(FSM2.build(_machine(1, 0x79E9EAA2), target_game=Game.ECHOES), target_game=Game.ECHOES), Game.ECHOES
    )
    start = fsm.raw.states[0]
    assert fsm.resolve(start.transitions[0]).name == "Delay"
    assert fsm.resolve(start.transitions[1]).name == "Dead"
    assert fsm.resolve(fsm.raw.triggers[0].targets[0]).name == "Explode"
    assert fsm.state_names == ["Start", "Dead"]


def test_compare_p2(prime2_asset_manager: AssetManager, fsm2_asset_id: AssetId):
    test_lib.parse_and_build_compare(prime2_asset_manager, fsm2_asset_id, Fsm2)


def test_compare_p3(prime3_asset_manager: AssetManager, fsm2_asset_id: AssetId):
    test_lib.parse_and_build_compare(prime3_asset_manager, fsm2_asset_id, Fsm2)


def test_dark_samus_p2(prime2_asset_manager: AssetManager):
    fsm = prime2_asset_manager.get_parsed_asset(0x9F23AC7B, type_hint=Fsm2)

    assert fsm.raw.version == 1
    assert len(fsm.raw.states) == 59
    assert len(fsm.raw.triggers) == 92
    assert not fsm.raw.actions
    assert not fsm.raw.sub_machines

    start = fsm.raw.states[0]
    assert start.name == "Start"
    # StartsInTheAir -> FallFromTheAir, otherwise go straight to TurnToFacePlayer
    assert [fsm.resolve(t).name for t in start.transitions] == ["StartsInTheAir", "TurnToFacePlayer"]
    assert [t.kind for t in start.transitions] == [ReferenceKind.TRIGGER, ReferenceKind.STATE]
    starts_in_air = fsm.resolve(start.transitions[0])
    assert [fsm.resolve(t).name for t in starts_in_air.targets] == ["FallFromTheAir"]

    # CanMissileDeflect is chained (AND) with AnyIncomingMissiles before reaching MissileDeflect
    can_deflect = next(t for t in fsm.raw.triggers if t.name == "CanMissileDeflect")
    chained = fsm.resolve(can_deflect.targets[0])
    assert chained.name == "AnyIncomingMissiles"
    assert fsm.resolve(chained.targets[0]).name == "MissileDeflect"


def test_dependencies_p2(prime2_asset_manager: AssetManager):
    fsm = prime2_asset_manager.get_parsed_asset(0x30C88D1A, type_hint=Fsm2)

    assert [sub.name for sub in fsm.raw.sub_machines] == ["Main"]
    assert fsm.raw.states[0].transitions[0].name == "ExitPortal"
    assert Dependency("FSM2", 0x79E9EAA2) in list(fsm.dependencies_for())
