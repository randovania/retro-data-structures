import construct
from construct import FocusedSeq, Rebuild, len_, this, stream_tell, Construct, Optional, Const


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
    macro = FocusedSeq(
        "items",
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


def BitwiseWith32Blocks(subcon):
    """
    Bit level decoding in Retro's format are done from least significant bit, but in blocks of 32 bits.

    """
    return construct.Restreamed(
        subcon,
        lambda data: bytes(reversed(construct.bytes2bits(data))),
        4,
        lambda data: construct.bits2bytes(bytes(reversed(data))),
        32,
        lambda n: n // 32,
    )


def Skip(count, subcon):
    return construct.Seek(count * subcon.length, 1)


class LazyPatchedForBug(construct.Lazy):
    r"""
    See https://github.com/construct/construct/issues/938
    """

    def _parse(self, stream, context, path):
        offset = stream_tell(stream, path)

        def execute():
            fallback = stream_tell(stream, path)
            construct.stream_seek(stream, offset, 0, path)
            obj = self.subcon._parsereport(stream, context, path)
            construct.stream_seek(stream, fallback, 0, path)
            return obj

        length = self.subcon._actualsize(stream, context, path)
        construct.stream_seek(stream, length, 1, path)
        return execute


class ErrorWithMessage(Construct):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.flagbuildnone = True

    def _parse(self, stream, context, path):
        message = construct.evaluate(self.message, context)
        raise construct.ExplicitError(f"Error field was activated during parsing with error {message}", path=path)

    def _build(self, obj, stream, context, path):
        message = construct.evaluate(self.message, context)
        raise construct.ExplicitError(f"Error field was activated during building with error {message}", path=path)

    def _sizeof(self, context, path):
        raise construct.SizeofError("Error does not have size, because it interrupts parsing and building", path=path)


def LabeledOptional(label, subcon):
    return Optional(
        FocusedSeq(
            "subcon",
            Const(label),
            "subcon" / subcon,
        )
    )
