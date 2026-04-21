from __future__ import annotations

from typing import TYPE_CHECKING

from tests import test_lib

from retro_data_structures.formats import Savw

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId

_ECHOES_SAVW = 0x32E95269


def test_compare_p1(prime1_asset_manager, savw_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        savw_asset_id,
        Savw,
    )


def test_compare_p2(prime2_asset_manager, savw_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        savw_asset_id,
        Savw,
    )


def test_compare_p3(prime3_asset_manager, savw_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        savw_asset_id,
        Savw,
    )


def test_add_system_state_env_var(prime2_asset_manager) -> None:
    savw = prime2_asset_manager.get_parsed_asset(_ECHOES_SAVW, type_hint=Savw)

    count_before = len(savw._raw.system_state_env_vars)
    savw.add_system_state_env_var("MySystemVar")

    assert len(savw._raw.system_state_env_vars) == count_before + 1
    entry = savw._raw.system_state_env_vars[-1]
    assert entry.name == "MySystemVar"
    assert entry.unk_a == 0
    assert entry.unk_b == 1
    assert entry.unk_c == 0

    reparsed = Savw.parse(savw.build(), savw.target_game)
    assert len(reparsed._raw.system_state_env_vars) == count_before + 1
    reparsed_entry = reparsed._raw.system_state_env_vars[-1]
    assert reparsed_entry.name == "MySystemVar"
    assert reparsed_entry.unk_a == 0
    assert reparsed_entry.unk_b == 1
    assert reparsed_entry.unk_c == 0
    assert len(reparsed._raw.game_state_env_vars) == len(savw._raw.game_state_env_vars)


def test_add_game_state_env_var(prime2_asset_manager) -> None:
    savw = prime2_asset_manager.get_parsed_asset(_ECHOES_SAVW, type_hint=Savw)

    count_before = len(savw._raw.game_state_env_vars)
    savw.add_game_state_env_var("MyGameVar")

    assert len(savw._raw.game_state_env_vars) == count_before + 1
    entry = savw._raw.game_state_env_vars[-1]
    assert entry.name == "MyGameVar"
    assert entry.unk_a == 0
    assert entry.unk_b == 1
    assert entry.unk_c == 0

    reparsed = Savw.parse(savw.build(), savw.target_game)
    assert len(reparsed._raw.game_state_env_vars) == count_before + 1
    reparsed_entry = reparsed._raw.game_state_env_vars[-1]
    assert reparsed_entry.name == "MyGameVar"
    assert reparsed_entry.unk_a == 0
    assert reparsed_entry.unk_b == 1
    assert reparsed_entry.unk_c == 0
    assert len(reparsed._raw.system_state_env_vars) == len(savw._raw.system_state_env_vars)
