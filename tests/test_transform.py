from __future__ import annotations

import math

import numpy as np
import pytest

from retro_data_structures.properties.vector import Vector
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

    assert (xfm / 2.0) == Transform(
        np.array(
            [
                [0.5, 0.0, 0.0, 0.0],
                [0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.5, 0.0],
                [0.0, 0.0, 0.0, 0.5],
            ]
        )
    )


def test_transform_flatten():
    xfm = Transform.identity()

    assert xfm == Transform.unflatten(xfm.flatten())


def test_invalid_cases():
    with pytest.raises(ValueError, match="Transform requires a list of exactly 12 floats"):
        xfm = Transform.unflatten([0.0])

    with pytest.raises(ValueError, match="Transform requires three lists of exactly 4 floats each"):
        xfm = Transform.from_rows([0.0], [1.0], [2.0])

    with pytest.raises(ValueError, match="Transform only supports float32"):
        xfm = Transform.identity()
        np.array(xfm, dtype=np.float64)


def test_equality():
    identity = Transform.identity()

    assert (identity == Transform.identity()) is True
    assert np.array_equal(identity == np.asarray(identity), np.array([[True] * 4] * 4))


def test_print():
    xfm = Transform.identity()

    assert repr(xfm) == (
        "array([[1., 0., 0., 0.],\n"
        "       [0., 1., 0., 0.],\n"
        "       [0., 0., 1., 0.],\n"
        "       [0., 0., 0., 1.]], dtype=float32)"
    )
    assert str(xfm) == ("[[1. 0. 0. 0.]\n [0. 1. 0. 0.]\n [0. 0. 1. 0.]\n [0. 0. 0. 1.]]")


# test suite for __array_ufunc__ :
# https://github.com/numpy/numpy/blob/main/numpy/lib/tests/test_mixins.py
