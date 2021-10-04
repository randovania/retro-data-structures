"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import hashlib
import io

import construct
from construct import (
    Int32ub, Struct, Const, Float32b, Array, Aligned, GreedyBytes, ListContainer, Container, Rebuild,
    Tell, Computed, FocusedSeq, IfThenElse, Prefixed, Pointer, Subconstruct, Switch
)

from retro_data_structures import game_check
from retro_data_structures.common_types import AssetId32
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.data_section import DataSectionSizes, DataSectionSizePointer
from retro_data_structures.construct_extensions import PrefixedWithPaddingBefore

class DataSectionInGroup(Subconstruct):
    def _parse(self, stream, context, path):
        group = self.subcon._parsereport(stream, context, path)

        size_pointer = DataSectionSizePointer()

        sections = []
        offset = 0
        for i in range(group.section_count):
            section_size = size_pointer._parsereport(stream, context, path)
            data = group.data[offset:offset + section_size]

            sections.append(Container(
                data=data,
                hash=hashlib.sha256(data).hexdigest(),
            ))
            offset += section_size

        return Container(
            compressed=group.header.value.compressed_size > 0,
            sections=ListContainer(sections),
        )

    def _build(self, sections, stream, context, path):
        if sections:
            raise NotImplementedError

        compressed_blocks = []
        obj2 = ListContainer(compressed_blocks)

        buildret = self.subcon._build(obj2, stream, context, path)

        return obj2


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
        "_compressed_block_count" / Aligned(16, Rebuild(Int32ub, construct.len_(construct.this.section_groups))),

        # Array containing the size of each data section in the file. Every size is always a multiple of 32.
        "_data_section_sizes" / Aligned(32, DataSectionSizes(construct.this._root.data_section_count)),
        "_current_section" / construct.Computed(lambda this: 0),

        # Sections. Each group is compressed separately
        "section_groups" / FocusedSeq(
            "groups",
            headers=Aligned(32, Array(construct.this._._compressed_block_count, Struct(
                address=Tell,
                value=Struct(
                    "buffer_size" / Int32ub,
                    "uncompressed_size" / Int32ub,
                    "compressed_size" / Int32ub,
                    "section_count" / Int32ub,
                ),
            ))),
            groups=Aligned(32, Array(
                construct.this._._compressed_block_count,
                DataSectionInGroup(Struct(
                    header=Computed(lambda this: this._.headers[this._index]),
                    section_count=Pointer(lambda this: this.header.address + 12, Int32ub),
                    data=IfThenElse(
                        lambda this: this.header.value.compressed_size > 0,
                        PrefixedWithPaddingBefore(
                            Computed(lambda this: this.header.value.compressed_size),
                            LZOCompressedBlock(lambda this: this.header.value.uncompressed_size),
                        ),

                        Prefixed(Pointer(lambda this: this.header.address + 4, Int32ub), GreedyBytes),
                    ),
                )),
            )),
        ),
    ]

    return Struct(*fields)


Prime2MREA = create(0x19, AssetId32)

MREA = Switch(
    game_check.get_current_game,
    {
        game_check.Game.ECHOES: Prime2MREA,
    },
    construct.Error,
)
