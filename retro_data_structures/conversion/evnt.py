from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.conversion.errors import UnsupportedTargetGame, UnsupportedSourceGame
from retro_data_structures.game_check import Game


def convert_from_prime(data, converter: AssetConverter):
    if converter.target_game != Game.ECHOES:
        raise UnsupportedTargetGame(Game.PRIME, converter.target_game)

    for particle_poi_node in data["particle_poi_nodes"]:
        particle_poi_node["base"]["unk_1"] = 2

    for i, poi_node in enumerate(data["particle_poi_nodes"]):
        poi_node["bone_name"] = None
        poi_node["bone_id"] = i  # FIXME - Pull Bone ID from corresponding Bone Name - in CINF File

    for i, sound_poi_node in enumerate(data["sound_poi_nodes"]):
        sound_poi_node["base"]["unk_1"] = 2
        sound_poi_node["sound_id"] = 0x80002748
        sound_poi_node["echoes"] = {"unk_a": 0, "unk_b": 7372, "unk_c": 7372, "unk_d": 0}

    return data


def convert_from_echoes(data, converter: AssetConverter):
    if converter.target_game != Game.PRIME:
        raise UnsupportedTargetGame(Game.ECHOES, converter.target_game)

    for particle_poi_node in data["particle_poi_nodes"]:
        particle_poi_node["base"]["unk_1"] = 1

    for i, poi_node in enumerate(data["particle_poi_nodes"]):
        bone_name = str(poi_node["base"]["name"]).split("-", 1)
        poi_node["bone_name"] = f'{bone_name[0]}'  # HACK - Not sure this will always work...?
        poi_node["bone_id"] = None

    for i, sound_poi_node in enumerate(data["sound_poi_nodes"]):
        sound_poi_node["base"]["unk_1"] = 1
        sound_poi_node["sound_id"] = 0x80000074
        sound_poi_node["echoes"] = None

    return data


def convert_from_corruption(data, converter: AssetConverter):
    raise UnsupportedSourceGame(Game.CORRUPTION)


CONVERTERS = {
    Game.PRIME: convert_from_prime,
    Game.ECHOES: convert_from_echoes,
    Game.CORRUPTION: convert_from_corruption,
}
