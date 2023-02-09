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
        size=Int64ul,
        unk=Int64ul,
        id=Const(data_type, FourCC),
        version=Const(version, Int32ul),
        other_version=Int32ul,
        data=construct.FixedSized(construct.this.size, contents),
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

PakWiiU = FormDescription(
    "PACK", 1, Struct(
        tocc=FormDescription(
            "TOCC", 3, construct.ExprAdapter(
                construct.GreedyRange(ChunkDescriptor),
                lambda obj, ctx: construct.Container((chunk.id, chunk) for chunk in obj),
                lambda obj, ctx: construct.ListContainer(obj.values()),
            ),
        ),
        remain=construct.GreedyBytes,
    ),
)

PakWiiUNoData = Struct(
    resources=construct.ExprAdapter(
        PakWiiU,
        lambda obj, ctx: obj.data.tocc.data.ADIR.data,
        lambda obj, ctx: None,
    )
)


class ConstructPakWiiU(construct.Construct):
    def _parse(self, stream, context, path):
        header = PakWiiU._parsereport(stream, context, f"{path} -> header")

        files = []
        for i, resource in enumerate(header.resources):
            if resource.offset != construct.stream_tell(stream, path):
                raise construct.ConstructError(
                    f"Expected resource at {resource.offset}, was at {construct.stream_tell(stream, path)}", path)

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
