import typing

import construct
from construct import Struct, PrefixedArray, Int32ub, If, Aligned

from retro_data_structures import game_check
from retro_data_structures.common_types import String, Vector3, Quaternion
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.game_check import Game

Bone = Struct(
    id=Int32ub,
    parent_id=Int32ub,
    position=Vector3,
    rotation=If(game_check.current_game_at_least(Game.ECHOES), Quaternion),
    local_rotation=If(game_check.current_game_at_least(Game.ECHOES), Quaternion),
    linked_bone_id_array=PrefixedArray(Int32ub, Int32ub),
)

BoneName = Struct(
    name=String,
    bone_id=Int32ub,
)

CINF = Aligned(
    32,
    Struct(
        bones=PrefixedArray(Int32ub, Bone),
        build_order_id=PrefixedArray(Int32ub, Int32ub),
        bone_names=PrefixedArray(Int32ub, BoneName),
    ),
    pattern=b"\xFF",
)


class Cinf(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "CINF"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return CINF

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
