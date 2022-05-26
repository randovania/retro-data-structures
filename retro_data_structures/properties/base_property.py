import typing


class BaseProperty:
    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):
        raise NotImplementedError()

    def to_stream(self, data: typing.BinaryIO) -> None:
        raise NotImplementedError()

    @classmethod
    def from_json(cls, data: typing.Any):
        raise NotImplementedError()

    def to_json(self) -> typing.Any:
        raise NotImplementedError()
