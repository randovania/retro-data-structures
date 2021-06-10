"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""

import construct
from construct import (
    Int32ub, Struct, Const, Float32b, Array, Aligned, Computed, Switch, Peek, FocusedSeq, Sequence
)

from retro_data_structures.common_types import AssetId32
from retro_data_structures.compression import LZOCompressedBlock


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


Prime2MREA = create(0x19, AssetId32)

MREA = FocusedSeq(
    "mrea",
    header=Peek(Sequence(Int32ub, Int32ub)),
    mrea=Switch(
        construct.this.header[1],
        {
            0x19: Prime2MREA,
        },
        construct.Error,
    )
)
