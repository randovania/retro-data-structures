from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.formats import mrea
from retro_data_structures.formats.mlvl import Mlvl
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.script_object import ScriptInstance
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator

    import construct

    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetId


def check_all_instances(
    encoded: bytes,
    target_game: Game,
    all_instances: Callable[[Mrea], Iterator[ScriptInstance]],
):
    decoded = Mrea.parse(encoded, target_game=target_game)
    for instance in all_instances(decoded):
        assert isinstance(instance, ScriptInstance)

    return decoded


def compare_all_instances(
    asset_manager: AssetManager,
    mrea_asset_id: AssetId,
    all_instances: Callable[[Mrea], Iterator[ScriptInstance]],
    simple_construct: construct.Construct | None,
) -> None:
    """
    :param asset_manager:
    :param mrea_asset_id: The mrea to compare.
    :param all_instances: A callable for providing instances. See check_all_instances
    :param simple_construct: When set, it's used to parse both the original resource and the re-built one,
                             with the results compared. Used for byte-matching.
    :return:
    """
    resource = asset_manager.get_raw_asset(mrea_asset_id)
    decoded = check_all_instances(resource.data, asset_manager.target_game, all_instances)

    encoded = decoded.build()
    decoded2 = check_all_instances(encoded, asset_manager.target_game, all_instances)

    if simple_construct is not None:
        assert test_lib.purge_hidden(simple_construct.parse(resource.data)) == test_lib.purge_hidden(
            simple_construct.parse(encoded)
        )
    else:
        assert test_lib.purge_hidden(decoded2.raw) == test_lib.purge_hidden(decoded.raw)


def _all_instances_p1_p2(mrea: Mrea):
    for layer in mrea.script_layers:
        yield from layer.instances

    if mrea.target_game >= Game.ECHOES:
        yield from mrea.generated_objects_layer.instances


def test_parse_all_p1(prime1_asset_manager, mrea_asset_id: AssetId):
    resource = prime1_asset_manager.get_raw_asset(mrea_asset_id)
    check_all_instances(resource.data, prime1_asset_manager.target_game, _all_instances_p1_p2)


def test_compare_p1(prime1_asset_manager, mrea_asset_id: AssetId):
    # Known difference: some Prime 1 script layers have sizes that
    # are not multiples of 32; building always pads to 32
    # FIXME: re-encoding script layer will cause mismatches. Maybe because of ^?
    compare_all_instances(prime1_asset_manager, mrea_asset_id, lambda obj: iter([]), mrea.MREASimple)


def test_compare_p2(prime2_asset_manager, mrea_asset_id: AssetId):
    compare_all_instances(prime2_asset_manager, mrea_asset_id, _all_instances_p1_p2, mrea.MREASimple)


def test_compare_p3(prime3_asset_manager, mrea_asset_id: AssetId):
    compare_all_instances(prime3_asset_manager, mrea_asset_id, _all_instances_p1_p2, mrea.MREASimple)


def _compare_mrea_hashes(hash_file_name: str, encoded: bytes, asset_id: AssetId):
    hash_file = Path(__file__).parent.parent.joinpath("test_files", hash_file_name)
    with hash_file.open() as f:
        hashes: dict[str, str] = json.load(f)

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


def test_compare_p3_hashes(prime3_asset_manager, mrea_asset_id: AssetId):
    raw, decoded, encoded = test_lib.parse_and_build_compare(
        prime3_asset_manager, mrea_asset_id, Mrea, byte_match=False
    )
    _compare_mrea_hashes("mrea_hashes_corruption.json", encoded, mrea_asset_id)


def test_compare_p2_add_layer_hashes(prime2_asset_manager, mrea_asset_id: AssetId):
    mlvl = prime2_asset_manager.get_parsed_asset(prime2_asset_manager.find_mlvl_for_mrea(mrea_asset_id), type_hint=Mlvl)

    area = mlvl.get_area(mrea_asset_id)
    test_layer = area.add_layer("Test Layer")
    test_layer.add_instance("TRGR")

    mlvl_encoded = mlvl.build()
    mrea_encoded = area.mrea.build()

    _compare_mrea_hashes("mrea_hashes_echoes_add_layer.json", mlvl_encoded + mrea_encoded, mrea_asset_id)
