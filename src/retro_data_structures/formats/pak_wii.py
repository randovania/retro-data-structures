from __future__ import annotations

import construct
from construct import Bytes, Const, Int32ub, PrefixedArray, Struct, FocusedSeq, Rebuild, IfThenElse

from typing import TYPE_CHECKING

import dataclasses

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC, String, AssetId64
from retro_data_structures.base_resource import AssetId, AssetType, Dependency
from retro_data_structures.compression import LZOCompressedBlock, ZlibCompressedBlock
from retro_data_structures.construct_extensions.dict import make_dict
from retro_data_structures.construct_extensions.alignment import AlignTo

if TYPE_CHECKING:
    from retro_data_structures.game_check import Game

PAKHeader = construct.Aligned(
    64,
    Struct(
        version=Const(2, Int32ub),
        header_size=Int32ub,
        md5_hash=Bytes(16),
    ),
)

ConstructResourceHeader = Struct(
    compressed=Int32ub,
    asset_type=FourCC,
    asset_id=AssetId64,
    size=Int32ub,
    offset=Int32ub,
)


def _emitparse_header(code: construct.CodeGen) -> str:
    code.append("ResourceHeader_Format = struct.Struct('>LLQLL')")
    code.append(
        """def _create_resource_header(compressed, asset_type, asset_id, size, offset):
    return Container(compressed=compressed, asset_type=asset_type.to_bytes(4, "big").decode("ascii"),
                     asset_id=asset_id, size=size, offset=offset)
    """
    )
    return "_create_resource_header(*ResourceHeader_Format.unpack(io.read(24)))"


ConstructResourceHeader._emitparse = _emitparse_header

PAKNoData = Struct(
    _start=construct.Tell,      # Should always be 0x00
    _header=PAKHeader,
    _table_of_contents_start=construct.Tell,        #  Should always be 0x40
    table_of_contents=construct.Aligned(64, make_dict(Int32ub, FourCC)),
    # Usually starts at 0x80, though ToC semantically has a dynamic length
    _named_resources_start=construct.Tell,      
    named_resources=construct.Aligned(
        64,
        PrefixedArray(
            Int32ub,
            Struct(
                name=String,
                asset_type=FourCC,
                asset_id=AssetId64,
            ),
        ),
    ),
    _resources_start=construct.Tell,
    _resources_start_assert=construct.Check(
        construct.this.table_of_contents.STRG == construct.this._resources_start - construct.this._named_resources_start
    ),
    resources=construct.Aligned(64, PrefixedArray(Int32ub, ConstructResourceHeader)),
    _resources_end=construct.Tell,
    _resources_end_assert=construct.Check(
        construct.this.table_of_contents.RSHD == construct.this._resources_end - construct.this._resources_start
    ),
) 
# TODO : Once the struct is confirmed, compile it

CompressedPakResource = FocusedSeq(
    "data",
    decompressed_size = Rebuild(Int32ub, construct.len_(construct.this.data)),
    # Added Zlib check for DKCR
    data = IfThenElse(
        game_check.uses_lzo,
        LZOCompressedBlock(construct.this.decompressed_size),
        ZlibCompressedBlock
    )
)

@dataclasses.dataclass
class PakFile:
    asset_id: AssetId
    asset_type: AssetType
    should_compress: bool 
    uncompressed_data: bytes | None    
    compressed_data: bytes | None      
    extra: construct.Container | None = None

    def get_decompressed(self, target_game : Game) -> bytes:
        if self.compressed_data is None:
            self.uncompressed_data = CompressedPakResource.parse(
                self.compressed_data,
                target_game = target_game
            )
        return self.uncompressed_data
        
    def get_compressed(self, target_game : Game) -> bytes:
        if self.compressed_data is None:
                self.compressed_data = CompressedPakResource.build(
                    self.uncompressed_data,
                    target_game = target_game
                )
        return self.compressed_data

    def set_new_data(self, data: bytes):
         self.uncompressed_data = data
         self.compressed_data = None

@dataclasses.dataclass
class PakBody:
     named_resources: dict[str, Dependency]
     files: list[PakFile]

class ConstructPakWii(construct.Construct):
    def _parse(self, stream, context, path) -> PakBody:
        header = PAKNoData._parsereport(stream, context, f"{path} -> header")

        AlignTo(64)._parse(stream, context, path)

        files = []
        # Resource offsets are relative to the start of the DATA section
        data_start = construct.stream_tell(stream, path)
        for i, resource in enumerate(header.resources):
            if resource.offset + data_start != construct.stream_tell(stream, path):
                raise construct.ConstructError(f"Expected resource at {resource.offset + data_start}", path)
            
            data = construct.stream_read(stream, resource.size, path)
            # TODO : Padding to be added ?
            if resource.compressed > 0:
                uncompressed_data = None
                compressed_data = data
            else :
                uncompressed_data = data
                compressed_data = None
            
            files.append(
                PakFile(
                    resource.asset_id,
                    resource.asset_type,
                    resource.compressed > 0,
                    uncompressed_data,
                    compressed_data
                )
            )

        return PakBody(
            named_resources = {
                named.name: Dependency(type = named.asset_type, id = named.asset_id)
                for named in header.named_resources
            },
            files = files
        )

    def _build(self, obj: PakBody, stream, context, path):
        assert isinstance(obj, PakBody)

        header = construct.Container(
            _header = construct.Container(),
            named_resources = construct.ListContainer(
                construct.Container(
                    asset_type = dep.asset_type,
                    asset_id = dep.asset_id,
                    name = name
                )
                for name, dep in obj.named_resources.items()
            ),
            resources = construct.ListContainer(
                construct.Container(
                    compressed = 0,
                    asset_type = file.asset_type,
                    asset_id = file.asset_id,
                    size = 0,
                    offset = 0
                )
                for file in obj.files
            )
        )

        header_start = construct.stream_tell(stream, path)
        PAKNoData._build(header, stream, context, path)
        # Not sure what is the purpose for this line
        AlignTo(64)._build(None, stream, context, path)

        for i, file in enumerate(obj.files):
            compressed = file.should_compress
            game = game_check.get_current_game(context)
            if compressed:
                data = file.get_compressed(game)
            else :
                data = file.get_decompressed(game)
            
            # TODO : If the file ends up bigger, don't compress
            # if compressed and len(data) > len(file.get_decompressed(game)):
            #     compressed = False
            #     data = file.get_decompressed(game)

            pad = 64 - (len(data) % 64)
            if pad < 64:
                data += b"\xFF" * pad
            
            header.resources[i].offset = construct.stream_tell(stream, path)
            header.resources[i].size = len(data)
            header.resources[i].compressed = int(compressed)
            construct.stream_write(stream, data, len(data), path)

        # Update header to contain accurate information to PAK contents
        files_end = construct.steam_tell(stream, path)
        construct.stream_seek(stream, header_start, 0, path)
        PAKNoData._build(header, stream, context, path)
        construct.stream_seek(stream, files_end, 0, path)

PAK_WII = ConstructPakWii()