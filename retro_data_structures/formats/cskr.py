import construct
from construct import Struct, PrefixedArray, Int32ub, Float32b, Prefixed, GreedyBytes, Int16ub, Switch, Terminated, \
    IfThenElse, Array, Aligned

from retro_data_structures import game_check
from retro_data_structures.game_check import Game

Weight = Struct(
    bone_id=Int32ub,
    weight=Float32b,
)

VertexGroup = Struct(
    weights_array=PrefixedArray(Int32ub, Weight),
    vertex_count=Int32ub,
)

Prime1FooterField = Struct(
    first=Int32ub,
    # These values are read by the game, but discarded
    other=IfThenElse(
        construct.this.first == 0xFFFFFFFF,
        Int32ub,
        Array(construct.this.first, Array(3, Int32ub)),
    ),
)

Prime1Footer = Struct(
    unk_a=Prime1FooterField,
    unk_b=Prime1FooterField,
    trailing_bytes=GreedyBytes,
)

Prime2Footer = Struct(
    # These values are read by the game, but unknown purpose
    pool_to_skin_idx=PrefixedArray(Int32ub, Int16ub),
    trailing_bytes=Prefixed(Int32ub, GreedyBytes),
)

CSKR = Struct(
    vertex_groups=PrefixedArray(Int32ub, VertexGroup),
    footer=Switch(
        game_check.get_current_game,
        {
            Game.PRIME: Prime1Footer,
            Game.ECHOES: Prime2Footer,
        },
        construct.Error,
    ),
    _end=Terminated,
)
