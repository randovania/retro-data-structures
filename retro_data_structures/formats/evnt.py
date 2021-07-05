from construct import Struct, Int32ub, PrefixedArray, Int16ub, Byte, Float32b, If, Int32sb, Hex

from retro_data_structures import game_check
from retro_data_structures.common_types import String, CharAnimTime
from retro_data_structures.construct_extensions import WithVersion

BasePOINode = Struct(
    unk_1=Int16ub,
    name=String,
    type=Int16ub,
    timestamp=CharAnimTime,
    index=Int32ub,
    unk_2=If(game_check.is_prime3, Int32ub),
    unique=Byte,
    weight=Float32b,
    character_index=Int32sb,
    flags=Int32ub,
    unk_extra=If(game_check.is_prime3, Struct(
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
    particle=game_check.ObjectTagCorrect,
    bone_name=If(game_check.is_prime1, String),
    bone_id=If(game_check.is_prime2, Int32ub),
    effect_scale=Float32b,
    transform_type=Int32ub,
)

SoundPOINode = Struct(
    base=BasePOINode,
    sound_id=Hex(Int32ub),
    fall_off=Float32b,
    max_distance=Float32b,
    echoes=If(game_check.is_prime2, Struct(
        unk_a=Int32ub,
        unk_b=Int16ub,
        unk_c=Int16ub,
        unk_d=Float32b,
    ))
)

EVNT = Struct(
    version=Int32ub,
    bool_poi_nodes=PrefixedArray(Int32ub, BoolPOINode),
    int32_poi_nodes=PrefixedArray(Int32ub, Int32POINode),
    particle_poi_nodes=PrefixedArray(Int32ub, ParticlePOINode),
    sound_poi_nodes=WithVersion(2, PrefixedArray(Int32ub, SoundPOINode)),
)


def dependencies_for(obj, target_game):
    for particle_poi in obj.particle_poi_nodes:
        yield particle_poi.particle.type, particle_poi.particle.id
