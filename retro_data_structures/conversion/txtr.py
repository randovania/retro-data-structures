from retro_data_structures.conversion.asset_converter import AssetConverter, Resource, AssetDetails
from retro_data_structures.game_check import Game


def convert_from_gx1(data: Resource, details: AssetDetails, converter: AssetConverter):
    # This file format only changes in Tropical Freeze
    return data


CONVERTERS = {
    Game.PRIME: convert_from_gx1,
    Game.ECHOES: convert_from_gx1,
    Game.CORRUPTION: convert_from_gx1,
}
