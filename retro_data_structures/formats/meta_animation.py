import enum

import construct
from construct import Struct, Int32ub, Switch, Float32b, Byte, PrefixedArray, Int64ub

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.common_types import String, AssetId64, AssetId32


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


def dependencies_for(obj, target_game):
    if obj.type == MetaAnimationType.Play:
        yield "ANIM", obj.body.asset_id

    elif obj.type in (MetaAnimationType.Blend, MetaAnimationType.PhaseBlend):
        yield from dependencies_for(obj.body.anim_a, target_game)
        yield from dependencies_for(obj.body.anim_b, target_game)

    elif obj.type == MetaAnimationType.Random:
        for anim in obj.body:
            yield from dependencies_for(anim.animation, target_game)

    elif obj.type == MetaAnimationType.Sequence:
        for item in obj.body:
            yield from dependencies_for(item, target_game)
