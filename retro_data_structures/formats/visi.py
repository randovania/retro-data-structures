from construct.core import (
    BitStruct,
    BitsInteger,
    BitsSwapped,
    If,
    Int16ub,
    Int24ub,
    Int8ub,
    Switch,
    this,
    Array,
    Const,
    Enum,
    FixedSized,
    Flag,
    GreedyBytes,
    GreedyRange,
    Int32ub,
    Prefixed,
    Struct,
)

from retro_data_structures.common_types import FourCC, AABox

OctreeNode = Struct(
    "header"
    / BitsSwapped(
        BitStruct(
            "subdivide_x" / Flag,
            "subdivide_y" / Flag,
            "subdivide_z" / Flag,
            "node_type" / Enum(BitsInteger(2, swapped=True), out_of_bounds=1, end_of_hierarchy=2, regular_node=3),
            "pointer_size" / Enum(BitsInteger(2, swapped=True), _16_bit=0, _8_bit=1, _24_bit=2),
        )
    ),
    "child_pointers"
    / Array(
        (2 ** (this.header.subdivide_x + this.header.subdivide_y + this.header.subdivide_z)) - 1,
        Switch(this.header.pointer_size, {"_16_bit": Int16ub, "_8_bit": Int8ub, "_24_bit": Int24ub}),
    ),
    "leaf_data"
    / If(
        lambda this: not (this.header.subdivide_x or this.header.subdivide_y or this.header.subdivide_z),
        FixedSized(this._.leaf_size, GreedyBytes),  # TODO: handle leaf data
    ),
)

VISI = Struct(
    "magic" / Const("VISI", FourCC),
    "version" / Enum(Int32ub, prime=2),
    "has_actors" / Flag,
    "unk1" / Flag,
    "feature_count" / Int32ub,
    "light_count" / Int32ub,
    "2nd_layer_light_count" / Int32ub,
    "entity_count" / Int32ub,
    "leaf_size" / Int32ub,
    "light_visibility_node_count" / Int32ub,
    "entities" / Array(this.entity_count, Int32ub),
    "light_visibility_nodes" / Array(this.light_visibility_node_count, FixedSized(this.leaf_size, GreedyBytes)),
    "bounding_box" / AABox,
    "total_visibility_count" / Int32ub,
    "total_light_count" / Int32ub,
    "octree" / Prefixed(Int32ub, GreedyRange(OctreeNode)),
)
