from retro_data_structures.formats.cskr import CSKR
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare


def test_compare_p1(prime1_pwe_project):
    parse_and_build_compare(CSKR, Game.PRIME, prime1_pwe_project.joinpath("Resources/NoARAM/Fusion.CSKR"))


def test_compare_p2(prime2_pwe_project):
    parse_and_build_compare(CSKR, Game.ECHOES, prime2_pwe_project.joinpath("Resources/SamusGunLow/Holo.CSKR"))
