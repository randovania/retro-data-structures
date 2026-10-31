"""
Computes the ordered list of resources for a pak.

Paks without MLVL (non-world paks):
- Each named resource, in the order of the named resources table, is preceded by its recursive dependencies.
  Each resource is included only once.

World paks, for each MLVL in the named resources table:
- Each area, in the order of the MLVL:
  - Echoes: the area's MLVL dependencies (geometry textures, then EGMC and PATH), the area name, then the
    dependencies of each layer, as listed in the MLVL. Only the ANCS characters the area uses are included.
  - Prime: the geometry textures and the textures used directly by objects, sorted by id. Then the dependencies of
    each object, using the order of the MLVL, except that each ANCS and everything it needs come together, where the
    first of them is listed. The layers are merged so that objects are sorted by id, while keeping the order of
    objects inside each layer. Then the area name, what the objects need that's packed with the area but not
    listed (like scans), the PATH and the MREA.
  - Each item is preceded by its recursive dependencies.
  - Some areas include again everything they need, even if it's already in the pak. Otherwise, only new resources
    are included.
- Then the skybox, the world name, the dark world name (Echoes), the SAVW, the MAPAs, the MAPW and the MLVL.

Dependencies of resources are listed in a specific order, see the `_*_direct_dependencies` methods.
Echoes' SCAN stores the list of everything it needs, which is used as is; the ANCS in it aren't expanded, since the
list already has what the shown characters need.

Exceptions to these rules are in `_UNCOMPRESSED_NAMED_RESOURCES`, `_EXTRA_DEPENDENCIES` and
`_PRIME_AREAS_WITH_UNKNOWN_OBJECT_ORDER`.
"""

from __future__ import annotations

import dataclasses
import heapq
import logging
import re
import typing

from retro_data_structures import formats
from retro_data_structures.base_resource import Dependency
from retro_data_structures.exceptions import DependenciesHandledElsewhere, UnknownAssetId
from retro_data_structures.formats import dependency_cheating, effect_script, meta_animation, meta_transition
from retro_data_structures.formats.mlvl import Mlvl
from retro_data_structures.formats.scan import Scan
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator

    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetId, AssetType, RawResource
    from retro_data_structures.formats.mlvl import Area
    from retro_data_structures.formats.script_object import ScriptInstance
    from retro_data_structures.properties.base_property import BaseObjectType

logger = logging.getLogger(__name__)

# Types whose dependencies are never packed alongside them.
_NO_PAK_DEPENDENCIES = {"MLVL", "MREA", "CSNG"}

# For effects, Retro's packer lists dependencies grouped by element, in this order. Elements not listed come last,
# in file order. Inferred from the relative order of dependencies across all vanilla paks.
_EFFECT_ELEMENT_ORDER = {
    "PART": ("TEXR", "TIND", "PMDL", "SSWH", "SELC", "ICTS", "IDTS", "IITS", "KSSM"),
    "ELSC": ("SSWH", "GPSM", "EPSM", "TEXR"),
    "WPSC": ("APSM", "APS2", "ASW1", "ASW2", "ASW3", "COLR", "OHEF", "B1TX", "B2TX", "TTEX"),
    "CRSC": (
        "DEFS",
        "DENM",
        "DCHR",
        "TALP",
        "DDCL",
        "WODL",
        "CODL",
        "MEDL",
        "GRDL",
        "ICDL",
        "GODL",
        "WTDL",
        "DESH",
    ),
    "DPSC": ("1TEX", "2TEX", "DMDL"),
}


_EFFECT_TYPES = {cls.resource_type(): cls for cls in effect_script.BaseEffect.__subclasses__()}


# Objects that can display any character of their ANCS, like the player with each suit.
_OBJECTS_WITH_ALL_CHARACTERS = {"PlayerActor", "WorldTeleporter"}

# Exception: Prime's NoARAM.pak starts with the suit models of the inventory screen and their dependencies, all
# uncompressed. These same resources are compressed in the other paks.
_UNCOMPRESSED_NAMED_RESOURCES = {
    (Game.PRIME, "noaram.pak"): re.compile(r"(CMDL|CSKR)_Inv\w*Suit\d"),
}

# Exception: resources that the vanilla paks include as dependencies of these resources, even though nothing
# references them.
_EXTRA_DEPENDENCIES: dict[tuple[Game, AssetId], tuple[AssetId, ...]] = {
    # Echoes, SamusGun.pak: gun_cmdl. game_check.special_ancs_dependencies has the same textures for an ANCS.
    (Game.ECHOES, 0x19AE626C): (0x607638EA, 0xCEA098FE, 0x578E51B8, 0x9E6F9531),
    # Echoes, SamusGunLow.pak: gunLowRes_cmdl
    (Game.ECHOES, 0x7F7385B1): (0x578E51B8, 0x9E6F9531),
    # Echoes, GGuiSys.pak and NoARAM.pak: DUMB_ScanHierarchy
    (Game.ECHOES, 0xDD79DC2A): (0xD05D3465, 0x94DD2E9C, 0xA815CA29),
    # Echoes, Metroid3.pak: a SCAN of a Space Pirate
    (Game.ECHOES, 0x8AF708D3): (0xB249E0EA, 0xD91BE71E, 0xBC65FDE5, 0xB12D7A58, 0xA67CC564),
    # Prime, Metroid3.pak: a CMDL
    (Game.PRIME, 0x87BFC431): (0xBB9590D9, 0x3901C7C4),
}

# Exception: the MREA of the Prime areas whose objects vanilla doesn't go through in the order of `_merge_layers`.
# Each layer keeps its order, but the layers are interleaved in an order that isn't in the game files.
_PRIME_AREAS_WITH_UNKNOWN_OBJECT_ORDER = frozenset(
    {
        # Metroid1.pak
        0xD1241219,  # Exterior Docking Hangar
        0xC5DE3C06,  # Biotech Research Area 2
        0x85578E54,  # Biotech Research Area 1
        # Metroid2.pak
        0xD5CDB809,  # Main Plaza
        0x165A4DE9,  # Ruined Fountain
        0x3C785450,  # Ruined Shrine
        0x18AB6106,  # Arboretum
        0x0D72F1F7,  # Tower of Light
        0xE34FD92B,  # Ruined Gallery
        0x47E73BC5,  # Gathering Hall
        0xC8309DF6,  # Hive Totem
        0x9A0A03EB,  # Sunchamber
        0x492CBF4A,  # Watery Hall
        0x4148F7B0,  # Burn Dome
        0x2E318473,  # Furnace
        0xFB54A0CB,  # Hall of the Elders
        0x361ECAAC,  # Reflecting Pool
        # Metroid3.pak
        0xF7285979,  # Phendrana Shorelines
        0xB33A0620,  # Ice Ruins West
        0x1921876D,  # Ruined Courtyard
        0xB51FCE29,  # Research Entrance
        0xD79EE805,  # Frozen Pike
        0xB3C33249,  # Control Tower
        0x21B4BFF6,  # Research Lab Aether
        # Metroid4.pak
        0xB9ABCD56,  # Frigate Crash Site
        0xBD8C8625,  # Root Cave
        0x2398E906,  # Artifact Temple
        0xAC2C58FE,  # Biohazard Containment
        # metroid5.pak
        0x956F1552,  # Mine Security Station
        0xC50AF17A,  # Elite Control
        0xAD2E7EB9,  # Phazon Processing Center
        0xBB3AFC4E,  # Metroid Quarantine B
    }
)


def has_compression_exceptions(game: Game, pak_name: str) -> bool:
    """If the given pak has resources that are uncompressed when they would be compressed elsewhere."""
    return (game, pak_name.lower()) in _UNCOMPRESSED_NAMED_RESOURCES


@dataclasses.dataclass(frozen=True)
class PakLayout:
    asset_ids: list[AssetId]
    """The resources of the pak, in order. Resources can be included more than once."""

    uncompressed: frozenset[AssetId] = frozenset()
    """Resources that must not be compressed in this pak, as exceptions to the usual rules."""


def _instance_properties(
    instances: Iterable[ScriptInstance], area: Area
) -> Iterator[tuple[ScriptInstance, BaseObjectType]]:
    for instance in instances:
        try:
            yield instance, instance.get_properties()
        except Exception as e:
            logger.warning("Unable to decode %s in %s: %s", instance, area.internal_name, e)


def _animation_parameters(obj: typing.Any, all_characters: bool) -> Iterator[tuple[AssetId, int | None]]:
    if type(obj).__name__ == "AnimationParameters":
        yield obj.ancs, None if all_characters else obj.character_index
    elif dataclasses.is_dataclass(obj):
        for field in dataclasses.fields(obj):
            yield from _animation_parameters(getattr(obj, field.name), all_characters)


def used_ancs_characters(manager: AssetManager, area: Area) -> Iterator[tuple[AssetId, int | None]]:
    """
    Lists which characters of which ANCS are used by objects in the given area, or by the scans it uses.
    `None` as the character means all characters are used.
    """
    for instance, properties in _instance_properties(area.all_instances, area):
        yield from _animation_parameters(properties, instance.script_type.__name__ in _OBJECTS_WITH_ALL_CHARACTERS)

    if manager.target_game >= Game.ECHOES:
        for dep in area.dependencies.all_dependencies:
            if dep.type == "SCAN":
                scan = manager.get_parsed_asset(dep.id, type_hint=Scan)
                yield from _animation_parameters(scan.scannable_object_info.get_properties(), False)


def find_duplicate_areas(resources: Iterable[tuple[AssetType, AssetId]]) -> dict[AssetId, bool]:
    """
    For the resources of a world pak, finds which areas include again everything they need. These are areas that
    contain a resource that was already in the pak before them.
    :return: A dict of MREA id to if the area is duplicated.
    """
    seen: set[AssetId] = set()
    area: set[AssetId] = set()
    duplicated = False
    result: dict[AssetId, bool] = {}

    for asset_type, asset_id in resources:
        if asset_id in seen and asset_id not in area:
            duplicated = True
        area.add(asset_id)
        if asset_type == "MREA":
            result[asset_id] = duplicated
            seen.update(area)
            area = set()
            duplicated = False

    return result


class _DirectDependencyManager:
    """
    Wraps an AssetManager so that `dependencies_for` of a resource lists only its direct dependencies,
    instead of the recursive list.
    """

    def __init__(self, manager: AssetManager):
        self._manager = manager

    def __getattr__(self, item: str) -> typing.Any:
        return getattr(self._manager, item)

    def get_dependencies_for_asset(self, asset_id: AssetId, *, must_exist: bool = False) -> Iterator[Dependency]:
        manager = self._manager
        if not manager.target_game.is_valid_asset_id(asset_id):
            return
        if not manager.does_asset_exists(asset_id):
            if must_exist:
                raise UnknownAssetId(asset_id)
            return
        yield Dependency(manager.get_asset_type(asset_id), asset_id)

    def get_dependencies_for_ancs(self, asset_id: AssetId, char_index: int | None = None) -> Iterator[Dependency]:
        # Paks always contain the entire ANCS, regardless of which character is used
        yield from self.get_dependencies_for_asset(asset_id)


class PakLayoutBuilder:
    def __init__(self, manager: AssetManager):
        self.manager = manager
        self.game = manager.target_game
        self._direct = _DirectDependencyManager(manager)
        self._direct_cache: dict[AssetId, tuple[AssetId, ...]] = {}
        self._expand_cache: dict[AssetId, tuple[AssetId, ...]] = {}
        self._used_characters: dict[AssetId, set[int]] = {}
        # Assets whose expansion depends on the used characters
        self._character_dependent: set[AssetId] = set()
        # The pak being built. The same id can have different contents in different paks, so the pak's own copy is
        # used when there's one.
        self._pak_name: str | None = None
        # Assets whose expansion depends on the pak being built
        self._pak_dependent: set[AssetId] = set()

    def _set_pak(self, pak_name: str) -> None:
        if pak_name == self._pak_name:
            return
        self._pak_name = pak_name
        for asset_id in self._pak_dependent:
            self._expand_cache.pop(asset_id, None)
            self._direct_cache.pop(asset_id, None)
        self._pak_dependent.clear()

    def _get_raw(self, asset_id: AssetId) -> RawResource:
        manager = self.manager
        paks = sorted(manager.pak_group.find_paks(asset_id)) if manager.pak_group.does_asset_exists(asset_id) else []
        if asset_id in manager._modified_resources or not paks:
            return manager.get_raw_asset(asset_id)

        if len(paks) > 1:
            self._pak_dependent.add(asset_id)
        result = manager.pak_group.get_raw_asset(asset_id, self._pak_name if self._pak_name in paks else paks[0])
        if result is None:
            raise UnknownAssetId(asset_id)
        return result

    def _parse(self, asset_id: AssetId) -> typing.Any:
        """Parses the asset, using a manager that gives only direct dependencies."""
        return self.manager.get_asset_format(asset_id).parse(
            self._get_raw(asset_id).data, target_game=self.game, asset_manager=self._direct
        )

    def _set_used_characters(self, used_characters: dict[AssetId, set[int]]) -> None:
        """
        In world paks, only the characters of an ANCS that are used by the area are included.
        ANCS not in the given dict include all characters.
        """
        if used_characters == self._used_characters:
            return
        self._used_characters = used_characters
        for asset_id in self._character_dependent:
            self._expand_cache.pop(asset_id, None)
            self._direct_cache.pop(asset_id, None)
        self._character_dependent.clear()

    # Dependencies

    def _ancs_direct_dependencies(self, asset_id: AssetId) -> Iterator[Dependency]:
        direct = self._direct
        raw = self._parse(asset_id).raw

        from retro_data_structures.formats.ancs import char_dependencies_for

        used_characters = self._used_characters.get(asset_id)
        characters = [
            (char_index, char)
            for char_index, char in enumerate(raw.character_set.characters)
            if used_characters is None or char_index in used_characters
        ]
        for _, char in characters:
            yield from char_dependencies_for(char, direct)

        # Only the animations of the used characters
        animations = list(enumerate(raw.animation_set.animations))
        if used_characters is not None:
            names = {anim.name for _, char in characters for anim in char.animation_names}
            animations = [(index, anim) for index, anim in animations if anim.name in names]

        # The primitive animations are sorted by name, ignoring case by comparing in upper case
        primitives: dict[AssetId, str] = {}

        def collect(meta: typing.Any) -> None:
            if meta.type == meta_animation.MetaAnimationType.Play:
                primitives.setdefault(meta.body.asset_id, meta.body.name)
            elif meta.type in (meta_animation.MetaAnimationType.Blend, meta_animation.MetaAnimationType.PhaseBlend):
                collect(meta.body.anim_a)
                collect(meta.body.anim_b)
            elif meta.type == meta_animation.MetaAnimationType.Random:
                for it in meta.body:
                    collect(it.animation)
            elif meta.type == meta_animation.MetaAnimationType.Sequence:
                for it in meta.body:
                    collect(it)

        for _, animation in animations:
            collect(animation.meta)

        # Transitions can also play animations
        animation_set = raw.animation_set
        transitions = [it.transition for it in animation_set.transitions]
        transitions.append(animation_set.default_transition)
        transitions.extend(it.transition for it in animation_set.half_transitions or [])
        for transition in transitions:
            if transition.type == meta_transition.MetaTransitionType.Animation:
                collect(transition.body)

        events = {}
        if raw.animation_set.animation_resources is not None:
            events = {res.anim_id: res.event_id for res in raw.animation_set.animation_resources}

        for anim_id, _ in sorted(primitives.items(), key=lambda it: it[1].upper()):
            if anim_id in events:
                yield from direct.get_dependencies_for_asset(events[anim_id])
            yield from direct.get_dependencies_for_asset(anim_id)

        if raw.animation_set.event_sets is not None:
            from retro_data_structures.formats import evnt

            char_filter = [None] if used_characters is None else [char_index for char_index, _ in characters]
            for index, _ in animations:
                for char_index in char_filter:
                    # The sounds are never included because of the ANCS. In world paks and in the LogBook,
                    # they're included because the MLVL or SCAN lists them.
                    yield from (
                        dep
                        for dep in evnt.dependencies_for(raw.animation_set.event_sets[index], direct, char_index)
                        if dep.type != "AGSC"
                    )

        yield from self.game.special_ancs_dependencies(asset_id)

    def _cmdl_direct_dependencies(self, asset_id: AssetId) -> Iterator[Dependency]:
        cmdl = self._parse(asset_id)
        for material_set in cmdl.raw.material_sets:
            texture_ids = material_set.texture_file_ids
            used = []
            for material in material_set.materials:
                # Retro's packer lists the first texture slot of each material last
                indices = list(material.texture_indices)
                for index in indices[1:] + indices[:1]:
                    used.append(texture_ids[index])
            used.extend(texture_ids)
            for texture_id in used:
                yield from self._direct.get_dependencies_for_asset(texture_id)

    def _effect_direct_dependencies(self, asset_id: AssetId, asset_type: AssetType) -> Iterator[Dependency]:
        effect_class = _EFFECT_TYPES[asset_type]
        effect = effect_class.parse(self._get_raw(asset_id).data, target_game=self.game, asset_manager=self._direct)
        texture_keys = set(effect_class.texture_keys())
        spawn_keys = set(effect_class.spawn_system_keys())
        id_keys = set(effect_class.asset_id_keys())

        by_element: list[tuple[str, int]] = []
        for element in effect.raw.elements:
            if element.type in texture_keys:
                if element.body.body is not None:
                    by_element.append((element.type, element.body.body.id))
            elif element.type in spawn_keys:
                if element.body.magic != "NONE":
                    for spawn in element.body.value.spawns:
                        for it in spawn.v2:
                            by_element.append((element.type, it.id))
            elif element.type in id_keys:
                if element.body is not None and element.body.body is not None:
                    by_element.append((element.type, element.body.body))

        order = _EFFECT_ELEMENT_ORDER.get(asset_type, ())
        by_element.sort(key=lambda it: order.index(it[0]) if it[0] in order else len(order))
        for _, dep_id in by_element:
            yield from self._direct.get_dependencies_for_asset(dep_id)

    def _calculate_direct_dependencies(self, asset_id: AssetId) -> Iterator[Dependency]:  # noqa: PLR0911
        manager = self.manager
        asset_type = manager.get_asset_type(asset_id)

        if asset_type in _NO_PAK_DEPENDENCIES:
            return

        if asset_type == "ANCS":
            yield from self._ancs_direct_dependencies(asset_id)
            return

        if asset_type == "SCAN" and self.game >= Game.ECHOES:
            # Echoes' SCAN stores the list of everything it needs, which already has only the used characters.
            for dep in self._parse(asset_id).raw.dependencies:
                yield from self._direct.get_dependencies_for_asset(dep.asset_id)
            return

        if asset_type == "CMDL" and self.game <= Game.ECHOES:
            yield from self._cmdl_direct_dependencies(asset_id)
            return

        if asset_type in _EFFECT_TYPES:
            yield from self._effect_direct_dependencies(asset_id, asset_type)
            return

        if dependency_cheating.should_cheat_asset(asset_type):
            yield from dependency_cheating.get_cheated_dependencies(self._get_raw(asset_id), self._direct)
            return

        if not formats.has_resource_type(asset_type):
            return

        format_class = manager.get_asset_format(asset_id)
        if not format_class.has_dependencies(self.game):
            return

        resource = self._parse(asset_id)
        try:
            yield from resource.dependencies_for()
        except DependenciesHandledElsewhere:
            return

    def direct_dependencies(self, asset_id: AssetId) -> tuple[AssetId, ...]:
        if asset_id not in self._direct_cache:
            result = []
            try:
                for dep in self._calculate_direct_dependencies(asset_id):
                    if dep.id != asset_id and dep.id not in result:
                        result.append(dep.id)
            except UnknownAssetId:
                pass
            for extra in _EXTRA_DEPENDENCIES.get((self.game, asset_id), ()):
                if extra not in result and self.manager.does_asset_exists(extra):
                    result.append(extra)
            self._direct_cache[asset_id] = tuple(result)
        return self._direct_cache[asset_id]

    def expand(self, asset_id: AssetId) -> tuple[AssetId, ...]:
        """All recursive dependencies of the given asset, dependencies first and the asset itself last."""
        if asset_id in self._expand_cache:
            return self._expand_cache[asset_id]

        if not self.manager.does_asset_exists(asset_id):
            return ()

        # Guard against cycles
        self._expand_cache[asset_id] = (asset_id,)

        result: dict[AssetId, None] = {}
        asset_type = self.manager.get_asset_type(asset_id)
        is_ancs = asset_type == "ANCS"
        for dep in self.direct_dependencies(asset_id):
            if asset_type == "SCAN" and self.game >= Game.ECHOES and self.manager.get_asset_type(dep) == "ANCS":
                # The SCAN already lists what's needed for the characters it shows
                result[dep] = None
                continue
            for it in self.expand(dep):
                result[it] = None
            if dep in self._character_dependent:
                is_ancs = True
            if dep in self._pak_dependent:
                self._pak_dependent.add(asset_id)
        if is_ancs:
            self._character_dependent.add(asset_id)
        result.pop(asset_id, None)
        result[asset_id] = None

        self._expand_cache[asset_id] = tuple(result)
        return self._expand_cache[asset_id]

    # Layouts

    def non_world_layout(self, named_resources: Iterable[AssetId], seen: set[AssetId] | None = None) -> list[AssetId]:
        """
        The resources for the given named resources, each preceded by its dependencies.
        :param seen: Resources to skip, which is updated with the new resources.
        """
        self._set_used_characters({})
        result: list[AssetId] = []
        if seen is None:
            seen = set()
        for asset_id in named_resources:
            for dep in self.expand(asset_id):
                if dep not in seen:
                    seen.add(dep)
                    result.append(dep)
        return result

    def _object_dependencies(self, properties: BaseObjectType) -> list[Dependency]:
        try:
            return list(properties.dependencies_for(self._direct))
        except Exception as e:
            logger.warning("Unable to get dependencies of %s: %s", properties, e)
            return []

    def _prime_area_items(self, area: Area) -> list[AssetId]:
        """
        Prime's packer goes through the objects of all layers, merged by their id, and lists each object's
        dependencies in the order the MLVL has them. Before that come the area's textures, sorted by id.
        """
        deps = area.dependencies
        non_layer = [dep.id for dep in deps.non_layer]
        path = [dep for dep in non_layer if self.manager.get_asset_type(dep) == "PATH"]

        # Objects are identified by (layer index, object index)
        ids_per_layer: list[list[int]] = []
        object_dependencies: dict[tuple[int, int], list[Dependency]] = {}
        # The MLVL layer list, split by which object introduced each item
        segments: dict[tuple[int, int], list[AssetId]] = {}

        for layer_index, (layer, layer_deps) in enumerate(zip(area.layers, deps.layers)):
            ids = []
            # The first object of the layer that uses each asset
            owner: dict[AssetId, tuple[int, int]] = {}
            for object_index, (instance, properties) in enumerate(_instance_properties(layer.instances, area)):
                key = (layer_index, object_index)
                ids.append(instance.id & 0xFFFF)
                object_dependencies[key] = self._object_dependencies(properties)
                segments[key] = []
                for dep in object_dependencies[key]:
                    for it in self.expand(dep.id):
                        owner.setdefault(it, key)

            # Items we can't explain go with the previous item
            current = (layer_index, 0) if ids else None
            for dep in layer_deps:
                current = owner.get(dep.id, current)
                if current is not None:
                    segments[current].append(dep.id)

            ids_per_layer.append(ids)

        merged = self._merge_layers(area, ids_per_layer, segments)

        textures = {dep for dep in non_layer if dep not in path}
        textures.update(dep.id for key in merged for dep in object_dependencies[key] if dep.type == "TXTR")
        items = sorted(textures)

        for key in merged:
            items.extend(self._prime_segment_items(segments[key]))
        items.append(area.name_strg_id)

        # What's packed with the area but not listed, like scans, comes last
        for key in merged:
            items.extend(dep.id for dep in object_dependencies[key] if dep.exclude_for_mlvl)
        items.extend(path)
        items.append(area.mrea_asset_id)
        return items

    def _prime_segment_items(self, segment: list[AssetId]) -> Iterator[AssetId]:
        """The items of an object's segment of the MLVL layer list, in the order the pak has them."""
        # The MLVL lists animations in the order each character uses them, but the pak has them in
        # the ANCS order instead.
        segment = [dep for dep in segment if self.manager.get_asset_type(dep) not in {"ANIM", "EVNT"}]

        # The MLVL only lists what the used characters need, but the pak has the whole ANCS. The pak has all of
        # it in the ANCS order, where the first of its resources is listed.
        ancs_of: dict[AssetId, AssetId] = {}
        for dep in segment:
            if self.manager.get_asset_type(dep) == "ANCS":
                for it in self.expand(dep):
                    ancs_of.setdefault(it, dep)

        for dep in segment:
            if dep in ancs_of:
                yield ancs_of[dep]
            yield dep

    def _merge_layers(
        self,
        area: Area,
        ids_per_layer: list[list[int]],
        segments: dict[tuple[int, int], list[AssetId]],
    ) -> list[tuple[int, int]]:
        """
        The order Prime's packer went through the objects of all layers, as (layer index, object index).
        Each layer keeps its order, and the layers are merged by taking the object with the lowest id among the
        next object of each layer.
        """
        return [
            (layer_index, object_index)
            for _, layer_index, object_index in heapq.merge(
                *(
                    [(object_id, layer_index, object_index) for object_index, object_id in enumerate(ids)]
                    for layer_index, ids in enumerate(ids_per_layer)
                )
            )
        ]

    def _area_items(self, area: Area) -> list[AssetId]:
        if self.game == Game.PRIME:
            return self._prime_area_items(area)

        deps = area.dependencies
        items: list[AssetId] = [dep.id for dep in deps.non_layer]
        items.append(area.name_strg_id)
        for layer in deps.layers:
            items.extend(dep.id for dep in layer)
        items.append(area.mrea_asset_id)
        return items

    def _area_used_characters(self, area: Area) -> dict[AssetId, set[int]]:
        used_characters: dict[AssetId, set[int]] = {}
        all_characters: set[AssetId] = set()
        for ancs_id, char_index in used_ancs_characters(self.manager, area):
            if char_index is None:
                all_characters.add(ancs_id)
            else:
                used_characters.setdefault(ancs_id, set()).add(char_index)
        for ancs_id in all_characters:
            used_characters.pop(ancs_id, None)
        return used_characters

    def world_layout(
        self,
        mlvl_ids: Iterable[AssetId],
        duplicate_area: Callable[[AssetId, AssetId], bool],
    ) -> list[AssetId]:
        result: list[AssetId] = []
        pak_seen: set[AssetId] = set()

        mlvl_ids = list(mlvl_ids)
        mlvls = [self.manager.get_file(mlvl_id, type_hint=Mlvl) for mlvl_id in mlvl_ids]

        def emit(asset_id: AssetId, local_seen: set[AssetId]) -> None:
            for dep in self.expand(asset_id):
                if dep not in local_seen:
                    local_seen.add(dep)
                    pak_seen.add(dep)
                    result.append(dep)

        for mlvl_id, mlvl in zip(mlvl_ids, mlvls):
            for area in mlvl.areas:
                if self.game >= Game.ECHOES:
                    # Prime always packs the entire ANCS, while Echoes only packs the characters each area uses
                    self._set_used_characters(self._area_used_characters(area))
                local_seen = set() if duplicate_area(mlvl_id, area.mrea_asset_id) else pak_seen
                for item in self._area_items(area):
                    emit(item, local_seen)

            raw = mlvl.raw
            tail = [raw.default_skybox_id, raw.world_name_id]
            if self.game == Game.ECHOES:
                tail.append(raw.dark_world_name_id)
            tail.append(raw.world_save_info_id)
            tail.extend(mlvl.mapw.raw.area_map)
            tail.append(raw.world_map_id)
            tail.append(mlvl_id)
            for item in tail:
                if self.game.is_valid_asset_id(item):
                    emit(item, pak_seen)

        return result

    def pak_layout(
        self,
        pak_name: str,
        named_resources: Iterable[tuple[str, AssetId]],
        duplicate_area: Callable[[AssetId, AssetId], bool],
    ) -> PakLayout:
        """
        The layout of a pak with the given named resources.
        :param duplicate_area: For world paks, if the area (mlvl id, mrea id) includes everything it needs again.
        """
        self._set_pak(pak_name)
        named_resources = list(named_resources)
        mlvl_ids = [asset_id for _, asset_id in named_resources if self.manager.get_asset_type(asset_id) == "MLVL"]
        others = [asset_id for _, asset_id in named_resources if asset_id not in mlvl_ids]

        result: list[AssetId] = []
        seen: set[AssetId] = set()
        uncompressed: set[AssetId] = set()

        if mlvl_ids:
            result.extend(self.world_layout(mlvl_ids, duplicate_area))
            seen.update(result)

        pattern = _UNCOMPRESSED_NAMED_RESOURCES.get((self.game, pak_name.lower()))
        if pattern is not None:
            group = [asset_id for name, asset_id in named_resources if pattern.fullmatch(name)]
            first = self.non_world_layout(group, seen)
            uncompressed.update(first)
            result.extend(first)

        result.extend(self.non_world_layout(others, seen))
        return PakLayout(result, frozenset(uncompressed))
