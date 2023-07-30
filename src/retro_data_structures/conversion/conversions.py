from __future__ import annotations

from typing import TYPE_CHECKING

from retro_data_structures.conversion import ancs, anim, cinf, cmdl, cskr, evnt, part, txtr

if TYPE_CHECKING:
    from retro_data_structures.conversion.asset_converter import AssetDetails, ResourceConverter

ALL_FORMATS = {
    "ANCS": ancs.CONVERTERS,
    "ANIM": anim.CONVERTERS,
    "CINF": cinf.CONVERTERS,
    "CMDL": cmdl.CONVERTERS,
    "CSKR": cskr.CONVERTERS,
    "EVNT": evnt.CONVERTERS,
    "PART": part.CONVERTERS,
    "TXTR": txtr.CONVERTERS,
}


def converter_for(details: AssetDetails) -> ResourceConverter:
    try:
        format_converters = ALL_FORMATS[details.asset_type.upper()]
    except KeyError as e:
        raise KeyError(f"No conversion available for format {e}")

    return format_converters[details.original_game]
