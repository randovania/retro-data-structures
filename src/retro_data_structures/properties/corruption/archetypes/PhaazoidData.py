# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PhaazoidDataJson(typing_extensions.TypedDict):
        stage: int
        unknown_0x02a3e092: bool
        play_initial_anim: bool
        acceleration: float
        max_speed: float
        min_attack_dist: float
        max_attack_dist: float
        unknown_0xb5d19503: float
        unknown_0xe2dfc540: float
        moving_map_opacity: float
        unknown_0xd04a6e1c: float
        shock_wave_info: json_util.JsonObject
        phaazoid_projectile: int
        damage_info: json_util.JsonObject


@dataclasses.dataclass()
class PhaazoidData(BaseProperty):
    stage: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB25774E2, original_name="Stage"),
        },
    )
    unknown_0x02a3e092: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x02A3E092, original_name="Unknown"),
        },
    )
    play_initial_anim: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x88FDE98C, original_name="PlayInitialAnim"),
        },
    )
    acceleration: float = dataclasses.field(
        default=65.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39FB7978, original_name="Acceleration"),
        },
    )
    max_speed: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x82DB0CBE, original_name="MaxSpeed"),
        },
    )
    min_attack_dist: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D7447B4, original_name="MinAttackDist"),
        },
    )
    max_attack_dist: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2ED25F50, original_name="MaxAttackDist"),
        },
    )
    unknown_0xb5d19503: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB5D19503, original_name="Unknown"),
        },
    )
    unknown_0xe2dfc540: float = dataclasses.field(
        default=3.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE2DFC540, original_name="Unknown"),
        },
    )
    moving_map_opacity: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3317D0C6, original_name="MovingMapOpacity"),
        },
    )
    unknown_0xd04a6e1c: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD04A6E1C, original_name="Unknown"),
        },
    )
    shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x12B8E543,
                original_name="ShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    phaazoid_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE8CD9627, original_name="PhaazoidProjectile"),
        },
    )
    damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x1DC69E38,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
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
        assert property_id == 0xB25774E2
        stage = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02A3E092
        unknown_0x02a3e092 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88FDE98C
        play_initial_anim = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39FB7978
        acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82DB0CBE
        max_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D7447B4
        min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ED25F50
        max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5D19503
        unknown_0xb5d19503 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2DFC540
        unknown_0xe2dfc540 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3317D0C6
        moving_map_opacity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD04A6E1C
        unknown_0xd04a6e1c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12B8E543
        shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8CD9627
        phaazoid_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1DC69E38
        damage_info = DamageInfo.from_stream(data, game, property_size)

        return cls(
            stage,
            unknown_0x02a3e092,
            play_initial_anim,
            acceleration,
            max_speed,
            min_attack_dist,
            max_attack_dist,
            unknown_0xb5d19503,
            unknown_0xe2dfc540,
            moving_map_opacity,
            unknown_0xd04a6e1c,
            shock_wave_info,
            phaazoid_projectile,
            damage_info,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"\xb2Wt\xe2")  # 0xb25774e2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.stage))

        data.write(b"\x02\xa3\xe0\x92")  # 0x2a3e092
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x02a3e092))

        data.write(b"\x88\xfd\xe9\x8c")  # 0x88fde98c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.play_initial_anim))

        data.write(b"9\xfbyx")  # 0x39fb7978
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.acceleration))

        data.write(b"\x82\xdb\x0c\xbe")  # 0x82db0cbe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_speed))

        data.write(b"}tG\xb4")  # 0x7d7447b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_dist))

        data.write(b".\xd2_P")  # 0x2ed25f50
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_dist))

        data.write(b"\xb5\xd1\x95\x03")  # 0xb5d19503
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb5d19503))

        data.write(b"\xe2\xdf\xc5@")  # 0xe2dfc540
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe2dfc540))

        data.write(b"3\x17\xd0\xc6")  # 0x3317d0c6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.moving_map_opacity))

        data.write(b"\xd0Jn\x1c")  # 0xd04a6e1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd04a6e1c))

        data.write(b"\x12\xb8\xe5C")  # 0x12b8e543
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe8\xcd\x96'")  # 0xe8cd9627
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.phaazoid_projectile))

        data.write(b"\x1d\xc6\x9e8")  # 0x1dc69e38
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PhaazoidDataJson", data)
        return cls(
            stage=json_data["stage"],
            unknown_0x02a3e092=json_data["unknown_0x02a3e092"],
            play_initial_anim=json_data["play_initial_anim"],
            acceleration=json_data["acceleration"],
            max_speed=json_data["max_speed"],
            min_attack_dist=json_data["min_attack_dist"],
            max_attack_dist=json_data["max_attack_dist"],
            unknown_0xb5d19503=json_data["unknown_0xb5d19503"],
            unknown_0xe2dfc540=json_data["unknown_0xe2dfc540"],
            moving_map_opacity=json_data["moving_map_opacity"],
            unknown_0xd04a6e1c=json_data["unknown_0xd04a6e1c"],
            shock_wave_info=ShockWaveInfo.from_json(json_data["shock_wave_info"]),
            phaazoid_projectile=json_data["phaazoid_projectile"],
            damage_info=DamageInfo.from_json(json_data["damage_info"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "stage": self.stage,
            "unknown_0x02a3e092": self.unknown_0x02a3e092,
            "play_initial_anim": self.play_initial_anim,
            "acceleration": self.acceleration,
            "max_speed": self.max_speed,
            "min_attack_dist": self.min_attack_dist,
            "max_attack_dist": self.max_attack_dist,
            "unknown_0xb5d19503": self.unknown_0xb5d19503,
            "unknown_0xe2dfc540": self.unknown_0xe2dfc540,
            "moving_map_opacity": self.moving_map_opacity,
            "unknown_0xd04a6e1c": self.unknown_0xd04a6e1c,
            "shock_wave_info": self.shock_wave_info.to_json(),
            "phaazoid_projectile": self.phaazoid_projectile,
            "damage_info": self.damage_info.to_json(),
        }


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB25774E2: ("stage", structs.decode_BIG_l),
    0x02A3E092: ("unknown_0x02a3e092", structs.decode_BIG_bool_),
    0x88FDE98C: ("play_initial_anim", structs.decode_BIG_bool_),
    0x39FB7978: ("acceleration", structs.decode_BIG_f),
    0x82DB0CBE: ("max_speed", structs.decode_BIG_f),
    0x7D7447B4: ("min_attack_dist", structs.decode_BIG_f),
    0x2ED25F50: ("max_attack_dist", structs.decode_BIG_f),
    0xB5D19503: ("unknown_0xb5d19503", structs.decode_BIG_f),
    0xE2DFC540: ("unknown_0xe2dfc540", structs.decode_BIG_f),
    0x3317D0C6: ("moving_map_opacity", structs.decode_BIG_f),
    0xD04A6E1C: ("unknown_0xd04a6e1c", structs.decode_BIG_f),
    0x12B8E543: ("shock_wave_info", _decode_shock_wave_info),
    0xE8CD9627: ("phaazoid_projectile", structs.decode_BIG_Q),
    0x1DC69E38: ("damage_info", _decode_damage_info),
}
