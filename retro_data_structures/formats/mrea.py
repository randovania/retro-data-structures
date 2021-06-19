"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import hashlib
import io

import construct
from construct import (
    Int32ub, Struct, Const, Float32b, Array, Aligned, Computed, Switch, Peek, FocusedSeq, Sequence, IfThenElse,
    Prefixed, GreedyBytes, Adapter, ListContainer, Container, Tell, Rebuild, Pointer
)

from retro_data_structures.common_types import AssetId32
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.data_section import DataSectionSizes


class PrefixedWithPaddingBefore(construct.Subconstruct):
    def __init__(self, length_field, subcon):
        super().__init__(subcon)
        self.padding = 32
        self.length_field = length_field

    def _parse(self, stream, context, path):
        length = self.length_field._parsereport(stream, context, path)
        bytes_to_pad = self.padding - (length % self.padding)
        if bytes_to_pad < self.padding:
            construct.stream_read(stream, bytes_to_pad, path)
        data = construct.stream_read(stream, length, path)
        if self.subcon is GreedyBytes:
            return data
        return self.subcon._parsereport(io.BytesIO(data), context, path)

    def _build(self, obj, stream, context, path):
        stream2 = io.BytesIO()
        buildret = self.subcon._build(obj, stream2, context, path)
        data = stream2.getvalue()
        length = len(data)
        self.length_field._build(length, stream, context, path)

        bytes_to_pad = self.padding - (length % self.padding)
        if bytes_to_pad < self.padding:
            construct.stream_write(stream, b"\x00" * bytes_to_pad, bytes_to_pad, path)

        construct.stream_write(stream, data, len(data), path)
        return buildret


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
        "_data_section_sizes" / Aligned(32, DataSectionSizes(construct.this.data_section_count)),
    ]

    class DataSectionInGroup(Adapter):
        def _decode(self, group, context, path):
            if "section_count_offset" not in context:
                context["section_count_offset"] = 0

            sections = []
            offset = 0
            for i in range(group.section_count):
                section_size = context._._data_section_sizes[context.section_count_offset + i]
                sections.append(Container(data=group.data[offset:offset + section_size.value]))
                offset += section_size.value

            context.section_count_offset += group.section_count

            return ListContainer(sections)

        def _encode(self, sections, context, path):
            if sections:
                raise NotImplementedError

            compressed_blocks = []

            return ListContainer(compressed_blocks)

    fields.extend([
        "section_groups" / Aligned(32, FocusedSeq(
            "groups",
            headers=Array(construct.this._._compressed_block_count, Struct(
                address=Tell,
                value=Struct(
                    "buffer_size" / Int32ub,
                    "uncompressed_size" / Int32ub,
                    "compressed_size" / Int32ub,
                    "section_count" / Int32ub,
                ),
            )),
            groups=Array(
                construct.this._._compressed_block_count,
                DataSectionInGroup(Struct(
                    _header=Computed(lambda this: this._.headers[this._index]),
                    section_count=Pointer(lambda this: this._header.address + 12, Int32ub),
                    data=IfThenElse(
                        construct.this._header.value.compressed_size == 0,
                        Prefixed(Pointer(lambda this: this._header.address + 4, Int32ub), GreedyBytes),
                        PrefixedWithPaddingBefore(Computed(lambda this: this._header.value.compressed_size),
                                                  LZOCompressedBlock(0x0),
                                                  ),
                    ),

                    # Adding some hash to easy validation
                    hash=Computed(lambda this: hashlib.sha256(this.data).hexdigest())
                )),
            )
        )),
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
