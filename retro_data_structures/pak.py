import construct
from construct import (Struct, Const, Int16ub, PrefixedArray, Int32ub, PascalString, IfThenElse,
                       FocusedSeq, Bytes, Lazy, Pointer, Prefixed, Aligned, FixedSized, Byte, Tell, Rebuild,
                       GreedyBytes, Pass, Computed)

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
            size=FocusedSeq("address", address=Tell, value=construct.Seek(4, 1)),
            offset=Int32ub,
            data=Lazy(Pointer(
                construct.this.offset,
                IfThenElse(
                    construct.this.compressed > 0,
                    Struct(
                        # "data",
                        decompressed_size=Rebuild(Int32ub, construct.len_(construct.this.data)),
                        compressed_size=Pointer(construct.this._.size, Int32ub),
                        data=Prefixed(
                            Pointer(construct.this._.size, Int32ub),
                            Aligned(32, IfThenElse(
                                game_check.uses_lzo,
                                LZOCompressedBlock(construct.this.decompressed_size),
                                ZlibCompressedBlock,
                            ))
                        ),
                    ),
                    Struct(
                        data=Prefixed(
                            Pointer(construct.this._.size, Int32ub),
                            GreedyBytes,
                        ),
                        compressed_size=Computed(construct.len_(construct.this.data)),
                    )
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
