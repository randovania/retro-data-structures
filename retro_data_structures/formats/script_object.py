"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

from typing import Iterator, Type

from construct import Container
from construct.core import (
    BitStruct, BitsInteger, GreedyBytes, Hex, Int8ub, Int16ub, Int32ub, Prefixed,
    PrefixedArray, Struct, Union,
)

from retro_data_structures import game_check, properties
from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import Game, current_game_at_least_else
from retro_data_structures.properties.base_property import BaseProperty


def Connection(subcon):
    return Struct(
        state=subcon,
        message=subcon,
        target=Hex(Int32ub),
    )


_prefix = current_game_at_least_else(Game.ECHOES, Int16ub, Int32ub)

ScriptInstance = Struct(
    type=game_check.current_game_at_least_else(Game.ECHOES, FourCC, Int8ub),
    instance=Prefixed(
        _prefix,
        Struct(
            id=Union(
                "raw",
                "raw" / Hex(Int32ub),
                "parts" / BitStruct(
                    "layer" / BitsInteger(6),
                    "area" / BitsInteger(10),
                    "instance" / BitsInteger(16)
                )
            ),
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
    def new_instance(cls, target_game: Game, instance_type):
        property_type = properties.get_game_object(target_game, instance_type)

        # TODO: make this less ugly lmao
        raw = ScriptInstance.parse(ScriptInstance.build({
            "type": instance_type,
            "instance": {
                "id": {"raw": 0},
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
    def name(self) -> str:
        return self.get_property(("editor_properties", "name"))

    @property
    def _property_type(self) -> Type[BaseProperty]:
        return properties.get_game_object(self.target_game, self.type)

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

    def add_connection(self, state, message, target: "ScriptInstanceHelper"):
        self.connections.append(Container(
            state=state,
            message=message,
            target=target.id
        ))
