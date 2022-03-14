"""
Wiki: https://wiki.axiodl.com/w/SAND_(File_Format)
"""
import typing
from typing import Optional, List

import construct
from construct import Int16ub, Const, Struct, PrefixedArray, Int32ub, Int8ub, Float32b

from retro_data_structures.base_resource import BaseResource, Dependency, AssetType
from retro_data_structures.common_types import AssetId64
from retro_data_structures.formats.evnt import SoundPOINode, Int32POINode, ParticlePOINode
from retro_data_structures.formats.meta_transition import MetaTransition_v2
from retro_data_structures.game_check import Game

# This format is only for Prime 3, so AssetId is always 64-bit
ConstructAssetId = AssetId64

Transition = Struct(
    _unknown=Const(0, Int8ub),
    animation_id_a=ConstructAssetId * "ANIM",
    animation_id_b=ConstructAssetId * "ANIM",
    transition=MetaTransition_v2,
)

AdditiveAnimation = Struct(
    animation_id=ConstructAssetId * "ANIM",
    fade_in_time=Float32b,
    fade_out_time=Float32b,
)

HalfTransitions = Struct(
    _unknown=Const(0, Int8ub),
    animation_id=ConstructAssetId * "ANIM",
    transition=MetaTransition_v2,
)

AnimEventSet = Struct(
    id=ConstructAssetId * "ANIM",
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
    for transition in obj.transitions:
        yield from _yield_dependency_if_valid(transition.animation_id_a, "ANIM", target_game)
        yield from _yield_dependency_if_valid(transition.animation_id_b, "ANIM", target_game)

    for transition in obj.half_transitions:
        yield from _yield_dependency_if_valid(transition.animation_id, "ANIM", target_game)

    for animation in obj.additive_animations:
        yield from _yield_dependency_if_valid(animation.animation_id, "ANIM", target_game)

    for anim in obj.anim_events:
        yield from _yield_dependency_if_valid(anim.id, "ANIM", target_game)


class Sand(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "SAND"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return SAND

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from dependencies_for(self.raw, self.target_game)
