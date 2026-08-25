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
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.archetypes.PlatformMotionProperties import PlatformMotionProperties
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

    class PlatformJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        model: int
        animation_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        collision_model: int
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        x_ray_transparency: float
        maximum_splashes: int
        splash_generation_rate: int
        render_rain_splashes: bool
        unknown_0xf203bc81: bool
        motion_properties: json_util.JsonObject
        unknown_0x24fdeea1: json_util.JsonValue
        random_animation_offset: float


@dataclasses.dataclass()
class Platform(BaseObjectType):
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
    collision_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["DCLN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0FC966DC, original_name="CollisionModel"),
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
    x_ray_transparency: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6150D687, original_name="XRayTransparency"),
        },
    )
    maximum_splashes: int = dataclasses.field(
        default=200,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDCD56FE8, original_name="MaximumSplashes"),
        },
    )
    splash_generation_rate: int = dataclasses.field(
        default=20,
        metadata={
            "reflection": FieldReflection[int](int, id=0x682DE15C, original_name="SplashGenerationRate"),
        },
    )
    render_rain_splashes: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAC3ADDA6, original_name="RenderRainSplashes"),
        },
    )
    unknown_0xf203bc81: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF203BC81, original_name="Unknown"),
        },
    )
    motion_properties: PlatformMotionProperties = dataclasses.field(
        default_factory=PlatformMotionProperties,
        metadata={
            "reflection": FieldReflection[PlatformMotionProperties](
                PlatformMotionProperties,
                id=0x0A9DBF91,
                original_name="MotionProperties",
                from_json=PlatformMotionProperties.from_json,
                to_json=PlatformMotionProperties.to_json,
            ),
        },
    )
    unknown_0x24fdeea1: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.15000000596046448, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x24FDEEA1, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    random_animation_offset: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBF69C03E, original_name="RandomAnimationOffset"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PLAT"

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
        if property_count != 17:
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
        assert property_id == 0xC27FFA8F
        model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FC966DC
        collision_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6150D687
        x_ray_transparency = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCD56FE8
        maximum_splashes = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x682DE15C
        splash_generation_rate = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC3ADDA6
        render_rain_splashes = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF203BC81
        unknown_0xf203bc81 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A9DBF91
        motion_properties = PlatformMotionProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24FDEEA1
        unknown_0x24fdeea1 = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF69C03E
        random_animation_offset = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            collision_box,
            collision_offset,
            model,
            animation_information,
            actor_information,
            collision_model,
            health,
            vulnerability,
            x_ray_transparency,
            maximum_splashes,
            splash_generation_rate,
            render_rain_splashes,
            unknown_0xf203bc81,
            motion_properties,
            unknown_0x24fdeea1,
            random_animation_offset,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x11")  # 17 properties

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

        data.write(b"\x0f\xc9f\xdc")  # 0xfc966dc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.collision_model))

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

        data.write(b"aP\xd6\x87")  # 0x6150d687
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.x_ray_transparency))

        data.write(b"\xdc\xd5o\xe8")  # 0xdcd56fe8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.maximum_splashes))

        data.write(b"h-\xe1\\")  # 0x682de15c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.splash_generation_rate))

        data.write(b"\xac:\xdd\xa6")  # 0xac3adda6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.render_rain_splashes))

        data.write(b"\xf2\x03\xbc\x81")  # 0xf203bc81
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf203bc81))

        data.write(b"\n\x9d\xbf\x91")  # 0xa9dbf91
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"$\xfd\xee\xa1")  # 0x24fdeea1
        data.write(b"\x00\x0c")  # size
        self.unknown_0x24fdeea1.to_stream(data, game)

        data.write(b"\xbfi\xc0>")  # 0xbf69c03e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.random_animation_offset))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlatformJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            model=json_data["model"],
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            collision_model=json_data["collision_model"],
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            x_ray_transparency=json_data["x_ray_transparency"],
            maximum_splashes=json_data["maximum_splashes"],
            splash_generation_rate=json_data["splash_generation_rate"],
            render_rain_splashes=json_data["render_rain_splashes"],
            unknown_0xf203bc81=json_data["unknown_0xf203bc81"],
            motion_properties=PlatformMotionProperties.from_json(json_data["motion_properties"]),
            unknown_0x24fdeea1=Vector.from_json(json_data["unknown_0x24fdeea1"]),
            random_animation_offset=json_data["random_animation_offset"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "model": self.model,
            "animation_information": self.animation_information.to_json(),
            "actor_information": self.actor_information.to_json(),
            "collision_model": self.collision_model,
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "x_ray_transparency": self.x_ray_transparency,
            "maximum_splashes": self.maximum_splashes,
            "splash_generation_rate": self.splash_generation_rate,
            "render_rain_splashes": self.render_rain_splashes,
            "unknown_0xf203bc81": self.unknown_0xf203bc81,
            "motion_properties": self.motion_properties.to_json(),
            "unknown_0x24fdeea1": self.unknown_0x24fdeea1.to_json(),
            "random_animation_offset": self.random_animation_offset,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_collision_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.collision_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_collision_model, "collision_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Platform.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_motion_properties(data: typing.BinaryIO, game: Game, property_size: int) -> PlatformMotionProperties:
    return PlatformMotionProperties.from_stream(data, game, property_size)


def _decode_unknown_0x24fdeea1(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xF344C0B0: ("collision_box", _decode_collision_box),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0xC27FFA8F: ("model", structs.decode_BIG_L),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x0FC966DC: ("collision_model", structs.decode_BIG_L),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0x6150D687: ("x_ray_transparency", structs.decode_BIG_f),
    0xDCD56FE8: ("maximum_splashes", structs.decode_BIG_l),
    0x682DE15C: ("splash_generation_rate", structs.decode_BIG_l),
    0xAC3ADDA6: ("render_rain_splashes", structs.decode_BIG_bool_),
    0xF203BC81: ("unknown_0xf203bc81", structs.decode_BIG_bool_),
    0x0A9DBF91: ("motion_properties", _decode_motion_properties),
    0x24FDEEA1: ("unknown_0x24fdeea1", _decode_unknown_0x24fdeea1),
    0xBF69C03E: ("random_animation_offset", structs.decode_BIG_f),
}
