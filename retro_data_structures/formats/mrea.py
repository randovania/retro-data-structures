"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import hashlib
import io

import construct
from construct import (
    RawCopy, Adapter, If, this, Byte, Int32ub, Struct, Const, Float32b, Array, Aligned, GreedyBytes, ListContainer, Container, Rebuild,
    Tell, Computed, FocusedSeq, IfThenElse, Prefixed, Pointer, Subconstruct, Switch
)
from construct.core import FixedSized, RestreamData

from retro_data_structures import game_check
from retro_data_structures.common_types import AssetId32
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.data_section import DataSectionSizePointer, DataSectionSizes, GetDataSectionId, GetDataSectionSize
from retro_data_structures.construct_extensions import PrefixedWithPaddingBefore

DataSectionGroup = Struct(
    "header" / Computed(lambda this: this._.headers[this._index]),
    "data" / IfThenElse(
        this.header.compressed_size > 0,
        PrefixedWithPaddingBefore(
            Pointer(this._.header.address + 8, Int32ub),
            LZOCompressedBlock(this._.header.uncompressed_size),
        ),

        Prefixed(Pointer(this.header.address + 4, Int32ub), GreedyBytes),
    )
)

class DataSectionGroupAdapter(Adapter):
    def _decode(self, group, context, path):
        sections = []
        offset = 0

        for i in range(group.header.section_count):
            section_id = GetDataSectionId(context)
            section_size = GetDataSectionSize(context)
            data = group.data[offset:offset+section_size]

            sections.append(Container(
                data=data,
                hash=hashlib.sha256(data).hexdigest(),
                size=section_size,
                id=section_id
            ))

            offset += section_size
        
        return ListContainer(sections)
    
    def _encode(self, group, context, path):
        return b''.join([section.data for section in group])


class CompressedBlocksAdapter(Adapter):
    def _decode(self, section_groups, context, path):
        _sections = []

        for group in section_groups:
            _sections.extend(group)
        
        def cat(label):
            return {"label": label, "value": context[label]}
        
        _categories = sorted([
            cat("geometry_section"),
            cat("script_layers_section"),
            cat("generated_script_objects_section"),
            cat("collision_section"),
            cat("unknown_section_1"),
            cat("lights_section"),
            cat("visibility_tree_section"),
            cat("path_section"),
            cat("unknown_section_2"),
            cat("portal_area_section"),
            cat("static_geometry_map_section"),
            cat("data_section_count")
        ], key=lambda cat:cat["value"])

        sections = {}
        for i in range(len(_categories)-1):
            c = _categories[i]
            start = c["value"]
            end = _categories[i+1]["value"]
            sections[c["label"]] = _sections[start:end]
        
        return sections

    def _encode(self, sections, context, path):
        groups = []

        current_group_size = 0
        current_group = []

        for cat_label, cat_sections in sections.items():
            for section in cat_sections:
                def start_new_group():
                    if current_group_size == 0:
                        return False
                    if current_group_size + section.size > 0x20000:
                        return True
                    if cat_label == "script_layers_section":
                        return True
                    if cat_label == "generated_script_objects_section":
                        return True
            
            if start_new_group():
                groups.append(current_group)
                current_group = []
                current_group_size = 0
            
            current_group.append(section)
            current_group_size += section.size
        
        return groups

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
        "_compressed_block_count" / Aligned(16, Rebuild(Int32ub, construct.len_(construct.this.sections))),

        # Array containing the size of each data section in the file. Every size is always a multiple of 32.
        "_data_section_sizes" / Aligned(32, DataSectionSizes(this._.data_section_count, True)),
        "_current_section" / construct.Computed(lambda this: 0),

        # Sections. Each group is compressed separately
        "sections" / CompressedBlocksAdapter(FocusedSeq(
            "groups",
            headers=Aligned(32, Array(construct.this._._compressed_block_count, Struct(
                "address" / Tell,
                "buffer_size" / Int32ub,
                "uncompressed_size" / Int32ub,
                "compressed_size" / Int32ub,
                "section_count" / Int32ub,
            ))),
            groups=Aligned(32, Array(
                construct.this._._compressed_block_count,
                DataSectionGroupAdapter(DataSectionGroup),
            ))),
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
