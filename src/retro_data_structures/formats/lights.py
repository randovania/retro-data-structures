from construct import Array, Const, Enum, Flag, Float32b, If, Int32ub, StopIf, Struct
from construct.core import IfThenElse, PrefixedArray

from retro_data_structures import game_check
from retro_data_structures.common_types import Color4f, Vector3

Lights = Struct(
    "magic" / Const(0xBABEDEAD, Int32ub),
    "layers"
    / Array(
        lambda this: 4 if game_check.is_prime3(this) else 2,
        PrefixedArray(
            Int32ub,
            Struct(
                "light_type" / Enum(Int32ub, local_ambient=0, directional=1, spot=3),
                "color" / IfThenElse(game_check.is_prime3, Color4f, Vector3),
                "position" / Vector3,
                "direction" / Vector3,
                "codirection" / If(game_check.is_prime3, Vector3),
                "brightness" / Float32b,
                "spot_cutoff" / Float32b,
                "unk1" / Float32b,
                "unk2" / Flag,
                "unk3" / Float32b,
                "falloff_type" / Enum(Int32ub, constant=0, linear=1, quadratic=2),
                "unk4" / Float32b,
                StopIf(lambda this: not game_check.is_prime3(this)),
                "unk5" / Float32b,
                "unk6" / Float32b,
                "unk6" / Float32b,
                "unk7" / Float32b,
                "unk8" / Int32ub,
            ),
        ),
    ),
)
