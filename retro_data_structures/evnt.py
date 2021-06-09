from construct import Struct, Int32ub, PrefixedArray, Int16ub, Byte, Float32b, If, Int32sb

from retro_data_structures import hacked_version_check
from retro_data_structures.common_types import String, CharAnimTime, FourCC, ObjectTag_32
from retro_data_structures.construct_extensions import WithVersion

# TODO: prime 3
AssetId = Int32ub


def is_prime_3(context):
    return False


BasePOINode = Struct(
    unk_1=Int16ub,
    name=String,
    type=Int16ub,
    timestamp=CharAnimTime,
    index=Int32ub,
    unk_2=If(is_prime_3, Int32ub),
    unique=Byte,
    weight=Float32b,
    character_index=Int32sb,
    flags=Int32ub,
    unk_extra=If(is_prime_3, Struct(
        Int32ub,
        Int32ub,
        Int32ub,
        Float32b,
        Float32b,
    ))
)

BoolPOINode = Struct(
    base=BasePOINode,
    value=Byte,
)

Int32POINode = Struct(
    base=BasePOINode,
    value=Int32sb,
    locator_name=String,
)

ParticlePOINode = Struct(
    # TODO: prime 3 stuff
    base=BasePOINode,
    duration=Int32ub,
    particle=ObjectTag_32,
    bone_name=If(hacked_version_check.is_prime1, String),
    bone_id=If(hacked_version_check.is_prime2, Int32ub),
    effect_scale=Float32b,
    transform_type=Int32ub,
)

SoundPOINode = Struct(
    base=BasePOINode,
    sound_id=Int32ub,
    fall_off=Float32b,
    max_distance=Float32b,
    echoes=If(hacked_version_check.is_prime2, Struct(
        Int32ub,
        Int16ub,
        Int16ub,
        Float32b,
    ))
)


EVNT = Struct(
    version=Int32ub,
    bool_poi_nodes=PrefixedArray(Int32ub, BoolPOINode),
    int32_poi_nodes=PrefixedArray(Int32ub, Int32POINode),
    particle_poi_nodes=PrefixedArray(Int32ub, ParticlePOINode),
    sound_poi_nodes=WithVersion(2, PrefixedArray(Int32ub, SoundPOINode)),
)
