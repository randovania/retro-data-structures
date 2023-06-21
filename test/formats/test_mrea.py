from test import test_lib

import pytest

from retro_data_structures.base_resource import AssetId
from retro_data_structures.formats import Mlvl
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.script_object import ScriptInstance


@pytest.mark.xfail
def test_compare_p1(prime1_asset_manager):
    # Known difference: some Prime 1 script layers have sizes that
    # are not multiples of 32; building always pads to 32

    # Resources/Worlds/EndCinema/!EndCinema_Master/01_endcinema.MREA
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        0xB4B41C48,
        Mrea
    )


def test_compare_p2(prime2_asset_manager, mrea_asset_id: AssetId):
    resource = prime2_asset_manager.get_raw_asset(mrea_asset_id)

    decoded = Mrea.parse(resource.data, target_game=prime2_asset_manager.target_game)
    for inst in decoded._all_non_scgn_instances():
        assert isinstance(inst, ScriptInstance)

    encoded = decoded.build()

    decoded2 = Mrea.parse(encoded, target_game=prime2_asset_manager.target_game)
    for inst in decoded2._all_non_scgn_instances():
        assert isinstance(inst, ScriptInstance)

    assert test_lib.purge_hidden(decoded2.raw) == test_lib.purge_hidden(decoded.raw)


def test_add_instance(prime2_asset_manager):
    from retro_data_structures.enums import echoes
    from retro_data_structures.properties.echoes.objects.SpecialFunction import SpecialFunction

    mlvl = prime2_asset_manager.get_parsed_asset(0x42b935e4, type_hint=Mlvl)
    area = mlvl.get_area(0x5DFA984F)
    area.get_layer("Default").add_instance_with(SpecialFunction(
        function=echoes.Function.Darkworld,
    ))
    assert area.mrea.build() is not None
