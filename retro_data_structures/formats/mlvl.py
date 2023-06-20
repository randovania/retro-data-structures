"""
Wiki: https://wiki.axiodl.com/w/MLVL_(File_Format)
"""
from __future__ import annotations

import itertools
import typing
from itertools import count
from typing import Iterator

import construct
from construct import (
    Adapter,
    Array,
    Bitwise,
    Const,
    Container,
    CString,
    Error,
    Flag,
    Float32b,
    FocusedSeq,
    Int8ub,
    Int16ub,
    Int32ub,
    ListContainer,
    Peek,
    PrefixedArray,
    Sequence,
    Struct,
    Switch,
    len_,
)

from retro_data_structures.adapters.offset import OffsetAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency, NameOrAssetId
from retro_data_structures.common_types import AssetId32, AssetId64, FourCC, Vector3
from retro_data_structures.construct_extensions.misc import PrefixedArrayWithExtra
from retro_data_structures.exceptions import UnknownAssetId
from retro_data_structures.formats import Mapw
from retro_data_structures.formats.cmdl import dependencies_for_material_set
from retro_data_structures.formats.guid import GUID
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.savw import Savw
from retro_data_structures.formats.script_layer import ScriptLayerHelper, new_layer
from retro_data_structures.formats.script_object import InstanceId, ScriptInstanceHelper
from retro_data_structures.formats.strg import Strg
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager

MLVLConnectingDock = Struct(
    area_index=Int32ub,
    dock_index=Int32ub,
)

MLVLDock = Struct(
    connecting_dock=PrefixedArray(Int32ub, MLVLConnectingDock),
    dock_coordinates=PrefixedArray(Int32ub, Vector3),
)

MLVLMemoryRelay = Struct(
    memory_relay_index=Int32ub,
    target_index=Int32ub,
    message=Int16ub,
    active=Int8ub,
)


class LayerFlags(Adapter):
    def __init__(self):
        super().__init__(Struct(
            layer_count=Int32ub,
            layer_flags=Bitwise(Array(64, Flag)),
        ))

    def _decode(self, obj, context, path):
        return ListContainer(reversed(obj.layer_flags))[:obj.layer_count]

    def _encode(self, obj, context, path):
        flags = [True for i in range(64)]
        flags[:len(obj)] = obj
        return Container({
            "layer_count": len(obj),
            "layer_flags": list(reversed(flags))
        })


class LayerNameOffsetAdapter(OffsetAdapter):
    def _get_table(self, context):
        return context._.layer_names

    def _get_table_length(self, context):
        return len(self._get_table(context))

    def _get_item_size(self, item):
        return len(item.encode('utf-8'))


class AreaDependencyOffsetAdapter(OffsetAdapter):
    def _get_table(self, context):
        return context._.dependencies_b

    def _get_table_length(self, context):
        return len_(self._get_table(context))

    def _get_item_size(self, item):
        return 8


def create_area(version: int, asset_id):
    MLVLAreaDependency = Struct(
        asset_id=asset_id,
        asset_type=FourCC,
    )

    # TODO: better offset stuff
    MLVLAreaDependencies = Struct(
        Const(0, Int32ub),
        "dependencies" / PrefixedArray(Int32ub, MLVLAreaDependency),
        "offsets" / PrefixedArray(Int32ub, Int32ub),
    )

    area_fields = [
        "area_name_id" / asset_id,
        "area_transform" / Array(12, Float32b),
        "area_bounding_box" / Array(6, Float32b),
        "area_mrea_id" / asset_id,
        "internal_area_id" / asset_id,
    ]

    # DKCR
    if version < 0x1B:
        area_fields.append("attached_area_index" / PrefixedArray(Int32ub, Int16ub))

    # Corruption
    if version < 0x19:
        area_fields.append("dependencies" / MLVLAreaDependencies)

    area_fields.append("docks" / PrefixedArray(Int32ub, MLVLDock))

    # Echoes
    if version == 0x17:
        area_fields.append(
            "module_dependencies"
            / Struct(
                rel_module=PrefixedArray(Int32ub, CString("utf-8")),
                rel_offset=PrefixedArray(Int32ub, Int32ub),
            )
        )

    # DKCR
    if version >= 0x1B:
        # Unknown, always 0?
        area_fields.append(Const(0, Int32ub))

    # Prime 2 Demo
    if version >= 0x14:
        area_fields.append("internal_area_name" / CString("utf-8"))

    return Struct(*area_fields)


def create(version: int, asset_id):
    area = create_area(version, asset_id)

    fields = [
        "magic" / Const(0xDEAFBABE, Int32ub),
        "version" / Const(version, Int32ub),
        "world_name_id" / asset_id,
    ]

    # Prime 2
    if version == 0x17:
        fields.append("dark_world_name_id" / asset_id)

    # Prime 2 and 3
    if 0x17 <= version <= 0x19:
        fields.append("temple_key_world_index" / Int32ub)

    # TODO: time attack for DKCR

    fields.extend(
        [
            "world_save_info_id" / asset_id,
            "default_skybox_id" / asset_id,
        ]
    )

    # Prime 1
    if version <= 0x11:
        # Array describing all outgoing Memory Relay connections in this world.
        # Memory Relays connected to multiple objects are listed multiple times.
        fields.append("memory_relays" / PrefixedArray(Int32ub, MLVLMemoryRelay))

    # Prime 1
    if version <= 0x11:
        # Extra field is unknown, always 1
        fields.append("areas" / PrefixedArrayWithExtra(Int32ub, Const(1, Int32ub), area))
    else:
        fields.append("areas" / PrefixedArray(Int32ub, area))

    # DKCR
    if version <= 0x1B:
        fields.append("world_map_id" / asset_id)  # MAPW

        # This is presumably the same unknown value as at the beginning of the SCLY format. Always 0.
        fields.append("unknown_scly_field" / Const(0, Int8ub))

        # The MLVL format embeds a script layer. This script layer is used in the MP1 demo for storing Dock instances,
        # but it's unused in all retail builds, so this is always 0.
        fields.append("script_instance_count" / Const(0x0, Int32ub))

    # Prime 1
    if version <= 0x11:
        fields.append(
            "audio_group"
            / PrefixedArray(
                Int32ub,
                Struct(
                    group_id=Int32ub,
                    agsc_id=asset_id,
                ),
            )
        )

        # Unknown purpose, always empty
        fields.append(CString("utf-8"))

    fields.extend(
        [
            "area_layer_flags" / PrefixedArray(Int32ub, LayerFlags()),
            "layer_names" / PrefixedArray(Int32ub, CString("utf-8")),
        ]
    )

    # Corruption
    if version >= 0x19:
        fields.append("layer_guid" / PrefixedArray(Int32ub, GUID))

    fields.append("area_layer_name_offset" / PrefixedArray(Int32ub, Int32ub))

    return Struct(*fields)


Prime1MLVL = create(0x11, AssetId32)
Prime2MLVL = create(0x17, AssetId32)
Prime3MLVL = create(0x19, AssetId64)

MLVL = FocusedSeq(
    "mlvl",
    header=Peek(Sequence(Int32ub, Int32ub)),
    mlvl=Switch(
        lambda this: this.header[1] if this._parsing else this.mlvl.version,
        {
            0x11: Prime1MLVL,
            0x17: Prime2MLVL,
            0x19: Prime3MLVL,
        },
        Error,
    ),
)


_hardcoded_dependencies: dict[int, dict[str, list[Dependency]]] = {
    0xD7C3B839: {
        # Sanctum
        "Default": [("TXTR", 0xd5b9e5d1)],
        "Emperor Ing Stage 1": [("TXTR", 0x52c7d438)],
        "Emperor Ing Stage 3": [("TXTR", 0xd5b9e5d1)],
        "Emperor Ing Stage 1 Intro Cine": [("TXTR", 0x52c7d438)],
        "Emperor Ing Stage 3 Death Cine": [("TXTR", 0xd5b9e5d1)],
    },
    0xA92F00B3: {
        # Hive Temple
        "CliffsideBoss": [
            ("TXTR", 0x24149e16),
            ("TXTR", 0xbdb8a88a),
            ("FSM2", 0x3d31822b),
        ]
    },
    0xC0113CE8: {
        # Dynamo Works
        "3rd Pass": [("RULE", 0x393ca543)]
    },
    0x5571E89E: {
        # Hall of Combat Mastery
        "2nd Pass Enemies": [("RULE", 0x393ca543)]
    },
    0x7B94B06B: {
        # Hive Portal Chamber
        "1st Pass": [("RULE", 0x393ca543)],
        "2nd Pass": [("RULE", 0x393ca543)]
    },
    0xF8DBC03D: {
        # Hive Reactor
        "2nd Pass": [("RULE", 0x393ca543)]
    },
    0xB666B655: {
        # Reactor Access
        "2nd Pass": [("RULE", 0x393ca543)]
    },
    0xE79AAFAE: {
        # Transport A Access
        "2nd Pass": [("RULE", 0x393ca543)]
    },
    0xFEB7BD27: {
        # Transport B Access
        "Default": [("RULE", 0x393ca543)]
    },
    0x89D246FD: {
        # Portal Access
        "Default": [("RULE", 0x393ca543)]
    },
    0x0253782D: {
        # Dark Forgotten Bridge
        "Default": [("RULE", 0x393ca543)]
    },
    0x09DECF21: {
        # Forgotten Bridge
        "Default": [("RULE", 0x393ca543)]
    },
    0x629790F4: {
        # Sacrificial Chamber
        "1st Pass": [("RULE", 0x393ca543)]
    },
    0xBBE4B3AE: {
        # Dungeon
        "Default": [("TXTR", 0xe252e7f6)]
    },
    0x2BCD44A7: {
        # Portal Terminal
        "Default": [("TXTR", 0xb6fa5023)]
    },
    0xC68B5B51: {
        # Transport to Sanctuary Fortress
        "!!non_layer!!": [("TXTR", 0x75a219a8)]
    },
    0x625A2692: {
        # Temple Transport Access
        "!!non_layer!!": [("TXTR", 0x581c56ea)]
    },
    0x96F4CA1E: {
        # Minigyro Chamber
        "Default": [("TXTR", 0xac080dfb)]
    },
    0x5BBF334F: {
        # Staging Area
        "!!non_layer!!": [("TXTR", 0x738feb19)]
    }
}


class AreaWrapper:
    _flags: Container
    _layer_names: ListContainer
    _index: int

    _mrea: Mrea = None
    _strg: Strg = None

    # FIXME: since the whole Mlvl is now being passed, this function can have the other arguments removed
    def __init__(self, raw: Container, asset_manager: AssetManager, flags: Container, names: Container,
                 index: int, parent_mlvl: Mlvl):
        self._raw = raw
        self.asset_manager = asset_manager
        self._flags = flags
        self._layer_names = names
        self._index = index
        self._parent_mlvl = parent_mlvl

    @property
    def id(self) -> int:
        return self._raw.internal_area_id

    @property
    def index(self) -> int:
        return self._index

    @property
    def name(self) -> str:
        try:
            return self.strg.strings[0]
        except UnknownAssetId:
            return "!!" + self.internal_name

    @name.setter
    def name(self, value):
        self.strg.set_string(0, value)

    @property
    def internal_name(self) -> str:
        return self._raw.get("internal_area_name", "Unknown")

    @property
    def strg(self) -> Strg:
        if self._strg is None:
            self._strg = self.asset_manager.get_file(self._raw.area_name_id, type_hint=Strg)
        return self._strg

    @property
    def mrea(self) -> Mrea:
        if self._mrea is None:
            self._mrea = self.asset_manager.get_file(self.mrea_asset_id, type_hint=Mrea)
        return self._mrea

    @property
    def mrea_asset_id(self) -> int:
        return self._raw.area_mrea_id

    @property
    def layers(self) -> Iterator[ScriptLayerHelper]:
        for layer in self.mrea.script_layers:
            yield layer.with_parent(self)

    @property
    def generated_objects_layer(self) -> ScriptLayerHelper:
        return self.mrea.generated_objects_layer

    def get_layer(self, name: str) -> ScriptLayerHelper:
        return next(layer for layer in self.layers if layer.name == name)

    def add_layer(self, name: str, active: bool = True) -> ScriptLayerHelper:
        index = len(self._layer_names)
        self._layer_names.append(name)
        self._flags.append(active)
        raw = new_layer(index, self.asset_manager.target_game)
        self.mrea._raw.sections.script_layer_section.append(raw)
        return self.get_layer(name)

    @property
    def next_instance_id(self) -> int:
        ids = [instance.id.instance for layer in self.layers for instance in layer.instances]
        return next(i for i in count() if i not in ids)

    def get_instance(self, instance_id: typing.Union[int, InstanceId]) -> typing.Optional[ScriptInstanceHelper]:
        if not isinstance(instance_id, InstanceId):
            instance_id = InstanceId(instance_id)

        for layer in self.layers:
            if instance_id.layer == layer.index:
                return layer.get_instance(instance_id)

        return None

    def get_instance_by_name(self, name: str) -> ScriptInstanceHelper:
        return self.mrea.get_instance_by_name(name)

    def _raw_connect_to(self, source_dock_number: int, target_area: AreaWrapper, target_dock_number: int):
        source_dock = self._raw.docks[source_dock_number]
        assert len(source_dock.connecting_dock) == 1, "Only docks with one connection supported"
        source_dock.connecting_dock[0].area_index = target_area._index
        source_dock.connecting_dock[0].dock_index = target_dock_number

        attached_area_index = []
        for docks in self._raw.docks:
            for c in docks.connecting_dock:
                if c.area_index not in attached_area_index:
                    attached_area_index.append(c.area_index)
        self._raw.attached_area_index = construct.ListContainer(attached_area_index)

    def connect_dock_to(self, source_dock_number: int, target_area: AreaWrapper, target_dock_number: int):
        self._raw_connect_to(source_dock_number, target_area, target_dock_number)
        target_area._raw_connect_to(target_dock_number, self, source_dock_number)

    def build_non_layer_dependencies(self) -> typing.Iterator[Dependency]:
        if self.asset_manager.target_game <= Game.ECHOES:
            geometry_section = self.mrea.get_raw_section("geometry_section")
            if geometry_section:
                for asset_id in PrefixedArray(Int32ub, AssetId32).parse(geometry_section[0]):
                    yield from self.asset_manager.get_dependencies_for_asset(asset_id, True)
        else:
            geometry = self.mrea.get_geometry()
            if geometry is not None:
                yield from dependencies_for_material_set(geometry[0].materials, self.asset_manager, True)

        valid_asset = self.asset_manager.target_game.is_valid_asset_id
        if valid_asset(portal_area := self.mrea.get_portal_area()):
            yield "PTLA", portal_area
        if valid_asset(static_geometry_map := self.mrea.get_static_geometry_map()):
            yield "EGMC", static_geometry_map
        if valid_asset(path := self.mrea.get_path()):
            yield "PATH", path

    def build_scgn_dependencies(self, layer_deps: list[list[Dependency]], only_modified: bool = False):
        layer_deps = list(layer_deps)

        layers = list(self.layers)
        for instance in self.generated_objects_layer.instances:
            inst_layer = instance.id.layer
            if not only_modified or layers[inst_layer].is_modified:
                layer_deps[inst_layer].extend(instance.mlvl_dependencies_for(self.asset_manager))

        return [list(dict.fromkeys(deps)) for deps in layer_deps]

    def build_mlvl_dependencies(self, only_modified: bool = False):
        layer_deps = [
            list(
                layer.build_mlvl_dependencies(self.asset_manager)
                if (not only_modified) or layer.is_modified() else
                layer.dependencies
            ) for layer in self.layers
        ]

        if only_modified:
            # assume we never modify these
            layer_deps.append(list(self.non_layer_dependencies))
        else:
            non_layer_deps = list(self.build_non_layer_dependencies())
            if "!!non_layer!!" in _hardcoded_dependencies.get(self.mrea_asset_id, {}):
                non_layer_deps.extend(_hardcoded_dependencies[self.mrea_asset_id]["!!non_layer!!"])
            layer_deps.append(non_layer_deps)


        layer_deps = self.build_scgn_dependencies(layer_deps, only_modified)

        if self.mrea_asset_id in _hardcoded_dependencies:
            for layer_name, missing in _hardcoded_dependencies[self.mrea_asset_id].items():
                if layer_name == "!!non_layer!!":
                    continue

                layer = self.get_layer(layer_name)
                if only_modified and not layer.is_modified:
                    continue

                layer_deps[layer.index].extend(missing)

        offset = 0
        offsets = []
        for layer in layer_deps:
            offsets.append(offset)
            offset += len(layer)

        deps = list(itertools.chain(*layer_deps))
        deps = [Container(asset_type=typ, asset_id=idx) for typ, idx in deps]
        self._raw.dependencies.dependencies = deps
        self._raw.dependencies.offsets = offsets

    @property
    def layer_dependencies(self):
        return {
            layer.name: list(layer.dependencies)
            for layer in self.layers
        }

    @property
    def all_layer_deps(self):
        deps = set()
        for layer_deps in self.layer_dependencies.values():
            deps.update(dep["asset_id"] for dep in layer_deps)
        return deps

    @property
    def non_layer_dependencies(self):
        deps = self._raw.dependencies
        global_deps = deps.dependencies[deps.offsets[len(self._layer_names)]:]
        yield from [(dep.asset_type, dep.asset_id) for dep in global_deps]

    @property
    def dependencies(self):
        deps = self.layer_dependencies
        deps["!!non_layer!!"] = list(self.non_layer_dependencies)
        return deps


class Mlvl(BaseResource):
    _mapw: Mapw = None
    _savw: Savw = None

    @classmethod
    def resource_type(cls) -> AssetType:
        return "MLVL"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return MLVL

    def dependencies_for(self, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
        raise NotImplementedError()

    def __repr__(self) -> str:
        try:
            if self.asset_manager.target_game == Game.ECHOES:
                return f"{self.world_name} ({self.dark_world_name})"
            return self.world_name
        except UnknownAssetId:
            return super().__repr__()

    @property
    def areas(self) -> Iterator[AreaWrapper]:
        offsets = self._raw.area_layer_name_offset
        names = self._raw.layer_names
        for i, area in enumerate(self._raw.areas):
            area_layer_names = names[offsets[i]:] if i == len(self._raw.areas) - 1 else names[offsets[i]:offsets[i+1]]
            yield AreaWrapper(area, self.asset_manager, self._raw.area_layer_flags[i], area_layer_names, i, self)

    def get_area(self, asset_id: NameOrAssetId) -> AreaWrapper:
        return next(area for area in self.areas if area.mrea_asset_id == self.asset_manager._resolve_asset_id(asset_id))

    _name_strg_cached: Strg = None
    _dark_strg_cached: Strg = None

    @property
    def _name_strg(self) -> Strg:
        if self._name_strg_cached is None:
            self._name_strg_cached = self.asset_manager.get_file(self._raw.world_name_id, type_hint=Strg)
        return self._name_strg_cached

    @property
    def _dark_strg(self) -> Strg:
        if self.asset_manager.target_game != Game.ECHOES:
            raise ValueError("Only Echoes has dark world names.")
        if self._dark_strg_cached is None:
            self._dark_strg_cached = self.asset_manager.get_file(self._raw.dark_world_name_id, type_hint=Strg)
        return self._dark_strg_cached

    @property
    def world_name(self) -> str:
        return self._name_strg.strings[0]

    @world_name.setter
    def world_name(self, value: str):
        self._name_strg.set_string(0, value)

    @property
    def dark_world_name(self) -> str:
        return self._dark_strg.strings[0]

    @dark_world_name.setter
    def dark_world_name(self, value: str):
        self._dark_strg.set_string(0, value)

    @property
    def mapw(self) -> Mapw:
        if self._mapw is None:
            self._mapw = self.asset_manager.get_file(self.raw.world_map_id, type_hint=Mapw)
        return self._mapw

    @property
    def savw(self) -> Savw:
        if self._savw is None:
            self._savw = self.asset_manager.get_file(self.raw.world_save_info_id, type_hint=Savw)
        return self._savw
