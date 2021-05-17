from construct import FocusedSeq, Rebuild, this, len_, GreedyRange, Int32ul, stream_tell, Int32ub


def PrefixedArrayWithExtra(countfield, extrafield, subcon):
    r"""
    Prefixes an array with item count (as opposed to prefixed by byte count, see :class:`~construct.core.Prefixed`), with an extra field between the count and the data.

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
        return (position2-position1) + count * subcon._sizeof(context, path) + extrafield._sizeof(context, path)
    macro._actualsize = _actualsize

    def _emitseq(ksy, bitwise):
        return [
            dict(id="countfield", type=countfield._compileprimitivetype(ksy, bitwise)),
            dict(id="extra", type=extrafield._compileprimitivetype(ksy, bitwise)),
            dict(id="data", type=subcon._compileprimitivetype(ksy, bitwise), repeat="expr", repeat_expr="countfield"),
        ]
    macro._emitseq = _emitseq

    return macro
