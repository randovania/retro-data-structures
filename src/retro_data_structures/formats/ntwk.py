from __future__ import annotations

import typing

import construct

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import FourCC
from retro_data_structures.formats.script_object import ConstructScriptInstance, ScriptInstance

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game

NTWK = construct.Aligned(
    32,
    construct.Struct(
        "magic" / construct.Const("NTWK", FourCC),
        "version" / construct.Const(1, construct.Int8ub),
        "script_instances" / construct.PrefixedArray(construct.Int32ub, ConstructScriptInstance),
    ),
)


class Ntwk(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return NTWK

    @classmethod
    def resource_type(cls) -> AssetType:
        return "NTWK"

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []

    @property
    def instances(self) -> typing.Iterator[ScriptInstance]:
        for instance in self._raw.script_instances:
            yield ScriptInstance(instance, self.target_game)
