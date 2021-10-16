from construct.core import (
    Array,
    Const,
    FixedSized,
    Hex,
    If,
    IfThenElse,
    Int8ub,
    Int32ub,
    Peek,
    Pointer,
    PrefixedArray,
    Struct,
    Tell,
    this,
)

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC
from retro_data_structures.construct_extensions import Skip
from retro_data_structures.formats.script_object import ScriptInstance

ScriptLayerPrime = Struct(
    "magic" / Const("SCLY", FourCC),
    "unknown" / Int32ub,
    "_layer_count_address" / Tell,
    "_layer_count" / Peek(Int32ub),
    Skip(1, Int32ub),
    "layer_sizes" / Array(this._layer_count, Int32ub),
    "layers"
    / PrefixedArray(
        Pointer(this._._layer_count_address, Int32ub),
        FixedSized(
            lambda this: this._.layer_sizes[this._index],
            Struct(
                "unk" / Hex(Int8ub),
                "objects" / PrefixedArray(Int32ub, ScriptInstance),
            ),
        ),
    ),
)


def ScriptLayer(identifier):
    return Struct(
        "magic" / Const(identifier, FourCC),
        "unknown" / Int8ub,
        "layer_index" / If(identifier == "SCLY", Int32ub),
        "version" / Const(1, Int8ub),
        "script_instances" / PrefixedArray(Int32ub, ScriptInstance),
    )


SCLY = IfThenElse(game_check.current_game_at_least(game_check.Game.ECHOES), ScriptLayer("SCLY"), ScriptLayerPrime)
SCGN = ScriptLayer("SCGN")
