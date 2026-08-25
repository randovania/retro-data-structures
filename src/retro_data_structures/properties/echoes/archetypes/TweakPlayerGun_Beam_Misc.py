# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.common.archetypes.TDamageInfo import TDamageInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayerGun_Beam_MiscJson(typing_extensions.TypedDict):
        unknown_0x8aacfc27: json_util.JsonObject
        unknown_0xa054ff1c: json_util.JsonObject
        imploder_annihilator: json_util.JsonObject
        ai_burn_damage: float
        unknown_0x4848f444: float
        max_absorbed_phazon_shots: int
        unknown_0x3ae5d1fa: float


@dataclasses.dataclass()
class TweakPlayerGun_Beam_Misc(BaseProperty):
    unknown_0x8aacfc27: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0x8AACFC27,
                original_name="Unknown",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    unknown_0xa054ff1c: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0xA054FF1C,
                original_name="Unknown",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    imploder_annihilator: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0xABFA93E9,
                original_name="Imploder_Annihilator",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    ai_burn_damage: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8F9BF33, original_name="AIBurnDamage"),
        },
    )
    unknown_0x4848f444: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4848F444, original_name="Unknown"),
        },
    )
    max_absorbed_phazon_shots: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1E710222, original_name="MaxAbsorbedPhazonShots"),
        },
    )
    unknown_0x3ae5d1fa: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3AE5D1FA, original_name="Unknown"),
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
        assert property_id == 0x8AACFC27
        unknown_0x8aacfc27 = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 1,
                "damage_amount": 1.0,
                "radius_damage_amount": 1.0,
                "damage_radius": 0.0,
                "knock_back_power": 0.10000000149011612,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA054FF1C
        unknown_0xa054ff1c = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 2,
                "damage_amount": 0.800000011920929,
                "radius_damage_amount": 0.800000011920929,
                "damage_radius": 0.0,
                "knock_back_power": 0.800000011920929,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xABFA93E9
        imploder_annihilator = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 3,
                "damage_amount": 0.800000011920929,
                "radius_damage_amount": 0.800000011920929,
                "damage_radius": 0.0,
                "knock_back_power": 0.800000011920929,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8F9BF33
        ai_burn_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4848F444
        unknown_0x4848f444 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E710222
        max_absorbed_phazon_shots = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3AE5D1FA
        unknown_0x3ae5d1fa = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            unknown_0x8aacfc27,
            unknown_0xa054ff1c,
            imploder_annihilator,
            ai_burn_damage,
            unknown_0x4848f444,
            max_absorbed_phazon_shots,
            unknown_0x3ae5d1fa,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\x8a\xac\xfc'")  # 0x8aacfc27
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x8aacfc27.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 1,
                "damage_amount": 1.0,
                "radius_damage_amount": 1.0,
                "damage_radius": 0.0,
                "knock_back_power": 0.10000000149011612,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa0T\xff\x1c")  # 0xa054ff1c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xa054ff1c.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 2,
                "damage_amount": 0.800000011920929,
                "radius_damage_amount": 0.800000011920929,
                "damage_radius": 0.0,
                "knock_back_power": 0.800000011920929,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xab\xfa\x93\xe9")  # 0xabfa93e9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.imploder_annihilator.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 3,
                "damage_amount": 0.800000011920929,
                "radius_damage_amount": 0.800000011920929,
                "damage_radius": 0.0,
                "knock_back_power": 0.800000011920929,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf8\xf9\xbf3")  # 0xf8f9bf33
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ai_burn_damage))

        data.write(b"HH\xf4D")  # 0x4848f444
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4848f444))

        data.write(b'\x1eq\x02"')  # 0x1e710222
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_absorbed_phazon_shots))

        data.write(b":\xe5\xd1\xfa")  # 0x3ae5d1fa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3ae5d1fa))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_Beam_MiscJson", data)
        return cls(
            unknown_0x8aacfc27=TDamageInfo.from_json(json_data["unknown_0x8aacfc27"]),
            unknown_0xa054ff1c=TDamageInfo.from_json(json_data["unknown_0xa054ff1c"]),
            imploder_annihilator=TDamageInfo.from_json(json_data["imploder_annihilator"]),
            ai_burn_damage=json_data["ai_burn_damage"],
            unknown_0x4848f444=json_data["unknown_0x4848f444"],
            max_absorbed_phazon_shots=json_data["max_absorbed_phazon_shots"],
            unknown_0x3ae5d1fa=json_data["unknown_0x3ae5d1fa"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x8aacfc27": self.unknown_0x8aacfc27.to_json(),
            "unknown_0xa054ff1c": self.unknown_0xa054ff1c.to_json(),
            "imploder_annihilator": self.imploder_annihilator.to_json(),
            "ai_burn_damage": self.ai_burn_damage,
            "unknown_0x4848f444": self.unknown_0x4848f444,
            "max_absorbed_phazon_shots": self.max_absorbed_phazon_shots,
            "unknown_0x3ae5d1fa": self.unknown_0x3ae5d1fa,
        }


def _decode_unknown_0x8aacfc27(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "weapon_type": 1,
            "damage_amount": 1.0,
            "radius_damage_amount": 1.0,
            "damage_radius": 0.0,
            "knock_back_power": 0.10000000149011612,
        },
    )


def _decode_unknown_0xa054ff1c(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "weapon_type": 2,
            "damage_amount": 0.800000011920929,
            "radius_damage_amount": 0.800000011920929,
            "damage_radius": 0.0,
            "knock_back_power": 0.800000011920929,
        },
    )


def _decode_imploder_annihilator(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "weapon_type": 3,
            "damage_amount": 0.800000011920929,
            "radius_damage_amount": 0.800000011920929,
            "damage_radius": 0.0,
            "knock_back_power": 0.800000011920929,
        },
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8AACFC27: ("unknown_0x8aacfc27", _decode_unknown_0x8aacfc27),
    0xA054FF1C: ("unknown_0xa054ff1c", _decode_unknown_0xa054ff1c),
    0xABFA93E9: ("imploder_annihilator", _decode_imploder_annihilator),
    0xF8F9BF33: ("ai_burn_damage", structs.decode_BIG_f),
    0x4848F444: ("unknown_0x4848f444", structs.decode_BIG_f),
    0x1E710222: ("max_absorbed_phazon_shots", structs.decode_BIG_l),
    0x3AE5D1FA: ("unknown_0x3ae5d1fa", structs.decode_BIG_f),
}
