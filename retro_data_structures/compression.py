import math

import construct
import lzokay
from construct import Adapter


class AbsInt(Adapter):
    def _decode(self, obj, context, path):
        return abs(obj)

    def _encode(self, obj, context, path):
        return obj


class CompressedLZO(construct.Tunnel):
    def __init__(self, subcon, length):
        super().__init__(subcon)
        self.lib = lzokay
        self.length = length

    def _decode(self, data, context, path):
        length = construct.evaluate(self.length, context)
        return self.lib.decompress(data, length)

    def _encode(self, data, context, path):
        return self.lib.compress(data)


def LZOSegment(decompressed_size):
    return construct.FocusedSeq(
        "data",
        segment_size=construct.Peek(construct.Int16sb),
        data=construct.IfThenElse(
            construct.this.segment_size > 0,
            construct.Prefixed(construct.Int16sb, CompressedLZO(construct.GreedyBytes, decompressed_size)),
            construct.Prefixed(AbsInt(construct.Int16sb), construct.GreedyBytes),
        )
    )


class LZOCompressedBlock(construct.Construct):
    def __init__(self, uncompressed_size, start_offset=None):
        super().__init__()
        self.uncompressed_size = uncompressed_size
        self.start_offset = start_offset

    def _parse(self, stream, context, path):
        if self.start_offset is None:
            if construct.stream_size(stream) % 32:
                raise ValueError("stream size must be a multiple of 32 when start_offset is None")
        else:
            construct.stream_read(stream, construct.evaluate(self.start_offset, context), path)

        uncompressed_size = construct.evaluate(self.uncompressed_size, context)
        num_segments = uncompressed_size / 0x4000
        size_left = uncompressed_size
        segments = []
        for _ in range(math.ceil(num_segments)):
            new_segment = LZOSegment(min(0x4000, size_left))._parsereport(stream, context, path)
            size_left -= len(new_segment)
            segments.append(new_segment)

        assert size_left == 0
        return b"".join(segments)


ZlibCompressedBlock = construct.Compressed(construct.GreedyBytes, "zlib", level=9)
