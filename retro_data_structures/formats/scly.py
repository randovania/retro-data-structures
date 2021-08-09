import construct
from construct import (Struct, Const, Int8ub, Int32ub, PrefixedArray, Int16ub, PaddedString, Hex,
                       Switch, Bytes, Flag)

from retro_data_structures.common_types import FourCC, String

PROPERTY_TYPES = {}

Property = Struct(
    id=Hex(Int32ub),
    size=Int16ub,
    data=Switch(
        construct.this.id,
        PROPERTY_TYPES,
        Bytes(construct.this.size),
    )
)

SubProperties = PrefixedArray(Int16ub, Property)

PROPERTY_TYPES.update({
    0x255A4580: SubProperties,
    0x494E414D: String,
    0x41435456: Flag,
    0xB581574B: Int32ub,
    0x95F8D644: Int32ub,
    0x3FA164BC: Int32ub,
    0xDE3E40A3: Int32ub,
    0xD3AF8D72: Int32ub,
    0x8DB9398A: Int32ub,
    0x03BDEA98: Int32ub,
    0x70729364: Int32ub,
    0xCEC16932: SubProperties,
    0xE709DDC0: SubProperties,
    0x49614C51: SubProperties,
    0xB498B424: SubProperties,
})


PropertyStruct = Struct(
    id=Hex(Int32ub),
    size=Int16ub,
    data=SubProperties,
)

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
    properties=PropertyStruct,
)

SCLY = Struct(
    magic=Const(b"SCLY"),
    unk1=Int8ub,
    layer_index=Int32ub,
    version=Const(1, Int8ub),
    script_instances=PrefixedArray(Int32ub, ScriptInstance),
)
