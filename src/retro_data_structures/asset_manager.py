from __future__ import annotations

import io
import json
import logging
import typing
from abc import ABC, abstractmethod
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import override

import ppc_asm.dol_file

from retro_data_structures import formats
from retro_data_structures.base_resource import (
    AssetId,
    AssetType,
    BaseResource,
    Dependency,
    NameOrAssetId,
    RawResource,
    Resource,
    resolve_asset_id,
)
from retro_data_structures.exceptions import DependenciesHandledElsewhere, UnknownAssetId
from retro_data_structures.formats import Dgrp, dependency_cheating
from retro_data_structures.formats.audio_group import Agsc, Atbl
from retro_data_structures.formats.ntwk import Ntwk
from retro_data_structures.formats.pak import Pak
from retro_data_structures.game_check import Game
from retro_data_structures.pak_group import PakGroup

if typing.TYPE_CHECKING:
    from collections.abc import Iterable, Iterator
    from pathlib import Path

    import construct

    from retro_data_structures.file_provider import FileProvider
    from retro_data_structures.formats.ancs import Ancs
    from retro_data_structures.formats.pak import Pak

T = typing.TypeVar("T", bound=BaseResource)
logger = logging.getLogger(__name__)


class MemoryDol(ppc_asm.dol_file.DolEditor):
    def __init__(self, dol: bytes):
        super().__init__(ppc_asm.dol_file.DolHeader.from_bytes(dol))
        self.dol_file = io.BytesIO(dol)

    def _seek_and_read(self, seek: int, size: int):
        self.dol_file.seek(seek)
        return self.dol_file.read(size)

    def _seek_and_write(self, seek: int, data: bytes):
        self.dol_file.seek(seek)
        self.dol_file.write(data)


class FileWriter:
    def open_text(self, name: str) -> typing.TextIO:
        raise NotImplementedError

    def open_binary(self, name: str) -> typing.BinaryIO:
        raise NotImplementedError

    def write_dol(self, data: bytes) -> None:
        raise NotImplementedError


class PathFileWriter(FileWriter):
    def __init__(self, root: Path):
        if not root.is_dir():
            raise FileNotFoundError(f"{root} is not a directory")
        self.root = root
        self.file_root = root.joinpath("files")

    def _ensure_directories(self, name: str) -> None:
        self.file_root.joinpath(name).parent.mkdir(parents=True, exist_ok=True)

    def open_text(self, name: str) -> typing.TextIO:
        self._ensure_directories(name)
        return self.file_root.joinpath(name).open("w")

    def open_binary(self, name: str) -> typing.BinaryIO:
        self._ensure_directories(name)
        return self.file_root.joinpath(name).open("w+b")

    def write_dol(self, data: bytes) -> None:
        target_dol = self.root.joinpath("sys/main.dol")
        target_dol.parent.mkdir(exist_ok=True, parents=True)
        target_dol.write_bytes(data)


def _get_name(asset_id: NameOrAssetId) -> str | None:
    if isinstance(asset_id, str):
        return asset_id
    return None


class PakExportStrategy(ABC):
    def __init__(self, manager: AssetManager):
        self.manager = manager

    @abstractmethod
    def ensure_present(self, pak_name: str, asset_id: NameOrAssetId) -> None:
        raise NotImplementedError

    @abstractmethod
    def export(self, output: FileWriter) -> None:
        raise NotImplementedError


class PakExportStrategyAppend(PakExportStrategy):
    """
    Edits the existing paks, by appending the new resources as ensured.
    """

    _ensured_asset_ids: dict[str, set[AssetId]]
    """Mapping of pak name to assets we'll copy into it when saving."""

    def __init__(self, manager: AssetManager):
        super().__init__(manager)

        self._ensured_asset_ids = {pak_name: set() for pak_name in self.manager.all_paks}

    @override
    def ensure_present(self, pak_name: str, asset_id: NameOrAssetId) -> None:
        """
        Ensures the given pak has the given assets, collecting from other paks if needed.
        """
        if pak_name not in self._ensured_asset_ids:
            raise ValueError(f"Unknown pak_name: {pak_name}")

        original_name = _get_name(asset_id)
        asset_id = self.manager.resolve_asset_id(asset_id)

        # Test if the asset exists
        if not self.manager.does_asset_exists(asset_id):
            raise UnknownAssetId(asset_id, original_name)

        # If the pak already has the given asset, do nothing
        if pak_name not in self.manager.pak_group.find_paks(asset_id):
            self._ensured_asset_ids[pak_name].add(asset_id)

    @override
    def export(self, output: FileWriter) -> None:
        manager = self.manager
        pak_group = manager.pak_group
        modified_resources = manager._modified_resources

        modified_paks = set()
        asset_ids_to_copy = {}

        for asset_id in modified_resources.keys():
            modified_paks.update(pak_group.find_paks(asset_id))

        # Make sure all paks were loaded
        for pak_name in modified_paks:
            pak_group.get_pak(pak_name)

        # Read all asset ids we need to copy somewhere else
        for pak_name, asset_ids in self._ensured_asset_ids.items():
            if not asset_ids:
                continue

            modified_paks.add(pak_name)
            for asset_id in asset_ids:
                if asset_id not in asset_ids_to_copy:
                    asset_ids_to_copy[asset_id] = manager.get_raw_asset(asset_id)

        # Update the PAKs
        for pak_name in modified_paks:
            logger.info("Updating %s", pak_name)
            pak = pak_group.get_pak(pak_name)

            for asset_id, raw_asset in modified_resources.items():
                if pak_name in pak_group.find_paks(asset_id):
                    pak.replace_asset(asset_id, raw_asset)

            # Add the files that were ensured to be present in this pak
            for asset_id in self._ensured_asset_ids[pak_name]:
                pak.add_asset(asset_id, asset_ids_to_copy[asset_id])

            # Write the data
            logger.info("Writing %s", pak_name)
            with output.open_binary(pak_name) as f:
                pak.build_stream(f)

        pak_group.release_in_memory_paks()


class AssetManager:
    """
    Manages efficiently reading all PAKs in the game and writing out modifications to a new path.

    _modified_resources: mapping of asset id to raw resources. When saving, these asset ids are replaced
    """

    provider: FileProvider
    headers: dict[str, construct.Container]
    pak_group: PakGroup
    _modified_resources: dict[AssetId, RawResource]
    _memory_files: dict[AssetId, BaseResource]
    _dol: MemoryDol | None = None
    _tweaks: Ntwk | None = None
    _mrea_to_mlvl: dict[AssetId, AssetId] | None = None

    _custom_asset_ids: dict[str, AssetId]
    _audio_group_dependency: tuple[Dgrp, ...] | None = None

    _cached_dependencies: dict[AssetId, tuple[Dependency, ...]]
    _cached_ancs_per_char_dependencies: defaultdict[AssetId, dict[int, tuple[Dependency, ...]]]
    _sound_id_to_agsc: dict[int, AssetId | None] | None = None

    def __init__(
        self, provider: FileProvider, target_game: Game, pak_strategy: type[PakExportStrategy] = PakExportStrategyAppend
    ):
        self.provider = provider
        self.target_game = target_game
        self._modified_resources = {}
        self._memory_files = {}
        self._next_generated_id = 0xFFFF0000

        self._update_headers()

        if target_game in [Game.PRIME, Game.ECHOES]:
            self.dol = MemoryDol(provider.get_dol())
        if target_game == Game.ECHOES:
            with provider.open_binary("Standard.ntwk") as f:
                self.tweaks = Ntwk.parse(f.read(), target_game)

        self._cached_dependencies = {}
        self._cached_ancs_per_char_dependencies = defaultdict(dict)
        self.pak_strategy = pak_strategy(self)

    def resolve_asset_id(self, value: NameOrAssetId) -> AssetId:
        if value in self._custom_asset_ids:
            return self._custom_asset_ids[value]
        return resolve_asset_id(self.target_game, value)

    def _update_headers(self) -> None:
        self._custom_asset_ids = {}
        if self.provider.is_file("custom_names.json"):
            custom_names_text = self.provider.read_binary("custom_names.json").rstrip(b"\xff").decode("utf-8")

            self._custom_asset_ids.update(dict(json.loads(custom_names_text).items()))

        self.all_paks = list(self.provider.rglob("*.pak"))
        self.pak_group = PakGroup(self.provider, self.all_paks, self.target_game)

    def generate_asset_id(self) -> int:
        result = self._next_generated_id
        while self.does_asset_exists(result):
            result += 1

        self._next_generated_id = result + 1
        return result

    def register_custom_asset_name(self, name: str, asset_id: AssetId) -> None:
        if self.does_asset_exists(asset_id):
            raise ValueError(f"{asset_id} ({name}) already exists")

        if name in self._custom_asset_ids and self._custom_asset_ids[name] != asset_id:
            raise ValueError(f"{name} already exists")

        self._custom_asset_ids[name] = asset_id

    def get_custom_asset(self, name: str) -> AssetId | None:
        return self._custom_asset_ids.get(name)

    def get_custom_name_for(self, asset_id: AssetId) -> str | None:
        """"""
        for name, custom_id in self._custom_asset_ids.items():
            if custom_id == asset_id:
                return name
        return None

    def all_asset_ids(self) -> Iterable[AssetId]:
        """
        Returns an iterator of all asset ids in this manager.
        """
        all_ids = set()
        for asset_id in self.pak_group.all_asset_ids():
            yield asset_id
            all_ids.add(asset_id)

        for asset_id in self._modified_resources:
            if asset_id not in all_ids:
                yield asset_id

    def all_asset_ids_of_type(self, asset_type: str) -> Iterator[AssetId]:
        """
        Returns an iterator of all asset ids in the available paks that have the matching file type.
        """
        for asset_id in self.all_asset_ids():
            if self.get_asset_type(asset_id) == asset_type:
                yield asset_id

    def find_paks(self, asset_id: NameOrAssetId) -> Iterator[str]:
        """
        Find all paks that contains the given asset id
        """
        original_name = _get_name(asset_id)
        asset_id = self.resolve_asset_id(asset_id)
        try:
            return self.pak_group.find_paks(asset_id)
        except KeyError:
            raise UnknownAssetId(asset_id, original_name) from None

    def does_asset_exists(self, asset_id: NameOrAssetId) -> bool:
        """
        Checks if a given asset id exists.
        """
        asset_id = self.resolve_asset_id(asset_id)

        if asset_id in self._modified_resources:
            return True

        return self.pak_group.does_asset_exists(asset_id)

    def get_asset_type(self, asset_id: NameOrAssetId) -> AssetType:
        """
        Gets the type that is associated with the given asset name/id in the pak headers.
        :param asset_id:
        :return:
        """
        original_name = _get_name(asset_id)
        asset_id = self.resolve_asset_id(asset_id)

        if asset_id in self._modified_resources:
            return self._modified_resources[asset_id].type

        try:
            return self.pak_group.get_asset_type(asset_id)
        except KeyError:
            raise UnknownAssetId(asset_id, original_name) from None

    def get_asset_format(self, asset_id: NameOrAssetId) -> type[BaseResource]:
        """
        Gets the BaseResource class that is associated with the given asset id in the PAKs.

        """
        asset_type = self.get_asset_type(asset_id)

        if asset_type == "DUMB":
            return BaseResource

        return formats.resource_type_for(asset_type)

    def get_raw_asset(self, asset_id: NameOrAssetId) -> RawResource:
        """
        Gets the bytes data for the given asset name/id.
        :raises ValueError if the asset was deleted.
        :raises UnknownAssetId if the asset doesn't exist.
        """
        original_name = _get_name(asset_id)
        asset_id = self.resolve_asset_id(asset_id)

        if asset_id in self._modified_resources:
            return self._modified_resources[asset_id]

        try:
            result = self.pak_group.get_raw_asset(asset_id)
            if result is not None:
                return result

            if asset_id in self._memory_files:
                raise ValueError(f"Attempt to get raw of new asset {asset_id}, but it hasn't been built yet.")

            raise UnknownAssetId(asset_id, original_name) from None
        except KeyError:
            raise UnknownAssetId(asset_id, original_name) from None

    def get_parsed_asset(self, asset_id: NameOrAssetId, *, type_hint: type[T] = BaseResource) -> T:
        """
        Gets the resource with the given name and decodes it based on the extension.
        """
        format_class = self.get_asset_format(asset_id)

        if format_class is BaseResource:
            if type_hint is BaseResource:
                raise ValueError(f"pak listed {self.get_asset_type(asset_id)}, this case requires type_hint to be set")

            format_class = type_hint

        elif type_hint is not BaseResource and type_hint != format_class:
            raise ValueError(f"type_hint was {type_hint}, pak listed {format_class}")

        return format_class.parse(self.get_raw_asset(asset_id).data, target_game=self.target_game, asset_manager=self)

    def get_file(self, asset_id: NameOrAssetId, type_hint: type[T] = BaseResource) -> T:
        """
        Gets a file as from `get_parsed_asset` and keep it in memory.
        Modifications made to it are applied by `build_modified_files`.
        """
        asset_id = self.resolve_asset_id(asset_id)
        if asset_id not in self._memory_files:
            self._memory_files[asset_id] = self.get_parsed_asset(asset_id, type_hint=type_hint)
        return self._memory_files[asset_id]

    def _get_asset_in_memory_or_pak(self, asset_id: NameOrAssetId, type_hint: type[T] = BaseResource) -> T:
        """
        Gets a file from memory if present, otherwise parses it but does not keep it in memory.
        Useful for a read-only view when you aren't sure whether the asset is currently in memory.
        """
        asset_id = self.resolve_asset_id(asset_id)
        result = self._memory_files.get(asset_id)
        if result is not None:
            return result
        return self.get_parsed_asset(asset_id, type_hint=type_hint)

    # Adding new Files

    def _internal_add_modified_resource(
        self, name: str, asset_id: AssetId, new_data: Resource, keep_in_memory: bool
    ) -> None:

        if isinstance(new_data, BaseResource):
            logger.debug("Encoding %s (%s, %s)", asset_id, name, new_data.resource_type())
            raw_asset = RawResource(
                type=new_data.resource_type(),
                raw_data=new_data.build(),
            )
            self._modified_resources[asset_id] = raw_asset

            if keep_in_memory:
                self._memory_files[asset_id] = new_data

        else:
            raw_asset = new_data
            self._modified_resources[asset_id] = raw_asset

        self._clear_cached_dependencies_for_asset(asset_id)

    def add_new_asset(self, name: str, new_data: Resource) -> AssetId:
        """
        Adds an asset that doesn't already exist.
        :return: Asset id of the new asset.
        """
        asset_id = self.resolve_asset_id(name)
        self.register_custom_asset_name(name, asset_id)
        self._internal_add_modified_resource(name, asset_id, new_data, keep_in_memory=True)
        return asset_id

    def duplicate_asset(self, asset_id: AssetId, new_name: str) -> AssetId:
        """
        Creates a new asset named `new_name` with the contents of `asset_id`.
        Useful for the purposes of creating new assets as modifications of existing ones.
        :return: Asset id of the new asset.
        """
        return self.add_new_asset(new_name, self.get_raw_asset(asset_id))

    def replace_asset(self, asset_id: NameOrAssetId, new_data: Resource, *, keep_in_memory: bool = True) -> AssetId:
        """
        Replaces an existing asset.

        See `add_new_asset` for new assets.

        :param asset_id: The name or Asset ID for the asset being replaced.
        :param new_data: The new data, either in raw or parsed form.
        :param keep_in_memory: If `new_data` is a parsed resource, keep it in memory.

        :return: The resolved Asset ID of the replaced asset.
        """
        original_name = str(asset_id)
        asset_id = self.resolve_asset_id(asset_id)

        # Test if the asset exists
        if not self.does_asset_exists(asset_id):
            raise UnknownAssetId(asset_id, original_name)

        self._internal_add_modified_resource(original_name, asset_id, new_data, keep_in_memory)

        return asset_id

    def add_or_replace_custom_asset(self, name: str, new_data: Resource) -> AssetId:
        """Adds a new asset named `name`, or replaces an existing one if it already exists."""
        if self.does_asset_exists(name):
            return self.replace_asset(name, new_data)
        else:
            return self.add_new_asset(name, new_data)

    def ensure_present(self, pak_name: str, asset_id: NameOrAssetId) -> None:
        """
        Ensures the given pak has the given assets, collecting from other paks if needed.
        """

        self.pak_strategy.ensure_present(pak_name, asset_id)

    def get_pak(self, pak_name: str) -> Pak:
        # FIXME: delete
        return self.pak_group.get_pak(pak_name)

    ##################
    # Dependency Block

    def _clear_cached_dependencies_for_asset(self, asset_id: AssetId) -> None:
        self._cached_dependencies.pop(asset_id, None)
        self._cached_ancs_per_char_dependencies.pop(asset_id, None)

    def _get_dependencies_for_asset(
        self,
        asset_id: AssetId,
        must_exist: bool,
    ) -> Iterator[Dependency]:
        if not self.target_game.is_valid_asset_id(asset_id):
            return

        if not self.does_asset_exists(asset_id):
            if must_exist:
                raise UnknownAssetId(asset_id)
            return

        asset_type = self.get_asset_type(asset_id)

        dep_cache = self._cached_dependencies
        deps: tuple[Dependency, ...] = ()

        if asset_id in dep_cache:
            # logger.debug(f"Fetching cached asset {asset_id:#8x}...")
            deps = dep_cache[asset_id]
        else:
            # always calculate if the file is already in memory
            if asset_id in self._memory_files:
                should_calc = True

            # don't bother parsing the file if we have a quicker way to get its dependencies
            elif dependency_cheating.should_cheat_asset(asset_type):
                should_calc = False
                deps = tuple(dependency_cheating.get_cheated_dependencies(self.get_raw_asset(asset_id), self))

            # calculate dependencies if possible
            elif formats.has_resource_type(asset_type):
                should_calc = True

            # ideally this never happens!
            else:
                should_calc = False
                logger.warning(f"Potential missing assets for {asset_type} {asset_id}")

            if should_calc:
                if self.get_asset_format(asset_id).has_dependencies(self.target_game):
                    deps = tuple(self._get_asset_in_memory_or_pak(asset_id).dependencies_for())
                deps += tuple(self.target_game.special_ancs_dependencies(asset_id))

            # logger.debug(f"Adding {asset_id:#8x} deps to cache...")
            dep_cache[asset_id] = deps

        yield from deps
        yield Dependency(asset_type, asset_id, False)

    def get_dependencies_for_asset(self, asset_id: AssetId, *, must_exist: bool = False) -> Iterator[Dependency]:
        override = asset_id in self.target_game.mlvl_dependencies_to_ignore
        try:
            deps = self._get_dependencies_for_asset(asset_id, must_exist)
        except DependenciesHandledElsewhere:
            return
        for it in deps:
            yield Dependency(it.type, it.id, it.exclude_for_mlvl or override)

    def get_dependencies_for_ancs(self, asset_id: AssetId, char_index: int | None = None) -> Iterator[Dependency]:
        if not self.target_game.is_valid_asset_id(asset_id):
            return

        if (asset_type := self.get_asset_type(asset_id)) != "ANCS":
            raise ValueError(f"{hex(asset_id)} ({asset_type}) is not an ANCS!")

        if char_index is None:
            yield from self.get_dependencies_for_asset(asset_id)
            return

        if char_index in self._cached_ancs_per_char_dependencies[asset_id]:
            # logger.debug(f"Fetching cached asset {asset_id:#8x}...")
            deps = self._cached_ancs_per_char_dependencies[asset_id][char_index]
        else:
            deps_list = list(self.target_game.special_ancs_dependencies(asset_id))
            ancs: Ancs = self._get_asset_in_memory_or_pak(asset_id)
            deps_list.extend(ancs.ancs_dependencies_for(char_index=char_index))
            deps = tuple(deps_list)
            self._cached_ancs_per_char_dependencies[asset_id][char_index] = deps

        yield from deps
        yield Dependency("ANCS", asset_id)

    def _build_audio_group_dependency_table(self) -> None:
        atbl: Atbl | None = None
        agsc_ids: list[AssetId] = []

        for asset_id in self.all_asset_ids():
            asset_type = self.get_asset_type(asset_id)
            if asset_type == "ATBL":
                if atbl is not None:
                    logger.warning("Two ATBL files found!")
                atbl = self.get_parsed_asset(asset_id)
            elif asset_type == "AGSC":
                agsc_ids.append(asset_id)

        assert atbl is not None

        define_id_to_agsc: dict[int, AssetId | None] = {0xFFFF: None, -1: None}
        for agsc_id in agsc_ids:
            try:
                agsc = self.get_parsed_asset(agsc_id, type_hint=Agsc)
                for define_id in agsc.define_ids:
                    define_id_to_agsc[define_id] = agsc_id
            except Exception as e:
                raise Exception(f"Error parsing AGSC {hex(agsc_id)}: {e}")

        self._sound_id_to_agsc = {-1: None}
        for sound_id, define_id in enumerate(atbl.raw):
            if define_id in define_id_to_agsc:
                self._sound_id_to_agsc[sound_id] = define_id_to_agsc[define_id]

    def get_audio_group_dependency(self, sound_id: int) -> Iterator[Dependency]:
        if self._sound_id_to_agsc is None:
            self._build_audio_group_dependency_table()

        agsc = self._sound_id_to_agsc[sound_id]
        if agsc is None:
            return

        if self._audio_group_dependency is None:
            self._audio_group_dependency = tuple(
                self.get_file(asset_id, Dgrp) for asset_id in self.target_game.audio_group_dependencies()
            )

        dep = Dependency("AGSC", agsc, False)
        if any((dep in deps.direct_dependencies) for deps in self._audio_group_dependency):
            return
        else:
            yield dep

    ###########
    # Exporting

    def build_modified_files(self):
        """"""

        # flush dependencies before building to prevent inaccuracy
        self._cached_dependencies.clear()
        self._cached_ancs_per_char_dependencies.clear()

        with ThreadPoolExecutor() as executor:
            for name, resource in self._memory_files.items():
                executor.submit(self.replace_asset, name, resource, keep_in_memory=False)
        self._memory_files.clear()

    def _save_dol(self, output: FileWriter) -> None:
        if self.dol is not None:
            output.write_dol(self.dol.dol_file.getvalue())

    def _save_tweaks(self, output: FileWriter) -> None:
        if self.tweaks is not None:
            tweaks_bytes = self.tweaks.build()
            with output.open_binary("Standard.ntwk") as std_tweak:
                std_tweak.write(tweaks_bytes)

    def _write_custom_names(self, output: FileWriter) -> None:
        with output.open_text("custom_names.json") as f:
            json.dump(
                dict(self._custom_asset_ids.items()),
                f,
                indent=4,
            )

    def save_modifications(self, output: FileWriter) -> None:
        self.pak_strategy.export(output)
        self._save_dol(output)
        self._save_tweaks(output)
        self._write_custom_names(output)
        self._modified_resources = {}
        self._update_headers()

    def find_mlvl_for_mrea(self, mrea_id: AssetId) -> AssetId:
        """
        Searches all MLVL for the one that contains the given MREA as an area.
        Results are cached, so it'll be a fast operation in subsequent uses.

        :param mrea_id: Asset ID of the MREA to search for
        :return: Asset ID of the found MLVL
        :raise: KeyError, if no MLVL contains the given MREA
        """

        if self._mrea_to_mlvl is None:
            self._mrea_to_mlvl = {}
            for mlvl_id in self.all_asset_ids_of_type("MLVL"):
                mlvl = self._get_asset_in_memory_or_pak(mlvl_id)
                for area in mlvl.areas:
                    self._mrea_to_mlvl[area.mrea_asset_id] = mlvl_id

        return self._mrea_to_mlvl[mrea_id]
