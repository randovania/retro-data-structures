from construct.core import (
    Array,
    Const,
    Float16b,
    GreedyBytes,
    GreedyRange,
    Int16sb,
    Int16ub,
    Int32ub,
    PrefixedArray,
    Struct, Construct,
)

from retro_data_structures.common_types import AABox, Color4f, Transform4f, Vector2f, Vector3
from retro_data_structures.construct_extensions.version import get_version
from retro_data_structures.formats.arot import AROT
from retro_data_structures.formats.cmdl import MaterialSet, Normal, Surface
from retro_data_structures.formats.mrea import MREAVersion

WorldModelHeader = Struct("visor_flags" / Int32ub, "transform" / Transform4f, "bounding_box" / AABox)  # TODO: FlagEnum

SurfaceGroupBounds = Struct(
    "bounding_box" / AABox,
    "world_model_index" / Int16ub,
    "surface_group_index" / Int16ub,
    "unk1" / Int16sb,  # IfThenElse(this._index == 0, Const(1, Int16sb), Const(-1, Int16sb)),
    "unk2" / Int16sb,  # IfThenElse(this._index == 0, Const(-1, Int16sb), Const(this.surface_group_index+1, Int16sb))
)


def SurfaceGroupIds(surface_count):
    return PrefixedArray(
        Const(surface_count, Int16ub), Struct("model_relative_id" / Int16ub, "area_relative_id" / Int16ub)
    )


def SurfaceLookupTable(surface_group_count, surface_count):
    return Struct(
        "surface_group_count" / Const(surface_group_count, Int16ub),
        "lookup_table_index_array" / Array(surface_group_count, Int16ub),  # TODO: rebuild
        "surface_lookup_table" / Array(surface_count, Int16ub),
    )


def GeometryCodec(category, context, path, encode, codec):
    if category[0]["size"] <= 0 or category[0]["decompressed"] == False:
        return category

    current_section = 0

    def subcategory_codec(identifier, subcon: Construct = GreedyBytes, size=1):
        nonlocal current_section

        subcategory = category[current_section : current_section + size]
        codec(subcategory, subcon, context, path)

        for section in subcategory:
            section["label"] = identifier
        current_section += size

    subcategory_codec("material_set", MaterialSet)

    for i in range(context._root.header.world_model_count):
        subcategory_codec("header", WorldModelHeader)

        # TODO: strip padding
        subcategory_codec("positions", GreedyRange(Vector3))
        subcategory_codec("normals", GreedyRange(Normal))
        subcategory_codec("colors", GreedyRange(Color4f))
        subcategory_codec("uvs", GreedyRange(Vector2f))
        subcategory_codec("lightmap_uvs", GreedyRange(Array(2, Float16b)))

        if encode:
            surface_count = len(category[current_section]["data"])
        subcategory_codec("surface_offsets", PrefixedArray(Int32ub, Int32ub))
        if not encode:
            surface_count = len(category[current_section - 1]["data"])

        subcategory_codec("surface", Surface, surface_count)

        if get_version(context, MREAVersion) <= MREAVersion.Prime:
            continue

        if encode:
            surface_group_count = len(category[current_section]["data"])
        subcategory_codec("surface_group_ids", SurfaceGroupIds(surface_count))
        if not encode:
            surface_group_count = len(category[current_section - 1]["data"])

        subcategory_codec("surface_lookup_table", SurfaceLookupTable(surface_group_count, surface_count))

    if get_version(context, MREAVersion) >= MREAVersion.Echoes:
        subcategory_codec("area_octree", AROT)
        subcategory_codec("surface_group_bounds", PrefixedArray(Int32ub, SurfaceGroupBounds))

    return category
