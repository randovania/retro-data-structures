import typing

import construct
from construct import Const, Int32ub, PrefixedArray

from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.game_check import Game, AssetIdCorrect

SavedStateDescriptor = construct.Struct(
    # TODO: guid for mp3+
    instance_id=Int32ub,
)

LayerToggle = construct.Struct(
    area_id=Int32ub,
    layer_index=Int32ub,
)

ScannableObject = construct.Struct(
    scan_asset_id=AssetIdCorrect,
    logbook_category=Int32ub,
)

SAVW = construct.Struct(
    _magic=Const(0xC001D00D, Int32ub),
    version=Int32ub,
    area_count=Int32ub,
    cinematic_skips=PrefixedArray(Int32ub, SavedStateDescriptor),
    memory_relays=PrefixedArray(Int32ub, SavedStateDescriptor),
    layer_toggles=PrefixedArray(Int32ub, LayerToggle),
    doors=PrefixedArray(Int32ub, SavedStateDescriptor),
    scannable_objects=PrefixedArray(Int32ub, ScannableObject),
    rest=construct.GreedyBytes,
)


class Savw(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "SAVW"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return SAVW

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
