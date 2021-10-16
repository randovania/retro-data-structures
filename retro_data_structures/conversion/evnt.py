from retro_data_structures.conversion.asset_converter import AssetConverter, Resource, AssetDetails
from retro_data_structures.conversion.errors import UnsupportedTargetGame, UnsupportedSourceGame
from retro_data_structures.game_check import Game

_BONE_NAME_MAPPING = {
    "Skeleton_Root": 1,
    "root": 0,
    "Electric": 6,
    "WBbottom_SDK": 4,
    "WBtop_SDK": 3,
    "move_SDK": 2,
    "snaplocators": 5,
    "Missile_Launcher_SDK": 3,
    "grapple_SDK": 2,
    "skeleton_root": 1,
    "can_SDK": 3,
    "visor_SDK": 2,
    "EnergyTank_SDK": 2,
    "MorphBall_Pickup_SDK": 2,
    "bomb_SDK": 2,
    "power_SDK": 2,
    "powerbombleft_SDK": 3,
    "powerbombright_SDK": 2,
    "Powerup_SDK": 2,
    "bottom_piece": 4,
    "cubes": 2,
    "top_piece": 5,
    "trails": 3,
    "midring_SDK": 4,
    "outring_SDK": 3,
    "rotate_SDK": 2,
}


def _convert_particles(data, converter: AssetConverter, source_game: Game):
    for poi_node in data["particle_poi_nodes"]:
        poi_node["particle"]["id"] = converter.convert_id(poi_node["particle"]["id"], source_game)


def convert_from_prime(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.ECHOES:
        raise UnsupportedTargetGame(Game.PRIME, converter.target_game)

    for particle_poi_node in data["particle_poi_nodes"]:
        particle_poi_node["base"]["unk_1"] = 2

    for i, poi_node in enumerate(data["particle_poi_nodes"]):
        poi_node["bone_id"] = _BONE_NAME_MAPPING.get(poi_node["bone_name"], i)
        poi_node["bone_name"] = None

    for i, sound_poi_node in enumerate(data["sound_poi_nodes"]):
        sound_poi_node["base"]["unk_1"] = 2
        sound_poi_node["sound_id"] = 0x80002748
        sound_poi_node["echoes"] = {"unk_a": 0, "unk_b": 7372, "unk_c": 7372, "unk_d": 0}

    _convert_particles(data, converter, Game.PRIME)

    return data


def convert_from_echoes(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.PRIME:
        raise UnsupportedTargetGame(Game.ECHOES, converter.target_game)

    for particle_poi_node in data["particle_poi_nodes"]:
        particle_poi_node["base"]["unk_1"] = 1

    for i, poi_node in enumerate(data["particle_poi_nodes"]):
        bone_name = str(poi_node["base"]["name"]).split("-", 1)
        poi_node["bone_name"] = f"{bone_name[0]}"  # HACK - Not sure this will always work...?
        poi_node["bone_id"] = None

    for i, sound_poi_node in enumerate(data["sound_poi_nodes"]):
        sound_poi_node["base"]["unk_1"] = 1
        sound_poi_node["sound_id"] = 0x80000074
        sound_poi_node["echoes"] = None

    _convert_particles(data, converter, Game.ECHOES)

    return data


def convert_from_corruption(data: Resource, details: AssetDetails, converter: AssetConverter):
    raise UnsupportedSourceGame(Game.CORRUPTION)


CONVERTERS = {
    Game.PRIME: convert_from_prime,
    Game.ECHOES: convert_from_echoes,
    Game.CORRUPTION: convert_from_corruption,
}
