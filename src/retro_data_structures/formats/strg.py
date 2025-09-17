from __future__ import annotations

import io
import re
from typing import TYPE_CHECKING

import construct
from construct import Array, Const, Container, CString, If, Int32ub, Prefixed, Rebuild, Struct, len_, this

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import FourCC
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.formats.room import GreedyBytes
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from collections.abc import Iterator

    from typing_extensions import Self

    from retro_data_structures.asset_manager import AssetManager


class NameTableConstruct(construct.Adapter):
    def __init__(self):
        super().__init__(
            Struct(
                "name_count" / Rebuild(Int32ub, len_(this.data.entries)),
                "data"
                / Prefixed(
                    Int32ub,
                    construct.Struct(
                        "data_start" / construct.Tell,
                        "entries"
                        / Array(
                            this._.name_count,
                            Struct(
                                "name_offset" / Int32ub,
                                "string_index" / Int32ub,
                            ),
                        ),
                        "strings_start" / construct.Tell,
                        "raw_strings" / construct.GreedyBytes,
                    ),
                ),
            )
        )

    def _decode(self, obj: Container, context: Container, path: str) -> dict[str, int]:
        c = CString("utf-8")
        raw_strings = io.BytesIO(obj.data.raw_strings)

        def stream_at(offset: int):
            raw_strings.seek(offset - (obj.data.strings_start - obj.data.data_start))
            return raw_strings

        return {c.parse_stream(stream_at(entry.name_offset)): entry.string_index for entry in obj.data.entries}

    def _encode(self, obj: dict[str, int], context: Container, path: str) -> Container:
        raw_strings = []
        entries = []

        name_offset = Int32ub.sizeof() * 2 * len(obj)
        for name, index in obj.items():
            raw_strings.append(name.encode("ascii") + b"\x00")
            entries.append(
                Container(
                    name_offset=name_offset,
                    string_index=index,
                )
            )
            name_offset += len(raw_strings[-1])

        return Container(
            data=Container(
                entries=entries,
                raw_strings=b"".join(raw_strings),
            )
        )


NameTable = NameTableConstruct()

STRGHeader = Struct(
    "magic" / Const(0x87654321, Int32ub),
    "version" / construct.Enum(Int32ub, prime1=0, prime2=1, prime3=3),
    "language_count" / Int32ub,
    "string_count" / Int32ub,
)

Language = Struct(
    "lang" / FourCC,
    "offset" / Int32ub,
    "size" / If(this._.header.version == "prime2", Int32ub),
)

STRG_V1 = Struct(
    "header" / STRGHeader,
    "language_table" / Array(this.header.language_count, Language),
    "name_table" / If(this.header.version == "prime2", NameTable),
    "string_tables"
    / Array(
        this.header.language_count,
        Struct(
            "size" / If(this._.header.version == "prime1", Int32ub),
            "offsets" / Array(this._.header.string_count, Int32ub),
            "raw_strings" / Array(this._.header.string_count, GreedyBytes),
        ),
    ),
    AlignTo(32),
    construct.Terminated,
)

STRG_V3 = Struct(
    "header" / STRGHeader,
    "name_table" / NameTable,
    "language_ids" / Array(this.header.language_count, FourCC),
    "language_table"
    / Array(
        this.header.language_count,
        Struct(
            "strings_size" / Int32ub,
            "string_offsets" / Array(this._.header.string_count, Int32ub),
        ),
    ),
    "strings" / construct.GreedyRange(Prefixed(Int32ub, CString("utf-8"))),
    AlignTo(32),
    construct.Terminated,
)

STRG = construct.FocusedSeq(
    "strg",
    header=construct.Peek(STRGHeader),
    strg=construct.Switch(
        lambda this: this.header.version if this._parsing else this.strg.header.version,
        {
            "prime1": STRG_V1,
            "prime2": STRG_V1,
            "prime3": STRG_V3,
        },
        construct.Error,
    ),
)

image_regex = re.compile(r"&image=(?:.+?,)*?((?:[a-fA-F0-9]+,?)+);")
font_regex = re.compile(r"&font=([a-fA-F0-9]+?);")


class Strg(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "STRG"

    # Parsing

    @classmethod
    def _parse_v1(cls, stream: io.BytesIO, header: Container, target_game: Game) -> Container:
        languages = Language[header.language_count].parse_stream(stream, header=header)
        name_table = None
        if target_game >= Game.ECHOES:
            name_table = NameTable.parse_stream(stream)

        result = {}

        for language in languages:
            if target_game == Game.PRIME:
                # table_size
                Int32ub.parse_stream(stream)

            Int32ub[header.string_count].parse_stream(stream)  # offsets
            result[language.lang] = CString("utf-16-be")[header.string_count].parse_stream(stream)

        return Container(
            languages=result,
            name_table=name_table,
        )

    @classmethod
    def _parse_v3(cls, stream: io.BytesIO, header: Container, target_game: Game) -> Container:
        name_table = NameTable.parse_stream(stream)
        language_ids = FourCC[header.language_count].parse_stream(stream)

        language_sizes = {}
        language_offsets = {}

        for language_id in language_ids:
            # strings_size
            language_sizes[language_id] = Int32ub.parse_stream(stream)
            language_offsets[language_id] = Int32ub[header.string_count].parse_stream(stream)

        raw_data = stream.read()
        raw_strings = io.BytesIO(raw_data)

        def stream_at(offset: int):
            raw_strings.seek(offset)
            return raw_strings

        languages = {
            language_id: [Prefixed(Int32ub, CString("utf-8")).parse_stream(stream_at(offset)) for offset in offsets]
            for language_id, offsets in language_offsets.items()
        }

        return Container(
            languages=languages,
            name_table=name_table,
        )

    @classmethod
    def parse(cls, data: bytes, target_game: Game, asset_manager: AssetManager | None = None) -> Self:
        stream = io.BytesIO(data)

        header = STRGHeader.parse_stream(stream)
        if header.version in {"prime1", "prime2"}:
            raw = cls._parse_v1(stream, header, target_game)
        else:
            raw = cls._parse_v3(stream, header, target_game)

        return Strg(raw, target_game, asset_manager)

    # Building

    def _build_v1(self, header: Container) -> bytes:
        languages = []
        string_tables = []

        current_lang_offset = 0
        for language_id, language_strings in self._raw.languages.items():
            offsets = []
            raw_strings = []

            current_strings_offset = 0
            for string in language_strings:
                offsets.append(current_strings_offset)
                raw_strings.append(CString("utf-16-be").build(string))
                current_strings_offset += len(raw_strings[-1])

            languages.append(
                Container(
                    lang=language_id,
                    offset=current_lang_offset,
                    size=current_strings_offset,
                )
            )
            current_lang_offset += current_strings_offset
            string_tables.append(
                Container(
                    size=current_strings_offset,
                    offsets=offsets,
                    raw_strings=raw_strings,
                )
            )

        return STRG_V1.build(
            Container(
                header=header,
                language_table=languages,
                name_table=self._raw.name_table,
                string_tables=string_tables,
            )
        )

    def _build_v3(self, header: Container) -> bytes:
        languages = []

        known_strings = {}
        raw_strings = []
        current_strings_offset = 0

        for language_id, language_strings in self._raw.languages.items():
            offsets = []

            language_size = 0
            for string in language_strings:
                encoded_str = CString("utf-8").build(string)
                language_size += len(encoded_str)

                if string not in known_strings:
                    raw_strings.append(string)
                    known_strings[string] = current_strings_offset
                    current_strings_offset += 4 + len(encoded_str)

                offsets.append(known_strings[string])

            languages.append(
                Container(
                    strings_size=language_size,
                    string_offsets=offsets,
                )
            )

        return STRG_V3.build(
            Container(
                header=header,
                name_table=self._raw.name_table,
                language_ids=list(self._raw.languages.keys()),
                language_table=languages,
                strings=raw_strings,
            )
        )

    def build(self) -> bytes:
        string_count = None
        for language_id, language_strings in self._raw.languages.items():
            if string_count is None:
                string_count = len(language_strings)
            else:
                assert string_count == len(language_strings)

        game_to_version = {
            Game.PRIME: "prime1",
            Game.ECHOES: "prime2",
            Game.CORRUPTION: "prime3",
        }
        header = Container(
            version=game_to_version[self.target_game],
            language_count=len(self._raw.languages),
            string_count=string_count,
        )

        # FIXME: ensure name table is sorted

        if self.target_game <= Game.ECHOES:
            return self._build_v1(header)
        else:
            return self._build_v3(header)

    # Methods

    @property
    def _raw_languages(self) -> dict[str, list[str]]:
        return self._raw.languages

    def dependencies_for(self) -> Iterator[Dependency]:
        def _str_to_deps(id_str: str):
            yield from self.asset_manager.get_dependencies_for_asset(int(id_str, 16))

        for string_list in self._raw_languages.values():
            for string in string_list:
                for match in image_regex.finditer(string):
                    ids = match.group(1).split(",")
                    for asset_id in ids:
                        yield from _str_to_deps(asset_id)
                for match in font_regex.finditer(string):
                    yield from _str_to_deps(match.group(1))

    def get_language_list(self) -> tuple[str, ...]:
        return tuple(self._raw_languages.keys())

    def get_strings(self, language: str = "ENGL") -> tuple[str, ...]:
        return tuple(self._raw_languages[language])

    def set_single_string(self, index: int, string: str, language: str | None = None) -> None:
        """
        Changes the string at the given index.
        :param index:
        :param string: The string to add.
        :param language: The language to change, or all languages if None.
        :return:
        """
        for lang, string_list in self._raw_languages.items():
            if language is None or lang == language:
                string_list[index] = string

    def set_string_list(self, string_list: list[str], language: str | None = None) -> None:
        """
        When changing the list length, make sure all languages have the same length.
        :param string_list:
        :param language: The language to change, or all languages if None.
        :return:
        """
        for lang in self._raw_languages.keys():
            if language is None or lang == language:
                self._raw_languages[lang] = list(string_list)

    @property
    def strings(self) -> tuple[str, ...]:
        return self.get_strings("ENGL")
