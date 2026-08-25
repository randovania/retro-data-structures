# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.BasicSwarmProperties import BasicSwarmProperties
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class FlyerSwarmJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        animation_information: json_util.JsonObject
        active: bool
        basic_swarm_properties: json_util.JsonObject
        unknown_0x4a85a2da: float
        unknown_0x10cccd3c: float
        unknown_0x1e8e90a4: float
        unknown_0x262e586d: float
        roll_upright_speed: float
        roll_upright_min_angle: float


@dataclasses.dataclass()
class FlyerSwarm(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    actor_information: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x7E397FED,
                original_name="ActorInformation",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    animation_information: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xE25FB08C,
                original_name="AnimationInformation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    active: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC6BB2F45, original_name="Active"),
        },
    )
    basic_swarm_properties: BasicSwarmProperties = dataclasses.field(
        default_factory=BasicSwarmProperties,
        metadata={
            "reflection": FieldReflection[BasicSwarmProperties](
                BasicSwarmProperties,
                id=0xE1EC7346,
                original_name="BasicSwarmProperties",
                from_json=BasicSwarmProperties.from_json,
                to_json=BasicSwarmProperties.to_json,
            ),
        },
    )
    unknown_0x4a85a2da: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4A85A2DA, original_name="Unknown"),
        },
    )
    unknown_0x10cccd3c: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x10CCCD3C, original_name="Unknown"),
        },
    )
    unknown_0x1e8e90a4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E8E90A4, original_name="Unknown"),
        },
    )
    unknown_0x262e586d: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x262E586D, original_name="Unknown"),
        },
    )
    roll_upright_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x479A5727, original_name="RollUprightSpeed"),
        },
    )
    roll_upright_min_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD572D1DA, original_name="RollUprightMinAngle"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "FSWM"

    @classmethod
    def modules(cls) -> list[str]:
        return ["SwarmBasics.rel", "FlyerSwarm.rel"]

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6BB2F45
        active = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1EC7346
        basic_swarm_properties = BasicSwarmProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A85A2DA
        unknown_0x4a85a2da = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10CCCD3C
        unknown_0x10cccd3c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E8E90A4
        unknown_0x1e8e90a4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x262E586D
        unknown_0x262e586d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x479A5727
        roll_upright_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD572D1DA
        roll_upright_min_angle = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            actor_information,
            animation_information,
            active,
            basic_swarm_properties,
            unknown_0x4a85a2da,
            unknown_0x10cccd3c,
            unknown_0x1e8e90a4,
            unknown_0x262e586d,
            roll_upright_speed,
            roll_upright_min_angle,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe2_\xb0\x8c")  # 0xe25fb08c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\xbb/E")  # 0xc6bb2f45
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.active))

        data.write(b"\xe1\xecsF")  # 0xe1ec7346
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.basic_swarm_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"J\x85\xa2\xda")  # 0x4a85a2da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4a85a2da))

        data.write(b"\x10\xcc\xcd<")  # 0x10cccd3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x10cccd3c))

        data.write(b"\x1e\x8e\x90\xa4")  # 0x1e8e90a4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1e8e90a4))

        data.write(b"&.Xm")  # 0x262e586d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x262e586d))

        data.write(b"G\x9aW'")  # 0x479a5727
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.roll_upright_speed))

        data.write(b"\xd5r\xd1\xda")  # 0xd572d1da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.roll_upright_min_angle))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyerSwarmJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            active=json_data["active"],
            basic_swarm_properties=BasicSwarmProperties.from_json(json_data["basic_swarm_properties"]),
            unknown_0x4a85a2da=json_data["unknown_0x4a85a2da"],
            unknown_0x10cccd3c=json_data["unknown_0x10cccd3c"],
            unknown_0x1e8e90a4=json_data["unknown_0x1e8e90a4"],
            unknown_0x262e586d=json_data["unknown_0x262e586d"],
            roll_upright_speed=json_data["roll_upright_speed"],
            roll_upright_min_angle=json_data["roll_upright_min_angle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_information": self.actor_information.to_json(),
            "animation_information": self.animation_information.to_json(),
            "active": self.active,
            "basic_swarm_properties": self.basic_swarm_properties.to_json(),
            "unknown_0x4a85a2da": self.unknown_0x4a85a2da,
            "unknown_0x10cccd3c": self.unknown_0x10cccd3c,
            "unknown_0x1e8e90a4": self.unknown_0x1e8e90a4,
            "unknown_0x262e586d": self.unknown_0x262e586d,
            "roll_upright_speed": self.roll_upright_speed,
            "roll_upright_min_angle": self.roll_upright_min_angle,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.basic_swarm_properties.dependencies_for, "basic_swarm_properties", "BasicSwarmProperties"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for FlyerSwarm.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_basic_swarm_properties(data: typing.BinaryIO, game: Game, property_size: int) -> BasicSwarmProperties:
    return BasicSwarmProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0xC6BB2F45: ("active", structs.decode_BIG_bool_),
    0xE1EC7346: ("basic_swarm_properties", _decode_basic_swarm_properties),
    0x4A85A2DA: ("unknown_0x4a85a2da", structs.decode_BIG_f),
    0x10CCCD3C: ("unknown_0x10cccd3c", structs.decode_BIG_f),
    0x1E8E90A4: ("unknown_0x1e8e90a4", structs.decode_BIG_f),
    0x262E586D: ("unknown_0x262e586d", structs.decode_BIG_f),
    0x479A5727: ("roll_upright_speed", structs.decode_BIG_f),
    0xD572D1DA: ("roll_upright_min_angle", structs.decode_BIG_f),
}
