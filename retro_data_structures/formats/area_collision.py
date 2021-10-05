from construct import Rebuild, Byte, this, Aligned, BitsInteger, Bitwise, Struct, Int32ub, Const, Int16ub, Enum, Tell, Prefixed
from construct.core import Adapter, Array, ExprAdapter, FlagsEnum, If, Int, Int64ub, Pass, PrefixedArray, Switch

from retro_data_structures.common_types import AABox, Vector3
from retro_data_structures import game_check

def NodeTypeEnum(subcon):
    return Enum(subcon, none=0, branch=1, leaf=2)

_node_cases = {}

CollisionLeaf = Struct(
    "bounding_box" / AABox,
    "triangle_index_list" / PrefixedArray(Int16ub, Int16ub)
)

def CollisionBranch():
    return Struct(
        "child_node_types" / Aligned(32, Bitwise(Array(8, NodeTypeEnum(BitsInteger(2))))),
        "child_node_offsets" / Array(8, Int32ub), # TODO: offset adapter
        "child_nodes" / Array(8, Switch(
            lambda this: this.child_node_types[7-this._index],
            _node_cases
        ))
    )

_node_cases = {
    "none": Pass,
    "branch": CollisionBranch(),
    "leaf": CollisionLeaf
}

Prime1Materials = FlagsEnum(Int32ub,
    unknown=0x00000001,
    stone=0x00000002,
    metal=0x00000004,
    grass=0x00000008,
    ice=0x00000010,
    pillar=0x00000020,
    metal_grating=0x00000040,
    phazon=0x00000080,
    dirt=0x00000100,
    lava=0x00000200,

    snow=0x00000800,
    slow_mud=0x00001000,
    halfpipe=0x00002000,
    mud=0x00004000,
    glass=0x00008000,
    shield=0x00010000,
    sand=0x00020000,
    shoot_thru=0x00040000,
    solid=0x00080000,

    camera_thru=0x00200000,
    wood=0x00400000,
    organic=0x00800000,

    flipped_tri=0x02000000,
    see_thru=0x04000000,
    scan_thru=0x08000000,
    ai_walk_thru=0x10000000,
    ceiling=0x20000000,
    wall=0x40000000,
    floor=0x80000000
)

Prime23Materials = FlagsEnum(
    Int64ub,
    unknown=0x00000001,
    stone=0x00000002,
    metal=0x00000004,
    grass=0x00000008,
    ice=0x00000010,
    pillar=0x00000020,
    metal_grating=0x00000040,
    phazon=0x00000080,
    dirt=0x00000100,
    sp_metal=0x00000200,
    glass=0x00000400,
    snow=0x00000800,
    fabric=0x00001000,
    halfpipe=0x00002000,
    
    shield=0x00010000,
    sand=0x00020000,
    alien_organics=0x00040000,
    web=0x00080000,
    shoot_thru=0x00100000,
    camera_thru=0x00200000,
    wood=0x00400000,
    organic=0x00800000,
    flipped_tri=0x01000000,
    rubber=0x02000000,
    see_thru=0x04000000,
    scan_thru=0x08000000,
    ai_walk_thru=0x10000000,
    ceiling=0x20000000,
    wall=0x40000000,
    floor=0x80000000,

    jump_not_allowed=0x0400000000000000,
    spider_ball=0x2000000000000000,
    screw_attack_wall_jump=0x4000000000000000
)

_material_types = {
    game_check.Game.PRIME: Prime1Materials,
    game_check.Game.ECHOES: Prime23Materials,
    game_check.Game.CORRUPTION: Prime23Materials
}

class TriangleAdapter(Adapter):
    def _decode(self, obj, context, path):
        for i in range(len(obj)//3):
            obj[i:i+3] = {"edgeA": obj[i], "edgeB": obj[i+1], "edgeC": obj[i+2]}
        return obj

    def _encoder(self, obj, context, path):
        encoded = []
        for triangle in obj:
            encoded.extend(triangle.values())
        return encoded

CollisionIndex = Struct(
    "collision_materials" / PrefixedArray(Int32ub, Switch(game_check.get_current_game, _material_types)),
    "vertex_indices" / PrefixedArray(Int32ub, Byte),
    "edge_indices" / PrefixedArray(Int32ub, Byte),
    "triangle_indices" / PrefixedArray(Int32ub, Byte),
    "edges" / PrefixedArray(Int32ub, Struct(vertexA=Int16ub, vertexB=Int16ub)),
    "triangle_edges" / PrefixedArray(Int32ub, Int16ub),
    "unknowns" / If(lambda this: not game_check.is_prime1, PrefixedArray(Int32ub, Int16ub)),
    "vertices" / PrefixedArray(Int32ub, Vector3)
)

AreaCollision = Struct(
    "unk" / Const(0x01000000, Int32ub),
    "size" / Rebuild(Int32ub, this._size_end - this._size_start),
    "_size_start" / Tell,
    "magic" / Const(0xDEAFBABE, Int32ub),
    "version" / Enum(Int32ub, prime1=3, prime23=4, dkcr=5),
    "bounding_box" / AABox,
    "root_node_type" / NodeTypeEnum(Int32ub),
    "octree" / Prefixed(Int32ub, Switch(
        this.root_node_type,
        _node_cases
    )),
    "collision_indices" / CollisionIndex,
    "_size_end" / Tell
)