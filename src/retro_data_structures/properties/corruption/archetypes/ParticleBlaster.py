# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.StaticGeometryTest import StaticGeometryTest
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ParticleBlasterJson(typing_extensions.TypedDict):
        projectile_static_geometry_test: json_util.JsonObject
        projectile: int
        damage: json_util.JsonObject
        sound: int
        visor_effect: int
        visor_impact_sound: int
        max_attack_range: float
        min_attack_time: float
        attack_time_variance: float
        unknown: float


@dataclasses.dataclass()
class ParticleBlaster(BaseProperty):
    projectile_static_geometry_test: StaticGeometryTest = dataclasses.field(
        default_factory=StaticGeometryTest,
        metadata={
            "reflection": FieldReflection[StaticGeometryTest](
                StaticGeometryTest,
                id=0x9A892818,
                original_name="ProjectileStaticGeometryTest",
                from_json=StaticGeometryTest.from_json,
                to_json=StaticGeometryTest.to_json,
            ),
        },
    )
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
    sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA55DACF6, original_name="Sound"),
        },
    )
    visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART", "ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE9C8E2BD, original_name="VisorEffect"),
        },
    )
    visor_impact_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x86FFB3F6, original_name="VisorImpactSound"),
        },
    )
    max_attack_range: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFF77C96F, original_name="MaxAttackRange"),
        },
    )
    min_attack_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2EDF3368, original_name="MinAttackTime"),
        },
    )
    attack_time_variance: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F269614, original_name="AttackTimeVariance"),
        },
    )
    unknown: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x71587B45, original_name="Unknown"),
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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A892818
        projectile_static_geometry_test = StaticGeometryTest.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF485DB9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA55DACF6
        sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9C8E2BD
        visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86FFB3F6
        visor_impact_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF77C96F
        max_attack_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2EDF3368
        min_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F269614
        attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71587B45
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            projectile_static_geometry_test,
            projectile,
            damage,
            sound,
            visor_effect,
            visor_impact_sound,
            max_attack_range,
            min_attack_time,
            attack_time_variance,
            unknown,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"\x9a\x89(\x18")  # 0x9a892818
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_static_geometry_test.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

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

        data.write(b"\xa5]\xac\xf6")  # 0xa55dacf6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound))

        data.write(b"\xe9\xc8\xe2\xbd")  # 0xe9c8e2bd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_effect))

        data.write(b"\x86\xff\xb3\xf6")  # 0x86ffb3f6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_impact_sound))

        data.write(b"\xffw\xc9o")  # 0xff77c96f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_range))

        data.write(b".\xdf3h")  # 0x2edf3368
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_time))

        data.write(b"\x9f&\x96\x14")  # 0x9f269614
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_time_variance))

        data.write(b"qX{E")  # 0x71587b45
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ParticleBlasterJson", data)
        return cls(
            projectile_static_geometry_test=StaticGeometryTest.from_json(json_data["projectile_static_geometry_test"]),
            projectile=json_data["projectile"],
            damage=DamageInfo.from_json(json_data["damage"]),
            sound=json_data["sound"],
            visor_effect=json_data["visor_effect"],
            visor_impact_sound=json_data["visor_impact_sound"],
            max_attack_range=json_data["max_attack_range"],
            min_attack_time=json_data["min_attack_time"],
            attack_time_variance=json_data["attack_time_variance"],
            unknown=json_data["unknown"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "projectile_static_geometry_test": self.projectile_static_geometry_test.to_json(),
            "projectile": self.projectile,
            "damage": self.damage.to_json(),
            "sound": self.sound,
            "visor_effect": self.visor_effect,
            "visor_impact_sound": self.visor_impact_sound,
            "max_attack_range": self.max_attack_range,
            "min_attack_time": self.min_attack_time,
            "attack_time_variance": self.attack_time_variance,
            "unknown": self.unknown,
        }


def _decode_projectile_static_geometry_test(
    data: typing.BinaryIO, game: Game, property_size: int
) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x9A892818: ("projectile_static_geometry_test", _decode_projectile_static_geometry_test),
    0xEF485DB9: ("projectile", structs.decode_BIG_Q),
    0x337F9524: ("damage", _decode_damage),
    0xA55DACF6: ("sound", structs.decode_BIG_Q),
    0xE9C8E2BD: ("visor_effect", structs.decode_BIG_Q),
    0x86FFB3F6: ("visor_impact_sound", structs.decode_BIG_Q),
    0xFF77C96F: ("max_attack_range", structs.decode_BIG_f),
    0x2EDF3368: ("min_attack_time", structs.decode_BIG_f),
    0x9F269614: ("attack_time_variance", structs.decode_BIG_f),
    0x71587B45: ("unknown", structs.decode_BIG_f),
}
