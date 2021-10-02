"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

from construct import (Hex, Int16ub, Int32ub, PaddedString, Pointer,
                       PrefixedArray, Rebuild, Seek, Struct, Tell, this)
from retro_data_structures.common_types import FourCC
from retro_data_structures.properties import Property

Connection = Struct(
    state=PaddedString(4, "ascii"),
    message=PaddedString(4, "ascii"),
    target=Hex(Int32ub),
)

ScriptInstance = Struct(
    "type" / FourCC,
    "_size_start" / Tell,
    Seek(Int16ub.sizeof(), 1),
    "_start" / Tell,
    "id" / Hex(Int32ub),
    "connections" / PrefixedArray(Int16ub, Connection),
    "properties" / Property,
    "_end" / Tell,
    "size" / Pointer(this._size_start, Rebuild(Int16ub, this._end - this._start))
)
