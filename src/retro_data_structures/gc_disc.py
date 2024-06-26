from __future__ import annotations

import construct

# boot.bin
DiscHeader = construct.Struct(
    game_code=construct.Bytes(4),
    maker_code=construct.Bytes(2),
    disc_id=construct.Int8ub,  # for multi-disc games
    version=construct.Int8ub,
    audio_streaming=construct.Int8ub,
    stream_buffer_size=construct.Int8ub,
    _unused_a=construct.Const(b"\x00" * 14),
    _wii_magic_word=construct.Const(0, construct.Int32ub),  # 0x5D1C9EA3
    _gc_magic_word=construct.Const(0xC2339F3D, construct.Int32ub),
    game_name=construct.PaddedString(0x3E0, "utf8"),
    debug_monitor_offset=construct.Int32ub,
    debug_monitor_load_address=construct.Int32ub,
    _unused_b=construct.Const(b"\x00" * 24),
    main_executable_offset=construct.Int32ub,
    fst_offset=construct.Int32ub,
    fst_size=construct.Int32ub,
    fst_maximum_size=construct.Int32ub,
    user_position=construct.Int32ub,
    user_length=construct.Int32ub,
    unknown=construct.Int32ub,
    _unused_c=construct.Const(b"\x00" * 4),  # construct.Bytes(0x4),
)
assert DiscHeader.sizeof() == 0x0440

DiscHeaderInformation = construct.Struct(
    debug_monitor_size=construct.Int32ub,
    simulated_memory_size=construct.Int32ub,
    argument_offset=construct.Int32ub,
    debug_flag=construct.Int32ub,
    track_address=construct.Int32ub,
    track_size=construct.Int32ub,
    country_code=construct.Int32ub,
    unknown=construct.Int32ub,
    padding=construct.Bytes(8160),
)
assert DiscHeaderInformation.sizeof() == 0x2000

AppLoader = construct.Struct(
    date=construct.Aligned(16, construct.Bytes(10)),
    entry_point=construct.Hex(construct.Int32ub),
    _size=construct.Rebuild(construct.Int32ub, construct.len_(construct.this.code)),
    trailer_size=construct.Int32ub,
    code=construct.Bytes(construct.this._size),
)

FileEntry = construct.Struct(
    is_directory=construct.Flag,
    file_name=construct.Int24ub,
    offset=construct.Int32ub,
    param=construct.Int32ub,
)
RootFileEntry = construct.Struct(
    is_directory=construct.Const(True, construct.Flag),
    file_name=construct.Const(0, construct.Int24ub),
    _offset=construct.Const(0, construct.Int32ub),
    num_entries=construct.Int32ub,
)

GcDisc = construct.Struct(
    header=DiscHeader,
    header_information=DiscHeaderInformation,
    app_loader=AppLoader,
    root_offset=construct.Tell,
    _fst_seek=construct.Seek(construct.this.header.fst_offset),
    fst=construct.FixedSized(
        construct.this.header.fst_size,
        construct.Struct(
            root_entry=construct.Peek(RootFileEntry),
            file_entries=FileEntry[construct.this.root_entry.num_entries],
            names=construct.GreedyBytes,
        ),
    ),
)
