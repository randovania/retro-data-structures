import typing

import construct
from construct import Struct, Int32ul, Int64ul, Const

from retro_data_structures.common_types import FourCC
from retro_data_structures.construct_extensions.misc import ErrorWithMessage


def ChunkDescriptor(data_types: typing.Dict[str, construct.Construct]):
    return Struct(
        id=FourCC,
        size=Int64ul,
        unk=Const(1, Int32ul),
        skip=Const(0, Int64ul),  # TODO: support skip, but this is unused in remastered?
        data=construct.FixedSized(
            construct.this.size,
            construct.Switch(
                construct.this.id,
                data_types,
                ErrorWithMessage(lambda ctx: f"Unknown type: {ctx.id}"),
            )
        ),
    )


def SingleTypeChunkDescriptor(type_name: str, contents: construct.Construct, *, add_terminated: bool = True):
    if add_terminated:
        contents = construct.FocusedSeq("data", data=contents, terminate=construct.Terminated)

    return construct.FocusedSeq(
        "data",
        id=Const(type_name, FourCC),
        size=Int64ul,
        unk=Const(1, Int32ul),
        skip=Const(0, Int64ul),  # TODO: support skip, but this is unused in remastered?
        data=construct.FixedSized(construct.this.size, contents),
    )
