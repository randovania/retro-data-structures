from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.formats.mlvl import Mlvl
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


@pytest.mark.skip(reason="Corruption MREA not implemented correctly")
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


def _compare_mrea_hashes(hash_file_name: str, encoded: bytes, asset_id: AssetId):
    hash_file = Path(__file__).parent.parent.joinpath("test_files", hash_file_name)
    with hash_file.open() as f:
        hashes: dict[AssetId, str] = json.load(f)

    mrea_hash = hashlib.sha256(encoded).digest().hex(" ")
    asset_id_key = f"{asset_id:08X}"

    # # uncomment to update the hashes if they're changing on purpose
    # # never ever do this in xdist btw. it's gotta be serial
    # hashes[asset_id_key] = mrea_hash
    # with hash_file.open("w") as f:
    #     json.dump(hashes, f, indent=2)

    assert mrea_hash == hashes[asset_id_key]


@pytest.mark.skip(reason="Prime 1 MREA building not implemented")
def test_compare_p1_hashes(prime1_asset_manager, mrea_asset_id: AssetId):
    raw, decoded, encoded = test_lib.parse_and_build_compare(
        prime1_asset_manager, mrea_asset_id, Mrea, byte_match=False
    )
    _compare_mrea_hashes("mrea_hashes_prime.json", encoded, mrea_asset_id)


def test_compare_p2_hashes(prime2_asset_manager, mrea_asset_id: AssetId):
    raw, decoded, encoded = test_lib.parse_and_build_compare(
        prime2_asset_manager, mrea_asset_id, Mrea, byte_match=False
    )
    _compare_mrea_hashes("mrea_hashes_echoes.json", encoded, mrea_asset_id)


@pytest.mark.skip(reason="Corruption MREA not implemented correctly")
def test_compare_p3_hashes(prime3_asset_manager, mrea_asset_id: AssetId):
    raw, decoded, encoded = test_lib.parse_and_build_compare(
        prime3_asset_manager, mrea_asset_id, Mrea, byte_match=False
    )
    _compare_mrea_hashes("mrea_hashes_corruption.json", encoded, mrea_asset_id)


def test_compare_p2_add_layer_hashes(prime2_asset_manager, mlvl_asset_id: AssetId, mrea_asset_id: AssetId):
    mlvl = prime2_asset_manager.get_parsed_asset(mlvl_asset_id, type_hint=Mlvl)

    try:
        area = mlvl.get_area(mrea_asset_id)
    except StopIteration:
        return  # area isn't in this level

    test_layer = area.add_layer("Test Layer")
    test_layer.add_instance("TRGR")

    mlvl_encoded = mlvl.build()
    mrea_encoded = area.mrea.build()

    _compare_mrea_hashes("mrea_hashes_echoes_add_layer.json", mlvl_encoded + mrea_encoded, mrea_asset_id)
