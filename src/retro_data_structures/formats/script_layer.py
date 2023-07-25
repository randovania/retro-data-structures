from __future__ import annotations

import logging
import typing

import construct
from construct.core import (
    Const,
    Hex,
    If,
    IfThenElse,
    Int8ub,
    Int32ub,
    Peek,
    Pointer,
    Prefixed,
    PrefixedArray,
    Seek,
    Struct,
    Tell,
)
from construct.lib.containers import Container

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC
from retro_data_structures.construct_extensions.misc import Skip
from retro_data_structures.formats.script_object import (
    ConstructScriptInstance,
    InstanceId,
    InstanceIdRef,
    InstanceRef,
    ScriptInstance,
    resolve_instance_id,
)
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.formats.mlvl import Area
    from retro_data_structures.properties import BaseObjectType

ScriptLayerPrime = Struct(
    "magic" / Const("SCLY", FourCC),
    "unknown" / Int32ub,
    "_layer_count_address" / Tell,
    "_layer_count" / Peek(Int32ub),
    Skip(1, Int32ub),
    "_layer_size_address" / Tell,
    Seek(lambda this: (this._layer_count or len(this.layers)) * Int32ub.sizeof(), 1),
    "layers"
    / PrefixedArray(
        Pointer(construct.this._._layer_count_address, Int32ub),
        Prefixed(
            Pointer(lambda this: this._._layer_size_address + this._index * Int32ub.sizeof(), Int32ub),
            Struct(
                "unk" / Hex(Int8ub),
                "script_instances" / PrefixedArray(Int32ub, ConstructScriptInstance),
            ),
        ),
    ),
)


def ConstructScriptLayer(identifier):
    return Struct(
        "magic" / Const(identifier, FourCC),
        "unknown" / Int8ub,
        "layer_index" / If(identifier == "SCLY", Int32ub),
        "version" / Const(1, Int8ub),
        "script_instances" / PrefixedArray(Int32ub, ConstructScriptInstance),
    )


def new_layer(index: int | None, target_game: Game) -> Container:
    if target_game <= Game.PRIME:
        raise NotImplementedError
    return Container(
        {
            "magic": "SCLY" if index is not None else "SCGN",
            "unknown": 0,
            "layer_index": index,
            "version": 1,
            "script_instances": [],
        }
    )


SCLY = IfThenElse(
    game_check.current_game_at_least(game_check.Game.ECHOES), ConstructScriptLayer("SCLY"), ScriptLayerPrime
)
SCGN = ConstructScriptLayer("SCGN")


def dependencies_for_layer(
    asset_manager: AssetManager, instances: typing.Iterable[ScriptInstance]
) -> typing.Iterator[Dependency]:
    deps: list[Dependency] = []
    for instance in instances:
        deps.extend(instance.mlvl_dependencies_for(asset_manager))

    unique_deps: set[Dependency] = set()
    for dep in deps:
        if dep in unique_deps:
            continue
        # specifically keep the order of the *first* appearance of the dependency
        unique_deps.add(dep)
        yield dep


class ScriptLayer:
    _parent_area: Area | None = None
    _index: int
    _modified: bool = False

    def __init__(self, raw: Container, index: int, target_game: Game) -> None:
        self._raw = raw
        self.target_game = target_game
        self._index = index

    def __repr__(self) -> str:
        if self.has_parent:
            return f"{self.name} ({'Active' if self.active else 'Inactive'})"
        return super().__repr__()

    def with_parent(self, parent: Area) -> ScriptLayer:
        self._parent_area = parent
        return self

    @property
    def index(self):
        return self._index

    @property
    def instances(self):
        for instance in self._raw.script_instances:
            yield ScriptInstance(instance, self.target_game, on_modify=self.mark_modified)

    def has_instance(self, ref: InstanceRef) -> bool:
        try:
            self.get_instance(ref)
        except KeyError:
            return False
        return True

    def get_instance(self, ref: InstanceRef) -> ScriptInstance:
        if isinstance(ref, str):
            return self._get_instance_by_name(ref)
        return self._get_instance_by_id(ref)

    def _get_instance_by_id(self, instance_id: InstanceIdRef) -> ScriptInstance:
        instance_id = resolve_instance_id(instance_id)
        for instance in self.instances:
            if instance.id_matches(instance_id):
                return instance
        raise KeyError(instance_id)

    def _get_instance_by_name(self, name: str) -> ScriptInstance:
        for instance in self.instances:
            if instance.name == name:
                return instance
        raise KeyError(name)

    def _internal_add_instance(self, instance: ScriptInstance):
        if self.has_instance(instance):
            raise RuntimeError(f"Instance with id {instance.id} already exists.")

        self._modified = True
        self._raw.script_instances.append(instance._raw)
        return self._get_instance_by_id(instance.id)

    def add_instance(self, instance_type: str, name: str | None = None) -> ScriptInstance:
        instance = ScriptInstance.new_instance(self.target_game, instance_type, self)
        if name is not None:
            instance.name = name
        return self._internal_add_instance(instance)

    def add_instance_with(self, object_properties: BaseObjectType) -> ScriptInstance:
        instance = ScriptInstance.new_from_properties(object_properties, self)
        return self._internal_add_instance(instance)

    def add_memory_relay(self, name: str | None = None) -> ScriptInstance:
        relay = self.add_instance("MRLY", name)
        savw = self._parent_area._parent_mlvl.savw
        savw.raw.memory_relays.append({"instance_id": relay.id})
        return relay

    def remove_instance(self, instance: InstanceRef):
        if isinstance(instance, str):
            instance = self._get_instance_by_name(instance)
        instance = resolve_instance_id(instance)

        matching_instances = [i for i in self._raw.script_instances if i.id == instance]

        if not matching_instances:
            raise KeyError(instance)

        self._modified = True
        for i in matching_instances:
            self._raw.script_instances.remove(i)

    def remove_instances(self):
        self._modified = True
        self._raw.script_instances = []

    def assert_parent(self):
        if self.has_parent:
            return
        if self._parent_area is None:
            raise AttributeError(f"{self} has no parent!")
        if self._index is None:
            raise AttributeError(f"{self} has no index!")

    @property
    def has_parent(self) -> bool:
        return self._parent_area is not None and self._index is not None

    @property
    def active(self) -> bool:
        self.assert_parent()
        return self._parent_area._flags[self._index]

    @active.setter
    def active(self, value: bool):
        self.assert_parent()
        self._modified = True
        self._parent_area._flags[self._index] = value

    @property
    def name(self) -> str:
        self.assert_parent()
        return self._parent_area._layer_names[self._index]

    @name.setter
    def name(self, value: str):
        self.assert_parent()
        self._modified = True
        self._parent_area._layer_names[self._index] = value

    def new_instance_id(self) -> InstanceId:
        return InstanceId.new(self._index, self._parent_area.index, self._parent_area.next_instance_id)

    def is_modified(self) -> bool:
        return self._modified

    def mark_modified(self):
        self._modified = True

    def build_mlvl_dependencies(self, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
        logging.debug("        Layer: %s", self.name)
        yield from dependencies_for_layer(asset_manager, self.instances)

    @property
    def dependencies(self) -> typing.Iterator[Dependency]:
        self.assert_parent()
        yield from self._parent_area.dependencies.layers[self._index]

    def build_module_dependencies(self) -> typing.Iterator[str]:
        rels = list(self.module_dependencies)
        for instance in self.instances:
            rels.extend(instance.get_properties().modules())

        yield from list(dict.fromkeys(rels))

    @property
    def module_dependencies(self) -> typing.Iterator[str]:
        self.assert_parent()
        yield from self._parent_area.module_dependencies[self._index]
