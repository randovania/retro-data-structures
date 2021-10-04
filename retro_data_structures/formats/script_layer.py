from construct import (If, Struct, Const, Int8ub, Int32ub, PrefixedArray)
from retro_data_structures.common_types import FourCC

from retro_data_structures.formats.script_object import ScriptInstance

def ScriptLayer(identifier):
    return Struct(
        "magic" / Const(identifier, FourCC),
        "unknown" / Int8ub,
        "layer_index" / If(identifier == 'SCLY', Int32ub),
        "version" / Const(1, Int8ub),
        "script_instances" / PrefixedArray(Int32ub, ScriptInstance)
    ) 

SCLY = ScriptLayer('SCLY')
SCGN = ScriptLayer('SCGN')
