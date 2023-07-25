from __future__ import annotations

import enum

import construct
from construct import Byte, Float32b, Int32ub, Int64ub, PrefixedArray, Struct, Switch

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.common_types import AssetId32, AssetId64, String


class MetaAnimationType(enum.IntEnum):
    Play = 0
    Blend = 1
    PhaseBlend = 2
    Random = 3
    Sequence = 4


CharAnimTime = Struct(
    time=Float32b,
    differential_state=Int32ub,  # TODO: use enum
)


def create(asset_id):
    meta_bodies = {}

    meta = Struct(
        type=EnumAdapter(MetaAnimationType),
        body=Switch(construct.this.type, meta_bodies),
    )

    meta_bodies[MetaAnimationType.Play] = Struct(
        asset_id=asset_id,
        primitive_id=Int32ub,
        name=String,
        unknown=CharAnimTime,
    )

    meta_bodies[MetaAnimationType.Blend] = meta_bodies[MetaAnimationType.PhaseBlend] = Struct(
        anim_a=meta,
        anim_b=meta,
        unknown_1=Float32b,
        unknown_2=Byte,
    )

    meta_bodies[MetaAnimationType.Random] = PrefixedArray(
        Int32ub,
        Struct(
            animation=meta,
            probability=Int32ub,
        ),
    )

    meta_bodies[MetaAnimationType.Sequence] = PrefixedArray(Int32ub, meta)

    return meta


MetaAnimation_AssetId32 = create(AssetId32)
MetaAnimation_AssetId64 = create(AssetId64)

by_asset_type = {
    Int32ub: MetaAnimation_AssetId32,
    Int64ub: MetaAnimation_AssetId64,
}


def legacy_dependencies(obj, target_game):
    if obj.type == MetaAnimationType.Play:
        yield "ANIM", obj.body.asset_id

    elif obj.type in (MetaAnimationType.Blend, MetaAnimationType.PhaseBlend):
        yield from legacy_dependencies(obj.body.anim_a, target_game)
        yield from legacy_dependencies(obj.body.anim_b, target_game)

    elif obj.type == MetaAnimationType.Random:
        for anim in obj.body:
            yield from legacy_dependencies(anim.animation, target_game)

    elif obj.type == MetaAnimationType.Sequence:
        for item in obj.body:
            yield from legacy_dependencies(item, target_game)


def dependencies_for(obj, asset_manager):
    if obj.type == MetaAnimationType.Play:
        yield from asset_manager.get_dependencies_for_asset(obj.body.asset_id)

    elif obj.type in (MetaAnimationType.Blend, MetaAnimationType.PhaseBlend):
        yield from dependencies_for(obj.body.anim_a, asset_manager)
        yield from dependencies_for(obj.body.anim_b, asset_manager)

    elif obj.type == MetaAnimationType.Random:
        for anim in obj.body:
            yield from dependencies_for(anim.animation, asset_manager)

    elif obj.type == MetaAnimationType.Sequence:
        for item in obj.body:
            yield from dependencies_for(item, asset_manager)
