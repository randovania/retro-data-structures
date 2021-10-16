from retro_data_structures.formats.mrea import _MREA
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare, parse_and_build_compare_parsed

_mrea_path_p1 = "Resources/Worlds/EndCinema/!EndCinema_Master/01_endcinema.MREA"
_mrea_path_p2 = "Resources/Worlds/TempleHub/!TempleHub_Master/game_end_part5.MREA"


def test_compare_p1(prime1_pwe_project):
    path = prime1_pwe_project.joinpath(_mrea_path_p1)

    parse_and_build_compare_parsed(_MREA(lambda this: True), Game.PRIME, path)


def test_compare_p2(prime2_pwe_project):
    path = prime2_pwe_project.joinpath(_mrea_path_p2)

    # ignoring compression
    parse_and_build_compare(_MREA(lambda this: False), Game.ECHOES, path)

    # with compression
    parse_and_build_compare(_MREA(lambda this: True), Game.ECHOES, path)


# def test_compare_parsed_p2(prime2_pwe_project):
#     path = prime2_pwe_project.joinpath(_mrea_path_p2)

#     # ignoring compression
#     parse_and_build_compare_parsed(MREA(lambda this: False), Game.ECHOES, path)

#     # with compression
#     parse_and_build_compare_parsed(MREA(lambda this: True), Game.ECHOES, path, True, True)
