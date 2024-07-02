from __future__ import annotations

import pytest

import typing
from retro_data_structures.base_resource import Dependency
from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.pak_wii import PAK_WII, CompressedPakResource, PakBody, PakFile, PAKNoData, ConstructPakWii
from retro_data_structures.game_check import Game

# ruff: noqa: E501

def test_identical_when_keep_data(prime3_iso_provider):
    game = Game.CORRUPTION
    with prime3_iso_provider.open_binary("MiscData.pak") as f:
        raw = f.read()

    decoded = Pak.parse(raw, target_game=game)
    print("parsing done")
    encoded = decoded.build()

    assert raw == encoded

def test_compare_header_keep_data(prime3_iso_provider):
    game = Game.CORRUPTION
    with prime3_iso_provider.open_binary("MiscData.pak") as f:
        raw = f.read()

    raw_header = PAKNoData.parse(raw, target_game=game)
    raw_sizes = [(r.compressed, r.offset, r.size) for r in raw_header.resources]

    decoded = PAK_WII.parse(raw, target_game=game)
    # for r in decoded.resources:
    #     r.contents.pop("data")

    encoded = PAK_WII.build(decoded, target_game=game)

    custom_header = PAKNoData.parse(encoded, target_game=game)

    custom_sizes = [(r.compressed, r.offset, r.size) for r in custom_header.resources]
    assert custom_sizes == raw_sizes
