from __future__ import annotations

from unittest.mock import ANY

from retro_data_structures.properties.echoes.archetypes import EditorProperties
from retro_data_structures.properties.echoes.objects import ScanTreeCategory
from tests import test_lib

from retro_data_structures.formats.tree import Tree


def test_compare_p2(prime2_asset_manager):
    # Resources/Logbook/DUMB_ScanTree.DUMB
    _, parsed, _ = test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0x95B61279,
        Tree,
    )

    parsed2 = prime2_asset_manager.get_parsed_asset(0x95B61279, type_hint=Tree)
    assert parsed.raw == parsed2.raw

    for i, instance in enumerate(parsed2.nodes):
        assert i == instance.id

    assert parsed2.get_node_by_id(320).get_properties() == ScanTreeCategory(
        editor_properties=EditorProperties(name="Visors", transform=ANY, active=True, unknown=3),
        name_string_table=0x892CB671,
        name_string_name="Visors",
    )
