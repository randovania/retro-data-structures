import typing

import construct
from construct import (
    Float32b,
    Prefixed,
    GreedyBytes,
    Int16ub,
    IfThenElse,
    Array,
    If,
    Const,
)
from construct import Struct, PrefixedArray, Int32ub

from retro_data_structures import game_check
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
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

OtherFooter = Struct(
    # These values are read by the game, but unknown purpose
    pool_to_skin_idx=PrefixedArray(Int32ub, Int16ub),
    trailing_bytes=Prefixed(Int32ub, GreedyBytes),
)

CSKR = Struct(
    _magic=If(game_check.current_game_at_least(Game.CORRUPTION),Const(0x534B494E, Int32ub)),
    unk=If(game_check.current_game_at_least(Game.CORRUPTION),Int32ub), # Version ?
    vertex_groups=PrefixedArray(Int32ub, VertexGroup),
    footer=IfThenElse(
        game_check.is_prime1,
        Prime1Footer,
        OtherFooter,
    ),
)


class Cskr(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "CSKR"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return CSKR

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
