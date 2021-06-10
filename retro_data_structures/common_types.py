from construct import Array, Struct, Float32b, PaddedString, CString, Int32ub, Int64ub

Vector2f = Array(2, Float32b)
Vector3 = Array(3, Float32b)
Quaternion = Array(4, Float32b)
Color4f = Array(4, Float32b)
AABox = Struct(
    min=Vector3,
    max=Vector3,
)
FourCC = PaddedString(4, "ascii")
String = CString("utf-8")
CharAnimTime = Struct(
    time=Float32b,
    differential_state=Int32ub,  # TODO: use enum
)

AssetId32 = Int32ub
AssetId64 = Int64ub
ObjectTag_32 = Struct(
    type=FourCC,
    id=AssetId32,
)
ObjectTag_64 = Struct(
    type=FourCC,
    id=AssetId64,
)
