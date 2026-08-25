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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.EchoParameters import EchoParameters
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
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

    class ActorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        mass: float
        gravity: float
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        model: int
        collision_model: int
        animation_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        echo_information: json_util.JsonObject
        is_loop: bool
        immovable: bool
        is_solid: bool
        is_camera_through: bool
        is_scan_through: bool
        render_texture_set: int
        draws_shadow: bool
        scale_animation: bool
        ai_shoot_through: bool
        random_animation_offset: float
        projectile: int
        projectile_damage: json_util.JsonObject


@dataclasses.dataclass()
class Actor(BaseObjectType):
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
    mass: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75DBB375, original_name="Mass"),
        },
    )
    gravity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2F2AE3E5, original_name="Gravity"),
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
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC27FFA8F, original_name="Model"),
        },
    )
    collision_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["DCLN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0FC966DC, original_name="CollisionModel"),
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
    echo_information: EchoParameters = dataclasses.field(
        default_factory=EchoParameters,
        metadata={
            "reflection": FieldReflection[EchoParameters](
                EchoParameters,
                id=0x192B0E70,
                original_name="EchoInformation",
                from_json=EchoParameters.from_json,
                to_json=EchoParameters.to_json,
            ),
        },
    )
    is_loop: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC08D1B93, original_name="IsLoop"),
        },
    )
    immovable: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1E32523E, original_name="Immovable"),
        },
    )
    is_solid: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1D8DD846, original_name="IsSolid"),
        },
    )
    is_camera_through: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7859B520, original_name="IsCameraThrough"),
        },
    )
    is_scan_through: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2AFFD6FE, original_name="IsScanThrough"),
        },
    )
    render_texture_set: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x32FAB97E, original_name="RenderTextureSet"),
        },
    )
    draws_shadow: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x97687446, original_name="DrawsShadow"),
        },
    )
    scale_animation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x261E92A4, original_name="ScaleAnimation"),
        },
    )
    ai_shoot_through: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCC27F827, original_name="AiShootThrough"),
        },
    )
    random_animation_offset: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBF69C03E, original_name="RandomAnimationOffset"),
        },
    )
    projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEF485DB9, original_name="Projectile"),
        },
    )
    projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x553B1339,
                original_name="ProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "ACTR"

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
        if property_count != 24:
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
        assert property_id == 0x75DBB375
        mass = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F2AE3E5
        gravity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FC966DC
        collision_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x192B0E70
        echo_information = EchoParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC08D1B93
        is_loop = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E32523E
        immovable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D8DD846
        is_solid = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7859B520
        is_camera_through = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2AFFD6FE
        is_scan_through = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32FAB97E
        render_texture_set = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97687446
        draws_shadow = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x261E92A4
        scale_animation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC27F827
        ai_shoot_through = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF69C03E
        random_animation_offset = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF485DB9
        projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553B1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11})

        return cls(
            editor_properties,
            collision_box,
            collision_offset,
            mass,
            gravity,
            health,
            vulnerability,
            model,
            collision_model,
            animation_information,
            actor_information,
            echo_information,
            is_loop,
            immovable,
            is_solid,
            is_camera_through,
            is_scan_through,
            render_texture_set,
            draws_shadow,
            scale_animation,
            ai_shoot_through,
            random_animation_offset,
            projectile,
            projectile_damage,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x17")  # 23 properties
        num_properties_written = 23

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

        data.write(b"u\xdb\xb3u")  # 0x75dbb375
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mass))

        data.write(b"/*\xe3\xe5")  # 0x2f2ae3e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity))

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

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.model))

        data.write(b"\x0f\xc9f\xdc")  # 0xfc966dc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.collision_model))

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

        data.write(b"\x19+\x0ep")  # 0x192b0e70
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.echo_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc0\x8d\x1b\x93")  # 0xc08d1b93
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_loop))

        data.write(b"\x1e2R>")  # 0x1e32523e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.immovable))

        data.write(b"\x1d\x8d\xd8F")  # 0x1d8dd846
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_solid))

        data.write(b"xY\xb5 ")  # 0x7859b520
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_camera_through))

        if self.is_scan_through != default_override.get("is_scan_through", False):
            num_properties_written += 1
            data.write(b"*\xff\xd6\xfe")  # 0x2affd6fe
            data.write(b"\x00\x01")  # size
            data.write(structs.BIG_bool_.pack(self.is_scan_through))

        data.write(b"2\xfa\xb9~")  # 0x32fab97e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.render_texture_set))

        data.write(b"\x97htF")  # 0x97687446
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.draws_shadow))

        data.write(b"&\x1e\x92\xa4")  # 0x261e92a4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scale_animation))

        data.write(b"\xcc'\xf8'")  # 0xcc27f827
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ai_shoot_through))

        data.write(b"\xbfi\xc0>")  # 0xbf69c03e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.random_animation_offset))

        data.write(b"\xefH]\xb9")  # 0xef485db9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b"U;\x139")  # 0x553b1339
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_damage.to_stream(data, game, default_override={"di_weapon_type": 11})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            mass=json_data["mass"],
            gravity=json_data["gravity"],
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            model=json_data["model"],
            collision_model=json_data["collision_model"],
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            echo_information=EchoParameters.from_json(json_data["echo_information"]),
            is_loop=json_data["is_loop"],
            immovable=json_data["immovable"],
            is_solid=json_data["is_solid"],
            is_camera_through=json_data["is_camera_through"],
            is_scan_through=json_data["is_scan_through"],
            render_texture_set=json_data["render_texture_set"],
            draws_shadow=json_data["draws_shadow"],
            scale_animation=json_data["scale_animation"],
            ai_shoot_through=json_data["ai_shoot_through"],
            random_animation_offset=json_data["random_animation_offset"],
            projectile=json_data["projectile"],
            projectile_damage=DamageInfo.from_json(json_data["projectile_damage"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "mass": self.mass,
            "gravity": self.gravity,
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "model": self.model,
            "collision_model": self.collision_model,
            "animation_information": self.animation_information.to_json(),
            "actor_information": self.actor_information.to_json(),
            "echo_information": self.echo_information.to_json(),
            "is_loop": self.is_loop,
            "immovable": self.immovable,
            "is_solid": self.is_solid,
            "is_camera_through": self.is_camera_through,
            "is_scan_through": self.is_scan_through,
            "render_texture_set": self.render_texture_set,
            "draws_shadow": self.draws_shadow,
            "scale_animation": self.scale_animation,
            "ai_shoot_through": self.ai_shoot_through,
            "random_animation_offset": self.random_animation_offset,
            "projectile": self.projectile,
            "projectile_damage": self.projectile_damage.to_json(),
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_collision_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.collision_model)

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self._dependencies_for_collision_model, "collision_model", "AssetId"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Actor.{field_name} ({field_type}): {e}")


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


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_echo_information(data: typing.BinaryIO, game: Game, property_size: int) -> EchoParameters:
    return EchoParameters.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xF344C0B0: ("collision_box", _decode_collision_box),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0x75DBB375: ("mass", structs.decode_BIG_f),
    0x2F2AE3E5: ("gravity", structs.decode_BIG_f),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0xC27FFA8F: ("model", structs.decode_BIG_L),
    0x0FC966DC: ("collision_model", structs.decode_BIG_L),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x192B0E70: ("echo_information", _decode_echo_information),
    0xC08D1B93: ("is_loop", structs.decode_BIG_bool_),
    0x1E32523E: ("immovable", structs.decode_BIG_bool_),
    0x1D8DD846: ("is_solid", structs.decode_BIG_bool_),
    0x7859B520: ("is_camera_through", structs.decode_BIG_bool_),
    0x2AFFD6FE: ("is_scan_through", structs.decode_BIG_bool_),
    0x32FAB97E: ("render_texture_set", structs.decode_BIG_l),
    0x97687446: ("draws_shadow", structs.decode_BIG_bool_),
    0x261E92A4: ("scale_animation", structs.decode_BIG_bool_),
    0xCC27F827: ("ai_shoot_through", structs.decode_BIG_bool_),
    0xBF69C03E: ("random_animation_offset", structs.decode_BIG_f),
    0xEF485DB9: ("projectile", structs.decode_BIG_L),
    0x553B1339: ("projectile_damage", _decode_projectile_damage),
}
