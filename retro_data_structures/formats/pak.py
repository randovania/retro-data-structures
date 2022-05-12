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
    Pointer,
    Aligned,
    Tell,
    Rebuild,
    GreedyBytes,
    Array,
    Seek,
    Computed,
    RawCopy,
)

from retro_data_structures import game_check
from retro_data_structures.common_types import ObjectTag_32
from retro_data_structures.compression import LZOCompressedBlock, ZlibCompressedBlock
from retro_data_structures.construct_extensions.alignment import AlignTo, AlignedPrefixed
from retro_data_structures.construct_extensions.misc import LazyPatchedForBug
from retro_data_structures.formats import BaseResource
from retro_data_structures.base_resource import AssetId, AssetType, RawResource
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
)


def header_field(offset):
    def result(ctx):
        parents = [ctx]
        while "_" in parents[-1]:
            parents.append(parents[-1]["_"])

        start_headers = None
        index = None

        for c in reversed(parents):
            if "_start_headers" in c:
                start_headers = c["_start_headers"]
                break

        for c in parents:
            if "_resource_index" in c:
                index = c["_resource_index"]
                break

        if index is None or start_headers is None:
            raise ValueError("Missing required context key")

        return start_headers + (index * ResourceHeader.sizeof()) + offset

    return result


def skip_headers(ctx):
    result = ResourceHeader.sizeof() * ctx["_num_resources"]
    return result


CompressedPakResource = FocusedSeq(
    "data",
    decompressed_size=Rebuild(Int32ub, construct.len_(construct.this.data)),
    data=IfThenElse(
        game_check.uses_lzo,
        LZOCompressedBlock(construct.this.decompressed_size),
        ZlibCompressedBlock,
    ),
)


def create():
    return "PAK" / Struct(
        _header=PAKHeader,
        named_resources=PrefixedArray(
            Int32ub,
            Struct(
                asset=ObjectTag_32,
                name=PascalString(Int32ub, "utf-8"),
            ),
        ),
        _num_resources=Rebuild(Int32ub, construct.len_(construct.this.resources)),
        _start_headers=Tell,
        _skip_headers=Seek(skip_headers, 1),
        _align=AlignTo(32),
        resources=Array(
            construct.this["_num_resources"],
            Aligned(
                32,
                Struct(
                    _start=Tell,
                    _resource_index=Computed(lambda ctx: ctx["_index"]),
                    compressed=Pointer(header_field(0x0), Int32ub),
                    asset=Pointer(header_field(0x4), ObjectTag_32),
                    contents=RawCopy(
                        LazyPatchedForBug(
                            AlignedPrefixed(
                                Pointer(header_field(0xC), Int32ub),
                                IfThenElse(
                                    construct.this.compressed > 0,
                                    CompressedPakResource,
                                    GreedyBytes,
                                ),
                                32,
                                Int32ub.length,
                            )
                        )
                    ),
                    _end=Tell,
                    size=Pointer(header_field(0xC), Rebuild(Int32ub, construct.this.contents.length)),
                    _offset=Pointer(header_field(0x10), Rebuild(Int32ub, lambda ctx: ctx["_start"])),
                ),
            ),
        ),
    )


PAK = create()


@dataclasses.dataclass(frozen=True)
class PakFile:
    asset_id: AssetId
    asset_name: AssetType
    data: bytes


class Pak(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return PAK

    @classmethod
    def parse_stream(cls, stream: typing.BinaryIO, target_game: Game) -> "Pak":
        return cls(cls.construct_class(target_game).parse_stream(stream, target_game=target_game),
                   target_game)

    def build_stream(self, stream: typing.BinaryIO) -> bytes:
        return self.construct_class(self.target_game).build_stream(self._raw, stream, target_game=self.target_game)

    def offsets_for_asset(self, asset_id: AssetId) -> typing.Iterator[int]:
        for file in self.raw.resources:
            if file.asset.id == asset_id:
                yield file._offset

    @property
    def all_assets(self) -> typing.Iterator[PakFile]:
        for file in self.raw.resources:
            yield PakFile(file.asset.id, file.asset.type, file.contents.value())

    def get_asset(self, asset_id: AssetId) -> typing.Optional[RawResource]:
        """
        Gets the asset of given id, getting the bytes and type
        :param asset_id:
        :return:
        """
        for file in self.raw.resources:
            if file.asset.id == asset_id:
                return RawResource(file.asset.type, file.contents.value())

        return None

    def replace_asset(self, asset_id: AssetId, asset: RawResource):
        found = False

        for file in self.raw.resources:
            if file.asset.id == asset_id:
                file.asset.type = asset.type
                file.contents = construct.Container(value=asset.data)
                found = True

        if not found:
            raise ValueError(f"Unknown asset id: {asset_id}")

    def add_asset(self, asset_id: AssetId, asset: RawResource):
        self.raw.resources.append(construct.Container(
            compressed=0,
            asset=construct.Container(
                type=asset.type,
                id=asset_id,
            ),
            contents=construct.Container(
                value=asset.data,
            ),
        ))

    def remove_asset(self, asset_id: AssetId):
        for file in self.raw.named_resources:
            if file.asset.id == asset_id:
                raise ValueError(f"Asset id {asset_id} is named {file.name}, can't be removed.")

        found = False
        for file in list(self.raw.resources):
            if file.asset.id == asset_id:
                self.raw.resources.remove(file)
                found = True

        if not found:
            raise ValueError(f"Unknown asset id: {asset_id}")

