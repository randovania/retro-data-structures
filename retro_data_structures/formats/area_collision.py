import enum

from construct.core import (
    Pointer,
    Rebuild,
    this,
    Aligned,
    BitsInteger,
    Bitwise,
    Struct,
    Int32ub,
    Const,
    Int16ub,
    Enum,
    Tell,
    Prefixed,
    Adapter,
    Array,
    FlagsEnum,
    If,
    Int64ub,
    Int8ub,
    LazyBound,
    Pass,
    PrefixedArray,
    Switch,
)

from retro_data_structures.common_types import AABox, Vector3
from retro_data_structures.construct_extensions.misc import ErrorWithMessage, Skip


class AreaCollisionVersion(enum.IntEnum):
    prime1 = 3
    prime23 = 4
    dkcr = 5

VersionEnum = Enum(Int32ub, AreaCollisionVersion)

_shared_materials = {
    "Unknown (Default)": 0x00000001,
    "Stone": 0x00000002,
    "Metal": 0x00000004,
    "Grass": 0x00000008,
    "Ice": 0x00000010,
    "Pillar": 0x00000020,
    "Metal Grating": 0x00000040,
    "Phazon": 0x00000080,
    "Dirt": 0x00000100,
    "Snow": 0x00000800,
    "Halfpipe": 0x00002000,
    "Shield": 0x00010000,
    "Sand": 0x00020000,
    "Camera Thru": 0x00200000,
    "Wood": 0x00400000,
    "Organic": 0x00800000,
    "See Thru": 0x04000000,
    "Scan Thru": 0x08000000,
    "AI Walk Thru": 0x10000000,
    "Ceiling": 0x20000000,
    "Wall": 0x40000000,
    "Floor": 0x80000000,
}

_prime1_materials = dict(
    _shared_materials,
    **{
        "Lava": 0x00000200,
        "unknown_1": 0x00000400,
        "Slow Mud": 0x00001000,
        "Mud": 0x00004000,
        "Glass": 0x00008000,
        "Shoot Thru": 0x00040000,
        "Solid": 0x00080000,
        "unknown_2": 0x00100000,
        "unknown_3": 0x01000000,
        "Redundant Edge/Flipped Tri": 0x02000000,
    }
)

_prime23_materials = dict(
    _shared_materials,
    **{
        "SP_Metal": 0x00000200,
        "Glass": 0x00000400,
        "Fabric": 0x00001000,
        "unused_1": 0x00004000,
        "unused_2": 0x00008000,
        "Moth Organics/Seed Organics": 0x00040000,
        "Web": 0x00080000,
        "Shoot Thru": 0x00100000,
        "Redundant Edge/Flipped Tri": 0x01000000,
        "Rubber": 0x02000000,
        "Jump Not Allowed": 0x0400000000000000,
        "Spider Ball": 0x2000000000000000,
        "Screw Attack Wall Jump": 0x4000000000000000,
    }
)

_internal_materials = {
    "Player (Internal)": 0x0000000100000000,
    "Character (Internal": 0x0000000200000000,
    "Trigger (Internal)": 0x0000000400000000,
    "Projectile (Internal)": 0x0000000800000000,
    "Bomb (Internal)": 0x0000001000000000,
    "Ground Collider (Internal)": 0x0000002000000000,
    "No Static World Collision (Internal)": 0x0000004000000000,
    "Scannable (Internal)": 0x0000008000000000,
    "Target (Internal)": 0x0000010000000000,
    "Orbit (Internal)": 0x0000020000000000,
    "Occluder (Internal)": 0x0000040000000000,
    "Immovable (Internal)": 0x0000080000000000,
    "Debris (Internal)": 0x0000100000000000,
    "Power Bomb (Internal)": 0x0000200000000000,
    "Targetable Projectile (Internal)": 0x0000400000000000,
    "Collision Only Actor (Internal)": 0x0000800000000000,
    "AI Block (Internal)": 0x0001000000000000,
    "Platform (Internal)": 0x0002000000000000,
    "Non Solid Damageable (Internal)": 0x0004000000000000,
    "Show on Radar (Internal)": 0x0008000000000000,
    "Platform Slave (Internal)": 0x0010000000000000,
    "No Ice Spread (Internal)": 0x0020000000000000,
    "Grapple Thru (Internal)": 0x0040000000000000,
    "Can Jump on Character (Internal)": 0x0080000000000000,
    "Exclude From Line of Sight Test (Internal)": 0x0100000000000000,
    "Don't Show on Radar (Internal)": 0x0200000000000000,
    "Solid (Internal)": 0x0800000000000000,
    "Complex (Internal)": 0x1000000000000000,
    "Seek (Internal)": 0x8000000000000000,
}

_prime23_materials_all = dict(_prime23_materials, **_internal_materials)

_material_types = {
    "prime1": FlagsEnum(Int32ub, **_prime1_materials),
    "prime23": FlagsEnum(Int64ub, **_prime23_materials),
}


def NodeTypeEnum(subcon):
    return Enum(subcon, none=0, branch=1, leaf=2)


CollisionLeaf = Struct("bounding_box" / AABox, "triangle_index_list" / Aligned(4, PrefixedArray(Int16ub, Int16ub)))

_node_types = {"none": Pass, "branch": LazyBound(lambda: CollisionBranch), "leaf": CollisionLeaf}

CollisionBranch = Struct(
    "child_node_types" / Aligned(4, Bitwise(Array(8, NodeTypeEnum(BitsInteger(2))))),
    "child_node_offsets" / Array(8, Int32ub),  # TODO: offset adapter
    "child_nodes" / Array(8, Switch(lambda this: this.child_node_types[7 - this._index], _node_types)),
)


class TriangleAdapter(Adapter):
    def _decode(self, vertices, context, path):
        triangles = []
        for i in range(0, len(vertices), 3):
            triangles.append({"edgeA": vertices[i], "edgeB": vertices[i + 1], "edgeC": vertices[i + 2]})
        return triangles

    def _encode(self, triangles, context, path):
        vertices = []
        for triangle in triangles:
            vertices.extend(triangle.values())
        return vertices


CollisionIndex = Struct(
    "collision_materials"
    / PrefixedArray(
        Int32ub, Switch(this._._.version, _material_types, ErrorWithMessage("Unknown collision material format!"))
    ),
    "vertex_indices" / PrefixedArray(Int32ub, Int8ub),
    "edge_indices" / PrefixedArray(Int32ub, Int8ub),
    "triangle_indices" / PrefixedArray(Int32ub, Int8ub),
    "edges" / PrefixedArray(Int32ub, Struct(vertexA=Int16ub, vertexB=Int16ub)),
    "triangles" / TriangleAdapter(PrefixedArray(Int32ub, Int16ub)),
    "unknowns" / If(lambda this: AreaCollisionVersion[this._.version] > AreaCollisionVersion.prime1, PrefixedArray(Int32ub, Int16ub)),
    "vertices" / PrefixedArray(Int32ub, Vector3),
)

AreaCollision = Struct(
    "unk" / Const(0x01000000, Int32ub),
    "_size_addr" / Tell,
    Skip(1, Int32ub),
    "_size_start" / Tell,
    "magic" / Const(0xDEAFBABE, Int32ub),
    "version" / VersionEnum,
    "bounding_box" / AABox,
    "root_node_type" / NodeTypeEnum(Int32ub),
    "octree" / Prefixed(Int32ub, Switch(this.root_node_type, {
        "none": Pass, "branch": CollisionBranch, "leaf": CollisionLeaf,
    })),
    "collision_indices" / CollisionIndex,
    "_size_end" / Tell,
    "size" / Pointer(this._size_addr, Rebuild(Int32ub, this._size_end - this._size_start)),
)
