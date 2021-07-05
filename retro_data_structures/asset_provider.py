import logging
from pathlib import Path
from typing import List, BinaryIO, Optional

from retro_data_structures import formats
from retro_data_structures.formats import AssetType, AssetId
from retro_data_structures.formats.pak import CompressedPakResource, PAKNoData
from retro_data_structures.game_check import Game

logger = logging.getLogger(__name__)


class UnknownAssetId(Exception):
    def __init__(self, asset_id):
        super().__init__(f"Unknown asset id 0x{asset_id:08X}")
        self.asset_id = asset_id


class InvalidAssetId(Exception):
    def __init__(self, asset_id, reason: str):
        super().__init__(f"Unable to decode asset id 0x{asset_id:08X}: {reason}")
        self.asset_id = asset_id
        self.reason = reason


class AssetProvider:
    _pak_files: Optional[List[BinaryIO]] = None

    def __init__(self, pak_paths: List[Path], target_game: Game):
        self.pak_paths = pak_paths
        self.target_game = target_game
        self.loaded_assets = {}

    def __enter__(self):
        self._pak_files = [
            path.open("rb")
            for path in self.pak_paths
        ]
        self._paks = []
        for i, pak_file in enumerate(self._pak_files):
            logger.info("Parsing PAK at %s", str(self.pak_paths[i]))
            self._paks.append(PAKNoData.parse_stream(pak_file, target_game=self.target_game))

        self._resource_by_asset_id = {}
        for i, pak in enumerate(self._paks):
            for resource in pak.resources:
                if resource.asset.id not in self._resource_by_asset_id:
                    self._resource_by_asset_id[resource.asset.id] = (resource, i)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for pak in self._pak_files:
            pak.close()
        self._pak_files = None

    def get_asset(self, asset_id: AssetId):
        if asset_id in self.loaded_assets:
            return self.loaded_assets[asset_id]

        try:
            resource, pak_id = self._resource_by_asset_id[asset_id]
        except KeyError:
            raise UnknownAssetId(asset_id)

        pak_file = self._pak_files[pak_id]
        pak_file.seek(resource.offset)
        data = pak_file.read(resource.size)
        if resource.compressed:
            data = CompressedPakResource.parse(data, target_game=self.target_game)

        try:
            format_for_type = formats.format_for(resource.asset.type)
        except Exception:
            raise InvalidAssetId(asset_id, f"Unsupported type {resource.asset.type}")

        try:
            asset = format_for_type.parse(data, target_game=self.target_game)
        except Exception:
            raise InvalidAssetId(asset_id, f"Unable to decode using type {resource.asset.type}")

        self.loaded_assets[asset_id] = asset
        return asset

    def get_type_for_asset(self, asset_id: AssetId) -> AssetType:
        try:
            return self._resource_by_asset_id[asset_id][0].asset.type
        except KeyError:
            raise UnknownAssetId(asset_id)

    def asset_id_exists(self, asset_id: AssetId) -> bool:
        return asset_id in self._resource_by_asset_id

    @property
    def all_resource_headers(self):
        for resource, _ in self._resource_by_asset_id.values():
            yield resource
