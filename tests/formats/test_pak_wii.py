from __future__ import annotations

# The two following imports are only used by file tests
from pathlib import Path

from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.pak_wii import PAK_WII, PAKNoData
from retro_data_structures.game_check import Game

# ruff: noqa: E501

# The following variables are used for file and debug tests and should be set before executing said tests locally
pak_target = Path("C:/Users/belok/Emu/PAKTool/testpak.pak")
pak_build_dir = Path("C:/Users/belok/Emu/PAKTool/Compressed-resources")
resource_target = Path("C:/Users/belok/Emu/PAKTool/Compressed-resources/63344da1b78a8eb9.TXTR")
prime3_iso_pak_target = "Metroid3.pak"
csv_target = Path("C:/Users/belok/Emu/PAKTool/decompression_analysis.csv")

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
#     """
#     This test writes an arbitrary pak file
#     This is mostly to test whether written pak files work with Aruki's PakTool
#     """
#     game = Game.CORRUPTION
#     files = [PakFile(0xDEADBEEF, "STRG", False, b"abcdefg", None), PakFile(0xDEADD00D, "STRG", False, b"hijklmn", None)]
#     body = PakBody(
#         b"joe mama so fat ", [("Hey its me Jack Block from minecraft", Dependency("STRG", 0xDEADBEEF))], files
#     )

#     output_pak = Pak(body, game)
#     encoded = output_pak.build()

#     with pak_target.open("wb") as fd:
#         fd.write(encoded)


# def test_build_from_extracted_pak():
#     """
#     This test builds a pak from a specified folder filled with different resources
#     Its purpose is to rebuild a pak that was extracted via PakTool, see if it can be repackaged,
#     and if the game can still run with the rebuilt pak
#     """
#     game = Game.CORRUPTION

#     files = []
#     for file in pak_build_dir.glob("*"):
#         asset_id, asset_type = file.name.split(".")
#         asset_id = int(asset_id.name, 16)

#         data = b""
#         with file.open("rb") as fd:
#             data = fd.read()

#         files.append(PakFile(asset_id, asset_type, False, data, None))

#     # Values specific to Metroid3.pak
#     body = PakBody(
#         b"\x1b\x62\xf7\xca\x15\x60\xb1\x85\xc1\xe1\x09\x43\x99\x4f\xb9\xac",
#         [
#             ("03b_Bryyo_Fire_#SERIAL#", Dependency("MLVL", 0x9BA9292D588D6EB8)),
#             ("03b_Bryyo_Reptilicus_#SERIAL#", Dependency("MLVL", 0x9F059B53561A9695)),
#             ("03b_Bryyo_Ice_#SERIAL#", Dependency("MLVL", 0xB0D67636D61F3868)),
#         ],
#         files,
#     )

#     output_pak = Pak(body, game)
#     encoded = output_pak.build()

#     with pak_target.open("wb") as fd:
#         fd.write(encoded)


# def test_parse_new_pak():
#     """
#     This tests whether a pak file that was built with RDS can be parsed back
#     """
#     game = Game.CORRUPTION

#     with pak_target.open("rb") as fd:
#         raw = fd.read()

#     decoded = Pak.parse(raw, game)
#     return decoded


# def test_resource_extraction(prime3_iso_provider):
#     """
#     This test is here to check whether a specific compressed resource is extracted properly by comparing it
#     to a decompressed resource extracted by PakTool
#     """
#     game = Game.CORRUPTION

#     with prime3_iso_provider.open_binary(prime3_iso_pak_target) as f:
#         raw = f.read()

#     decoded = Pak.parse(raw, game)

#     with resource_target.open("rb") as fd:
#         original_data = fd.read()

#     filename = resource_target.name
#     original_id, original_type = filename.split(".")
#     original_id = int(original_id, 16)

#     # Search for target resource in pak
#     for resource in decoded._raw.files:
#         if resource.asset_id == original_id:
#             pak_resource = resource
#             break

#     assert original_data == pak_resource.get_decompressed(game)

# # The following functions are debug functions : they serve no purpose as tests and are only here
# # to search for specific resources or look for patterns

# def write_resources(target_dir : Path, resource_list : list[PakFile], decompressed : bool = True):
#     for resource in resource_list :
#         file_name = hex(resource.asset_id)[2:]
#         file_extension = resource.asset_type

#         output_file = target_dir / Path(file_name + "." + file_extension)
#         with output_file.open("wb") as fd :
#             fd.write(resource.uncompressed_data if decompressed else resource.compressed_data)

# def test_get_all_compressed(prime3_iso_provider):
#     game = Game.CORRUPTION

#     with prime3_iso_provider.open_binary(prime3_iso_pak_target) as f:
#         raw = f.read()

#     decoded = Pak.parse(raw, game)

#     res = [cmpd_res for cmpd_res in decoded._raw.files if cmpd(cmpd_res)]
#     write_resources(pak_build_dir, res, False)

# def analyze_decompression(decoded_pak : Pak) -> dict[any : Exception | None] :
#     """
#     Analyzes the decompression process for all compressed resources within a given Pak file.
#     Useful for running statistics of how decompression may fail depending on which factors.
#     The tuple indices are as follows :
#     0 : resource id
#     1 : resource type
#     2 : Number of compressed blocks
#     """
#     game = Game.CORRUPTION
#     assert decoded_pak.target_game == game

#     res = {}
#     for cmpd_res in decoded_pak._raw.files :
#         if cmpd_res.should_compress :
#             exception = None
#             id_str = hex(cmpd_res.asset_id)[2:]
#             try :
#                 cmpd_res.get_decompressed(game)
#             except Exception as e:
#                 exception = e
#             finally :
#                 res[(id_str, cmpd_res.asset_type, int.from_bytes(cmpd_res.compressed_data[4:8]))] = exception

#     return res

# def analyze_pak(prime3_iso_provider, pakfile):
#     game = Game.CORRUPTION

#     with prime3_iso_provider.open_binary(pakfile) as f:
#         raw = f.read()

#     decoded = Pak.parse(raw, game)

#     res = analyze_decompression(decoded)
#     return res

# def test_analyze_game_exceptions(prime3_iso_provider):
#     """
#     Runs statistics on decompressing all resources in the game and logs them into a CSV
#     Right now, it analyzes the outcome of decompression, which error is raised
#     """
#     game = Game.CORRUPTION
#     res = {}

#     # Counting errors and sorting them by error type
#     for pakfile in paks:
#         pak_analysis = analyze_pak(prime3_iso_provider, pakfile + ".pak")
#         for exception in pak_analysis.values():
#             if type(exception) not in res.keys():
#                 res[type(exception)] = 1
#             else :
#                 res[type(exception)] += 1

#     # Logging results into csv
#     with csv_target.open("w") as fd_out:
#         index = 0
#         columns = list(res.items())
#         for field in columns:
#             fd_out.write(str(field[0]) + ("," if index < len(columns) - 1 else "\n"))
#             index += 1
#         index = 0
#         for value in columns:
#             fd_out.write(str(value[1]) + ("," if index < len(columns) - 1 else "\n"))
#             index += 1


# # The following functions only denote specific filters for PakFiles to target them specifically

# def cmpd(resource : PakFile) -> bool:
#     return resource.should_compress

# def cmpd_gt_1_block(resource : PakFile) -> bool:
#     return resource.should_compress and (resource.compressed_data[4:8] > b"\x00\x00\x00\x01")

# def cmpd_gt_2_block(resource : PakFile) -> bool:
#     return resource.should_compress and (resource.compressed_data[4:8] > b"\x00\x00\x00\x02")
