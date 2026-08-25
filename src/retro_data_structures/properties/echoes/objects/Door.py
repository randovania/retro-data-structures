# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.archetypes.ScannableParameters import ScannableParameters
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

    class DoorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        animation_information: json_util.JsonObject
        shell_model: int
        blue_shell_model: int
        shell_color: json_util.JsonValue
        burn_texture: int
        actor_information: json_util.JsonObject
        orbit_offset: json_util.JsonValue
        is_open: bool
        is_locked: bool
        open_animation_time: float
        close_animation_time: float
        close_delay: float
        shield_fade_out_time: float
        shield_fade_in_time: float
        morph_ball_tunnel: bool
        horizontal: bool
        alt_scannable: json_util.JsonObject


@dataclasses.dataclass()
class Door(BaseObjectType):
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
    collision_box: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xF344C0B0, original_name="CollisionBox", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x2E686C2A,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xCF90D15E,
                original_name="Health",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x7B71AE90,
                original_name="Vulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
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
    shell_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB20CC271, original_name="ShellModel"),
        },
    )
    blue_shell_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAE5B2114, original_name="BlueShellModel"),
        },
    )
    shell_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x47B4E863, original_name="ShellColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    burn_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2589C3F0, original_name="BurnTexture"),
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
    orbit_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x850115E4, original_name="OrbitOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    is_open: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA1DFFAD2, original_name="IsOpen"),
        },
    )
    is_locked: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xDEE730F5, original_name="IsLocked"),
        },
    )
    open_animation_time: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2007B71D, original_name="OpenAnimationTime"),
        },
    )
    close_animation_time: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF1A50D29, original_name="CloseAnimationTime"),
        },
    )
    close_delay: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x06DCF118, original_name="CloseDelay"),
        },
    )
    shield_fade_out_time: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5DCF0A64, original_name="ShieldFadeOutTime"),
        },
    )
    shield_fade_in_time: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCDCA592B, original_name="ShieldFadeInTime"),
        },
    )
    morph_ball_tunnel: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCC009F35, original_name="MorphBallTunnel"),
        },
    )
    horizontal: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC29765EA, original_name="Horizontal"),
        },
    )
    alt_scannable: ScannableParameters = dataclasses.field(
        default_factory=ScannableParameters,
        metadata={
            "reflection": FieldReflection[ScannableParameters](
                ScannableParameters,
                id=0x9EC62712,
                original_name="AltScannable",
                from_json=ScannableParameters.from_json,
                to_json=ScannableParameters.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DOOR"

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
        if property_count != 22:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF344C0B0
        collision_box = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E686C2A
        collision_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB20CC271
        shell_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE5B2114
        blue_shell_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47B4E863
        shell_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2589C3F0
        burn_texture = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x850115E4
        orbit_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1DFFAD2
        is_open = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDEE730F5
        is_locked = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2007B71D
        open_animation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1A50D29
        close_animation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06DCF118
        close_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5DCF0A64
        shield_fade_out_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCDCA592B
        shield_fade_in_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC009F35
        morph_ball_tunnel = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC29765EA
        horizontal = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9EC62712
        alt_scannable = ScannableParameters.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            collision_box,
            collision_offset,
            health,
            vulnerability,
            animation_information,
            shell_model,
            blue_shell_model,
            shell_color,
            burn_texture,
            actor_information,
            orbit_offset,
            is_open,
            is_locked,
            open_animation_time,
            close_animation_time,
            close_delay,
            shield_fade_out_time,
            shield_fade_in_time,
            morph_ball_tunnel,
            horizontal,
            alt_scannable,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x16")  # 22 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3D\xc0\xb0")  # 0xf344c0b0
        data.write(b"\x00\x0c")  # size
        self.collision_box.to_stream(data, game)

        data.write(b".hl*")  # 0x2e686c2a
        data.write(b"\x00\x0c")  # size
        self.collision_offset.to_stream(data, game)

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{q\xae\x90")  # 0x7b71ae90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vulnerability.to_stream(data, game)
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

        data.write(b"\xb2\x0c\xc2q")  # 0xb20cc271
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shell_model))

        data.write(b"\xae[!\x14")  # 0xae5b2114
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.blue_shell_model))

        data.write(b"G\xb4\xe8c")  # 0x47b4e863
        data.write(b"\x00\x10")  # size
        self.shell_color.to_stream(data, game)

        data.write(b"%\x89\xc3\xf0")  # 0x2589c3f0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.burn_texture))

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x85\x01\x15\xe4")  # 0x850115e4
        data.write(b"\x00\x0c")  # size
        self.orbit_offset.to_stream(data, game)

        data.write(b"\xa1\xdf\xfa\xd2")  # 0xa1dffad2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_open))

        data.write(b"\xde\xe70\xf5")  # 0xdee730f5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_locked))

        data.write(b" \x07\xb7\x1d")  # 0x2007b71d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.open_animation_time))

        data.write(b"\xf1\xa5\r)")  # 0xf1a50d29
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.close_animation_time))

        data.write(b"\x06\xdc\xf1\x18")  # 0x6dcf118
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.close_delay))

        data.write(b"]\xcf\nd")  # 0x5dcf0a64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shield_fade_out_time))

        data.write(b"\xcd\xcaY+")  # 0xcdca592b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shield_fade_in_time))

        data.write(b"\xcc\x00\x9f5")  # 0xcc009f35
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.morph_ball_tunnel))

        data.write(b"\xc2\x97e\xea")  # 0xc29765ea
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.horizontal))

        data.write(b"\x9e\xc6'\x12")  # 0x9ec62712
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.alt_scannable.to_stream(data, game)
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
        json_data = typing.cast("DoorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            shell_model=json_data["shell_model"],
            blue_shell_model=json_data["blue_shell_model"],
            shell_color=Color.from_json(json_data["shell_color"]),
            burn_texture=json_data["burn_texture"],
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            orbit_offset=Vector.from_json(json_data["orbit_offset"]),
            is_open=json_data["is_open"],
            is_locked=json_data["is_locked"],
            open_animation_time=json_data["open_animation_time"],
            close_animation_time=json_data["close_animation_time"],
            close_delay=json_data["close_delay"],
            shield_fade_out_time=json_data["shield_fade_out_time"],
            shield_fade_in_time=json_data["shield_fade_in_time"],
            morph_ball_tunnel=json_data["morph_ball_tunnel"],
            horizontal=json_data["horizontal"],
            alt_scannable=ScannableParameters.from_json(json_data["alt_scannable"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "animation_information": self.animation_information.to_json(),
            "shell_model": self.shell_model,
            "blue_shell_model": self.blue_shell_model,
            "shell_color": self.shell_color.to_json(),
            "burn_texture": self.burn_texture,
            "actor_information": self.actor_information.to_json(),
            "orbit_offset": self.orbit_offset.to_json(),
            "is_open": self.is_open,
            "is_locked": self.is_locked,
            "open_animation_time": self.open_animation_time,
            "close_animation_time": self.close_animation_time,
            "close_delay": self.close_delay,
            "shield_fade_out_time": self.shield_fade_out_time,
            "shield_fade_in_time": self.shield_fade_in_time,
            "morph_ball_tunnel": self.morph_ball_tunnel,
            "horizontal": self.horizontal,
            "alt_scannable": self.alt_scannable.to_json(),
        }

    def _dependencies_for_shell_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shell_model)

    def _dependencies_for_blue_shell_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.blue_shell_model)

    def _dependencies_for_burn_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.burn_texture)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self._dependencies_for_shell_model, "shell_model", "AssetId"),
            (self._dependencies_for_blue_shell_model, "blue_shell_model", "AssetId"),
            (self._dependencies_for_burn_texture, "burn_texture", "AssetId"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.alt_scannable.dependencies_for, "alt_scannable", "ScannableParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Door.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_shell_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_orbit_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_alt_scannable(data: typing.BinaryIO, game: Game, property_size: int) -> ScannableParameters:
    return ScannableParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xF344C0B0: ("collision_box", _decode_collision_box),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0xB20CC271: ("shell_model", structs.decode_BIG_L),
    0xAE5B2114: ("blue_shell_model", structs.decode_BIG_L),
    0x47B4E863: ("shell_color", _decode_shell_color),
    0x2589C3F0: ("burn_texture", structs.decode_BIG_L),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x850115E4: ("orbit_offset", _decode_orbit_offset),
    0xA1DFFAD2: ("is_open", structs.decode_BIG_bool_),
    0xDEE730F5: ("is_locked", structs.decode_BIG_bool_),
    0x2007B71D: ("open_animation_time", structs.decode_BIG_f),
    0xF1A50D29: ("close_animation_time", structs.decode_BIG_f),
    0x06DCF118: ("close_delay", structs.decode_BIG_f),
    0x5DCF0A64: ("shield_fade_out_time", structs.decode_BIG_f),
    0xCDCA592B: ("shield_fade_in_time", structs.decode_BIG_f),
    0xCC009F35: ("morph_ball_tunnel", structs.decode_BIG_bool_),
    0xC29765EA: ("horizontal", structs.decode_BIG_bool_),
    0x9EC62712: ("alt_scannable", _decode_alt_scannable),
}
