from __future__ import annotations

# The two following imports are only used by file tests
# from glob import glob
# from os import path
from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.pak_wii import (
    PAK_WII,
    PAKNoData,
)

# The two following classes are only used by file tests
# PakFile,
# PakBody
from retro_data_structures.game_check import Game

# ruff: noqa: E501

# The following variables are only used for the file tests and should be set before executing said tests locally
# pak_target = "."
# pak_build_dir = "."

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


# The following tests are what I call file tests :
# They produce or read local files specified by the two global variables pak_target and pak_build_dir
# They are NOT to be executed as tests by CI and are only here for reviewing the testing process

# def test_write_new_pak():
#     game = Game.CORRUPTION
#     files = [
#         PakFile(0xDEADBEEF, "STRG", False, b"abcdefg", None),
#         PakFile(0xDEADD00D, "STRG", False, b"hijklmn", None)
#     ]
#     body = PakBody(b"joe mama so fat ", [
#         ("Hey its me Jack Block from minecraft",
#         Dependency("STRG", 0xDEADBEEF))
#         ],
#         files
#     )

#     output_pak = Pak(body, game)
#     encoded = output_pak.build()

#     with open(pak_target, "wb") as fd :
#         fd.write(encoded)

# def test_build_from_extracted_pak():
#     game = Game.CORRUPTION

#     files = []
#     for file in glob(pak_build_dir + "/*"):
#         asset_id, asset_type = file.split(".")
#         asset_id = int(path.basename(asset_id), 16)

#         data = b""
#         with open(file, "rb") as fd:
#             data = fd.read()

#         files.append(PakFile(asset_id, asset_type, False, data, None))

#     body = PakBody(b"\x1B\x62\xF7\xCA\x15\x60\xB1\x85\xC1\xE1\x09\x43\x99\x4F\xB9\xAC", [
#                     ("03b_Bryyo_Fire_#SERIAL#",
#                     Dependency("MLVL", 0x9BA9292D588D6EB8)),
#                     ("03b_Bryyo_Reptilicus_#SERIAL#",
#                     Dependency("MLVL", 0x9F059B53561A9695)),
#                     ("03b_Bryyo_Ice_#SERIAL#",
#                     Dependency("MLVL", 0xB0D67636D61F3868))
#                     ],
#                 files
#             )

#     output_pak = Pak(body, game)
#     encoded = output_pak.build()

#     with open(pak_target, "wb") as fd:
#         fd.write(encoded)

# def test_parse_new_pak():
#     game = Game.CORRUPTION

#     with open(pak_target, "rb") as fd:
#         raw = fd.read()

#     decoded = Pak.parse(raw, game)
#     return decoded
