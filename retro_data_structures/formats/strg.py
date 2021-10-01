"""
https://wiki.axiodl.com/w/STRG_(File_Format)
"""

from construct import (AdaptationError, Adapter, Array, Computed, Const,
                       CString, Enum, GreedyRange, If, IfThenElse, Int32ub,
                       Rebuild, Struct, Tell, len_, this)
from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC, String
from retro_data_structures.game_check import Game
from retro_data_structures.adapters.offset import OffsetAdapter

class CorruptionLanguageOffsetAdapter(OffsetAdapter):
    def _get_table(self, context):
        return context._.string_table
    
    def _get_table_length(self, context):
        return len_(context._.string_table)
    
    def _get_item_size(self, item):
        return item.size

class LanguageOffsetAdapter(OffsetAdapter):
    pass

class NameTableOffsetAdapter(OffsetAdapter):
    pass

class StringTableOffsetAdapter(OffsetAdapter):
    pass

def _compute_corruption_strings_size(ctx):
    string_table = ctx._.string_table
    offset_table = ctx.offsets
    size = 0

    for i in range(len_(offset_table)):
        index = offset_table[i]
        string = string_table[index]
        size += string.size
    
    return size

Language = Struct(
    lang=FourCC,
    offset=Rebuild(
        Int32ub,
        IfThenElse(
            this._index == 0,
            Computed(0),
            Computed(this._.language_table[this._index-1].offset + this._.language_table[this._index-1].size)
        )
    ),
    size=If(
        game_check.is_prime2,
        Rebuild(
            Int32ub,
            Computed(this._.string_tables[this._index]._size_end - this._.string_tables[this._index]._size_start)
        )
    )
)

CorruptionLanguage = Struct(
    strings_size=Rebuild(Int32ub, _compute_corruption_strings_size),
    offsets=Array(this._.string_count, CorruptionLanguageOffsetAdapter(Int32ub)),
)

NameTable = Struct(
    name_count=Rebuild(Int32ub, len_(this.name_entries)),
    size=Rebuild(Int32ub, Computed(this._size_end - this._size_start)),
    _size_start=Tell,
    name_entries=Array(
        this.name_count,
        Struct(
            _size_start=Tell,
            offset=Rebuild(
                Int32ub,
                IfThenElse(
                    this._index == 0,
                    Computed(this._._name_size_end - this._._size_start),
                    Computed(this._.name_entries[this._index-1].offset + (this._.name_array[this._index-1]._size_end - this._.name_array[this._index-1]._size_start))
                )
            ),
            index=Int32ub,
            _size_end=Tell,
        )
    ),
    _name_size_end=Tell,
    name_array=Array(this.name_count, String),
    _size_end=Tell,
)

StringTable = Struct(
    size=If(
        game_check.is_prime1,
        Rebuild(
            Int32ub,
            Computed(this._size_end - this._size_start)
        )
    ),
    _size_start=Tell,
    offsets=Array(
        this._.string_count,
        Rebuild(
            Int32ub,
            IfThenElse(
                this._index == 0,
                Computed(0),
                Computed(this.offsets[this._index-1] + (this.strings[this._index-1]._size_end - this.strings[this._index-1]._size_start))
            )
        )
    ),
    strings=Array(
        this._.string_count,
        Struct(
            _size_start=Tell,
            string=CString("utf-16"),
            _size_end=Tell
        )
    ),
    _size_end=Tell
)

CorruptionString = Struct(
    size=Rebuild(Int32ub, Computed(this._size_end - this._size_start)),
    _size_start=Tell,
    string=String,
    _size_end=Tell
)

STRG = Struct(
    magic=Const(0x87654321, Int32ub),
    version=Enum(Int32ub, prime1=0, prime2=1, prime3=3),
    language_count=Rebuild(Int32ub, len_(this.language_table)),
    string_count=Rebuild(Int32ub, len_(this.string_tables[0])),

    language_table=If(game_check.current_game_at_most(Game.ECHOES), Array(this.language_count, Language)),

    name_table=If(game_check.current_game_at_least(Game.ECHOES), NameTable),

    language_ids=If(game_check.is_prime3, Array(this.language_count, FourCC)),
    corruption_language_table=If(game_check.is_prime3, Array(this.language_count, CorruptionLanguage)),

    string_tables=If(game_check.current_game_at_most(Game.ECHOES), Array(this.language_count, StringTable)),
    string_table=If(game_check.is_prime3, GreedyRange(CorruptionString))
)
