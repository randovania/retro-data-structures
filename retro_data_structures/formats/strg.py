import construct
from construct import (Struct, Const, Int32ub, Array, CString)

from retro_data_structures.common_types import (FourCC, String)

STRG = Struct(
    magic=Const(0x87654321, Int32ub),
    version=Int32ub,
    language_count=Int32ub,
    string_count=Int32ub,
    language_table=Array(
        construct.this.language_count,
        Struct(
            lang=FourCC,
            offset=Int32ub,
            size=Int32ub,
        )
    ),
    name_table=Struct(
        name_count=Int32ub,
        size=Int32ub,
        name_entries=Array(
            construct.this.name_count,
            Struct(
                offset=Int32ub,
                index=Int32ub,
            )
        ),
        name_array=Array(construct.this.name_count, String)
    ),
    string_tables=Array(
        construct.this.language_count,
        Struct(
            offsets=Array(construct.this._.string_count, Int32ub),
            strings=Array(construct.this._.string_count, CString("utf-16"))
        )
    )
)