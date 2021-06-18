from construct import Struct, PrefixedArray, Int32ub, If, Aligned

from retro_data_structures import game_check
from retro_data_structures.common_types import String, Vector3, Quaternion

Bone = Struct(
    id=Int32ub,
    parent_id=Int32ub,
    position=Vector3,
    rotation=If(game_check.is_prime2, Quaternion),
    local_rotation=If(game_check.is_prime2, Quaternion),
    linked_bone_id_array=PrefixedArray(Int32ub, Int32ub),
)

BoneName = Struct(
    name=String,
    bone_id=Int32ub,
)

CINF = Aligned(32, Struct(
    bones=PrefixedArray(Int32ub, Bone),
    build_order_id=PrefixedArray(Int32ub, Int32ub),
    bone_names=PrefixedArray(Int32ub, BoneName),
), pattern=b"\xFF")
