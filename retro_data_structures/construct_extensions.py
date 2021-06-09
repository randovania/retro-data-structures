from typing import Any

from construct import (
    FocusedSeq, Rebuild, this, len_, GreedyRange, Int32ul, stream_tell, Int32ub, ListContainer,
    EnumIntegerString, Container, Adapter, Enum, If
)


def PrefixedArrayWithExtra(countfield, extrafield, subcon):
    r"""
    Prefixes an array with item count (as opposed to prefixed by byte count, see :class:`~construct.core.Prefixed`),
    with an extra field between the count and the data.

    Example::

        >>> d = PrefixedArrayWithExtra(Int32ub, Int32ub, GreedyRange(Int32ul))
        >>> d.parse(b"\x08abcdefgh")
        [1684234849, 1751606885]

        >>> d = PrefixedArrayWithExtra(Int32ub, Int32ub, Int32ul)
        >>> d.parse(b"\x02abcdefgh")
        [1684234849, 1751606885]
    """
    macro = FocusedSeq("items",
                       "count" / Rebuild(countfield, len_(this.items)),
                       "extra" / extrafield,
                       "items" / subcon[this.count],
                       )

    def _actualsize(self, stream, context, path):
        position1 = stream_tell(stream, path)
        count = countfield._parse(stream, context, path)
        position2 = stream_tell(stream, path)
        return (position2 - position1) + count * subcon._sizeof(context, path) + extrafield._sizeof(context, path)

    macro._actualsize = _actualsize

    def _emitseq(ksy, bitwise):
        return [
            dict(id="countfield", type=countfield._compileprimitivetype(ksy, bitwise)),
            dict(id="extra", type=extrafield._compileprimitivetype(ksy, bitwise)),
            dict(id="data", type=subcon._compileprimitivetype(ksy, bitwise), repeat="expr", repeat_expr="countfield"),
        ]

    macro._emitseq = _emitseq

    return macro


class EnumAdapter(Adapter):
    def __init__(self, enum_class, subcon=Int32ub):
        super().__init__(Enum(subcon, enum_class))
        self._enum_class = enum_class

    def _decode(self, obj, context, path):
        return self._enum_class[obj]


def convert_to_raw_python(value) -> Any:
    if isinstance(value, ListContainer):
        return [
            convert_to_raw_python(item)
            for item in value
        ]

    if isinstance(value, Container):
        return {
            key: convert_to_raw_python(item)
            for key, item in value.items()
            if not key.startswith("_")
        }

    if isinstance(value, EnumIntegerString):
        return str(value)

    return value


def get_version(this):
    if 'version' not in this:
        return get_version(this['_'])
    else:
        return this.version


def WithVersion(version, subcon):
    return If(lambda this: get_version(this) >= version, subcon)


def BeforeVersion(version, subcon):
    return If(lambda this: get_version(this) < version, subcon)
