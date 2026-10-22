"""
FSM2: AI finite state machine, used by Echoes (version 1) and Corruption (versions 1 and 2).

Layout (big endian):

- Header: magic ``FSM2``, version, then the record counts of the four sections below.
- ``states``: name, list of transitions. A transition either points at a trigger (the
  transition is taken if that trigger chain succeeds) or directly at a state.
- ``triggers``: name of a trigger function (such as ``AnimOver``) plus its float parameter and
  a list of targets. Targets pointing at another trigger require that trigger too (AND); a
  target pointing at a state finishes the chain.
- ``actions``: name of an action function (such as ``SelectTarget``) and the targets to
  continue with after it runs.
- ``sub_machines``: named entry points into another FSM2 asset.

Names are resolved against the game's own tables at runtime. For example, Echoes'
DarkSamus.rel binds each state/trigger name to a CDarkSamus virtual function.
"""

from __future__ import annotations

import enum
import typing

import construct
from construct import Const, Float32b, If, Int8ub, Int24ub, Int32ub, PrefixedArray, Rebuild, Struct, len_, this

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import GUID, String
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.game_check import AssetIdCorrect, CurrentGameCheck, Game


class ReferenceKind(enum.IntEnum):
    TRIGGER = 0
    STATE = 1
    ACTION = 2
    SUB_MACHINE = 3


Reference = Struct(
    "name" / String,
    "kind" / EnumAdapter(ReferenceKind, Int8ub, strict=True),
    "index" / Int24ub,
)

References = PrefixedArray(Int32ub, Reference)


def _record(*fields: construct.Construct) -> construct.Struct:
    return Struct(
        "name" / String,
        "guid" / If(this._.version >= 2, GUID),
        *fields,
    )


State = _record("transitions" / References)

Trigger = _record(
    "parameter" / Float32b,
    "targets" / References,
    "unknown" / Int8ub,
)

Action = _record("targets" / References)

SubMachine = _record(
    "entries" / References,
    "state_machine" / AssetIdCorrect,
)

FSM2 = Struct(
    "_magic" / Const(b"FSM2"),
    "version" / Int32ub,
    "_state_count" / Rebuild(Int32ub, len_(this.states)),
    "_trigger_count" / Rebuild(Int32ub, len_(this.triggers)),
    "_action_count" / Rebuild(Int32ub, len_(this.actions)),
    "_sub_machine_count" / Rebuild(Int32ub, len_(this.sub_machines)),
    "states" / construct.Array(this._state_count, State),
    "triggers" / construct.Array(this._trigger_count, Trigger),
    "actions" / construct.Array(this._action_count, Action),
    "sub_machines" / construct.Array(this._sub_machine_count, SubMachine),
    CurrentGameCheck(Game.CORRUPTION, AlignTo(64, b"\xff"), AlignTo(32, b"\xff")),
    construct.Terminated,
)

_SECTION_FOR_KIND = {
    ReferenceKind.TRIGGER: "triggers",
    ReferenceKind.STATE: "states",
    ReferenceKind.ACTION: "actions",
    ReferenceKind.SUB_MACHINE: "sub_machines",
}


class Fsm2(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "FSM2"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return FSM2

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        for sub_machine in self.raw.sub_machines:
            yield from self.asset_manager.get_dependencies_for_asset(sub_machine.state_machine)

    @property
    def state_names(self) -> list[str]:
        return [state.name for state in self.raw.states]

    def resolve(self, reference: construct.Container) -> construct.Container:
        """Returns the record a reference points at."""
        return self.raw[_SECTION_FOR_KIND[reference.kind]][reference.index]
