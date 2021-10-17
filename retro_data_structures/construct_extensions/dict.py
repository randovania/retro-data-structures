from construct import Adapter, Struct, VarInt, PrefixedArray

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
            if self.objisdict:
                v["*Key"] = k
            else:
                v = {"*Key": k, "Value": v}
            L.append(v)
        return L


def DictStruct(*fields):
    return Struct(*fields, "*Key" / String)
