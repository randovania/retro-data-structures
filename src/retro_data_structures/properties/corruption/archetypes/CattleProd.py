# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CattleProdJson(typing_extensions.TypedDict):
        damage: json_util.JsonObject
        hyper_damage: json_util.JsonObject
        max_attack_dist: float
        visor_effect: int
        stun_time: float
        unknown: float
        player_impact_sound: int


@dataclasses.dataclass()
class CattleProd(BaseProperty):
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
    hyper_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xB3DABF84,
                original_name="HyperDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    max_attack_dist: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2ED25F50, original_name="MaxAttackDist"),
        },
    )
    visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART", "ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE9C8E2BD, original_name="VisorEffect"),
        },
    )
    stun_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7E192395, original_name="StunTime"),
        },
    )
    unknown: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5D1652E2, original_name="Unknown"),
        },
    )
    player_impact_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE33A996D, original_name="PlayerImpactSound"),
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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3DABF84
        hyper_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ED25F50
        max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9C8E2BD
        visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E192395
        stun_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D1652E2
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE33A996D
        player_impact_sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(damage, hyper_damage, max_attack_dist, visor_effect, stun_time, unknown, player_impact_sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3\xda\xbf\x84")  # 0xb3dabf84
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b".\xd2_P")  # 0x2ed25f50
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_dist))

        data.write(b"\xe9\xc8\xe2\xbd")  # 0xe9c8e2bd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_effect))

        data.write(b"~\x19#\x95")  # 0x7e192395
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_time))

        data.write(b"]\x16R\xe2")  # 0x5d1652e2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\xe3:\x99m")  # 0xe33a996d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.player_impact_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CattleProdJson", data)
        return cls(
            damage=DamageInfo.from_json(json_data["damage"]),
            hyper_damage=DamageInfo.from_json(json_data["hyper_damage"]),
            max_attack_dist=json_data["max_attack_dist"],
            visor_effect=json_data["visor_effect"],
            stun_time=json_data["stun_time"],
            unknown=json_data["unknown"],
            player_impact_sound=json_data["player_impact_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "damage": self.damage.to_json(),
            "hyper_damage": self.hyper_damage.to_json(),
            "max_attack_dist": self.max_attack_dist,
            "visor_effect": self.visor_effect,
            "stun_time": self.stun_time,
            "unknown": self.unknown,
            "player_impact_sound": self.player_impact_sound,
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_hyper_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x337F9524: ("damage", _decode_damage),
    0xB3DABF84: ("hyper_damage", _decode_hyper_damage),
    0x2ED25F50: ("max_attack_dist", structs.decode_BIG_f),
    0xE9C8E2BD: ("visor_effect", structs.decode_BIG_Q),
    0x7E192395: ("stun_time", structs.decode_BIG_f),
    0x5D1652E2: ("unknown", structs.decode_BIG_f),
    0xE33A996D: ("player_impact_sound", structs.decode_BIG_Q),
}
