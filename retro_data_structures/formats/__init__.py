from retro_data_structures.formats.ancs import ANCS
from retro_data_structures.formats.anim import ANIM
from retro_data_structures.formats.cinf import CINF
from retro_data_structures.formats.cmdl import CMDL
from retro_data_structures.formats.cskr import CSKR
from retro_data_structures.formats.evnt import EVNT
from retro_data_structures.formats.mlvl import MLVL
from retro_data_structures.formats.mrea import MREA
from retro_data_structures.formats.pak import PAK

ALL_FORMATS = {
    "ancs": ANCS,
    "cmdl": CMDL,
    "mlvl": MLVL,
    "mrea": MREA,
    "pak": PAK,
    "anim": ANIM,
    "cinf": CINF,
    "cskr": CSKR,
    "evnt": EVNT,
}


def format_for(type_name: str):
    return ALL_FORMATS[type_name.lower()]
