from __future__ import annotations

import construct
from construct import Const, Int32ul, Int64ul, Struct

from retro_data_structures.common_types import FourCC
from retro_data_structures.construct_extensions.misc import ErrorWithMessage


def ChunkDescriptor(data_types: dict[str, construct.Construct]):
    return Struct(
        id=FourCC,
        data=construct.Prefixed(
            construct.FocusedSeq(
                "size",
                size=Int64ul,
                unk=Const(1, Int32ul),
                skip=Const(0, Int64ul),  # TODO: support skip, but this is unused in remastered?
            ),
            construct.FocusedSeq(
                "chunk_item",
                chunk_item=construct.Switch(
                    construct.this._.id,
                    data_types,
                    ErrorWithMessage(lambda ctx: f"Unknown type: {ctx.id}"),
                ),
                terminate=construct.Terminated,
            ),
        ),
    )


def SingleTypeChunkDescriptor(type_name: str, contents: construct.Construct, *, add_terminated: bool = True):
    if add_terminated:
        contents = construct.FocusedSeq("data", data=contents, terminate=construct.Terminated)

    return construct.FocusedSeq(
        "data",
        id=Const(type_name, FourCC),
        data=construct.Prefixed(
            construct.FocusedSeq(
                "size",
                size=Int64ul,
                unk=Const(1, Int32ul),
                skip=Const(0, Int64ul),  # TODO: support skip, but this is unused in remastered?
            ),
            contents,
        ),
    )
