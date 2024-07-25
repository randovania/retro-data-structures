from __future__ import annotations

import construct

from retro_data_structures.disc import disc_common
from retro_data_structures.disc.disc_common import DiscHeader

AppLoader = construct.Struct(
    date=construct.Aligned(16, construct.Bytes(10)),
    entry_point=construct.Hex(construct.Int32ub),
    size=construct.Rebuild(construct.Int32ub, construct.len_(construct.this.code)),
    trailer_size=construct.Int32ub,
    code=construct.Bytes(construct.this.size),
)


GcDisc = construct.Struct(
    header=construct.Peek(DiscHeader),
    partitions=construct.Struct(
        disc_header=DiscHeader,  # boot.bin
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
