"""
https://wiki.axiodl.com/w/SCAN_(File_Format)
"""

import typing

import construct
from construct import Struct, Int32ub
from construct.core import Array, Byte, Check, Const, Enum, Float32b, GreedyRange, Hex, IfThenElse

from retro_data_structures import game_check
from retro_data_structures.common_types import AssetId32, FourCC
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.formats import dgrp
from retro_data_structures.formats.dgrp import DGRP
from retro_data_structures.formats.script_object import ScriptInstance, ScriptInstanceHelper
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

Prime23SCAN = Struct(
    "magic" / Const("SCAN", FourCC),
    "unknown1" / Const(2, Int32ub),
    "unknown2" / Byte,
    "instance_count" / Const(1, Int32ub),
    "scannable_object_info" / ScriptInstance,
    "dependencies" / DGRP,
    "junk" / GreedyRange(Byte),
)

SCAN = IfThenElse(game_check.is_prime1, Prime1SCAN, Prime23SCAN)


def dependencies_for(obj, target_game: Game):
    if target_game == Game.PRIME:
        yield "FRME", obj.frame_id
        yield "STRG", obj.text_id
        for image in obj.scan_images:
            yield "TXTR", image.texture
    else:
        yield from dgrp.dependencies_for(obj.dependencies, target_game)


class Scan(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "SCAN"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return SCAN

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from dependencies_for(self.raw, self.target_game)
    
    @property
    def scannable_object_info(self) -> ScriptInstanceHelper:
        assert self.target_game != Game.PRIME
        return ScriptInstanceHelper(self._raw.scannable_object_info, self.target_game)
