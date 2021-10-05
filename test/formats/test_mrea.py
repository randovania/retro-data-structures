from retro_data_structures.formats.mrea import MREA
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare

def test_compare(prime2_pwe_project):
    # ignoring compression
    parse_and_build_compare(MREA(lambda this: False), Game.ECHOES, prime2_pwe_project.joinpath(
        "Resources/Worlds/TempleHub/!TempleHub_Master/game_end_part5.MREA"
    ), True)
