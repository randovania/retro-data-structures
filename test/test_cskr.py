from retro_data_structures.cskr import CSKR
from test_lib import parse_and_build_compare


def test_compare_p1(prime1_pwe_project):
    parse_and_build_compare(CSKR, 1, prime1_pwe_project.joinpath(
        "Resources/NoARAM/Fusion.CSKR"))


def test_compare_p2(prime2_pwe_project):
    parse_and_build_compare(CSKR, 2, prime2_pwe_project.joinpath(
        "Resources/SamusGunLow/Holo.CSKR"))
