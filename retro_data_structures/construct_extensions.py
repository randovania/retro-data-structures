import io
from typing import Any

import construct
from construct import (
    FocusedSeq, Rebuild, this, len_, GreedyRange, Int32ul, stream_tell, Int32ub, ListContainer,
    EnumIntegerString, Container, Adapter, Enum, If, Subconstruct, Construct
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

    def _encode(self, obj, context, path):
        return obj.name


def convert_to_raw_python(value) -> Any:
    if callable(value):
        value = value()

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


class AlignTo(Construct):
    def __init__(self, modulus):
        super().__init__()
        self.modulus = modulus
        self.pattern = b"\x00"
        self.flagbuildnone = True

    def _parse(self, stream, context, path):
        modulus = construct.evaluate(self.modulus, context)
        position = stream_tell(stream, path)
        pad = modulus - (position % modulus)
        if pad < modulus:
            return construct.stream_read(stream, pad, path)
        return b""

    def _build(self, obj, stream, context, path):
        modulus = construct.evaluate(self.modulus, context)
        position = stream_tell(stream, path)
        pad = modulus - (position % modulus)
        if pad < modulus:
            construct.stream_write(stream, self.pattern * pad, pad, path)


def BitwiseWith32Blocks(subcon):
    """
    Bit level decoding in Retro's format are done from least significant bit, but in blocks of 32 bits.

    """
    return construct.Restreamed(
        subcon,
        lambda data: bytes(reversed(construct.bytes2bits(data))), 4,
        lambda data: construct.bits2bytes(bytes(reversed(data))), 32,
        lambda n: n // 32,
    )


class AlignedPrefixed(Subconstruct):
    def __init__(self, length_field, subcon, modulus, length_size, pad_byte=b"\xFF"):
        super().__init__(subcon)
        self.length_field = length_field
        self.modulus = modulus
        self.length_size = length_size
        self.pad_byte = pad_byte

    def _parse(self, stream, context, path):
        modulus = construct.evaluate(self.modulus, context)
        length_size = construct.evaluate(self.modulus, context)

        length = self.length_field._parsereport(stream, context, path)
        data = construct.stream_read(stream, length, path)
        pad = modulus - ((len(data) - length_size) % modulus)
        if pad < modulus:
            data += self.pad_byte * pad

        if self.subcon is construct.GreedyBytes:
            return data
        if type(self.subcon) is construct.GreedyString:
            return data.decode(self.subcon.encoding)
        return self.subcon._parsereport(io.BytesIO(data), context, path)

    def _build(self, obj, stream, context, path):
        modulus = construct.evaluate(self.modulus, context)
        length_size = construct.evaluate(self.modulus, context)

        stream2 = io.BytesIO()
        buildret = self.subcon._build(obj, stream2, context, path)
        data = stream2.getvalue()
        pad = modulus - ((len(data) - length_size) % modulus)
        if pad < modulus:
            data += self.pad_byte * pad

        self.length_field._build(len(data), stream, context, path)
        construct.stream_write(stream, data, len(data), path)
        return buildret

    def _sizeof(self, context, path):
        return self.length_field._sizeof(context, path) + self.subcon._sizeof(context, path)

    def _actualsize(self, stream, context, path):
        position1 = stream_tell(stream, path)
        length = self.length_field._parse(stream, context, path)
        position2 = stream_tell(stream, path)
        return (position2 - position1) + length


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
