import io
import math

import construct
import lzokay
from construct import GreedyRange, ExprAdapter


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


class LZOSegment(construct.Subconstruct):
    def __init__(self, decompressed_size):
        super().__init__(CompressedLZO(construct.GreedyBytes, decompressed_size))
        self.decompressed_size = decompressed_size

    def _parse(self, stream, context, path):
        length = construct.Int16sb._parsereport(stream, context, path)
        data = construct.stream_read(stream, abs(length), path)
        if length > 0:
            return self.subcon._parsereport(io.BytesIO(data), context, path)
        else:
            return data

    def _build(self, uncompressed, stream, context, path):
        stream2 = io.BytesIO()
        buildret = self.subcon._build(uncompressed, stream2, context, path)
        compressed_data = stream2.getvalue()
        if len(compressed_data) < len(uncompressed):
            construct.Int16sb._build(len(compressed_data), stream, context, path)
            construct.stream_write(stream, compressed_data, len(compressed_data), path)
            return buildret
        else:
            construct.Int16sb._build(-len(uncompressed), stream, context, path)
            construct.stream_write(stream, uncompressed, len(uncompressed), path)
            return buildret


def LZOCompressedBlock(decompressed_size, segment_size=0x4000):
    return ExprAdapter(
        GreedyRange(LZOSegment(segment_size)),
        lambda segments, ctx: b"".join(segments),
        lambda uncompressed, ctx: [uncompressed[segment_size * i:segment_size * (i + 1)]
                                   for i in range(math.ceil(len(uncompressed) / segment_size))]
    )


ZlibCompressedBlock = construct.Compressed(construct.GreedyBytes, "zlib", level=9)
