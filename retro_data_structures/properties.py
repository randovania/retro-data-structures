from construct import (Byte, Computed, Flag, Float32b, GreedyRange, Hex,
                       Int16ub, Int32sb, Int32ub, Prefixed, PrefixedArray,
                       Struct, Switch, this)

from retro_data_structures.common_types import String
from retro_data_structures.game_check import AssetIdCorrect

PROPERTY_INFO = {}
PROPERTY_TYPES = {}

Property = Struct(
    "id" / Hex(Int32ub),
    "data" / Prefixed(Int16ub, GreedyRange(Switch(this.id, PROPERTY_TYPES, Byte))),
    "comment" / Computed(lambda this: PROPERTY_INFO.get(this.id, "Unknown property"))
)

SubProperties = PrefixedArray(Int16ub, Property)

def AddPropertyInfo(_id, data_type, comment=""):
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

# ScannableObjectInfo Properties
AddPropertyInfo(0x2F5B6423, AssetIdCorrect, "STRG, Scan Text")
AddPropertyInfo(0xC308A322, Int32sb, "Scan Speed (0 for fast, 1 for slow)")
AddPropertyInfo(0x7B714814, Flag, "Is Important? (0 for blue, 1 for red)")
AddPropertyInfo(0x1733B1EC, Flag, "Use Logbook Model After Scan?")
AddPropertyInfo(0x53336141, AssetIdCorrect, "CMDL, Post-Scan Override Texture")
AddPropertyInfo(0x3DE0BA64, Float32b, "Logbook Default X Rotation")
AddPropertyInfo(0x2ADD6628, Float32b, "Logbook Default Z Rotation")
AddPropertyInfo(0xD0C15066, Float32b, "Logbook Scale")
AddPropertyInfo(0xB7ADC418, AssetIdCorrect, "CMDL, Logbook Model")
AddPropertyInfo(0x15694EE1, Byte, "AnimationParameters, Logbook AnimSet")
AddPropertyInfo(0x58F9FE99, Byte, "AnimationParameters, Unknown")
AddPropertyInfo(0x1C5B4A3A, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x1C5B4A3A, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x8728A0EE, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0xF1CD99D3, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x6ABE7307, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x1C07EBA9, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x8774017D, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0xF1913840, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x6AE2D294, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x1CE2091C, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
# TODO: unknown prime 3 property 1
# TODO: unknown prime 3 property 2

# ScanInfoSecondaryModel Properties
AddPropertyInfo(0x1F7921BC, AssetIdCorrect, "CMDL, Model")
AddPropertyInfo(0xCDD202D1, Byte, "AnimationParameters, AnimSet")
AddPropertyInfo(0x3EA2BED8, String, "Attach Bone Name")
