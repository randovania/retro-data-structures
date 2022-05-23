from retro_data_structures.formats.scan import SCAN
from retro_data_structures.game_check import Game

from test.test_lib import parse_and_build_compare


def test_compare_p1(prime1_pwe_project):
    parse_and_build_compare(
        SCAN, Game.PRIME, prime1_pwe_project.joinpath("Resources/Uncategorized/Chozo Lore 002.SCAN")
    )


def test_compare_p2(prime2_pwe_project):
    parse_and_build_compare(SCAN, Game.ECHOES, prime2_pwe_project.joinpath("Resources/Uncategorized/Brizgee_0.SCAN"))


def test_compare_p3(prime3_pwe_project):
    parse_and_build_compare(
        SCAN,
        Game.CORRUPTION,
        prime3_pwe_project.joinpath("Resources/uncategorized/Your PED Suit will allow you to absorb this Phazon.SCAN"),
    )
