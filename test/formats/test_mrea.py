from pathlib import Path

import pytest

from retro_data_structures.base_resource import AssetId
from retro_data_structures.formats import Mlvl
from retro_data_structures.formats.mrea import MREA, Mrea
from retro_data_structures.game_check import Game
from test import test_lib

_mrea_path_p1 = "Resources/Worlds/EndCinema/!EndCinema_Master/01_endcinema.MREA"
_mrea_path_p2 = "Resources/Worlds/SandWorld/!SandWorld_Master/00_pickup_sand_d_dark.MREA"


@pytest.fixture(name="p1_mrea_path")
def _p1_mrea_path(prime1_pwe_project) -> Path:
    return prime1_pwe_project.joinpath(_mrea_path_p1)


@pytest.fixture(name="p2_mrea_path")
def _p2_mrea_path(prime2_pwe_project) -> Path:
    return prime2_pwe_project.joinpath(_mrea_path_p2)


def test_compare_p1(p1_mrea_path):
    # Known difference: some Prime 1 script layers have sizes that
    # are not multiples of 32; building always pads to 32
    test_lib.parse_and_build_compare(MREA, Game.PRIME, p1_mrea_path)


def test_compare_p1_parsed(p1_mrea_path):
    test_lib.parse_and_build_compare_parsed(MREA, Game.PRIME, p1_mrea_path)


def test_compare_p2(p2_mrea_path):
    test_lib.parse_and_build_compare_parsed(MREA, Game.ECHOES, p2_mrea_path)


def test_compare_all_p2(prime2_asset_manager, mrea_asset_id: AssetId):
    resource, decoded, encoded = test_lib.parse_and_build_compare_from_manager(
        prime2_asset_manager,
        mrea_asset_id,
        Mrea,
    )
    assert isinstance(decoded, Mrea)


def test_add_instance(prime2_asset_manager):
    from retro_data_structures.properties.echoes.objects.SpecialFunction import SpecialFunction
    from retro_data_structures.enums import echoes

    mlvl = prime2_asset_manager.get_parsed_asset(0x42b935e4, type_hint=Mlvl)
    area = mlvl.get_area(0x5DFA984F)
    area.get_layer("Default").add_instance_with(SpecialFunction(
        function=echoes.Function.Darkworld,
    ))
    assert area.mrea.build() is not None
