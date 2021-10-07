"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

from construct import (Hex, Int16ub, Int32ub, PaddedString, Pointer,
                       PrefixedArray, Rebuild, Seek, Struct, Tell, this)
from construct.core import GreedyBytes, Int8ub, Prefixed
from retro_data_structures.common_types import FourCC
from retro_data_structures.properties import Property

Connection = Struct(
    state=PaddedString(4, "ascii"),
    message=PaddedString(4, "ascii"),
    target=Hex(Int32ub),
)

ConnectionPrime = Struct(
    state=Int32ub,
    message=Int32ub,
    target=Hex(Int32ub)
)

ScriptInstance = Struct(
    "type" / FourCC,
    "instance" / Prefixed(Int16ub, Struct(
        "id" / Hex(Int32ub),
        "connections" / PrefixedArray(Int16ub, Connection),
        "properties" / Property,
    ))
)

ScriptInstancePrime = Struct(
    "type" / Hex(Int8ub),
    "instance" / Prefixed(Int32ub, Struct(
        "id" / Hex(Int32ub),
        "connections" / PrefixedArray(Int32ub, ConnectionPrime),
        "property_count" / Int32ub,
        "properties" / GreedyBytes
    ))
)
