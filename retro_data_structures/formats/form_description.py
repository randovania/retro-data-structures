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


def FormDescription(data_type: str, version: int, other_version: int, contents: construct.Construct,
                    *, add_terminated: bool = True):
    if add_terminated:
        contents = construct.FocusedSeq("data", data=contents, terminate=construct.Terminated)

    return construct.FocusedSeq(
        "data",
        magic=Const(b"RFRM"),
        data=construct.Prefixed(
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
