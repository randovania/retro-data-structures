from __future__ import annotations

from construct import Int32ub, PrefixedArray, Struct

from retro_data_structures.common_types import AssetId64, FourCC

DEPS = Struct(
    "dependencies" / PrefixedArray(Int32ub, Struct("asset_id" / AssetId64, "type" / FourCC)),
    "offsets" / PrefixedArray(Int32ub, Int32ub),
)
