from __future__ import annotations

import struct
from enum import IntEnum

import pytest

from retro_data_structures.adapters.enum_adapter import EnumAdapter


def test_enum_adapter():
    # setup
    class SomeEnum(IntEnum):
        foo = 0
        bar = 1

    valid_in_value = struct.pack(">L", SomeEnum.foo)
    invalid_in_value = struct.pack(">L", 3)

    # test strict adapter, invalid data
    strict = EnumAdapter(SomeEnum, strict=True)
    with pytest.raises(ValueError, match="Invalid value for SomeEnum: 3"):
        parse_result = strict.parse(invalid_in_value)
    with pytest.raises(ValueError, match="Invalid value for SomeEnum: 3"):
        build_result = strict.build(3)

    # test non-strict adapter, invalid data
    non_strict = EnumAdapter(SomeEnum, strict=False)
    parse_result = non_strict.parse(invalid_in_value)
    assert parse_result == 3
    build_result = non_strict.build(3)
    assert build_result == invalid_in_value

    # test both with valid data
    for adapter in (strict, non_strict):
        parse_result = adapter.parse(valid_in_value)
        assert parse_result is SomeEnum.foo
        build_result = adapter.build(SomeEnum.foo)
        assert build_result == valid_in_value
