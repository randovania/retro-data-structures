"""
https://wiki.axiodl.com/w/STRG_(Metroid_Prime)
"""

import construct
from construct import (this, len_, Enum, Struct, Const, Int32ub, Array, CString, Rebuild, Computed, If, IfThenElse)

from retro_data_structures.common_types import (FourCC, String)
from retro_data_structures import game_check

Language = Struct(
    lang=FourCC,
    offset=Rebuild(
        Int32ub,
        IfThenElse(
            this._index == 0,
            Const(0, Int32ub),
            Computed(this._.language_table[this._index-1].offset + this._.language_table[this._index-1].size)
        )
    ),
    size=If(
        game_check.is_prime2,
        Rebuild(
            Int32ub,
            this._.string_tables[this._index].sizeof(),
        )
    )
)

NameTable = Struct(
    name_count=Rebuild(Int32ub, len_(this.name_entries)),
    size=Rebuild(Int32ub, Computed(this.name_entries.sizeof() + this.name_array.sizeof())),
    name_entries=Array(
        this.name_count,
        Struct(
            offset=Rebuild(
                Int32ub,
                IfThenElse(
                    this._index == 0,
                    this._.name_entries.sizeof(),
                    Computed(this._.name_entries[this._index-1].offset + this._.name_array[this._index-1].sizeof())
                )
            ),
            index=Int32ub,
        )
    ),
    name_array=Array(this.name_count, String)
)

StringTable = Struct(
    size=If(
        game_check.is_prime1,
        Rebuild(
            Int32ub,
            Computed(this.sizeof() - construct.Construct.sizeof(Int32ub))
        )
    ),
    offsets=Array(
        this._.string_count,
        Rebuild(
            Int32ub,
            IfThenElse(
                this._index == 0,
                Const(0, Int32ub),
                Computed(this.offsets[this._index-1] + this.strings[this._index-1].sizeof())
            )
        )
    ),
    strings=Array(this._.string_count, CString("utf-16"))
)

STRG = Struct(
    magic=Const(0x87654321, Int32ub),
    version=Enum(Int32ub, prime1=0, prime2=1, prime3=3),
    language_count=Rebuild(Int32ub, len_(this.language_table)),
    string_count=Rebuild(Int32ub, len_(this.string_tables[0])),
    language_table=Array(this.language_count, Language),
    name_table=If(game_check.is_prime2, NameTable),
    string_tables=Array(this.language_count, StringTable)
)