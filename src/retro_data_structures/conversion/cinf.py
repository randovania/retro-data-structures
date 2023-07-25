from __future__ import annotations

from typing import TYPE_CHECKING

from retro_data_structures.conversion.errors import UnsupportedSourceGame, UnsupportedTargetGame
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.conversion.asset_converter import AssetConverter, AssetDetails, Resource


def convert_from_prime(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.ECHOES:
        raise UnsupportedTargetGame(Game.PRIME, converter.target_game)

    for bone in data["bones"]:
        bone["id"] = bone["id"] - 3
        if bone["parent_id"] == 2:
            bone["parent_id"] = 0x61
        else:
            bone["parent_id"] = bone["parent_id"] - 3
        for i, it in enumerate(bone["linked_bone_id_array"]):
            if it == 2:
                bone["linked_bone_id_array"][i] = 0x61
            else:
                bone["linked_bone_id_array"][i] = it - 3

        bone["rotation"] = [1.0, 0.0, 0.0, 0.0]
        bone["local_rotation"] = [1.0, 0.0, 0.0, 0.0]

    for i, it in enumerate(data["build_order_id"]):
        data["build_order_id"][i] = it - 3

    for bone_name in data["bone_names"]:
        bone_name["bone_id"] = bone_name["bone_id"] - 3

    return data


def convert_from_echoes(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.PRIME:
        raise UnsupportedTargetGame(Game.ECHOES, converter.target_game)

    for bone in data["bones"]:
        bone["id"] = bone["id"] + 3
        if bone["parent_id"] == 0x61:
            bone["parent_id"] = 2
        else:
            bone["parent_id"] = bone["parent_id"] + 3
        for i, it in enumerate(bone["linked_bone_id_array"]):
            if it == 0x61:
                bone["linked_bone_id_array"][i] = 2
            else:
                bone["linked_bone_id_array"][i] = it + 3

    for i, it in enumerate(data["build_order_id"]):
        data["build_order_id"][i] = it + 3

    for bone_name in data["bone_names"]:
        bone_name["bone_id"] = bone_name["bone_id"] + 3

    return data


def convert_from_corruption(data: Resource, details: AssetDetails, converter: AssetConverter):
    raise UnsupportedSourceGame(Game.CORRUPTION)


CONVERTERS = {
    Game.PRIME: convert_from_prime,
    Game.ECHOES: convert_from_echoes,
    Game.CORRUPTION: convert_from_corruption,
}
