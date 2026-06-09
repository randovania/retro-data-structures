from __future__ import annotations

import typing

from construct import Const, Construct, Int32ub, PrefixedArray, Struct

from retro_data_structures.base_resource import AssetId, AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AssetId32, Color4f, String, Transform4f
from retro_data_structures.construct_extensions import wrapper_classes
from retro_data_structures.game_check import Game
from retro_data_structures.transform import Transform

if typing.TYPE_CHECKING:
    from construct.lib import Container

_WorldConstruct = Struct(
    "name" / String,
    "mlvl" / AssetId32,
    "transform" / Transform4f,
    "hexagon_transforms" / PrefixedArray(Int32ub, Transform4f),
    "color" / Color4f,
)


class MAPUWorld(wrapper_classes.FieldsMixin):
    def __init__(self, raw: Container):
        self._raw = raw

    name = wrapper_classes.field(str)
    mlvl = wrapper_classes.field(AssetId)
    transform = wrapper_classes.field(Transform)
    hexagon_transforms = wrapper_classes.field(list[Transform])
    color = wrapper_classes.field(list[float])


WorldConstruct = wrapper_classes.WrapperClassAdapter(_WorldConstruct, MAPUWorld)


MAPU = Struct(
    "_magic" / Const(0xABCDEF01, Int32ub),
    "_version" / Const(1, Int32ub),
    "hexagon_mapa" / AssetId32,
    "worlds" / PrefixedArray(Int32ub, WorldConstruct),
)


class Mapu(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "MAPU"

    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        if target_game > Game.ECHOES:
            raise ValueError(f"{target_game} does not support MAPU!")
        return MAPU

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from self.asset_manager.get_dependencies_for_asset(self.raw.hexagon_mapa)

    @property
    def hexagon_mapa(self) -> AssetId:
        return self.raw.hexagon_mapa

    @hexagon_mapa.setter
    def hexagon_mapa(self, value: AssetId) -> None:
        self.raw.hexagon_mapa = value

    @property
    def worlds(self) -> list[MAPUWorld]:
        return self.raw.worlds

    @worlds.setter
    def worlds(self, value: list[MAPUWorld]) -> None:
        self.raw.worlds = value
