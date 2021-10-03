"""
https://wiki.axiodl.com/w/SCAN_(File_Format)
"""

from construct import (Array, Byte, Check, Const, Enum, Flag, Float32b,
                       GreedyRange, Hex, IfThenElse, Int32sb, Int32ub, Struct)
from retro_data_structures import game_check
from retro_data_structures.common_types import AssetId32, FourCC, String
from retro_data_structures.formats import dgrp
from retro_data_structures.formats.dgrp import DGRP
from retro_data_structures.formats.script_object import ScriptInstance
from retro_data_structures.game_check import AssetIdCorrect, Game
from retro_data_structures.properties import AddPropertyInfo, SubProperties

ScanImage = Struct(
    "texture" / AssetId32, #TXTR
    "appearance_threshold" / Float32b,
    Check(lambda this: this.appearance_threshold >= 0.0 and this.appearance_threshold <= 1.0),
    "image_position" / Int32ub,
    "width" / Int32ub,
    "height" / Int32ub,
    "interval" / Float32b,
    "duration" / Float32b
)

Prime1SCAN = Struct(
    "version" / Enum(Int32ub, demo=3, final=5),
    "magic" / Hex(Const(0x0BADBEEF, Int32ub)),
    "frame_id" / AssetId32, # FRME
    "text_id" / AssetId32, # STRG
    "scan_speed" / Enum(Int32ub, fast=0, slow=1),
    "logbook_category" / Enum(
        Int32ub,
        none=0,
        pirate=1,
        chozo=2,
        creatures=3,
        research=4,
        artifacts=5
    ),
    "scan_icon" / Enum(Byte, orange=0, red=1),
    "scan_images" / Array(4, ScanImage),
    "junk" / GreedyRange(Byte)
)

# ScannableObjectInfo Properties
AddPropertyInfo(0x2F5B6423, AssetIdCorrect, "STRG, Scan Text")
AddPropertyInfo(0xC308A322, Int32sb, "Scan Speed (0 for fast, 1 for slow)")
AddPropertyInfo(0x7B714814, Flag, "Is Important? (0 for blue, 1 for red)")
AddPropertyInfo(0x1733B1EC, Flag, "Use Logbook Model After Scan?")
AddPropertyInfo(0x53336141, AssetIdCorrect, "CMDL, Post-Scan Override Texture")
AddPropertyInfo(0x3DE0BA64, Float32b, "Logbook Default X Rotation")
AddPropertyInfo(0x2ADD6628, Float32b, "Logbook Default Z Rotation")
AddPropertyInfo(0xD0C15066, Float32b, "Logbook Scale")
AddPropertyInfo(0xB7ADC418, AssetIdCorrect, "CMDL, Logbook Model")
AddPropertyInfo(0x15694EE1, Byte, "AnimationParameters, Logbook AnimSet")
AddPropertyInfo(0x58F9FE99, Byte, "AnimationParameters, Unknown")
AddPropertyInfo(0x1C5B4A3A, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x1C5B4A3A, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x8728A0EE, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0xF1CD99D3, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x6ABE7307, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x1C07EBA9, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x8774017D, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0xF1913840, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x6AE2D294, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
AddPropertyInfo(0x1CE2091C, SubProperties, "ScanInfoSecondaryModel, Secondary Model 1")
# TODO: unknown prime 3 property 1
# TODO: unknown prime 3 property 2

# ScanInfoSecondaryModel Properties
AddPropertyInfo(0x1F7921BC, AssetIdCorrect, "CMDL, Model")
AddPropertyInfo(0xCDD202D1, Byte, "AnimationParameters, AnimSet")
AddPropertyInfo(0x3EA2BED8, String, "Attach Bone Name")

Prime23SCAN = Struct(
    "magic" / Const("SCAN", FourCC),
    "unknown1" / Const(2, Int32ub),
    "unknown2" / Byte,
    "instance_count" / Const(1, Int32ub),
    "scannable_object_info" / ScriptInstance,
    "dependencies" / DGRP,
    "junk" / GreedyRange(Byte)
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
