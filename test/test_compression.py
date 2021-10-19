import construct
from construct import Bytes, Struct, Prefixed, VarInt, GreedyBytes

from retro_data_structures import compression


def test_build_parse_lzo():
    s = Struct(
        header=Prefixed(VarInt, GreedyBytes),
        length=VarInt,
        body=compression.LZOCompressedBlock(construct.this.length)
    )

    data = {
        "header": b"abcdef",
        "length": 100,
        "body": b"\x01" * 100,
    }

    encoded = s.build(data)
    decoded = s.parse(encoded)

    assert data == decoded

