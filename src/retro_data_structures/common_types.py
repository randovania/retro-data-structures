from __future__ import annotations

import uuid

import construct
from construct import (
    Array,
    Byte,
    CString,
    Float32b,
    Hex,
    Int8ub,
    Int32ub,
    Int64ub,
    PaddedString,
    PrefixedArray,
    Struct,
)

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
    cached_tangents_a=construct.If(construct.this.unk_a == 5, Vector2f),
    cached_tangents_b=construct.If(construct.this.unk_b == 5, Vector2f),
)

AABox = Struct(
    min=Vector3,
    max=Vector3,
)

OBBox = Struct(
    transform=Transform4f,
    extents=Vector3,
)

GUID = construct.ExprAdapter(
    construct.Bytes(16),
    lambda obj, ctx: uuid.UUID(bytes_le=obj),
    lambda obj, ctx: obj.bytes_le,
)

FourCC = PaddedString(4, "ascii")
String = CString("utf-8")
CharAnimTime = Struct(
    time=Float32b,
    differential_state=Int32ub,  # TODO: use enum
)

AssetId32 = Hex(Int32ub)
AssetId64 = Hex(Int64ub)
AssetId128 = Hex(construct.BytesInteger(16, swapped=True))
ObjectTag_32 = Struct(
    type=FourCC,
    id=AssetId32,
)

ObjectTag_64 = Struct(
    type=FourCC,
    id=AssetId64,
)

MayaSpline = Struct(
    pre_infinity=Int8ub,
    post_infinity=Int8ub,
    knots=PrefixedArray(Int32ub, Knot),
    clamp_mode=Byte,
    minimum_amplitude=Float32b,
    maximum_amplitude=Float32b,
)
