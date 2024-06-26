from __future__ import annotations

import construct

from retro_data_structures.disc import disc_common

# boot.bin
GcDiscHeader = construct.Struct(
    game_code=construct.Bytes(4),
    maker_code=construct.Bytes(2),
    disc_id=construct.Int8ub,  # for multi-disc games
    version=construct.Int8ub,
    audio_streaming=construct.Int8ub,
    stream_buffer_size=construct.Int8ub,
    _unused_a=construct.Const(b"\x00" * 14),
    _wii_magic_word=construct.Const(0, construct.Int32ub),
    _gc_magic_word=construct.Const(0xC2339F3D, construct.Int32ub),
    game_name=construct.PaddedString(64, "utf8"),
    disable_hash_verification=construct.Flag,
    disable_disc_encryption=construct.Flag,
    _unused_b=construct.Const(b"\x00" * 0x39E),
    debug_monitor_offset=construct.Int32ub,
    debug_monitor_load_address=construct.Int32ub,
    _unused_c=construct.Const(b"\x00" * 24),
    main_executable_offset=construct.Int32ub,
    fst_offset=construct.Int32ub,
    fst_size=construct.Int32ub,
    fst_maximum_size=construct.Int32ub,
    fst_memory_address=construct.Int32ub,
    user_position=construct.Int32ub,
    user_length=construct.Int32ub,
    _unused_d=construct.Const(b"\x00" * 4),  # construct.Bytes(0x4),
)

assert GcDiscHeader.sizeof() == 0x0440

AppLoader = construct.Struct(
    date=construct.Aligned(16, construct.Bytes(10)),
    entry_point=construct.Hex(construct.Int32ub),
    size=construct.Rebuild(construct.Int32ub, construct.len_(construct.this.code)),
    trailer_size=construct.Int32ub,
    code=construct.Bytes(construct.this.size),
)


GcDisc = construct.Struct(
    header=construct.Peek(GcDiscHeader),
    partitions=construct.Struct(
        disc_header=GcDiscHeader,
        disc_header_info=disc_common.DiscHeaderInformation,
        app_loader=AppLoader,
        root_offset=construct.Tell,
        _fst_seek=construct.Seek(construct.this.disc_header.fst_offset),
        fst=disc_common.file_system_tree(
            construct.this.disc_header.fst_size,
            construct.Int32ub,
        ),
    )[1],
    data_partition=construct.Computed(construct.this.partitions[0]),
)
