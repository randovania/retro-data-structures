"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

import io
from typing import Iterator

import construct
from construct import Container
from construct.core import (
    Adapter, BitStruct, BitsInteger, GreedyBytes, Hex, Int8ub, Int16ub, Int32ub, Prefixed,
    PrefixedArray, Struct, Union,
)

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import Game, current_game_at_least_else
from retro_data_structures.property_template import GetPropertyConstruct


def Connection(subcon):
    return Struct(
        state=subcon,
        message=subcon,
        target=Hex(Int32ub),
    )


class ScriptInstanceAdapter(Adapter):
    def __init__(self, obj_id_func):
        super().__init__(GreedyBytes)
        self.obj_id_func = obj_id_func

    def _get_property_construct(self, context):
        game = construct.evaluate(game_check.get_current_game, context)
        obj_id = construct.evaluate(self.obj_id_func, context)
        return GetPropertyConstruct(game, obj_id)

    def _decode(self, obj, context, path):
        subcon = self._get_property_construct(context)
        return subcon._parsereport(io.BytesIO(obj), context, path)

    def _encode(self, obj, context, path):
        subcon = self._get_property_construct(context)
        encoded = io.BytesIO()
        subcon._build(obj, encoded, context, path)
        return encoded.getvalue()


def ThisTypeAsString(this):
    return f"0x{this._.type:X}" if isinstance(this._.type, int) else this._.type


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
            # base_property=ScriptInstanceAdapter(ThisTypeAsString),
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
        prop_construct = GetPropertyConstruct(target_game, instance_type, True)
        # TODO: make this less ugly lmao
        raw = ScriptInstance.parse(ScriptInstance.build({
            "type": instance_type,
            "instance": {
                "id": {"raw": 0},
                "connections": [],
                "base_property": prop_construct.build({}, target_game=target_game)
            }
        }, target_game=target_game), target_game=target_game)
        return cls(raw, target_game)

    @property
    def type(self) -> str:
        return self._raw.type

    @property
    def type_name(self) -> str:
        try:
            return self.get_properties()["_name"]
        except Exception:
            return self.type

    @property
    def id(self) -> int:
        return self._raw.instance.id.raw

    @property
    def name(self) -> str:
        return self.get_property(("EditorProperties", "Name"))

    @property
    def _property_construct(self):
        return GetPropertyConstruct(self.target_game, self.type)

    def get_properties(self):
        return self._property_construct.parse(
            self._raw.instance.base_property,
            target_game=self.target_game,
        )

    def set_properties(self, data: Container):
        self._raw.instance.base_property = self._property_construct.build(
            data, target_game=self.target_game,
        )

    def get_property(self, chain: Iterator[str]):
        prop = self.get_properties()
        for name in chain:
            prop = prop[name]
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
