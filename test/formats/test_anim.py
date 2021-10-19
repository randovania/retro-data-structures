from pathlib import Path

from retro_data_structures.construct_extensions.json import convert_to_raw_python
from retro_data_structures.formats.anim import ANIM
from retro_data_structures.game_check import Game


def do_file(path: Path):
    raw = path.read_bytes()
    try:
        data = ANIM.parse(raw, target_game=2)
        encoded = ANIM.build(data, target_game=2)
        return path, raw, encoded, None
    except Exception as e:
        return path, None, None, e


def test_compare(prime2_pwe_project):
    input_path = prime2_pwe_project.joinpath("Resources/Uncategorized/01_gate_open.ANIM")
    game = Game.ECHOES
    raw = input_path.read_bytes()

    data = ANIM.parse(raw, target_game=game)
    encoded = ANIM.build(data, target_game=game)
    data2 = ANIM.parse(encoded, target_game=game)

    assert data2 == data

    assert encoded == raw


def test_missile_launcher(prime1_pwe_project, prime2_pwe_project):
    prime1_path = prime1_pwe_project.joinpath("Resources/Uncategorized/Missile_Launcher_ready.ANIM")
    prime2_path = prime2_pwe_project.joinpath("Resources/Uncategorized/Missile_Launcher_ready.ANIM")

    p1_data = ANIM.parse_file(prime1_path, target_game=Game.PRIME)
    p2_data = ANIM.parse_file(prime2_path, target_game=Game.ECHOES)

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
