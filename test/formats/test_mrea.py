from pathlib import Path

import pytest

from retro_data_structures.formats.mrea import MREA
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare, parse_and_build_compare_parsed, purge_hidden

_mrea_path_p1 = "Resources/Worlds/EndCinema/!EndCinema_Master/01_endcinema.MREA"
_mrea_path_p2 = "Resources/Worlds/TempleHub/!TempleHub_Master/game_end_part5.MREA"


@pytest.fixture(name="p1_mrea_path")
def _p1_mrea_path(prime1_pwe_project) -> Path:
    return prime1_pwe_project.joinpath(_mrea_path_p1)


@pytest.fixture(name="p2_mrea_path")
def _p2_mrea_path(prime2_pwe_project) -> Path:
    return prime2_pwe_project.joinpath(_mrea_path_p2)


def test_compare_p1(p1_mrea_path):
    # Known difference: some Prime 1 script layers have sizes that
    # are not multiples of 32; building always pads to 32
    parse_and_build_compare(MREA, Game.PRIME, p1_mrea_path)


def test_compare_p1_parsed(p1_mrea_path):
    parse_and_build_compare_parsed(MREA, Game.PRIME, p1_mrea_path)


def test_compare_p2(p2_mrea_path):
    parse_and_build_compare_parsed(MREA, Game.ECHOES, p2_mrea_path)


def test_parse_build_twice(p2_mrea_path):
    game = Game.ECHOES
    raw = p2_mrea_path.read_bytes()

    data1 = purge_hidden(MREA.parse(raw, target_game=game))
    data2 = purge_hidden(MREA.parse(raw, target_game=game))
    encoded1 = MREA.build(data1, target_game=game)
    encoded2 = MREA.build(data2, target_game=game)

    assert data1 == data2
    assert encoded1 == encoded2
