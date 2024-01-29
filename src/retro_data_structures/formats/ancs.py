"""
Wiki: https://wiki.axiodl.com/w/ANCS_(File_Format)
"""

from __future__ import annotations

import typing

import construct
from construct import Const, Float32b, If, Int8ub, Int16ub, Int32ub, PrefixedArray, Struct

from retro_data_structures import game_check
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AABox, AssetId32, ObjectTag_32, String
from retro_data_structures.construct_extensions.version import BeforeVersion, WithVersion
from retro_data_structures.formats import evnt, meta_animation, meta_transition
from retro_data_structures.formats.evnt import EVNT
from retro_data_structures.formats.meta_animation import MetaAnimation_AssetId32
from retro_data_structures.formats.meta_transition import MetaTransition_v1
from retro_data_structures.formats.pas_database import PASDatabase

if typing.TYPE_CHECKING:
    from collections.abc import Iterable

    from retro_data_structures.asset_manager import AssetManager
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


def _yield_dependency_if_valid(asset_id: int | None, asset_type: str, game: Game):
    if asset_id is not None and game.is_valid_asset_id(asset_id):
        yield asset_type, asset_id


def _yield_dependency_array(asset_ids: list[int] | None, asset_type: str, game: Game):
    if asset_ids is not None:
        for asset_id in asset_ids:
            yield from _yield_dependency_if_valid(asset_id, asset_type, game)


def char_dependencies_for(character, asset_manager: AssetManager):
    def _array(asset_ids: Iterable[int] | None):
        if asset_ids is not None:
            for asset_id in asset_ids:
                yield from asset_manager.get_dependencies_for_asset(asset_id, must_exist=False)

    yield from _array(
        (
            character.model_id,
            character.skin_id,
            character.skeleton_id,
            character.frozen_model,
            character.frozen_skin,
            character.spatial_primitives_id,
        )
    )

    # ParticleResourceData
    psd = character.particle_resource_data
    yield from _array(psd.generic_particles)
    yield from _array(psd.swoosh_particles)
    yield from _array(psd.electric_particles)
    yield from _array(psd.spawn_particles)


def legacy_dependencies(obj, target_game: Game):
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
        yield from meta_animation.legacy_dependencies(animation.meta, target_game)

    if obj.animation_set.animation_resources is not None:
        for res in obj.animation_set.animation_resources:
            yield from _yield_dependency_if_valid(res.anim_id, "ANIM", target_game)
            yield from _yield_dependency_if_valid(res.event_id, "EVNT", target_game)

    event_sets = obj.animation_set.event_sets or []
    for event in event_sets:
        yield from evnt.legacy_dependencies(event, target_game)


class Ancs(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "ANCS"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return ANCS

    def ancs_dependencies_for(self, char_index: int | None) -> typing.Iterator[Dependency]:
        def char_anims(char) -> typing.Iterator[tuple[int, str]]:
            for anim_name in char.animation_names:
                yield next((i, a) for i, a in enumerate(self.raw.animation_set.animations) if a.name == anim_name.name)

        def char_deps(char):
            yield from char_dependencies_for(char, self.asset_manager)

            for anim_index, anim in char_anims(char):
                yield from meta_animation.dependencies_for(anim.meta, self.asset_manager)

                if self.raw.animation_set.animation_resources is not None:
                    res = self.raw.animation_set.animation_resources[anim_index]
                    yield from self.asset_manager.get_dependencies_for_asset(res.anim_id)

                    if not self.asset_manager.target_game.is_valid_asset_id(res.event_id):
                        continue
                    yield Dependency("EVNT", res.event_id)
                    evnt_file = self.asset_manager.get_parsed_asset(res.event_id)
                    yield from evnt.dependencies_for(evnt_file.raw, self.asset_manager, char_index)

                elif self.raw.animation_set.event_sets is not None:
                    yield from evnt.dependencies_for(
                        self.raw.animation_set.event_sets[anim_index], self.asset_manager, char_index
                    )

        if char_index is not None:
            chars = [self.raw.character_set.characters[char_index]]
        else:
            chars = self.raw.character_set.characters

        for char in chars:
            yield from char_deps(char)

        for transition in self.raw.animation_set.transitions:
            yield from meta_transition.dependencies_for(transition.transition, self.asset_manager)

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from self.ancs_dependencies_for(None)
