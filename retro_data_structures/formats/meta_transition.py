import enum

import construct
from construct import Struct, Int32ub, Switch, Float32b, Byte, Int16ub, Int64ub

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.formats import meta_animation


class MetaTransitionType(enum.IntEnum):
    Animation = 0
    Transition = 1
    PhaseTransition = 2
    Snap = 3
    UnknownType = 4


def create(version: int):
    if version == 1:
        asset_id = Int32ub
    else:
        asset_id = Int64ub
    meta_bodies = {}

    meta = Struct(
        type=EnumAdapter(MetaTransitionType),
        body=Switch(construct.this.type, meta_bodies),
    )

    meta_bodies[MetaTransitionType.Animation] = meta_animation.by_asset_type[asset_id]

    trans_v1 = Struct(
        duration_time=Float32b,
        duration_time_Mode=Int32ub,
        unknown_2=Byte,
        runA=Byte,
        flags=Int32ub,
    )
    trans_v2 = Struct(
        unk1=Int32ub,
        unk2=Float32b,
        unk3=Int32ub,
        unk4=Int16ub,
        unk5=Byte,
        unk6=Int32ub,
    )
    if version > 1:
        trans = trans_v2
    else:
        trans = trans_v1
    meta_bodies[MetaTransitionType.Transition] = meta_bodies[MetaTransitionType.PhaseTransition] = trans

    meta_bodies[MetaTransitionType.Snap] = Struct()

    if version > 1:
        meta_bodies[MetaTransitionType.UnknownType] = Struct(
            unk1=Int32ub,
            unk2=Float32b,
            unk3=Int32ub,
            unk4=Int32ub,
            unk5=Int32ub,
        )

    return meta


MetaTransition_v1 = create(1)
MetaTransition_v2 = create(2)
