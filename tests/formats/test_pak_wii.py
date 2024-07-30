from __future__ import annotations

# The two following imports are only used by file tests
import pytest

from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.pak_wii import PAK_WII, CompressedPakResource, PAKNoData
from retro_data_structures.game_check import Game

# ruff: noqa: E501

paks = {
    "FrontEnd",
    "GuiDVD",
    "GuiNAND",
    "InGameAudio",
    "InGameDVD",
    "InGameNAND",
    "Logbook",
    "Metroid1",
    "Metroid3",
    "Metroid4",
    "Metroid5",
    "Metroid6",
    "Metroid7",
    "Metroid8",
    "MiscData",
    "NoARAM",
    "SamGunFx",
    "SamusGun",
    "UniverseArea",
    "Worlds",
}


@pytest.fixture(name="compressed_resources")
def _compressed_resources():
    """
    The resources can be found in Metroid3.pak
    """
    return [
        {  # 2 segments resource
            "compressed": 1,
            "asset": {"type": "TXTR", "id": 4849971089334802081},
            "contents": {
                "data": b"CMPD\x00\x00\x00\x02\x00\x00\x00\x0c\x00\x00\x00\x0c\xc0\x00\x00\x11\x00\x00\x00\xa0"
                b"\x00\x00\x00\n\x00\x10\x00\x10\x00\x00\x00\x02\x00\x0f\x16\x01\xe0\x02\xa0\xaa@\x00 "
                b"w\x1c\x00\x11\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff",
                "value": (
                    b"\x00\x00\x00\n\x00\x10\x00\x10\x00\x00\x00\x02\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02"
                    b"\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01"
                    b"\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa"
                    b"\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa"
                    b"\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02"
                    b"\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01"
                    b"\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa"
                    b"\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa\x01\xe0\x02\xa0\xaa\xaa\xaa\xaa"
                ),
            },
        },
        {  # 1 segment resource
            "compressed": 1,
            "asset": {"type": "CSKR", "id": 2135532429836327754},
            "contents": {
                "data": b"CMPD\x00\x00\x00\x01\xa0\x00\x00*\x00\x00\x00J\x00(\x19SKIN\x00\x00\x00\x02M\x00\x01"
                b"\xcf\x00\x03?\x80W\x00\x00\n\x1as\x00\x00\x00\xff/\x00\x00\xdc\x04+\x02\x00\x01\x00\x11\x00\x00"
                b"\xff\xff\xff\xff\xff\xff",
                "value": (
                    b"SKIN\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x03?\x80\x00\x00\x00\x00\n"
                    b"\x1a\x00\x00\x00\n\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
                    b"\xff\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00"
                ),
            },
        },
    ]


def test_identical_when_keep_data(prime3_iso_provider):
    game = Game.CORRUPTION
    for pakfile in paks:
        with prime3_iso_provider.open_binary(pakfile + ".pak") as f:
            raw = f.read()

        decoded = Pak.parse(raw, target_game=game)
        encoded = decoded.build()

        assert raw == encoded


def test_compare_header_keep_data(prime3_iso_provider):
    game = Game.CORRUPTION
    for pakfile in paks:
        with prime3_iso_provider.open_binary(pakfile + ".pak") as f:
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


def test_corruption_resource_decode(compressed_resources):
    for compressed_resource in compressed_resources:
        decoded = CompressedPakResource.parse(compressed_resource["contents"]["data"], target_game=Game.CORRUPTION)

        assert len(decoded) == len(compressed_resource["contents"]["value"])
        assert decoded == compressed_resource["contents"]["value"]


def test_corruption_resource_encode_decode(compressed_resources):
    for compressed_resource in compressed_resources:
        raw = compressed_resource["contents"]["value"]
        decoded = CompressedPakResource.build(raw, target_game=Game.CORRUPTION)
        encoded = CompressedPakResource.parse(decoded, target_game=Game.CORRUPTION)
        assert raw == encoded
