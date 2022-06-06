import io
import typing


class BaseProperty:
    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):
        raise NotImplementedError()

    @classmethod
    def from_bytes(cls, data: bytes):
        stream = io.BytesIO(data)
        return cls.from_stream(stream, len(data))

    def to_stream(self, data: typing.BinaryIO) -> None:
        raise NotImplementedError()

    def to_bytes(self) -> bytes:
        stream = io.BytesIO()
        self.to_stream(stream)
        return stream.getvalue()

    @classmethod
    def from_json(cls, data: typing.Any):
        raise NotImplementedError()

    def to_json(self) -> typing.Any:
        raise NotImplementedError()
