"""
Wiki: https://wiki.axiodl.com/w/ANCS_(File_Format)
"""
import typing
from typing import Optional, List

import construct
from construct import Int16ub, Const, Struct, PrefixedArray, Int32ub, If, Int8ub, Float32b

from retro_data_structures import game_check
from retro_data_structures.common_types import AABox, String, ObjectTag_32, AssetId32
from retro_data_structures.construct_extensions.version import WithVersion, BeforeVersion
from retro_data_structures.formats import meta_animation, evnt
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.formats.evnt import EVNT
from retro_data_structures.formats.meta_animation import MetaAnimation_AssetId32
from retro_data_structures.formats.meta_transition import MetaTransition_v1
from retro_data_structures.formats.pas_database import PASDatabase
from retro_data_structures.game_check import Game

# This format is only for Prime 1 and 2, so AssetId is always 32-bit
ConstructAssetId = AssetId32

AnimationName = Struct(
    animation_id=Int32ub,
    unknown=BeforeVersion(10, String),
    name=String,
)
ParticleResourceData = Struct(
    generic_particles=PrefixedArray(Int32ub, ConstructAssetId) * "PART",
    swoosh_particles=PrefixedArray(Int32ub, ConstructAssetId) * "SWHC",
    unknown=WithVersion(6, Int32ub),
    electric_particles=PrefixedArray(Int32ub, ConstructAssetId) * "ELSC",
    spawn_particles=WithVersion(10, PrefixedArray(Int32ub, ConstructAssetId)) * "SPSC",
)
AnimationAABB = Struct(
    name=String,
    bounding_box=AABox,
)
EffectComponent = Struct(
    name=String,
    particle=ObjectTag_32,
    bone_name=If(game_check.is_prime1, String),
    bone_id=If(game_check.is_prime2, Int32ub),
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
    model_id=ConstructAssetId * "CMDL",
    skin_id=ConstructAssetId * "CSKR",
    skeleton_id=ConstructAssetId * "CINF",
    animation_names=PrefixedArray(Int32ub, AnimationName),
    pas_database=PASDatabase,
    particle_resource_data=ParticleResourceData,
    unknown_1=Int32ub,
    unknown_2=WithVersion(10, Int32ub),
    animation_aabb_array=WithVersion(2, PrefixedArray(Int32ub, AnimationAABB)),
    effect_array=WithVersion(2, PrefixedArray(Int32ub, Effect)),
    frozen_model=WithVersion(4, ConstructAssetId) * "CMDL",
    frozen_skin=WithVersion(4, ConstructAssetId) * "CSKR",
    animation_id_map=WithVersion(5, PrefixedArray(Int32ub, Int32ub)),
    spatial_primitives_id=WithVersion(10, ConstructAssetId) * "CSPP",
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
    anim_id=ConstructAssetId * "ANIM",
    event_id=ConstructAssetId * "EVNT",
)

AnimationSet = Struct(
    table_count=Int16ub,
    animations=PrefixedArray(Int32ub, Animation),
    transitions=PrefixedArray(Int32ub, Transition),
    default_transition=MetaTransition_v1,
    additive=If(
        construct.this.table_count >= 2,
        Struct(
            additive_animations=PrefixedArray(Int32ub, AdditiveAnimation),
            default_fade_in_time=Float32b,
            default_fade_out_time=Float32b,
        ),
    ),
    half_transitions=If(construct.this.table_count >= 3, PrefixedArray(Int32ub, HalfTransitions)),
    animation_resources=If(game_check.is_prime1, PrefixedArray(Int32ub, AnimationResourcePair)),
    event_sets=If(game_check.is_prime2, PrefixedArray(Int32ub, EVNT)),
)

ANCS = Struct(
    version=Const(1, Int16ub),
    character_set=CharacterSet,
    animation_set=AnimationSet,
)


def _yield_dependency_if_valid(asset_id: Optional[int], asset_type: str, game: Game):
    if asset_id is not None and game.is_valid_asset_id(asset_id):
        yield asset_type, asset_id


def _yield_dependency_array(asset_ids: Optional[List[int]], asset_type: str, game: Game):
    if asset_ids is not None:
        for asset_id in asset_ids:
            yield from _yield_dependency_if_valid(asset_id, asset_type, game)


def dependencies_for(obj, target_game: Game):
    for character in obj.character_set.characters:
        yield from _yield_dependency_if_valid(character.model_id, "CMDL", target_game)
        yield from _yield_dependency_if_valid(character.skin_id, "CSKR", target_game)
        yield from _yield_dependency_if_valid(character.skeleton_id, "CINF", target_game)
        yield from _yield_dependency_if_valid(character.frozen_model, "CMDL", target_game)
        yield from _yield_dependency_if_valid(character.frozen_skin, "CSKR", target_game)
        yield from _yield_dependency_if_valid(character.spatial_primitives_id, "CSPP", target_game)

        # ParticleResourceData
        psd = character.particle_resource_data
        _yield_dependency_array(psd.generic_particles, "PART", target_game)
        _yield_dependency_array(psd.swoosh_particles, "SWHC", target_game)
        _yield_dependency_array(psd.electric_particles, "ELSC", target_game)
        _yield_dependency_array(psd.spawn_particles, "SPSC", target_game)

    for animation in obj.animation_set.animations:
        yield from meta_animation.dependencies_for(animation.meta, target_game)

    if obj.animation_set.animation_resources is not None:
        for res in obj.animation_set.animation_resources:
            yield from _yield_dependency_if_valid(res.anim_id, "ANIM", target_game)
            yield from _yield_dependency_if_valid(res.event_id, "EVNT", target_game)

    event_sets = obj.animation_set.event_sets or []
    for event in event_sets:
        yield from evnt.dependencies_for(event, target_game)


class Ancs(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "ANCS"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return ANCS

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from dependencies_for(self.raw, self.target_game)
