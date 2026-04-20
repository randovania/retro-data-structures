from __future__ import annotations

import typing

import construct
from construct import Const, If, Int32ub, PrefixedArray

from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import GUID, String
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.game_check import AssetIdCorrect, Game

SavedStateDescriptor = construct.Struct(
    guid=If(construct.this._root.version >= 6, GUID),
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

EnvVar = construct.Struct(
    name=String,
    unk_a=Int32ub,
    unk_b=Int32ub,
    unk_c=Int32ub,
)

SAVW = construct.Struct(
    _magic=Const(0xC001D00D, Int32ub),
    version=Int32ub,
    area_count=Int32ub,
    cinematic_skips=PrefixedArray(Int32ub, SavedStateDescriptor),
    memory_relays=PrefixedArray(Int32ub, SavedStateDescriptor),
    layer_toggles=If(construct.this.version <= 5, PrefixedArray(Int32ub, LayerToggle)),
    doors=PrefixedArray(Int32ub, SavedStateDescriptor),
    scannable_objects=PrefixedArray(Int32ub, ScannableObject),
    system_state_env_vars=If(construct.this.version >= 5, PrefixedArray(Int32ub, EnvVar)),
    game_state_env_vars=If(construct.this.version >= 5, PrefixedArray(Int32ub, EnvVar)),
    unmappable_objects=If(lambda this: 5 <= this.version <= 6, PrefixedArray(Int32ub, SavedStateDescriptor)),
    puzzle_pieces=If(construct.this.version >= 8, PrefixedArray(Int32ub, SavedStateDescriptor)),
    _align=AlignTo(lambda this: 64 if this.version >= 6 else 32, b"\xff"),
    _end=construct.Terminated,
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
