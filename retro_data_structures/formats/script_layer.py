from construct import (If, Struct, Const, Int8ub, Int32ub, PrefixedArray)
from construct.core import Computed, FixedSized, Hex, IfThenElse, PascalString, Peek, Pointer, Prefixed, Rebuild, Array, Seek, Tell, this
from retro_data_structures.common_types import FourCC
from retro_data_structures.construct_extensions import Skip
from retro_data_structures import game_check

from retro_data_structures.formats.script_object import ScriptInstance, ScriptInstancePrime

ScriptLayerPrime = Struct(
    "magic" / Const("SCLY", FourCC),
    "unknown" / Int32ub,
    "_layer_count_address" / Tell,
    "_layer_count" / Peek(Int32ub),
    Skip(1, Int32ub),
    "layer_sizes" / Array(this._layer_count, Int32ub),
    "layers" / PrefixedArray(
        Pointer(this._._layer_count_address, Int32ub), 
        FixedSized(
            lambda this: this._.layer_sizes[this._index],
            Struct(
                "unk" / Hex(Int8ub),
                "objects" / PrefixedArray(Int32ub, ScriptInstancePrime),
            )
        )
    ),
)

def ScriptLayer(identifier):
    return Struct(
        "magic" / Const(identifier, FourCC),
        "unknown" / Int8ub,
        "layer_index" / If(identifier == 'SCLY', Int32ub),
        "version" / Const(1, Int8ub),
        "script_instances" / PrefixedArray(Int32ub, ScriptInstance)
    ) 

SCLY = IfThenElse(
    game_check.current_game_at_least(game_check.Game.ECHOES),
    ScriptLayer('SCLY'),
    ScriptLayerPrime
)
SCGN = ScriptLayer('SCGN')
