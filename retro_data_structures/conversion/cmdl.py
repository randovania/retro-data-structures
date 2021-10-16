from construct.lib import ListContainer

from retro_data_structures.conversion.asset_converter import AssetConverter, Resource, AssetDetails
from retro_data_structures.conversion.errors import UnsupportedTargetGame, UnsupportedSourceGame
from retro_data_structures.game_check import Game


def _convert_textures(material_set, converter: AssetConverter, source_game: Game):
    material_set["texture_file_ids"] = ListContainer(
        [converter.convert_id(file_id, source_game) for file_id in material_set["texture_file_ids"]]
    )


def convert_from_prime(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.ECHOES:
        raise UnsupportedTargetGame(Game.PRIME, converter.target_game)

    data["version"] = 4
    for material_set in data["material_sets"]:
        _convert_textures(material_set, converter, Game.PRIME)

        for material in material_set["materials"]:
            material["flags"] |= 0x3000
            material["vertex_attribute_flags"] |= 0x81000000
            material["unk_1"] = 0
            material["unk_2"] = 0

    for surface in data["surfaces"]:
        surface["header"]["unk_1"] = 0
        surface["header"]["unk_2"] = 0
        for primitive in surface["primitives"]:
            for vertex in primitive["vertices"]:
                vertex["matrix"]["position"] = 0
                vertex["matrix"]["tex"]["6"] = 0

    return data


def convert_from_echoes(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.PRIME:
        raise UnsupportedTargetGame(Game.ECHOES, converter.target_game)

    data["version"] = 2
    for material_set in data["material_sets"]:
        _convert_textures(material_set, converter, Game.ECHOES)

        for material in material_set["materials"]:
            material["flags"] |= 0x1
            material["flags"] &= ~0x3000
            material["vertex_attribute_flags"] &= ~0x81000000
            material["unk_1"] = None
            material["unk_2"] = None

    for surface in data["surfaces"]:
        surface["header"]["unk_1"] = None
        surface["header"]["unk_2"] = None
        for primitive in surface["primitives"]:
            for vertex in primitive["vertices"]:
                vertex["matrix"]["position"] = None
                vertex["matrix"]["tex"]["6"] = None

    return data


def convert_from_corruption(data: Resource, details: AssetDetails, converter: AssetConverter):
    raise UnsupportedSourceGame(Game.CORRUPTION)


CONVERTERS = {
    Game.PRIME: convert_from_prime,
    Game.ECHOES: convert_from_echoes,
    Game.CORRUPTION: convert_from_corruption,
}
