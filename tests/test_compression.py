from __future__ import annotations

import construct
from construct import GreedyBytes, Prefixed, Struct, VarInt

from retro_data_structures import compression


def test_build_parse_lzo():
    s = Struct(
        header=Prefixed(VarInt, GreedyBytes), length=VarInt, body=compression.LZOCompressedBlock(construct.this.length)
    )

    data = {
        "header": b"abcdef",
        "length": 100,
        "body": b"\x01" * 100,
    }

    encoded = s.build(data)
    decoded = s.parse(encoded)

    assert data == decoded
