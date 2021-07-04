import copy
from typing import Callable, Dict, Tuple, Any, NamedTuple

from retro_data_structures.asset_provider import AssetProvider
from retro_data_structures.formats import AssetType, AssetId
from retro_data_structures.game_check import Game

IdGenerator = Callable[[AssetType], AssetId]
Resource = Any
ResourceConverter = Callable[[Resource, "AssetConverter"], Resource]


class ConvertedAsset(NamedTuple):
    id: AssetId
    type: AssetType
    resource: Resource


class AssetConverter:
    target_game: Game
    asset_providers: Dict[Game, AssetProvider]
    id_generator: IdGenerator
    converted_ids: Dict[Tuple[Game, AssetId], AssetId]
    converted_assets: Dict[AssetId, ConvertedAsset]

    def __init__(self, target_game: Game, asset_providers: Dict[Game, AssetProvider], id_generator: IdGenerator,
                 converters: Callable[[Game, AssetType], ResourceConverter]):
        self.target_game = target_game
        self.asset_providers = asset_providers
        self.id_generator = id_generator
        self.converters = converters
        self.converted_ids = {}
        self.converted_assets = {}
        self._being_converted = set()

    def convert_by_id(self, asset_id: AssetId, source_game: Game) -> ConvertedAsset:
        new_id = self.converted_ids.get((source_game, asset_id))
        if new_id is not None:
            return self.converted_assets[new_id]

        if asset_id in self._being_converted:
            raise ValueError(f"Loop detected when converting {asset_id}")

        self._being_converted.add(asset_id)

        asset_provider = self.asset_providers[source_game]
        source_asset = asset_provider.get_asset(asset_id)
        asset_type = asset_provider.get_type_for_asset(asset_id)

        new_asset = self.convert_asset(source_asset, asset_type, source_game)
        self.converted_ids[(source_game, asset_id)] = new_asset.id
        self._being_converted.remove(asset_id)

        return new_asset

    def convert_asset(self, asset, asset_type: AssetType, source_game: Game) -> ConvertedAsset:
        new_asset_id = self.id_generator(asset_type)
        converted_resource = self.converters(source_game, asset_type)(copy.deepcopy(asset), self)
        converted_asset = ConvertedAsset(new_asset_id, asset_type, converted_resource)

        self.converted_assets[new_asset_id] = converted_asset
        return converted_asset

    @property
    def invalid_asset_id(self) -> AssetId:
        return self.target_game.invalid_asset_id
