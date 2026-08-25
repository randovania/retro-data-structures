# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct34Json(typing_extensions.TypedDict):
        health: json_util.JsonObject
        damage: json_util.JsonObject
        explosion: int
        effect: int
        trail: int
        mass: float
        unknown_0x417f4a91: float
        min_launch_speed: float
        max_launch_speed: float
        unknown_0xfbcdb101: int
        sound_bounce: int
        sound_explode: int
        max_turn_angle: float
        unknown_0x47f99fbc: float
        min_generation: int
        max_generation: int
        unknown_0xfbf8ea0a: float
        allow_lock_on: bool


@dataclasses.dataclass()
class UnknownStruct34(BaseProperty):
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
    explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD8C6D15C, original_name="Explosion"),
        },
    )
    effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB68C6D96, original_name="Effect"),
        },
    )
    trail: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCB0B919B, original_name="Trail"),
        },
    )
    mass: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75DBB375, original_name="Mass"),
        },
    )
    unknown_0x417f4a91: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x417F4A91, original_name="Unknown"),
        },
    )
    min_launch_speed: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50A19B1F, original_name="MinLaunchSpeed"),
        },
    )
    max_launch_speed: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF7951B66, original_name="MaxLaunchSpeed"),
        },
    )
    unknown_0xfbcdb101: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFBCDB101, original_name="Unknown"),
        },
    )
    sound_bounce: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x6758BF01, original_name="Sound_Bounce"),
        },
    )
    sound_explode: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x524A8073, original_name="Sound_Explode"),
        },
    )
    max_turn_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50E46527, original_name="MaxTurnAngle"),
        },
    )
    unknown_0x47f99fbc: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47F99FBC, original_name="Unknown"),
        },
    )
    min_generation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDC5AF41E, original_name="MinGeneration"),
        },
    )
    max_generation: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8DA34F43, original_name="MaxGeneration"),
        },
    )
    unknown_0xfbf8ea0a: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFBF8EA0A, original_name="Unknown"),
        },
    )
    allow_lock_on: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x98D21B22, original_name="AllowLockOn"),
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
        if property_count != 18:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 9, "di_damage": 5.0, "di_knock_back_power": 1.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8C6D15C
        explosion = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB68C6D96
        effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB0B919B
        trail = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75DBB375
        mass = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x417F4A91
        unknown_0x417f4a91 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50A19B1F
        min_launch_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF7951B66
        max_launch_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBCDB101
        unknown_0xfbcdb101 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6758BF01
        sound_bounce = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x524A8073
        sound_explode = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50E46527
        max_turn_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47F99FBC
        unknown_0x47f99fbc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC5AF41E
        min_generation = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8DA34F43
        max_generation = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBF8EA0A
        unknown_0xfbf8ea0a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98D21B22
        allow_lock_on = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            health,
            damage,
            explosion,
            effect,
            trail,
            mass,
            unknown_0x417f4a91,
            min_launch_speed,
            max_launch_speed,
            unknown_0xfbcdb101,
            sound_bounce,
            sound_explode,
            max_turn_angle,
            unknown_0x47f99fbc,
            min_generation,
            max_generation,
            unknown_0xfbf8ea0a,
            allow_lock_on,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x12")  # 18 properties

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(
            data, game, default_override={"di_weapon_type": 9, "di_damage": 5.0, "di_knock_back_power": 1.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd8\xc6\xd1\\")  # 0xd8c6d15c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.explosion))

        data.write(b"\xb6\x8cm\x96")  # 0xb68c6d96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.effect))

        data.write(b"\xcb\x0b\x91\x9b")  # 0xcb0b919b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.trail))

        data.write(b"u\xdb\xb3u")  # 0x75dbb375
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mass))

        data.write(b"A\x7fJ\x91")  # 0x417f4a91
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x417f4a91))

        data.write(b"P\xa1\x9b\x1f")  # 0x50a19b1f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_launch_speed))

        data.write(b"\xf7\x95\x1bf")  # 0xf7951b66
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_launch_speed))

        data.write(b"\xfb\xcd\xb1\x01")  # 0xfbcdb101
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xfbcdb101))

        data.write(b"gX\xbf\x01")  # 0x6758bf01
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_bounce))

        data.write(b"RJ\x80s")  # 0x524a8073
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_explode))

        data.write(b"P\xe4e'")  # 0x50e46527
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_turn_angle))

        data.write(b"G\xf9\x9f\xbc")  # 0x47f99fbc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x47f99fbc))

        data.write(b"\xdcZ\xf4\x1e")  # 0xdc5af41e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.min_generation))

        data.write(b"\x8d\xa3OC")  # 0x8da34f43
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_generation))

        data.write(b"\xfb\xf8\xea\n")  # 0xfbf8ea0a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfbf8ea0a))

        data.write(b'\x98\xd2\x1b"')  # 0x98d21b22
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.allow_lock_on))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct34Json", data)
        return cls(
            health=HealthInfo.from_json(json_data["health"]),
            damage=DamageInfo.from_json(json_data["damage"]),
            explosion=json_data["explosion"],
            effect=json_data["effect"],
            trail=json_data["trail"],
            mass=json_data["mass"],
            unknown_0x417f4a91=json_data["unknown_0x417f4a91"],
            min_launch_speed=json_data["min_launch_speed"],
            max_launch_speed=json_data["max_launch_speed"],
            unknown_0xfbcdb101=json_data["unknown_0xfbcdb101"],
            sound_bounce=json_data["sound_bounce"],
            sound_explode=json_data["sound_explode"],
            max_turn_angle=json_data["max_turn_angle"],
            unknown_0x47f99fbc=json_data["unknown_0x47f99fbc"],
            min_generation=json_data["min_generation"],
            max_generation=json_data["max_generation"],
            unknown_0xfbf8ea0a=json_data["unknown_0xfbf8ea0a"],
            allow_lock_on=json_data["allow_lock_on"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "health": self.health.to_json(),
            "damage": self.damage.to_json(),
            "explosion": self.explosion,
            "effect": self.effect,
            "trail": self.trail,
            "mass": self.mass,
            "unknown_0x417f4a91": self.unknown_0x417f4a91,
            "min_launch_speed": self.min_launch_speed,
            "max_launch_speed": self.max_launch_speed,
            "unknown_0xfbcdb101": self.unknown_0xfbcdb101,
            "sound_bounce": self.sound_bounce,
            "sound_explode": self.sound_explode,
            "max_turn_angle": self.max_turn_angle,
            "unknown_0x47f99fbc": self.unknown_0x47f99fbc,
            "min_generation": self.min_generation,
            "max_generation": self.max_generation,
            "unknown_0xfbf8ea0a": self.unknown_0xfbf8ea0a,
            "allow_lock_on": self.allow_lock_on,
        }

    def _dependencies_for_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.explosion)

    def _dependencies_for_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.effect)

    def _dependencies_for_trail(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.trail)

    def _dependencies_for_sound_bounce(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_bounce)

    def _dependencies_for_sound_explode(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_explode)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_explosion, "explosion", "AssetId"),
            (self._dependencies_for_effect, "effect", "AssetId"),
            (self._dependencies_for_trail, "trail", "AssetId"),
            (self._dependencies_for_sound_bounce, "sound_bounce", "int"),
            (self._dependencies_for_sound_explode, "sound_explode", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct34.{field_name} ({field_type}): {e}")


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_weapon_type": 9, "di_damage": 5.0, "di_knock_back_power": 1.0}
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCF90D15E: ("health", _decode_health),
    0x337F9524: ("damage", _decode_damage),
    0xD8C6D15C: ("explosion", structs.decode_BIG_L),
    0xB68C6D96: ("effect", structs.decode_BIG_L),
    0xCB0B919B: ("trail", structs.decode_BIG_L),
    0x75DBB375: ("mass", structs.decode_BIG_f),
    0x417F4A91: ("unknown_0x417f4a91", structs.decode_BIG_f),
    0x50A19B1F: ("min_launch_speed", structs.decode_BIG_f),
    0xF7951B66: ("max_launch_speed", structs.decode_BIG_f),
    0xFBCDB101: ("unknown_0xfbcdb101", structs.decode_BIG_l),
    0x6758BF01: ("sound_bounce", structs.decode_BIG_l),
    0x524A8073: ("sound_explode", structs.decode_BIG_l),
    0x50E46527: ("max_turn_angle", structs.decode_BIG_f),
    0x47F99FBC: ("unknown_0x47f99fbc", structs.decode_BIG_f),
    0xDC5AF41E: ("min_generation", structs.decode_BIG_l),
    0x8DA34F43: ("max_generation", structs.decode_BIG_l),
    0xFBF8EA0A: ("unknown_0xfbf8ea0a", structs.decode_BIG_f),
    0x98D21B22: ("allow_lock_on", structs.decode_BIG_bool_),
}
