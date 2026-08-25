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
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PlayerControllerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_0xe71de331: int
        model: int
        animation_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        proxy_type: int
        player_offset: json_util.JsonValue
        initial_state: int
        player_visor: int
        unknown_0xf09c2b4b: float
        unknown_0x760859e5: float
        unknown_0xbd548a40: float
        rotation_for_type3: json_util.JsonValue
        unknown_0x70bc90a6: str


@dataclasses.dataclass()
class PlayerController(BaseObjectType):
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
    unknown_0xe71de331: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE71DE331, original_name="Unknown"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC27FFA8F, original_name="Model"),
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
    proxy_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCA56A18A, original_name="ProxyType"),
        },
    )
    player_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=1.5),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x1D8B933F, original_name="PlayerOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    initial_state: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCB753319, original_name="InitialState"),
        },
    )
    player_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD9C09CF7, original_name="PlayerVisor"),
        },
    )
    unknown_0xf09c2b4b: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF09C2B4B, original_name="Unknown"),
        },
    )
    unknown_0x760859e5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x760859E5, original_name="Unknown"),
        },
    )
    unknown_0xbd548a40: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBD548A40, original_name="Unknown"),
        },
    )
    rotation_for_type3: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xC012F196,
                original_name="RotationForType3",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    unknown_0x70bc90a6: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x70BC90A6, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PLCT"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ScriptPlayerProxy.rel"]

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
        if property_count != 14:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE71DE331
        unknown_0xe71de331 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCA56A18A
        proxy_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D8B933F
        player_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB753319
        initial_state = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD9C09CF7
        player_visor = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF09C2B4B
        unknown_0xf09c2b4b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x760859E5
        unknown_0x760859e5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD548A40
        unknown_0xbd548a40 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC012F196
        rotation_for_type3 = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70BC90A6
        unknown_0x70bc90a6 = data.read(property_size)[:-1].decode("utf-8")

        return cls(
            editor_properties,
            unknown_0xe71de331,
            model,
            animation_information,
            actor_information,
            proxy_type,
            player_offset,
            initial_state,
            player_visor,
            unknown_0xf09c2b4b,
            unknown_0x760859e5,
            unknown_0xbd548a40,
            rotation_for_type3,
            unknown_0x70bc90a6,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe7\x1d\xe31")  # 0xe71de331
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe71de331))

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.model))

        data.write(b"\xe2_\xb0\x8c")  # 0xe25fb08c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation_information.to_stream(data, game)
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

        data.write(b"\xcaV\xa1\x8a")  # 0xca56a18a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.proxy_type))

        data.write(b"\x1d\x8b\x93?")  # 0x1d8b933f
        data.write(b"\x00\x0c")  # size
        self.player_offset.to_stream(data, game)

        data.write(b"\xcbu3\x19")  # 0xcb753319
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.initial_state))

        data.write(b"\xd9\xc0\x9c\xf7")  # 0xd9c09cf7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.player_visor))

        data.write(b"\xf0\x9c+K")  # 0xf09c2b4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf09c2b4b))

        data.write(b"v\x08Y\xe5")  # 0x760859e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x760859e5))

        data.write(b"\xbdT\x8a@")  # 0xbd548a40
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbd548a40))

        data.write(b"\xc0\x12\xf1\x96")  # 0xc012f196
        data.write(b"\x00\x0c")  # size
        self.rotation_for_type3.to_stream(data, game)

        data.write(b"p\xbc\x90\xa6")  # 0x70bc90a6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x70bc90a6.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerControllerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            unknown_0xe71de331=json_data["unknown_0xe71de331"],
            model=json_data["model"],
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            proxy_type=json_data["proxy_type"],
            player_offset=Vector.from_json(json_data["player_offset"]),
            initial_state=json_data["initial_state"],
            player_visor=json_data["player_visor"],
            unknown_0xf09c2b4b=json_data["unknown_0xf09c2b4b"],
            unknown_0x760859e5=json_data["unknown_0x760859e5"],
            unknown_0xbd548a40=json_data["unknown_0xbd548a40"],
            rotation_for_type3=Vector.from_json(json_data["rotation_for_type3"]),
            unknown_0x70bc90a6=json_data["unknown_0x70bc90a6"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "unknown_0xe71de331": self.unknown_0xe71de331,
            "model": self.model,
            "animation_information": self.animation_information.to_json(),
            "actor_information": self.actor_information.to_json(),
            "proxy_type": self.proxy_type,
            "player_offset": self.player_offset.to_json(),
            "initial_state": self.initial_state,
            "player_visor": self.player_visor,
            "unknown_0xf09c2b4b": self.unknown_0xf09c2b4b,
            "unknown_0x760859e5": self.unknown_0x760859e5,
            "unknown_0xbd548a40": self.unknown_0xbd548a40,
            "rotation_for_type3": self.rotation_for_type3.to_json(),
            "unknown_0x70bc90a6": self.unknown_0x70bc90a6,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PlayerController.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_player_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_rotation_for_type3(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0x70bc90a6(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xE71DE331: ("unknown_0xe71de331", structs.decode_BIG_l),
    0xC27FFA8F: ("model", structs.decode_BIG_L),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xCA56A18A: ("proxy_type", structs.decode_BIG_l),
    0x1D8B933F: ("player_offset", _decode_player_offset),
    0xCB753319: ("initial_state", structs.decode_BIG_l),
    0xD9C09CF7: ("player_visor", structs.decode_BIG_l),
    0xF09C2B4B: ("unknown_0xf09c2b4b", structs.decode_BIG_f),
    0x760859E5: ("unknown_0x760859e5", structs.decode_BIG_f),
    0xBD548A40: ("unknown_0xbd548a40", structs.decode_BIG_f),
    0xC012F196: ("rotation_for_type3", _decode_rotation_for_type3),
    0x70BC90A6: ("unknown_0x70bc90a6", _decode_unknown_0x70bc90a6),
}
