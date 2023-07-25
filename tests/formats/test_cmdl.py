from __future__ import annotations

import construct

from retro_data_structures.base_resource import Dependency
from retro_data_structures.common_types import AABox
from retro_data_structures.construct_extensions.json import convert_to_raw_python
from retro_data_structures.formats.cmdl import CMDL
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


def test_compare(prime2_asset_manager):
    # Resources/Uncategorized/annihilatorBeam.CMDL
    raw = prime2_asset_manager.get_raw_asset(0x6FE2E8A0).data
    game = Game.ECHOES

    data = CMDL.parse(raw, target_game=game)
    data_as_dict = convert_to_raw_python(data)
    encoded = CMDL.build(data_as_dict, target_game=game)

    raw_header = CMDLHeader.parse(raw, target_game=game)
    custom_header = CMDLHeader.parse(encoded, target_game=game)

    assert custom_header == raw_header
    assert [int.from_bytes(c, "big") for c in chunks(encoded, 4)] == [int.from_bytes(c, "big") for c in chunks(raw, 4)]


def test_dependencies_p2(prime2_asset_manager):
    result = list(prime2_asset_manager.get_dependencies_for_asset(0x6FE2E8A0))
    assert result == [
        Dependency(type="TXTR", id=326302585),
        Dependency(type="TXTR", id=1583844215),
        Dependency(type="TXTR", id=2998183659),
        Dependency(type="TXTR", id=3392247412),
        Dependency(type="TXTR", id=3714447378),
        Dependency(type="CMDL", id=1877141664),
    ]
