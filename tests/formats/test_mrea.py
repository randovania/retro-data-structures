from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.script_object import ScriptInstance
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


def _all_instances(mrea: Mrea):
    for layer in mrea.script_layers:
        yield from layer.instances

    if mrea.target_game >= Game.ECHOES:
        yield from mrea.generated_objects_layer.instances


def test_parse_all_p1(prime1_asset_manager, mrea_asset_id: AssetId):
    resource = prime1_asset_manager.get_raw_asset(mrea_asset_id)
    decoded = Mrea.parse(resource.data, target_game=prime1_asset_manager.target_game)
    assert decoded is not None

    for instance in _all_instances(decoded):
        assert isinstance(instance, ScriptInstance)


def test_compare_p1(prime1_asset_manager):
    # Known difference: some Prime 1 script layers have sizes that
    # are not multiples of 32; building always pads to 32

    with pytest.raises(NotImplementedError):
        # Resources/Worlds/EndCinema/!EndCinema_Master/01_endcinema.MREA
        test_lib.parse_and_build_compare(prime1_asset_manager, 0xB4B41C48, Mrea)


def test_compare_p2(prime2_asset_manager, mrea_asset_id: AssetId):
    resource = prime2_asset_manager.get_raw_asset(mrea_asset_id)

    decoded = Mrea.parse(resource.data, target_game=prime2_asset_manager.target_game)
    for instance in _all_instances(decoded):
        assert isinstance(instance, ScriptInstance)

    encoded = decoded.build()

    decoded2 = Mrea.parse(encoded, target_game=prime2_asset_manager.target_game)

    for instance in _all_instances(decoded2):
        assert isinstance(instance, ScriptInstance)

    assert test_lib.purge_hidden(decoded2.raw) == test_lib.purge_hidden(decoded.raw)


def test_compare_p3(prime3_asset_manager, mrea_asset_id: AssetId):
    def _all_instances(mrea: Mrea):
        for layer in mrea.script_layers:
            yield from layer.instances
        yield from mrea.generated_objects_layer.instances

    resource = prime3_asset_manager.get_raw_asset(mrea_asset_id)

    decoded = Mrea.parse(resource.data, target_game=prime3_asset_manager.target_game)
    for instance in _all_instances(decoded):
        assert isinstance(instance, ScriptInstance)

    encoded = decoded.build()

    decoded2 = Mrea.parse(encoded, target_game=prime3_asset_manager.target_game)
    for instance in _all_instances(decoded2):
        assert isinstance(instance, ScriptInstance)

    assert test_lib.purge_hidden(decoded2.raw) == test_lib.purge_hidden(decoded.raw)
