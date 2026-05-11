from __future__ import annotations

import collections
import typing

from retro_data_structures.base_resource import AssetId, RawResource
from retro_data_structures.formats import pak_gc, pak_wii, pak_wiiu
from retro_data_structures.formats.pak_gc import PakBody, PakFile
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from collections.abc import Iterator


def _pak_for_game(game: Game):
    if game == Game.PRIME_REMASTER:
        return pak_wiiu.PAK_WIIU
    elif game >= Game.CORRUPTION:
        return pak_wii.PAK_WII
    else:
        return pak_gc.PAK_GC


class Pak:
    _raw: PakBody
    target_game: Game
    _file_indices_by_id: collections.defaultdict[AssetId, list[int]]

    def __init__(self, raw: PakBody, target_game: Game):
        self._raw = raw
        self.target_game = target_game
        self._calculate_files_by_id()

    def _calculate_files_by_id(self) -> None:
        files_by_id = collections.defaultdict(list)
        for i, file in enumerate(self._raw.files):
            files_by_id[file.asset_id].append(i)
        self._file_indices_by_id = files_by_id

    @staticmethod
    def header_for_game(game: Game):
        if game == Game.PRIME_REMASTER:
            return pak_wiiu.PakWiiUNoData
        elif game >= Game.CORRUPTION:
            return pak_wii.PAKNoData
        else:
            return pak_gc.PAKNoData

    @classmethod
    def parse(cls: type[Pak], data: bytes, target_game: Game) -> Pak:
        return cls(_pak_for_game(target_game).parse(data, target_game=target_game), target_game)

    def build(self) -> bytes:
        return _pak_for_game(self.target_game).build(self._raw, target_game=self.target_game)

    @classmethod
    def parse_stream(cls, stream: typing.BinaryIO, target_game: Game) -> Pak:
        return cls(_pak_for_game(target_game).parse_stream(stream, target_game=target_game), target_game)

    def build_stream(self, stream: typing.BinaryIO) -> bytes:
        return _pak_for_game(self.target_game).build_stream(self._raw, stream, target_game=self.target_game)

    def get_all_assets(self) -> Iterator[tuple[AssetId, RawResource]]:
        for file in self._raw.files:
            yield file.asset_id, RawResource(file.asset_type, file.get_decompressed(self.target_game))

    def get_asset(self, asset_id: AssetId) -> RawResource | None:
        """
        Gets the asset of given id, getting the bytes and type
        :param asset_id:
        :return:
        """
        for index in self._file_indices_by_id[asset_id]:
            file = self._raw.files[index]
            return RawResource(file.asset_type, file.get_decompressed(self.target_game))

        return None

    def replace_asset(self, asset_id: AssetId, asset: RawResource):
        found = False

        for index in self._file_indices_by_id[asset_id]:
            file = self._raw.files[index]
            file.asset_type = asset.type
            file.set_new_data(asset.data)
            found = True

        if not found:
            raise ValueError(f"Unknown asset id: {asset_id}")

    def add_asset(self, asset_id: AssetId, asset: RawResource):
        self._raw.files.append(
            PakFile(
                asset_id=asset_id,
                asset_type=asset.type,
                should_compress=False,
                uncompressed_data=asset.data,
                compressed_data=None,
            )
        )
        self._file_indices_by_id[asset_id].append(len(self._raw.files))

    def remove_asset(self, asset_id: AssetId):
        for name, file in self._raw.named_resources.items():
            if file.id == asset_id:
                raise ValueError(f"Asset id {asset_id:08x} is named {name}, can't be removed.")

        found = False
        for index in reversed(self._file_indices_by_id[asset_id]):
            self._raw.files.pop(index)
            found = True

        if not found:
            raise ValueError(f"Unknown asset id: {asset_id}")

        self._calculate_files_by_id()
