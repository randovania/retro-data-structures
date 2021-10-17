import construct

from retro_data_structures.formats.cmdl import CMDL
from retro_data_structures.common_types import AABox
from retro_data_structures.construct_extensions.json import convert_to_raw_python
from retro_data_structures.game_check import Game

CMDLHeader = construct.Struct(
    magic=construct.Const(0xDEADBABE, construct.Int32ub),
    version=construct.Int32ub,
    flags=construct.Int32ub,
    aabox=AABox,
    data_section_count=construct.Int32ub,
    material_set_count=construct.Int32ub,
    data_section_sizes=construct.Array(construct.this.data_section_count, construct.Int32ub),
)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def test_compare(prime2_pwe_project):
    input_path = prime2_pwe_project.joinpath("Resources/Uncategorized/annihilatorBeam.CMDL")
    game = Game.ECHOES
    raw = input_path.read_bytes()

    data = CMDL.parse(raw, target_game=game)
    data_as_dict = convert_to_raw_python(data)
    encoded = CMDL.build(data_as_dict, target_game=game)

    raw_header = CMDLHeader.parse(raw, target_game=game)
    custom_header = CMDLHeader.parse(encoded, target_game=game)

    assert custom_header == raw_header
    assert [int.from_bytes(c, "big") for c in chunks(encoded, 4)] == [int.from_bytes(c, "big") for c in chunks(raw, 4)]
