import construct
from construct import (Struct, Const, Int32ub, Array, CString, Rebuild, Computed, If, IfThenElse)

from retro_data_structures.common_types import (FourCC, String)
from retro_data_structures import game_check

Language = Struct(
    lang=FourCC,
    offset=Rebuild(
        Int32ub,
        IfThenElse(
            construct.this._index == 0,
            Const(0, Int32ub),
            Computed(construct.this._[construct.this._index-1].offset + construct.this._[construct.this._index-1].size)
        )
    ),
    size=If(
        game_check.is_prime2,
        Rebuild(
            Int32ub,
            construct.Construct.sizeof(construct.this._.string_tables[construct.this._index]),
        )
    )
)

NameTable = Struct(
    name_count=Rebuild(Int32ub, construct.len_(construct.this.name_entries)),
    size=Rebuild(Int32ub, Computed(construct.Construct.sizeof(construct.this.name_entries) + construct.Construct.sizeof(construct.this.name_strings))),
    name_entries=Array(
        construct.this.name_count,
        Struct(
            offset=Rebuild(
                Int32ub,
                IfThenElse(
                    construct.this._index == 0,
                    construct.Construct.sizeof(construct.this._),
                    Computed(construct.this._[construct.this._index-1].offset + construct.Construct.sizeof(construct.this._._.name_array[construct.this._index-1]))
                )
            ),
            index=Int32ub,
        )
    ),
    name_array=Array(construct.this.name_count, String)
)

StringTable = Struct(
    size=If(
        game_check.is_prime1,
        Rebuild(
            Int32ub,
            Computed(construct.Construct.sizeof(construct.this._) - construct.Construct.sizeof(construct.this))
        )
    ),
    offsets=Array(
        construct.this._.string_count,
        Rebuild(
            Int32ub,
            IfThenElse(
                construct.this._index == 0,
                Const(0, Int32ub),
                Computed(construct.this._[construct.this._index-1] + construct.Construct.sizeof(construct.this._._.strings[construct.this._index-1]))
            )
        )
    ),
    strings=Array(construct.this._.string_count, CString("utf-16"))
)

STRG = Struct(
    magic=Const(0x87654321, Int32ub),
    version=Int32ub,
    language_count=Rebuild(Int32ub, construct.len_(construct.this.language_table)),
    string_count=Rebuild(Int32ub, construct.len_(construct.this.string_tables[0])),
    language_table=Array(construct.this.language_count, Language),
    name_table=If(game_check.is_prime2, NameTable),
    string_tables=Array(construct.this.language_count, StringTable)
)