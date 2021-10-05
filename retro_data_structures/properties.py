from construct import (Byte, Computed, Flag, Float32b, GreedyRange, Hex,
                       Int16ub, Int32sb, Int32ub, Prefixed, PrefixedArray,
                       Struct, Switch, this)

from retro_data_structures.common_types import String
from retro_data_structures.game_check import AssetIdCorrect

PROPERTY_INFO = {}
PROPERTY_TYPES = {}

Property = Struct(
    "id" / Hex(Int32ub),
    "comment" / Computed(lambda this: PROPERTY_INFO.get(this.id, "Unknown property")),
    "data" / Prefixed(Int16ub, GreedyRange(Switch(this.id, PROPERTY_TYPES, Byte))),
)

SubProperties = PrefixedArray(Int16ub, Property)

def AddPropertyInfo(_id, data_type, comment="Unknown property"):
    PROPERTY_TYPES[_id] = data_type
    PROPERTY_INFO[_id] = comment

# TODO: add missing comments
AddPropertyInfo(0x255A4580, SubProperties, "EditorProperties")
AddPropertyInfo(0x494E414D, String)
AddPropertyInfo(0x41435456, Flag)
AddPropertyInfo(0xB581574B, Int32sb)
AddPropertyInfo(0x95F8D644, Int32sb)
AddPropertyInfo(0x3FA164BC, Int32sb)
AddPropertyInfo(0xDE3E40A3, Int32sb)
AddPropertyInfo(0xD3AF8D72, Int32sb)
AddPropertyInfo(0x8DB9398A, Int32sb)
AddPropertyInfo(0x03BDEA98, Int32sb)
AddPropertyInfo(0x70729364, Int32sb)
AddPropertyInfo(0xCEC16932, SubProperties)
AddPropertyInfo(0xE709DDC0, SubProperties)
AddPropertyInfo(0x49614C51, SubProperties)
AddPropertyInfo(0xB498B424, SubProperties)
AddPropertyInfo(0xFFFFFFFF, SubProperties, "Base property struct")
