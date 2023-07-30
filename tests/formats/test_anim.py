from __future__ import annotations

from tests import test_lib

from retro_data_structures.base_resource import Dependency
from retro_data_structures.construct_extensions.json import convert_to_raw_python
from retro_data_structures.formats.anim import Anim


def test_compare_p2(prime2_asset_manager):
    # Resources/Uncategorized/01_gate_open.ANIM
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0x101367C6,
        Anim,
    )


def test_missile_launcher(prime1_asset_manager, prime2_asset_manager):
    # Resources/Uncategorized/Missile_Launcher_ready.ANIM
    p1_data = prime1_asset_manager.get_parsed_asset(0x5E2F550E, type_hint=Anim).raw
    p2_data = prime2_asset_manager.get_parsed_asset(0x5E2F550E, type_hint=Anim).raw

    p1_aux = convert_to_raw_python(p1_data)
    p2_aux = convert_to_raw_python(p2_data)

    # This mapping needs thinking
    bone_id_mapping = {
        4: 1,
        6: 2,
        3: 0,
    }

    old = p1_aux["anim"]["bone_channel_descriptors"]
    p1_aux["anim"]["bone_channel_descriptors"] = [None] * len(old)
    index_conversion = {}
    for i, it in enumerate(old):
        new_bone_id = bone_id_mapping[it["bone_id"]]
        it["bone_id"] = new_bone_id
        it["scale_keys_count"] = 0
        p1_aux["anim"]["bone_channel_descriptors"][new_bone_id] = it
        index_conversion[new_bone_id] = i

    p1_aux["anim"]["scale_multiplier"] = 0.0
    p1_aux["anim"]["event_id"] = None
    p1_aux["anim"]["root_bone_id"] = bone_id_mapping[p1_aux["anim"]["root_bone_id"]]
    p1_aux["anim"]["unk_1"] = None

    for key in p1_aux["anim"]["animation_keys"]:
        if key["channels"] is not None:
            key["channels"] = [key["channels"][index_conversion[i]] for i, _ in enumerate(key["channels"])]

    # These changes need more thinking
    p1_aux["anim"]["unk_2"] = 257
    p1_aux["anim"]["scratch_size"] = 405

    assert p1_aux == p2_aux


def test_no_dependencies(prime2_asset_manager):
    result = list(prime2_asset_manager.get_dependencies_for_asset(0x5E2F550E))
    assert result == [Dependency(type="ANIM", id=0x5E2F550E)]
