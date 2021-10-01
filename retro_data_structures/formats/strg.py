"""
https://wiki.axiodl.com/w/STRG_(File_Format)
"""

from construct import (Byte, Index, Pointer, Seek, AdaptationError, Adapter, Array, Computed, Const,
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
        return len_(self._get_table(context))

class LanguageOffsetAdapter(OffsetAdapter):
    def _get_table(self, context):
        return context._.string_tables
    
    def _get_table_length(self, context):
        return context._.language_count
    
    def _get_item_size(self, item):
        return item._size_end - item._size_start

class NameTableOffsetAdapter(OffsetAdapter):
    def _get_table(self, context):
        return context._.name_array
    
    def _get_table_length(self, context):
        return context._.name_count
    
    def _get_base_offset(self, context):
        return context._._name_size_end - context._._size_start

class StringTableOffsetAdapter(OffsetAdapter):
    def _get_table(self, context):
        return context.strings
    
    def _get_table_length(self, context):
        return context._.string_count
    
    def _get_base_offset(self, context):
        return Int32ub.sizeof() * context._.string_count


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
    "lang" / FourCC,
    "offset" / LanguageOffsetAdapter(Int32ub),
    "size" / If(
        game_check.is_prime2,
        Int32ub
        #Rebuild(
        #    Int32ub,
        #    this._.string_tables[this._index]._size
        #)
        # TODO: rebuild
    )
)

CorruptionLanguage = Struct(
    "strings_size" / Rebuild(Int32ub, _compute_corruption_strings_size),
    "offsets" / CorruptionLanguageOffsetAdapter(Int32ub)[this._.string_count],
)

NameTable = Struct(
    "name_count" / Rebuild(Int32ub, len_(this.name_entries)),
    "_start" / Tell,
    Seek(Int32ub.sizeof(), 1),
    "_size_start" / Tell,
    "_entries_start" / Tell,
    Seek(Int32ub.sizeof() * this.name_count * 2, 1),
    "_name_size_end" / Tell,
    "name_array" / Array(
        this.name_count,
        Struct(
            "_size_start" / Tell,
            "string" / String,
            "_size_end" / Tell,
            "size" / Computed(this._size_end - this._size_start)
        )
    ),
    "name_entries" / Pointer(
        this._entries_start,
        Array(
            this.name_count,
            Struct(
                "offset" / NameTableOffsetAdapter(Int32ub),
                "index" / Int32ub,
            )
        )
    ),
    "_size_end" / Tell,
    "size" / Pointer(this._start, Rebuild(Int32ub, this._size_end - this._size_start)),
)

StringTable = Struct(
    "_start" / Tell,
    If(game_check.is_prime1, Seek(Int32ub.sizeof(), 1)),

    "_size_start" / Tell,
    "_offset_start" / Tell,
    Seek(Int32ub.sizeof() * this._.string_count, 1),
    "strings" / Array(
        this._.string_count,
        Struct(
            "_size_start" / Tell,
            "string" / CString("utf-16-be"),
            "_size_end" / Tell,
            "size" / Computed(this._size_end - this._size_start)
        )
    ),
    "_size_end" / Tell,

    "offsets" / Pointer(
        this._offset_start,
        StringTableOffsetAdapter(Int32ub)[this._.string_count]
    ),

    "_size" / Computed(this._size_end - this._size_start),
    "size" / If(
        game_check.is_prime1,
        Pointer(
            this._start,
            Rebuild(
                Int32ub,
                this._size
            )
        )
    ),
)

CorruptionString = Struct(
    "size" /Rebuild(Int32ub, Computed(this._size_end - this._size_start)),
    "_size_start" / Tell,
    "string" / String,
    "_size_end" / Tell
)

STRG = Struct(
    "magic" / Const(0x87654321, Int32ub),
    "version" / Enum(Int32ub, prime1=0, prime2=1, prime3=3),
    "language_count" / Int32ub,
    "string_count" / Int32ub,

    "lang_table_start" / Tell,
    If(game_check.is_prime1, Seek(Language.sizeof(target_game=Game.PRIME)  * this.language_count, 1)),
    If(game_check.is_prime2, Seek(Language.sizeof(target_game=Game.ECHOES) * this.language_count, 1)),

    "name_table" / If(game_check.current_game_at_least(Game.ECHOES), NameTable),

    "language_ids" / If(game_check.is_prime3, FourCC[this.language_count]),
    "corruption_language_table" / If(game_check.is_prime3, CorruptionLanguage[this.language_count]),

    "string_tables" / If(game_check.current_game_at_most(Game.ECHOES), StringTable[this.language_count]),
    "string_table" / If(game_check.is_prime3, GreedyRange(CorruptionString)),

    "language_table" / If(game_check.current_game_at_most(Game.ECHOES), Pointer(this.lang_table_start, Language[this.language_count])),

    "junk" / GreedyRange(Byte)
)
