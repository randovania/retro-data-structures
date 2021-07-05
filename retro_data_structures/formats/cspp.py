from construct import Struct, PrefixedArray, Int32ub, Float32b

from retro_data_structures.common_types import Vector3, OBBox

SegId = Int32ub
UnknownPair = Struct(
    a=Int32ub,
    b=Int32ub,
)

CSPP = Struct(
    elements_a=PrefixedArray(Int32ub, Struct(
        seg_id_a=SegId,
        seg_id_b=SegId,
        unk_1=UnknownPair,
        vec=Vector3,
        unk_2=Float32b,
    )),
    elements_b=PrefixedArray(Int32ub, Struct(
        seg_id_a=SegId,
        seg_id_b=SegId,
        unk_1=UnknownPair,
        oobox=OBBox,
    ))
)
