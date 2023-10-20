from __future__ import annotations

import dataclasses
import io
import typing
from abc import ABC

if typing.TYPE_CHECKING:
    import typing_extensions

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetId, Dependency
    from retro_data_structures.game_check import Game


@dataclasses.dataclass()
class BaseProperty:
    @classmethod
    def game(cls) -> Game:
        raise NotImplementedError

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: int | None = None) -> typing_extensions.Self:
        raise NotImplementedError

    @classmethod
    def from_bytes(cls, data: bytes) -> typing_extensions.Self:
        stream = io.BytesIO(data)
        return cls.from_stream(stream, len(data))

    def to_stream(self, data: typing.BinaryIO) -> None:
        raise NotImplementedError

    def to_bytes(self) -> bytes:
        stream = io.BytesIO()
        self.to_stream(stream)
        return stream.getvalue()

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        raise NotImplementedError

    def to_json(self) -> json_util.JsonValue:
        raise NotImplementedError

    def _is_property_mrea_or_mlvl(self, field: dataclasses.Field) -> bool:
        asset_types = field.metadata.get("asset_types", [])
        return any((typ in asset_types) for typ in ("MLVL", "MREA"))

    def _dependencies_for_field(
        self, field: dataclasses.Field, asset_manager: AssetManager
    ) -> typing.Iterator[Dependency]:
        if issubclass(field.type, BaseProperty):
            prop: BaseProperty = getattr(self, field.name)
            yield from prop.dependencies_for(asset_manager)

        elif issubclass(field.type, int) and "sound" in field.metadata:
            sound_id: int = getattr(self, field.name)
            yield from asset_manager.get_audio_group_dependency(sound_id)

        elif issubclass(field.type, int) and (field.default == 0xFFFFFFFF or "asset_types" in field.metadata):
            if self._is_property_mrea_or_mlvl(field):
                return
            asset_id: AssetId = getattr(self, field.name)
            yield from asset_manager.get_dependencies_for_asset(asset_id)

    def dependencies_for(self, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
        for field in dataclasses.fields(self):
            try:
                yield from self._dependencies_for_field(field, asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for {self.__class__.__name__}.{field.name} ({field.type}): {e}"
                )


class BaseObjectType(BaseProperty, ABC):
    @classmethod
    def object_type(cls) -> str | int:
        raise NotImplementedError

    @classmethod
    def modules(cls) -> list[str]:
        return []

    def get_name(self) -> str | None:
        raise NotImplementedError

    def set_name(self, name: str) -> None:
        raise NotImplementedError
