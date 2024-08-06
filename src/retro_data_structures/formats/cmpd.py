from __future__ import annotations

import construct
from construct import Bytes, Const, FocusedSeq, IfThenElse, Int32ub, Struct

from retro_data_structures.compression import LZOCompressedBlockCorruption

CMPD = Struct(
    magic=Const(b"CMPD"),
    block_count=Int32ub,
    block_header=construct.Array(
        construct.this.block_count,
        Struct(
            flag=construct.Byte,
            compressed_size=construct.Int24ub,
            uncompressed_size=construct.Int32ub,
        ),
    ),
    blocks=construct.Array(
        construct.this.block_count,
        IfThenElse(
            lambda this: this.block_header[this._index].compressed_size
            < this.block_header[this._index].uncompressed_size,
            FocusedSeq(
                "block",
                block=LZOCompressedBlockCorruption(lambda this: this._.block_header[this._index].uncompressed_size),
            ),
            Bytes(lambda this: this.block_header[this._index].uncompressed_size),
        ),
    ),
)


class CMPDAdapter(construct.Adapter):
    def _decode(self, obj, context, path):
        return b"".join(obj.blocks)

    # Going to rip a page out of PWE's book and compress everything in a single block
    def _encode(self, uncompressed, context, path):
        res = construct.Container(
            [
                ("magic", b"CMPD"),
                ("block_count", 1),
                (
                    "block_header",
                    construct.ListContainer(
                        [
                            construct.Container(
                                [
                                    ("flag", 0xA0),
                                    ("compressed_size", None),
                                    ("uncompressed_size", len(uncompressed)),
                                ]
                            ),
                        ]
                    ),
                ),
                (
                    "blocks",
                    construct.ListContainer(
                        LZOCompressedBlockCorruption(len(uncompressed))._encode(uncompressed, context, path)
                    ),
                ),
            ]
        )
        res.block_header[0].compressed_size = len(res.blocks[0])
        return res


CompressedPakResource = CMPDAdapter(CMPD)
