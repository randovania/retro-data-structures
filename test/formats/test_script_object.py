import pytest

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
