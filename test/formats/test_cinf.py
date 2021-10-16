from retro_data_structures.formats.cinf import CINF
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare


def test_compare_p1(prime1_pwe_project):
    parse_and_build_compare(CINF, Game.PRIME, prime1_pwe_project.joinpath("Resources/Uncategorized/tickspin.CINF"))


def test_compare_p2(prime2_pwe_project):
    parse_and_build_compare(
        CINF, Game.ECHOES, prime2_pwe_project.joinpath("Resources/Uncategorized/Swamplands_Luminoth_Hologram.CINF")
    )
