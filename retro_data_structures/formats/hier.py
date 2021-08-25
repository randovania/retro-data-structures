import construct
from construct import Const, CString, Int32ub, PrefixedArray, Struct

HIER = Struct (
    magic=Const(b"HIER"),
    hierarchy_entries=PrefixedArray(Int32ub, Struct(
        string_table_id=Int32ub,
        name=CString("utf-16"),
        scan_id=Int32ub,
        parent_index=Int32ub
    ))
)