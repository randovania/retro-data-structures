from retro_data_structures.game_check import Game
from retro_data_structures.formats.strg import STRG
from test.test_lib import parse_and_build_compare


def test_compare_p1(prime1_pwe_project):
    parse_and_build_compare(
        STRG, Game.PRIME, prime1_pwe_project.joinpath("Resources/Strings/Uncategorized/Boost Ball.STRG")
    )


def test_compare_p2(prime2_pwe_project):
    # with name table
    parse_and_build_compare(
        STRG, Game.ECHOES, prime2_pwe_project.joinpath("Resources/Strings/Uncategorized/Luminoth Lore.STRG")
    )

    # without name table
    parse_and_build_compare(
        STRG, Game.ECHOES, prime2_pwe_project.joinpath("Resources/Strings/Uncategorized/Light Suit.STRG")
    )


def test_compare_p3(prime3_pwe_project):
    # with name table
    parse_and_build_compare(
        STRG, Game.CORRUPTION, prime3_pwe_project.joinpath("Resources/strings/metroid3/gui/fesliderpopup.STRG")
    )

    # without name table
    parse_and_build_compare(
        STRG, Game.CORRUPTION, prime3_pwe_project.joinpath("Resources/strings/uncategorized/Action.STRG")
    )

    # echoes format
    parse_and_build_compare(
        STRG, Game.CORRUPTION, prime3_pwe_project.joinpath("Resources/strings/metroid2/ingame/languageselection.STRG")
    )
