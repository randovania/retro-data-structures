import typing

import construct
from construct import Float32b
from construct import Struct, PrefixedArray, Int32ub

from retro_data_structures.common_types import OBBox
from retro_data_structures.common_types import Vector3
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.game_check import Game

SegId = Int32ub
UnknownPair = Struct(
    a=Int32ub,
    b=Int32ub,
)

CSPP = Struct(
    elements_a=PrefixedArray(
        Int32ub,
        Struct(
            seg_id_a=SegId,
            seg_id_b=SegId,
            unk_1=UnknownPair,
            vec=Vector3,
            unk_2=Float32b,
        ),
    ),
    elements_b=PrefixedArray(
        Int32ub,
        Struct(
            seg_id_a=SegId,
            seg_id_b=SegId,
            unk_1=UnknownPair,
            oobox=OBBox,
        ),
    ),
)


class Cspp(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "CSPP"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return CSPP

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
