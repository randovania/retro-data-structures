from __future__ import annotations

import pytest
from construct.lib import Container

from retro_data_structures.construct_extensions.wrapper_classes import FieldsMixin, field
from retro_data_structures.formats.script_object import InstanceId


class Wrapper(FieldsMixin):
    name = field(str)
    instance_id = field(InstanceId, factory=InstanceId)
    nested_number = field(float, location=("header",))


@pytest.fixture
def test_wrapper() -> Wrapper:
    return Wrapper(
        Container(
            {
                "name": "The Name",
                "instance_id": 0,
                "header": Container(
                    {
                        "nested_number": 0.0,
                    }
                ),
            }
        )
    )


def test_str(test_wrapper):
    assert str(test_wrapper) == ("Wrapper:\n    name = The Name\n    instance_id = 0x00000000\n    nested_number = 0.0")


def test_repr(test_wrapper):
    assert repr(test_wrapper) == ("<Wrapper name=The Name instance_id=0x00000000 nested_number=0.0>")


def test_equality(test_wrapper):
    other = Wrapper(Container(test_wrapper._raw))

    assert test_wrapper == other

    other.name = "The Other"
    assert test_wrapper != other

    assert test_wrapper != "foo"


def test_field_access(test_wrapper):
    assert test_wrapper.name == "The Name"

    regex = r"Cannot access field 'name' on class Wrapper \(must be accessed on an instance\)"
    with pytest.raises(AttributeError, match=regex):
        Wrapper.name


def test_field_repr():
    reprs = {name: repr(field) for name, field in Wrapper._fields}

    assert reprs == {
        "instance_id": (
            "<Field location='()' factory='<class 'retro_data_structures.formats.script_object.InstanceId'>'>"
        ),
        "name": "<Field location='()' factory='None'>",
        "nested_number": "<Field location='('header',)' factory='None'>",
    }
