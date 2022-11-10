import io
import typing
from abc import ABC

from retro_data_structures.game_check import Game

Self = typing.TypeVar("Self", bound="BaseProperty")


class BaseProperty:
    @classmethod
    def game(cls) -> Game:
        raise NotImplementedError()

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


class BaseObjectType(BaseProperty, ABC):
    @classmethod
    def object_type(cls) -> typing.Union[str, int]:
        raise NotImplementedError()

    @classmethod
    def modules(cls) -> typing.List[str]:
        return []

    def get_name(self) -> typing.Optional[str]:
        raise NotImplementedError()

    def set_name(self, name: str) -> None:
        raise NotImplementedError()
