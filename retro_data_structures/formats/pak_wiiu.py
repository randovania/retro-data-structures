import construct
from construct import Struct, Int32ul, Int64ul, PrefixedArray, Array

from retro_data_structures.common_types import FourCC, AssetId128

RFRMHeader = Struct(
    magic=Int32ul,
    data_size=Int64ul,
    unk1=Int64ul,
    type=FourCC,
    unk2=Int32ul,
    unk3=Int32ul,
)

ADIRHeader = Struct(
    magic=Int32ul,
    data_size=Int64ul,
    unk1=Int32ul,
    unk2=Int32ul,
    unk3=Int32ul,
    entry_count=Int32ul,
)

Resource = Struct(
    asset=Struct(
        type=FourCC,
        id=AssetId128,
    ),
    offset=Int64ul,
    size=Int64ul,
    unk1=Int64ul,
    unk2=Int64ul,
)

Meta = Struct(
    type=FourCC,
    section_size=Int64ul,
    unk1=Int32ul,
    unk2=Int32ul,
    unk3=Int32ul,
    entries=PrefixedArray(
        Int32ul,
        Struct(
            id1=Int64ul,
            id2=Int64ul,
            offset=Int32ul,
        )
    )
)

ConstructPakWiiU = Struct(
    PAK=RFRMHeader,
    TOCC=RFRMHeader,
    ADIR=ADIRHeader,
    resources=Array(
        construct.this.ADIR.entry_count,
        Resource,
    ),
    meta=Meta,
)
