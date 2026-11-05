from __future__ import annotations

import typing

import pytest
from tests import test_lib

from retro_data_structures.formats.scan import Scan
from retro_data_structures.properties.echoes.objects import ScannableObjectInfo


def test_compare_p1(prime1_asset_manager):
    # Resources/Uncategorized/Chozo Lore 002.SCAN
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        0x60AA2A56,
        Scan,
    )


def test_compare_p2(prime2_asset_manager):
    # Resources/Uncategorized/Brizgee_0.SCAN
    _, obj, _ = test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0x62572238,
        Scan,
    )
    scan = typing.cast("Scan", obj)
    prop = scan.scannable_object_info.get_properties_as(ScannableObjectInfo)
    strg = prime2_asset_manager.get_parsed_asset(prop.string)
    assert strg.strings == (
        "Morphology: Brizgee\nVenomous insectoid.",
        "Poisoned stinger concealed in back-mounted shell. Finish it off quickly once the stinger is exposed.",
        (
            "The Brizgee's tail ends in a venomous barb, which it conceals underneath a "
            "hard-packed layer of fused sand. A series of sharpened ridges along its body "
            "discourages most predators; those foolish enough to harass the Brizgee are "
            "quickly introduced to its deadly sting."
        ),
    )


@pytest.mark.xfail
def test_compare_p3(prime3_asset_manager):
    # Resources/uncategorized/Your PED Suit will allow you to absorb this Phazon.SCAN
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x5258014E053BFD2C,
        Scan,
    )


def test_prime_dependency_order(prime1_asset_manager):
    # Prime's SCANs list the string, then the images, then the frame
    asset_manager = prime1_asset_manager
    scan_ids = [
        asset_id for asset_id in asset_manager.all_asset_ids() if asset_manager.get_asset_type(asset_id) == "SCAN"
    ]
    assert scan_ids

    for scan_id in scan_ids:
        scan = asset_manager.get_parsed_asset(scan_id, type_hint=Scan)
        ids = [dep.id for dep in scan.dependencies_for()]
        expected = [
            asset_id
            for asset_id in (scan.raw.text_id, *(image.texture for image in scan.raw.scan_images), scan.raw.frame_id)
            if asset_manager.target_game.is_valid_asset_id(asset_id) and asset_manager.does_asset_exists(asset_id)
        ]
        positions = [ids.index(asset_id) for asset_id in expected]
        assert positions == sorted(positions), hex(scan_id)
