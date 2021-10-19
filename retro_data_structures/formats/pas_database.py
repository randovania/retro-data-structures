"""
Wiki: https://wiki.axiodl.com/w/PAS_Database
"""
import enum

import construct
from construct import Struct, Const, Int32ub, Array, Float32b, Switch, Int8ub

from retro_data_structures.adapters.enum_adapter import EnumAdapter


class ParmType(enum.IntEnum):
    Int32 = 0
    Uint32 = 1
    Real = 2
    Bool = 3
    Enum = 4


def construct_type_for_parm_type(t):
    return Switch(
        t,
        {
            ParmType.Int32: Int32ub,
            ParmType.Uint32: Int32ub,
            ParmType.Real: Int32ub,
            ParmType.Bool: Int8ub,
            ParmType.Enum: Int32ub,
        },
    )


class WeightFunction(enum.IntEnum):
    ExactMatch = 0
    PercentError = 1
    AngularPercent = 2
    NoWeight = 3


ParmInfo = Struct(
    "parm_type" / EnumAdapter(ParmType),
    "weight_function" / EnumAdapter(WeightFunction),
    "weight" / Float32b,
    "minimum_value" / construct_type_for_parm_type(construct.this.parm_type),
    "maximum_value" / construct_type_for_parm_type(construct.this.parm_type),
)

AnimInfo = Struct(
    "anim_id" / Int32ub,
    "parm_values"
    / Array(
        construct.this._.parm_info_count,
        construct_type_for_parm_type(lambda this: this._.parm_info_array[this._index].parm_type),
    ),
)

AnimState = Struct(
    "anim_state_type" / Int32ub,
    "parm_info_count" / Int32ub,
    "anim_info_count" / Int32ub,
    "parm_info_array" / Array(construct.this.parm_info_count, ParmInfo),
    "anim_info_array" / Array(construct.this.anim_info_count, AnimInfo),
)

PASDatabase = Struct(
    "magic" / Const(b"PAS4"),
    "anim_state_count" / Int32ub,
    "default_anim_state" / Int32ub,
    "anim_states" / Array(construct.this.anim_state_count, AnimState),
)
