from __future__ import annotations

import dataclasses
import typing
from collections import defaultdict
import logging
from typing import Iterator, Dict, NamedTuple, Optional, Set, List, Callable, Any, Union

from retro_data_structures import formats
from retro_data_structures.asset_provider import AssetProvider
from retro_data_structures.exceptions import UnknownAssetId, InvalidAssetId
from retro_data_structures.base_resource import AssetId, AssetType, BaseResource, Dependency, NameOrAssetId
from retro_data_structures.formats import scan, dgrp, ancs, cmdl, evnt, part
from retro_data_structures.formats.scan import Scan
from retro_data_structures.formats.script_layer import ScriptLayerHelper
from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty


if typing.TYPE_CHECKING:
    from retro_data_structures.conversion.asset_converter import AssetConverter
    from retro_data_structures.formats.mlvl import AreaWrapper


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


def recursive_dependencies_for(asset_manager: AssetManager,
                               asset_ids: List[AssetId],
                               ) -> Set[Dependency]:
    deps_by_asset_id: Dict[AssetId, Set[Dependency]] = {}

    def get_asset(aid: AssetId):
        return asset_manager.get_parsed_asset(aid).raw

    for asset_id in asset_ids:
        obj_type = asset_manager.get_asset_type(asset_id)
        _internal_dependencies_for(get_asset, asset_manager.target_game, asset_id, obj_type, deps_by_asset_id)

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


def recursive_dependencies_for_editor(editor: AssetProvider,
                                      asset_ids: List[AssetId],
                                      ) -> Set[Dependency]:
    deps_by_asset_id: Dict[AssetId, Set[Dependency]] = {}

    def _recursive(asset_id: AssetId):
        if asset_id in deps_by_asset_id:
            return

        raw_asset = editor.get_raw_asset(asset_id)
        deps_by_asset_id[asset_id] = {Dependency(raw_asset.type, asset_id)}

        try:
            format_class = formats.resource_type_for(raw_asset.type)
        except KeyError:
            return

        obj = format_class.parse(raw_asset.data, target_game=editor.game)

        for new_type, new_asset_id in obj.dependencies_for():
            deps_by_asset_id[asset_id].add(Dependency(new_type, new_asset_id))
            try:
                _recursive(new_asset_id)
            except UnknownAssetId:
                logging.warning(
                    f"Asset id 0x{asset_id:08X} has dependency 0x{new_asset_id:08X} ({new_type}) " f"that doesn't exist."
                )
            except InvalidAssetId:
                raise InvalidDependency(asset_id, new_asset_id, new_type)

    for it in asset_ids:
        _recursive(it)

    result = set()
    for deps in deps_by_asset_id.values():
        result.update(deps)

    return result


def recursive_dependencies(asset_manager: AssetManager, asset_id: NameOrAssetId) -> Iterator[Dependency]:
    asset_type = asset_manager.get_asset_type(asset_id)
    yield asset_type, asset_id

    resource_type = formats.resource_type_for(asset_type)
    if not resource_type.has_dependencies():
        return

    resource: BaseResource = asset_manager.get_parsed_asset(asset_id)
    
    for dependency in resource.dependencies_for():
        yield from recursive_dependencies(asset_manager, dependency)


@dataclasses.dataclass()
class AncsUsage:
    characters: set[int] = dataclasses.field(default_factory=set)
    animations: set[int] = dataclasses.field(default_factory=set)


class AncsUsageDependencies:
    usages: Dict[AssetId, AncsUsage]
    _ancs: Dict[AssetId, ancs.Ancs]

    asset_provider: AssetProvider

    def __init__(self, asset_manager: AssetProvider):
        self.asset_provider = asset_manager
        self.usages = defaultdict(AncsUsage)
        self._ancs = {}
    
    def _get_property_usages(self, prop: BaseProperty):
        from retro_data_structures.properties.prime.core import AnimationParameters as p1Anim
        from retro_data_structures.properties.echoes.core import AnimationParameters as p2Anim
        from retro_data_structures.properties.corruption.core import AnimationParameters as p3Anim
        if isinstance(prop, (p1Anim.AnimationParameters, p2Anim.AnimationParameters, p3Anim.AnimationParameters)):
            if not self.asset_provider.game.is_valid_asset_id(prop.ancs):
                return

            self.usages[prop.ancs].characters.add(prop.character_index)
            if prop.ancs not in self._ancs:
                self._ancs[prop.ancs] = self.asset_provider.get_parsed_asset(prop.ancs, type_hint=ancs.Ancs)
            self.usages[prop.ancs].animations = self.usages[prop.ancs].animations.union(self._ancs[prop.ancs].get_used_animations(prop.character_index))
            return

        for dependency in prop.mlvl_dependencies_for():
            if self.asset_provider.game.is_valid_asset_id(dependency):
                self._recursive_get_usages(dependency)

    def _get_resource_usages(self, resource: NameOrAssetId):
        asset_type = self.asset_provider.get_asset_type(resource)
        if asset_type != "SCAN":
            return
        
        scan_asset = self.asset_provider.get_parsed_asset(resource, type_hint=Scan)
        self._get_property_usages(scan_asset.scannable_object_info.get_properties())
    
    def _recursive_get_usages(self, dependency: Union[BaseProperty, NameOrAssetId]):
        if isinstance(dependency, BaseProperty):
            self._get_property_usages(dependency)
        else:
            self._get_resource_usages(dependency)

    def find_usage_for_area(self, area: AreaWrapper):
        raise NotImplementedError()
    
    def find_usage_for_layer(self, layer: ScriptLayerHelper):
        self.usages = defaultdict(AncsUsage)

        for instance in layer.instances:
            self._recursive_get_usages(instance.get_properties())


class MlvlDependencies:
    ancs_usage: AncsUsageDependencies
    _ancs_id: Optional[AssetId]
    _is_character_actor: bool
    _char_id: Optional[int]
    _properties_to_skip: set[str]

    asset_manager: AssetManager

    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager
        self.ancs_usage = AncsUsageDependencies(asset_manager)
        self._reset()
    
    def _reset(self):
        self._ancs_id = None
        self._char_id = None
        self._is_character_actor = False
        self._properties_to_skip = set()
    
    @property
    def game(self) -> Game:
        return self.asset_manager.game

    def _get_property_dependencies(self, prop: BaseProperty):
        dep_type = type(prop).__name__

        if dep_type == "StreamedAudio":
            yield from []
            return

        if dep_type == "PlayerActor":
            self._is_character_actor = True
            if self.game == Game.CORRUPTION:
                self._properties_to_skip = self._properties_to_skip.union(
                    {f"{suit}_model" for suit in {"varia_suit", "varia_suit_grapple", "stage01_suit", "stage02_suit", "stage03_suit", "stage04_suit"}},
                    {f"{suit}_skin_rule" for suit in {"varia_suit", "varia_suit_grapple", "stage01", "stage02", "stage03", "stage04"}}
                )
        
        elif dep_type == "AnimationParameters" and self.game <= Game.ECHOES:
            if self._is_character_actor:
                if self.game == Game.PRIME:
                    self._char_id = 5
                elif self.game == Game.ECHOES:
                    self._char_id = 3
            else:
                self._char_id = prop.character_index
        
        for dependency in prop.mlvl_dependencies_for(self._properties_to_skip):
            yield from self._inner_mlvl_dependencies(dependency)

        if dep_type == "AnimationParameters":
            self._char_id = None
        
        elif dep_type == "PlayerActor":
            self._is_character_actor = False
            self._properties_to_skip = set()

    def _get_resource_dependencies(self, asset_id: NameOrAssetId):
        if not self.game.is_valid_asset_id(asset_id):
            return

        asset_type = self.asset_manager.get_asset_type(asset_id)

        if asset_type == "SCAN" and self.game == Game.PRIME:
            yield from []
            return
        
        yield asset_type, asset_id

        resource_type = formats.resource_type_for(asset_type)
        if not resource_type.has_dependencies():
            return
        
        resource: BaseResource = self.asset_manager.get_parsed_asset(asset_id)

        for dep in resource.mlvl_dependencies_for(self):
            yield from self._inner_mlvl_dependencies(dep)

    def _inner_mlvl_dependencies(self, dependency: Union[NameOrAssetId, BaseProperty]):
        if isinstance(dependency, BaseProperty):
            yield from self._get_property_dependencies(dependency)
        else:
            yield from self._get_resource_dependencies(dependency)
    
    def recursive_dependencies(self, dependency: Union[NameOrAssetId, BaseProperty]):
        self._reset()
        
        yield from self._inner_mlvl_dependencies(dependency)

    def recursive_dependencies_for_layer(self, layer: ScriptLayerHelper):
        self.ancs_usage = AncsUsageDependencies(self.asset_manager)
        self.ancs_usage.find_usage_for_layer(layer)

        for instance in layer.instances:
            yield from self.recursive_dependencies(instance.get_properties())
