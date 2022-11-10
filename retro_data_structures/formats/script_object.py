"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

from __future__ import annotations

import typing
from typing import TYPE_CHECKING, Iterator, Type

import construct
from construct import Container
from construct.core import (
    GreedyBytes, Hex, Int8ub, Int16ub, Int32ub, Prefixed,
    PrefixedArray, Struct, Union,
)
from retro_data_structures import game_check, properties
from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import Game, current_game_at_least_else
from retro_data_structures.properties.base_property import BaseProperty, BaseObjectType

if TYPE_CHECKING:
    from retro_data_structures.formats.script_layer import ScriptLayerHelper


PropertyType = typing.TypeVar("PropertyType", bound=BaseObjectType)


def Connection(subcon):
    return Struct(
        state=subcon,
        message=subcon,
        target=Hex(Int32ub),
    )


class InstanceId(int):
    # 32 bits:
    # top 6 for layer
    # middle 10 for area
    # last 16 for instance

    @classmethod
    def new(cls, layer: int, area: int, instance: int) -> "InstanceId":
        assert 0 <= layer < 64
        assert 0 <= area < 1024
        assert 0 <= instance < 65536
        return InstanceId((layer << 26) + (area << 16) + instance)

    def __str__(self):
        return f"0x{self:08x}"

    @property
    def layer(self) -> int:
        return self >> 26

    @property
    def area(self) -> int:
        return (self >> 16) & 0x3ff

    @property
    def instance(self) -> int:
        return self & 0xffff


InstanceIdInternal = construct.ExprAdapter(
    Hex(Int32ub),
    decoder=lambda obj, ctx: InstanceId(obj),
    encoder=lambda obj, ctx: int(obj),
)

_prefix = current_game_at_least_else(Game.ECHOES, Int16ub, Int32ub)

ScriptInstanceInternal = Struct(
    type=game_check.current_game_at_least_else(Game.ECHOES, FourCC, Int8ub),
    instance=Prefixed(
        _prefix,
        Struct(
            id=InstanceIdInternal,
            connections=PrefixedArray(_prefix, Connection(current_game_at_least_else(Game.ECHOES, FourCC, Int32ub))),
            base_property=GreedyBytes,
        ),
    ),
).compile()

ScriptInstance = construct.ExprAdapter(
    ScriptInstanceInternal,
    decoder=lambda obj, ctx: Container(
        type=obj.type,
        id=obj.instance.id,
        connections=obj.instance.connections,
        base_property=obj.instance.base_property,
    ),
    encoder=lambda obj, ctx: Container(
        type=obj.type,
        instance=Container(
            id=obj.id,
            connections=obj.connections,
            base_property=obj.base_property,
        )
    )
)


class ScriptInstanceHelper:
    _raw: Container
    target_game: Game

    def __init__(self, raw: Container, target_game: Game, on_modify: typing.Callable[[], None] = lambda: None):
        self._raw = raw
        self.target_game = target_game
        self.on_modify = on_modify

    def __str__(self):
        return "<ScriptInstance {} 0x{:08x}>".format(self.type_name, self.id)

    def __eq__(self, other):
        return isinstance(other, ScriptInstanceHelper) and self._raw == other._raw

    @classmethod
    def new_instance(cls, target_game: Game, instance_type: str, layer: ScriptLayerHelper) -> ScriptInstanceHelper:
        property_type = properties.get_game_object(target_game, instance_type)

        raw = Container(
            type=instance_type,
            id=layer.new_instance_id(),
            connections=construct.ListContainer(),
            base_property=property_type().to_bytes(),
        )
        return cls(raw, target_game)

    @classmethod
    def new_from_properties(cls, object_properties: BaseObjectType, layer: ScriptLayerHelper) -> ScriptInstanceHelper:
        raw = Container(
            type=object_properties.object_type(),
            id=layer.new_instance_id(),
            connections=construct.ListContainer(),
            base_property=object_properties.to_bytes(),
        )
        return cls(raw, object_properties.game())

    @property
    def type(self) -> Type[BaseObjectType]:
        return properties.get_game_object(self.target_game, self.type_name)

    @property
    def type_name(self) -> typing.Union[int, str]:
        return self._raw.type

    @property
    def id(self) -> InstanceId:
        return self._raw.id

    @id.setter
    def id(self, value):
        self._raw.id = InstanceId(value)
        self.on_modify()

    def id_matches(self, id: typing.Union[int, InstanceId]) -> bool:
        if not isinstance(id, InstanceId):
            id = InstanceId(id)

        return self.id.area == id.area and self.id.instance == id.instance

    @property
    def name(self) -> typing.Union[str]:
        return self.get_properties().get_name()

    @name.setter
    def name(self, value: str):
        props = self.get_properties()
        props.set_name(value)
        self.set_properties(props)

    @property
    def raw_properties(self) -> bytes:
        return self._raw.base_property

    def get_properties(self) -> BaseObjectType:
        return self.type.from_bytes(self._raw.base_property)

    def get_properties_as(self, type_cls: Type[PropertyType]) -> PropertyType:
        props = self.get_properties()
        assert isinstance(props, type_cls)
        return props

    def set_properties(self, data: BaseObjectType):
        if not isinstance(data, self.type):
            raise ValueError(f"Got property of type {type(data).__name__}, expected {self.type_name}")

        self._raw.base_property = data.to_bytes()
        self.on_modify()

    def get_property(self, chain: Iterator[str]):
        prop = self.get_properties()
        for name in chain:
            prop = getattr(prop, name)
        return prop

    @property
    def connections(self):
        return self._raw.connections

    @connections.setter
    def connections(self, value):
        self._raw.connections = value

    def add_connection(self, state, message, target: ScriptInstanceHelper):
        self.connections.append(Container(
            state=state,
            message=message,
            target=target.id
        ))
        self.on_modify()

    def remove_connections(self, target: Union[int, ScriptInstanceHelper]):
        if isinstance(target, ScriptInstanceHelper):
            target = target.id

        self.connections = [c for c in self.connections if c.target != target]
        self.on_modify()
