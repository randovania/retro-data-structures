"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import io
import typing
from enum import IntEnum
from typing import Iterator, Optional

import construct
from construct import Struct, PrefixedArray, Int32ub, If, Aligned
from construct.core import (
    Adapter,
    AlignedStruct,
    Array,
    Computed,
    Const,
    Enum,
    FixedSized,
    GreedyBytes,
    Int8ub,
    Pointer,
    Rebuild,
    Tell,
    len_,
    this,
)
from construct.lib.containers import Container, ListContainer

from retro_data_structures import game_check
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.common_types import FourCC, Transform4f
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.construct_extensions.alignment import PrefixedWithPaddingBefore
from retro_data_structures.construct_extensions.misc import Skip
from retro_data_structures.construct_extensions.version import BeforeVersion, WithVersion, WithVersionElse
from retro_data_structures.data_section import DataSection, DataSectionSizes, GetDataSectionId, GetDataSectionSize
from retro_data_structures.formats.area_collision import AreaCollision
from retro_data_structures.formats.arot import AROT
from retro_data_structures.formats.lights import Lights
from retro_data_structures.formats.script_layer import SCGN, SCLY, ScriptLayerHelper
from retro_data_structures.formats.script_object import ScriptInstanceHelper
from retro_data_structures.formats.visi import VISI
from retro_data_structures.game_check import AssetIdCorrect
from retro_data_structures.game_check import Game


class MREAVersion(IntEnum):
    PrimeKioskDemo = 0xC
    Prime = 0xF
    EchoesDemo = 0x15
    Echoes = 0x19
    CorruptionE3Prototype = 0x1D
    Corruption = 0x1E
    DonkeyKongCountryReturns = 0x20


def _decode_data_section_group(subcon, header, stream, context, path):
    group = subcon._parsereport(stream, context, path)

    sections = []
    offset = 0

    for i in range(header.data_section_count):
        section_id = GetDataSectionId(context)
        section_size = GetDataSectionSize(context)

        data = group[offset: offset + section_size]

        sections.append(
            Container(
                data=data,
                id=section_id,
            )
        )

        offset += section_size

    return ListContainer(sections)


class UncompressedDataSections(Adapter):
    def __init__(self):
        super().__init__(
            Array(
                this.header.data_section_count,
                Aligned(32, FixedSized(
                    lambda this: this._root.data_section_sizes.value[this._index],
                    GreedyBytes
                )),
            )
        )

    def _decode(self, sections, context, path):
        decoded = []
        for i, section in enumerate(sections):
            decoded.append(
                Container(
                    data=section,
                    id=i,
                )
            )
        return [ListContainer(decoded)]

    def _encode(self, sections, context, path):
        return [section["data"] for category in sections.values() for section in category]


_all_categories = [
    "geometry_section",
    "unknown_section_2",
    "script_layers_section",
    "generated_script_objects_section",
    "collision_section",
    "unknown_section_1",
    "lights_section",
    "visibility_tree_section",
    "path_section",
    "area_octree_section",
    "portal_area_section",
    "static_geometry_map_section",
]

_CATEGORY_ENCODINGS = {
    "script_layers_section": SCLY,
    "generated_script_objects_section": SCGN,
    "area_octree_section": AROT,
    "collision_section": AreaCollision,
    "lights_section": Lights,
    "visibility_tree_section": VISI,
    "path_section": AssetIdCorrect,
    "portal_area_section": AssetIdCorrect,
    "static_geometry_map_section": AssetIdCorrect,
    "unknown_section_1": Struct(
        magic=If(game_check.is_prime3, Const("LLTE", FourCC)),
        data=Const(1, Int32ub)
    ),
    "unknown_section_2": Struct(
        unk1=PrefixedArray(Int32ub, Int32ub),
        # TODO: rebuild according to surface group count
        unk2=PrefixedArray(Int32ub, Enum(Int8ub, ON=0xFF, OFF=0x00)),
    ),
}


class SectionCategoryAdapter(Adapter):
    def _decode_category(self, category: ListContainer, subcon, context, path):
        for section in category:
            if len(section["data"]) > 0:
                decoded = subcon._parse(io.BytesIO(section["data"]), context, path)
                data = decoded
            else:
                data = None

            section.data = data

    def _encode_category(self, category: ListContainer, subcon, context, path):
        result = ListContainer()

        for section in category:
            if section["data"] is not None:
                encoded = io.BytesIO()
                subcon._build(section["data"], encoded, context, path)
                data = encoded.getvalue()
            else:
                data = b""

            result.append(Container(
                data=data,
                id=section.id,
            ))

        return result

    def _category_encodings(self):
        return {
            "script_layers_section": SCLY,
            "generated_script_objects_section": SCGN,
            "area_octree_section": AROT,
            "collision_section": AreaCollision,
            "lights_section": Lights,
            "visibility_tree_section": VISI,
            "path_section": AssetIdCorrect,
            "portal_area_section": AssetIdCorrect,
            "static_geometry_map_section": AssetIdCorrect,
            "unknown_section_1": Struct(
                "magic" / If(game_check.is_prime3, Const("LLTE", FourCC)),
                "data" / Const(1, Int32ub)
            ),
            "unknown_section_2": Struct(
                "unk1" / PrefixedArray(Int32ub, Int32ub),
                # TODO: rebuild according to surface group count
                "unk2" / PrefixedArray(Int32ub, Enum(Int8ub, ON=0xFF, OFF=0x00)),
            ),
        }

    def _decode(self, section_groups, context, path):
        _sections = []

        for group in section_groups:
            _sections.extend(group)

        def cat(label):
            return {"label": label, "value": context.header[label] if isinstance(context.header[label], int) else -1}

        _categories = [c for label in _all_categories if (c := cat(label))["value"] != -1]
        _categories.sort(key=lambda c: c["value"])

        sections = Container()
        for i, c in enumerate(_categories):
            start = c["value"]
            end = None
            if i < len(_categories) - 1:
                end = _categories[i + 1]["value"]
            sections[c["label"]] = ListContainer(_sections[start:end])

        # GeometryCodec(sections["geometry_section"], context, path, encode=False, codec=self._decode_category)
        for category, subcon in self._category_encodings().items():
            if category in sections or hasattr(sections, category):
                self._decode_category(sections[category], subcon, context, path)

        return sections

    def _encode(self, sections: Container, context, path):
        result = Container()

        # FIXME: World Geometry is not building correctly
        # GeometryCodec(sections["geometry_section"], context, path, encode=True, codec=self._encode_category)
        for category, subcon in self._category_encodings().items():
            if category in sections or hasattr(sections, category):
                result[category] = self._encode_category(sections[category], subcon, context, path)

        return result


class CompressedBlocksAdapter(SectionCategoryAdapter):
    def __init__(self):
        def get_size(ctx):
            header = ctx._.headers[ctx._index]
            if not header.compressed_size:
                return header.uncompressed_size
            return header.compressed_size + (-header.compressed_size % 32)

        super().__init__(AlignedStruct(
            32,
            "headers" / PrefixedArray(
                Pointer(this._root.header.compressed_block_count_addr, Int32ub),
                Struct(
                    "buffer_size" / Int32ub,
                    "uncompressed_size" / Int32ub,
                    "compressed_size" / Int32ub,
                    "data_section_count" / Int32ub,
                ),
            ),
            "groups" / PrefixedArray(
                Pointer(this._root.header.compressed_block_count_addr, Int32ub),
                FixedSized(get_size, GreedyBytes)
            )
        ))

    def _get_subcon(self, compressed_size, uncompressed_size, context):
        if compressed_size:
            return PrefixedWithPaddingBefore(Computed(compressed_size), LZOCompressedBlock(uncompressed_size))
        return DataSection(GreedyBytes, size=lambda: Computed(uncompressed_size))

    def _decode(self, section_groups, context, path):
        assert len(section_groups.headers) == len(section_groups.groups)
        decoded = ListContainer()

        for header, group in zip(section_groups.headers, section_groups.groups):
            subcon = self._get_subcon(header.compressed_size, header.uncompressed_size, context)
            decoded.append(
                _decode_data_section_group(subcon, header, io.BytesIO(group), context, path)
            )

        return super()._decode(decoded, context, path)

    def _start_new_group(self, group_size, section_size, curr_label, prev_label):
        if group_size == 0:
            return False, ""

        if group_size + section_size > 0x20000:
            return True, "Next section too big."

        if curr_label == "script_layers_section":
            return True, "New SCLY section."

        elif prev_label == "script_layers_section":
            return True, "Previous SCLY completed."

        if curr_label == "generated_script_objects_section":
            return True, "New SCGN section."

        elif prev_label == "generated_script_objects_section":
            return True, "Previous SCGN completed."

        return False, ""

    def _build(self, obj, stream, context, path):
        self._current_stream = stream
        return super()._build(obj, stream, context, path)

    def _encode(self, sections, context, path):
        sections = super()._encode(sections, context, path)

        compressed_blocks = ListContainer()

        current_group_size = 0
        current_group = ListContainer()
        previous_label = ""

        def add_group(r):
            nonlocal current_group_size, current_group
            # print(f"Group complete! {r} Group size: {current_group_size}")
            compressed_blocks.append(Container(
                header=Container(
                    buffer_size=current_group_size,
                    uncompressed_size=current_group_size,
                    compressed_size=0,
                    data_section_count=len(current_group)
                ),
                group=current_group,
            ))
            current_group = ListContainer()
            current_group_size = 0

        for cat_label, cat_sections in sorted(sections.items(), key=lambda item: item[1][0]["id"]):
            for section in cat_sections:
                start_new, reason = self._start_new_group(
                    current_group_size, len(section.data),
                    previous_label, cat_label
                )
                if start_new:
                    add_group(reason)

                current_group.append(section)
                current_group_size += len(section.data)

            previous_label = cat_label
        add_group("Final group.")

        for block in compressed_blocks:
            header = block.header
            raw_group = typing.cast(list, block.group)

            group = b"".join(
                section.data.ljust(len(section.data) + (-len(section.data) % 32), b"\x00")
                for section in raw_group
            )
            header.uncompressed_size = len(group)

            substream = io.BytesIO()
            LZOCompressedBlock(header.uncompressed_size)._build(group, substream, context, path)
            compressed_size = len(substream.getvalue())
            if compressed_size < header.uncompressed_size:
                header.compressed_size = compressed_size
                header.buffer_size += 0x120

            substream = io.BytesIO()
            subcon = self._get_subcon(header.compressed_size, header.uncompressed_size, context)
            subcon._build(group, substream, context, path)
            block.group = substream.getvalue()

            current_offset = construct.stream_tell(self._current_stream, path)
            construct.stream_seek(self._current_stream, current_offset, 0, path)

        return Container(
            headers=[block.header for block in compressed_blocks],
            groups=[block.group for block in compressed_blocks]
        )


def _used_categories(this):
    return list(filter(lambda item: this[item], _all_categories))


def MREAHeader():
    def get_section_id(category):
        return lambda self: self._.sections[category][0]["id"]

    return Struct(
        "magic" / Const(0xDEADBEEF, Int32ub),
        "version" / Enum(Int32ub, MREAVersion),

        # Matrix that represents the area's transform from the origin.
        # Most area data is pre-transformed, so this matrix is only used occasionally.
        "area_transform" / Transform4f,

        # Number of world models in this area.
        # TODO: rebuild
        "world_model_count" / Int32ub,

        # Number of script layers in this area.
        "script_layer_count" / WithVersion(
            MREAVersion.Echoes, Rebuild(Int32ub, len_(this._.sections.script_layers_section))
        ),

        # Number of data sections in the file.
        "data_section_count" / Rebuild(Int32ub, lambda self: sum(map(lambda cat: len(cat), self._.sections.values()))),

        # Section index for world geometry data. Always 0; starts on materials.
        "geometry_section" / Rebuild(Int32ub, get_section_id("geometry_section")),

        # Section index for script layer data.
        "script_layers_section" / Rebuild(Int32ub, get_section_id("script_layers_section")),

        # Section index for generated script object data.
        "generated_script_objects_section" / WithVersion(
            MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("generated_script_objects_section"))
        ),

        # Section index for collision data.
        "collision_section" / Rebuild(Int32ub, get_section_id("collision_section")),

        # Section index for first unknown section.
        "unknown_section_1" / Rebuild(Int32ub, get_section_id("unknown_section_1")),

        # Section index for light data.
        "lights_section" / Rebuild(Int32ub, get_section_id("lights_section")),

        # Section index for visibility tree data.
        "visibility_tree_section" / Rebuild(Int32ub, get_section_id("visibility_tree_section")),

        # Section index for path data.
        "path_section" / Rebuild(Int32ub, get_section_id("path_section")),

        # Section index for area octree data.
        "area_octree_section" / BeforeVersion(
            MREAVersion.EchoesDemo, Rebuild(Int32ub, get_section_id("area_octree_section"))
        ),

        # Section index for second unknown section.
        "unknown_section_2" / WithVersion(MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("unknown_section_2"))),

        # Section index for portal area data.
        "portal_area_section" / WithVersion(
            MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("portal_area_section"))
        ),

        # Section index for static geometry map data.
        "static_geometry_map_section" / WithVersion(
            MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("static_geometry_map_section"))
        ),

        # Number of compressed data blocks in the file.
        "compressed_block_count_addr" / WithVersion(MREAVersion.Echoes, Tell),

        WithVersion(MREAVersion.Echoes, Skip(1, Int32ub)),

        "categories" / Computed(_used_categories),
    )


MREA = AlignedStruct(
    32,
    "_current_section" / Computed(0),

    "header" / MREAHeader(),
    "header_end" / Tell,
    "version" / Computed(this.header.version),

    # Array containing the size of each data section in the file. Every size is always a multiple of 32.
    "data_section_sizes" / DataSectionSizes(
        this._.header.data_section_count,
        True,
        lambda ctx: 0,
    ),

    "sections" / WithVersionElse(
        MREAVersion.Echoes,
        CompressedBlocksAdapter(),
        SectionCategoryAdapter(UncompressedDataSections())
    ),
)

MREAHeader_v2 = Aligned(32, Struct(
    "magic" / Const(0xDEADBEEF, Int32ub),
    "version" / Enum(Int32ub, MREAVersion),

    # Matrix that represents the area's transform from the origin.
    # Most area data is pre-transformed, so this matrix is only used occasionally.
    "area_transform" / Transform4f,

    # Number of world models in this area.
    "world_model_count" / Int32ub,

    # Number of script layers in this area.
    "script_layer_count" / WithVersion(MREAVersion.Echoes, Int32ub),

    # Number of data sections in the file.
    "data_section_count" / Int32ub,

    # Section index for world geometry data. Always 0; starts on materials.
    "geometry_section" / Int32ub,

    # Section index for script layer data.
    "script_layers_section" / Int32ub,

    # Section index for generated script object data.
    "generated_script_objects_section" / WithVersion(MREAVersion.Echoes, Int32ub),

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

    # Section index for area octree data.
    "area_octree_section" / BeforeVersion(MREAVersion.EchoesDemo, Int32ub),

    # Section index for second unknown section.
    "unknown_section_2" / WithVersion(MREAVersion.Echoes, Int32ub),

    # Section index for portal area data.
    "portal_area_section" / WithVersion(MREAVersion.Echoes, Int32ub),

    # Section index for static geometry map data.
    "static_geometry_map_section" / WithVersion(MREAVersion.Echoes, Int32ub),

    # Number of compressed data blocks in the file.
    "compressed_block_count" / WithVersion(MREAVersion.Echoes, Int32ub),
))

CompressedBlockHeader = Struct(
    buffer_size=Int32ub,
    uncompressed_size=Int32ub,
    compressed_size=Int32ub,
    data_section_count=Int32ub,
)


def _get_compressed_block_size(header):
    if not header.compressed_size:
        return header.uncompressed_size
    return header.compressed_size + (-header.compressed_size % 32)


def _get_compressed_block_subcon(compressed_size, uncompressed_size):
    if compressed_size:
        return PrefixedWithPaddingBefore(Computed(compressed_size), LZOCompressedBlock(uncompressed_size))
    return DataSection(GreedyBytes, size=lambda: Computed(uncompressed_size))


def _decode_category(category: typing.List[bytes], subcon: construct.Construct, context, path):
    result = ListContainer()

    for section in category:
        if len(section) > 0:
            data = subcon._parse(io.BytesIO(section), context, path)
        else:
            data = None

        result.append(data)

    return result


def _encode_category(category: typing.List, subcon: construct.Construct, context, path) -> typing.List[bytes]:
    result = ListContainer()

    for section in category:
        if section is not None:
            stream = io.BytesIO()
            Aligned(32, subcon)._build(section, stream, context, path)
            data = stream.getvalue()
        else:
            data = b""

        result.append(data)

    return result


class MREAConstruct(construct.Construct):
    def _decode_compressed_blocks(self, mrea_header, data_section_sizes, stream, context, path) -> typing.List[bytes]:
        compressed_block_headers = Aligned(32, Array(mrea_header.compressed_block_count, CompressedBlockHeader)
                                           )._parsereport(stream, context, path)
        # Read compressed blocks from stream
        compressed_blocks = construct.ListContainer(
            Aligned(32, FixedSized(_get_compressed_block_size(header), GreedyBytes)
                    )._parsereport(stream, context, path)
            for header in compressed_block_headers
        )

        # Decompress blocks into the data sections
        data_sections = ListContainer()
        for compressed_header, compressed_block in zip(compressed_block_headers, compressed_blocks):
            subcon = _get_compressed_block_subcon(compressed_header.compressed_size,
                                                  compressed_header.uncompressed_size)
            decompressed_block = subcon._parsereport(io.BytesIO(compressed_block), context, path)
            if len(decompressed_block) != compressed_header.uncompressed_size:
                raise construct.ConstructError(
                    f"Expected {compressed_header.uncompressed_size} bytes, got {len(decompressed_block)}",
                    path,
                )
            offset = 0

            for i in range(compressed_header.data_section_count):
                section_size = data_section_sizes[len(data_sections)]
                data = decompressed_block[offset: offset + section_size]
                data_sections.append(data)
                offset += section_size

        return data_sections

    def _parse(self, stream, context, path):
        mrea_header = MREAHeader_v2._parsereport(stream, context, path)
        data_section_sizes = Array(mrea_header.data_section_count, Int32ub)._parsereport(stream, context, path)

        if mrea_header.compressed_block_count is not None:
            data_sections = self._decode_compressed_blocks(mrea_header, data_section_sizes, stream, context, path)
        else:
            data_sections = Array(
                mrea_header.data_section_count,
                Aligned(32, FixedSized(lambda ctx: data_section_sizes[ctx._index], GreedyBytes)),
            )._parsereport(stream, context, path)

        # Split data sections into the named sections
        categories = [
            {"label": label, "value": mrea_header[label]}
            for label in _all_categories
            if mrea_header[label] is not None
        ]
        categories.sort(key=lambda c: c["value"])

        sections = Container()
        for i, c in enumerate(categories):
            start = c["value"]
            end = None
            if i < len(categories) - 1:
                end = categories[i + 1]["value"]
            sections[c["label"]] = data_sections[start:end]

        # Decode each category
        for category, subcon in _CATEGORY_ENCODINGS.items():
            if category in sections:
                sections[category] = _decode_category(sections[category], subcon, context, path)

        return Container(
            version=mrea_header.version,
            area_transform=mrea_header.area_transform,
            world_model_count=mrea_header.world_model_count,
            sections=sections,
        )

    def _encode_compressed_blocks(self, data_sections: typing.List[bytes],
                                  category_starts: typing.Dict[str, typing.Optional[int]],
                                  context, path):
        def _start_new_group(group_size, section_size, curr_label, prev_label):
            if group_size == 0:
                return False, ""

            if group_size + section_size > 0x20000:
                return True, "Next section too big."

            if curr_label == "script_layers_section":
                return True, "New SCLY section."

            elif prev_label == "script_layers_section":
                return True, "Previous SCLY completed."

            if curr_label == "generated_script_objects_section":
                return True, "New SCGN section."

            elif prev_label == "generated_script_objects_section":
                return True, "Previous SCGN completed."

            return False, ""

        compressed_blocks = ListContainer()
        filtered_starts = [(cat, start) for cat, start in category_starts.items() if start is not None]
        filtered_starts.sort(key=lambda it: it[1])
        category_starts = dict(filtered_starts)

        current_group_size = 0
        current_group = []
        previous_label = ""

        def add_group(r):
            nonlocal current_group_size, current_group
            # print(f"Group complete! {r} Group size: {current_group_size}")

            # The padding is not included in the block's uncompressed size
            merged_and_padded_group = b"".join(
                item.ljust(len(item) + (-len(item) % 32), b"\x00")
                for item in current_group
            )
            header = Container(
                buffer_size=current_group_size,
                uncompressed_size=current_group_size,
                compressed_size=0,
                data_section_count=len(current_group)
            )

            substream = io.BytesIO()
            LZOCompressedBlock(header.uncompressed_size)._build(merged_and_padded_group, substream, context, path)
            data = substream.getvalue()
            compressed_size = len(data)
            compressed_pad = (32 - (compressed_size % 32)) & 0x1F
            if compressed_size + compressed_pad < header.uncompressed_size:
                header.compressed_size = compressed_size
                header.buffer_size += 0x120
            else:
                data = merged_and_padded_group

            compressed_blocks.append(Container(
                header=header,
                data=data,
            ))
            current_group = ListContainer()
            current_group_size = 0

        for i, section in enumerate(data_sections):
            all_garbage = [cat for cat, start in category_starts.items() if i >= start]
            cat_label = all_garbage[-1]

            start_new, reason = _start_new_group(
                current_group_size, len(section),
                previous_label, cat_label
            )
            if start_new:
                add_group(reason)

            current_group.append(section)
            current_group_size += len(section)

            previous_label = cat_label

        add_group("Final group.")
        return compressed_blocks

    def _build(self, obj: Container, stream, context, path):
        mrea_header = Container()

        # Encode each category
        sections = Container()
        for category, values in obj.sections.items():
            sections[category] = _encode_category(values, _CATEGORY_ENCODINGS.get(category, GreedyBytes),
                                                  context, f"{path} -> {category}")

        # Combine all sections into the data sections array
        data_sections = ListContainer()

        for category in _all_categories:
            if category in sections:
                mrea_header[category] = len(data_sections)
                data_sections.extend(sections[category])
            else:
                mrea_header[category] = None

        # Compress the data sections
        if int(obj.version) >= MREAVersion.Echoes.value:
            compressed_blocks = self._encode_compressed_blocks(
                data_sections,
                mrea_header,
                context,
                path
            )
            mrea_header.compressed_block_count = len(compressed_blocks)
        else:
            compressed_blocks = None
            raise RuntimeError("Not implemented yet")

        mrea_header.version = obj.version
        mrea_header.area_transform = obj.area_transform
        mrea_header.world_model_count = obj.world_model_count
        mrea_header.script_layer_count = len(obj.sections.script_layers_section)
        mrea_header.data_section_count = len(data_sections)

        MREAHeader_v2._build(mrea_header, stream, context, path)
        Array(mrea_header.data_section_count, Int32ub)._build(
            [len(section) for section in data_sections],
            stream, context, path,
        )
        if compressed_blocks is not None:
            Aligned(32, Array(mrea_header.compressed_block_count, CompressedBlockHeader))._build(
                [block.header for block in compressed_blocks],
                stream, context, path,
            )
            for compressed_block in compressed_blocks:
                block_header = compressed_block.header
                if block_header.compressed_size:
                    subcon = PrefixedWithPaddingBefore(Computed(block_header.compressed_size), GreedyBytes)
                else:
                    subcon = DataSection(GreedyBytes, size=lambda: Computed(block_header.uncompressed_size))
                subcon._build(compressed_block.data, stream, context, path)
        else:
            # TODO
            pass


class Mrea(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "MREA"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return MREAConstruct()

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        raise NotImplementedError()

    @property
    def script_layers(self) -> Iterator[ScriptLayerHelper]:
        for section in self._raw.sections.script_layers_section:
            yield ScriptLayerHelper(section["data"], self.target_game)

    def get_instance(self, instance_id: int) -> Optional[ScriptInstanceHelper]:
        for layer in self.script_layers:
            if (instance := layer.get_instance(instance_id)) is not None:
                return instance

    def get_instance_by_name(self, name: str) -> Optional[ScriptInstanceHelper]:
        for layer in self.script_layers:
            if (instance := layer.get_instance_by_name(name)) is not None:
                return instance
