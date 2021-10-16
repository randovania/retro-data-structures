from retro_data_structures.formats.tree import TREE
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare


def test_compare(prime2_pwe_project):
    parse_and_build_compare(TREE, Game.ECHOES, prime2_pwe_project.joinpath("Resources/Logbook/DUMB_ScanTree.DUMB"))
