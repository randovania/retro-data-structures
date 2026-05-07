from __future__ import annotations

from tests import test_lib

from retro_data_structures.formats.hier import Hier, HierEntry


def test_compare_p2(prime2_asset_manager):
    # Resources/NoARAM/DUMB_ScanHierarchy.DUMB

    _, parsed, _ = test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0xDD79DC2A,
        Hier,
    )

    parsed2 = prime2_asset_manager.get_parsed_asset(0xDD79DC2A, type_hint=Hier)
    assert parsed == parsed2

    assert parsed2.entries[0] == HierEntry(
        string_table_id=0x3F341ABD, name="Sandbats", scan_id=0x609C0C44, parent_id=178
    )
    assert parsed2.entries[178] == HierEntry(
        string_table_id=0x3F341ABD, name="Small Flyers", scan_id=0xFFFFFFFF, parent_id=184
    )
    assert parsed2.entries[184] == HierEntry(
        string_table_id=0x3F341ABD, name="Flying", scan_id=0xFFFFFFFF, parent_id=230
    )
    assert parsed2.entries[230] == HierEntry(
        string_table_id=0x3F341ABD, name="Light World", scan_id=0xFFFFFFFF, parent_id=234
    )
