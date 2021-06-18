from retro_data_structures.cinf import CINF
from test_lib import parse_and_build_compare


def test_compare_p1(prime1_pwe_project):
    parse_and_build_compare(CINF, 1, prime1_pwe_project.joinpath(
        "Resources/Uncategorized/tickspin.CINF"))


def test_compare_p2(prime2_pwe_project):
    parse_and_build_compare(CINF, 2, prime2_pwe_project.joinpath(
        "Resources/Uncategorized/Swamplands_Luminoth_Hologram.CINF"))
