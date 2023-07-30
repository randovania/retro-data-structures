"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

from __future__ import annotations

import contextlib
import dataclasses
import enum
import io
import logging
import struct
import typing
from typing import TYPE_CHECKING

import construct
from construct.core import (
    Hex,
    Int8ub,
    Int16ub,
    Int32ub,
    PrefixedArray,
    Struct,
)

from retro_data_structures import game_check, properties
from retro_data_structures.common_types import FourCC
from retro_data_structures.enums import helper as enum_helper
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.enums.shared_enums import Message, State
    from retro_data_structures.formats.script_layer import ScriptLayer
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

    def __repr__(self):
        return f"0x{self:08x}"

    @property
    def layer(self) -> int:
        return self >> 26

    @property
    def area(self) -> int:
        return (self >> 16) & 0x3FF

    @property
    def instance(self) -> int:
        return self & 0xFFFF


@dataclasses.dataclass(frozen=True)
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


def _raw_script_instance_construct(obj_type_con, obj_len_con):
    header = construct.Struct(
        type=obj_type_con,
        raw_data=construct.Prefixed(obj_len_con, construct.GreedyBytes),
    ).compile()
    body = construct.Struct(
        instance_id=Int32ub,
        connections=PrefixedArray(obj_len_con, ConstructConnection(obj_type_con)),
        base_property=construct.GreedyBytes,
    ).compile()

    return header, body


_PrimeRawScript = _raw_script_instance_construct(Int8ub, Int32ub)
_EchoesRawScript = _raw_script_instance_construct(FourCC, Int16ub)


class _ConstructScriptInstance(construct.Construct):
    def _parse(self, stream, context, path) -> ScriptInstanceRaw:
        game = game_check.get_current_game(context)

        if game >= Game.ECHOES:
            header_construct, body_construct = _EchoesRawScript
        else:
            header_construct, body_construct = _PrimeRawScript

        header = header_construct._parse(stream, context, path)
        body = body_construct._parse(io.BytesIO(header.raw_data), context, path)

        obj_type: str | int = header.type
        obj_id: int = body.instance_id
        base_property = body.base_property

        inst_id = InstanceId(obj_id)

        cons = []
        for con in body.connections:
            try:
                cons.append(Connection.from_construct(game, con))
            except ValueError:
                con.target = InstanceId(con.target)  # for prettier printing
                logging.warning(f"Removing corrupted connection from instance {inst_id} ({obj_type}): {con=}")

        return ScriptInstanceRaw(
            type=obj_type,
            id=inst_id,
            connections=tuple(cons),
            base_property=base_property,
        )

    def _build(self, obj: ScriptInstanceRaw, stream, context, path):
        game = game_check.get_current_game(context)

        if game >= Game.ECHOES:
            header_construct, body_construct = _EchoesRawScript
        else:
            header_construct, body_construct = _PrimeRawScript

        sub_stream = io.BytesIO()
        body_construct._build(
            construct.Container(
                instance_id=obj.id,
                connections=[conn.as_construct() for conn in obj.connections],
                base_property=obj.base_property,
            ),
            sub_stream,
            context,
            path,
        )

        header_construct._build(
            construct.Container(
                type=obj.type,
                raw_data=sub_stream.getvalue(),
            ),
            stream,
            context,
            path,
        )


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


def _try_quick_get_name(data: bytes) -> str | None:
    try:
        # Is first property EditorProperties?
        if data[8:12] != b"%ZE\x80":
            return None
        # 12:14  (first prop size)
        # 14:16  (EditorProperties, prop count)
        if data[16:20] != b"INAM":
            return None

        string_size = struct.unpack_from(">H", data, 20)[0]
        return data[22 : 22 + string_size - 1].decode("ascii")

    except IndexError:
        return None


class ScriptInstance:
    _raw: ScriptInstanceRaw
    target_game: Game

    def __init__(self, raw: ScriptInstanceRaw, target_game: Game, on_modify: typing.Callable[[], None] = lambda: None):
        self._raw = raw
        self.target_game = target_game
        self.on_modify = on_modify

    def __repr__(self):
        return f"<ScriptInstance {self.type_name} 0x{self.id:08x}>"

    def __eq__(self, other):
        return isinstance(other, ScriptInstance) and self._raw == other._raw

    @classmethod
    def new_instance(cls, target_game: Game, instance_type: str, layer: ScriptLayer) -> ScriptInstance:
        property_type = properties.get_game_object(target_game, instance_type)

        raw = ScriptInstanceRaw(
            type=instance_type,
            id=layer.new_instance_id(),
            connections=(),
            base_property=property_type().to_bytes(),
        )
        return cls(raw, target_game, on_modify=layer.mark_modified)

    @classmethod
    def new_from_properties(cls, object_properties: BaseObjectType, layer: ScriptLayer) -> ScriptInstance:
        raw = ScriptInstanceRaw(
            type=object_properties.object_type(),
            id=layer.new_instance_id(),
            connections=(),
            base_property=object_properties.to_bytes(),
        )
        return cls(raw, object_properties.game(), on_modify=layer.mark_modified)

    @property
    def type(self) -> type[BaseObjectType]:
        return properties.get_game_object(self.target_game, self.type_name)

    @property
    def type_name(self) -> int | str:
        return self._raw.type

    @property
    def id(self) -> InstanceId:
        return self._raw.id

    @id.setter
    def id(self, value):
        self._raw.id = InstanceId(value)
        self.on_modify()

    def id_matches(self, other: InstanceIdRef) -> bool:
        other = resolve_instance_id(other)
        return self.id.area == other.area and self.id.instance == other.instance

    @property
    def name(self) -> str | None:
        if self.target_game == Game.ECHOES:
            name = _try_quick_get_name(self._raw.base_property)
            if name is not None:
                return name
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

    def get_properties_as(self, type_cls: type[PropertyType]) -> PropertyType:
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

    @contextlib.contextmanager
    def edit_properties(self, type_cls: type[PropertyType]):
        props = self.get_properties_as(type_cls)
        yield props
        self.set_properties(props)

    @property
    def connections(self) -> tuple[Connection, ...]:
        return tuple(self._raw.connections)

    @connections.setter
    def connections(self, value: typing.Iterable[Connection]):
        self._raw.connections = tuple(value)
        self.on_modify()

    def add_connection(self, state: str | State, message: str | Message, target: InstanceIdRef):
        correct_state = enum_helper.STATE_PER_GAME[self.target_game]
        correct_message = enum_helper.MESSAGE_PER_GAME[self.target_game]

        target = resolve_instance_id(target)

        self.connections = self.connections + (
            Connection(
                state=_resolve_to_enum(correct_state, state),
                message=_resolve_to_enum(correct_message, message),
                target=target,
            ),
        )

    def remove_connection(self, connection: Connection):
        self.connections = [c for c in self.connections if c != connection]

    def remove_connections_from(self, target: InstanceIdRef):
        target = resolve_instance_id(target)
        self.connections = [c for c in self.connections if c.target != target]

    def mlvl_dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from self.get_properties().dependencies_for(asset_manager)


InstanceIdRef = InstanceId | int | ScriptInstance
InstanceRef = InstanceIdRef | str


def resolve_instance_id(inst: InstanceIdRef) -> InstanceId:
    if isinstance(inst, InstanceId):
        return inst
    if isinstance(inst, ScriptInstance):
        return inst.id
    if isinstance(inst, int):
        return InstanceId(inst)
    raise TypeError(f"Invalid type: Expected InstanceIdRef, got {type(inst)}")
