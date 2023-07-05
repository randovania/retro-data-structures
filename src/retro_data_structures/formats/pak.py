from __future__ import annotations

import typing
from collections import defaultdict

from retro_data_structures.base_resource import AssetId, RawResource
from retro_data_structures.formats import pak_gc, pak_wiiu
from retro_data_structures.formats.pak_gc import PakBody, PakFile
from retro_data_structures.game_check import Game


def _pak_for_game(game: Game):
    if game == Game.PRIME_REMASTER:
        return pak_wiiu.PAK_WIIU
    else:
        return pak_gc.PAK_GC


class Pak:
    _raw: PakBody
    target_game: Game
    _next_offset: int
    _offsets_for_asset: defaultdict[AssetId, list[int]]

    def __init__(self, raw: PakBody, target_game: Game):
        self._raw = raw
        self.target_game = target_game
        self._next_offset = 0
        self._offsets_for_asset = defaultdict(list)

    @staticmethod
    def header_for_game(game: Game):
        if game == Game.PRIME_REMASTER:
            return pak_wiiu.PakWiiUNoData
        else:
            return pak_gc.PAKNoData

    @staticmethod
    def max_seek_distance(game: Game):
        return 0x1000000 # idk

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

    def get_asset(self, asset_id: AssetId, can_be_compressed: bool = False) -> RawResource | None:
        """
        Gets the asset of given id, getting the bytes and type
        :param asset_id:
        :return:
        """
        for file in self._raw.files:
            if file.asset_id == asset_id:
                if can_be_compressed and file.compressed_data is not None:
                    return RawResource(file.asset_type, file.get_compressed(self.target_game), True)
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

    def add_asset_dumb(self, asset_id: AssetId, asset: RawResource):
        self.add_asset(asset_id, asset, duplicate=True, force_duplicate=True)

    def add_asset(self, asset_id: AssetId, asset: RawResource, duplicate: bool = False, force_duplicate: bool = False):
        if not duplicate and self._offsets_for_asset[asset_id]:
            return

        if not force_duplicate:
            max_seek = Pak.max_seek_distance(self.target_game)

            if any(
                self._next_offset - offset < max_seek
                for offset in self._offsets_for_asset[asset_id]
            ):
                return # no need to duplicate asset

        file_ = PakFile(
            asset_id=asset_id,
            asset_type=asset.type,
            uncompressed_data=asset.data if not asset.compressed else None,
            compressed_data=asset.data if asset.compressed else None
        )
        self._raw.files.append(file_)
        self._offsets_for_asset[asset_id].append(self._next_offset)
        self._next_offset += file_.get_size(self.target_game)

    @property
    def named_assets(self):
        return dict(self._raw.named_resources)

    def clear_assets(self):
        self._raw.files = []
        self._next_offset = 0
        self._offsets_for_asset.clear()
