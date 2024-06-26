from __future__ import annotations

import collections
import dataclasses
import io
import typing

import construct

from retro_data_structures.formats import dol
from retro_data_structures.gc_disc import GcDisc

if typing.TYPE_CHECKING:
    from pathlib import Path


@dataclasses.dataclass
class FileEntry:
    offset: int
    size: int


FileTree: typing.TypeAlias = dict[str, typing.Union[FileEntry, "FileTree"]]


class GameDisc:
    _file_path: Path
    _raw: construct.Container
    _file_tree: FileTree

    def __init__(self, file_path: Path, raw: construct.Container, file_tree: FileTree):
        self._file_path = file_path
        self._raw = raw
        self._file_tree = file_tree

    @classmethod
    def parse(cls, file_path: Path) -> GameDisc:
        with file_path.open("rb") as source:
            data = GcDisc.parse_stream(source)

        file_tree: dict = {}
        current_dir = file_tree

        end_folder = collections.defaultdict(list)

        names_stream = io.BytesIO(data.fst.names)
        for i, file in enumerate(data.fst.file_entries):
            if i == 0:
                continue

            if i in end_folder:
                current_dir = end_folder.pop(i)[0]

            names_stream.seek(file.file_name)
            name = construct.CString("ascii").parse_stream(names_stream)
            if file.is_directory:
                new_dir = {}
                end_folder[file.param].append(current_dir)
                current_dir[name] = new_dir
                current_dir = new_dir
            else:
                current_dir[name] = FileEntry(
                    offset=file.offset,
                    size=file.param,
                )

        return GameDisc(file_path, data, file_tree)

    def _get_file_entry(self, name: str) -> FileEntry:
        file_entry = self._file_tree
        for segment in name.split("/"):
            file_entry = file_entry[segment]

        if isinstance(file_entry, FileEntry):
            return file_entry
        else:
            raise OSError(f"{name} is a directory")

    def files(self) -> list[str]:
        result = []

        def recurse(parent: str, tree: FileTree) -> None:
            for key, item in tree.items():
                name = f"{parent}/{key}" if parent else key

                if isinstance(item, FileEntry):
                    result.append(name)
                else:
                    recurse(name, item)

        recurse("", self._file_tree)
        return result

    def open_binary(self, name: str) -> typing.BinaryIO:
        entry = self._get_file_entry(name)
        file = self._file_path.open("rb")
        file.seek(entry.offset)
        return file

    def read_binary(self, name: str) -> bytes:
        entry = self._get_file_entry(name)
        with self._file_path.open("rb") as file:
            file.seek(entry.offset)
            return file.read(entry.size)

    def get_dol(self) -> bytes:
        with self._file_path.open("rb") as file:
            file.seek(self._raw.header.main_executable_offset)
            header = dol.DolHeader.parse_stream(file)
            dol_size = dol.calculate_size_from_header(header)
            file.seek(self._raw.header.main_executable_offset)
            return file.read(dol_size)
