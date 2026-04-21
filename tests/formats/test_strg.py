from __future__ import annotations

from typing import TYPE_CHECKING

from tests import test_lib

from retro_data_structures.formats.strg import Strg

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetId


def test_compare_p1(prime1_asset_manager, strg_asset_id: AssetId):
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        strg_asset_id,
        Strg,
    )


# These string tables have a duplicated entry in the name table
_MALFORMED_NAME_TABLE = {
    0x3F341ABD,
    0xA5C74B8B,
}


def test_compare_p2(prime2_asset_manager: AssetManager, strg_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        strg_asset_id,
        Strg,
        byte_match=strg_asset_id not in _MALFORMED_NAME_TABLE,
    )


def test_get_by_name(prime2_asset_manager: AssetManager) -> None:
    table = prime2_asset_manager.get_parsed_asset(0x88E242D6, type_hint=Strg)

    assert table.get_string_by_name("CorruptedFile") == (
        "The Metroid Prime 2 Echoes save file on the \nMemory Card in Slot A is corrupted\nand must be deleted."
    )
    table.set_single_string_by_name("ChoiceDeleteCorruptedFile", "Delete Incompatible File")
    assert table.get_string_by_name("ChoiceDeleteCorruptedFile") == "Delete Incompatible File"


_APPEND_STRING_ASSET = 0x98E7E268


def test_append_string_with_name(prime2_asset_manager: AssetManager) -> None:
    table = prime2_asset_manager.get_parsed_asset(_APPEND_STRING_ASSET, type_hint=Strg)

    name_table_names = list(table._raw.name_table)
    assert name_table_names == sorted(name_table_names)

    table.append_string("Test String Value", name="AAA_TestEntry")

    assert "Test String Value" in table.get_strings()
    assert table.get_string_by_name("AAA_TestEntry") == "Test String Value"

    reparsed = Strg.parse(table.build(), table.target_game)
    reparsed_names = list(reparsed._raw.name_table)
    assert reparsed_names == sorted(reparsed_names)
    assert reparsed.get_string_by_name("AAA_TestEntry") == "Test String Value"


def test_append_string_without_name(prime2_asset_manager: AssetManager) -> None:
    table = prime2_asset_manager.get_parsed_asset(_APPEND_STRING_ASSET, type_hint=Strg)

    count_before = len(table.get_strings())
    name_table_size_before = len(table._raw.name_table)
    table.append_string("Nameless String")

    assert len(table.get_strings()) == count_before + 1
    assert table.get_strings()[-1] == "Nameless String"
    assert len(table._raw.name_table) == name_table_size_before

    reparsed = Strg.parse(table.build(), table.target_game)
    assert reparsed.get_strings()[-1] == "Nameless String"


def test_append_string_with_dict(prime2_asset_manager: AssetManager) -> None:
    table = prime2_asset_manager.get_parsed_asset(_APPEND_STRING_ASSET, type_hint=Strg)

    languages = table.get_language_list()
    dict_string = {lang: f"String for {lang}" for lang in languages}
    table.append_string(dict_string, name="ZZZ_DictEntry")

    for lang in languages:
        assert table.get_string_by_name("ZZZ_DictEntry", lang) == f"String for {lang}"

    reparsed = Strg.parse(table.build(), table.target_game)
    for lang in languages:
        assert reparsed.get_string_by_name("ZZZ_DictEntry", lang) == f"String for {lang}"
    reparsed_names = list(reparsed._raw.name_table)
    assert reparsed_names == sorted(reparsed_names)


def test_compare_p3(prime3_asset_manager: AssetManager) -> None:
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


def test_change_table_length(prime2_asset_manager: AssetManager) -> None:
    strg = prime2_asset_manager.get_parsed_asset(0x2E681FEF, type_hint=Strg)
    strg.set_string_list([])

    assert strg.build() == (
        b"\x87eC!\x00\x00\x00\x01\x00\x00\x00\x06\x00\x00\x00\x00ENGL\x00\x00\x00\x00"
        b"\x00\x00\x00\x00FREN\x00\x00\x00\x00\x00\x00\x00\x00GERM\x00\x00\x00\x00"
        b"\x00\x00\x00\x00SPAN\x00\x00\x00\x00\x00\x00\x00\x00ITAL\x00\x00\x00\x00"
        b"\x00\x00\x00\x00JAPN\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
    )
