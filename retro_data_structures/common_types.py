from construct import Array, PrefixedArray, Struct, Float32b, PaddedString, CString, Int16ub, Int32ub, Int64ub, Hex, Byte

Vector2f = Array(2, Float32b)
Vector3 = Array(3, Float32b)
Quaternion = Array(4, Float32b)
Color4f = Array(4, Float32b)
Transform4f = Array(12, Float32b)

Knot = Struct(
    time=Float32b,
    amplitude=Float32b,
    unk_a=Byte,
    unk_b=Byte,
)

AABox = Struct(
    min=Vector3,
    max=Vector3,
)

OBBox = Struct(
    transform=Transform4f,
    extents=Vector3,
)

FourCC = PaddedString(4, "ascii")
String = CString("utf-8")
CharAnimTime = Struct(
    time=Float32b,
    differential_state=Int32ub,  # TODO: use enum
)

AssetId32 = Hex(Int32ub)
AssetId64 = Hex(Int64ub)
ObjectTag_32 = Struct(
    type=FourCC,
    id=AssetId32,
)

ObjectTag_64 = Struct(
    type=FourCC,
    id=AssetId64,
)

MayaSpline = Struct(
    unk=Int16ub,
    knots=PrefixedArray(Int32ub, Knot),
    clampMode=Byte,
    minAmplitude=Float32b,
    maxAmplitude=Float32b,
)