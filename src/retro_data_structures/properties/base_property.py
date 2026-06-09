from __future__ import annotations

import dataclasses
import io
import typing
from abc import ABC

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game
    from retro_data_structures.properties.shared_archetypes import EditorProperties


@dataclasses.dataclass()
class BaseProperty:
    @classmethod
    def game(cls) -> Game:
        raise NotImplementedError

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: int | None = None) -> typing.Self:
        raise NotImplementedError

    @classmethod
    def from_bytes(cls, data: bytes) -> typing.Self:
        stream = io.BytesIO(data)
        return cls.from_stream(stream, len(data))

    def to_stream(self, data: typing.BinaryIO) -> None:
        raise NotImplementedError

    def to_bytes(self) -> bytes:
        stream = io.BytesIO()
        self.to_stream(stream)
        return stream.getvalue()

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing.Self:
        raise NotImplementedError

    def to_json(self) -> json_util.JsonValue:
        raise NotImplementedError


class BaseObjectType(BaseProperty, ABC):
    @classmethod
    def object_type(cls) -> str | int:
        raise NotImplementedError

    @classmethod
    def modules(cls) -> list[str]:
        return []

    def get_name(self) -> str:
        raise NotImplementedError

    def set_name(self, name: str) -> None:
        raise NotImplementedError

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        raise NotImplementedError


@typing.runtime_checkable
class ObjectWithEditorProperties(typing.Protocol):
    editor_properties: EditorProperties
