from __future__ import annotations

import construct
from construct import Bytes, Const, Int32ub, PrefixedArray, Struct

from retro_data_structures.common_types import AssetId64, FourCC, String
from retro_data_structures.construct_extensions.dict import make_dict

PAKHeader = construct.Aligned(
    64,
    Struct(
        version=Const(2, Int32ub),
        header_size=Int32ub,
        md5_hash=Bytes(16),
    ),
)

ConstructResourceHeader = Struct(
    compressed=Int32ub,
    asset_type=FourCC,
    asset_id=AssetId64,
    size=Int32ub,
    offset=Int32ub,
)


def _emitparse_header(code: construct.CodeGen) -> str:
    code.append("ResourceHeader_Format = struct.Struct('>LLQLL')")
    code.append(
        """def _create_resource_header(compressed, asset_type, asset_id, size, offset):
    return Container(compressed=compressed, asset_type=asset_type.to_bytes(4, "big").decode("ascii"),
                     asset_id=asset_id, size=size, offset=offset)
    """
    )
    return "_create_resource_header(*ResourceHeader_Format.unpack(io.read(24)))"


ConstructResourceHeader._emitparse = _emitparse_header

PAKNoData = Struct(
    _start=construct.Tell,
    _header=PAKHeader,
    table_of_contents=construct.Aligned(64, make_dict(Int32ub, FourCC)),
    _named_resources_start=construct.Tell,
    named_resources=construct.Aligned(
        64,
        PrefixedArray(
            Int32ub,
            Struct(
                name=String,
                asset_type=FourCC,
                asset_id=AssetId64,
            ),
        ),
    ),
    _resources_start=construct.Tell,
    _resources_start_assert=construct.Check(
        construct.this.table_of_contents.STRG == construct.this._resources_start - construct.this._named_resources_start
    ),
    resources=construct.Aligned(64, PrefixedArray(Int32ub, ConstructResourceHeader)),
    _resources_end=construct.Tell,
    _resources_end_assert=construct.Check(
        construct.this.table_of_contents.RSHD == construct.this._resources_end - construct.this._resources_start
    ),
)
