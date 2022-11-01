from __future__ import annotations

import typing
from typing import Optional, Union

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
from retro_data_structures.formats.script_object import ScriptInstance, ScriptInstanceHelper, InstanceId
from retro_data_structures.game_check import Game
from retro_data_structures.properties import BaseObjectType

if typing.TYPE_CHECKING:
    from retro_data_structures.formats.mlvl import AreaWrapper

ScriptLayerPrime = Struct(
    "magic" / Const("SCLY", FourCC),
    "unknown" / Int32ub,
    "_layer_count_address" / Tell,
    "_layer_count" / Peek(Int32ub),
    Skip(1, Int32ub),
    "_layer_size_address" / Tell,
    Seek(lambda this: (this._layer_count or len(this.layers)) * Int32ub.sizeof(), 1),
    "layers" / PrefixedArray(
        Pointer(construct.this._._layer_count_address, Int32ub),
        Prefixed(
            Pointer(lambda this: this._._layer_size_address + this._index * Int32ub.sizeof(), Int32ub),
            Struct(
                "unk" / Hex(Int8ub),
                "script_instances" / PrefixedArray(Int32ub, ScriptInstance),
            ),
        ),
    ),
)


def ScriptLayer(identifier):
    return Struct(
        "magic" / Const(identifier, FourCC),
        "unknown" / Int8ub,
        "layer_index" / If(identifier == "SCLY", Int32ub),
        "version" / Const(1, Int8ub),
        "script_instances" / PrefixedArray(Int32ub, ScriptInstance),
    )


def new_layer(index: Optional[int], target_game: Game) -> Container:
    if target_game <= Game.PRIME:
        raise NotImplementedError()
    return Container({
        "magic": "SCLY" if index is not None else "SCGN",
        "unknown": 0,
        "layer_index": index,
        "version": 1,
        "script_instances": []
    })


SCLY = IfThenElse(game_check.current_game_at_least(game_check.Game.ECHOES), ScriptLayer("SCLY"), ScriptLayerPrime)
SCGN = ScriptLayer("SCGN")


class ScriptLayerHelper:
    _parent_area: Optional[AreaWrapper] = None
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

    def with_parent(self, parent: AreaWrapper) -> ScriptLayerHelper:
        self._parent_area = parent
        return self

    @property
    def index(self):
        return self._index

    @property
    def instances(self):
        for instance in self._raw.script_instances:
            yield ScriptInstanceHelper(instance, self.target_game, on_modify=self.mark_modified)

    def get_instance(self, instance_id: int) -> Optional[ScriptInstanceHelper]:
        for instance in self.instances:
            if instance.id_matches(instance_id):
                return instance
        return None

    def get_instance_by_name(self, name: str, *, raise_if_missing: bool = True) -> ScriptInstanceHelper:
        for instance in self.instances:
            if instance.name == name:
                return instance
        if raise_if_missing:
            raise KeyError(name)

    def _internal_add_instance(self, instance: ScriptInstanceHelper):
        if self.get_instance(instance.id) is not None:
            raise RuntimeError(f"Instance with id {instance.id} already exists.")

        self._modified = True
        self._raw.script_instances.append(instance._raw)
        return self.get_instance(instance.id)

    def add_instance(self, instance_type: str, name: Optional[str] = None) -> ScriptInstanceHelper:
        instance = ScriptInstanceHelper.new_instance(self.target_game, instance_type, self)
        if name is not None:
            instance.name = name
        return self._internal_add_instance(instance)

    def add_instance_with(self, object_properties: BaseObjectType) -> ScriptInstanceHelper:
        instance = ScriptInstanceHelper.new_from_properties(object_properties, self)
        return self._internal_add_instance(instance)

    def add_existing_instance(self, instance: ScriptInstanceHelper) -> ScriptInstanceHelper:
        if instance.id.area != self._parent_area.id:
            new_id = InstanceId.new(self._index, self._parent_area.id, self._parent_area.next_instance_id)
        else:
            new_id = InstanceId.new(self._index, instance.id.area, instance.id.instance)

        instance.id = new_id
        return self._internal_add_instance(instance)

    def remove_instance(self, instance: Union[int, str, ScriptInstanceHelper]):
        if isinstance(instance, str):
            instance = self.get_instance_by_name(instance)
        if isinstance(instance, ScriptInstanceHelper):
            instance = instance.id

        matching_instances = [
            i for i in self._raw.script_instances
            if i.id == instance
        ]

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
