from construct import Construct

from retro_data_structures.formats.ancs import ANCS
from retro_data_structures.formats.anim import ANIM
from retro_data_structures.formats.base_resource import BaseResource, AssetType, AssetId
from retro_data_structures.formats.char import CHAR
from retro_data_structures.formats.cinf import CINF
from retro_data_structures.formats.cmdl import CMDL
from retro_data_structures.formats.cskr import CSKR
from retro_data_structures.formats.cspp import CSPP
from retro_data_structures.formats.dgrp import DGRP
from retro_data_structures.formats.evnt import EVNT
from retro_data_structures.formats.mlvl import MLVL
from retro_data_structures.formats.mrea import MREA, Mrea
from retro_data_structures.formats.pak import PAK
from retro_data_structures.formats.part import PART
from retro_data_structures.formats.sand import SAND
from retro_data_structures.formats.scan import SCAN
from retro_data_structures.formats.strg import STRG
from retro_data_structures.formats.txtr import TXTR

ALL_FORMATS = {
    "ANCS": ANCS,
    "ANIM": ANIM,
    "CINF": CINF,
    "CMDL": CMDL,
    "CSKR": CSKR,
    "CSPP": CSPP,
    "DGRP": DGRP,
    "EVNT": EVNT,
    "MLVL": MLVL,
    "MREA": Mrea,
    "PAK": PAK,
    "PART": PART,
    "SCAN": SCAN,
    "STRG": STRG,
    "TXTR": TXTR,
}


def format_for(type_name: AssetType) -> Construct:
    return ALL_FORMATS[type_name.upper()]
