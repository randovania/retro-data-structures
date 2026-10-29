"""
DCLN: dynamic collision, a group of oriented bounding box trees used by platforms and other actors.
Same layout in Prime and Echoes, besides the version and the collision index (see area collision).
"""

from __future__ import annotations

import typing

import construct
from construct import Const, Flag, If, Int16ub, Int32ub, LazyBound, Mapping, PrefixedArray, Struct, this

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import OBBox
from retro_data_structures.formats.area_collision import CollisionIndex

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game

DclnVersion = Mapping(Int32ub, {"prime1": 2, "prime23": 4})

OBBTreeNode = Struct(
    "bounding_box" / OBBox,
    "is_leaf" / Flag,
    "left" / If(lambda ctx: not ctx.is_leaf, LazyBound(lambda: OBBTreeNode)),
    "right" / If(lambda ctx: not ctx.is_leaf, LazyBound(lambda: OBBTreeNode)),
    "triangle_indices" / If(this.is_leaf, PrefixedArray(Int32ub, Int16ub)),
)


def _round_up_4(value: int) -> int:
    return value + (-value % 4)


def node_memory_size(node: construct.Container) -> int:
    """How much memory the game allocates for the node tree. Same sizes in Prime and Echoes."""
    if node.is_leaf:
        children = _round_up_4(0x10 + 2 * len(node.triangle_indices))
    else:
        children = node_memory_size(node.left) + node_memory_size(node.right)
    return _round_up_4(0x50 + children)


OBBTree = Struct(
    "magic" / Const(0xDEAFBABE, Int32ub),
    "version" / DclnVersion,
    "memory_size" / construct.Rebuild(Int32ub, lambda ctx: node_memory_size(ctx.root)),
    "collision_indices" / CollisionIndex,
    "root" / OBBTreeNode,
)

DCLN = construct.Aligned(32, Struct("trees" / PrefixedArray(Int32ub, OBBTree)), pattern=b"\xff")


class Dcln(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "DCLN"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return DCLN

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
