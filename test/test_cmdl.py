from pathlib import Path

import construct

from retro_data_structures.cmdl import CMDL
from retro_data_structures.common_types import AABox

CMDLHeader = construct.Struct(
    magic=construct.Const(0xDEADBABE, construct.Int32ub),
    version=construct.Int32ub,
    flags=construct.Int32ub,
    aabox=AABox,
    data_section_count=construct.Int32ub,
    material_set_count=construct.Int32ub,
    data_section_sizes=construct.Array(construct.this.data_section_count, construct.Int32ub),
)


def test_compare(prime2_pwe_project):
    input_path = prime2_pwe_project.joinpath("Resources/Uncategorized/annihilatorBeam.CMDL")
    game = 2
    raw = input_path.read_bytes()

    data = CMDL.parse(raw, target_game=game)
    encoded = CMDL.build(data, target_game=game)

    raw_header = CMDLHeader.parse(raw)
    custom_header = CMDLHeader.parse(encoded)

    assert custom_header == raw_header
    assert encoded == raw
