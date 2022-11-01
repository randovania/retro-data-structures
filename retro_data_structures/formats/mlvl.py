"""
Wiki: https://wiki.axiodl.com/w/MLVL_(File_Format)
"""
from __future__ import annotations

from itertools import count
from typing import Iterator
import typing
import construct
from construct import (
    Adapter,
    Array,
    Bitwise,
    Container,
    Error,
    ListContainer,
    Struct,
    Int32ub,
    PrefixedArray,
    Int64ub,
    Float32b,
    Int16ub,
    CString,
    Const,
    Int8ub,
    Switch,
    Peek,
    Sequence,
    FocusedSeq,
    Flag,
    len_
)
from retro_data_structures.adapters.offset import OffsetAdapter


from retro_data_structures.common_types import Vector3, AssetId32, AssetId64, FourCC
from retro_data_structures.construct_extensions.misc import PrefixedArrayWithExtra
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency, NameOrAssetId
from retro_data_structures.exceptions import UnknownAssetId
from retro_data_structures.formats import Mapw
from retro_data_structures.formats.guid import GUID
from retro_data_structures.formats.mrea import Mrea
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
        # Always empty
        dependencies_a=PrefixedArray(Int32ub, MLVLAreaDependency),
        dependencies_b=PrefixedArray(Int32ub, MLVLAreaDependency),
        dependencies_offset=PrefixedArray(Int32ub, Int32ub),
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


class AreaWrapper:
    _flags: Container
    _layer_names: ListContainer
    _index: int

    _mrea: Mrea = None
    _strg: Strg = None

    def __init__(self, raw: Container, asset_manager: AssetManager, flags: Container, names: Container, index: int):
        self._raw = raw
        self.asset_manager = asset_manager
        self._flags = flags
        self._layer_names = names
        self._index = index
    
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
        except UnknownAssetId as e:
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


class Mlvl(BaseResource):
    _mapw: Mapw = None

    @classmethod
    def resource_type(cls) -> AssetType:
        return "MLVL"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return MLVL

    def dependencies_for(self) -> typing.Iterator[Dependency]:
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
            yield AreaWrapper(area, self.asset_manager, self._raw.area_layer_flags[i], area_layer_names, i)
    
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
