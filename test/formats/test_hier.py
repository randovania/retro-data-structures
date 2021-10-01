from retro_data_structures.formats.hier import HIER
from retro_data_structures.game_check import Game
from test_lib import parse_and_build_compare

def test_compare(prime2_pwe_project):
    parse_and_build_compare(HIER, Game.ECHOES, prime2_pwe_project.joinpath(
        "NoARAM/DUMB_ScanHierarchy.DUMB"
    ))