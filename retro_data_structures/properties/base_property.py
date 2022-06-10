import io
import typing


Self = typing.TypeVar("Self", bound="BaseProperty")


class BaseProperty:
    @classmethod
    def from_stream(cls: typing.Type[Self], data: typing.BinaryIO, size: typing.Optional[int] = None) -> Self:
        raise NotImplementedError()

    @classmethod
    def from_bytes(cls: typing.Type[Self], data: bytes) -> Self:
        stream = io.BytesIO(data)
        return cls.from_stream(stream, len(data))

    def to_stream(self, data: typing.BinaryIO) -> None:
        raise NotImplementedError()

    def to_bytes(self) -> bytes:
        stream = io.BytesIO()
        self.to_stream(stream)
        return stream.getvalue()

    @classmethod
    def from_json(cls: typing.Type[Self], data: typing.Any) -> Self:
        raise NotImplementedError()

    def to_json(self) -> typing.Any:
        raise NotImplementedError()
