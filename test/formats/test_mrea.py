from retro_data_structures.formats.mrea import MREA
from retro_data_structures.game_check import Game
from test.test_lib import parse_and_build_compare

def test_compare(prime2_pwe_project):
    parse_and_build_compare(MREA, Game.ECHOES, prime2_pwe_project.joinpath(
        "Resources/Worlds/TempleInt/!TempleInt_Master/07_temple_mothlordsanctuary.MREA"
    ), True)