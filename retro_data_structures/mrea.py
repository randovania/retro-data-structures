"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import math
import sys

import construct
import lzokay
from construct import (
    Int32ub, Struct, Const, Float32b, Array, Aligned, Int16sb
)


class LZOSegment(construct.Construct):
    def __init__(self, segment_size: int):
        super().__init__()
        self.segment_size = segment_size

    def _parse(self, stream, context, path):
        segment_size = Int16sb._parsereport(stream, context, path)
        data = construct.stream_read(stream, abs(segment_size), path)
        if segment_size < 0:
            return data
        else:
            return lzokay.decompress(data, self.segment_size)


class MaybeCompressedBytes(construct.Construct):
    def length(self, context):
        block = context.compressed_blocks[context._index]
        if block.compressed_size == 0:
            return block.uncompressed_size, False
        else:
            return block.compressed_size, True

    def _parse(self, stream, context, path):
        length, compressed = self.length(context)

        if compressed:
            start_offset = 32 - (length % 32)
            if start_offset != 32:
                construct.stream_read(stream, start_offset, path)

        if compressed:
            block = context.compressed_blocks[context._index]
            num_segments = block.uncompressed_size / 0x4000

            size_left = block.uncompressed_size
            segments = []
            for _ in range(math.ceil(num_segments)):
                new_segment = LZOSegment(min(0x4000, size_left))._parsereport(stream, context, path)
                size_left -= len(new_segment)
                segments.append(new_segment)

            assert size_left == 0

            return b"".join(segments)
        else:
            return construct.stream_read(stream, length, path)

    def _build(self, obj, stream, context, path):
        length, compressed = self.length(context)

        if compressed:
            start_offset = 32 - (length % 32)
            if start_offset != 32:
                construct.stream_write(stream, b"\x00" * start_offset, start_offset, path)

        data = construct.integer2bytes(obj, length) if isinstance(obj, int) else obj
        data = bytes(data) if type(data) is bytearray else data
        construct.stream_write(stream, data, length, path)
        return data

    def _sizeof(self, context, path):
        try:
            return self.length(context)[0]
        except (KeyError, AttributeError):
            raise construct.SizeofError("cannot calculate size, key not found in context", path=path)


def create(version: int, asset_id):
    fields = [
        "magic" / Const(0xDEADBEEF, Int32ub),
        "version" / Const(version, Int32ub),

        # Matrix that represents the area's transform from the origin.
        # Most area data is pre-transformed, so this matrix is only used occasionally.
        "area_transform" / Array(12, Float32b),

        # Number of world models in this area.
        "world_model_count" / Int32ub,

        # Number of script layers in this area.
        "script_layer_count" / Int32ub,

        # Number of data sections in the file.
        "data_section_count" / Int32ub,

        # Section index for world geometry data. Always 0; starts on materials.
        "geometry_section" / Int32ub,

        # Section index for script layer data.
        "script_layers_section" / Int32ub,

        # Section index for generated script object data.
        "generated_script_objects_section" / Int32ub,

        # Section index for collision data.
        "collision_section" / Int32ub,

        # Section index for first unknown section.
        "unknown_section_1" / Int32ub,

        # Section index for light data.
        "lights_section" / Int32ub,

        # Section index for visibility tree data.
        "visibility_tree_section" / Int32ub,

        # Section index for path data.
        "path_section" / Int32ub,

        # Section index for second unknown section.
        "unknown_section_2" / Int32ub,

        # Section index for portal area data.
        "portal_area_section" / Int32ub,

        # Section index for static geometry map data.
        "static_geometry_map_section" / Int32ub,

        # Number of compressed data blocks in the file.
        "compressed_block_count" / Aligned(16, Int32ub),

        # Array containing the size of each data section in the file. Every size is always a multiple of 32.
        "data_section_sizes" / Aligned(32, Array(construct.this.data_section_count, Int32ub)),

        "compressed_blocks" / Aligned(32, Array(construct.this.compressed_block_count, Struct(
            "buffer_size" / Int32ub,
            "uncompressed_size" / Int32ub,
            "compressed_size" / Int32ub,
            "data_section_count" / Int32ub,
        ))),

        "compressed_bytes" / Array(construct.this.compressed_block_count, MaybeCompressedBytes()),
    ]

    return Struct(*fields)


Prime2MREA = create(0x19, Int32ub)


def main():
    mrea = Prime2MREA.parse_file(sys.argv[1])
    print(mrea)


if __name__ == '__main__':
    main()
