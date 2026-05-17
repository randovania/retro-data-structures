from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

import construct
from construct import FocusedSeq, IfThenElse, Int32ub, Rebuild

from retro_data_structures import game_check
from retro_data_structures.compression import LZOCompressedBlock, ZlibCompressedBlock
from retro_data_structures.formats.cmpd import CompressedWiiPakResource
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId, AssetType, Dependency

CompressedGcPakResource = FocusedSeq(
    "data",
    decompressed_size=Rebuild(Int32ub, construct.len_(construct.this.data)),
    data=IfThenElse(
        game_check.uses_lzo,
        LZOCompressedBlock(construct.this.decompressed_size),
        ZlibCompressedBlock,
    ),
)


def _decompress(data: bytes, target_game: Game) -> bytes:
    if target_game <= Game.ECHOES:
        return CompressedGcPakResource.parse(data, target_game=target_game)
    else:
        return CompressedWiiPakResource.parse(data, target_game=target_game)


def _compress(data: bytes, target_game: Game) -> bytes:
    if target_game <= Game.ECHOES:
        return CompressedGcPakResource.build(data, target_game=target_game)
    else:
        return CompressedWiiPakResource.build(data, target_game=target_game)


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
            assert self.compressed_data is not None
            self.uncompressed_data = _decompress(self.compressed_data, target_game)

        return self.uncompressed_data

    def get_compressed(self, target_game: Game) -> bytes:
        if self.compressed_data is None:
            assert self.uncompressed_data is not None
            self.compressed_data = _compress(self.uncompressed_data, target_game)

        return self.compressed_data

    def set_new_data(self, data: bytes):
        self.uncompressed_data = data
        self.compressed_data = None


@dataclasses.dataclass
class PakBody:
    named_resources: list[tuple[str, Dependency]]
    files: list[PakFile]
    md5_hash: bytes | None = None
