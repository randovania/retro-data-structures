"""
Wiki: https://wiki.axiodl.com/w/CHAR_(Metroid_Prime_3)

To Do: DKCR CHAR Format
"""
import typing
from typing import Optional, List

import construct
from construct import Const, Struct, PrefixedArray, Int8ub, Int32ub, Float32b, Array

from retro_data_structures.base_resource import Dependency
from retro_data_structures.common_types import AABox, String, AssetId64, FourCC
from retro_data_structures.formats import BaseResource, AssetType
from retro_data_structures.formats.evnt import SoundPOINode, ParticlePOINode
from retro_data_structures.formats.meta_animation import MetaAnimation_AssetId64
from retro_data_structures.formats.pas_database import PASDatabase
from retro_data_structures.game_check import Game

# This format is only for Prime 3/DKCR, so AssetId is always 64-bit
ConstructAssetId = AssetId64

ParticleResourceData = Struct(
    generic_particles=PrefixedArray(Int32ub, ConstructAssetId) * "PART",
    swoosh_particles=PrefixedArray(Int32ub, ConstructAssetId) * "SWHC",
    electric_particles=PrefixedArray(Int32ub, ConstructAssetId) * "ELSC",
    spawn_particles=PrefixedArray(Int32ub, ConstructAssetId) * "SPSC",
    _unk=Const(0, Int32ub),
    _unk1=Const(0, Int32ub),
)

AnimationAABB = Struct(
    anim_id=ConstructAssetId * "ANIM",
    bounding_box=AABox,
)

Animation = Struct(
    name=String,
    meta=MetaAnimation_AssetId64,
)

EffectEvent = Struct(
    name=String,
    event=ParticlePOINode,
)

SoundEvent = Struct(
    name=String,
    sound=SoundPOINode,
)

CharEventSet = Struct(
    id=Int32ub,
    name=String,
    event_sets=PrefixedArray(Int32ub, EffectEvent),
    sound_sets=PrefixedArray(Int32ub, SoundEvent),
)

OverlayModel = Struct(
    type=FourCC,
    model_id=ConstructAssetId * "CMDL",
    skin_id=ConstructAssetId * "CSKR",
)

CollisionPrimitive = Struct(
    unk_ints=Array(5, Int32ub),
    unk_floats=Array(8, Float32b),
    name=String,
    end_unk=Float32b,
)

CollisionSet = Struct(
    name=String,
    primitives=PrefixedArray(Int32ub, CollisionPrimitive),
)

CHAR = Struct(
    version=Int8ub,  # 0x03/0x05 for Corruption 0x59 for DKCR
    id=Int8ub,
    name=String,
    model_id=ConstructAssetId * "CMDL",
    skin_id=ConstructAssetId * "CSKR",
    overlays=PrefixedArray(Int32ub, OverlayModel),
    skeleton_id=ConstructAssetId * "CINF",
    sand_id=ConstructAssetId * "SAND",
    pas_database=PASDatabase,
    particle_resource_data=ParticleResourceData,
    event_sets=PrefixedArray(Int32ub, CharEventSet),
    animations=PrefixedArray(Int32ub, Animation),
    animation_aabb_array=PrefixedArray(Int32ub, AnimationAABB),
    bool=Int8ub,
    unk_bool_array=PrefixedArray(Int32ub, Int8ub),
    collision_sets=PrefixedArray(Int32ub, CollisionSet),
    sound_resources=PrefixedArray(Int32ub, ConstructAssetId) * "CAUD",
)


def _yield_dependency_if_valid(asset_id: Optional[int], asset_type: str, game: Game):
    if asset_id is not None and game.is_valid_asset_id(asset_id):
        yield asset_type, asset_id


def _yield_dependency_array(asset_ids: Optional[List[int]], asset_type: str, game: Game):
    if asset_ids is not None:
        for asset_id in asset_ids:
            yield from _yield_dependency_if_valid(asset_id, asset_type, game)


def dependencies_for(obj, target_game: Game):
    yield from _yield_dependency_if_valid(obj.model_id, "CMDL", target_game)
    yield from _yield_dependency_if_valid(obj.skin_id, "CSKR", target_game)
    yield from _yield_dependency_if_valid(obj.skeleton_id, "CINF", target_game)
    yield from _yield_dependency_if_valid(obj.sand_id, "SAND", target_game)

    # ParticleResourceData
    psd = obj.particle_resource_data
    _yield_dependency_array(psd.generic_particles, "PART", target_game)
    _yield_dependency_array(psd.swoosh_particles, "SWHC", target_game)
    _yield_dependency_array(psd.electric_particles, "ELSC", target_game)
    _yield_dependency_array(psd.spawn_particles, "SPSC", target_game)
    _yield_dependency_array(obj.sound_resources, "CAUD", target_game)

    # Overlays
    for overlay in obj.overlays:
        yield from _yield_dependency_if_valid(overlay.model_id, "CMDL", target_game)
        yield from _yield_dependency_if_valid(overlay.skin_id, "CSKR", target_game)

    # Animations
    for animation in obj.animation_aabb_array:
        yield from _yield_dependency_if_valid(animation.anim_id, "ANIM", target_game)


class Char(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "CHAR"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return CHAR

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from dependencies_for(self.raw, self.target_game)
