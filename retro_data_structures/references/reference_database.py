import functools
import pprint
from pathlib import Path

import construct

from retro_data_structures.asset_reference import AssetReference

_ConstructReferenceDB = construct.Compressed(construct.PrefixedArray(construct.VarInt, construct.Struct(
    name=construct.CString("utf-8"),
    asset_id=construct.VarInt,
)), "zlib", level=9)


@functools.cache
def echoes_db() -> dict[int, AssetReference]:
    db = _ConstructReferenceDB.parse_file(Path(__file__).parent.joinpath("prime2_reference.bin"))
    return {
        reference["asset_id"]: AssetReference(
            asset_id=reference["asset_id"],
            description=reference["name"],
            is_custom=False,
        )
        for reference in db
    }


if __name__ == '__main__':
    pprint.pprint(echoes_db())
