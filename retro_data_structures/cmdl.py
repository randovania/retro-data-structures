import construct
from construct import Struct, Int32ub, Const, Array, Aligned, PrefixedArray, If, Int16ub, Byte, Float32b, \
    FixedSized, GreedyRange, IfThenElse, Float16b, Bytes, Switch, Int8ub

from retro_data_structures.common_types import AABox, AssetId32, Vector3, Color4f, Vector2f
from retro_data_structures.construct_extensions import AlignTo, WithVersion

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

    tev_stage_count=Int32ub,
    tev_stages=Array(construct.this.tev_stage_count, TEVStage),
    tev_inputs=Array(construct.this.tev_stage_count, TEVInput),

    texgen_flags=PrefixedArray(Int32ub, Int32ub),

    material_animations_section_size=Int32ub,
    uv_animations=PrefixedArray(Int32ub, UVAnimation),
)

MaterialSet = Struct(
    texture_file_ids=PrefixedArray(Int32ub, AssetId32),
    material_count=Int32ub,
    material_end_offsets=Array(construct.this.material_count, Int32ub),
    materials=Array(construct.this.material_count, Material),
)


def DataSection(subcon):
    def get_section_length(context):
        root = context["_root"]
        index = root["_current_section"]
        root["_current_section"] += 1
        return root.data_section_sizes[index]

    return FixedSized(get_section_length, subcon)


def get_material(context):
    surface = context
    while 'header' not in surface:
        surface = surface['_']
    return context._root.material_sets[0].materials[surface.header.material_index]


def VertexAttrib(flag):
    # TODO: In Echoes, the game supports having 8-bit indices if the flag value is 2 instead of 3.
    # But that isn't used by the game, so it's fine

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
        display_list_size=Int16ub,
        parent_model_pointer_storage=Int32ub,
        next_surface_pointer_storage=Int32ub,
        extra_data_size=Int32ub,
        surface_normal=Vector3,
        unk_1=WithVersion(4, Int16ub),
        unk_2=WithVersion(4, Int16ub),
        extra_data=Bytes(construct.this.extra_data_size),
    )),
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
)

# 0x2 = Prime 1
# 0x4 = Prime 2
# 0x5 = Prime 3
CMDL = Struct(
    magic=Const(0xDEADBABE, Int32ub),
    version=Int32ub,
    flags=Int32ub,
    aabox=AABox,
    data_section_count=Int32ub,
    material_set_count=Int32ub,
    data_section_sizes=Array(construct.this.data_section_count, Int32ub),
    _=AlignTo(32),
    _current_section=construct.Computed(lambda this: 0),
    _first_section=construct.Tell,
    material_sets=Array(construct.this.material_set_count, DataSection(MaterialSet)),
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
    surface_offsets=DataSection(PrefixedArray(Int32ub, Int32ub)),
    surfaces=Array(
        construct.len_(construct.this.surface_offsets),
        DataSection(Surface),
    ),
)


def main():
    import sys
    data = CMDL.parse_file(sys.argv[1])
    # print(data)

    new_binary = CMDL.build(data)
    from pathlib import Path
    old_binary = Path(sys.argv[1]).read_bytes()
    if new_binary == old_binary:
        print("THEY MATCH!")


if __name__ == '__main__':
    main()
