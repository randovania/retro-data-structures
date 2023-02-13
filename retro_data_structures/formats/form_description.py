import typing

import construct
from construct import Struct, Const, Int64ul, Int32ul

from retro_data_structures.common_types import FourCC

FormDescriptorHeader = Struct(
    magic=Const(b"RFRM"),
    size=Int64ul,
    unk=Int64ul,
    id=FourCC,
    version=Int32ul,
    other_version=Int32ul,
)


def FormDescription(data_type: str, version: int, contents: construct.Construct,
                    *, add_terminated: bool = True, other_version: typing.Optional[int] = None):
    if add_terminated:
        contents = construct.FocusedSeq("data", data=contents, terminate=construct.Terminated)

    if other_version is not None:
        other_version_con = Const(other_version, Int32ul)

        def create(**kwargs):
            return construct.FocusedSeq(
                "data",
                **kwargs,
            )
    else:
        other_version_con = Int32ul

        def create(**kwargs):
            return Struct(**kwargs)

    return create(
        magic=Const(b"RFRM"),
        size=construct.Rebuild(Int64ul, construct.len_(construct.this.data)),
        unk=Const(0, Int64ul),
        id=Const(data_type, FourCC),
        version=Const(version, Int32ul),
        other_version=other_version_con,
        data=construct.FixedSized(construct.this.size, contents),
    )
