from typing import Iterator, Tuple, Dict, Set, List

from retro_data_structures.asset_provider import AssetProvider
from retro_data_structures.formats import ancs, cmdl, evnt

Dependency = Tuple[str, int]


def _no_dependencies(_obj, _target_game):
    pass


_formats_without_dependencies = {
    "txtr",
    "cskr",
    "cinf",
    "anim",
}

_dependency_functions = {
    "cmdl": cmdl.dependencies_for,
    "ancs": ancs.dependencies_for,
    "evnt": evnt.dependencies_for,
}


def format_has_dependencies(obj_type: str):
    return obj_type.lower() not in _formats_without_dependencies


def direct_dependencies_for(obj, obj_type: str, target_game: int) -> Iterator[Dependency]:
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
        _internal_dependencies_for(asset_provider, new_asset_id, new_type, deps_by_asset_id)


def recursive_dependencies_for(asset_provider: AssetProvider, asset_ids: List[int]) -> Set[Dependency]:
    deps_by_asset_id: Dict[int, Set[Dependency]] = {}

    for asset_id in asset_ids:
        obj_type = asset_provider.resource_by_asset_id[asset_id].asset.type
        _internal_dependencies_for(asset_provider, asset_id, obj_type, deps_by_asset_id)

    result = set()
    for deps in deps_by_asset_id.values():
        result.update(deps)

    return result
