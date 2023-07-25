from __future__ import annotations

import re
import struct
import typing

import construct

from retro_data_structures.common_types import AssetId32, FourCC, String
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.data_section import DataSection
from retro_data_structures.exceptions import UnknownAssetId
from retro_data_structures.formats import Part, effect_script
from retro_data_structures.formats.hier import Hier
from retro_data_structures.formats.tree import Tree
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetType, Dependency, RawResource


class UnableToCheatError(Exception):
    pass


def _cheat(stream: bytes, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    asset_id_size = 4 if asset_manager.target_game.uses_asset_id_32 else 8
    max_byte = len(stream) - asset_id_size
    fmt = ">L" if asset_manager.target_game.uses_asset_id_32 else ">Q"

    for i in range(max_byte):
        possible_id = struct.unpack_from(fmt, buffer=stream, offset=i)[0]
        yield from asset_manager.get_dependencies_for_asset(possible_id, must_exist=False)


_csng = construct.FocusedSeq(
    "agsc_id", construct.Const(2, construct.Int32ub), construct.Seek(0xC), "agsc_id" / construct.Int32ub
)


def csng_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    yield from asset_manager.get_dependencies_for_asset(_csng.parse(asset.data))


def dumb_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    try:
        magic = FourCC.parse(asset.data)
    except Exception:
        raise UnableToCheatError

    if magic == "HIER":
        hier = Hier.parse(asset.data, asset_manager.target_game, asset_manager)
        yield from hier.dependencies_for()
    elif magic == "TREE":
        tree = Tree.parse(asset.data, asset_manager.target_game, asset_manager)
        yield from tree.dependencies_for()
    else:
        raise UnableToCheatError


_frme = construct.FocusedSeq(
    "deps",
    construct.Int32ub,
    "deps" / construct.PrefixedArray(construct.Int32ub, construct.Struct(type=FourCC, id=construct.Int32ub)),
)


def frme_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    for dep in _frme.parse(asset.data):
        try:
            yield from asset_manager.get_dependencies_for_asset(dep.id)
        except UnknownAssetId:
            raise UnableToCheatError


_fsm2 = construct.Struct(
    construct.Const(b"FSM2"),
    "version" / construct.Int32ub,
    "num_states" / construct.Int32ub,
    "num_unk1" / construct.Int32ub,
    "num_unk2" / construct.Int32ub,
    "num_unk3" / construct.Int32ub,
    "states"
    / construct.Array(
        lambda ctx: ctx.num_states,
        construct.Sequence(
            String,
            construct.If(lambda ctx: ctx._.version >= 2, construct.Seek(0x10, 1)),
            construct.PrefixedArray(construct.Int32ub, construct.Sequence(String, construct.Seek(0x4, 1))),
        ),
    ),
    "unk1"
    / construct.Array(
        lambda ctx: ctx.num_unk1,
        construct.Sequence(
            String,
            construct.If(lambda ctx: ctx._.version >= 2, construct.Seek(0x10, 1)),
            construct.Seek(0x4, 1),
            construct.PrefixedArray(construct.Int32ub, construct.Sequence(String, construct.Seek(0x4, 1))),
            construct.Seek(0x1, 1),
        ),
    ),
    "unk2"
    / construct.Array(
        lambda ctx: ctx.num_unk2,
        construct.Sequence(
            String,
            construct.If(lambda ctx: ctx._.version >= 2, construct.Seek(0x10, 1)),
            construct.PrefixedArray(construct.Int32ub, construct.Sequence(String, construct.Seek(0x4, 1))),
        ),
    ),
    "unk3"
    / construct.Array(
        lambda ctx: ctx.num_unk3,
        construct.Struct(
            "str" / String,
            construct.If(lambda ctx: ctx._.version >= 2, construct.Seek(0x10, 1)),
            "unk" / construct.PrefixedArray(construct.Int32ub, construct.Sequence(String, construct.Seek(0x4, 1))),
            "dep" / construct.Int32ub,
        ),
    ),
)


def fsm2_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    fsm2 = _fsm2.parse(asset.data)
    for unk in fsm2.unk3:
        yield from asset_manager.get_dependencies_for_asset(unk.dep)


_hint = construct.Struct(
    construct.Const(0x00BADBAD, construct.Int32ub),
    "version" / construct.Int32ub,
    "hints"
    / construct.PrefixedArray(
        construct.Int32ub,
        construct.Struct(
            "name" / String,
            "immediate_time" / construct.Float32b,
            "normal_time" / construct.Float32b,
            "popup_strg" / construct.Int32ub,
            "text_time" / construct.Float32b,
            "locations"
            / construct.PrefixedArray(
                construct.Int32ub,
                construct.Struct(
                    "mlvl" / construct.Int32ub,
                    "mrea" / construct.Int32ub,
                    "index" / construct.Int32ub,
                    "map_text_strg" / construct.Int32ub,
                ),
            ),
        ),
    ),
)


def hint_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    hint = _hint.parse(asset.data)
    for h in hint.hints:
        yield from asset_manager.get_dependencies_for_asset(h.popup_strg)
        for loc in h.locations:
            yield from asset_manager.get_dependencies_for_asset(loc.map_text_strg)
            # # there's no way these are recursive, right?
            # # if they're even valid dependencies at all
            # yield "MLVL", loc.mlvl, False
            # yield "MREA", loc.mrea, False


_rule = construct.Pointer(0x5, construct.Int32ub)


def rule_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    yield from asset_manager.get_dependencies_for_asset(_rule.parse(asset.data))


_font = construct.FocusedSeq("txtr", construct.Seek(0x22), String, "txtr" / construct.Int32ub)


def font_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    yield from asset_manager.get_dependencies_for_asset(_font.parse(asset.data))


_cmdl = construct.Struct(
    _skip=construct.Bytes(
        # Magic (4), Version (4), Flags (4), AABox (24)
        36,
    ),
    data_section_count=construct.Int32ub,
    material_set_count=construct.Int32ub,
    data_section_sizes=construct.Array(construct.this.data_section_count, construct.Int32ub),
    _=AlignTo(32),
    material_sets=construct.Array(
        construct.this.material_set_count,
        DataSection(
            # Assumes Prime 1/2
            construct.PrefixedArray(construct.Int32ub, AssetId32),
            size=lambda: construct.Computed(lambda ctx: ctx.data_section_sizes[ctx._index]),
        ),
    ),
)


def cmdl_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    if asset_manager.target_game >= Game.CORRUPTION:
        raise UnableToCheatError

    decoded = _cmdl.parse(asset.data)
    for material_set in decoded.material_sets:
        for txtr_id in material_set:
            yield from asset_manager.get_dependencies_for_asset(txtr_id)


ALL_EFFECTS = [Part]


def _make_re(types: typing.Iterable[AssetType]):
    return re.compile(b"|".join(key.encode("ascii") for key in types))


def effect_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    try:
        effect_type = next(c for c in ALL_EFFECTS if c.resource_type() == asset.type)

        for match in _make_re(effect_type.texture_keys()).finditer(asset.data):
            k = asset.data[match.end() : match.end() + 4]
            element = effect_script.TEXTURE_ELEMENT_TYPES[k.decode()].parse(
                asset.data[match.end() + 4 :],
                target_game=asset_manager.target_game,
            )
            if element is not None:
                yield from asset_manager.get_dependencies_for_asset(element.id, must_exist=False)

        for match in _make_re(effect_type.spawn_system_keys()).finditer(asset.data):
            element = effect_script.SpawnSystemKeyframeData.parse(
                asset.data[match.end() :],
                target_game=asset_manager.target_game,
            )
            if element.magic != "NONE":
                for spawn in element.value.spawns:
                    for t in spawn.v2:
                        yield from asset_manager.get_dependencies_for_asset(t.id, must_exist=False)

        for match in _make_re(effect_type.asset_id_keys()).finditer(asset.data):
            element = effect_script.GetAssetId.parse(
                asset.data[match.end() :],
                target_game=asset_manager.target_game,
            )
            if element is not None and element.body is not None:
                yield from asset_manager.get_dependencies_for_asset(element.body, must_exist=False)
    except Exception:
        raise UnableToCheatError


def no_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    yield from []


_FORMATS_TO_CHEAT = {
    "CSNG": csng_dependencies,
    "DUMB": dumb_dependencies,
    "FRME": frme_dependencies,
    "FSM2": fsm2_dependencies,
    "HINT": hint_dependencies,
    "RULE": rule_dependencies,
    "FONT": font_dependencies,
    "CMDL": cmdl_dependencies,
    "PART": effect_dependencies,
    "AFSM": no_dependencies,
    "DCLN": no_dependencies,
    "STLC": no_dependencies,
    "PATH": no_dependencies,
    "EGMC": no_dependencies,
    "PTLA": no_dependencies,
}


def should_cheat_asset(asset_type: AssetType) -> bool:
    return asset_type in _FORMATS_TO_CHEAT


def get_cheated_dependencies(asset: RawResource, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
    if asset.type in _FORMATS_TO_CHEAT:
        try:
            yield from _FORMATS_TO_CHEAT[asset.type](asset, asset_manager)
            return
        except UnableToCheatError:
            pass

    yield from _cheat(asset.data, asset_manager)
