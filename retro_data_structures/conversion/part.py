from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.conversion.errors import UnsupportedSourceGame, UnsupportedTargetGame
from retro_data_structures.game_check import Game


def part_convert(data, output_game):
    if output_game == 1:
        for element in data["elements"]:
            if element["type"] == u'KSSM':
                element["body"]["value"]["spawns"][0]["v2"][0]["type"] = 0
            if element["type"] == u'RDOP':
                element.pop()
            if element["type"] == u'XTAD':
                element.pop()
            if element["type"] == u'VMPC':
                element.pop()
            if element["type"] == u'VMPC':
                element.pop()
            if element["type"] == u'EMTR':
                if element["body"]["type"] == u'ELPS':
                    element["body"]["type"] = u'SPHE'
                    element["body"]["body"]["b"] = element["body"]["body"]["b"]["body"]["a"]
                    element["body"]["body"]["c"] = element["body"]["body"]["d"]
                    element["body"]["body"].pop("d")
                    element["body"]["body"].pop("e")
        return data
    elif output_game == 2:
        for element in data["elements"]:
            if element["type"] == u'KSSM':
                element["body"]["value"]["spawns"][0]["v2"][0]["type"] = u'PART'
        return data
    elif output_game == 3:
        return data


def convert_from_prime(data, converter: AssetConverter):
    if converter.target_game != Game.ECHOES:
        raise UnsupportedTargetGame(Game.PRIME, converter.target_game)

    # TODO
    return data


def convert_from_echoes(data, converter: AssetConverter):
    if converter.target_game != Game.PRIME:
        raise UnsupportedTargetGame(Game.ECHOES, converter.target_game)

    # TODO
    return data


def convert_from_corruption(data, converter: AssetConverter):
    raise UnsupportedSourceGame(Game.CORRUPTION)


CONVERTERS = {
    Game.PRIME: convert_from_prime,
    Game.ECHOES: convert_from_echoes,
    Game.CORRUPTION: convert_from_corruption,
}
