"""
https://wiki.axiodl.com/w/Scriptable_Layers_(File_Format)
"""

import io
from pathlib import Path
from construct.core import (Adapter, Computed, Construct, FocusedSeq, Hex, IfThenElse, Int16ub, Int32ub, PaddedString, Peek, Pointer,
                       PrefixedArray, Rebuild, Seek, Struct, Switch, Tell, this)
import construct
from construct.core import GreedyBytes, Int8ub, Prefixed
from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import Game, current_game_at_least_else, get_current_game
from retro_data_structures.properties import PropertyAdapter, StructProperty, Property
from retro_data_structures.property_template import GetGameTemplate, GetPropertyConstruct, PropertyConstructs
from retro_data_structures.construct_extensions import WithVersionElse

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
        data = subcon.parse(obj, **context)
        print(data)
        return data
    
    def _encode(self, obj, context, path):
        subcon = self._get_property_construct(context)
        data = subcon.build(obj, **context)
        print(data)
        return data

ScriptInstance = Struct(
    "type" / game_check.current_game_at_least_else(Game.ECHOES, FourCC, Int8ub),
    "instance" / Prefixed(
        current_game_at_least_else(Game.ECHOES, Int16ub, Int32ub),
        Struct(
            "id" / Int32ub, # TODO: Union
            "connections" / PrefixedArray(Int16ub, Connection(current_game_at_least_else(Game.ECHOES, FourCC, Int32ub))),
            "base_property" / ScriptInstanceAdapter(lambda this: f'0x{this._.type:X}' if isinstance(this._.type, int) else this._.type)
        )
    )
)
