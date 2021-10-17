"""
Wiki: https://wiki.axiodl.com/w/MREA_(Metroid_Prime_2)
"""
import hashlib
import io
from enum import IntEnum
from typing import Iterator

from construct.core import (
    Adapter,
    Aligned,
    Array,
    Computed,
    Const,
    Container,
    Enum,
    FixedSized,
    GreedyBytes,
    If,
    IfThenElse,
    Int8ub,
    Int32ub,
    ListContainer,
    PrefixedArray,
    Rebuild,
    Sequence,
    Struct,
    Tell,
    len_,
    this,
)

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC, Transform4f
from retro_data_structures.compression import LZOCompressedBlock
from retro_data_structures.construct_extensions.alignment import PrefixedWithPaddingBefore
from retro_data_structures.construct_extensions.version import BeforeVersion, WithVersion, WithVersionElse
from retro_data_structures.data_section import DataSection, DataSectionSizes, GetDataSectionId, GetDataSectionSize
from retro_data_structures.formats.area_collision import AreaCollision
from retro_data_structures.formats.arot import AROT
from retro_data_structures.formats.lights import Lights
from retro_data_structures.formats.script_layer import SCGN, SCLY, ScriptLayerHelper
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


from retro_data_structures.formats.world_geometry import GeometryCodec


def DataSectionGroup(decompress):
    return Struct(
        "header" / Computed(lambda this: this._.headers[this._index]),
        "address" / Tell,
        "decompressed" / Computed(decompress),
        "data"
        / IfThenElse(
            this.header.compressed_size > 0,
            PrefixedWithPaddingBefore(
                Computed(this.header.compressed_size),
                IfThenElse(decompress, LZOCompressedBlock(this.header.uncompressed_size), GreedyBytes),
            ),
            DataSection(GreedyBytes, size=lambda: Computed(this.header.uncompressed_size)),
        ),
    )


class DataSectionGroupAdapter(Adapter):
    def _decode(self, group, context, path):
        sections = []
        offset = 0

        for i in range(group.header.section_count):
            section_id = GetDataSectionId(context)
            section_size = GetDataSectionSize(context)

            data = b""
            if group.decompressed:
                data = group.data[offset : offset + section_size]
            elif i == 0:
                data = group.data

            sections.append(
                Container(
                    data=data,
                    hash=hashlib.sha256(data).hexdigest(),
                    size=section_size,
                    id=section_id,
                    decompressed=group.decompressed,
                )
            )

            offset += section_size

        return ListContainer(sections)

    def _encode(self, group, context, path):
        return {"data": b"".join([section["data"] for section in group])}


class UncompressedDataSections(Adapter):
    def __init__(self, parse_block_func):
        super().__init__(
            Array(
                this.header.data_section_count,
                Struct(
                    "data"
                    / Aligned(
                        32,
                        FixedSized(lambda this: this._root.header.data_section_sizes.value[this._index], GreedyBytes),
                    ),
                    "decompressed" / Computed(parse_block_func),
                ),
            )
        )
        self.parse_block_func = parse_block_func

    def _decode(self, sections, context, path):
        decoded = []
        for i in range(len(sections)):
            section = sections[i]
            decoded.append(
                Container(
                    data=section["data"],
                    hash=hashlib.sha256(section["data"]).hexdigest(),
                    size=len(section["data"]),
                    id=i,
                    decompressed=section["decompressed"],
                )
            )
        return [ListContainer(decoded)]

    def _encode(self, sections, context, path):
        return [{"data": section["data"]} for category in sections.values() for section in category]


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

            if section["size"] > 0 and section["decompressed"]:
                decoded = subcon._parse(io.BytesIO(section["data"]), context, path)
                category[i]["data"] = decoded
        return category

    def _encode_category(self, category, subcon, context, path):
        for i in range(len(category)):
            section = category[i]

            if section["size"] > 0 and section["decompressed"]:
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

        GeometryCodec(sections["geometry_section"], context, path, encode=False, codec=self._decode_category)
        for category, subcon in self._category_encodings().items():
            if category in sections or hasattr(sections, category):
                self._decode_category(sections[category], subcon, context, path)

        return sections

    def _encode(self, sections, context, path):
        GeometryCodec(sections["geometry_section"], context, path, encode=True, codec=self._encode_category)
        for category, subcon in self._category_encodings().items():
            if category in sections or hasattr(sections, category):
                self._encode_category(sections[category], subcon, context, path)

        return sections


class CompressedBlocksAdapter(SectionCategoryAdapter):
    def _encode(self, sections, context, path):
        sections = super()._encode(sections, context, path)

        groups = []

        current_group_size = 0
        current_group = []
        previous_label = ""

        def add_group(r):
            nonlocal current_group, current_group_size
            # print(f"Group complete! {r} Group size: {current_group_size}")
            groups.append(current_group)
            current_group = []
            current_group_size = 0

        for cat_label, cat_sections in sorted(sections.items(), key=lambda item: item[1][0]["id"]):
            for section in cat_sections:

                def start_new_group():
                    if current_group_size == 0:
                        return (False, "")
                    if current_group_size + section["size"] > 0x20000:
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
                current_group_size += section["size"]

            previous_label = cat_label

        add_group("Final group.")

        return groups


def CompressedBlocks(parse_block_func):
    return Aligned(
        32, Array(this.header.compressed_block_count, DataSectionGroupAdapter(DataSectionGroup(parse_block_func)))
    )


def _previous_sections_group(this):
    return sum([header.section_count for header in this._root.headers[0 : this._index]])


def _previous_sections_uncompressed(this):
    return this._index


def _previous_sections(this):
    if int(this._root.version) <= MREAVersion.Prime:
        return _previous_sections_uncompressed(this)
    return _previous_sections_group(this)


def IncludeCategories(*categories):
    def find_next_category(category, this):
        root = this._root
        cat_index = root.header[category]
        next_index = root.header.data_section_count

        for category in root.header.categories:
            index = root.header[category]
            if cat_index < index < next_index:
                next_index = index

        return next_index

    def _inclusion(this):
        root = this._root
        previous_sections = _previous_sections(this)

        for category in categories:
            if root.header[category] != None and root.header[category] <= previous_sections < find_next_category(
                category, this
            ):
                return True
        return False

    return _inclusion


def IncludeScriptLayers(this):
    """Parses only SCLY and SCGN sections."""
    return IncludeCategories("script_layers_section", "generated_script_objects_section")(this)


def IncludeAssetIdLayers(this):
    """Parses only sections which hold single Asset IDs."""
    return IncludeCategories("path_section", "portal_area_section", "static_geometry_map_section")(this)


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
        "compressed_block_count" / WithVersion(MREAVersion.Echoes, Aligned(16, Rebuild(Int32ub, len_(this._.headers)))),
        # Array containing the size of each data section in the file. Every size is always a multiple of 32.
        "data_section_sizes"
        / Aligned(
            32,
            DataSectionSizes(
                this._.data_section_count,
                True,
                lambda this: sorted(
                    [x for l in this._root.sections.values() for x in l], key=lambda section: section["id"]
                )[this._index]["size"],
            ),
        ),
        "categories" / Computed(_used_categories),
    )


def _MREA(parse_block_func=IncludeScriptLayers):
    fields = [
        "header" / Aligned(32, MREAHeader()),
        "_current_section" / Computed(0),
        "version" / Computed(this.header.version),
        # Sections. Each group is compressed separately
        "headers"
        / WithVersion(
            MREAVersion.Echoes,
            Aligned(
                32,
                Array(
                    this.header.compressed_block_count,
                    Struct(
                        "address" / Tell,
                        # TODO: all of these should be rebuilt
                        "buffer_size" / Int32ub,
                        "uncompressed_size" / Int32ub,
                        "compressed_size" / Int32ub,
                        "section_count" / Int32ub,
                    ),
                ),
            ),
        ),
        # FIXME: recompression doesn't match with original when building
        "sections"
        / WithVersionElse(
            MREAVersion.Echoes,
            CompressedBlocksAdapter(CompressedBlocks(parse_block_func)),
            SectionCategoryAdapter(UncompressedDataSections(parse_block_func)),
        ),
    ]

    return Struct(*fields)


MREA = _MREA()


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
