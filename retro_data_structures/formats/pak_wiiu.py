import construct
from construct import Struct, Int32ul, Int64ul, PrefixedArray, Hex

from retro_data_structures.common_types import FourCC, GUID
from retro_data_structures.formats.chunk_descriptor import ChunkDescriptor
from retro_data_structures.formats.form_description import FormDescriptorHeader, FormDescription
from retro_data_structures.formats.pak_gc import PakFile

StringTableEntry = Struct(
    asset=Struct(
        type=FourCC,
        id=GUID,
    ),
    name=construct.PascalString(Int32ul, "utf8"),
)

MetadataEntry = Struct(
    id=GUID,
    offset=Int32ul,
)

AssetDirectoryEntry = Struct(
    asset=Struct(
        type=FourCC,
        id=GUID,
    ),
    unk1=Hex(Int32ul),
    unk2=Hex(Int32ul),
    offset=Hex(Int64ul),
    decompressed_size=Hex(Int64ul),
    size=Hex(Int64ul),
)

TOCCChunkDescriptor = ChunkDescriptor(
    {
        "ADIR": PrefixedArray(Int32ul, AssetDirectoryEntry),
        "META": PrefixedArray(Int32ul, MetadataEntry),
        "STRG": PrefixedArray(Int32ul, StringTableEntry),
    },
).compile()

TOCC = FormDescription(
    "TOCC", 3, construct.ExprAdapter(
        construct.GreedyRange(TOCCChunkDescriptor),
        lambda obj, ctx: construct.Container((chunk.id, chunk) for chunk in obj),
        lambda obj, ctx: construct.ListContainer(obj.values()),
    ), other_version=3,
)

PakWiiU = FormDescription(
    "PACK", 1, Struct(
        tocc=TOCC,
        remain=construct.GreedyBytes,
    ), other_version=0,
)

PakWiiUNoData = Struct(
    header=FormDescriptorHeader,
    tocc=TOCC,
    resources=construct.Computed(construct.this.tocc.ADIR.data),
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
