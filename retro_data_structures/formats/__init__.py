import typing

from construct import Construct

from retro_data_structures.formats.ancs import ANCS, Ancs
from retro_data_structures.formats.anim import ANIM, Anim
from retro_data_structures.base_resource import BaseResource, AssetType
from retro_data_structures.formats.char import CHAR, Char
from retro_data_structures.formats.cinf import CINF, Cinf
from retro_data_structures.formats.cmdl import CMDL, Cmdl
from retro_data_structures.formats.cskr import CSKR, Cskr
from retro_data_structures.formats.cspp import CSPP, Cspp
from retro_data_structures.formats.dgrp import DGRP, Dgrp
from retro_data_structures.formats.evnt import EVNT, Evnt
from retro_data_structures.formats.mapw import Mapw
from retro_data_structures.formats.mlvl import MLVL, Mlvl
from retro_data_structures.formats.mrea import MREA, Mrea
from retro_data_structures.formats.pak import PAK, Pak
from retro_data_structures.formats.part import PART, Part
from retro_data_structures.formats.sand import SAND, Sand
from retro_data_structures.formats.savw import SAVW, Savw
from retro_data_structures.formats.scan import SCAN, Scan
from retro_data_structures.formats.strg import STRG, Strg
from retro_data_structures.formats.txtr import TXTR, Txtr

ALL_FORMATS = {
    "ANCS": ANCS,
    "ANIM": ANIM,
    "CHAR": CHAR,
    "CINF": CINF,
    "CMDL": CMDL,
    "CSKR": CSKR,
    "CSPP": CSPP,
    "DGRP": DGRP,
    "EVNT": EVNT,
    "MLVL": MLVL,
    "MREA": MREA,
    "PAK": PAK,
    "PART": PART,
    "SAND": SAND,
    "SAVW": SAVW,
    "SCAN": SCAN,
    "STRG": STRG,
    "TXTR": TXTR,
}

ALL_RESOURCE_TYPES = {
    "ANCS": Ancs,
    "ANIM": Anim,
    "CHAR": Char,
    "CINF": Cinf,
    "CMDL": Cmdl,
    "CSKR": Cskr,
    "CSPP": Cspp,
    "DGRP": Dgrp,
    "EVNT": Evnt,
    "MAPW": Mapw,
    "MLVL": Mlvl,
    "MREA": Mrea,
    "PAK": Pak,
    "PART": Part,
    "SAND": Sand,
    "SAVW": Savw,
    "SCAN": Scan,
    "STRG": Strg,
    "TXTR": Txtr,
}


def format_for(type_name: AssetType) -> Construct:
    return ALL_FORMATS[type_name.upper()]


def resource_type_for(type_name: AssetType) -> typing.Type[BaseResource]:
    return ALL_RESOURCE_TYPES[type_name.upper()]


__all__ = [
    "format_for",
    "resource_type_for",
]
