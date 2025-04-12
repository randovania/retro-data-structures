from __future__ import annotations

from retro_data_structures.properties.base_spline import BaseSpline


def test_base_spline_json_roundtrip():
    json_data: dict = {
        "pre_infinity": 0,
        "post_infinity": 0,
        "knots": [
            {
                "time": 0.0,
                "amplitude": 0.0,
                "unk_a": 0,
                "unk_b": 0,
                "cached_tangents_a": [0.0, 0.0],
                "cached_tangents_b": None,
            }
        ],
        "clamp_mode": 0,
        "minimum_amplitude": 0.0,
        "maximum_amplitude": 0.0,
    }
    spline = BaseSpline.from_json(json_data)

    assert spline.to_json() == json_data
