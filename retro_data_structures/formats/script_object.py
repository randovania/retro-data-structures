"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Iterator, Type

from construct import Container
from construct.core import (
    BitStruct, BitsInteger, GreedyBytes, Hex, Int8ub, Int16ub, Int32ub, Prefixed,
    PrefixedArray, Struct, Union,
)

from retro_data_structures import game_check, properties
from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import Game, current_game_at_least_else
from retro_data_structures.properties.base_property import BaseProperty

if TYPE_CHECKING:
    from retro_data_structures.formats.script_layer import ScriptLayerHelper


def Connection(subcon):
    return Struct(
        state=subcon,
        message=subcon,
        target=Hex(Int32ub),
    )


_prefix = current_game_at_least_else(Game.ECHOES, Int16ub, Int32ub)

InstanceId = Union(
    "raw",
    "raw" / Hex(Int32ub),
    "parts" / BitStruct(
        "layer" / BitsInteger(6),
        "area" / BitsInteger(10),
        "instance" / BitsInteger(16)
    )
)

ScriptInstance = Struct(
    type=game_check.current_game_at_least_else(Game.ECHOES, FourCC, Int8ub),
    instance=Prefixed(
        _prefix,
        Struct(
            id=InstanceId,
            connections=PrefixedArray(_prefix, Connection(current_game_at_least_else(Game.ECHOES, FourCC, Int32ub))),
            base_property=GreedyBytes,
        ),
    ),
)


class ScriptInstanceHelper:
    _raw: Container
    target_game: Game

    def __init__(self, raw: Container, target_game: Game):
        self._raw = raw
        self.target_game = target_game

    def __str__(self):
        return "<ScriptInstance {} 0x{:08x}>".format(self.type_name, self.id)

    def __eq__(self, other):
        return isinstance(other, ScriptInstanceHelper) and self._raw == other._raw

    @classmethod
    def new_instance(cls, target_game: Game, instance_type: str, layer: ScriptLayerHelper):
        property_type = properties.get_game_object(target_game, instance_type)

        # TODO: make this less ugly lmao
        raw = ScriptInstance.parse(ScriptInstance.build({
            "type": instance_type,
            "instance": {
                "id": {
                    "parts": {
                        "layer": layer._index,
                        "area": layer._parent_area._index,
                        "instance": layer._parent_area.next_instance_id
                    }
                },
                "connections": [],
                "base_property": property_type().to_bytes(),
            }
        }, target_game=target_game), target_game=target_game)
        return cls(raw, target_game)

    @property
    def type(self) -> str:
        return self._raw.type

    @property
    def type_name(self) -> str:
        return self.type

    @property
    def id(self) -> int:
        return self._raw.instance.id.raw
    
    @property
    def id_struct(self) -> Container:
        return self._raw.instance.id.parts
    
    def id_matches(self, id: int) -> bool:
        parts = InstanceId.parse(InstanceId.build({"raw": id})).parts
        return self.id_struct.area == parts.area and self.id_struct.instance == parts.instance

    @property
    def name(self) -> str:
        try:
            return self.get_property(("editor_properties", "name"))
        except Exception as e:
            return f"Id 0x{self.id:08x}"

    @property
    def _property_type(self) -> Type[BaseProperty]:
        return properties.get_game_object(self.target_game, self.type)

    @property
    def raw_properties(self) -> bytes:
        return self._raw.instance.base_property

    def get_properties(self):
        return self._property_type.from_bytes(self._raw.instance.base_property)

    def set_properties(self, data: BaseProperty):
        if not isinstance(data, self._property_type):
            raise ValueError(f"Got property of type {type(data).__name__}, expected {self.type}")

        self._raw.instance.base_property = data.to_bytes()

    def get_property(self, chain: Iterator[str]):
        prop = self.get_properties()
        for name in chain:
            prop = getattr(prop, name)
        return prop

    @property
    def connections(self):
        return self._raw.instance.connections
    
    @connections.setter
    def connections(self, value):
        self._raw.instance.connections = value

    def add_connection(self, state, message, target: "ScriptInstanceHelper"):
        self.connections.append(Container(
            state=state,
            message=message,
            target=target.id
        ))
    
    def remove_connections(self, target: Union[int, "ScriptInstanceHelper"]):
        if isinstance(target, ScriptInstanceHelper):
            target = target.id
        self.connections = [c for c in self.connections if c.target != target]
