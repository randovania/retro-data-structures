"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

from __future__ import annotations

import dataclasses
import enum
import io
import logging
import typing
from typing import TYPE_CHECKING, Iterator, Type

import construct
from construct.core import (
    Hex,
    Int8ub,
    Int16ub,
    Int32ub,
    PrefixedArray,
    Struct,
    Union,
)

from retro_data_structures import game_check, properties
from retro_data_structures.base_resource import Dependency
from retro_data_structures.common_types import FourCC
from retro_data_structures.enums import helper as enum_helper
from retro_data_structures.enums.shared_enums import Message, State
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.formats.script_layer import ScriptLayerHelper
    from retro_data_structures.properties.base_property import BaseObjectType

    PropertyType = typing.TypeVar("PropertyType", bound=BaseObjectType)


def ConstructConnection(subcon):
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
    def new(cls, layer: int, area: int, instance: int) -> InstanceId:
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


@dataclasses.dataclass()
class Connection:
    state: State
    message: Message
    target: InstanceId

    @classmethod
    def from_construct(cls, game: Game, obj: dict) -> Connection:
        return cls(
            state=enum_helper.STATE_PER_GAME[game](obj["state"]),
            message=enum_helper.MESSAGE_PER_GAME[game](obj["message"]),
            target=InstanceId(obj["target"]),
        )

    def as_construct(self) -> construct.Container:
        return construct.Container(
            state=self.state.value,
            message=self.message.value,
            target=self.target,
        )


@dataclasses.dataclass()
class ScriptInstanceRaw:
    type: int | str
    id: InstanceId
    connections: tuple[Connection, ...]
    base_property: bytes


class _ConstructScriptInstance(construct.Construct):
    def _parse(self, stream, context, path) -> ScriptInstanceRaw:
        game = game_check.get_current_game(context)

        if game >= Game.ECHOES:
            obj_type_con = FourCC
            obj_len_con = Int16ub
        else:
            obj_type_con = Int8ub
            obj_len_con = Int32ub

        obj_type: str | int = obj_type_con._parsereport(stream, context, f"{path} -> type")
        obj_len: int = obj_len_con._parsereport(stream, context, f"{path} -> object_length")
        sub_stream = io.BytesIO(construct.stream_read(stream, obj_len, f"{path} -> object_raw_data"))

        obj_id: int = Int32ub._parsereport(sub_stream, context, f"{path} -> instance_id")

        connections = PrefixedArray(obj_len_con, ConstructConnection(obj_type_con))._parsereport(
            sub_stream, context, f"{path} -> connections")

        base_property = construct.stream_read_entire(sub_stream, f"{path} -> base_property")

        return ScriptInstanceRaw(
            type=obj_type,
            id=InstanceId(obj_id),
            connections=tuple(
                Connection.from_construct(game, con)
                for con in connections
            ),
            base_property=base_property,
        )

    def _build(self, obj: ScriptInstanceRaw, stream, context, path):
        game = game_check.get_current_game(context)

        if game >= Game.ECHOES:
            obj_type_con = FourCC
            obj_len_con = Int16ub
        else:
            obj_type_con = Int8ub
            obj_len_con = Int32ub

        sub_stream = io.BytesIO()
        Int32ub._build(obj.id, sub_stream, context, f"{path} -> instance_id")
        PrefixedArray(obj_len_con, ConstructConnection(obj_type_con))._build(
            [conn.as_construct() for conn in obj.connections],
            sub_stream,
            context, f"{path} -> connections"
        )
        construct.stream_write(sub_stream, obj.base_property, len(obj.base_property), f"{path} -> base_property")

        obj_data = sub_stream.getvalue()

        obj_type_con._build(obj.type, stream, context, f"{path} -> type")
        obj_len_con._build(len(obj_data), stream, context, f"{path} -> object_length")
        construct.stream_write(stream, obj_data, len(obj_data), f"{path} -> object_raw_data")


ConstructScriptInstance = _ConstructScriptInstance()

E = typing.TypeVar("E", bound=enum.Enum)


def _resolve_to_enum(correct_type: type[E], value: str | enum.Enum) -> E:
    # It's already the enum we want, just use it
    if isinstance(value, correct_type):
        return value

    # If passing a string, assume it's a raw FourCC value
    if isinstance(value, str):
        return correct_type(value)

    # Otherwise, assume it's a proper enum but for the wrong game, so switch around
    return correct_type[value.name]


class ScriptInstanceHelper:
    _raw: ScriptInstanceRaw
    target_game: Game

    def __init__(self, raw: ScriptInstanceRaw, target_game: Game, on_modify: typing.Callable[[], None] = lambda: None):
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

        raw = ScriptInstanceRaw(
            type=instance_type,
            id=layer.new_instance_id(),
            connections=(),
            base_property=property_type().to_bytes(),
        )
        return cls(raw, target_game, on_modify=layer.mark_modified)

    @classmethod
    def new_from_properties(cls, object_properties: BaseObjectType, layer: ScriptLayerHelper) -> ScriptInstanceHelper:
        raw = ScriptInstanceRaw(
            type=object_properties.object_type(),
            id=layer.new_instance_id(),
            connections=(),
            base_property=object_properties.to_bytes(),
        )
        return cls(raw, object_properties.game(), on_modify=layer.mark_modified)

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
    def name(self) -> str | None:
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
        # hack to support using the shared_objects unions
        if hasattr(type_cls, "__args__"):
            type_cls = type_cls.__args__
        if not isinstance(props, type_cls):
            raise TypeError(f"Expected {type_cls}, got {props}")
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
    def connections(self) -> tuple[Connection, ...]:
        return tuple(self._raw.connections)

    @connections.setter
    def connections(self, value: typing.Iterable[Connection]):
        self._raw.connections = tuple(value)
        self.on_modify()

    def add_connection(self, state: str | State, message: str | Message, target: ScriptInstanceHelper):
        correct_state = enum_helper.STATE_PER_GAME[self.target_game]
        correct_message = enum_helper.MESSAGE_PER_GAME[self.target_game]

        self.connections = self.connections + (Connection(
            state=_resolve_to_enum(correct_state, state),
            message=_resolve_to_enum(correct_message, message),
            target=target.id
        ),)

    def remove_connection(self, connection: Connection):
        self.connections = [c for c in self.connections if c is not connection]

    def remove_connections(self, target: Union[int, ScriptInstanceHelper]):
        if isinstance(target, ScriptInstanceHelper):
            target = target.id

        self.connections = [c for c in self.connections if c.target != target]

    def mlvl_dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        logging.debug(f"            {self.name}")
        yield from self.get_properties().dependencies_for(asset_manager, is_mlvl=True)
