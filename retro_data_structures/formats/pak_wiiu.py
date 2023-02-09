import construct
from construct import Struct, Int32ul, Int64ul, PrefixedArray, Hex, Const

from retro_data_structures.common_types import FourCC, AssetId128
from retro_data_structures.formats.pak_gc import PakFile

FormDescriptorHeader = Struct(
    magic=Const("RFRM", FourCC),
    size=Int64ul,
    unk=Int64ul,
    id=FourCC,
    version=Int32ul,
    other_version=Int32ul,
)


def FormDescription(data_type: str, version: int, contents: construct.Construct):
    return Struct(
        magic=Const("RFRM", FourCC),
        _size=construct.Rebuild(Int64ul, construct.len_(construct.this.data)),
        unk=Int64ul,
        id=Const(data_type, FourCC),
        version=Const(version, Int32ul),
        other_version=Int32ul,
        data=construct.FixedSized(construct.this._size, contents),
    )


StringTableEntry = Struct(
    asset=Struct(
        type=FourCC,
        id=AssetId128,
    ),
    name=construct.PascalString(Int32ul, "utf8"),
)

MetadataEntry = Struct(
    id=AssetId128,
    offset=Int32ul,
)

AssetDirectoryEntry = Struct(
    asset=Struct(
        type=FourCC,
        id=AssetId128,
    ),
    unk1=Hex(Int32ul),
    unk2=Hex(Int32ul),
    offset=Hex(Int64ul),
    decompressed_size=Hex(Int64ul),
    size=Hex(Int64ul),
)

ChunkDescriptor = Struct(
    id=FourCC,
    size=Int64ul,
    unk=Int32ul,
    skip=Const(0, Int64ul),  # TODO: support skip, but this is unused in remastered?
    data=construct.FixedSized(
        construct.this.size,
        construct.Switch(
            construct.this.id,
            {
                "ADIR": PrefixedArray(Int32ul, AssetDirectoryEntry),
                "META": PrefixedArray(Int32ul, MetadataEntry),
                "STRG": PrefixedArray(Int32ul, StringTableEntry),
            },
            construct.GreedyBytes,
        )
    ),
)

TOCC = FormDescription(
    "TOCC", 3, construct.ExprAdapter(
        construct.GreedyRange(ChunkDescriptor),
        lambda obj, ctx: construct.Container((chunk.id, chunk) for chunk in obj),
        lambda obj, ctx: construct.ListContainer(obj.values()),
    ),
)

PakWiiU = FormDescription(
    "PACK", 1, Struct(
        tocc=TOCC,
        remain=construct.GreedyBytes,
    ),
)

PakWiiUNoData = Struct(
    header=FormDescriptorHeader,
    tocc=TOCC,
    resources=construct.Computed(construct.this.tocc.data.ADIR.data),
)


class ConstructPakWiiU(construct.Construct):
    def _parse(self, stream, context, path):
        header = PakWiiUNoData._parsereport(stream, context, f"{path} -> header")

        files = []
        for i, resource in enumerate(header.resources):
            # if resource.decompressed_size != resource.size:
            #     raise construct.ConstructError(
            #         f"Resource {i} ({resource.asset.id} {resource.asset.type}), is compressed", path)

            construct.stream_seek(stream, resource.offset, 0, path)
            data = construct.stream_read(stream, resource.size, path)
            files.append(PakFile(
                resource.asset.id,
                resource.asset.type,
                False,
                data,
                None,
            ))

        return construct.Container(
            header=header,
            files=files,
        )


PAK_WIIU = ConstructPakWiiU()
