from __future__ import annotations

import pytest
from tests import test_lib

from retro_data_structures.formats.mapa import AreaVisibility, Mapa, MappableObject, ObjectTypeMP2, ObjectVisibility
from retro_data_structures.game_check import Game
from retro_data_structures.transform import Transform

# Area Map


def test_compare_p2(prime2_asset_manager):
    # Worlds/SwampWorld/!SwampWorld_Master/00_save_swamp_b.MAPA

    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0xE2C3A0E5,
        Mapa,
    )


def test_mapa_api_p2(prime2_asset_manager):
    # Worlds/SwampWorld/!SwampWorld_Master/00_save_swamp_b.MAPA

    mapa = prime2_asset_manager.get_parsed_asset(0xE2C3A0E5, type_hint=Mapa)

    # read initial values
    assert mapa.version == 3
    assert not mapa.is_dark_world
    assert mapa.visibility_mode is AreaVisibility.VisitOrMapStation
    assert mapa.bounding_box_min == (-13.0, -9.883729934692383, 0.0)
    assert mapa.bounding_box_max == (9.8837308883667, 9.883729934692383, 7.2974982261657715)
    assert mapa.map_adjustment == (0.0, 0.0, -200.0)
    assert len(mapa.mappable_objects) == 2

    # set new values
    with pytest.raises(AttributeError, match="property 'version' of 'Mapa' object has no setter"):
        mapa.version = 1
    mapa.is_dark_world = True
    mapa.visibility_mode = AreaVisibility.Always
    mapa.bounding_box_min = (1.0, 2.0, 3.0)
    mapa.bounding_box_max = (3.0, 2.0, 1.0)
    mapa.map_adjustment = (10.0, 20.0, 30.0)
    mapa.mappable_objects = []

    # test new values
    assert mapa.version == 3
    assert mapa.is_dark_world
    assert mapa.visibility_mode is AreaVisibility.Always
    assert mapa.bounding_box_min == (1.0, 2.0, 3.0)
    assert mapa.bounding_box_max == (3.0, 2.0, 1.0)
    assert mapa.map_adjustment == (10.0, 20.0, 30.0)
    assert mapa.mappable_objects == []


def test_add_mappable_object_p2(prime2_asset_manager):
    # Worlds2/Temple/!Temple_World_Hub/cooked/04_temple_unknownenemies.MAPA

    mapa = prime2_asset_manager.get_parsed_asset(0x4A8B769C, type_hint=Mapa)
    mappable_obj = MappableObject[ObjectTypeMP2].create(
        object_type=ObjectTypeMP2.TranslatorGate,
        visibility_mode=ObjectVisibility.AreaVisitOrMapStation,
        editor_id=0x00000000,
        transform=Transform.unflatten([1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]),
    )
    mapa.mappable_objects.append(mappable_obj)

    encoded = mapa.build()

    decoded = Mapa.parse(encoded, Game.ECHOES)

    assert len(decoded.mappable_objects) == 4
    assert decoded.mappable_objects[3] == mappable_obj

    for orig, edited in zip(mapa.raw.primitive_headers, decoded.raw.primitive_headers, strict=True):
        assert orig._raw_primitive_start == edited._raw_primitive_start - 0x50
        assert orig._raw_border_start == edited._raw_border_start - 0x50

        assert orig.primitive_table_start == edited.primitive_table_start
        assert orig.border_table_start == edited.border_table_start
