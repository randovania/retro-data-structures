from retro_data_structures.formats.mrea import MREA, IncludeScriptLayers, IncludeAssetIdLayers
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare, parse_and_build_compare_parsed

_mrea_path = "Resources/Worlds/TempleHub/!TempleHub_Master/game_end_part5.MREA"

def test_compare_raw(prime2_pwe_project):
    path = prime2_pwe_project.joinpath(_mrea_path)

    # ignoring compression
    parse_and_build_compare(MREA(lambda this: False), Game.ECHOES, path)

    # with compression
    parse_and_build_compare(MREA(lambda this: True), Game.ECHOES, path)

def test_compare_parsed(prime2_pwe_project):
    path = prime2_pwe_project.joinpath(_mrea_path)

    # ignoring compression
    parse_and_build_compare_parsed(MREA(lambda this: False), Game.ECHOES, path)

    # with compression
    parse_and_build_compare_parsed(MREA(lambda this: True), Game.ECHOES, path, True)
