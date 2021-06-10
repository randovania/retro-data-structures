import construct
from construct import (Struct, Const, Int16ub, PrefixedArray, Int32ub, PascalString, IfThenElse,
                       FocusedSeq, Bytes, Lazy, Pointer)

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC, AssetId32, AssetId64
from retro_data_structures.compression import LZOCompressedBlock, ZlibCompressedBlock

PAKHeader = Struct(
    version_major=Const(3, Int16ub),
    version_minor=Const(5, Int16ub),
    unused=Const(0, Int32ub),
)


def create(asset_id):
    return "PAK" / Struct(
        header=PAKHeader,
        named_resources=PrefixedArray(Int32ub, Struct(
            asset_type=FourCC,
            asset_id=asset_id,
            name=PascalString(Int32ub, "utf-8"),
        )),
        resources=PrefixedArray(Int32ub, Struct(
            compressed=Int32ub,
            asset_type=FourCC,
            asset_id=asset_id,
            size=Int32ub,
            offset=Int32ub,
            data=Lazy(Pointer(
                construct.this.offset,
                IfThenElse(
                    construct.this.compressed > 0,
                    FocusedSeq(
                        "data",
                        decompressed_size=Int32ub,
                        data=IfThenElse(
                            game_check.uses_lzo,
                            LZOCompressedBlock(construct.this._.size, construct.this.decompressed_size),
                            ZlibCompressedBlock(construct.this._.size, construct.this.decompressed_size),
                        ),
                    ),
                    Bytes(construct.this.size),
                ),
            )),
        )),
    )


PAK_AssetId32 = create(AssetId32)
PAK_AssetId64 = create(AssetId64)

PAK = IfThenElse(
    game_check.uses_asset_id_32,
    PAK_AssetId32,
    PAK_AssetId64,
)
