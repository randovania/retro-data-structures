from typing import List, Any

import construct
from construct import (Struct, Int32ub, Int32sb, Float32b, PrefixedArray, Int16ub, PaddedString, Hex,
                       GreedyBytes, Prefixed, ExprAdapter, Flag)

from retro_data_structures.common_types import FourCC, String


class Property:
    id: int

    def __init__(self, property_id: int, data):
        self.id = property_id
        self.data = data

    @classmethod
    def from_raw(cls, raw: construct.Container) -> "Property":
        return cls(raw.id, cls._decode_data(raw.data))

    @classmethod
    def _decode_data(cls, data: bytes) -> Any:
        raise NotImplementedError()

    @property
    def to_raw(self):
        return construct.Container(
            id=self.id,
            data=self._encode_data,
        )

    @property
    def _encode_data(self):
        raise NotImplementedError()

    def __str__(self):
        return f"{type(self).__name__} 0x{self.id:08x}: {self.data}"


class GenericProperty(Property):
    data: bytes

    @classmethod
    def _decode_data(cls, data: bytes):
        return data

    @property
    def _encode_data(self):
        return self.data


PROPERTY_TYPES = {}

ConstructProperty = ExprAdapter(
    Struct(id=Hex(Int32ub), data=Prefixed(Int16ub, GreedyBytes)),
    lambda obj, ctx: PROPERTY_TYPES.get(obj.id, GenericProperty).from_raw(obj),
    lambda obj, ctx: obj.to_raw,
)

SubProperties = PrefixedArray(Int16ub, ConstructProperty)


class StringProperty(Property):
    data: str

    @classmethod
    def _decode_data(cls, data: bytes):
        return String.parse(data)

    @property
    def _encode_data(self):
        return String.build(self.data)


class BoolProperty(Property):
    data: bool

    @classmethod
    def _decode_data(cls, data: bytes):
        return Flag.parse(data)

    @property
    def _encode_data(self):
        return Flag.build(self.data)


class IntProperty(Property):
    data: int

    @classmethod
    def _decode_data(cls, data: bytes):
        return Int32sb.parse(data)

    @property
    def _encode_data(self):
        return Int32sb.build(self.data)


class FloatProperty(Property):
    data: float

    @classmethod
    def _decode_data(cls, data: bytes):
        return Float32b.parse(data)

    @property
    def _encode_data(self):
        return Float32b.build(self.data)


class StructProperty(Property):
    data: List[Property]

    @classmethod
    def _decode_data(cls, data: bytes):
        return SubProperties.parse(data)

    @property
    def _encode_data(self):
        return SubProperties.build(self.data)

    def by_id(self, the_id: int) -> Property:
        for p in self.data:
            if p.id == the_id:
                return p
        raise KeyError(f"Id not found: {the_id}")

    @property
    def properties(self):
        return self.data



PROPERTY_TYPES.update({
    0x255A4580: StructProperty,
    0x494E414D: StringProperty,
    0x41435456: BoolProperty,
    0xB581574B: IntProperty,
    0x95F8D644: IntProperty,
    0x3FA164BC: IntProperty,
    0xDE3E40A3: IntProperty,
    0xD3AF8D72: IntProperty,
    0x8DB9398A: IntProperty,
    0x03BDEA98: IntProperty,
    0x70729364: IntProperty,
    0xCEC16932: StructProperty,
    0xE709DDC0: StructProperty,
    0x49614C51: StructProperty,
    0xB498B424: StructProperty,
    0xFFFFFFFF: StructProperty,
})

Connection = Struct(
    state=PaddedString(4, "ascii"),
    message=PaddedString(4, "ascii"),
    target=Hex(Int32ub),
)

ScriptInstance = Struct(
    type=FourCC,
    size=Int16ub,  # TODO: calculate. Size in bytes starting after this field.
    id=Hex(Int32ub),
    connections=PrefixedArray(Int16ub, Connection),
    properties=ConstructProperty,
)
