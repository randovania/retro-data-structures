from construct import Array, Struct, Float32b, PaddedString, CString

Vector3 = Array(3, Float32b)
Quaternion = Array(4, Float32b)
Color4f = Array(4, Float32b)
AABox = Struct(
    min=Vector3,
    max=Vector3,
)
FourCC = PaddedString(4, "ascii")
String = CString("utf-8")
