from __future__ import annotations

import construct
from construct import Const, Int32ul, Int64ul, Struct

from retro_data_structures.common_types import FourCC

FormDescriptorHeader = Struct(
    _magic=Const(b"RFRM"),
    size=Int64ul,
    _unk=Const(0, Int64ul),
    id=FourCC,
    version=Int32ul,
    other_version=Int32ul,
)


def FormDescriptor(
    data_type: str, version: int, other_version: int, contents: construct.Construct, *, add_terminated: bool = True
):
    if add_terminated:
        contents = construct.FocusedSeq("contents", contents=contents, terminate=construct.Terminated)

    return construct.FocusedSeq(
        "form_data",
        magic=Const(b"RFRM"),
        form_data=construct.Prefixed(
            construct.FocusedSeq(
                "size",
                size=Int64ul,
                unk=Const(0, Int64ul),
                id=Const(data_type, FourCC),
                version=Const(version, Int32ul),
                other_version=Const(other_version, Int32ul),
            ),
            contents,
        ),
    )
