from __future__ import annotations

import math

from retro_data_structures.properties.echoes.core import Vector
from retro_data_structures.transform import Transform


def test_transform_rotation():
    rotation = Vector(45.0, 0.0, 180.0)

    bbox_min = Vector(0.0, 0.0, 0.0)
    bbox_max = Vector(1.0, 1.0, 1.0)

    xfm = Transform.rotation(rotation.x, rotation.y, rotation.z)

    # compare to the known good implementation of BaseVector.rotate()
    rot1 = (bbox_min.rotate(rotation).truncated(), bbox_max.rotate(rotation).truncated())
    rot2 = ((xfm @ bbox_min), (xfm @ bbox_max))

    for corner1, corner2 in zip(rot1, rot2, strict=True):
        for c1, c2 in zip(corner1, corner2, strict=True):
            assert math.isclose(c1, c2, abs_tol=1e-15)


def test_transform_from_vectors():
    xfm = Transform.from_vectors(
        position=Vector(1.0, 2.0, 3.0),
        rotation=Vector(),
        scale=Vector(10.0, 5.0, 1.0),
    )

    bbox_min = Vector(0.0, 0.0, 0.0)
    bbox_max = Vector(1.0, 1.0, 1.0)

    transformed = (xfm @ bbox_min, xfm @ bbox_max)

    assert transformed == (
        Vector(1.0, 2.0, 3.0),
        Vector(11.0, 7.0, 4.0),
    )


def test_transform_division():
    xfm = Transform.identity()

    other = Transform.from_vectors(
        position=Vector(1.0, 2.0, 3.0),
        rotation=Vector(),
        scale=Vector(10.0, 5.0, 1.0),
    )

    xfm @= other
    assert xfm == other

    xfm /= other
    assert xfm == Transform.identity()


def test_transform_flatten():
    xfm = Transform.identity()

    assert xfm == Transform.unflatten(xfm.flatten())
