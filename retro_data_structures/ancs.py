"""
Wiki: https://wiki.axiodl.com/w/ANCS_(File_Format)
"""

import construct
from construct import Int16ub, Const, Struct, PrefixedArray, Int32ub, If, Int8ub, Float32b

from retro_data_structures import game_check
from retro_data_structures.common_types import AABox, String, ObjectTag_32, AssetId32
from retro_data_structures.construct_extensions import WithVersion, BeforeVersion
from retro_data_structures.evnt import EVNT
from retro_data_structures.meta_animation import MetaAnimation_AssetId32
from retro_data_structures.meta_transition import MetaTransition_v1
from retro_data_structures.pas_database import PASDatabase

# This format is only for Prime 1 and 2, so AssetId is always 32-bit
AssetId = AssetId32

AnimationName = Struct(
    animation_id=Int32ub,
    unknown=BeforeVersion(10, String),
    name=String,
)
ParticleResourceData = Struct(
    generic_particles=PrefixedArray(Int32ub, AssetId),
    swoosh_particles=PrefixedArray(Int32ub, AssetId),
    unknown=WithVersion(6, Int32ub),
    electric_particles=PrefixedArray(Int32ub, AssetId),
    spawn_particles=WithVersion(10, PrefixedArray(Int32ub, AssetId)),
)
AnimationAABB = Struct(
    name=String,
    bounding_box=AABox,
)
EffectComponent = Struct(
    name=String,
    particle=ObjectTag_32,
    bone_name=String,
    scale=Float32b,
    parented_mode=Int32ub,
    flags=Int32ub,
)
Effect = Struct(
    name=String,
    components=PrefixedArray(Int32ub, EffectComponent),
)
IndexedAnimationAABB = Struct(
    id=Int32ub,
    bounding_box=AABox,
)

Character = Struct(
    id=Int32ub,
    version=Int16ub,
    name=String,
    model_id=AssetId,
    skin_id=AssetId,
    skeleton_id=AssetId,
    animation_names=PrefixedArray(Int32ub, AnimationName),
    pas_database=PASDatabase,
    particle_resource_data=ParticleResourceData,
    unknown_1=Int32ub,
    unknown_2=WithVersion(10, Int32ub),
    animation_aab_array=WithVersion(2, PrefixedArray(Int32ub, AnimationAABB)),
    effect_array=WithVersion(2, PrefixedArray(Int32ub, Effect)),
    frozen_model=WithVersion(4, AssetId),
    frozen_skin=WithVersion(4, AssetId),
    animation_id_map=WithVersion(5, PrefixedArray(Int32ub, Int32ub)),
    spatial_primitives_id=WithVersion(10, AssetId),
    unknown_3=WithVersion(10, Int8ub),
    indexed_animation_aabb_array=WithVersion(10, PrefixedArray(Int32ub, IndexedAnimationAABB)),
)

CharacterSet = Struct(
    version=Const(1, Int16ub),
    characters=PrefixedArray(Int32ub, Character),
)

Animation = Struct(
    name=String,
    meta=MetaAnimation_AssetId32,
)

Transition = Struct(
    unknown=Int32ub,
    animation_id_a=Int32ub,
    animation_id_b=Int32ub,
    transition=MetaTransition_v1,
)

AdditiveAnimation = Struct(
    animation_id=Int32ub,
    fade_in_time=Float32b,
    fade_out_time=Float32b,
)

HalfTransitions = Struct(
    animation_id=Int32ub,
    transition=MetaTransition_v1,
)

AnimationResourcePair = Struct(
    anim_id=AssetId,
    event_id=AssetId,
)

AnimationSet = Struct(
    table_count=Int16ub,
    animations=PrefixedArray(Int32ub, Animation),
    transitions=PrefixedArray(Int32ub, Transition),
    default_transition=MetaTransition_v1,
    additive=If(construct.this.table_count >= 2, Struct(
        additive_animations=PrefixedArray(Int32ub, AdditiveAnimation),
        default_fade_in_time=Float32b,
        default_fade_out_time=Float32b,
    )),
    half_transitions=If(construct.this.table_count >= 3, PrefixedArray(Int32ub, HalfTransitions)),
    animation_resources=If(game_check.is_prime1, PrefixedArray(Int32ub, AnimationResourcePair)),
    event_sets=If(game_check.is_prime2, PrefixedArray(Int32ub, EVNT)),
)

ANCS = Struct(
    version=Const(1, Int16ub),
    character_set=CharacterSet,
    animation_set=AnimationSet,
)
