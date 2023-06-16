from __future__ import annotations
import struct
import typing

import construct

from retro_data_structures.base_resource import AssetType, Dependency, RawResource
from retro_data_structures.common_types import String
from retro_data_structures.formats.hier import Hier

if typing.TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager



def _cheat(stream: bytes, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    asset_id_size = 4 if asset_manager.target_game.uses_asset_id_32 else 8
    max_byte = len(stream) - asset_id_size
    fmt = ">L" if asset_manager.target_game.uses_asset_id_32 else ">Q"

    for i in range(max_byte):
        possible_id = struct.unpack_from(fmt, buffer=stream, offset=i)[0]
        yield from asset_manager.get_dependencies_for_asset(possible_id, is_mlvl, not_exist_ok=True)


_csng = construct.FocusedSeq(
        "agsc_id",
        construct.Const(2, construct.Int32ub),
        construct.Seek(0xC),
        "agsc_id" / construct.Int32ub
    )
def csng_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    yield from asset_manager.get_dependencies_for_asset(_csng.parse(asset), is_mlvl)


def dumb_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    hier = Hier.parse(asset.data, asset_manager.target_game, asset_manager)
    yield from hier.dependencies_for(is_mlvl)


_frme = construct.FocusedSeq(
    "deps",
    construct.Int32ub,
    "deps" / construct.PrefixedArray(
        construct.Int32ub,
        construct.Int32ub
    )
)
def frme_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    for dep in _frme.parse(asset.data):
        yield from asset_manager.get_dependencies_for_asset(dep, is_mlvl)


def fsm2_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    raise NotImplementedError()

def fsmc_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    raise NotImplementedError()

def hint_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    raise NotImplementedError()

_rule = construct.Pointer(0x5, construct.Int32ub)
def rule_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    raise NotImplementedError()
    yield from asset_manager.get_dependencies_for_asset(_rule.parse(asset.data), is_mlvl)

_font = construct.FocusedSeq(
    "txtr",
    construct.Seek(0x22),
    String,
    "txtr" / construct.Int32ub
)
def font_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    yield from asset_manager.get_dependencies_for_asset(_font.parse(asset.data), is_mlvl)


_FORMATS_TO_CHEAT = {
    "CSNG": csng_dependencies,
    "DUMB": dumb_dependencies,
    "FRME": frme_dependencies,
    "FSM2": fsm2_dependencies,
    "FSMC": fsmc_dependencies,
    "HINT": hint_dependencies,
    "RULE": rule_dependencies,
    "FONT": font_dependencies,
}

def should_cheat_asset(asset_type: AssetType) -> bool:
    return asset_type in _FORMATS_TO_CHEAT

def get_cheated_dependencies(asset: RawResource, asset_manager: AssetManager, is_mlvl: bool = False) -> typing.Iterator[Dependency]:
    try:
        yield from _FORMATS_TO_CHEAT[asset.type](asset, asset_manager, is_mlvl)
    except:
        yield from _cheat(asset.data, asset_manager, is_mlvl)
