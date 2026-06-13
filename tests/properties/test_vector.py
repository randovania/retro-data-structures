from __future__ import annotations

import re

import pytest

from retro_data_structures.properties.vector import Vector


def test_vector_vector_operations():
    a = Vector(2.0, 3.0, 4.0)
    b = Vector(1.25, 1.5, 1.75)

    assert a + b == b + a == Vector(3.25, 4.5, 5.75)
    assert a - b == Vector(0.75, 1.5, 2.25)
    assert a * b == b * a == Vector(2.5, 4.5, 7.0)
    assert a / b == Vector(1.6, 2.0, 4.0 / 1.75)
    assert a // b == Vector(1.0, 2.0, 2.0)


def test_vector_number_operations():
    a = Vector(2.0, 3.0, 4.0)
    b = 1.5

    assert a * b == b * a == Vector(3.0, 4.5, 6.0)
    assert a / b == Vector(4.0 / 3.0, 2.0, 8.0 / 3.0)
    assert a // b == Vector(1.0, 2.0, 2.0)


def test_vector_invalid_operations():
    a = Vector()
    b = None

    def pattern(operator: str) -> str:
        unescaped = f"unsupported operand type(s) for {operator}: 'Vector' and 'NoneType'"
        return re.escape(unescaped)

    with pytest.raises(TypeError, match=pattern("+")):
        a + b  # type: ignore[operator]

    with pytest.raises(TypeError, match=pattern("-")):
        a - b  # type: ignore[operator]

    with pytest.raises(TypeError, match=pattern("*")):
        a * b  # type: ignore[operator]

    with pytest.raises(TypeError, match=pattern("/")):
        a / b  # type: ignore[operator]

    with pytest.raises(TypeError, match=pattern("//")):
        a // b  # type: ignore[operator]


@pytest.mark.parametrize(
    ("center", "expected"),
    (
        (None, Vector(x=-3.535533905029297, y=0.7071067690849304, z=-1.0)),
        (Vector(1.0, -3.0, 2.0), Vector(x=-3.242640733718872, y=-5.828427314758301, z=2.0)),
        (Vector(2.4, 0.3, -24.03), Vector(x=-17.915178298950195, y=18.211015701293945, z=-22.6299991607666)),
    ),
)
def test_rotation(center: Vector | None, expected: Vector):
    pos = Vector(1.0, 2.0, 3.0)
    rot = Vector(45.0, 90.0, 180.0)

    result = pos.rotate(rot, center)
    assert result.truncated() == expected.truncated()
