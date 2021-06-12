"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""

import construct
from construct import (
    Int32ub, Struct, Const, Float32b, Array, Aligned, Computed, Switch, Peek, FocusedSeq, Sequence, IfThenElse,
    Prefixed, GreedyBytes, Adapter, ListContainer
)

from retro_data_structures.common_types import AssetId32
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.data_section import DataSectionSizes


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
        "data_section_sizes" / Aligned(32, DataSectionSizes(construct.this.data_section_count)),
    ]

    class DataSectionInBlocks(Adapter):
        def _decode(self, compressed_blocks, context, path):
            uncompressed_data = b"".join(block.data for block in compressed_blocks)

            sections = []
            offset = 0
            for section_size in context.data_section_sizes:
                sections.append(uncompressed_data[offset:offset + section_size.value])
                offset += section_size.value

            return ListContainer(sections)

        def _encode(self, sections, context, path):
            if sections:
                raise NotImplementedError

            compressed_blocks = []

            return ListContainer(compressed_blocks)

    fields.extend([
        "data_sections" / DataSectionInBlocks(Aligned(32, FocusedSeq(
            "blocks",
            headers=Array(
                construct.this._.compressed_block_count,
                Struct(
                    "buffer_size" / Int32ub,
                    "uncompressed_size" / Int32ub,
                    "compressed_size" / Int32ub,
                    "section_count" / Int32ub,
                )
            ),
            blocks=Array(
                construct.this._.compressed_block_count,
                Struct(
                    header=Computed(lambda this: this._.headers[this._index]),
                    data=IfThenElse(
                        construct.this.header.compressed_size == 0,
                        Prefixed(Computed(construct.this.header.uncompressed_size), GreedyBytes),
                        Prefixed(Computed(lambda this: (this.header.compressed_size + 31) & ~31),
                                 LZOCompressedBlock(construct.this.header.uncompressed_size,
                                                    lambda this: 32 - (this.header.compressed_size % 32))),
                    )
                ),
            ),
        ))),
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
