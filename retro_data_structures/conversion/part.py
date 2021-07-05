import functools

from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.game_check import Game


def upgrade(data, converter: AssetConverter, source_game: Game):
    if source_game < Game.ECHOES <= converter.target_game:
        for element in data["elements"]:
            if element["type"] == u'KSSM' and element["body"]["magic"] != "NONE":
                for spawn in element["body"]["value"]["spawns"]:
                    for t in spawn["v2"]:
                        t["type"] = "PART"


def downgrade(data, converter: AssetConverter, source_game: Game):
    if converter.target_game <= Game.PRIME < source_game:
        for element in data["elements"]:
            if element["type"] == u'KSSM' and element["body"]["magic"] != "NONE":
                for spawn in element["body"]["value"]["spawns"]:
                    for t in spawn["v2"]:
                        t["type"] = 0
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


def convert(data, converter: AssetConverter, source_game: Game):
    if source_game.value < converter.target_game.value:
        upgrade(data, converter, source_game)
    elif source_game.value > converter.target_game.value:
        downgrade(data, converter, source_game)

    # convert asset references
    for element in data["elements"]:
        if element["type"] in ('TEXR', 'TIND'):
            body = element["body"]["body"]
            if body is not None:
                if body["id"] is not None:
                    body["id"] = converter.convert_by_id(body["id"], source_game)

        if element["type"] == 'KSSM' and element["body"]["magic"] != "NONE":
            for spawn in element["body"]["value"]["spawns"]:
                for t in spawn["v2"]:
                    t["id"] = converter.convert_by_id(t["id"], source_game)

        if element["type"] in ('SSWH', 'PMDL', 'SELC', 'IDTS', 'ICTS', 'IITS'):
            body = element["body"]
            if body["body"] is not None and source_game.is_valid_asset_id(body["body"]):
                body["body"] = converter.convert_by_id(body["body"], source_game)

    return data


class PARTConverter(dict):
    def __missing__(self, key: Game):
        if isinstance(key, Game):
            return functools.partial(convert, source_game=key)
        else:
            raise KeyError(key)


CONVERTERS = PARTConverter()
