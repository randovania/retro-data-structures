from retro_data_structures.conversion import anim, ancs, cinf, cmdl, cskr, evnt, part, txtr
from retro_data_structures.conversion.asset_converter import ResourceConverter
from retro_data_structures.formats import AssetType
from retro_data_structures.game_check import Game

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


def converter_for(source_game: Game, type_name: AssetType) -> ResourceConverter:
    try:
        format_converters = ALL_FORMATS[type_name.upper()]
    except KeyError as e:
        raise KeyError(f"No conversion available for format {e}")

    return format_converters[source_game]
