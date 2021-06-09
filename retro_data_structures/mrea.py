"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import hashlib
import math
import sys

import construct
import lzokay
from construct import (
    Int32ub, Struct, Const, Float32b, Array, Aligned, Int16sb, Computed
)

from retro_data_structures import construct_extensions


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


class LZOCompressedBlock(construct.Construct):
    def __init__(self, compressed_size, uncompressed_size):
        super().__init__()
        self.compressed_size = compressed_size
        self.uncompressed_size = uncompressed_size

    def _parse(self, stream, context, path):
        start_offset = 32 - (self.compressed_size % 32)
        if start_offset != 32:
            construct.stream_read(stream, start_offset, path)

        num_segments = self.uncompressed_size / 0x4000
        size_left = self.uncompressed_size
        segments = []
        for _ in range(math.ceil(num_segments)):
            new_segment = LZOSegment(min(0x4000, size_left))._parsereport(stream, context, path)
            size_left -= len(new_segment)
            segments.append(new_segment)

        assert size_left == 0
        return b"".join(segments)


class CompressedBlocks(construct.Construct):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def _parse(self, stream, context, path):
        count = construct.evaluate(self.count, context)

        headers = Array(count, Struct(
            "buffer_size" / Int32ub,
            "uncompressed_size" / Int32ub,
            "compressed_size" / Int32ub,
            "data_section_count" / Int32ub,
        ))._parsereport(stream, context, path)

        obj = construct.ListContainer()
        for block in headers:
            if block.compressed_size == 0:
                item = construct.stream_read(stream, block.uncompressed_size, path)
            else:
                item = LZOCompressedBlock(
                    block.compressed_size,
                    block.uncompressed_size
                )._parsereport(stream, context, path)

            e = construct.Container()
            e["header"] = block
            e["data"] = item
            obj.append(e)

        return obj


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

        "compressed_blocks" / Aligned(32, CompressedBlocks(construct.this.compressed_block_count)),
    ]

    # And now the computed fields

    def data_section(this):
        index = this["_index"]
        initial_offset = sum(this.data_section_sizes[:index])
        return this.uncompressed_data[initial_offset:initial_offset + this.data_section_sizes[this["_index"]]]

    fields.extend([
        "uncompressed_data" / Computed(lambda this: b"".join(block.data for block in this.compressed_blocks)),
        "data_sections" / Array(construct.this.data_section_count, Computed(data_section)),
    ])

    return Struct(*fields)


Prime2MREA = create(0x19, Int32ub)


def main():
    import pprint
    mrea = Prime2MREA.parse_file(sys.argv[1])
    d = construct_extensions.convert_to_raw_python(mrea)

    for block in d["compressed_blocks"]:
        block["data_hash"] = hashlib.sha256(block.pop("data")).hexdigest()

    d["uncompressed_data"] = hashlib.sha256(d["uncompressed_data"]).hexdigest()
    d["data_sections"] = [hashlib.sha256(it).hexdigest() for it in d["data_sections"]]
    pprint.pprint(d)


if __name__ == '__main__':
    main()
