import logging
from pathlib import Path
from typing import List

from retro_data_structures import formats
from retro_data_structures.formats import PAK

logger = logging.getLogger(__name__)


class AssetProvider:
    def __init__(self, pak_paths: List[Path], target_game: int):
        self.pak_paths = pak_paths
        self.target_game = target_game
        self.loaded_assets = {}

    def __enter__(self):
        self.pak_files = [
            path.open("rb")
            for path in self.pak_paths
        ]
        self.paks = []
        for i, pak_file in enumerate(self.pak_files):
            logger.info("Parsing PAK at %s", str(self.pak_paths[i]))
            self.paks.append(PAK.parse_stream(pak_file, target_game=self.target_game))

        self.resource_by_asset_id = {}
        for pak in self.paks:
            for resource in pak.resources:
                if resource.asset.id not in self.resource_by_asset_id:
                    self.resource_by_asset_id[resource.asset.id] = resource

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for pak in self.pak_files:
            pak.close()
        self.pak_files = None

    def get_asset(self, asset_id: int):
        if asset_id in self.loaded_assets:
            return self.loaded_assets[asset_id]

        resource = self.resource_by_asset_id[asset_id]
        asset = formats.format_for(resource.asset.type).parse(resource.contents.value(), target_game=self.target_game)
        self.loaded_assets[asset_id] = asset
        return asset
