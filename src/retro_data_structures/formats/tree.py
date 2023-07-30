from __future__ import annotations

import typing

from construct.core import Byte, Const, Int32ub, PrefixedArray, Struct

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import FourCC
from retro_data_structures.formats.script_layer import dependencies_for_layer
from retro_data_structures.formats.script_object import ConstructScriptInstance, ScriptInstance

if typing.TYPE_CHECKING:
    from construct import Construct

    from retro_data_structures.game_check import Game

TREE = Struct(
    "magic" / Const("TREE", FourCC),
    "root_node_id" / Int32ub,
    "unknown" / Const(1, Byte),
    "nodes" / PrefixedArray(Int32ub, ConstructScriptInstance),
)


class Tree(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "DUMB"

    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return TREE

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from dependencies_for_layer(self.asset_manager, self.nodes)

    @property
    def nodes(self) -> typing.Iterator[ScriptInstance]:
        for inst in self.raw.nodes:
            yield ScriptInstance(inst, self.target_game)
