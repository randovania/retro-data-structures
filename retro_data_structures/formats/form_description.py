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


def FormDescription(data_type: str, version: int, contents: construct.Construct):
    return Struct(
        magic=Const(b"RFRM"),
        size=construct.Rebuild(Int64ul, construct.len_(construct.this.data)),
        unk=Int64ul,
        id=Const(data_type, FourCC),
        version=Const(version, Int32ul),
        other_version=Int32ul,
        data=construct.FixedSized(construct.this.size, contents),
    )
