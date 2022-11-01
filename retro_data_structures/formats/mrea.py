"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import copy
import io
import typing
from enum import IntEnum
from typing import Iterator, Optional

import construct
from construct import Struct, PrefixedArray, Int32ub, If, Aligned
from construct.core import (
    Array,
    Computed,
    Const,
    Enum,
    FixedSized,
    GreedyBytes,
    Int8ub,
)
from construct.lib.containers import Container, ListContainer

from retro_data_structures import game_check
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.common_types import FourCC, Transform4f
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.construct_extensions.alignment import PrefixedWithPaddingBefore
from retro_data_structures.construct_extensions.version import BeforeVersion, WithVersion
from retro_data_structures.data_section import DataSection
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

MREAHeader = Aligned(32, Struct(
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
            if isinstance(section, bytes) or subcon is None:
                this_subcon = GreedyBytes
            else:
                this_subcon = subcon

            Aligned(32, this_subcon)._build(section, stream, context, path)
            data = stream.getvalue()
        else:
            data = b""

        result.append(data)

    return result


class MREAConstruct(construct.Construct):
    def _aligned_parse(self, conn: construct.Construct, stream, context, path):
        return Aligned(32, conn)._parsereport(stream, context, path)

    def _decode_compressed_blocks(self, mrea_header, data_section_sizes, stream, context, path) -> typing.List[bytes]:
        compressed_block_headers = self._aligned_parse(
            Array(mrea_header.compressed_block_count, CompressedBlockHeader),
            stream, context, path
        )

        # Read compressed blocks from stream
        compressed_blocks = construct.ListContainer(
            self._aligned_parse(
                FixedSized(_get_compressed_block_size(header), GreedyBytes),
                stream, context, path,
            )
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
        mrea_header = MREAHeader._parsereport(stream, context, path)
        data_section_sizes = self._aligned_parse(Array(mrea_header.data_section_count, Int32ub), stream, context, path)

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

        return Container(
            version=mrea_header.version,
            area_transform=mrea_header.area_transform,
            world_model_count=mrea_header.world_model_count,
            raw_sections=sections,
            sections=construct.Container(),
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

        raw_sections = copy.copy(obj.raw_sections)

        # Encode each category
        for category, values in obj.sections.items():
            raw_sections[category] = _encode_category(values, _CATEGORY_ENCODINGS.get(category),
                                                      context, f"{path} -> {category}")

        # Combine all sections into the data sections array
        data_sections = ListContainer()

        for category in _all_categories:
            if category in raw_sections:
                mrea_header[category] = len(data_sections)
                data_sections.extend(raw_sections[category])
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
        mrea_header.script_layer_count = len(obj.raw_sections.script_layers_section)
        mrea_header.data_section_count = len(data_sections)

        MREAHeader._build(mrea_header, stream, context, path)
        Aligned(32, Array(mrea_header.data_section_count, Int32ub))._build(
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


MREA = MREAConstruct()


class Mrea(BaseResource):
    _script_layer_helpers: Optional[typing.Dict[int, ScriptLayerHelper]] = None

    @classmethod
    def resource_type(cls) -> AssetType:
        return "MREA"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return MREA

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        raise NotImplementedError()

    def _ensure_decoded_section(self, section_name: str, lazy_load: bool = False):
        if section_name not in self._raw.sections:
            context = Container(target_game=self.target_game)
            context._parsing = True
            context._building = False
            context._sizing = False
            context._params = context

            self._raw.sections[section_name] = _decode_category(
                self._raw.raw_sections[section_name],
                GreedyBytes if lazy_load else _CATEGORY_ENCODINGS[section_name],
                context, "",
            )

    def build(self) -> bytes:
        for i, section in (self._script_layer_helpers or {}).items():
            if section.is_modified():
                self._raw.sections.script_layers_section[i] = section._raw
        return super().build()

    @property
    def script_layers(self) -> Iterator[ScriptLayerHelper]:
        self._ensure_decoded_section("script_layers_section", lazy_load=self.target_game != Game.PRIME)

        if self.target_game == Game.PRIME:
            section = self._raw.sections.script_layers_section[0]
            for i, layer in enumerate(section.layers):
                yield ScriptLayerHelper(layer, i, self.target_game)
        else:
            if self._script_layer_helpers is None:
                self._script_layer_helpers = {}

            for i, section in enumerate(self._raw.sections.script_layers_section):
                if i not in self._script_layer_helpers:
                    self._script_layer_helpers[i] = ScriptLayerHelper(
                        _CATEGORY_ENCODINGS["script_layers_section"].parse(
                            section, target_game=self.target_game
                        ),
                        i,
                        self.target_game
                    )

            yield from self._script_layer_helpers.values()

    def get_instance(self, instance_id: int) -> Optional[ScriptInstanceHelper]:
        for layer in self.script_layers:
            if (instance := layer.get_instance(instance_id)) is not None:
                return instance

    def get_instance_by_name(self, name: str) -> ScriptInstanceHelper:
        for layer in self.script_layers:
            if (instance := layer.get_instance_by_name(name, raise_if_missing=False)) is not None:
                return instance
        raise KeyError(name)
