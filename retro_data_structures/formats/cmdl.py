import construct
from construct import (Struct, Int32ub, Const, Array, Aligned, PrefixedArray, If, Int16ub, Byte, Float32b,
                       GreedyRange, IfThenElse, Float16b, Bytes, Switch, Int8ub, Rebuild, Pointer, Tell, Seek,
                       FocusedSeq)

from retro_data_structures.common_types import AABox, AssetId32, Vector3, Color4f, Vector2f
from retro_data_structures.construct_extensions import AlignTo, WithVersion, Skip
from retro_data_structures.data_section import DataSectionSizes, DataSection
from retro_data_structures.game_check import Game

TEVStage = Struct(
    color_input_flags=Int32ub,
    alpha_input_flags=Int32ub,
    color_combine_flags=Int32ub,
    alpha_combine_flags=Int32ub,
    padding=Byte,
    konst_alpha_input=Byte,
    konst_color_input=Byte,
    rasterized_color_input=Byte,
)

TEVInput = Struct(
    padding=Int16ub,
    texture_tev_input=Byte,
    tex_coord_tev_input=Byte,
)

param_count_per_uv_animtion_type = {
    0: 0,
    1: 0,
    2: 4,
    3: 2,
    4: 4,
    5: 4,
    6: 0,
    7: 2,
    8: 9,
}

UVAnimation = Struct(
    animation_type=Int32ub,
    parameters=Array(lambda this: param_count_per_uv_animtion_type[this.animation_type], Float32b),
)

Material = Struct(
    flags=Int32ub,
    texture_indices=PrefixedArray(Int32ub, Int32ub),
    vertex_attribute_flags=Int32ub,
    unk_1=WithVersion(4, Int32ub),
    unk_2=WithVersion(4, Int32ub),
    group_index=Int32ub,
    konst_colors=If(construct.this.flags & 0x8, PrefixedArray(Int32ub, Int32ub)),
    blend_destination_factor=Int16ub,
    blend_source_factor=Int16ub,
    reflection_indirect_texture_slot_index=If(construct.this.flags & 0x400, Int32ub),
    color_channel_flags=PrefixedArray(Int32ub, Int32ub),

    tev_stages=PrefixedArray(Int32ub, TEVStage),
    tev_inputs=Array(construct.len_(construct.this.tev_stages), TEVInput),

    texgen_flags=PrefixedArray(Int32ub, Int32ub),

    material_animations_section_size=Int32ub,
    uv_animations=PrefixedArray(Int32ub, UVAnimation),
)

MaterialSet = Struct(
    texture_file_ids=PrefixedArray(Int32ub, AssetId32),
    _material_count=Rebuild(Int32ub, construct.len_(construct.this.materials)),
    _material_end_offsets_address=Tell,
    _material_end_offsets=Seek(construct.this["_material_count"] * Int32ub.length, 1),
    _materials_start=Tell,
    materials=Array(construct.this["_material_count"], FocusedSeq(
        "material",
        material=Material,
        _end=Tell,
        update_end_offset=Pointer(
            lambda ctx: ctx["_"]["_material_end_offsets_address"] + Int32ub.length * ctx["_index"],
            Rebuild(Int32ub, lambda ctx: ctx["_end"] - ctx["_"]["_materials_start"])
        ),
    )),
)


def get_material(context):
    surface = context
    while 'header' not in surface:
        surface = surface['_']
    return context._root.material_sets[0].materials[surface.header.material_index]


def VertexAttrib(flag):
    if not flag:
        raise ValueError("Invalid flag!")

    shift = 0
    while (flag >> shift) & 1 == 0:
        shift += 1

    return Switch(
        lambda this: (get_material(this).vertex_attribute_flags & flag) >> shift,
        {
            3: Int16ub,
            2: Int8ub,
            1: Int8ub,
        }
    )


Surface = Struct(
    header=Aligned(32, Struct(
        center_point=Vector3,
        material_index=Int32ub,
        mantissa=Int16ub,
        _display_list_size_address=Tell,
        _display_list_size=Rebuild(Int16ub, lambda ctx: 0),
        parent_model_pointer_storage=Int32ub,
        next_surface_pointer_storage=Int32ub,
        _extra_data_size=Rebuild(Int32ub, construct.len_(construct.this.extra_data)),
        surface_normal=Vector3,
        unk_1=WithVersion(4, Int16ub),
        unk_2=WithVersion(4, Int16ub),
        extra_data=Bytes(construct.this["_extra_data_size"]),
    )),
    _primitives_address=Tell,
    primitives=GreedyRange(Struct(
        type=Byte,
        vertices=PrefixedArray(Int16ub, Struct(
            matrix=Struct(
                position=VertexAttrib(0x01 << 24),
                tex=Struct(*[
                    str(i) / VertexAttrib(flag << 24)
                    for i, flag in enumerate([0x02, 0x04, 0x08, 0x10,
                                              0x20, 0x40, 0x80])
                ]),
            ),
            position=VertexAttrib(0x03),
            normal=VertexAttrib(0x0c),
            color_0=VertexAttrib(0x30),
            color_1=VertexAttrib(0xc0),
            tex=Struct(*[
                str(i) / VertexAttrib(flag)
                for i, flag in enumerate([0x00000300, 0x00000C00, 0x00003000, 0x0000C000,
                                          0x00030000, 0x000C0000, 0x00300000, 0x00C00000])
            ]),
        ))
    )),
    _size=Tell,
    _update_display_size=Pointer(
        construct.this.header["_display_list_size_address"],
        Rebuild(Int16ub, lambda ctx: ((ctx["_size"] - ctx["_primitives_address"]) + 31) & ~31),
    ),
)

# 0x2 = Prime 1
# 0x4 = Prime 2
# 0x5 = Prime 3
CMDL = Struct(
    _magic=Const(0xDEADBABE, Int32ub),
    version=Int32ub,
    flags=Int32ub,
    aabox=AABox,
    _data_section_count=Rebuild(
        Int32ub,
        lambda context: (len(context.material_sets)
                         + sum(1 for k, v in context.attrib_arrays.items()
                               if not k.startswith("_") and v is not None)
                         + 1
                         + len(context.surfaces)),
    ),
    _material_set_count=Rebuild(Int32ub, construct.len_(construct.this.material_sets)),
    _data_section_sizes=DataSectionSizes(construct.this._root._data_section_count),
    _=AlignTo(32),
    _current_section=construct.Computed(lambda this: 0),
    material_sets=Array(construct.this._material_set_count, DataSection(MaterialSet)),
    attrib_arrays=Struct(
        positions=DataSection(GreedyRange(Vector3)),
        normals=DataSection(
            GreedyRange(IfThenElse(
                construct.this._root.flags & 0x2,
                construct.Error,  # TODO: read the half-vectors
                Vector3,
            )),
        ),
        # TODO: none of Retro's games actually have data here, so this might be the wrong type!
        colors=DataSection(GreedyRange(Color4f)),
        uvs=DataSection(GreedyRange(Vector2f)),
        lightmap_uvs=If(
            construct.this._root.flags & 0x4,
            DataSection(GreedyRange(Array(2, Float16b))),
        ),
    ),
    _surface_header_address=Tell,
    _surface_header=DataSection(Struct(
        num_surfaces=Rebuild(Int32ub, construct.len_(construct.this["_"].surfaces)),
        end_offsets=Skip(construct.this.num_surfaces, Int32ub),
    )),
    _surfaces_start=Tell,
    surfaces=Array(
        construct.this["_surface_header"].num_surfaces,
        FocusedSeq(
            "surface",
            surface=DataSection(Surface),
            end=Tell,
            update_end_offset=Pointer(
                # One extra Int32ub for the num_surfaces
                lambda ctx: ctx["_"]["_surface_header_address"] + Int32ub.length + Int32ub.length * ctx["_index"],
                Rebuild(Int32ub, lambda ctx: ctx.end - ctx["_"]["_surfaces_start"])),
        ),
    ),
)


def dependencies_for(obj, target_game: Game):
    for material_set in obj.material_sets:
        for file_id in material_set.texture_file_ids:
            yield "TXTR", file_id
