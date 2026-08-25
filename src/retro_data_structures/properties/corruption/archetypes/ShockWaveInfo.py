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

    class ShockWaveInfoJson(typing_extensions.TypedDict):
        shock_wave_effect: int
        damage: json_util.JsonObject
        duration: float
        knockback_decay_rate: float
        unknown_0x60df1486: bool
        radius: float
        height: float
        unknown_0xcf6c1de9: float
        radial_velocity: float
        radial_velocity_acceleration: float
        visor_electric_effect: int
        sound_visor_electric: int
        optional_shockwave_sound: int


@dataclasses.dataclass()
class ShockWaveInfo(BaseProperty):
    shock_wave_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x369F7D09, original_name="ShockWaveEffect"),
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
    duration: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B51E23F, original_name="Duration"),
        },
    )
    knockback_decay_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0320895B, original_name="KnockbackDecayRate"),
        },
    )
    unknown_0x60df1486: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x60DF1486, original_name="Unknown"),
        },
    )
    radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78C507EB, original_name="Radius"),
        },
    )
    height: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC2BE030D, original_name="Height"),
        },
    )
    unknown_0xcf6c1de9: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF6C1DE9, original_name="Unknown"),
        },
    )
    radial_velocity: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4CD1459B, original_name="RadialVelocity"),
        },
    )
    radial_velocity_acceleration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0A57B09B, original_name="RadialVelocityAcceleration"),
        },
    )
    visor_electric_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBD321538, original_name="VisorElectricEffect"),
        },
    )
    sound_visor_electric: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA2850B37, original_name="Sound_VisorElectric"),
        },
    )
    optional_shockwave_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x56936C97, original_name="OptionalShockwaveSound"),
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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x369F7D09
        shock_wave_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B51E23F
        duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0320895B
        knockback_decay_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60DF1486
        unknown_0x60df1486 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78C507EB
        radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2BE030D
        height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF6C1DE9
        unknown_0xcf6c1de9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4CD1459B
        radial_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A57B09B
        radial_velocity_acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD321538
        visor_electric_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA2850B37
        sound_visor_electric = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56936C97
        optional_shockwave_sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            shock_wave_effect,
            damage,
            duration,
            knockback_decay_rate,
            unknown_0x60df1486,
            radius,
            height,
            unknown_0xcf6c1de9,
            radial_velocity,
            radial_velocity_acceleration,
            visor_electric_effect,
            sound_visor_electric,
            optional_shockwave_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\r")  # 13 properties

        data.write(b"6\x9f}\t")  # 0x369f7d09
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.shock_wave_effect))

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8bQ\xe2?")  # 0x8b51e23f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b"\x03 \x89[")  # 0x320895b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.knockback_decay_rate))

        data.write(b"`\xdf\x14\x86")  # 0x60df1486
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x60df1486))

        data.write(b"x\xc5\x07\xeb")  # 0x78c507eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.radius))

        data.write(b"\xc2\xbe\x03\r")  # 0xc2be030d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.height))

        data.write(b"\xcfl\x1d\xe9")  # 0xcf6c1de9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcf6c1de9))

        data.write(b"L\xd1E\x9b")  # 0x4cd1459b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.radial_velocity))

        data.write(b"\nW\xb0\x9b")  # 0xa57b09b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.radial_velocity_acceleration))

        data.write(b"\xbd2\x158")  # 0xbd321538
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_electric_effect))

        data.write(b"\xa2\x85\x0b7")  # 0xa2850b37
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_visor_electric))

        data.write(b"V\x93l\x97")  # 0x56936c97
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.optional_shockwave_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShockWaveInfoJson", data)
        return cls(
            shock_wave_effect=json_data["shock_wave_effect"],
            damage=DamageInfo.from_json(json_data["damage"]),
            duration=json_data["duration"],
            knockback_decay_rate=json_data["knockback_decay_rate"],
            unknown_0x60df1486=json_data["unknown_0x60df1486"],
            radius=json_data["radius"],
            height=json_data["height"],
            unknown_0xcf6c1de9=json_data["unknown_0xcf6c1de9"],
            radial_velocity=json_data["radial_velocity"],
            radial_velocity_acceleration=json_data["radial_velocity_acceleration"],
            visor_electric_effect=json_data["visor_electric_effect"],
            sound_visor_electric=json_data["sound_visor_electric"],
            optional_shockwave_sound=json_data["optional_shockwave_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "shock_wave_effect": self.shock_wave_effect,
            "damage": self.damage.to_json(),
            "duration": self.duration,
            "knockback_decay_rate": self.knockback_decay_rate,
            "unknown_0x60df1486": self.unknown_0x60df1486,
            "radius": self.radius,
            "height": self.height,
            "unknown_0xcf6c1de9": self.unknown_0xcf6c1de9,
            "radial_velocity": self.radial_velocity,
            "radial_velocity_acceleration": self.radial_velocity_acceleration,
            "visor_electric_effect": self.visor_electric_effect,
            "sound_visor_electric": self.sound_visor_electric,
            "optional_shockwave_sound": self.optional_shockwave_sound,
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x369F7D09: ("shock_wave_effect", structs.decode_BIG_Q),
    0x337F9524: ("damage", _decode_damage),
    0x8B51E23F: ("duration", structs.decode_BIG_f),
    0x0320895B: ("knockback_decay_rate", structs.decode_BIG_f),
    0x60DF1486: ("unknown_0x60df1486", structs.decode_BIG_bool_),
    0x78C507EB: ("radius", structs.decode_BIG_f),
    0xC2BE030D: ("height", structs.decode_BIG_f),
    0xCF6C1DE9: ("unknown_0xcf6c1de9", structs.decode_BIG_f),
    0x4CD1459B: ("radial_velocity", structs.decode_BIG_f),
    0x0A57B09B: ("radial_velocity_acceleration", structs.decode_BIG_f),
    0xBD321538: ("visor_electric_effect", structs.decode_BIG_Q),
    0xA2850B37: ("sound_visor_electric", structs.decode_BIG_Q),
    0x56936C97: ("optional_shockwave_sound", structs.decode_BIG_Q),
}
