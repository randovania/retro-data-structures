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
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CoinJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        cone_spread: float
        minimum_speed: float
        maximum_speed: float
        minimum_spin_speed: float
        maximum_spin_speed: float
        minimum_life_time: float
        maximum_life_time: float
        disable_collision_time: float
        fade_in_end_percentage: float
        fade_out_start_percentage: float
        start_color: json_util.JsonValue
        end_color: json_util.JsonValue
        scale_start_percentage: float
        final_scale: json_util.JsonValue
        unknown_0x417f4a91: float
        gravity: float
        position_offset: json_util.JsonValue
        model: int
        actor_information: json_util.JsonObject
        particle1: int
        bounce_sound: int
        max_bounce_sounds: int
        unknown_0x76c79503: float
        unknown_0x310dfac8: float
        particle_system1_scale: json_util.JsonValue
        particle_system1_uses_global_translation: bool
        particle_system1_wait_for_particles_to_die: bool
        particle_system1_orientation: int
        particle2: int
        particle_system2_scale: json_util.JsonValue
        particle_system2_uses_global_translation: bool
        particle_system2_wait_for_particles_to_die: bool
        particle_system2_orientation: int
        death_particle: int
        death_particle_system_scale: json_util.JsonValue
        death_particle_system_orientation: int
        is_collider: bool
        is_shootable: bool
        die_on_collision: bool
        unknown_0xdcaa0f22: bool
        unknown_0xbfd82a19: bool
        unknown_0x723d42d6: bool
        disable_physics_threshold: float


@dataclasses.dataclass()
class Coin(BaseObjectType):
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
    cone_spread: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D6FC391, original_name="ConeSpread"),
        },
    )
    minimum_speed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0185263E, original_name="MinimumSpeed"),
        },
    )
    maximum_speed: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x140EF2CC, original_name="MaximumSpeed"),
        },
    )
    minimum_spin_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x863EBB76, original_name="MinimumSpinSpeed"),
        },
    )
    maximum_spin_speed: float = dataclasses.field(
        default=1.2000000476837158,
        metadata={
            "reflection": FieldReflection[float](float, id=0x957B5DDD, original_name="MaximumSpinSpeed"),
        },
    )
    minimum_life_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54A8C481, original_name="MinimumLifeTime"),
        },
    )
    maximum_life_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7DD63999, original_name="MaximumLifeTime"),
        },
    )
    disable_collision_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6B571BA5, original_name="DisableCollisionTime"),
        },
    )
    fade_in_end_percentage: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50051A17, original_name="FadeInEndPercentage"),
        },
    )
    fade_out_start_percentage: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6353C409, original_name="FadeOutStartPercentage"),
        },
    )
    start_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x3A5634D8, original_name="StartColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    end_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5AF5867D, original_name="EndColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    scale_start_percentage: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x886E7C9F, original_name="ScaleStartPercentage"),
        },
    )
    final_scale: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x80C22A0A, original_name="FinalScale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0x417f4a91: float = dataclasses.field(
        default=0.375,
        metadata={
            "reflection": FieldReflection[float](float, id=0x417F4A91, original_name="Unknown"),
        },
    )
    gravity: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2F2AE3E5, original_name="Gravity"),
        },
    )
    position_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xEF90F09D,
                original_name="PositionOffset",
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
    particle1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x41DD4D40, original_name="Particle1"),
        },
    )
    bounce_sound: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0BB3CCAE, original_name="BounceSound"),
        },
    )
    max_bounce_sounds: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x991202C3, original_name="MaxBounceSounds"),
        },
    )
    unknown_0x76c79503: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76C79503, original_name="Unknown"),
        },
    )
    unknown_0x310dfac8: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x310DFAC8, original_name="Unknown"),
        },
    )
    particle_system1_scale: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x19A6F71F,
                original_name="ParticleSystem1Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    particle_system1_uses_global_translation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0x3B03A01E, original_name="ParticleSystem1UsesGlobalTranslation"
            ),
        },
    )
    particle_system1_wait_for_particles_to_die: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0x3BDD2FED, original_name="ParticleSystem1WaitForParticlesToDie"
            ),
        },
    )
    particle_system1_orientation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x334A34BB, original_name="ParticleSystem1Orientation"),
        },
    )
    particle2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC7493FEE, original_name="Particle2"),
        },
    )
    particle_system2_scale: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x6E3825EF,
                original_name="ParticleSystem2Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    particle_system2_uses_global_translation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0xC9544DE6, original_name="ParticleSystem2UsesGlobalTranslation"
            ),
        },
    )
    particle_system2_wait_for_particles_to_die: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0xC98AC215, original_name="ParticleSystem2WaitForParticlesToDie"
            ),
        },
    )
    particle_system2_orientation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD9CCE9D9, original_name="ParticleSystem2Orientation"),
        },
    )
    death_particle: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x979042C8, original_name="DeathParticle"),
        },
    )
    death_particle_system_scale: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xE9214CD8,
                original_name="DeathParticleSystemScale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    death_particle_system_orientation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9DFADEE0, original_name="DeathParticleSystemOrientation"),
        },
    )
    is_collider: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2C7B18DD, original_name="IsCollider"),
        },
    )
    is_shootable: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8C73CB7C, original_name="IsShootable"),
        },
    )
    die_on_collision: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0D7FAD55, original_name="DieOnCollision"),
        },
    )
    unknown_0xdcaa0f22: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xDCAA0F22, original_name="Unknown"),
        },
    )
    unknown_0xbfd82a19: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBFD82A19, original_name="Unknown"),
        },
    )
    unknown_0x723d42d6: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x723D42D6, original_name="Unknown"),
        },
    )
    disable_physics_threshold: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x295F05B7, original_name="DisablePhysicsThreshold"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "COIN"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ScriptCoin.rel"]

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
        if property_count != 44:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={"active": False})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D6FC391
        cone_spread = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0185263E
        minimum_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x140EF2CC
        maximum_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x863EBB76
        minimum_spin_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x957B5DDD
        maximum_spin_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54A8C481
        minimum_life_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7DD63999
        maximum_life_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6B571BA5
        disable_collision_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50051A17
        fade_in_end_percentage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6353C409
        fade_out_start_percentage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A5634D8
        start_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5AF5867D
        end_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x886E7C9F
        scale_start_percentage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80C22A0A
        final_scale = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x417F4A91
        unknown_0x417f4a91 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F2AE3E5
        gravity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF90F09D
        position_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41DD4D40
        particle1 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0BB3CCAE
        bounce_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x991202C3
        max_bounce_sounds = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76C79503
        unknown_0x76c79503 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x310DFAC8
        unknown_0x310dfac8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19A6F71F
        particle_system1_scale = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3B03A01E
        particle_system1_uses_global_translation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3BDD2FED
        particle_system1_wait_for_particles_to_die = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x334A34BB
        particle_system1_orientation = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7493FEE
        particle2 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E3825EF
        particle_system2_scale = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9544DE6
        particle_system2_uses_global_translation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC98AC215
        particle_system2_wait_for_particles_to_die = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD9CCE9D9
        particle_system2_orientation = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x979042C8
        death_particle = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9214CD8
        death_particle_system_scale = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9DFADEE0
        death_particle_system_orientation = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C7B18DD
        is_collider = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8C73CB7C
        is_shootable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D7FAD55
        die_on_collision = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCAA0F22
        unknown_0xdcaa0f22 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFD82A19
        unknown_0xbfd82a19 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723D42D6
        unknown_0x723d42d6 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x295F05B7
        disable_physics_threshold = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            cone_spread,
            minimum_speed,
            maximum_speed,
            minimum_spin_speed,
            maximum_spin_speed,
            minimum_life_time,
            maximum_life_time,
            disable_collision_time,
            fade_in_end_percentage,
            fade_out_start_percentage,
            start_color,
            end_color,
            scale_start_percentage,
            final_scale,
            unknown_0x417f4a91,
            gravity,
            position_offset,
            model,
            actor_information,
            particle1,
            bounce_sound,
            max_bounce_sounds,
            unknown_0x76c79503,
            unknown_0x310dfac8,
            particle_system1_scale,
            particle_system1_uses_global_translation,
            particle_system1_wait_for_particles_to_die,
            particle_system1_orientation,
            particle2,
            particle_system2_scale,
            particle_system2_uses_global_translation,
            particle_system2_wait_for_particles_to_die,
            particle_system2_orientation,
            death_particle,
            death_particle_system_scale,
            death_particle_system_orientation,
            is_collider,
            is_shootable,
            die_on_collision,
            unknown_0xdcaa0f22,
            unknown_0xbfd82a19,
            unknown_0x723d42d6,
            disable_physics_threshold,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00,")  # 44 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={"active": False})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8do\xc3\x91")  # 0x8d6fc391
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cone_spread))

        data.write(b"\x01\x85&>")  # 0x185263e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.minimum_speed))

        data.write(b"\x14\x0e\xf2\xcc")  # 0x140ef2cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maximum_speed))

        data.write(b"\x86>\xbbv")  # 0x863ebb76
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.minimum_spin_speed))

        data.write(b"\x95{]\xdd")  # 0x957b5ddd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maximum_spin_speed))

        data.write(b"T\xa8\xc4\x81")  # 0x54a8c481
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.minimum_life_time))

        data.write(b"}\xd69\x99")  # 0x7dd63999
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maximum_life_time))

        data.write(b"kW\x1b\xa5")  # 0x6b571ba5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.disable_collision_time))

        data.write(b"P\x05\x1a\x17")  # 0x50051a17
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_in_end_percentage))

        data.write(b"cS\xc4\t")  # 0x6353c409
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_start_percentage))

        data.write(b":V4\xd8")  # 0x3a5634d8
        data.write(b"\x00\x10")  # size
        self.start_color.to_stream(data, game)

        data.write(b"Z\xf5\x86}")  # 0x5af5867d
        data.write(b"\x00\x10")  # size
        self.end_color.to_stream(data, game)

        data.write(b"\x88n|\x9f")  # 0x886e7c9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scale_start_percentage))

        data.write(b"\x80\xc2*\n")  # 0x80c22a0a
        data.write(b"\x00\x0c")  # size
        self.final_scale.to_stream(data, game)

        data.write(b"A\x7fJ\x91")  # 0x417f4a91
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x417f4a91))

        data.write(b"/*\xe3\xe5")  # 0x2f2ae3e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity))

        data.write(b"\xef\x90\xf0\x9d")  # 0xef90f09d
        data.write(b"\x00\x0c")  # size
        self.position_offset.to_stream(data, game)

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.model))

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"A\xddM@")  # 0x41dd4d40
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.particle1))

        data.write(b"\x0b\xb3\xcc\xae")  # 0xbb3ccae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.bounce_sound))

        data.write(b"\x99\x12\x02\xc3")  # 0x991202c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_bounce_sounds))

        data.write(b"v\xc7\x95\x03")  # 0x76c79503
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76c79503))

        data.write(b"1\r\xfa\xc8")  # 0x310dfac8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x310dfac8))

        data.write(b"\x19\xa6\xf7\x1f")  # 0x19a6f71f
        data.write(b"\x00\x0c")  # size
        self.particle_system1_scale.to_stream(data, game)

        data.write(b";\x03\xa0\x1e")  # 0x3b03a01e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_uses_global_translation))

        data.write(b";\xdd/\xed")  # 0x3bdd2fed
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_wait_for_particles_to_die))

        data.write(b"3J4\xbb")  # 0x334a34bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.particle_system1_orientation))

        data.write(b"\xc7I?\xee")  # 0xc7493fee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.particle2))

        data.write(b"n8%\xef")  # 0x6e3825ef
        data.write(b"\x00\x0c")  # size
        self.particle_system2_scale.to_stream(data, game)

        data.write(b"\xc9TM\xe6")  # 0xc9544de6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_uses_global_translation))

        data.write(b"\xc9\x8a\xc2\x15")  # 0xc98ac215
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_wait_for_particles_to_die))

        data.write(b"\xd9\xcc\xe9\xd9")  # 0xd9cce9d9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.particle_system2_orientation))

        data.write(b"\x97\x90B\xc8")  # 0x979042c8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.death_particle))

        data.write(b"\xe9!L\xd8")  # 0xe9214cd8
        data.write(b"\x00\x0c")  # size
        self.death_particle_system_scale.to_stream(data, game)

        data.write(b"\x9d\xfa\xde\xe0")  # 0x9dfadee0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.death_particle_system_orientation))

        data.write(b",{\x18\xdd")  # 0x2c7b18dd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_collider))

        data.write(b"\x8cs\xcb|")  # 0x8c73cb7c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_shootable))

        data.write(b"\r\x7f\xadU")  # 0xd7fad55
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.die_on_collision))

        data.write(b'\xdc\xaa\x0f"')  # 0xdcaa0f22
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xdcaa0f22))

        data.write(b"\xbf\xd8*\x19")  # 0xbfd82a19
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbfd82a19))

        data.write(b"r=B\xd6")  # 0x723d42d6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x723d42d6))

        data.write(b")_\x05\xb7")  # 0x295f05b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.disable_physics_threshold))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CoinJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            cone_spread=json_data["cone_spread"],
            minimum_speed=json_data["minimum_speed"],
            maximum_speed=json_data["maximum_speed"],
            minimum_spin_speed=json_data["minimum_spin_speed"],
            maximum_spin_speed=json_data["maximum_spin_speed"],
            minimum_life_time=json_data["minimum_life_time"],
            maximum_life_time=json_data["maximum_life_time"],
            disable_collision_time=json_data["disable_collision_time"],
            fade_in_end_percentage=json_data["fade_in_end_percentage"],
            fade_out_start_percentage=json_data["fade_out_start_percentage"],
            start_color=Color.from_json(json_data["start_color"]),
            end_color=Color.from_json(json_data["end_color"]),
            scale_start_percentage=json_data["scale_start_percentage"],
            final_scale=Vector.from_json(json_data["final_scale"]),
            unknown_0x417f4a91=json_data["unknown_0x417f4a91"],
            gravity=json_data["gravity"],
            position_offset=Vector.from_json(json_data["position_offset"]),
            model=json_data["model"],
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            particle1=json_data["particle1"],
            bounce_sound=json_data["bounce_sound"],
            max_bounce_sounds=json_data["max_bounce_sounds"],
            unknown_0x76c79503=json_data["unknown_0x76c79503"],
            unknown_0x310dfac8=json_data["unknown_0x310dfac8"],
            particle_system1_scale=Vector.from_json(json_data["particle_system1_scale"]),
            particle_system1_uses_global_translation=json_data["particle_system1_uses_global_translation"],
            particle_system1_wait_for_particles_to_die=json_data["particle_system1_wait_for_particles_to_die"],
            particle_system1_orientation=json_data["particle_system1_orientation"],
            particle2=json_data["particle2"],
            particle_system2_scale=Vector.from_json(json_data["particle_system2_scale"]),
            particle_system2_uses_global_translation=json_data["particle_system2_uses_global_translation"],
            particle_system2_wait_for_particles_to_die=json_data["particle_system2_wait_for_particles_to_die"],
            particle_system2_orientation=json_data["particle_system2_orientation"],
            death_particle=json_data["death_particle"],
            death_particle_system_scale=Vector.from_json(json_data["death_particle_system_scale"]),
            death_particle_system_orientation=json_data["death_particle_system_orientation"],
            is_collider=json_data["is_collider"],
            is_shootable=json_data["is_shootable"],
            die_on_collision=json_data["die_on_collision"],
            unknown_0xdcaa0f22=json_data["unknown_0xdcaa0f22"],
            unknown_0xbfd82a19=json_data["unknown_0xbfd82a19"],
            unknown_0x723d42d6=json_data["unknown_0x723d42d6"],
            disable_physics_threshold=json_data["disable_physics_threshold"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "cone_spread": self.cone_spread,
            "minimum_speed": self.minimum_speed,
            "maximum_speed": self.maximum_speed,
            "minimum_spin_speed": self.minimum_spin_speed,
            "maximum_spin_speed": self.maximum_spin_speed,
            "minimum_life_time": self.minimum_life_time,
            "maximum_life_time": self.maximum_life_time,
            "disable_collision_time": self.disable_collision_time,
            "fade_in_end_percentage": self.fade_in_end_percentage,
            "fade_out_start_percentage": self.fade_out_start_percentage,
            "start_color": self.start_color.to_json(),
            "end_color": self.end_color.to_json(),
            "scale_start_percentage": self.scale_start_percentage,
            "final_scale": self.final_scale.to_json(),
            "unknown_0x417f4a91": self.unknown_0x417f4a91,
            "gravity": self.gravity,
            "position_offset": self.position_offset.to_json(),
            "model": self.model,
            "actor_information": self.actor_information.to_json(),
            "particle1": self.particle1,
            "bounce_sound": self.bounce_sound,
            "max_bounce_sounds": self.max_bounce_sounds,
            "unknown_0x76c79503": self.unknown_0x76c79503,
            "unknown_0x310dfac8": self.unknown_0x310dfac8,
            "particle_system1_scale": self.particle_system1_scale.to_json(),
            "particle_system1_uses_global_translation": self.particle_system1_uses_global_translation,
            "particle_system1_wait_for_particles_to_die": self.particle_system1_wait_for_particles_to_die,
            "particle_system1_orientation": self.particle_system1_orientation,
            "particle2": self.particle2,
            "particle_system2_scale": self.particle_system2_scale.to_json(),
            "particle_system2_uses_global_translation": self.particle_system2_uses_global_translation,
            "particle_system2_wait_for_particles_to_die": self.particle_system2_wait_for_particles_to_die,
            "particle_system2_orientation": self.particle_system2_orientation,
            "death_particle": self.death_particle,
            "death_particle_system_scale": self.death_particle_system_scale.to_json(),
            "death_particle_system_orientation": self.death_particle_system_orientation,
            "is_collider": self.is_collider,
            "is_shootable": self.is_shootable,
            "die_on_collision": self.die_on_collision,
            "unknown_0xdcaa0f22": self.unknown_0xdcaa0f22,
            "unknown_0xbfd82a19": self.unknown_0xbfd82a19,
            "unknown_0x723d42d6": self.unknown_0x723d42d6,
            "disable_physics_threshold": self.disable_physics_threshold,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_particle1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle1)

    def _dependencies_for_particle2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle2)

    def _dependencies_for_death_particle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_particle)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_particle1, "particle1", "AssetId"),
            (self._dependencies_for_particle2, "particle2", "AssetId"),
            (self._dependencies_for_death_particle, "death_particle", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Coin.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={"active": False})


def _decode_start_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_end_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_final_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_position_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_particle_system1_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_particle_system2_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_death_particle_system_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x8D6FC391: ("cone_spread", structs.decode_BIG_f),
    0x0185263E: ("minimum_speed", structs.decode_BIG_f),
    0x140EF2CC: ("maximum_speed", structs.decode_BIG_f),
    0x863EBB76: ("minimum_spin_speed", structs.decode_BIG_f),
    0x957B5DDD: ("maximum_spin_speed", structs.decode_BIG_f),
    0x54A8C481: ("minimum_life_time", structs.decode_BIG_f),
    0x7DD63999: ("maximum_life_time", structs.decode_BIG_f),
    0x6B571BA5: ("disable_collision_time", structs.decode_BIG_f),
    0x50051A17: ("fade_in_end_percentage", structs.decode_BIG_f),
    0x6353C409: ("fade_out_start_percentage", structs.decode_BIG_f),
    0x3A5634D8: ("start_color", _decode_start_color),
    0x5AF5867D: ("end_color", _decode_end_color),
    0x886E7C9F: ("scale_start_percentage", structs.decode_BIG_f),
    0x80C22A0A: ("final_scale", _decode_final_scale),
    0x417F4A91: ("unknown_0x417f4a91", structs.decode_BIG_f),
    0x2F2AE3E5: ("gravity", structs.decode_BIG_f),
    0xEF90F09D: ("position_offset", _decode_position_offset),
    0xC27FFA8F: ("model", structs.decode_BIG_L),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x41DD4D40: ("particle1", structs.decode_BIG_L),
    0x0BB3CCAE: ("bounce_sound", structs.decode_BIG_l),
    0x991202C3: ("max_bounce_sounds", structs.decode_BIG_l),
    0x76C79503: ("unknown_0x76c79503", structs.decode_BIG_f),
    0x310DFAC8: ("unknown_0x310dfac8", structs.decode_BIG_f),
    0x19A6F71F: ("particle_system1_scale", _decode_particle_system1_scale),
    0x3B03A01E: ("particle_system1_uses_global_translation", structs.decode_BIG_bool_),
    0x3BDD2FED: ("particle_system1_wait_for_particles_to_die", structs.decode_BIG_bool_),
    0x334A34BB: ("particle_system1_orientation", structs.decode_BIG_l),
    0xC7493FEE: ("particle2", structs.decode_BIG_L),
    0x6E3825EF: ("particle_system2_scale", _decode_particle_system2_scale),
    0xC9544DE6: ("particle_system2_uses_global_translation", structs.decode_BIG_bool_),
    0xC98AC215: ("particle_system2_wait_for_particles_to_die", structs.decode_BIG_bool_),
    0xD9CCE9D9: ("particle_system2_orientation", structs.decode_BIG_l),
    0x979042C8: ("death_particle", structs.decode_BIG_L),
    0xE9214CD8: ("death_particle_system_scale", _decode_death_particle_system_scale),
    0x9DFADEE0: ("death_particle_system_orientation", structs.decode_BIG_l),
    0x2C7B18DD: ("is_collider", structs.decode_BIG_bool_),
    0x8C73CB7C: ("is_shootable", structs.decode_BIG_bool_),
    0x0D7FAD55: ("die_on_collision", structs.decode_BIG_bool_),
    0xDCAA0F22: ("unknown_0xdcaa0f22", structs.decode_BIG_bool_),
    0xBFD82A19: ("unknown_0xbfd82a19", structs.decode_BIG_bool_),
    0x723D42D6: ("unknown_0x723d42d6", structs.decode_BIG_bool_),
    0x295F05B7: ("disable_physics_threshold", structs.decode_BIG_f),
}
