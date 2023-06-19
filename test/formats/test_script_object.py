import pytest

import retro_data_structures.enums.echoes as _echoes_enums
import retro_data_structures.enums.prime as _prime_enums
from retro_data_structures.formats import script_object
from retro_data_structures.formats.script_object import InstanceId


@pytest.mark.parametrize(["layer", "area", "instance", "expected"], [
    (0, 0, 0, 0x00000000),
    (1, 0, 0, 0x04000000),
    (0, 1, 0, 0x00010000),
    (0, 0, 1, 0x00000001),
    (5, 2, 1, 0x14020001),
])
def test_instance_id_new(layer, area, instance, expected):
    assert InstanceId.new(layer, area, instance) == expected


@pytest.mark.parametrize(["correct_type", "value", "expected"], [
    (_prime_enums.State, _prime_enums.State.Exited, _prime_enums.State.Exited),
    (_prime_enums.State, _echoes_enums.State.Exited, _prime_enums.State.Exited),
    (_echoes_enums.State, _prime_enums.State.Exited, _echoes_enums.State.Exited),
    (_echoes_enums.State, 'EXIT', _echoes_enums.State.Exited),
    (_echoes_enums.State, _echoes_enums.State.Exited, _echoes_enums.State.Exited),
])
def test_resolve_to_enum(correct_type, value, expected):
    assert script_object._resolve_to_enum(correct_type, value) == expected
