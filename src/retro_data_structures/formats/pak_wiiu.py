from __future__ import annotations

import math

import construct
from construct import Hex, Int32ul, Int64ul, PrefixedArray, Struct

from retro_data_structures.common_types import GUID, FourCC
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.construct_extensions.misc import UntilEof
from retro_data_structures.formats.chunk_descriptor import ChunkDescriptor
from retro_data_structures.formats.form_descriptor import FormDescriptor, FormDescriptorHeader
from retro_data_structures.formats.pak_gc import PakFile

StringTableEntry = Struct(
    asset_type=FourCC,
    asset_id=GUID,
    name=construct.PascalString(Int32ul, "utf8"),
)

MetadataEntry = Struct(
    id=GUID,
    offset=Int32ul,
)

AssetDirectoryEntry = Struct(
    asset_type=FourCC,
    asset_id=GUID,
    version_a=Hex(Int32ul),
    version_b=Hex(Int32ul),
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

TOCC = FormDescriptor(
    "TOCC",
    3,
    3,
    construct.ExprAdapter(
        UntilEof(TOCCChunkDescriptor),
        lambda obj, ctx: construct.Container((chunk.id, chunk) for chunk in obj),
        lambda obj, ctx: construct.ListContainer(obj.values()),
    ),
)

PakWiiU = FormDescriptor(
    "PACK",
    1,
    0,
    Struct(
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
            #         f"Resource {i} ({resource.asset_id} {resource.asset_type}), is compressed", path)

            construct.stream_seek(stream, resource.offset, 0, path)
            data = construct.stream_read(stream, resource.size, path)
            files.append(
                PakFile(
                    resource.asset_id,
                    resource.asset_type,
                    False,
                    data,
                    None,
                    extra=construct.Container(
                        version_a=resource.version_a,
                        version_b=resource.version_b,
                        offset=resource.offset,
                        decompressed_size=resource.decompressed_size,
                    ),
                )
            )
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
                    asset_type=file.asset_type,
                    asset_id=file.asset_id,
                    version_a=file.extra.version_a,
                    version_b=file.extra.version_b,
                    offset=0,
                    decompressed_size=file.extra.get("decompressed_size", len(file.get_decompressed(game))),
                    size=len(file.get_decompressed(game)),
                )
                for file in sorted(files, key=lambda it: it.asset_id)
            ),
        )

        header_start = construct.stream_tell(stream, path)
        PakWiiUNoData._build(obj.header, stream, context, f"{path} -> header")

        for i, (adir, file) in enumerate(
            sorted(zip(tocc.ADIR.data, files), key=lambda it: it[1].extra.offset or math.inf)
        ):
            adir.offset = construct.stream_tell(stream, f"{path} -> file[{i}]")
            data = file.get_decompressed(game)
            construct.stream_write(stream, data, len(data), f"{path} -> file[{i}]")

        AlignTo(32)._build(None, stream, context, path)

        # Update header
        files_end = construct.stream_tell(stream, path)
        construct.stream_seek(stream, header_start, 0, path)
        PakWiiUNoData._build(obj.header, stream, context, path)
        construct.stream_seek(stream, files_end, 0, path)


PAK_WIIU = ConstructPakWiiU()
