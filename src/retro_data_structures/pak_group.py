from __future__ import annotations

import collections
import logging
from typing import TYPE_CHECKING

from retro_data_structures.formats.pak import Pak

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Mapping, Sequence

    from retro_data_structures.base_resource import AssetId, AssetType, RawResource
    from retro_data_structures.file_provider import FileProvider
    from retro_data_structures.game_check import Game

logger = logging.getLogger(__name__)


class PakGroup:
    _paks_for_asset_id: dict[AssetId, set[str]]
    _types_for_asset_id: dict[AssetId, AssetType]
    _in_memory_paks: dict[str, Pak]
    _named_resources_per_pak: dict[str, dict[str, AssetId]]

    def __init__(self, provider: FileProvider, pak_list: Sequence[str], target_game: Game):
        self.provider = provider
        self.pak_list = pak_list
        self.target_game = target_game

        self._paks_for_asset_id = collections.defaultdict(set)
        self._types_for_asset_id = {}
        self._in_memory_paks = {}
        self._named_resources_per_pak = {}

        for name in self.pak_list:
            with self.provider.open_binary(name) as f:
                pak_no_data = Pak.header_for_game(self.target_game).parse_stream(f, target_game=self.target_game)

            if "named_resources" in pak_no_data:
                self._named_resources_per_pak[name] = {}
                for named_resource in pak_no_data.named_resources:
                    self._named_resources_per_pak[name][named_resource.name] = named_resource.asset_id

            for entry in pak_no_data.resources:
                self._paks_for_asset_id[entry.asset_id].add(name)
                self._types_for_asset_id[entry.asset_id] = entry.asset_type

    def all_asset_ids(self) -> Iterable[AssetId]:
        """
        Returns an iterator of all asset ids in the available paks.
        """
        return self._paks_for_asset_id.keys()

    def find_paks(self, asset_id: AssetId) -> Iterator[str]:
        """
        Find all paks that contains the given asset id
        """
        yield from self._paks_for_asset_id[asset_id]

    def does_pak_contains_id(self, pak_name: str, asset_id: AssetId) -> bool:
        """
        Checks if the given pak contains the given asset id
        """
        return pak_name in self._paks_for_asset_id[asset_id]

    def does_asset_exists(self, asset_id: AssetId) -> bool:
        """
        Checks if a given asset id exists.
        """

        return asset_id in self._paks_for_asset_id

    def get_asset_type(self, asset_id: AssetId) -> AssetType:
        """
        Gets the type that is associated with the given asset name/id in the pak headers.
        :param asset_id:
        :return:
        :raises KeyError: if the asset doesn't exist
        """
        return self._types_for_asset_id[asset_id]

    def get_raw_asset(self, asset_id: AssetId) -> RawResource | None:
        """
        Gets the unparsed resource with the given id.
        :param asset_id:
        :return: None, if the id doesn't exist.
        """

        for pak_name in self._paks_for_asset_id[asset_id]:
            pak = self.get_pak(pak_name)
            result = pak.get_asset(asset_id)
            if result is not None:
                return result

        return None

    def get_pak(self, pak_name: str) -> Pak:
        """
        Gets a Pak object with the given name.
        Reads the whole Pak to memory and keeps it there for further calls.
        :param pak_name:
        :return:
        """

        if pak_name not in self.pak_list:
            raise ValueError(f"Unknown pak_name: {pak_name}. Known names: {self.pak_list}")

        if pak_name not in self._in_memory_paks:
            logger.info("Reading %s", pak_name)
            with self.provider.open_binary(pak_name) as data:
                self._in_memory_paks[pak_name] = Pak.parse_stream(data, target_game=self.target_game)

        return self._in_memory_paks[pak_name]

    def release_in_memory_paks(self) -> None:
        """
        Release all Paks that are currently in-memory, forcing the next get_pak call to read from disk.
        """
        self._in_memory_paks.clear()

    def get_named_resources_of_pak(self, pak_name: str) -> Mapping[str, AssetId]:
        """
        Gets the mapping of name to asset id for the given pak.
        """
        return dict(self._named_resources_per_pak[pak_name])
