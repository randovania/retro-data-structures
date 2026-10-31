from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.formats import Frme, dependency_cheating
from retro_data_structures.formats.pak import Pak
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


@pytest.mark.parametrize(
    "asset_id",
    (
        0x13856B27,
        0x58008329,
        0x96BC9B7D,
        0x977252CF,
        0xB5CF0C19,
        0xBAF48D93,
        0xD9D58FA5,
        0xE0BCA226,
    ),
)
def test_p2_pal(prime2_pal_iso_provider, asset_id) -> None:
    asset_manager = AssetManager(prime2_pal_iso_provider, target_game=Game.ECHOES)
    test_lib.parse_and_build_compare(
        asset_manager,
        asset_id,
        Frme,
    )


def test_compare_p2(prime2_asset_manager, frme_asset_id: AssetId) -> None:
    resource, decoded, _ = test_lib.parse_and_build_compare(
        prime2_asset_manager,
        frme_asset_id,
        Frme,
    )

    decoded_deps = list(decoded.dependencies_for())
    cheated_deps = list(dependency_cheating.get_cheated_dependencies(resource, prime2_asset_manager))
    assert decoded_deps == cheated_deps


@pytest.mark.parametrize(("pak_name", "frame_count"), [("GGuiSys.pak", 12), ("NoARAM.pak", 8)])
def test_prime_dependencies_in_pak_order(prime1_iso_provider, prime1_asset_manager, pak_name: str, frame_count: int):
    # Prime's FRME has no dependency list. The paks have what each frame uses in the order the frame's widgets are
    # walked, after the previous named resource.
    with prime1_iso_provider.open_binary(pak_name) as f:
        header = Pak.header_for_game(Game.PRIME).parse_stream(f, target_game=Game.PRIME)
    order = [resource.asset_id for resource in header.resources]
    named = {resource.asset_id for resource in header.named_resources}
    first: dict[int, int] = {}
    for index, asset_id in enumerate(order):
        first.setdefault(asset_id, index)

    frames = 0
    for index, asset_id in enumerate(order):
        if first[asset_id] != index or prime1_asset_manager.get_asset_type(asset_id) != "FRME":
            continue
        frames += 1

        data = prime1_asset_manager.get_raw_asset(asset_id).data
        used = list(dict.fromkeys(dependency_cheating._prime_frme_dependency_ids(data, prime1_asset_manager)))
        assert all(first[it] < index for it in used)

        start = max((k for k in range(index) if order[k] in named), default=-1)
        in_pak_order = [it for it in order[start + 1 : index] if it in used and first[it] > start]
        assert [it for it in used if first[it] > start] == in_pak_order

    assert frames == frame_count


def test_prime_widgets_ignore_truncated_data():
    assert dependency_cheating._prime_frme_widgets(b"MODLmodel\0parent\0MODLcut") == [(0, "model", "parent")]
