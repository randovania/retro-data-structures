from construct.core import Byte, Const, Int32ub, PrefixedArray, Struct

from retro_data_structures.common_types import FourCC
from retro_data_structures.formats.script_object import ScriptInstance

TREE = Struct(
    "magic" / Const("TREE", FourCC),
    "root_node_id" / Int32ub,
    "unknown" / Const(1, Byte),
    "nodes" / PrefixedArray(Int32ub, ScriptInstance),
)
