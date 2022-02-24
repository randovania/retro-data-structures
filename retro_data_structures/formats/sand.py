"""
Wiki: https://wiki.axiodl.com/w/SAND_(File_Format)
"""
from typing import Optional, List

import construct
from construct import Int16ub, Const, Struct, PrefixedArray, Int32ub, Int8ub, Float32b

from retro_data_structures import game_check
from retro_data_structures.common_types import AABox, String, ObjectTag_32, AssetId64
from retro_data_structures.construct_extensions.version import WithVersion, BeforeVersion
from retro_data_structures.formats import meta_animation, evnt
from retro_data_structures.formats.evnt import EVNT, SoundPOINode, Int32POINode, ParticlePOINode
from retro_data_structures.formats.meta_animation import MetaAnimation_AssetId32
from retro_data_structures.formats.meta_transition import MetaTransition_v2
from retro_data_structures.formats.pas_database import PASDatabase

# This format is only for Prime 3, so AssetId is always 64-bit
from retro_data_structures.game_check import Game

AssetId = AssetId64

Transition = Struct(
    _unknown=Const(0,Int8ub),
    animation_id_a=AssetId * "ANIM",
    animation_id_b=AssetId * "ANIM",
    transition=MetaTransition_v2,
)

AdditiveAnimation = Struct(
    animation_id=AssetId * "ANIM",
    fade_in_time=Float32b,
    fade_out_time=Float32b,
)

HalfTransitions = Struct(
    _unknown=Const(0,Int8ub),
    animation_id=AssetId * "ANIM",
    transition=MetaTransition_v2,
)

AnimEventSet = Struct(
    id=AssetId * "ANIM",
    unk=Int32ub,
    event_sets=PrefixedArray(Int32ub, ParticlePOINode),
    sound_sets=PrefixedArray(Int32ub, SoundPOINode),
    user_sets=PrefixedArray(Int32ub, Int32POINode),
)

SAND = Struct(
    _unk=Const(0, Int16ub),
    transitions=PrefixedArray(Int32ub, Transition),
    half_transitions=PrefixedArray(Int32ub, HalfTransitions),
    default_transition=MetaTransition_v2,
    additive_animations=PrefixedArray(Int32ub, AdditiveAnimation),
    default_fade_in_time=Float32b,
    default_fade_out_time=Float32b,
    _unk2=Const(0, Int8ub),
    anim_events=PrefixedArray(Int32ub, AnimEventSet),
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
