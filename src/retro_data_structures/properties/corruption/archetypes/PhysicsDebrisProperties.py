# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.PhysicsDebrisPropertiesOrientationEnum import (
    PhysicsDebrisPropertiesOrientationEnum,
)
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PhysicsDebrisPropertiesJson(typing_extensions.TypedDict):
        cone_spread_yaw: float
        cone_spread_pitch: float
        initial_direction: json_util.JsonValue
        position_offset: json_util.JsonValue
        transform_position_offset: bool
        minimum_speed: float
        maximum_speed: float
        minimum_spin_speed: json_util.JsonValue
        maximum_spin_speed: json_util.JsonValue
        minimum_lifetime: float
        maximum_lifetime: float
        disable_collision_time: float
        fade_in_end_percentage: float
        fade_out_start_percentage: float
        start_color: json_util.JsonValue
        middle_color: json_util.JsonValue
        end_color: json_util.JsonValue
        scale_start_percentage: float
        final_scale: json_util.JsonValue
        unknown_0x417f4a91: float
        friction: float
        gravity: float
        disable_physics_threshold: float
        model: int
        bounce_sound: int
        max_bounce_sounds: int
        unknown_0x76c79503: float
        unknown_0x310dfac8: float
        unknown_0x5e9f5215: float
        unknown_0x39743618: float
        unknown_0x33e0fbb4: float
        unknown_0xe82e7ed7: float
        unknown_0x855ee21b: float
        particle_system1: int
        particle_system1_scale: json_util.JsonValue
        particle_system1_uses_global_translation: bool
        particle_system1_uses_global_orientation: bool
        particle_system1_wait_for_particles_to_die: bool
        physics_debris_properties_orientation_enum_0x49286613: json_util.JsonObject
        particle_system2: int
        particle_system2_scale: json_util.JsonValue
        particle_system2_uses_global_translation: bool
        particle_system2_uses_global_orientation: bool
        particle_system2_wait_for_particles_to_die: bool
        physics_debris_properties_orientation_enum_0x1e0a4a41: json_util.JsonObject
        is_collider: bool
        is_shootable: bool
        die_on_collision: bool
        unknown_0xbfd82a19: bool
        unknown_0x723d42d6: bool
        unknown_0x4edb1d0e: bool
        unknown_0xbf496273: bool


@dataclasses.dataclass()
class PhysicsDebrisProperties(BaseProperty):
    cone_spread_yaw: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5C3C4A57, original_name="ConeSpreadYaw"),
        },
    )
    cone_spread_pitch: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA79FC55F, original_name="ConeSpreadPitch"),
        },
    )
    initial_direction: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x01A0DFE6,
                original_name="InitialDirection",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
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
    transform_position_offset: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC4B1E6A1, original_name="TransformPositionOffset"),
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
    minimum_spin_speed: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=-1.0, y=-1.0, z=-1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xF78C8AC7,
                original_name="MinimumSpinSpeed",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    maximum_spin_speed: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xB69BB541,
                original_name="MaximumSpinSpeed",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    minimum_lifetime: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD6594622, original_name="MinimumLifetime"),
        },
    )
    maximum_lifetime: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFF27BB3A, original_name="MaximumLifetime"),
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
    middle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x7C6EBE98, original_name="MiddleColor", from_json=Color.from_json, to_json=Color.to_json
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
    friction: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16B72D49, original_name="Friction"),
        },
    )
    gravity: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2F2AE3E5, original_name="Gravity"),
        },
    )
    disable_physics_threshold: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x295F05B7, original_name="DisablePhysicsThreshold"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC27FFA8F, original_name="Model"),
        },
    )
    bounce_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF1925576, original_name="BounceSound"),
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
    unknown_0x5e9f5215: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5E9F5215, original_name="Unknown"),
        },
    )
    unknown_0x39743618: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39743618, original_name="Unknown"),
        },
    )
    unknown_0x33e0fbb4: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x33E0FBB4, original_name="Unknown"),
        },
    )
    unknown_0xe82e7ed7: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE82E7ED7, original_name="Unknown"),
        },
    )
    unknown_0x855ee21b: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x855EE21B, original_name="Unknown"),
        },
    )
    particle_system1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x478D0AA3, original_name="ParticleSystem1"),
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
    particle_system1_uses_global_orientation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0xDB1FA61C, original_name="ParticleSystem1UsesGlobalOrientation"
            ),
        },
    )
    particle_system1_wait_for_particles_to_die: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0x3BDD2FED, original_name="ParticleSystem1WaitForParticlesToDie"
            ),
        },
    )
    physics_debris_properties_orientation_enum_0x49286613: PhysicsDebrisPropertiesOrientationEnum = dataclasses.field(
        default_factory=PhysicsDebrisPropertiesOrientationEnum,
        metadata={
            "reflection": FieldReflection[PhysicsDebrisPropertiesOrientationEnum](
                PhysicsDebrisPropertiesOrientationEnum,
                id=0x49286613,
                original_name="PhysicsDebrisPropertiesOrientationEnum",
                from_json=PhysicsDebrisPropertiesOrientationEnum.from_json,
                to_json=PhysicsDebrisPropertiesOrientationEnum.to_json,
            ),
        },
    )
    particle_system2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC119780D, original_name="ParticleSystem2"),
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
    particle_system2_uses_global_orientation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0x29484BE4, original_name="ParticleSystem2UsesGlobalOrientation"
            ),
        },
    )
    particle_system2_wait_for_particles_to_die: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](
                bool, id=0xC98AC215, original_name="ParticleSystem2WaitForParticlesToDie"
            ),
        },
    )
    physics_debris_properties_orientation_enum_0x1e0a4a41: PhysicsDebrisPropertiesOrientationEnum = dataclasses.field(
        default_factory=PhysicsDebrisPropertiesOrientationEnum,
        metadata={
            "reflection": FieldReflection[PhysicsDebrisPropertiesOrientationEnum](
                PhysicsDebrisPropertiesOrientationEnum,
                id=0x1E0A4A41,
                original_name="PhysicsDebrisPropertiesOrientationEnum",
                from_json=PhysicsDebrisPropertiesOrientationEnum.from_json,
                to_json=PhysicsDebrisPropertiesOrientationEnum.to_json,
            ),
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
    unknown_0x4edb1d0e: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4EDB1D0E, original_name="Unknown"),
        },
    )
    unknown_0xbf496273: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBF496273, original_name="Unknown"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 52:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C3C4A57
        cone_spread_yaw = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA79FC55F
        cone_spread_pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01A0DFE6
        initial_direction = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF90F09D
        position_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4B1E6A1
        transform_position_offset = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0185263E
        minimum_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x140EF2CC
        maximum_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF78C8AC7
        minimum_spin_speed = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB69BB541
        maximum_spin_speed = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6594622
        minimum_lifetime = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF27BB3A
        maximum_lifetime = structs.BIG_f.unpack(data.read(4))[0]

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
        assert property_id == 0x7C6EBE98
        middle_color = Color.from_stream(data, game, property_size)

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
        assert property_id == 0x16B72D49
        friction = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F2AE3E5
        gravity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x295F05B7
        disable_physics_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1925576
        bounce_sound = structs.BIG_Q.unpack(data.read(8))[0]

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
        assert property_id == 0x5E9F5215
        unknown_0x5e9f5215 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39743618
        unknown_0x39743618 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33E0FBB4
        unknown_0x33e0fbb4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE82E7ED7
        unknown_0xe82e7ed7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x855EE21B
        unknown_0x855ee21b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x478D0AA3
        particle_system1 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19A6F71F
        particle_system1_scale = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3B03A01E
        particle_system1_uses_global_translation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDB1FA61C
        particle_system1_uses_global_orientation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3BDD2FED
        particle_system1_wait_for_particles_to_die = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49286613
        physics_debris_properties_orientation_enum_0x49286613 = PhysicsDebrisPropertiesOrientationEnum.from_stream(
            data, game, property_size
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC119780D
        particle_system2 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E3825EF
        particle_system2_scale = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9544DE6
        particle_system2_uses_global_translation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29484BE4
        particle_system2_uses_global_orientation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC98AC215
        particle_system2_wait_for_particles_to_die = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E0A4A41
        physics_debris_properties_orientation_enum_0x1e0a4a41 = PhysicsDebrisPropertiesOrientationEnum.from_stream(
            data, game, property_size
        )

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
        assert property_id == 0xBFD82A19
        unknown_0xbfd82a19 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723D42D6
        unknown_0x723d42d6 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4EDB1D0E
        unknown_0x4edb1d0e = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF496273
        unknown_0xbf496273 = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            cone_spread_yaw,
            cone_spread_pitch,
            initial_direction,
            position_offset,
            transform_position_offset,
            minimum_speed,
            maximum_speed,
            minimum_spin_speed,
            maximum_spin_speed,
            minimum_lifetime,
            maximum_lifetime,
            disable_collision_time,
            fade_in_end_percentage,
            fade_out_start_percentage,
            start_color,
            middle_color,
            end_color,
            scale_start_percentage,
            final_scale,
            unknown_0x417f4a91,
            friction,
            gravity,
            disable_physics_threshold,
            model,
            bounce_sound,
            max_bounce_sounds,
            unknown_0x76c79503,
            unknown_0x310dfac8,
            unknown_0x5e9f5215,
            unknown_0x39743618,
            unknown_0x33e0fbb4,
            unknown_0xe82e7ed7,
            unknown_0x855ee21b,
            particle_system1,
            particle_system1_scale,
            particle_system1_uses_global_translation,
            particle_system1_uses_global_orientation,
            particle_system1_wait_for_particles_to_die,
            physics_debris_properties_orientation_enum_0x49286613,
            particle_system2,
            particle_system2_scale,
            particle_system2_uses_global_translation,
            particle_system2_uses_global_orientation,
            particle_system2_wait_for_particles_to_die,
            physics_debris_properties_orientation_enum_0x1e0a4a41,
            is_collider,
            is_shootable,
            die_on_collision,
            unknown_0xbfd82a19,
            unknown_0x723d42d6,
            unknown_0x4edb1d0e,
            unknown_0xbf496273,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x004")  # 52 properties

        data.write(b"\\<JW")  # 0x5c3c4a57
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cone_spread_yaw))

        data.write(b"\xa7\x9f\xc5_")  # 0xa79fc55f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cone_spread_pitch))

        data.write(b"\x01\xa0\xdf\xe6")  # 0x1a0dfe6
        data.write(b"\x00\x0c")  # size
        self.initial_direction.to_stream(data, game)

        data.write(b"\xef\x90\xf0\x9d")  # 0xef90f09d
        data.write(b"\x00\x0c")  # size
        self.position_offset.to_stream(data, game)

        data.write(b"\xc4\xb1\xe6\xa1")  # 0xc4b1e6a1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.transform_position_offset))

        data.write(b"\x01\x85&>")  # 0x185263e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.minimum_speed))

        data.write(b"\x14\x0e\xf2\xcc")  # 0x140ef2cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maximum_speed))

        data.write(b"\xf7\x8c\x8a\xc7")  # 0xf78c8ac7
        data.write(b"\x00\x0c")  # size
        self.minimum_spin_speed.to_stream(data, game)

        data.write(b"\xb6\x9b\xb5A")  # 0xb69bb541
        data.write(b"\x00\x0c")  # size
        self.maximum_spin_speed.to_stream(data, game)

        data.write(b'\xd6YF"')  # 0xd6594622
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.minimum_lifetime))

        data.write(b"\xff'\xbb:")  # 0xff27bb3a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maximum_lifetime))

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

        data.write(b"|n\xbe\x98")  # 0x7c6ebe98
        data.write(b"\x00\x10")  # size
        self.middle_color.to_stream(data, game)

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

        data.write(b"\x16\xb7-I")  # 0x16b72d49
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.friction))

        data.write(b"/*\xe3\xe5")  # 0x2f2ae3e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity))

        data.write(b")_\x05\xb7")  # 0x295f05b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.disable_physics_threshold))

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model))

        data.write(b"\xf1\x92Uv")  # 0xf1925576
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.bounce_sound))

        data.write(b"\x99\x12\x02\xc3")  # 0x991202c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_bounce_sounds))

        data.write(b"v\xc7\x95\x03")  # 0x76c79503
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76c79503))

        data.write(b"1\r\xfa\xc8")  # 0x310dfac8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x310dfac8))

        data.write(b"^\x9fR\x15")  # 0x5e9f5215
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5e9f5215))

        data.write(b"9t6\x18")  # 0x39743618
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x39743618))

        data.write(b"3\xe0\xfb\xb4")  # 0x33e0fbb4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x33e0fbb4))

        data.write(b"\xe8.~\xd7")  # 0xe82e7ed7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe82e7ed7))

        data.write(b"\x85^\xe2\x1b")  # 0x855ee21b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x855ee21b))

        data.write(b"G\x8d\n\xa3")  # 0x478d0aa3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.particle_system1))

        data.write(b"\x19\xa6\xf7\x1f")  # 0x19a6f71f
        data.write(b"\x00\x0c")  # size
        self.particle_system1_scale.to_stream(data, game)

        data.write(b";\x03\xa0\x1e")  # 0x3b03a01e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_uses_global_translation))

        data.write(b"\xdb\x1f\xa6\x1c")  # 0xdb1fa61c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_uses_global_orientation))

        data.write(b";\xdd/\xed")  # 0x3bdd2fed
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_wait_for_particles_to_die))

        data.write(b"I(f\x13")  # 0x49286613
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.physics_debris_properties_orientation_enum_0x49286613.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc1\x19x\r")  # 0xc119780d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.particle_system2))

        data.write(b"n8%\xef")  # 0x6e3825ef
        data.write(b"\x00\x0c")  # size
        self.particle_system2_scale.to_stream(data, game)

        data.write(b"\xc9TM\xe6")  # 0xc9544de6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_uses_global_translation))

        data.write(b")HK\xe4")  # 0x29484be4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_uses_global_orientation))

        data.write(b"\xc9\x8a\xc2\x15")  # 0xc98ac215
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_wait_for_particles_to_die))

        data.write(b"\x1e\nJA")  # 0x1e0a4a41
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.physics_debris_properties_orientation_enum_0x1e0a4a41.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b",{\x18\xdd")  # 0x2c7b18dd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_collider))

        data.write(b"\x8cs\xcb|")  # 0x8c73cb7c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_shootable))

        data.write(b"\r\x7f\xadU")  # 0xd7fad55
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.die_on_collision))

        data.write(b"\xbf\xd8*\x19")  # 0xbfd82a19
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbfd82a19))

        data.write(b"r=B\xd6")  # 0x723d42d6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x723d42d6))

        data.write(b"N\xdb\x1d\x0e")  # 0x4edb1d0e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4edb1d0e))

        data.write(b"\xbfIbs")  # 0xbf496273
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbf496273))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PhysicsDebrisPropertiesJson", data)
        return cls(
            cone_spread_yaw=json_data["cone_spread_yaw"],
            cone_spread_pitch=json_data["cone_spread_pitch"],
            initial_direction=Vector.from_json(json_data["initial_direction"]),
            position_offset=Vector.from_json(json_data["position_offset"]),
            transform_position_offset=json_data["transform_position_offset"],
            minimum_speed=json_data["minimum_speed"],
            maximum_speed=json_data["maximum_speed"],
            minimum_spin_speed=Vector.from_json(json_data["minimum_spin_speed"]),
            maximum_spin_speed=Vector.from_json(json_data["maximum_spin_speed"]),
            minimum_lifetime=json_data["minimum_lifetime"],
            maximum_lifetime=json_data["maximum_lifetime"],
            disable_collision_time=json_data["disable_collision_time"],
            fade_in_end_percentage=json_data["fade_in_end_percentage"],
            fade_out_start_percentage=json_data["fade_out_start_percentage"],
            start_color=Color.from_json(json_data["start_color"]),
            middle_color=Color.from_json(json_data["middle_color"]),
            end_color=Color.from_json(json_data["end_color"]),
            scale_start_percentage=json_data["scale_start_percentage"],
            final_scale=Vector.from_json(json_data["final_scale"]),
            unknown_0x417f4a91=json_data["unknown_0x417f4a91"],
            friction=json_data["friction"],
            gravity=json_data["gravity"],
            disable_physics_threshold=json_data["disable_physics_threshold"],
            model=json_data["model"],
            bounce_sound=json_data["bounce_sound"],
            max_bounce_sounds=json_data["max_bounce_sounds"],
            unknown_0x76c79503=json_data["unknown_0x76c79503"],
            unknown_0x310dfac8=json_data["unknown_0x310dfac8"],
            unknown_0x5e9f5215=json_data["unknown_0x5e9f5215"],
            unknown_0x39743618=json_data["unknown_0x39743618"],
            unknown_0x33e0fbb4=json_data["unknown_0x33e0fbb4"],
            unknown_0xe82e7ed7=json_data["unknown_0xe82e7ed7"],
            unknown_0x855ee21b=json_data["unknown_0x855ee21b"],
            particle_system1=json_data["particle_system1"],
            particle_system1_scale=Vector.from_json(json_data["particle_system1_scale"]),
            particle_system1_uses_global_translation=json_data["particle_system1_uses_global_translation"],
            particle_system1_uses_global_orientation=json_data["particle_system1_uses_global_orientation"],
            particle_system1_wait_for_particles_to_die=json_data["particle_system1_wait_for_particles_to_die"],
            physics_debris_properties_orientation_enum_0x49286613=PhysicsDebrisPropertiesOrientationEnum.from_json(
                json_data["physics_debris_properties_orientation_enum_0x49286613"]
            ),
            particle_system2=json_data["particle_system2"],
            particle_system2_scale=Vector.from_json(json_data["particle_system2_scale"]),
            particle_system2_uses_global_translation=json_data["particle_system2_uses_global_translation"],
            particle_system2_uses_global_orientation=json_data["particle_system2_uses_global_orientation"],
            particle_system2_wait_for_particles_to_die=json_data["particle_system2_wait_for_particles_to_die"],
            physics_debris_properties_orientation_enum_0x1e0a4a41=PhysicsDebrisPropertiesOrientationEnum.from_json(
                json_data["physics_debris_properties_orientation_enum_0x1e0a4a41"]
            ),
            is_collider=json_data["is_collider"],
            is_shootable=json_data["is_shootable"],
            die_on_collision=json_data["die_on_collision"],
            unknown_0xbfd82a19=json_data["unknown_0xbfd82a19"],
            unknown_0x723d42d6=json_data["unknown_0x723d42d6"],
            unknown_0x4edb1d0e=json_data["unknown_0x4edb1d0e"],
            unknown_0xbf496273=json_data["unknown_0xbf496273"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "cone_spread_yaw": self.cone_spread_yaw,
            "cone_spread_pitch": self.cone_spread_pitch,
            "initial_direction": self.initial_direction.to_json(),
            "position_offset": self.position_offset.to_json(),
            "transform_position_offset": self.transform_position_offset,
            "minimum_speed": self.minimum_speed,
            "maximum_speed": self.maximum_speed,
            "minimum_spin_speed": self.minimum_spin_speed.to_json(),
            "maximum_spin_speed": self.maximum_spin_speed.to_json(),
            "minimum_lifetime": self.minimum_lifetime,
            "maximum_lifetime": self.maximum_lifetime,
            "disable_collision_time": self.disable_collision_time,
            "fade_in_end_percentage": self.fade_in_end_percentage,
            "fade_out_start_percentage": self.fade_out_start_percentage,
            "start_color": self.start_color.to_json(),
            "middle_color": self.middle_color.to_json(),
            "end_color": self.end_color.to_json(),
            "scale_start_percentage": self.scale_start_percentage,
            "final_scale": self.final_scale.to_json(),
            "unknown_0x417f4a91": self.unknown_0x417f4a91,
            "friction": self.friction,
            "gravity": self.gravity,
            "disable_physics_threshold": self.disable_physics_threshold,
            "model": self.model,
            "bounce_sound": self.bounce_sound,
            "max_bounce_sounds": self.max_bounce_sounds,
            "unknown_0x76c79503": self.unknown_0x76c79503,
            "unknown_0x310dfac8": self.unknown_0x310dfac8,
            "unknown_0x5e9f5215": self.unknown_0x5e9f5215,
            "unknown_0x39743618": self.unknown_0x39743618,
            "unknown_0x33e0fbb4": self.unknown_0x33e0fbb4,
            "unknown_0xe82e7ed7": self.unknown_0xe82e7ed7,
            "unknown_0x855ee21b": self.unknown_0x855ee21b,
            "particle_system1": self.particle_system1,
            "particle_system1_scale": self.particle_system1_scale.to_json(),
            "particle_system1_uses_global_translation": self.particle_system1_uses_global_translation,
            "particle_system1_uses_global_orientation": self.particle_system1_uses_global_orientation,
            "particle_system1_wait_for_particles_to_die": self.particle_system1_wait_for_particles_to_die,
            "physics_debris_properties_orientation_enum_0x49286613": self.physics_debris_properties_orientation_enum_0x49286613.to_json(),
            "particle_system2": self.particle_system2,
            "particle_system2_scale": self.particle_system2_scale.to_json(),
            "particle_system2_uses_global_translation": self.particle_system2_uses_global_translation,
            "particle_system2_uses_global_orientation": self.particle_system2_uses_global_orientation,
            "particle_system2_wait_for_particles_to_die": self.particle_system2_wait_for_particles_to_die,
            "physics_debris_properties_orientation_enum_0x1e0a4a41": self.physics_debris_properties_orientation_enum_0x1e0a4a41.to_json(),
            "is_collider": self.is_collider,
            "is_shootable": self.is_shootable,
            "die_on_collision": self.die_on_collision,
            "unknown_0xbfd82a19": self.unknown_0xbfd82a19,
            "unknown_0x723d42d6": self.unknown_0x723d42d6,
            "unknown_0x4edb1d0e": self.unknown_0x4edb1d0e,
            "unknown_0xbf496273": self.unknown_0xbf496273,
        }


def _decode_initial_direction(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_position_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_minimum_spin_speed(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_maximum_spin_speed(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_start_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_middle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_end_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_final_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_particle_system1_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_physics_debris_properties_orientation_enum_0x49286613(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PhysicsDebrisPropertiesOrientationEnum:
    return PhysicsDebrisPropertiesOrientationEnum.from_stream(data, game, property_size)


def _decode_particle_system2_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_physics_debris_properties_orientation_enum_0x1e0a4a41(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PhysicsDebrisPropertiesOrientationEnum:
    return PhysicsDebrisPropertiesOrientationEnum.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5C3C4A57: ("cone_spread_yaw", structs.decode_BIG_f),
    0xA79FC55F: ("cone_spread_pitch", structs.decode_BIG_f),
    0x01A0DFE6: ("initial_direction", _decode_initial_direction),
    0xEF90F09D: ("position_offset", _decode_position_offset),
    0xC4B1E6A1: ("transform_position_offset", structs.decode_BIG_bool_),
    0x0185263E: ("minimum_speed", structs.decode_BIG_f),
    0x140EF2CC: ("maximum_speed", structs.decode_BIG_f),
    0xF78C8AC7: ("minimum_spin_speed", _decode_minimum_spin_speed),
    0xB69BB541: ("maximum_spin_speed", _decode_maximum_spin_speed),
    0xD6594622: ("minimum_lifetime", structs.decode_BIG_f),
    0xFF27BB3A: ("maximum_lifetime", structs.decode_BIG_f),
    0x6B571BA5: ("disable_collision_time", structs.decode_BIG_f),
    0x50051A17: ("fade_in_end_percentage", structs.decode_BIG_f),
    0x6353C409: ("fade_out_start_percentage", structs.decode_BIG_f),
    0x3A5634D8: ("start_color", _decode_start_color),
    0x7C6EBE98: ("middle_color", _decode_middle_color),
    0x5AF5867D: ("end_color", _decode_end_color),
    0x886E7C9F: ("scale_start_percentage", structs.decode_BIG_f),
    0x80C22A0A: ("final_scale", _decode_final_scale),
    0x417F4A91: ("unknown_0x417f4a91", structs.decode_BIG_f),
    0x16B72D49: ("friction", structs.decode_BIG_f),
    0x2F2AE3E5: ("gravity", structs.decode_BIG_f),
    0x295F05B7: ("disable_physics_threshold", structs.decode_BIG_f),
    0xC27FFA8F: ("model", structs.decode_BIG_Q),
    0xF1925576: ("bounce_sound", structs.decode_BIG_Q),
    0x991202C3: ("max_bounce_sounds", structs.decode_BIG_l),
    0x76C79503: ("unknown_0x76c79503", structs.decode_BIG_f),
    0x310DFAC8: ("unknown_0x310dfac8", structs.decode_BIG_f),
    0x5E9F5215: ("unknown_0x5e9f5215", structs.decode_BIG_f),
    0x39743618: ("unknown_0x39743618", structs.decode_BIG_f),
    0x33E0FBB4: ("unknown_0x33e0fbb4", structs.decode_BIG_f),
    0xE82E7ED7: ("unknown_0xe82e7ed7", structs.decode_BIG_f),
    0x855EE21B: ("unknown_0x855ee21b", structs.decode_BIG_f),
    0x478D0AA3: ("particle_system1", structs.decode_BIG_Q),
    0x19A6F71F: ("particle_system1_scale", _decode_particle_system1_scale),
    0x3B03A01E: ("particle_system1_uses_global_translation", structs.decode_BIG_bool_),
    0xDB1FA61C: ("particle_system1_uses_global_orientation", structs.decode_BIG_bool_),
    0x3BDD2FED: ("particle_system1_wait_for_particles_to_die", structs.decode_BIG_bool_),
    0x49286613: (
        "physics_debris_properties_orientation_enum_0x49286613",
        _decode_physics_debris_properties_orientation_enum_0x49286613,
    ),
    0xC119780D: ("particle_system2", structs.decode_BIG_Q),
    0x6E3825EF: ("particle_system2_scale", _decode_particle_system2_scale),
    0xC9544DE6: ("particle_system2_uses_global_translation", structs.decode_BIG_bool_),
    0x29484BE4: ("particle_system2_uses_global_orientation", structs.decode_BIG_bool_),
    0xC98AC215: ("particle_system2_wait_for_particles_to_die", structs.decode_BIG_bool_),
    0x1E0A4A41: (
        "physics_debris_properties_orientation_enum_0x1e0a4a41",
        _decode_physics_debris_properties_orientation_enum_0x1e0a4a41,
    ),
    0x2C7B18DD: ("is_collider", structs.decode_BIG_bool_),
    0x8C73CB7C: ("is_shootable", structs.decode_BIG_bool_),
    0x0D7FAD55: ("die_on_collision", structs.decode_BIG_bool_),
    0xBFD82A19: ("unknown_0xbfd82a19", structs.decode_BIG_bool_),
    0x723D42D6: ("unknown_0x723d42d6", structs.decode_BIG_bool_),
    0x4EDB1D0E: ("unknown_0x4edb1d0e", structs.decode_BIG_bool_),
    0xBF496273: ("unknown_0xbf496273", structs.decode_BIG_bool_),
}
