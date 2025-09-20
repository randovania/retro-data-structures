from __future__ import annotations

from typing import TYPE_CHECKING

from tests import test_lib

from retro_data_structures.formats.strg import Strg

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


def test_compare_p1(prime1_asset_manager, strg_asset_id: AssetId):
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        strg_asset_id,
        Strg,
        byte_match=False,  # FIXME
    )


def test_compare_p2(prime2_asset_manager, strg_asset_id: AssetId):
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        strg_asset_id,
        Strg,
        byte_match=False,  # FIXME
    )


def test_get_by_name(prime2_asset_manager):
    table = prime2_asset_manager.get_parsed_asset(0x88E242D6, type_hint=Strg)

    assert table.get_string_by_name("CorruptedFile") == (
        "The Metroid Prime 2 Echoes save file on the \nMemory Card in Slot A is corrupted\nand must be deleted."
    )
    table.set_single_string_by_name("ChoiceDeleteCorruptedFile", "Delete Incompatible File")
    assert table.get_string_by_name("ChoiceDeleteCorruptedFile") == "Delete Incompatible File"


def test_compare_p3(prime3_asset_manager):
    # with name table
    # Resources/strings/metroid3/gui/fesliderpopup.STRG
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x0D53311DE8B26040,
        Strg,
        byte_match=False,  # FIXME
    )

    # without name table
    # Resources/strings/uncategorized/Action.STRG
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x8A3242A997AAEDE7,
        Strg,
        byte_match=False,  # FIXME
    )

    # echoes format
    # Resources/strings/metroid2/ingame/languageselection.STRG
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x08417493AF6B57E2,
        Strg,
        byte_match=False,  # FIXME
    )


def test_change_table_length(prime2_asset_manager):
    strg = prime2_asset_manager.get_parsed_asset(0x2E681FEF)
    strg.set_string_list([])

    assert strg.build() == (
        b"\x87eC!\x00\x00\x00\x01\x00\x00\x00\x06\x00\x00\x00\x00ENGL\x00\x00\x00\x00"
        b"\x00\x00\x00\x00FREN\x00\x00\x00\x00\x00\x00\x00\x00GERM\x00\x00\x00\x00"
        b"\x00\x00\x00\x00SPAN\x00\x00\x00\x00\x00\x00\x00\x00ITAL\x00\x00\x00\x00"
        b"\x00\x00\x00\x00JAPN\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
    )
