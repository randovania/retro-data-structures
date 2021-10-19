from construct import Adapter, Int32ub, Enum


class EnumAdapter(Adapter):
    def __init__(self, enum_class, subcon=Int32ub):
        super().__init__(Enum(subcon, enum_class))
        self._enum_class = enum_class

    def _decode(self, obj, context, path):
        return self._enum_class[obj]

    def _encode(self, obj, context, path):
        return obj.name
