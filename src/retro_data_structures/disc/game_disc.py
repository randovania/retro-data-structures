from __future__ import annotations

import collections
import dataclasses
import io
import typing

import construct

from retro_data_structures.disc import disc_common
from retro_data_structures.disc.gc_disc import GcDisc
from retro_data_structures.disc.wii_disc import WiiDisc, WiiPartition
from retro_data_structures.formats import dol

if typing.TYPE_CHECKING:
    from pathlib import Path


class UnsupportedDiscFormat(Exception):
    pass


@dataclasses.dataclass
class FileEntry:
    offset: int
    size: int


FileTree: typing.TypeAlias = dict[str, typing.Union[FileEntry, "FileTree"]]


def decode_into_file_tree(fst: construct.Container) -> FileTree:
    file_tree: dict = {}
    current_dir = file_tree

    end_folder = collections.defaultdict(list)

    names_stream = io.BytesIO(fst.names)
    for i, file in enumerate(fst.file_entries):
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

    return file_tree


def encode_from_file_tree(file_tree: FileTree) -> construct.Container:
    file_entries = []
    names_blob = bytearray(b"\x00")  # offset 0 = empty root name

    def get_name_offset(name: str) -> int:
        offset = len(names_blob)
        names_blob.extend(name.encode("ascii") + b"\x00")
        return offset

    def add_entries(tree: FileTree, parent_index: int) -> None:
        for name, item in tree.items():
            name_offset = get_name_offset(name)
            if isinstance(item, FileEntry):
                file_entries.append(
                    construct.Container(
                        is_directory=False,
                        file_name=name_offset,
                        offset=item.offset,
                        param=item.size,
                    )
                )
            else:
                dir_entry_index = len(file_entries)
                file_entries.append(
                    construct.Container(
                        is_directory=True,
                        file_name=name_offset,
                        offset=parent_index,
                        param=0,  # filled in after recursion
                    )
                )
                add_entries(item, dir_entry_index)
                file_entries[dir_entry_index].param = len(file_entries)

    # Root entry at index 0
    file_entries.append(
        construct.Container(
            is_directory=True,
            file_name=0,
            offset=0,
            param=0,  # filled in after recursion
        )
    )
    add_entries(file_tree, 0)
    file_entries[0].param = len(file_entries)

    root_entry = construct.Container(
        is_directory=True,
        file_name=0,
        _offset=0,
        num_entries=len(file_entries),
    )

    return construct.Container(
        root_entry=root_entry,
        file_entries=file_entries,
        names=bytes(names_blob),
    )


MagicWordSeek = construct.Struct(construct.Seek(24), "magic_word" / construct.Int64ub)


class GameDisc:
    _raw: construct.Container
    _file_path: Path
    _file_tree: FileTree

    def __init__(self, raw: construct.Container, file_path: Path, is_wii: bool):
        self._raw = raw
        self._file_path = file_path
        self._is_wii = is_wii
        self._file_tree = decode_into_file_tree(raw.data_partition.fst)

    @classmethod
    def parse(cls, file_path: Path) -> GameDisc:
        with file_path.open("rb") as source:
            header = MagicWordSeek.parse_stream(source)
            source.seek(0)

            if header.magic_word == disc_common.WII_MAGIC_WORD:
                data = WiiDisc.parse_stream(source)
                is_wii = True
            elif header.magic_word == disc_common.GC_MAGIC_WORD:
                data = GcDisc.parse_stream(source)
                is_wii = False
            else:
                raise UnsupportedDiscFormat("Unknown disc format")

        return GameDisc(data, file_path, is_wii)

    def _get_file_entry(self, name: str) -> FileEntry:
        file_entry = self._file_tree

        try:
            for segment in name.split("/"):
                file_entry = file_entry[segment]
        except KeyError:
            raise FileNotFoundError(f"{name} does not exist")

        if isinstance(file_entry, FileEntry):
            return file_entry
        else:
            raise OSError(f"{name} is a directory")

    def files(self) -> list[str]:
        """
        Lists all files in this disc. For Wii, it's only the data partition.
        :return:
        """
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

    def _open_data_at_offset(self, offset: int, size: int) -> disc_common.DiscFileReader:
        if self._is_wii:
            assert isinstance(self._raw.data_partition, WiiPartition)
            return self._raw.data_partition.begin_read_stream(self._file_path, offset, size)
        else:
            return disc_common.DiscFileReader(self._file_path, offset, size)

    def open_binary(self, name: str) -> disc_common.DiscFileReader:
        """
        Returns an IOBase for reading a file with the given name.
        :param name:
        :return:
        """
        entry = self._get_file_entry(name)
        return self._open_data_at_offset(entry.offset, entry.size)

    def read_binary(self, name: str) -> bytes:
        """
        Returns the entire contents of the file with given name.
        :param name:
        :return:
        """
        entry = self._get_file_entry(name)
        with self._open_data_at_offset(entry.offset, entry.size) as file:
            return file.read(entry.size)

    def get_dol(self) -> bytes:
        """
        Gets the main dol for this disc. With Wii discs, returns the dol in the data partition.
        :return:
        """
        disc_header = self._raw.data_partition.disc_header
        with self._open_data_at_offset(disc_header.main_executable_offset, -1) as file:
            header = dol.DolHeader.parse_stream(file)
            dol_size = dol.calculate_size_from_header(header)

        with self._open_data_at_offset(disc_header.main_executable_offset, dol_size) as file:
            return file.read()
