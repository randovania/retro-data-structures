import logging
from typing import Iterator, Tuple, Dict, Set, List

from retro_data_structures.asset_provider import AssetProvider, UnknownAssetId, InvalidAssetId
from retro_data_structures.formats import ancs, cmdl, evnt, part
from retro_data_structures.game_check import Game

Dependency = Tuple[str, int]


class InvalidDependency(Exception):
    def __init__(self, this_asset_id: int, dependency_id: int, dependency_type: str):
        super().__init__(f"Asset id 0x{this_asset_id:08X} has dependency 0x{dependency_id:08X} ({dependency_type}) "
                         f"that can't be parsed.")
        self.this_asset_id = this_asset_id
        self.dependency_id = dependency_id
        self.dependency_type = dependency_type


def _no_dependencies(_obj, _target_game):
    pass


_formats_without_dependencies = {
    "txtr",
    "cskr",
    "cinf",
    "anim",
    "cspp",
}

_dependency_functions = {
    "cmdl": cmdl.dependencies_for,
    "ancs": ancs.dependencies_for,
    "evnt": evnt.dependencies_for,
    "part": part.dependencies_for,
}


def format_has_dependencies(obj_type: str):
    return obj_type.lower() not in _formats_without_dependencies


def direct_dependencies_for(obj, obj_type: str, target_game: Game) -> Iterator[Dependency]:
    if format_has_dependencies(obj_type):
        yield from _dependency_functions[obj_type.lower()](obj, target_game)


def _internal_dependencies_for(asset_provider: AssetProvider, asset_id: int, obj_type: str,
                               deps_by_asset_id: Dict[int, Set[Dependency]]):
    if asset_id in deps_by_asset_id:
        return

    deps_by_asset_id[asset_id] = set()
    if not format_has_dependencies(obj_type):
        return

    obj = asset_provider.get_asset(asset_id)
    for new_type, new_asset_id in direct_dependencies_for(obj, obj_type, asset_provider.target_game):
        deps_by_asset_id[asset_id].add((new_type, new_asset_id))
        try:
            _internal_dependencies_for(asset_provider, new_asset_id, new_type, deps_by_asset_id)
        except UnknownAssetId:
            logging.warning(f"Asset id 0x{asset_id:08X} has dependency 0x{new_asset_id:08X} ({new_type}) "
                            f"that doesn't exist.")
        except InvalidAssetId:
            raise InvalidDependency(asset_id, new_asset_id, new_type)


def recursive_dependencies_for(asset_provider: AssetProvider, asset_ids: List[int]) -> Set[Dependency]:
    deps_by_asset_id: Dict[int, Set[Dependency]] = {}

    for asset_id in asset_ids:
        obj_type = asset_provider.get_type_for_asset(asset_id)
        _internal_dependencies_for(asset_provider, asset_id, obj_type, deps_by_asset_id)

    result = set()
    for deps in deps_by_asset_id.values():
        result.update(deps)

    return result
