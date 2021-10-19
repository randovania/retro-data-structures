from pathlib import Path

import pytest

from retro_data_structures.formats.mrea import _MREA
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare, parse_and_build_compare_parsed

_mrea_path_p1 = "Resources/Worlds/EndCinema/!EndCinema_Master/01_endcinema.MREA"
_mrea_path_p2 = "Resources/Worlds/TempleHub/!TempleHub_Master/game_end_part5.MREA"


@pytest.fixture(name="p2_mrea_path")
def _p2_mrea_path(prime2_pwe_project) -> Path:
    return prime2_pwe_project.joinpath(_mrea_path_p2)


def test_compare_p1(prime1_pwe_project):
    path = prime1_pwe_project.joinpath(_mrea_path_p1)

    parse_and_build_compare_parsed(_MREA(lambda this: True), Game.PRIME, path)


def test_compare_p2_ignore_compression(p2_mrea_path):
    parse_and_build_compare(_MREA(lambda this: False), Game.ECHOES, p2_mrea_path)


def test_compare_p2_with_compression(p2_mrea_path):
    parse_and_build_compare(_MREA(lambda this: True), Game.ECHOES, p2_mrea_path)

# def test_compare_parsed_p2(prime2_pwe_project):
#     path = prime2_pwe_project.joinpath(_mrea_path_p2)

#     # ignoring compression
#     parse_and_build_compare_parsed(MREA(lambda this: False), Game.ECHOES, path)

#     # with compression
#     parse_and_build_compare_parsed(MREA(lambda this: True), Game.ECHOES, path, True, True)
