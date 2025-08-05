from __future__ import annotations

from construct import Int32ub, PrefixedArray, Struct

from retro_data_structures.common_types import String

RSOS = Struct(
    "modules" / PrefixedArray(Int32ub, String),
    "offsets" / PrefixedArray(Int32ub, Int32ub),
)
