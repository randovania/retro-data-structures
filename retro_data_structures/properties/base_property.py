import dataclasses
import io
import typing
from abc import ABC

from retro_data_structures.base_resource import AssetId, NameOrAssetId
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

    @classmethod    
    def dependency_fields(cls):
        for field in dataclasses.fields(cls):
            if issubclass(field.type, BaseProperty):
                fields = list(field.type.dependency_fields())
                if fields:
                    yield field.name, fields
            
            elif "asset_types" in field.metadata:
                yield field.name, field.metadata["asset_types"]

    def mlvl_dependencies_for(self, to_skip: set[str] = set()) -> typing.Iterator[typing.Union[AssetId, "BaseProperty"]]:
        for field in dataclasses.fields(self):
            if field.name not in to_skip and (issubclass(field.type, BaseProperty) or "asset_types" in field.metadata):
                yield getattr(self, field.name)

    def dependencies_for(self) -> typing.Iterator[AssetId]:
        for field in dataclasses.fields(self):
            if issubclass(field.type, BaseProperty):
                prop: BaseProperty = getattr(self, field.name)
                yield from prop.dependencies_for()
            
            elif "asset_types" in field.metadata:
                prop: field.type = getattr(self, field.name)
                if prop != field.default:
                    yield prop


class BaseObjectType(BaseProperty, ABC):
    @classmethod
    def object_type(cls) -> str:
        raise NotImplementedError()

    @classmethod
    def modules(cls) -> typing.List[str]:
        return []
