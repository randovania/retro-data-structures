import io
import math

import construct
import lzokay
from construct import GreedyRange, Adapter


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
        decompressed_size = construct.evaluate(self.decompressed_size, context)

        length = construct.Int16sb._parsereport(stream, context, path)
        data = construct.stream_read(stream, abs(length), path)
        if length > 0:
            result = self.subcon._parsereport(io.BytesIO(data), context, path)
            if len(result) != decompressed_size:
                raise construct.StreamError(
                    f"Expected to decompress {decompressed_size} bytes, got {len(result)}", path
                )
            return result
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


class LZOCompressedBlock(Adapter):
    def __init__(self, decompressed_size, segment_size=0x4000):
        super().__init__(GreedyRange(LZOSegment(self._actual_segment_size)))
        self.decompressed_size = decompressed_size
        self.segment_size = segment_size

    def _actual_segment_size(self, context):
        decompressed_size = construct.evaluate(self.decompressed_size, context)
        segment_size = construct.evaluate(self.segment_size, context)

        previous_segments = context._index * segment_size
        if previous_segments > decompressed_size:
            # This segment is redundant!
            raise construct.StopFieldError()

        elif previous_segments + segment_size > decompressed_size:
            # Last segment
            return decompressed_size - previous_segments

        else:
            # Another segment with this size
            return segment_size

    def _decode(self, segments, context, path):
        return b"".join(segments)

    def _encode(self, uncompressed, context, path):

        decompressed_size = construct.evaluate(self.decompressed_size, context)
        if decompressed_size != len(uncompressed):
            raise ValueError("Decompressed size {} doesn't match size of data to compress ({}) at {}".format(
                decompressed_size,
                len(uncompressed),
                path,
            ))

        segment_size = self.segment_size
        return [
            uncompressed[segment_size * i : segment_size * (i + 1)]
            for i in range(math.ceil(len(uncompressed) / segment_size))
        ]


ZlibCompressedBlock = construct.Compressed(construct.GreedyBytes, "zlib", level=9)
