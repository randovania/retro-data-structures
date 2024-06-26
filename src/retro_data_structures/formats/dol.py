from __future__ import annotations

import construct

DolHeader = construct.Struct(
    text_offset=construct.Int32ub[7],
    data_offset=construct.Int32ub[11],
    text_base_address=construct.Int32ub[7],
    data_base_address=construct.Int32ub[11],
    text_size=construct.Int32ub[7],
    data_size=construct.Int32ub[11],
    bss_start=construct.Int32ub,
    bss_size=construct.Int32ub,
    entrypoint=construct.Int32ub,
)


def calculate_size_from_header(header: construct.Container) -> int:
    result = header.text_offset[0]
    for size in header.text_size:
        result += size
    for size in header.data_size:
        result += size
    return result
