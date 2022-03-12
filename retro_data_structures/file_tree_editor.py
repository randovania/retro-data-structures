import json
import logging
import typing
from pathlib import Path
from typing import Optional, Iterator

import construct

from retro_data_structures import formats
from retro_data_structures.formats.base_resource import (
    AssetId, BaseResource, NameOrAssetId, RawResource,
    resolve_asset_id
)
from retro_data_structures.formats.pak import PAKNoData, Pak
from retro_data_structures.game_check import Game

T = typing.TypeVar("T")
logger = logging.getLogger(__name__)


class FileProvider:
    def is_file(self, name: str) -> bool:
        raise NotImplementedError()

    def rglob(self, pattern: str) -> Iterator[str]:
        raise NotImplementedError()

    def open(self, name: str, mode: str):
        raise NotImplementedError()


class PathFileProvider(FileProvider):
    def __init__(self, root: Path):
        self.root = root

    def is_file(self, name: str) -> bool:
        return self.root.joinpath(name).is_file()

    def rglob(self, name: str) -> Iterator[str]:
        for it in self.root.rglob(name):
            yield it.relative_to(self.root).as_posix()

    def open(self, name: str, mode: str):
        return self.root.joinpath(name).open(mode)


class FileTreeEditor:
    """
    Manages efficiently reading all PKGs in the game and writing out modifications to a new path.

    _files_for_asset_id: mapping of asset id to all paks it can be found at
    _ensured_asset_ids: mapping of pak name to assets we'll copy into it when saving
    _modified_resources: mapping of asset id to raw resources. When saving, these asset ids are replaced
    """
    headers: dict[str, construct.Container]
    _files_for_asset_id: dict[AssetId, set[str]]
    _ensured_asset_ids: dict[str, set[AssetId]]
    _modified_resources: dict[AssetId, Optional[RawResource]]
    _in_memory_paks: dict[str, Pak]

    def __init__(self, provider: FileProvider, target_game: Game):
        self.provider = provider
        self.target_game = target_game
        self._modified_resources = {}
        self._in_memory_paks = {}

        self._update_headers()

    def _resolve_asset_id(self, value: NameOrAssetId) -> AssetId:
        return resolve_asset_id(self.target_game, value)

    def _add_pak_name_for_asset_id(self, asset_id: AssetId, pak_name: str):
        self._files_for_asset_id[asset_id] = self._files_for_asset_id.get(asset_id, set())
        self._files_for_asset_id[asset_id].add(pak_name)

    def _update_headers(self):
        self._ensured_asset_ids = {}
        self._files_for_asset_id = {}

        self._name_for_asset_id = {}
        if self.provider.is_file("custom_names.json"):
            with self.provider.open("custom_names.json", "r") as f:
                self._name_for_asset_id.update({
                    asset_id: name
                    for name, asset_id in json.load(f).items()
                })

        self.all_pkgs = list(
            self.provider.rglob("*.pak")
        )

        for name in self.all_pkgs:
            with self.provider.open(name, "rb") as f:
                pak_no_data = PAKNoData.parse_stream(f, target_game=self.target_game)

            self._ensured_asset_ids[name] = set()
            for entry in pak_no_data.resources:
                self._add_pak_name_for_asset_id(entry.asset.id, name)

    def all_asset_ids(self) -> Iterator[AssetId]:
        """
        Returns an iterator of all asset ids in the available paks.
        """
        yield from self._files_for_asset_id.keys()

    def find_paks(self, asset_id: NameOrAssetId) -> Iterator[str]:
        for pkg_name in self._files_for_asset_id[self._resolve_asset_id(asset_id)]:
            yield pkg_name

    def does_asset_exists(self, asset_id: NameOrAssetId) -> bool:
        """
        Checks if a given asset id exists.
        """
        asset_id = self._resolve_asset_id(asset_id)

        if asset_id in self._modified_resources:
            return self._modified_resources[asset_id] is not None

        return asset_id in self._files_for_asset_id

    def get_raw_asset(self, asset_id: NameOrAssetId) -> RawResource:
        """
        Gets the bytes data for the given asset name/id, optionally restricting from which pkg.
        :raises ValueError if the asset doesn't exist.
        """
        original_name = asset_id
        asset_id = self._resolve_asset_id(asset_id)

        if asset_id in self._modified_resources:
            result = self._modified_resources[asset_id]
            if result is None:
                raise ValueError(f"Deleted asset_id: {original_name}")
            else:
                return result

        for pak_name in self._files_for_asset_id[asset_id]:
            pkg = self.get_pak(pak_name)
            result = pkg.get_asset(asset_id)
            if result is not None:
                return result

        raise ValueError(f"Unknown asset_id: {original_name}")

    def get_parsed_asset(self, asset_id: NameOrAssetId, *,
                         type_hint: typing.Type[T] = BaseResource) -> T:
        """
        Gets the resource with the given name and decodes it based on the extension.
        """
        raw_asset = self.get_raw_asset(asset_id)

        format_class = formats.format_for(raw_asset.type)
        if type_hint is not BaseResource and type_hint != format_class:
            raise ValueError(f"type_hint was {type_hint}, pak listed {format_class}")

        return format_class.parse(raw_asset.data, target_game=self.target_game)

    def add_new_asset(self, name: str, new_data: typing.Union[RawResource, BaseResource],
                      in_pkgs: typing.Iterable[str]):
        """
        Adds an asset that doesn't already exist.
        """
        asset_id = self._resolve_asset_id(name)
        if self.does_asset_exists(asset_id):
            raise ValueError(f"{name} already exists")

        in_pkgs = list(in_pkgs)
        files_set = set()

        self._name_for_asset_id[asset_id] = name
        self._files_for_asset_id[asset_id] = files_set
        self.replace_asset(name, new_data)
        for pkg_name in in_pkgs:
            self.ensure_present(pkg_name, asset_id)

    def replace_asset(self, asset_id: NameOrAssetId, new_data: typing.Union[RawResource, BaseResource]):
        """
        Replaces an existing asset.
        See `add_new_asset` for new assets.
        """

        # Test if the asset exists
        if not self.does_asset_exists(asset_id):
            raise ValueError(f"Unknown asset: {asset_id}")

        if isinstance(new_data, BaseResource):
            logger.debug("Encoding %s", str(asset_id))
            raw_asset = RawResource(
                type=new_data.resource_type(),
                data=new_data.build(),
            )

        else:
            raw_asset = new_data

        self._modified_resources[self._resolve_asset_id(asset_id)] = raw_asset

    def delete_asset(self, asset_id: NameOrAssetId):
        # Test if the asset exists
        if not self.does_asset_exists(asset_id):
            raise ValueError(f"Unknown asset: {asset_id}")

        asset_id = self._resolve_asset_id(asset_id)

        self._modified_resources[asset_id] = None

        # If this asset id was previously ensured, remove that
        for ensured_ids in self._ensured_asset_ids.values():
            if asset_id in ensured_ids:
                ensured_ids.remove(asset_id)

    def ensure_present(self, pak_name: str, asset_id: NameOrAssetId):
        """
        Ensures the given pak has the given assets, collecting from other paks if needed.
        """
        if pak_name not in self._ensured_asset_ids:
            raise ValueError(f"Unknown pak_name: {pak_name}")

        # Test if the asset exists
        if not self.does_asset_exists(asset_id):
            raise ValueError(f"Unknown asset: {asset_id}")

        # If the pkg already has the given asset, do nothing
        asset_id = self._resolve_asset_id(asset_id)
        if pak_name not in self._files_for_asset_id[asset_id]:
            self._ensured_asset_ids[pak_name].add(asset_id)

    def get_pak(self, pak_name: str) -> Pak:
        if pak_name not in self._ensured_asset_ids:
            raise ValueError(f"Unknown pak_name: {pak_name}")

        if pak_name not in self._in_memory_paks:
            logger.info("Reading %s", pak_name)
            with self.provider.open(pak_name, "rb") as f:
                self._in_memory_paks[pak_name] = Pak.parse_stream(f, target_game=self.target_game)

        return self._in_memory_paks[pak_name]

    def save_modifications(self, output_path: Path):
        modified_paks = set()
        asset_ids_to_copy = {}

        for asset_id in self._modified_resources.keys():
            modified_paks.update(self._files_for_asset_id[asset_id])

        # Read all asset ids we need to copy somewhere else
        for asset_ids in self._ensured_asset_ids.values():
            for asset_id in asset_ids:
                if asset_id not in asset_ids_to_copy:
                    asset_ids_to_copy[asset_id] = self.get_raw_asset(asset_id)

        # Update the PKGs
        for pak_name in modified_paks:
            logger.info("Updating %s", pak_name)
            pak = self._in_memory_paks.pop(pak_name)

            for asset_id, raw_asset in self._modified_resources.items():
                if pak_name in self._files_for_asset_id[asset_id]:
                    if raw_asset is None:
                        pak.remove_asset(asset_id)
                    else:
                        pak.replace_asset(asset_id, raw_asset)

            # Add the files that were ensured to be present in this pak
            for asset_id in self._ensured_asset_ids[pak_name]:
                pak.add_asset(asset_id, asset_ids_to_copy[asset_id])

            # Write the data
            out_pak_path = output_path.joinpath(pak_name)
            logger.info("Writing %s", out_pak_path)
            out_pak_path.parent.mkdir(parents=True, exist_ok=True)
            with out_pak_path.open("wb") as f:
                pak.build_stream(f)

        custom_names = output_path.joinpath("custom_names.json")
        with custom_names.open("w") as f:
            json.dump(
                {
                    name: asset_id
                    for asset_id, name in self._name_for_asset_id.items()
                },
                f,
                indent=4,
            )

        self._modified_resources = {}
        self._update_headers()
