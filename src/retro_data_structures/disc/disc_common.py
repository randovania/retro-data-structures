from __future__ import annotations

import io
import os
import typing
from pathlib import Path

import construct

DiscHeaderInformation = construct.Struct(
    debug_monitor_size=construct.Int32ub,
    simulated_memory_size=construct.Int32ub,
    argument_offset=construct.Int32ub,
    debug_flag=construct.Int32ub,
    track_address=construct.Int32ub,
    track_size=construct.Int32ub,
    country_code=construct.Int32ub,
    unknown1=construct.Int32ub,
    unknown2=construct.Int32ub,
    unknown3=construct.Int32ub,
    dol_limit=construct.Int32ub,
    unknown4=construct.Int32ub,
    padding=construct.Padding(8144),
)
assert DiscHeaderInformation.sizeof() == 0x2000

RootFileEntry = construct.Struct(
    is_directory=construct.Const(True, construct.Flag),
    file_name=construct.Const(0, construct.Int24ub),
    _offset=construct.Const(0, construct.Int32ub),
    num_entries=construct.Int32ub,
)


def file_system_tree(length: typing.Callable, offset_type: construct.Construct) -> construct.Construct:
    """
    Creates a Construct for parsing the FST of a Gc Disc or Wii Disc Partition

    :param length: Path to the entry with the length of fst, in bytes.
    :param offset_type: Construct for offset field of the file entries.
    :return:
    """
    file_entry = construct.Struct(
        is_directory=construct.Flag,
        file_name=construct.Int24ub,
        offset=offset_type,
        param=construct.Int32ub,
    )

    return construct.FixedSized(
        length,
        construct.Struct(
            root_entry=construct.Peek(RootFileEntry),
            file_entries=file_entry[construct.this.root_entry.num_entries],
            names=construct.GreedyBytes,
        ),
    )


class DiscFileReader(io.IOBase):
    _file: typing.BinaryIO

    def __init__(self, file_path: Path | typing.BinaryIO, base_offset: int, size: int):
        if isinstance(file_path, Path):
            self._file = file_path.open("rb")
        else:
            self._file = file_path

        self._base_offset = base_offset
        self._size = size

        self._file.seek(self._base_offset)

    def read(self, size: int = -1) -> bytes:
        if size == -1:
            size = self._size

        if 0 < self._size < size + self.tell():
            size -= self.tell()
        return self._file.read(size)

    def seek(self, offset: int, whence: int = os.SEEK_SET, /) -> None:
        if whence == os.SEEK_CUR:
            self._file.seek(offset, os.SEEK_CUR)
            return

        if whence == os.SEEK_END:
            offset += self._size

        self._file.seek(self._base_offset + offset)

    def tell(self) -> int:
        return self._file.tell() - self._base_offset

    def writable(self) -> bool:
        return False

    def __enter__(self) -> typing.Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def close(self) -> None:
        super().close()
        self._file.close()


class ShiftedInteger(construct.Adapter):
    """
    An int, shifted by 2 after parsing. Used in Wii addresses and offsets.
    """

    def _decode(self, obj, context, path):
        return obj << 2

    def _encode(self, obj, context, path):
        return obj >> 2


ShiftedOnWii = construct.IfThenElse(construct.this.is_wii, ShiftedInteger(construct.Int32ub), construct.Int32ub)
ShiftedOnWii._sizeof = lambda context, path: construct.Int32ub._sizeof(context, path)

WII_MAGIC_WORD = 0x5D1C9EA300000000
GC_MAGIC_WORD = 0x00000000C2339F3D

DiscHeader = construct.Struct(
    game_code=construct.PaddedString(4, "ascii"),
    maker_code=construct.PaddedString(2, "ascii"),
    disc_id=construct.Int8ub,  # for multi-disc games
    version=construct.Int8ub,
    audio_streaming=construct.Int8ub,
    stream_buffer_size=construct.Int8ub,
    _unused_a=construct.Const(b"\x00" * 14),
    _magic_words=construct.OneOf(construct.Int64ub, {WII_MAGIC_WORD, GC_MAGIC_WORD}),
    is_wii=construct.Computed(construct.this._magic_words == WII_MAGIC_WORD),
    game_name=construct.PaddedString(64, "utf8"),
    disable_hash_verification=construct.Flag,
    disable_disc_encryption=construct.Flag,
    _unused_b=construct.Const(b"\x00" * 0x39E),
    debug_monitor_offset=construct.Int32ub,
    debug_monitor_load_address=construct.Int32ub,
    _unused_c=construct.Const(b"\x00" * 24),
    main_executable_offset=ShiftedOnWii,
    fst_offset=ShiftedOnWii,
    fst_size=ShiftedOnWii,
    fst_maximum_size=construct.Int32ub,
    fst_memory_address=construct.Int32ub,
    user_position=construct.Int32ub,
    user_length=construct.Int32ub,
    _unused_d=construct.Const(b"\x00" * 4),  # construct.Bytes(0x4),
)
assert DiscHeader.sizeof() == 0x0440
