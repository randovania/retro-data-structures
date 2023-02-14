import construct
from construct import Struct, Int32ul, Int64ul, PrefixedArray, Hex

from retro_data_structures.common_types import FourCC, GUID
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.construct_extensions.misc import UntilEof
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
        "META": Struct(
            entries=PrefixedArray(Int32ul, MetadataEntry),
            entry_data=construct.GreedyBytes,
        ),
        "STRG": PrefixedArray(Int32ul, StringTableEntry),
    },
)

TOCC = FormDescription(
    "TOCC", 3, 3, construct.ExprAdapter(
        UntilEof(TOCCChunkDescriptor),
        lambda obj, ctx: construct.Container((chunk.id, chunk) for chunk in obj),
        lambda obj, ctx: construct.ListContainer(obj.values()),
    ),
)

PakWiiU = FormDescription(
    "PACK", 1, 0, Struct(
        tocc=TOCC,
        remain=construct.GreedyBytes,
    ),
)

PakWiiUNoData = Struct(
    header=FormDescriptorHeader,
    tocc=TOCC,
    resources=construct.Computed(lambda ctx: ctx.tocc.ADIR.data),
)


class ConstructPakWiiU(construct.Construct):
    def _parse(self, stream, context, path):
        header = PakWiiUNoData._parsereport(stream, context, f"{path} -> header")

        files = construct.ListContainer()

        last = construct.stream_tell(stream, path)

        for i, resource in enumerate(header.tocc.ADIR.data):
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
            last = max(last, construct.stream_tell(stream, path))

        construct.stream_seek(stream, last, 0, path)
        AlignTo(32)._parsereport(stream, context, path)
        construct.Terminated._parsereport(stream, context, path)

        return construct.Container(
            header=header,
            files=files,
        )

    def _build(self, obj, stream, context, path):
        files: list[PakFile] = obj.files
        game = context["target_game"]

        tocc = obj.header.tocc
        tocc.ADIR = construct.Container(
            id="ADIR",
            data=construct.ListContainer(
                construct.Container(
                    asset=construct.Container(
                        type=file.asset_type,
                        id=file.asset_id,
                    ),
                    unk1=147,
                    unk2=160,
                    offset=0,
                    decompressed_size=len(file.get_decompressed(game)),
                    size=len(file.get_decompressed(game)),
                )
                for file in files
            )
        )

        header_start = construct.stream_tell(stream, path)
        PakWiiUNoData._build(obj.header, stream, context, f"{path} -> header")

        for i, file in enumerate(files):
            tocc.ADIR.data[i].offset = construct.stream_tell(stream, f"{path} -> file[{i}]")
            data = file.get_decompressed(game)
            construct.stream_write(stream, data, len(data), f"{path} -> file[{i}]")

        AlignTo(32)._build(None, stream, context, path)

        # Update header
        files_end = construct.stream_tell(stream, path)
        construct.stream_seek(stream, header_start, 0, path)
        PakWiiUNoData._build(obj.header, stream, context, path)
        construct.stream_seek(stream, files_end, 0, path)


PAK_WIIU = ConstructPakWiiU()
