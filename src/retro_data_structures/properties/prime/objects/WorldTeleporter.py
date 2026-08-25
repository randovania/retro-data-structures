# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class WorldTeleporterJson(typing_extensions.TypedDict):
        name: str
        active: bool
        world_id: int
        area_id: int
        player_model: json_util.JsonObject
        player_scale: json_util.JsonValue
        platform_model: int
        platform_scale: json_util.JsonValue
        background_model: int
        background_scale: json_util.JsonValue
        up_elevator: bool
        elevator_sound: int
        volume: int
        panning: int
        show_text: bool
        font_id: int
        string_id: int
        fade_white: bool
        char_fade_in_time: float
        char_fade_out_time: float
        show_delay: float


@dataclasses.dataclass()
class WorldTeleporter(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="Active"),
        },
    )
    world_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["MLVL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000002, original_name="WorldID"),
        },
    )
    area_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["MREA"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000003, original_name="AreaID"),
        },
    )
    player_model: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000004,
                original_name="Player Model",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    player_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000005, original_name="PlayerScale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    platform_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000006, original_name="PlatformModel"),
        },
    )
    platform_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000007, original_name="PlatformScale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    background_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="BackgroundModel"),
        },
    )
    background_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000009,
                original_name="BackgroundScale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    up_elevator: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="UpElevator"),
        },
    )
    elevator_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000000B, original_name="ElevatorSound"),
        },
    )
    volume: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000C, original_name="Volume"),
        },
    )
    panning: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000D, original_name="Panning"),
        },
    )
    show_text: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="ShowText"),
        },
    )
    font_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["FONT"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000F, original_name="FontID"),
        },
    )
    string_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["STRG"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000010, original_name="StringID"),
        },
    )
    fade_white: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000011, original_name="FadeWhite"),
        },
    )
    char_fade_in_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="CharFadeInTime"),
        },
    )
    char_fade_out_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="CharFadeOutTime"),
        },
    )
    show_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="ShowDelay"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x62

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        world_id = structs.BIG_L.unpack(data.read(4))[0]
        area_id = structs.BIG_L.unpack(data.read(4))[0]
        player_model = AnimationParameters.from_stream(data, game, property_size)
        player_scale = Vector.from_stream(data, game, property_size)
        platform_model = structs.BIG_L.unpack(data.read(4))[0]
        platform_scale = Vector.from_stream(data, game, property_size)
        background_model = structs.BIG_L.unpack(data.read(4))[0]
        background_scale = Vector.from_stream(data, game, property_size)
        up_elevator = structs.BIG_bool_.unpack(data.read(1))[0]
        elevator_sound = structs.BIG_l.unpack(data.read(4))[0]
        volume = structs.BIG_l.unpack(data.read(4))[0]
        panning = structs.BIG_l.unpack(data.read(4))[0]
        show_text = structs.BIG_bool_.unpack(data.read(1))[0]
        font_id = structs.BIG_L.unpack(data.read(4))[0]
        string_id = structs.BIG_L.unpack(data.read(4))[0]
        fade_white = structs.BIG_bool_.unpack(data.read(1))[0]
        char_fade_in_time = structs.BIG_f.unpack(data.read(4))[0]
        char_fade_out_time = structs.BIG_f.unpack(data.read(4))[0]
        show_delay = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            active,
            world_id,
            area_id,
            player_model,
            player_scale,
            platform_model,
            platform_scale,
            background_model,
            background_scale,
            up_elevator,
            elevator_sound,
            volume,
            panning,
            show_text,
            font_id,
            string_id,
            fade_white,
            char_fade_in_time,
            char_fade_out_time,
            show_delay,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x15")  # 21 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_L.pack(self.world_id))
        data.write(structs.BIG_L.pack(self.area_id))
        self.player_model.to_stream(data, game)
        self.player_scale.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.platform_model))
        self.platform_scale.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.background_model))
        self.background_scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.up_elevator))
        data.write(structs.BIG_l.pack(self.elevator_sound))
        data.write(structs.BIG_l.pack(self.volume))
        data.write(structs.BIG_l.pack(self.panning))
        data.write(structs.BIG_bool_.pack(self.show_text))
        data.write(structs.BIG_L.pack(self.font_id))
        data.write(structs.BIG_L.pack(self.string_id))
        data.write(structs.BIG_bool_.pack(self.fade_white))
        data.write(structs.BIG_f.pack(self.char_fade_in_time))
        data.write(structs.BIG_f.pack(self.char_fade_out_time))
        data.write(structs.BIG_f.pack(self.show_delay))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WorldTeleporterJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            world_id=json_data["world_id"],
            area_id=json_data["area_id"],
            player_model=AnimationParameters.from_json(json_data["player_model"]),
            player_scale=Vector.from_json(json_data["player_scale"]),
            platform_model=json_data["platform_model"],
            platform_scale=Vector.from_json(json_data["platform_scale"]),
            background_model=json_data["background_model"],
            background_scale=Vector.from_json(json_data["background_scale"]),
            up_elevator=json_data["up_elevator"],
            elevator_sound=json_data["elevator_sound"],
            volume=json_data["volume"],
            panning=json_data["panning"],
            show_text=json_data["show_text"],
            font_id=json_data["font_id"],
            string_id=json_data["string_id"],
            fade_white=json_data["fade_white"],
            char_fade_in_time=json_data["char_fade_in_time"],
            char_fade_out_time=json_data["char_fade_out_time"],
            show_delay=json_data["show_delay"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "world_id": self.world_id,
            "area_id": self.area_id,
            "player_model": self.player_model.to_json(),
            "player_scale": self.player_scale.to_json(),
            "platform_model": self.platform_model,
            "platform_scale": self.platform_scale.to_json(),
            "background_model": self.background_model,
            "background_scale": self.background_scale.to_json(),
            "up_elevator": self.up_elevator,
            "elevator_sound": self.elevator_sound,
            "volume": self.volume,
            "panning": self.panning,
            "show_text": self.show_text,
            "font_id": self.font_id,
            "string_id": self.string_id,
            "fade_white": self.fade_white,
            "char_fade_in_time": self.char_fade_in_time,
            "char_fade_out_time": self.char_fade_out_time,
            "show_delay": self.show_delay,
        }

    def _dependencies_for_platform_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.platform_model)

    def _dependencies_for_background_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.background_model)

    def _dependencies_for_elevator_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.elevator_sound)

    def _dependencies_for_font_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.font_id)

    def _dependencies_for_string_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.string_id)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.player_model.dependencies_for, "player_model", "AnimationParameters"),
            (self._dependencies_for_platform_model, "platform_model", "AssetId"),
            (self._dependencies_for_background_model, "background_model", "AssetId"),
            (self._dependencies_for_elevator_sound, "elevator_sound", "int"),
            (self._dependencies_for_font_id, "font_id", "AssetId"),
            (self._dependencies_for_string_id, "string_id", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for WorldTeleporter.{field_name} ({field_type}): {e}")
