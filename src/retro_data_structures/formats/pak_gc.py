from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

import construct
from construct import Const, FocusedSeq, IfThenElse, Int16ub, Int32ub, PascalString, PrefixedArray, Rebuild, Struct

from retro_data_structures import game_check
from retro_data_structures.base_resource import AssetId, AssetType, Dependency
from retro_data_structures.common_types import AssetId32, FourCC
from retro_data_structures.compression import LZOCompressedBlock, ZlibCompressedBlock
from retro_data_structures.construct_extensions.alignment import AlignTo

if TYPE_CHECKING:
    from retro_data_structures.game_check import Game

PAKHeader = Struct(
    version_major=Const(3, Int16ub),
    version_minor=Const(5, Int16ub),
    unused=Const(0, Int32ub),
)
ConstructResourceHeader = Struct(
    compressed=Int32ub,
    asset_type=FourCC,
    asset_id=AssetId32,
    size=Int32ub,
    offset=Int32ub,
)


def _emitparse_header(code: construct.CodeGen) -> str:
    code.append("ResourceHeader_Format = struct.Struct('>LLLLL')")
    code.append(
        """def _create_resource_header(compressed, asset_type, asset_id, size, offset):
    return Container(compressed=compressed, asset_type=asset_type.to_bytes(4, "big").decode("ascii"),
                     asset_id=asset_id, size=size, offset=offset)
    """
    )
    return "_create_resource_header(*ResourceHeader_Format.unpack(io.read(20)))"


ConstructResourceHeader._emitparse = _emitparse_header

PAKNoData = Struct(
    _header=PAKHeader,
    named_resources=PrefixedArray(
        Int32ub,
        Struct(
            asset_type=FourCC,
            asset_id=AssetId32,
            name=PascalString(Int32ub, "utf-8"),
        ),
    ),
    resources=PrefixedArray(Int32ub, ConstructResourceHeader),
).compile()

CompressedPakResource = FocusedSeq(
    "data",
    decompressed_size=Rebuild(Int32ub, construct.len_(construct.this.data)),
    data=IfThenElse(
        game_check.uses_lzo,
        LZOCompressedBlock(construct.this.decompressed_size),
        ZlibCompressedBlock,
    ),
)


@dataclasses.dataclass
class PakFile:
    asset_id: AssetId
    asset_type: AssetType
    should_compress: bool
    uncompressed_data: bytes | None
    compressed_data: bytes | None
    extra: construct.Container | None = None

    def get_decompressed(self, target_game: Game) -> bytes:
        if self.uncompressed_data is None:
            self.uncompressed_data = CompressedPakResource.parse(
                self.compressed_data,
                target_game=target_game,
            )

        return self.uncompressed_data

    def get_compressed(self, target_game: Game) -> bytes:
        if self.compressed_data is None:
            self.compressed_data = CompressedPakResource.build(
                self.uncompressed_data,
                target_game=target_game,
            )

        return self.compressed_data

    def set_new_data(self, data: bytes):
        self.uncompressed_data = data
        self.compressed_data = None


@dataclasses.dataclass
class PakBody:
    named_resources: dict[str, Dependency]
    files: list[PakFile]


class ConstructPakGc(construct.Construct):
    def _parse(self, stream, context, path) -> PakBody:
        header = PAKNoData._parsereport(stream, context, f"{path} -> header")

        AlignTo(32)._parse(stream, context, path)

        files = []
        for i, resource in enumerate(header.resources):
            if resource.offset != construct.stream_tell(stream, path):
                raise construct.ConstructError(f"Expected resource at {resource.offset}", path)

            data = construct.stream_read(stream, resource.size, path)
            # TODO: There's some padding here
            if resource.compressed > 0:
                uncompressed_data = None
                compressed_data = data
            else:
                uncompressed_data = data
                compressed_data = None

            files.append(
                PakFile(
                    resource.asset_id,
                    resource.asset_type,
                    resource.compressed > 0,
                    uncompressed_data,
                    compressed_data,
                )
            )

        return PakBody(
            named_resources={
                named.name: Dependency(type=named.asset_type, id=named.asset_id) for named in header.named_resources
            },
            files=files,
        )

    def _build(self, obj: PakBody, stream, context, path):
        assert isinstance(obj, PakBody)

        header = construct.Container(
            _header=construct.Container(),
            named_resources=construct.ListContainer(
                construct.Container(
                    asset_type=dep.type,
                    asset_id=dep.id,
                    name=name,
                )
                for name, dep in obj.named_resources.items()
            ),
            resources=construct.ListContainer(
                construct.Container(
                    compressed=0,
                    asset_type=file.asset_type,
                    asset_id=file.asset_id,
                    size=0,
                    offset=0,
                )
                for file in obj.files
            ),
        )

        header_start = construct.stream_tell(stream, path)
        PAKNoData._build(header, stream, context, path)
        AlignTo(32)._build(None, stream, context, path)

        for i, file in enumerate(obj.files):
            compressed = file.should_compress
            if compressed:
                data = file.get_compressed(game_check.get_current_game(context))
            else:
                data = file.get_decompressed(game_check.get_current_game(context))

            # TODO: don't compress if it ends up bigger
            # if len(data) > len(file.data):
            #     compressed = False
            #     data = file.data

            pad = 32 - (len(data) % 32)
            if pad < 32:
                data += b"\xff" * pad

            header.resources[i].offset = construct.stream_tell(stream, path)
            header.resources[i].size = len(data)
            header.resources[i].compressed = int(compressed)
            construct.stream_write(stream, data, len(data), path)

        # Update header
        files_end = construct.stream_tell(stream, path)
        construct.stream_seek(stream, header_start, 0, path)
        PAKNoData._build(header, stream, context, path)
        construct.stream_seek(stream, files_end, 0, path)


PAK_GC = ConstructPakGc()
