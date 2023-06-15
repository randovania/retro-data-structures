from __future__ import annotations
import dataclasses
import io
import typing
from abc import ABC

from retro_data_structures.base_resource import AssetId, Dependency
from retro_data_structures.formats.ancs import Ancs

from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager

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
    
    def dependencies_for(self, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
        for field in dataclasses.fields(self):
            if issubclass(field.type, BaseProperty):
                prop: BaseProperty = getattr(self, field.name)
                yield from prop.dependencies_for(asset_manager)
            
            if issubclass(field.type, AssetId):
                asset_id: AssetId = getattr(self, field.name)
                yield from asset_manager.get_dependencies_for_asset(asset_id)

    def mlvl_dependencies_for(self, asset_manager: AssetManager, is_player_actor: bool = False) -> typing.Iterator[Dependency]:
        # i'm so sorry
        classname = self.__class__.__name__
        if classname == "PlayerActor":
            is_player_actor = True

        for field in dataclasses.fields(self):
            try:
                if issubclass(field.type, BaseProperty):
                    if field.type.__name__ == "AreaAttributes":
                        continue # ignore the skybox
                    prop: BaseProperty = getattr(self, field.name)
                    yield from prop.mlvl_dependencies_for(asset_manager, is_player_actor)
                elif issubclass(field.type, int) and (field.default == 0xFFFFFFFF or 'asset_types' in field.metadata):
                    if (
                        ('asset_types' in field.metadata)
                        and (("MLVL" in field.metadata['asset_types'])
                             or ("MREA" in field.metadata['asset_types'])
                        )
                    ):
                        continue
                    asset_id: AssetId = getattr(self, field.name)
                    yield from asset_manager.get_mlvl_dependencies_for_asset(asset_id, is_player_actor)
            except Exception as e:
                raise Exception(f"Error finding dependencies for {classname}.{field.name} ({field.type}): {e}")


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
