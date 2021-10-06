"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import hashlib
import io

import construct
from construct import (Adapter, Aligned, Array, Computed, Const, Container,
                       GreedyBytes, IfThenElse, Int32ub, ListContainer,
                       Prefixed, Rebuild, Struct, Switch, Tell, len_, this)
from retro_data_structures.common_types import Transform4f
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.construct_extensions import \
    PrefixedWithPaddingBefore
from retro_data_structures.data_section import (DataSectionSizes,
                                                GetDataSectionId,
                                                GetDataSectionSize)
from retro_data_structures.formats.area_collision import AreaCollision
from retro_data_structures.formats.lights import Lights
from retro_data_structures.formats.script_layer import SCGN, SCLY
from retro_data_structures.formats.world_geometry import \
    WorldGeometryCompressedBlockAdapter
from retro_data_structures.game_check import (AssetIdCorrect, Game,
                                              get_current_game)


def DataSectionGroup(decompress):
    return Struct(
        "header" / Computed(lambda this: this._.headers[this._index]),
        "address" / Tell,
        "decompressed" / Computed(decompress),
        "data" / IfThenElse(
            this.header.compressed_size > 0,
            PrefixedWithPaddingBefore(
                Computed(this.header.compressed_size),
                IfThenElse(
                    decompress,
                    LZOCompressedBlock(this.header.uncompressed_size),
                    GreedyBytes
                )
            ),
            Aligned(32, Prefixed(Computed(this.header.uncompressed_size), GreedyBytes))
        ),
    )

class DataSectionGroupAdapter(Adapter):
    def _decode(self, group, context, path):
        sections = []
        offset = 0

        for i in range(group.header.section_count):
            section_id = GetDataSectionId(context)
            section_size = GetDataSectionSize(context)
            
            data = b''
            if group.decompressed:
                data = group.data[offset:offset+section_size]
            elif i == 0:
                data = group.data

            sections.append(Container(
                data=data,
                hash=hashlib.sha256(data).hexdigest(),
                size=section_size,
                id=section_id,
                _decompressed=group.decompressed,
                group_address=group.address
            ))

            offset += section_size
        
        return ListContainer(sections)
    
    def _encode(self, group, context, path):
        #print(group)
        return {"data": b''.join([section.data for section in group])}

class CompressedBlocksAdapter(Adapter):
    def _decode_category(self, category, subcon, context, path):
        for i in range(len(category)):
            section = category[i]

            if section._decompressed:
                decoded = subcon._parse(io.BytesIO(section.data), context, path)
                category[i].data = decoded
        return category
    
    def _encode_category(self, category, subcon, context, path):
        for i in range(len(category)):
            section = category[i]

            if section._decompressed:
                encoded = io.BytesIO()
                subcon._build(section.data, encoded, context, path)
                category[i].data = encoded.getvalue()
        return category
    
    def _geometry_codec(self, category, context, path, encode):
        return

    def _category_encodings(self):
        return {
            "script_layers_section": SCLY,
            "generated_script_objects_section": SCGN,
            "collision_section": AreaCollision,
            "lights_section": Lights,
            # TODO: implement these formats
            #"visibility_tree_section": VISI,
            "path_section": AssetIdCorrect,
            "portal_area_section": AssetIdCorrect,
            "static_geometry_map_section": AssetIdCorrect
        }

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
        
        self._geometry_codec(sections["geometry_section"], context, path, encode=False)
        for category, subcon in self._category_encodings().items():
            self._decode_category(sections[category], subcon, context, path)

        return sections

    def _encode(self, sections, context, path):
        groups = []

        current_group_size = 0
        current_group = []
        previous_label = ""

        self._geometry_codec(sections["geometry_section"], context, path, encode=True)
        for category, subcon in self._category_encodings().items():
            self._encode_category(sections[category], subcon, context, path)

        def add_group(reason):
            nonlocal current_group, current_group_size
            # print(f"Group complete! {reason} Group size: {current_group_size}")
            groups.append(current_group)
            current_group = []
            current_group_size = 0

        for cat_label, cat_sections in sorted(sections.items(), key=lambda item: item[1][0].id):
            for section in cat_sections:
                def start_new_group():
                    if current_group_size == 0:
                        return (False, "")
                    if current_group_size + section.size > 0x20000:
                        return (True, "Next section too big.")
                    if cat_label == "script_layers_section":
                        return (True, "New SCLY section.")
                    elif previous_label == "script_layers_section":
                        return (True, "Previous SCLY completed.")
                    if cat_label == "generated_script_objects_section":
                        return (True, "New SCGN section.")
                    elif previous_label == "generated_script_objects_section":
                        return (True, "Previous SCGN completed.")
                    return (False, "")
            
                start_new, reason = start_new_group()
                if start_new:
                    add_group(reason)
                
                current_group.append(section)
                current_group_size += section.size
            
            previous_label = cat_label
        
        add_group("Final group.")
        
        return groups

def CompressedBlocks(parse_block_func):
    return Aligned(32, Array(
        this.compressed_block_count,
        DataSectionGroupAdapter(DataSectionGroup(parse_block_func))
    ))

def _previous_sections(this):
    return sum([header.section_count for header in this._root.headers[0:this._index]])

def IncludeScriptLayers(this):
    """Parses only SCLY and SCGN sections."""
    root = this._root
    previous_sections = _previous_sections(this)
    scly_sections = previous_sections >= root.script_layers_section-1 and previous_sections < (root.script_layers_section + root.script_layer_count)
    scgn_section = previous_sections == root.generated_script_objects_section
    return scly_sections or scgn_section

def IncludeAssetIdLayers(this):
    """Parses only sections which hold single Asset IDs."""
    root = this._root
    previous_sections = _previous_sections(this)
    path_section = previous_sections == root.path_section
    portal_area_section = previous_sections == root.portal_area_section
    static_geometry_map_section = previous_sections == root.static_geometry_map_section
    return path_section or portal_area_section or static_geometry_map_section

def create(version: int, parse_block_func):
    fields = [
        "magic" / Const(0xDEADBEEF, Int32ub),
        "version" / Const(version, Int32ub),

        # Matrix that represents the area's transform from the origin.
        # Most area data is pre-transformed, so this matrix is only used occasionally.
        "area_transform" / Transform4f,

        # Number of world models in this area.
        # TODO: rebuild
        "world_model_count" / Int32ub,

        # Number of script layers in this area.
        "script_layer_count" / Rebuild(Int32ub, len_(this.sections.script_layers_section)),

        # Number of data sections in the file.
        "data_section_count" / Rebuild(
            Int32ub,
            lambda this: sum(map(
                lambda cat: len(cat),
                this.sections.values()
            ))
        ),

        # Section index for world geometry data. Always 0; starts on materials.
        "geometry_section" / Rebuild(Int32ub, lambda this: this.sections["geometry_section"][0].id),

        # Section index for script layer data.
        "script_layers_section" / Rebuild(Int32ub, lambda this: this.sections["script_layers_section"][0].id),

        # Section index for generated script object data.
        "generated_script_objects_section" / Rebuild(Int32ub, lambda this: this.sections["generated_script_objects_section"][0].id),

        # Section index for collision data.
        "collision_section" / Rebuild(Int32ub, lambda this: this.sections["collision_section"][0].id),

        # Section index for first unknown section.
        "unknown_section_1" / Rebuild(Int32ub, lambda this: this.sections["unknown_section_1"][0].id),

        # Section index for light data.
        "lights_section" / Rebuild(Int32ub, lambda this: this.sections["lights_section"][0].id),

        # Section index for visibility tree data.
        "visibility_tree_section" / Rebuild(Int32ub, lambda this: this.sections["visibility_tree_section"][0].id),

        # Section index for path data.
        "path_section" / Rebuild(Int32ub, lambda this: this.sections["path_section"][0].id),

        # Section index for second unknown section.
        "unknown_section_2" / Rebuild(Int32ub, lambda this: this.sections["unknown_section_2"][0].id),

        # Section index for portal area data.
        "portal_area_section" / Rebuild(Int32ub, lambda this: this.sections["portal_area_section"][0].id),

        # Section index for static geometry map data.
        "static_geometry_map_section" / Rebuild(Int32ub, lambda this: this.sections["static_geometry_map_section"][0].id),

        # Number of compressed data blocks in the file.
        "compressed_block_count" / Aligned(16, Rebuild(Int32ub, len_(this.headers))),

        # Array containing the size of each data section in the file. Every size is always a multiple of 32.
        "data_section_sizes" / Aligned(32, DataSectionSizes(
            this._.data_section_count,
            True, 
            lambda this: sorted(
                [x for l in this._root.sections.values() for x in l],
                key=lambda section: section.id
            )[this._index].size)
        ),
        "_current_section" / Computed(0),

        # Sections. Each group is compressed separately
        "headers" / Aligned(32, Array(this.compressed_block_count, Struct(
            "address" / Tell,
            # TODO: all of these should be rebuilt
            "buffer_size" / Int32ub,
            "uncompressed_size" / Int32ub,
            "compressed_size" / Int32ub,
            "section_count" / Int32ub, 
        ))),
        
        # FIXME: recompression doesn't match with original when building
        "sections" / WorldGeometryCompressedBlockAdapter(CompressedBlocks(parse_block_func)),

    ]

    return Struct(*fields)


def Prime2MREA(parse_block_func):
    return create(0x19, parse_block_func)

def MREA(parse_block_func=IncludeScriptLayers):
        return Switch(
        get_current_game,
        {
            Game.ECHOES: Prime2MREA(parse_block_func),
        },
        construct.Error,
    )
