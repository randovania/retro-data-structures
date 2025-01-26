from __future__ import annotations

from typing import TYPE_CHECKING

from tests import test_lib

from retro_data_structures.formats import RuleSet
from retro_data_structures.formats.rule import ComparisonOperator

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetId


def test_compare_p2(prime2_asset_manager: AssetManager, rule_asset_id: AssetId) -> None:
    resource = prime2_asset_manager.get_raw_asset(rule_asset_id)
    decoded = RuleSet.parse(resource.data, target_game=prime2_asset_manager.target_game)
    encoded = decoded.build()

    decoded2 = RuleSet.parse(encoded, target_game=prime2_asset_manager.target_game)

    assert test_lib.purge_hidden(decoded2.raw) == test_lib.purge_hidden(decoded.raw)


def test_build_matches_p2(prime2_asset_manager: AssetManager, rule_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(prime2_asset_manager, rule_asset_id, RuleSet)


def test_pickup_rules(prime2_asset_manager: AssetManager) -> None:
    # The pickup generator rules most retail areas use: below 20% health, 75% chance of a mega health
    rules = prime2_asset_manager.get_file(0x1BB549FB, type_hint=RuleSet).raw.rules
    first = rules[0]
    assert [(c.id, c.operator, c.value) for c in first.conditions] == [("PHLT", ComparisonOperator.LessThan, 20.0)]
    assert [(a.id, list(a.properties)) for a in first.actions] == [("GGHL", [0x42960000, 1, 1])]
