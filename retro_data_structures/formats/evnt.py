import typing

import construct
from construct import (
    Int16ub, Byte, Float32b, Int32sb, Hex,
    Int64ub, Array, Int8ub, IfThenElse, Switch,
    Struct, PrefixedArray, Int32ub, If,
)

from retro_data_structures import game_check
from retro_data_structures.common_types import String, CharAnimTime, MayaSpline
from retro_data_structures.construct_extensions.version import WithVersion
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.game_check import Game

BasePOINode = Struct(
    unk_1=Int16ub,
    name=String,
    type=Int16ub,
    timestamp=CharAnimTime,
    index=Int32ub,
    unk_2=If(game_check.is_prime3, Int32ub),
    unique=Byte,
    weight=Float32b,
    character_index=Int32sb,
    flags=Int32ub,
    unk_extra=If(
        game_check.is_prime3,
        Struct(
            Int32ub,
            Int32ub,
            Int32ub,
            Float32b,
            Float32b,
        ),
    ),
)

BoolPOINode = Struct(
    base=BasePOINode,
    value=Byte,
)

Int32POINode = Struct(
    base=BasePOINode,
    value=If(game_check.current_game_at_most(Game.ECHOES), Int32sb),
    locator_name=If(game_check.current_game_at_most(Game.ECHOES), String),
    corruption=If(game_check.is_prime3,
                  Struct(
                      unk_a=Int8ub,
                      unk_b=Int16ub,
                      unk_c=Int16ub,
                  ),
                  ),
)

ParticlePOINode = Struct(
    base=BasePOINode,
    duration=If(game_check.current_game_at_most(Game.ECHOES), Int32ub),
    particle=game_check.ObjectTagCorrect,
    bone_name=If(game_check.is_prime1, String),
    bone_id=If(game_check.is_prime2, Int32ub),
    effect_scale=If(game_check.current_game_at_most(Game.ECHOES), Float32b),
    transform_type=If(game_check.current_game_at_most(Game.ECHOES), Int32ub),
    unk_float=If(game_check.is_prime3, Float32b),
    unk_id=If(game_check.is_prime3, Int32ub),
)

SoundPOINode = Struct(
    base=BasePOINode,
    sound_id=IfThenElse(
        game_check.current_game_at_most(Game.ECHOES),
        Hex(Int32ub),
        Hex(Int64ub),
    ),
    fall_off=If(game_check.current_game_at_most(Game.ECHOES), Float32b),
    max_distance=If(game_check.current_game_at_most(Game.ECHOES), Float32b),
    echoes=If(
        game_check.is_prime2,
        Struct(
            unk_a=Int32ub,
            unk_b=Int16ub,
            unk_c=Int16ub,
            unk_d=Float32b,
        ),
    ),
    corruption=If(
        game_check.is_prime3,
        Struct(
            unk_a=Int32ub,
            unk_b=Int32ub,
            data=Array(2,
                       Struct(
                           type=Int32ub,
                           data=Switch(construct.this.type,
                                       {
                                           1: Int32ub,
                                           2: MayaSpline,
                                       }
                                       ),
                       ),
                       ),
        ),
    ),
)

EVNT = Struct(
    version=Int32ub,
    bool_poi_nodes=PrefixedArray(Int32ub, BoolPOINode),
    int32_poi_nodes=PrefixedArray(Int32ub, Int32POINode),
    particle_poi_nodes=PrefixedArray(Int32ub, ParticlePOINode),
    sound_poi_nodes=WithVersion(2, PrefixedArray(Int32ub, SoundPOINode)),
)


def dependencies_for(obj, target_game):
    for particle_poi in obj.particle_poi_nodes:
        yield particle_poi.particle.type, particle_poi.particle.id


class Evnt(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "EVNT"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return EVNT

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from dependencies_for(self.raw, self.target_game)
