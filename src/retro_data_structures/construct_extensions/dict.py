from __future__ import annotations

from construct import Adapter, PrefixedArray, Struct, VarInt

from retro_data_structures.common_types import String


class DictAdapter(Adapter):
    def __init__(self, subcon, objisdict=True):
        if not objisdict:
            subcon = Struct("*Key" / VarInt, "Value" / subcon)
        super().__init__(PrefixedArray(VarInt, subcon))
        self.objisdict = objisdict

    def _decode(self, obj, context, path):
        D = {}
        for v in obj:
            if self.objisdict:
                D[v["*Key"]] = v
                del v["*Key"]
            else:
                D[v["*Key"]] = v["Value"]
        return D

    def _encode(self, obj, context, path):
        L = []
        for k, v in obj.items():
            new_item = v
            if self.objisdict:
                v["*Key"] = k
            else:
                new_item = {"*Key": k, "Value": v}
            L.append(new_item)
        return L


def DictStruct(*fields):
    return Struct(*fields, "*Key" / String)
