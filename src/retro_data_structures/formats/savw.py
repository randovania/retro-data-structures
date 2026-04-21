"""
The SAVW format describes save data in the Metroid Prime series and Donkey Kong Country Returns.

Reference: https://wiki.axiodl.com/w/SAVW_(File_Format)
"""

from __future__ import annotations

import enum
import typing

import construct
from construct import Const, If, Int32ub, PrefixedArray

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import GUID, String
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.game_check import AssetIdCorrect, Game


class SavwVersion(enum.IntEnum):
    PRIME_1 = 3
    PRIME_2 = 5
    PRIME_3 = 6
    DKCR = 8


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
    # Based on the wiki, these are always 0, 1 and 0 respectively. Their use is unknown.
    unk_a=Int32ub,
    unk_b=Int32ub,
    unk_c=Int32ub,
)


def _before_corruption(ctx: construct.Container) -> bool:
    return ctx.version < SavwVersion.PRIME_3


def _before_dkcr(ctx: construct.Container) -> bool:
    return ctx.version < SavwVersion.DKCR


def _starting_echoes(ctx: construct.Container) -> bool:
    return ctx.version >= SavwVersion.PRIME_2


def _echoes_or_corruption(ctx: construct.Container) -> bool:
    return ctx.version in {SavwVersion.PRIME_2, SavwVersion.PRIME_3}


def _starting_dkcr(ctx: construct.Container) -> bool:
    return ctx.version >= SavwVersion.DKCR


SAVW = construct.Struct(
    _magic=Const(0xC001D00D, Int32ub),
    version=EnumAdapter(SavwVersion),
    area_count=Int32ub,
    cinematic_skips=PrefixedArray(Int32ub, SavedStateDescriptor),
    memory_relays=PrefixedArray(Int32ub, SavedStateDescriptor),
    layer_toggles=If(_before_corruption, PrefixedArray(Int32ub, LayerToggle)),
    doors=If(_before_dkcr, PrefixedArray(Int32ub, SavedStateDescriptor)),
    scannable_objects=If(_before_dkcr, PrefixedArray(Int32ub, ScannableObject)),
    system_state_env_vars=If(_starting_echoes, PrefixedArray(Int32ub, EnvVar)),
    game_state_env_vars=If(_starting_echoes, PrefixedArray(Int32ub, EnvVar)),
    unmappable_objects=If(_echoes_or_corruption, PrefixedArray(Int32ub, SavedStateDescriptor)),
    puzzle_pieces=If(_starting_dkcr, PrefixedArray(Int32ub, SavedStateDescriptor)),
    _align=AlignTo(lambda this: 64 if this.version >= SavwVersion.PRIME_3 else 32, b"\xff"),
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

    def add_system_state_env_var(self, name: str, unk_a: int = 0, unk_b: int = 1, unk_c: int = 0) -> None:
        """
        Adds a new environment variables to the system state.
        The unknown parameters defaults to the expected values.
        """
        self._raw.system_state_env_vars.append(
            construct.Container(
                name=name,
                unk_a=unk_a,
                unk_b=unk_b,
                unk_c=unk_c,
            )
        )

    def add_game_state_env_var(self, name: str, unk_a: int = 0, unk_b: int = 1, unk_c: int = 0) -> None:
        """
        Adds a new environment variables to the game state.
        The unknown parameters defaults to the expected values.
        """
        self._raw.game_state_env_vars.append(
            construct.Container(
                name=name,
                unk_a=unk_a,
                unk_b=unk_b,
                unk_c=unk_c,
            )
        )
