from construct import Struct, Const, Int32ub, PrefixedArray, GreedyRange, Byte

from retro_data_structures.common_types import AssetId32, String

HIER = Struct(
    magic=Const(b"HIER"),
    entries=PrefixedArray(
        Int32ub,
        Struct(
            string_table_id=AssetId32,
            name=String,
            scan_id=AssetId32,
            parent_id=Int32ub,
        ),
    ),
    junk=GreedyRange(Byte),
)
