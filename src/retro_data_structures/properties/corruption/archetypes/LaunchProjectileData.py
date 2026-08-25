# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class LaunchProjectileDataJson(typing_extensions.TypedDict):
        projectile: int
        damage: json_util.JsonObject
        scale: json_util.JsonValue
        delay: float
        delay_variance: float
        visor_effect: int
        sound_visor_effect: int
        stop_homing_range: float
        burn_damage: float
        burn_duration: float
        targetable: bool
        collision_box: json_util.JsonValue
        hit_points: float
        generate_pickup_chance: float


@dataclasses.dataclass()
class LaunchProjectileData(BaseProperty):
    projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEF485DB9, original_name="Projectile"),
        },
    )
    damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x337F9524,
                original_name="Damage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xF726E5DA, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    delay: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14FFF39C, original_name="Delay"),
        },
    )
    delay_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7DA8EA23, original_name="DelayVariance"),
        },
    )
    visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE9C8E2BD, original_name="VisorEffect"),
        },
    )
    sound_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA3E8EC4E, original_name="Sound_VisorEffect"),
        },
    )
    stop_homing_range: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x053AE4A7, original_name="StopHomingRange"),
        },
    )
    burn_damage: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF201BFA, original_name="BurnDamage"),
        },
    )
    burn_duration: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x88137FA8, original_name="BurnDuration"),
        },
    )
    targetable: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB2D02323, original_name="Targetable"),
        },
    )
    collision_box: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xF344C0B0, original_name="CollisionBox", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    hit_points: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x056B20B2, original_name="HitPoints"),
        },
    )
    generate_pickup_chance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF78469D6, original_name="GeneratePickupChance"),
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
        if property_count != 14:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF485DB9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF726E5DA
        scale = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14FFF39C
        delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7DA8EA23
        delay_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9C8E2BD
        visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3E8EC4E
        sound_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x053AE4A7
        stop_homing_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF201BFA
        burn_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88137FA8
        burn_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2D02323
        targetable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF344C0B0
        collision_box = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x056B20B2
        hit_points = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF78469D6
        generate_pickup_chance = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            projectile,
            damage,
            scale,
            delay,
            delay_variance,
            visor_effect,
            sound_visor_effect,
            stop_homing_range,
            burn_damage,
            burn_duration,
            targetable,
            collision_box,
            hit_points,
            generate_pickup_chance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x00\x07")  # 7 properties
        num_properties_written = 7

        data.write(b"\xefH]\xb9")  # 0xef485db9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.projectile))

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf7&\xe5\xda")  # 0xf726e5da
        data.write(b"\x00\x0c")  # size
        self.scale.to_stream(data, game)

        data.write(b"\x14\xff\xf3\x9c")  # 0x14fff39c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.delay))

        data.write(b"}\xa8\xea#")  # 0x7da8ea23
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.delay_variance))

        data.write(b"\xe9\xc8\xe2\xbd")  # 0xe9c8e2bd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_effect))

        data.write(b"\xa3\xe8\xecN")  # 0xa3e8ec4e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_visor_effect))

        if self.stop_homing_range != default_override.get("stop_homing_range", 20.0):
            num_properties_written += 1
            data.write(b"\x05:\xe4\xa7")  # 0x53ae4a7
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.stop_homing_range))

        if self.burn_damage != default_override.get("burn_damage", 1.0):
            num_properties_written += 1
            data.write(b"\xcf \x1b\xfa")  # 0xcf201bfa
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.burn_damage))

        if self.burn_duration != default_override.get("burn_duration", 3.0):
            num_properties_written += 1
            data.write(b"\x88\x13\x7f\xa8")  # 0x88137fa8
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.burn_duration))

        if self.targetable != default_override.get("targetable", True):
            num_properties_written += 1
            data.write(b"\xb2\xd0##")  # 0xb2d02323
            data.write(b"\x00\x01")  # size
            data.write(structs.BIG_bool_.pack(self.targetable))

        if self.collision_box != default_override.get("collision_box", Vector(x=1.0, y=1.0, z=1.0)):
            num_properties_written += 1
            data.write(b"\xf3D\xc0\xb0")  # 0xf344c0b0
            data.write(b"\x00\x0c")  # size
            self.collision_box.to_stream(data, game)

        if self.hit_points != default_override.get("hit_points", 1.0):
            num_properties_written += 1
            data.write(b"\x05k \xb2")  # 0x56b20b2
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.hit_points))

        if self.generate_pickup_chance != default_override.get("generate_pickup_chance", 0.0):
            num_properties_written += 1
            data.write(b"\xf7\x84i\xd6")  # 0xf78469d6
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.generate_pickup_chance))

        if num_properties_written != 7:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack(">H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LaunchProjectileDataJson", data)
        return cls(
            projectile=json_data["projectile"],
            damage=DamageInfo.from_json(json_data["damage"]),
            scale=Vector.from_json(json_data["scale"]),
            delay=json_data["delay"],
            delay_variance=json_data["delay_variance"],
            visor_effect=json_data["visor_effect"],
            sound_visor_effect=json_data["sound_visor_effect"],
            stop_homing_range=json_data["stop_homing_range"],
            burn_damage=json_data["burn_damage"],
            burn_duration=json_data["burn_duration"],
            targetable=json_data["targetable"],
            collision_box=Vector.from_json(json_data["collision_box"]),
            hit_points=json_data["hit_points"],
            generate_pickup_chance=json_data["generate_pickup_chance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "projectile": self.projectile,
            "damage": self.damage.to_json(),
            "scale": self.scale.to_json(),
            "delay": self.delay,
            "delay_variance": self.delay_variance,
            "visor_effect": self.visor_effect,
            "sound_visor_effect": self.sound_visor_effect,
            "stop_homing_range": self.stop_homing_range,
            "burn_damage": self.burn_damage,
            "burn_duration": self.burn_duration,
            "targetable": self.targetable,
            "collision_box": self.collision_box.to_json(),
            "hit_points": self.hit_points,
            "generate_pickup_chance": self.generate_pickup_chance,
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xEF485DB9: ("projectile", structs.decode_BIG_Q),
    0x337F9524: ("damage", _decode_damage),
    0xF726E5DA: ("scale", _decode_scale),
    0x14FFF39C: ("delay", structs.decode_BIG_f),
    0x7DA8EA23: ("delay_variance", structs.decode_BIG_f),
    0xE9C8E2BD: ("visor_effect", structs.decode_BIG_Q),
    0xA3E8EC4E: ("sound_visor_effect", structs.decode_BIG_Q),
    0x053AE4A7: ("stop_homing_range", structs.decode_BIG_f),
    0xCF201BFA: ("burn_damage", structs.decode_BIG_f),
    0x88137FA8: ("burn_duration", structs.decode_BIG_f),
    0xB2D02323: ("targetable", structs.decode_BIG_bool_),
    0xF344C0B0: ("collision_box", _decode_collision_box),
    0x056B20B2: ("hit_points", structs.decode_BIG_f),
    0xF78469D6: ("generate_pickup_chance", structs.decode_BIG_f),
}
