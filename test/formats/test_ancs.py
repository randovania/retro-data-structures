from retro_data_structures.formats.ancs import ANCS
from retro_data_structures.construct_extensions import convert_to_raw_python
from retro_data_structures.game_check import Game


def test_compare_p1(prime1_pwe_project):
    input_path = prime1_pwe_project.joinpath("Resources/Uncategorized/alpha_metaree.ANCS")
    game = Game.PRIME
    raw = input_path.read_bytes()

    data = ANCS.parse(raw, target_game=game)
    encoded = ANCS.build(data, target_game=game)

    assert encoded == raw


def test_compare_p2(prime2_pwe_project):
    input_path = prime2_pwe_project.joinpath("Resources/Uncategorized/annihilatorBeam.ANCS")
    game = Game.ECHOES
    raw = input_path.read_bytes()

    data = ANCS.parse(raw, target_game=game)
    data_as_dict = convert_to_raw_python(data)
    encoded = ANCS.build(data_as_dict, target_game=game)

    assert encoded == raw
