from construct import (Struct, Const, Int8ub, Int32ub, PrefixedArray)

from retro_data_structures.formats.script_object import ScriptInstance

SCLY = Struct(
    magic=Const(b"SCLY"),
    unk1=Int8ub,
    layer_index=Int32ub,
    version=Const(1, Int8ub),
    script_instances=PrefixedArray(Int32ub, ScriptInstance),
)
