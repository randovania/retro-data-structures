import io

import construct
from construct import Construct, stream_tell, Subconstruct, GreedyBytes


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


class PrefixedWithPaddingBefore(Subconstruct):
    def __init__(self, length_field, subcon, padding=32):
        super().__init__(subcon)
        self.padding = padding
        self.length_field = length_field

    def _parse(self, stream, context, path):
        length = self.length_field._parsereport(stream, context, path)
        bytes_to_pad = self.padding - (length % self.padding)
        if bytes_to_pad < self.padding:
            construct.stream_read(stream, bytes_to_pad, path)
        data = construct.stream_read(stream, length, path)
        if self.subcon is GreedyBytes:
            return data
        return self.subcon._parsereport(io.BytesIO(data), context, path)

    def _build(self, obj, stream, context, path):
        stream2 = io.BytesIO()
        buildret = self.subcon._build(obj, stream2, context, path)
        data = stream2.getvalue()
        length = len(data)
        self.length_field._build(length, stream, context, path)

        bytes_to_pad = self.padding - (length % self.padding)
        if bytes_to_pad < self.padding:
            construct.stream_write(stream, b"\x00" * bytes_to_pad, bytes_to_pad, path)

        construct.stream_write(stream, data, len(data), path)
        return buildret
