import typing

from retro_data_structures.base_resource import NameOrAssetId, BaseResource, AssetType, RawResource
from retro_data_structures.game_check import Game

T = typing.TypeVar("T")


class AssetProvider:
    @property
    def game(self) -> Game:
        raise NotImplementedError()

    def get_raw_asset(self, asset_id: NameOrAssetId) -> RawResource:
        """
        Gets the bytes data for the given asset name/id, optionally restricting from which pak.
        :raises: ValueError if the asset doesn't exist.
        """
        raise NotImplementedError()

    def get_parsed_asset(self, asset_id: NameOrAssetId, *,
                         type_hint: typing.Type[T] = BaseResource) -> T:
        """
        Gets the resource with the given name and decodes it based on the type listed in the PAK.
        """
        raise NotImplementedError()

    def get_asset_type(self, asset_id: NameOrAssetId) -> AssetType:
        raise NotImplementedError()

    def get_file(self, path: NameOrAssetId, type_hint: typing.Type[T] = BaseResource) -> T:
        """
        Wrapper for get_parsed_asset. Override in subclasses for additional behavior such as automatic saving.
        """
        return self.get_parsed_asset(path, type_hint=type_hint)
