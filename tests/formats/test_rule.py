from __future__ import annotations

from typing import TYPE_CHECKING

from tests import test_lib

from retro_data_structures.formats import RuleSet
from retro_data_structures.formats.rule import ActionId, ComparisonOperator, ValueType
from retro_data_structures.game_check import Game

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
    assert [(a.id, list(a.properties)) for a in first.actions] == [(ActionId.HEALTH_100, [75.0, 1, 1])]
    assert first.actions[0].id == "GGHL"


def test_all_actions_known(prime2_asset_manager: AssetManager) -> None:
    for asset_id in prime2_asset_manager.all_asset_ids():
        if prime2_asset_manager.get_asset_type(asset_id) == "RULE":
            for rule in prime2_asset_manager.get_file(asset_id, type_hint=RuleSet).rules:
                assert all(isinstance(action.id, ActionId) for action in rule.actions)


def test_edit_api() -> None:
    game = Game.ECHOES
    rule_set = RuleSet.create(game)
    assert rule_set.parent_rule is None

    rule = rule_set.add_rule()
    rule.add_condition("PHLT", ComparisonOperator.LessThan, 20.0)
    rule.add_condition("ALIV", ComparisonOperator.LessThan, True)
    rule.add_action(ActionId.HEALTH_100, 75.0, 1, 1)
    rule.add_action(ActionId.FREEZE, 2.5)
    rule_set.add_rule(0).add_action(ActionId.NONE)
    rule_set.parent_rule = 0x1BB549FB

    rule_set.rules[1].actions[0].properties[0] = 50.0

    decoded = RuleSet.parse(rule_set.build(), game)
    assert decoded.parent_rule == 0x1BB549FB
    assert len(decoded.rules) == 2
    assert decoded.rules[0].actions[0].id == ActionId.NONE
    conditions = decoded.rules[1].conditions
    assert [(c.id, c.value) for c in conditions] == [("PHLT", 20.0), ("ALIV", True)]
    assert conditions[0].value_type == ValueType.Float
    assert [(a.id, list(a.properties)) for a in decoded.rules[1].actions] == [
        (ActionId.HEALTH_100, [50.0, 1, 1]),
        (ActionId.FREEZE, [2.5]),
    ]

    del decoded.rules[0]
    assert len(RuleSet.parse(decoded.build(), game).rules) == 1
