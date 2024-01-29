"""
https://wiki.axiodl.com/w/SCAN_(File_Format)
"""

from __future__ import annotations

import logging
import typing

import construct
from construct import Aligned, Int32ub, Struct
from construct.core import Array, Byte, Check, Const, Enum, Float32b, GreedyRange, Hex, IfThenElse

from retro_data_structures import game_check
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AssetId32, FourCC
from retro_data_structures.formats import dgrp
from retro_data_structures.formats.dgrp import DGRP
from retro_data_structures.formats.script_object import ConstructScriptInstance, ScriptInstance
from retro_data_structures.game_check import Game

ScanImage = Struct(
    "texture" / AssetId32,  # TXTR
    "appearance_threshold" / Float32b,
    Check(lambda this: this.appearance_threshold >= 0.0 and this.appearance_threshold <= 1.0),
    "image_position" / Int32ub,
    "width" / Int32ub,
    "height" / Int32ub,
    "interval" / Float32b,
    "duration" / Float32b,
)

Prime1SCAN = Struct(
    "version" / Enum(Int32ub, demo=3, final=5),
    "magic" / Hex(Const(0x0BADBEEF, Int32ub)),
    "frame_id" / AssetId32,  # FRME
    "text_id" / AssetId32,  # STRG
    "scan_speed" / Enum(Int32ub, fast=0, slow=1),
    "logbook_category" / Enum(Int32ub, none=0, pirate=1, chozo=2, creatures=3, research=4, artifacts=5),
    "scan_icon" / Enum(Byte, orange=0, red=1),
    "scan_images" / Array(4, ScanImage),
    "junk" / GreedyRange(Byte),
)

Prime23SCAN = Aligned(
    32,
    Struct(
        "magic" / Const("SCAN", FourCC),
        "unknown1" / Const(2, Int32ub),
        "unknown2" / Byte,
        "instance_count" / Const(1, Int32ub),
        "scannable_object_info" / ConstructScriptInstance,
        "dependencies" / DGRP,
    ),
    b"\xff",
)

SCAN = IfThenElse(game_check.is_prime1, Prime1SCAN, Prime23SCAN)


def legacy_dependencies(obj, target_game: Game):
    if target_game == Game.PRIME:
        yield "FRME", obj.frame_id
        yield "STRG", obj.text_id
        for image in obj.scan_images:
            yield "TXTR", image.texture
    else:
        yield from dgrp.legacy_dependencies(obj.dependencies, target_game)


class Scan(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "SCAN"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return SCAN

    def _internal_dependencies_for(self) -> typing.Iterator[Dependency]:
        if self.target_game == Game.PRIME:
            yield from self.asset_manager.get_dependencies_for_asset(self.raw.frame_id)
            yield from self.asset_manager.get_dependencies_for_asset(self.raw.text_id)
            for image in self.raw.scan_images:
                yield from self.asset_manager.get_dependencies_for_asset(image.texture)
        else:
            scan_info = self.scannable_object_info.get_properties()
            yield from scan_info.dependencies_for(self.asset_manager)

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        for it in self._internal_dependencies_for():
            yield Dependency(it.type, it.id, True)

    _scannable_object_info: ScriptInstance | None = None

    @property
    def scannable_object_info(self) -> ScriptInstance:
        assert self.target_game != Game.PRIME
        if self._scannable_object_info is None:
            self._scannable_object_info = ScriptInstance(
                self._raw.scannable_object_info, self.target_game, on_modify=self.rebuild_dependencies
            )
        return self._scannable_object_info

    def rebuild_dependencies(self):
        logging.debug("rebuilding deps for a SCAN!")
        if self.target_game == Game.PRIME:
            return
        scan_info = self.scannable_object_info.get_properties()
        self._raw.dependencies = [
            {"asset_type": dep.type, "asset_id": dep.id} for dep in scan_info.dependencies_for(self.asset_manager)
        ]
