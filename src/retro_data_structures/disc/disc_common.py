from __future__ import annotations

import typing

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
