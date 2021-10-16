import math

from construct import Aligned, Array, Const, Int32ub, Struct, this, FlagsEnum, Int16ub
from construct.core import Computed, If

from retro_data_structures.common_types import AABox, FourCC

# TODO: all necessary rebuilding lol

AROT = Struct(
    "header"
    / Aligned(
        32,
        Struct(
            "magic" / Const("AROT", FourCC),
            "version" / Const(1, Int32ub),
            "mesh_bitmap_count" / Int32ub,
            "mesh_bitmap_bit_count" / Int32ub,
            "node_count" / Int32ub,
            "bounding_box" / AABox,
        ),
    ),
    "mesh_bitmaps"
    / Array(lambda this: math.ceil(this.header.mesh_bitmap_bit_count / 32) * this.header.mesh_bitmap_count, Int32ub),
    "node_offsets" / Array(this.header.node_count, Int32ub),
    "nodes"
    / Array(
        this.header.node_count,
        Struct(
            "bitmap_index" / Int16ub,
            "subdivision_flags" / FlagsEnum(Int16ub, x=1, y=2, z=4),
            "subdivisions" / Computed(this.subdivision_flags.z + this.subdivision_flags.y + this.subdivision_flags.x),
            "children" / If(this.subdivisions, Array(2 ** this.subdivisions, Int16ub)),
        ),
    ),
)
