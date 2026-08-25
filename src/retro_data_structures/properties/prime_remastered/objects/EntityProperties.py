# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime_remastered.archetypes.Vector3f import Vector3f

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class EntityPropertiesJson(typing_extensions.TypedDict):
        unk_bool_1: bool
        unk_bool_2: bool
        position: json_util.JsonObject
        rotation: json_util.JsonObject
        scale: json_util.JsonObject


@dataclasses.dataclass()
class EntityProperties(BaseProperty):
    unk_bool_1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="Unk Bool 1"),
        },
    )
    unk_bool_2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="Unk Bool 2"),
        },
    )
    position: Vector3f = dataclasses.field(
        default_factory=Vector3f,
        metadata={
            "reflection": FieldReflection[Vector3f](
                Vector3f,
                id=0x00000002,
                original_name="Position",
                from_json=Vector3f.from_json,
                to_json=Vector3f.to_json,
            ),
        },
    )
    rotation: Vector3f = dataclasses.field(
        default_factory=Vector3f,
        metadata={
            "reflection": FieldReflection[Vector3f](
                Vector3f,
                id=0x00000003,
                original_name="Rotation",
                from_json=Vector3f.from_json,
                to_json=Vector3f.to_json,
            ),
        },
    )
    scale: Vector3f = dataclasses.field(
        default_factory=Vector3f,
        metadata={
            "reflection": FieldReflection[Vector3f](
                Vector3f, id=0x00000004, original_name="Scale", from_json=Vector3f.from_json, to_json=Vector3f.to_json
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unk_bool_1 = structs.LITTLE_bool_.unpack(data.read(1))[0]
        unk_bool_2 = structs.LITTLE_bool_.unpack(data.read(1))[0]
        position = Vector3f.from_stream(data, game, property_size)
        rotation = Vector3f.from_stream(data, game, property_size)
        scale = Vector3f.from_stream(data, game, property_size)
        return cls(unk_bool_1, unk_bool_2, position, rotation, scale)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.LITTLE_bool_.pack(self.unk_bool_1))
        data.write(structs.LITTLE_bool_.pack(self.unk_bool_2))
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EntityPropertiesJson", data)
        return cls(
            unk_bool_1=json_data["unk_bool_1"],
            unk_bool_2=json_data["unk_bool_2"],
            position=Vector3f.from_json(json_data["position"]),
            rotation=Vector3f.from_json(json_data["rotation"]),
            scale=Vector3f.from_json(json_data["scale"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unk_bool_1": self.unk_bool_1,
            "unk_bool_2": self.unk_bool_2,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
        }
