from __future__ import annotations

import typing

from construct.core import Byte, Const, Int32ub, PrefixedArray, Struct, Terminated

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import FourCC
from retro_data_structures.formats.script_layer import dependencies_for_layer
from retro_data_structures.formats.script_object import (
    ConstructScriptInstance,
    InstanceId,
    ScriptInstance,
    ScriptInstanceRaw,
)

if typing.TYPE_CHECKING:
    from construct import Construct

    from retro_data_structures.game_check import Game
    from retro_data_structures.properties import BaseObjectType

TREE = Struct(
    "magic" / Const("TREE", FourCC),
    "root_node_id" / Int32ub,
    "unknown" / Const(1, Byte),
    "nodes" / PrefixedArray(Int32ub, ConstructScriptInstance),
    Terminated,
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
        """Gets all nodes in the tree."""
        for inst in self._raw.nodes:
            yield ScriptInstance(inst, self.target_game)

    def get_node_by_id(self, index: int) -> ScriptInstance:
        """Gets a node by its ID"""
        return ScriptInstance(self._raw.nodes[index], self.target_game)

    def add_new_instance(self, properties: BaseObjectType) -> ScriptInstance:
        """Creates a new node. No validation is made that the properties are of a type that makes sense."""
        new_id = len(self._raw.nodes)
        self._raw.nodes.append(
            ScriptInstanceRaw(
                type=properties.object_type(),
                id=InstanceId(new_id),
                connections=(),
                base_property=properties.to_bytes(self.target_game),
            )
        )
        return self.get_node_by_id(new_id)
