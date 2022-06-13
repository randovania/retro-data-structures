"""
https://wiki.axiodl.com/w/STRG_(File_Format)
"""
import typing

from construct import (
    Array,
    Byte,
    Computed,
    Const,
    CString,
    Construct,
    Enum,
    GreedyRange,
    Pointer,
    Rebuild,
    Seek,
    Tell,
    len_,
    this,
)
from construct import Struct, Int32ub, If
import construct

from retro_data_structures.adapters.offset import OffsetAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import FourCC, String
from retro_data_structures.game_check import Game


class CorruptionLanguageOffsetAdapter(OffsetAdapter):
    def _get_table(self, context):
        return context._.string_table

    def _get_table_length(self, context):
        return context._.string_table_length

    def _get_item_size(self, item):
        return super()._get_item_size(item) + Int32ub.sizeof()


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

    for i in range(ctx._.string_count):
        index = offset_table[i]
        string = string_table[index]
        size += string.size

    return size


Language = Struct(
    "lang" / FourCC,
    "offset" / LanguageOffsetAdapter(Int32ub),
    "size" / If(this._.prime2, Rebuild(Int32ub, lambda this: this._.string_tables[this.offset]._size)),
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
    "name_array"
    / Array(
        this.name_count,
        Struct(
            "_size_start" / Tell,
            "string" / String,
            "_size_end" / Tell,
            "size" / Computed(this._size_end - this._size_start),
        ),
    ),
    "name_entries"
    / Pointer(
        this._entries_start,
        Array(
            this.name_count,
            Struct(
                "offset" / NameTableOffsetAdapter(Int32ub),
                "index" / Int32ub,
            ),
        ),
    ),
    "_size_end" / Tell,
    "size" / Pointer(this._start, Rebuild(Int32ub, this._size_end - this._size_start)),
)

StringTable = Struct(
    "_start" / Tell,
    If(this._.prime1, Seek(Int32ub.sizeof(), 1)),
    "_size_start" / Tell,
    "_offset_start" / Tell,
    Seek(Int32ub.sizeof() * this._.string_count, 1),
    "strings"
    / Array(
        this._.string_count,
        Struct(
            "_size_start" / Tell,
            "string" / CString("utf-16-be"),
            "_size_end" / Tell,
            "size" / Computed(this._size_end - this._size_start),
        ),
    ),
    "_size_end" / Tell,
    "offsets" / Pointer(this._offset_start, StringTableOffsetAdapter(Int32ub)[this._.string_count]),
    "_size" / Computed(this._size_end - this._size_start),
    "size" / If(this._.prime1, Pointer(this._start, Rebuild(Int32ub, this._size))),
)

CorruptionString = Struct(
    "_start" / Tell,
    Seek(Int32ub.sizeof(), 1),
    "_size_start" / Tell,
    "string" / String,
    "_size_end" / Tell,
    "size" / Pointer(this._start, Rebuild(Int32ub, this._size_end - this._size_start)),
)     

STRG = Struct(
    "magic" / Const(0x87654321, Int32ub),
    "version" / Enum(Int32ub, prime1=0, prime2=1, prime3=3),
    "language_count" / Int32ub,
    "string_count" / Int32ub,
    "prime1" / Computed(this.version == "prime1"),
    "prime2" / Computed(this.version == "prime2"),
    "prime3" / Computed(this.version == "prime3"),
    "lang_table_start" / Tell,
    If(this.prime1 | this.prime2, Seek((FourCC.sizeof() + Int32ub.sizeof()) * this.language_count, 1)),
    If(this.prime2, Seek(Int32ub.sizeof() * this.language_count, 1)),
    "name_table" / If(this.prime2 | this.prime3, NameTable),
    "corr_lang_ids_start" / Tell,
    If(this.prime3, Seek(FourCC.sizeof() * this.language_count, 1)),
    "corr_lang_table_start" / Tell,
    If(this.prime3, Seek(Int32ub.sizeof() * (this.string_count + 1) * this.language_count, 1)),
    "string_tables" / If(this.prime1 | this.prime2, StringTable[this.language_count]),
    "string_table" / If(this.prime3, GreedyRange(CorruptionString)),
    "string_table_length" / If(this.prime3, Computed(len_(this.string_table))),
    "language_table" / If(this.prime1 | this.prime2, Pointer(this.lang_table_start, Language[this.language_count])),
    "language_ids" / If(this.prime3, Pointer(this.corr_lang_ids_start, FourCC[this.language_count])),
    "corruption_language_table"
    / If(this.prime3, Pointer(this.corr_lang_table_start, CorruptionLanguage[this.language_count])),
    "junk" / GreedyRange(Byte),
)


class Strg(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "STRG"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return STRG

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
    
    def get_strings(self, language: str) -> typing.Iterator[str]:
        found = False

        if self._raw.prime3:
            for i, lang in enumerate(self._raw.language_ids):
                if lang != language:
                    continue
                for offset in self._raw.corruption_language_table[i].offsets:
                    yield self._raw.string_table[offset].string
                found = True
                break
        
        else:
            for i, lang in enumerate(self._raw.language_table):
                if lang.lang != language:
                    continue
                for string in self._raw.string_tables[i].strings:
                    yield string.string
                found = True
                break
        
        if not found:
            raise ValueError(f"No language {language} found in STRG")
    
    def set_strings(self, language: str, strings: typing.List[str]):
        found = False

        if self._raw.prime3:
            for i, lang in enumerate(self._raw.language_ids):
                if lang != language:
                    continue
                for j, offset in enumerate(self._raw.corruption_language_table[i].offsets):
                    self._raw.string_table[offset].string = strings[j]
                found = True
                break
        
        else:
            for i, lang in enumerate(self._raw.language_table):
                if lang.lang != language:
                    continue
                for j, string in enumerate(self._raw.string_tables[i].strings):
                    string.string = strings[j]
                found = True
                break
        
        if not found:
            raise ValueError(f"No language {language} found in STRG")
            
    @property
    def strings(self) -> typing.List[str]:
        return list(self.get_strings("ENGL"))
    
    @strings.setter
    def strings(self, value: typing.List[str]):
        self.set_strings("ENGL", value)
    
    def set_string(self, index: int, value: str, *, language: str = "ENGL"):
        strings = list(self.get_strings(language))
        strings[index] = value
        self.set_strings(language, strings)
