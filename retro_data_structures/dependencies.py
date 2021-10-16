import logging
from typing import Iterator, Dict, Set, List, NamedTuple, Callable, Any

from retro_data_structures.asset_provider import AssetProvider, UnknownAssetId, InvalidAssetId
from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.formats import scan, dgrp, ancs, cmdl, evnt, part, AssetId, AssetType
from retro_data_structures.game_check import Game


class Dependency(NamedTuple):
    type: AssetType
    id: AssetId


class InvalidDependency(Exception):
    def __init__(self, this_asset_id: AssetId, dependency_id: AssetId, dependency_type: AssetType):
        super().__init__(
            f"Asset id 0x{this_asset_id:08X} has dependency 0x{dependency_id:08X} ({dependency_type}) "
            f"that can't be parsed."
        )
        self.this_asset_id = this_asset_id
        self.dependency_id = dependency_id
        self.dependency_type = dependency_type


def _no_dependencies(_obj, _target_game):
    pass


_formats_without_dependencies = {"txtr", "cskr", "cinf", "anim", "cspp", "strg"}

_dependency_functions = {
    "cmdl": cmdl.dependencies_for,
    "ancs": ancs.dependencies_for,
    "evnt": evnt.dependencies_for,
    "part": part.dependencies_for,
    "scan": scan.dependencies_for,
    "dgrp": dgrp.dependencies_for,
}


def format_has_dependencies(obj_type: AssetType):
    return obj_type.lower() not in _formats_without_dependencies


def direct_dependencies_for(obj, obj_type: AssetType, target_game: Game) -> Iterator[Dependency]:
    if format_has_dependencies(obj_type):
        yield from _dependency_functions[obj_type.lower()](obj, target_game)


def _internal_dependencies_for(
    get_asset: Callable[[AssetId], Any],
    target_game: Game,
    asset_id: AssetId,
    obj_type: AssetType,
    deps_by_asset_id: Dict[AssetId, Set[Dependency]],
):
    if asset_id in deps_by_asset_id:
        return

    deps_by_asset_id[asset_id] = {Dependency(obj_type, asset_id)}
    if not format_has_dependencies(obj_type):
        return

    obj = get_asset(asset_id)
    for new_type, new_asset_id in direct_dependencies_for(obj, obj_type, target_game):
        deps_by_asset_id[asset_id].add(Dependency(new_type, new_asset_id))
        try:
            _internal_dependencies_for(get_asset, target_game, new_asset_id, new_type, deps_by_asset_id)
        except UnknownAssetId:
            logging.warning(
                f"Asset id 0x{asset_id:08X} has dependency 0x{new_asset_id:08X} ({new_type}) " f"that doesn't exist."
            )
        except InvalidAssetId:
            raise InvalidDependency(asset_id, new_asset_id, new_type)


def recursive_dependencies_for(asset_provider: AssetProvider, asset_ids: List[AssetId]) -> Set[Dependency]:
    deps_by_asset_id: Dict[AssetId, Set[Dependency]] = {}

    for asset_id in asset_ids:
        obj_type = asset_provider.get_type_for_asset(asset_id)
        _internal_dependencies_for(
            asset_provider.get_asset, asset_provider.target_game, asset_id, obj_type, deps_by_asset_id
        )

    result = set()
    for deps in deps_by_asset_id.values():
        result.update(deps)

    return result


def all_converted_dependencies(asset_converter: AssetConverter) -> Dict[AssetId, Set[Dependency]]:
    deps_by_asset_id: Dict[AssetId, Set[Dependency]] = {}

    def get_asset(asset_id: AssetId):
        try:
            return asset_converter.converted_assets[asset_id].resource
        except KeyError:
            raise UnknownAssetId(asset_id) from None

    for converted in asset_converter.converted_assets.values():
        if converted.id not in deps_by_asset_id:
            _internal_dependencies_for(
                get_asset, asset_converter.target_game, converted.id, converted.type, deps_by_asset_id
            )

    return deps_by_asset_id
