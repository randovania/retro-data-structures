"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import hashlib
import io
from enum import IntEnum
from typing import Iterator, Optional

from construct.core import (
    Adapter,
    Aligned,
    AlignedStruct,
    Array,
    Computed,
    Const,
    Enum,
    FixedSized,
    GreedyBytes,
    If,
    Int8ub,
    Int32ub,
    Pass,
    Pointer,
    PrefixedArray,
    Rebuild,
    Sequence,
    Struct,
    Tell,
    len_,
    this,
)
from construct.lib.containers import Container, ListContainer

from retro_data_structures import game_check
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
from retro_data_structures.game_check import AssetIdCorrect, Game


class MREAVersion(IntEnum):
    PrimeKioskDemo = 0xC
    Prime = 0xF
    EchoesDemo = 0x15
    Echoes = 0x19
    CorruptionE3Prototype = 0x1D
    Corruption = 0x1E
    DonkeyKongCountryReturns = 0x20


class DataSectionGroupAdapter(Adapter):
    def __init__(self, subcon, header):
        super().__init__(subcon)
        self.header = header

    def _decode(self, group, context, path):
        sections = []
        offset = 0

        for i in range(self.header.data_section_count):
            section_id = GetDataSectionId(context)
            section_size = GetDataSectionSize(context)

            data = group[offset: offset + section_size]

            sections.append(
                Container(
                    data=data,
                    hash=hashlib.sha256(data).hexdigest(),
                    size=section_size,
                    id=section_id,
                )
            )

            offset += section_size

        return ListContainer(sections)

    def _encode(self, group, context, path):
        return b"".join(
            [section["data"].ljust(len(section["data"]) + (-len(section["data"]) % 32), b"\x00") for section in group])


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
        for i in range(len(sections)):
            section = sections[i]
            decoded.append(
                Container(
                    data=section,
                    hash=hashlib.sha256(section).hexdigest(),
                    size=len(section),
                    id=i,
                )
            )
        return [ListContainer(decoded)]

    def _encode(self, sections, context, path):
        return [section["data"] for category in sections.values() for section in category]


_all_categories = [
    "geometry_section",
    "script_layers_section",
    "generated_script_objects_section",
    "collision_section",
    "unknown_section_1",
    "lights_section",
    "visibility_tree_section",
    "path_section",
    "area_octree_section",
    "unknown_section_2",
    "portal_area_section",
    "static_geometry_map_section",
]


class SectionCategoryAdapter(Adapter):
    def _decode_category(self, category, subcon, context, path):
        for i in range(len(category)):
            section = category[i]
            if section["size"] > 0:
                decoded = subcon._parse(io.BytesIO(section["data"]), context, path)
                category[i]["data"] = decoded
        return category

    def _encode_category(self, category, subcon, context, path):
        for i in range(len(category)):
            section = category[i]
            if section["size"] > 0:
                encoded = io.BytesIO()
                subcon._build(section["data"], encoded, context, path)
                category[i]["data"] = encoded.getvalue()
        return category

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
                "magic" / If(game_check.is_prime3, Const("LLTE", FourCC)), "data" / Const(1, Int32ub)
            ),
            "unknown_section_2": Sequence(
                Const(0, Int32ub),
                PrefixedArray(Int32ub, Const(0xFF, Int8ub)),  # TODO: rebuild according to surface group count
            ),
        }

    def _decode(self, section_groups, context, path):
        _sections = []

        for group in section_groups:
            _sections.extend(group)

        def cat(label):
            return {"label": label, "value": context.header[label] if isinstance(context.header[label], int) else -1}

        _categories = sorted(
            list(filter(lambda item: item["value"] != -1, list(map(lambda label: cat(label), _all_categories)))),
            key=lambda cat: cat["value"],
        )

        sections = Container()
        for i in range(len(_categories)):
            c = _categories[i]
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

    def _encode(self, sections, context, path):
        # FIXME: World Geometry is not building correctly
        # GeometryCodec(sections["geometry_section"], context, path, encode=True, codec=self._encode_category)
        for category, subcon in self._category_encodings().items():
            if category in sections or hasattr(sections, category):
                self._encode_category(sections[category], subcon, context, path)

        return sections


class CompressedBlocksAdapter(SectionCategoryAdapter):
    def __init__(self):
        def get_size(ctx):
            header = ctx._.headers[ctx._index]
            if not header.compressed_size:
                return header.uncompressed_size
            return header.compressed_size + (-header.compressed_size % 32)

        super().__init__(AlignedStruct(32,
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
        groups = section_groups.groups
        for i in range(len(groups)):
            header = section_groups.headers[i]
            subcon = self._get_subcon(header.compressed_size, header.uncompressed_size, context)
            groups[i] = DataSectionGroupAdapter(subcon, header)._parsereport(io.BytesIO(groups[i]), context, path)

        return super()._decode(groups, context, path)

    def _start_new_group(self, group_size, section_size, curr_label, prev_label):
        if group_size == 0:
            return (False, "")
        if group_size + section_size > 0x20000:
            return (True, "Next section too big.")
        if curr_label == "script_layers_section":
            return (True, "New SCLY section.")
        elif prev_label == "script_layers_section":
            return (True, "Previous SCLY completed.")
        if curr_label == "generated_script_objects_section":
            return (True, "New SCGN section.")
        elif prev_label == "generated_script_objects_section":
            return (True, "Previous SCGN completed.")
        return (False, "")

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
            current_group = []
            current_group_size = 0

        for cat_label, cat_sections in sorted(sections.items(), key=lambda item: item[1][0]["id"]):
            for section in cat_sections:
                start_new, reason = self._start_new_group(
                    current_group_size, section["size"],
                    previous_label, cat_label
                )
                if start_new:
                    add_group(reason)

                current_group.append(section)
                current_group_size += section["size"]

            previous_label = cat_label
        add_group("Final group.")

        for block in compressed_blocks:
            group = block.group
            header = block.header

            group = DataSectionGroupAdapter(Pass, header)._encode(group, context, path)

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

        return Container(
            headers=[block.header for block in compressed_blocks],
            groups=[block.group for block in compressed_blocks]
        )


def _used_categories(this):
    return list(filter(lambda item: this[item], _all_categories))


def MREAHeader():
    def get_section_id(category):
        return lambda this: this._.sections[category][0]["id"]

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
        "script_layer_count"
        / WithVersion(MREAVersion.Echoes, Rebuild(Int32ub, len_(this._.sections.script_layers_section))),
        # Number of data sections in the file.
        "data_section_count" / Rebuild(Int32ub, lambda this: sum(map(lambda cat: len(cat), this._.sections.values()))),
        # Section index for world geometry data. Always 0; starts on materials.
        "geometry_section" / Rebuild(Int32ub, get_section_id("geometry_section")),
        # Section index for script layer data.
        "script_layers_section" / Rebuild(Int32ub, get_section_id("script_layers_section")),
        # Section index for generated script object data.
        "generated_script_objects_section"
        / WithVersion(MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("generated_script_objects_section"))),
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
        "area_octree_section"
        / BeforeVersion(MREAVersion.EchoesDemo, Rebuild(Int32ub, get_section_id("area_octree_section"))),
        # Section index for second unknown section.
        "unknown_section_2" / WithVersion(MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("unknown_section_2"))),
        # Section index for portal area data.
        "portal_area_section"
        / WithVersion(MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("portal_area_section"))),
        # Section index for static geometry map data.
        "static_geometry_map_section"
        / WithVersion(MREAVersion.Echoes, Rebuild(Int32ub, get_section_id("static_geometry_map_section"))),
        # Number of compressed data blocks in the file.
        "compressed_block_count_addr" / WithVersion(MREAVersion.Echoes, Tell),
        WithVersion(MREAVersion.Echoes, Skip(1, Int32ub)),
        "categories" / Computed(_used_categories),
    )


MREA = AlignedStruct(32,
                     "_current_section" / Computed(0),

                     "header" / MREAHeader(),
                     "version" / Computed(this.header.version),

                     # Array containing the size of each data section in the file. Every size is always a multiple of 32.
                     "data_section_sizes" / DataSectionSizes(
                         this._.header.data_section_count,
                         True,
                         lambda this: sorted(
                             [x for l in this._root.sections.values() for x in l], key=lambda section: section["id"]
                         )[this._index]["size"],
                     ),

                     "sections"
                     / WithVersionElse(
                         MREAVersion.Echoes,
                         CompressedBlocksAdapter(),
                         SectionCategoryAdapter(UncompressedDataSections())
                     ),
                     )


class Mrea:
    _raw: Container
    target_game: Game

    def __init__(self, raw: Container, target_game: Game):
        self._raw = raw
        self.target_game = target_game

    @classmethod
    def parse(cls, data: bytes, target_game: Game) -> "Mrea":
        return cls(MREA.parse(data, target_game=target_game), target_game)

    def build(self) -> bytes:
        return MREA.build(self._raw, target_game=self.target_game)

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
