from __future__ import annotations

import dataclasses
import typing

import construct
from construct import (
    Struct,
    Const,
    Int16ub,
    PrefixedArray,
    Int32ub,
    PascalString,
    IfThenElse,
    FocusedSeq,
    Rebuild,
)

from retro_data_structures import game_check
from retro_data_structures.base_resource import AssetId, AssetType, RawResource, Dependency
from retro_data_structures.common_types import ObjectTag_32
from retro_data_structures.compression import LZOCompressedBlock, ZlibCompressedBlock
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.game_check import Game

PAKHeader = Struct(
    version_major=Const(3, Int16ub),
    version_minor=Const(5, Int16ub),
    unused=Const(0, Int32ub),
)

ResourceHeader = Struct(
    compressed=Int32ub,
    asset=ObjectTag_32,
    size=Int32ub,
    offset=Int32ub,
)

PAKNoData = Struct(
    _header=PAKHeader,
    named_resources=PrefixedArray(
        Int32ub,
        Struct(
            asset=ObjectTag_32,
            name=PascalString(Int32ub, "utf-8"),
        ),
    ),
    resources=PrefixedArray(Int32ub, ResourceHeader),
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
    uncompressed_data: typing.Optional[bytes]
    compressed_data: typing.Optional[bytes]

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
    named_resources: typing.Dict[str, Dependency]
    files: typing.List[PakFile]


class PAKNew(construct.Construct):
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

            files.append(PakFile(
                resource.asset.id,
                resource.asset.type,
                resource.compressed > 0,
                uncompressed_data,
                compressed_data,
            ))

        return PakBody(
            named_resources={
                named.name: Dependency(type=named.asset.type, id=named.asset.id)
                for named in header.named_resources
            },
            files=files,
        )

    def _build(self, obj: PakBody, stream, context, path):
        assert isinstance(obj, PakBody)

        header = construct.Container(
            _header=construct.Container(),
            named_resources=construct.ListContainer(
                construct.Container(
                    asset=construct.Container(
                        type=dep.type,
                        id=dep.id,
                    ),
                    name=name,
                )
                for name, dep in obj.named_resources.items()
            ),
            resources=construct.ListContainer(
                construct.Container(
                    compressed=0,
                    asset=construct.Container(
                        type=file.asset_type,
                        id=file.asset_id,
                    ),
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
                data += b"\xFF" * pad

            header.resources[i].offset = construct.stream_tell(stream, path)
            header.resources[i].size = len(data)
            header.resources[i].compressed = int(compressed)
            construct.stream_write(stream, data, len(data), path)

        # Update header
        files_end = construct.stream_tell(stream, path)
        construct.stream_seek(stream, header_start, 0, path)
        PAKNoData._build(header, stream, context, path)
        construct.stream_seek(stream, files_end, 0, path)


PAK = PAKNew()


class Pak:
    _raw: PakBody
    target_game: Game

    def __init__(self, raw: PakBody, target_game: Game):
        self._raw = raw
        self.target_game = target_game

    @classmethod
    def parse(cls: typing.Type[Pak], data: bytes, target_game: Game) -> Pak:
        return cls(PAK.parse(data, target_game=target_game), target_game)

    def build(self) -> bytes:
        return PAK.build(self._raw, target_game=self.target_game)

    @classmethod
    def parse_stream(cls, stream: typing.BinaryIO, target_game: Game) -> "Pak":
        return cls(PAK.parse_stream(stream, target_game=target_game), target_game)

    def build_stream(self, stream: typing.BinaryIO) -> bytes:
        return PAK.build_stream(self._raw, stream, target_game=self.target_game)

    def get_asset(self, asset_id: AssetId) -> typing.Optional[RawResource]:
        """
        Gets the asset of given id, getting the bytes and type
        :param asset_id:
        :return:
        """
        for file in self._raw.files:
            if file.asset_id == asset_id:
                return RawResource(file.asset_type, file.get_decompressed(self.target_game))

        return None

    def replace_asset(self, asset_id: AssetId, asset: RawResource):
        found = False

        for file in self._raw.files:
            if file.asset_id == asset_id:
                file.asset_type = asset.type
                file.set_new_data(asset.data)
                found = True

        if not found:
            raise ValueError(f"Unknown asset id: {asset_id}")

    def add_asset(self, asset_id: AssetId, asset: RawResource):
        self._raw.files.append(PakFile(
            asset_id=asset_id,
            asset_type=asset.type,
            should_compress=False,
            uncompressed_data=asset.data,
            compressed_data=None,
        ))

    def remove_asset(self, asset_id: AssetId):
        for name, file in self._raw.named_resources.items():
            if file.id == asset_id:
                raise ValueError(f"Asset id {asset_id:08x} is named {name}, can't be removed.")

        found = False
        for file in list(self._raw.files):
            if file.asset_id == asset_id:
                self._raw.files.remove(file)
                found = True

        if not found:
            raise ValueError(f"Unknown asset id: {asset_id}")
