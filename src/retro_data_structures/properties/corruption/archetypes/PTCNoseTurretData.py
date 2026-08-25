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

    class PTCNoseTurretDataJson(typing_extensions.TypedDict):
        aiming_prediction: float
        scanning_range_min: float
        scanning_range_max: float
        scanning_speed: float
        max_detection_angle: float
        unknown_0x494be648: float
        max_attack_angle: float
        max_rotation_speed: float
        max_rotation: float
        min_rotation: float
        max_pitch_speed: float
        max_pitch: float
        min_pitch: float
        projectile: int
        damage: json_util.JsonObject
        burst_delay: float
        unknown_0xb5702ca3: int
        burst_shot_delay: float
        unknown_0xaf28dc00: int
        sound_shot: int
        unknown_0x55d9abef: bool


@dataclasses.dataclass()
class PTCNoseTurretData(BaseProperty):
    aiming_prediction: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x395B81EF, original_name="AimingPrediction"),
        },
    )
    scanning_range_min: float = dataclasses.field(
        default=-90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x44E01377, original_name="ScanningRangeMin"),
        },
    )
    scanning_range_max: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA280BC96, original_name="ScanningRangeMax"),
        },
    )
    scanning_speed: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF71C6DD7, original_name="ScanningSpeed"),
        },
    )
    max_detection_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x679028BA, original_name="MaxDetectionAngle"),
        },
    )
    unknown_0x494be648: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x494BE648, original_name="Unknown"),
        },
    )
    max_attack_angle: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF11F7384, original_name="MaxAttackAngle"),
        },
    )
    max_rotation_speed: float = dataclasses.field(
        default=360.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50EEB9E3, original_name="MaxRotationSpeed"),
        },
    )
    max_rotation: float = dataclasses.field(
        default=135.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7721DEEA, original_name="MaxRotation"),
        },
    )
    min_rotation: float = dataclasses.field(
        default=-135.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x26D865B7, original_name="MinRotation"),
        },
    )
    max_pitch_speed: float = dataclasses.field(
        default=360.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9597A329, original_name="MaxPitchSpeed"),
        },
    )
    max_pitch: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD8C8763, original_name="MaxPitch"),
        },
    )
    min_pitch: float = dataclasses.field(
        default=-45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8DC3FF15, original_name="MinPitch"),
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
    burst_delay: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEB903473, original_name="BurstDelay"),
        },
    )
    unknown_0xb5702ca3: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB5702CA3, original_name="Unknown"),
        },
    )
    burst_shot_delay: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8F29E1E, original_name="BurstShotDelay"),
        },
    )
    unknown_0xaf28dc00: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAF28DC00, original_name="Unknown"),
        },
    )
    sound_shot: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC23A1955, original_name="Sound_Shot"),
        },
    )
    unknown_0x55d9abef: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x55D9ABEF, original_name="Unknown"),
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
        if property_count != 21:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x395B81EF
        aiming_prediction = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44E01377
        scanning_range_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA280BC96
        scanning_range_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF71C6DD7
        scanning_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x679028BA
        max_detection_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x494BE648
        unknown_0x494be648 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF11F7384
        max_attack_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50EEB9E3
        max_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7721DEEA
        max_rotation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26D865B7
        min_rotation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9597A329
        max_pitch_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD8C8763
        max_pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8DC3FF15
        min_pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF485DB9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB903473
        burst_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5702CA3
        unknown_0xb5702ca3 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8F29E1E
        burst_shot_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF28DC00
        unknown_0xaf28dc00 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC23A1955
        sound_shot = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55D9ABEF
        unknown_0x55d9abef = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            aiming_prediction,
            scanning_range_min,
            scanning_range_max,
            scanning_speed,
            max_detection_angle,
            unknown_0x494be648,
            max_attack_angle,
            max_rotation_speed,
            max_rotation,
            min_rotation,
            max_pitch_speed,
            max_pitch,
            min_pitch,
            projectile,
            damage,
            burst_delay,
            unknown_0xb5702ca3,
            burst_shot_delay,
            unknown_0xaf28dc00,
            sound_shot,
            unknown_0x55d9abef,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"9[\x81\xef")  # 0x395b81ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aiming_prediction))

        data.write(b"D\xe0\x13w")  # 0x44e01377
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scanning_range_min))

        data.write(b"\xa2\x80\xbc\x96")  # 0xa280bc96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scanning_range_max))

        data.write(b"\xf7\x1cm\xd7")  # 0xf71c6dd7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scanning_speed))

        data.write(b"g\x90(\xba")  # 0x679028ba
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_detection_angle))

        data.write(b"IK\xe6H")  # 0x494be648
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x494be648))

        data.write(b"\xf1\x1fs\x84")  # 0xf11f7384
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_angle))

        data.write(b"P\xee\xb9\xe3")  # 0x50eeb9e3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_rotation_speed))

        data.write(b"w!\xde\xea")  # 0x7721deea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_rotation))

        data.write(b"&\xd8e\xb7")  # 0x26d865b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_rotation))

        data.write(b"\x95\x97\xa3)")  # 0x9597a329
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_pitch_speed))

        data.write(b"\xcd\x8c\x87c")  # 0xcd8c8763
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_pitch))

        data.write(b"\x8d\xc3\xff\x15")  # 0x8dc3ff15
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_pitch))

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

        data.write(b"\xeb\x904s")  # 0xeb903473
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.burst_delay))

        data.write(b"\xb5p,\xa3")  # 0xb5702ca3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb5702ca3))

        data.write(b"\xe8\xf2\x9e\x1e")  # 0xe8f29e1e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.burst_shot_delay))

        data.write(b"\xaf(\xdc\x00")  # 0xaf28dc00
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xaf28dc00))

        data.write(b"\xc2:\x19U")  # 0xc23a1955
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_shot))

        data.write(b"U\xd9\xab\xef")  # 0x55d9abef
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x55d9abef))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PTCNoseTurretDataJson", data)
        return cls(
            aiming_prediction=json_data["aiming_prediction"],
            scanning_range_min=json_data["scanning_range_min"],
            scanning_range_max=json_data["scanning_range_max"],
            scanning_speed=json_data["scanning_speed"],
            max_detection_angle=json_data["max_detection_angle"],
            unknown_0x494be648=json_data["unknown_0x494be648"],
            max_attack_angle=json_data["max_attack_angle"],
            max_rotation_speed=json_data["max_rotation_speed"],
            max_rotation=json_data["max_rotation"],
            min_rotation=json_data["min_rotation"],
            max_pitch_speed=json_data["max_pitch_speed"],
            max_pitch=json_data["max_pitch"],
            min_pitch=json_data["min_pitch"],
            projectile=json_data["projectile"],
            damage=DamageInfo.from_json(json_data["damage"]),
            burst_delay=json_data["burst_delay"],
            unknown_0xb5702ca3=json_data["unknown_0xb5702ca3"],
            burst_shot_delay=json_data["burst_shot_delay"],
            unknown_0xaf28dc00=json_data["unknown_0xaf28dc00"],
            sound_shot=json_data["sound_shot"],
            unknown_0x55d9abef=json_data["unknown_0x55d9abef"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "aiming_prediction": self.aiming_prediction,
            "scanning_range_min": self.scanning_range_min,
            "scanning_range_max": self.scanning_range_max,
            "scanning_speed": self.scanning_speed,
            "max_detection_angle": self.max_detection_angle,
            "unknown_0x494be648": self.unknown_0x494be648,
            "max_attack_angle": self.max_attack_angle,
            "max_rotation_speed": self.max_rotation_speed,
            "max_rotation": self.max_rotation,
            "min_rotation": self.min_rotation,
            "max_pitch_speed": self.max_pitch_speed,
            "max_pitch": self.max_pitch,
            "min_pitch": self.min_pitch,
            "projectile": self.projectile,
            "damage": self.damage.to_json(),
            "burst_delay": self.burst_delay,
            "unknown_0xb5702ca3": self.unknown_0xb5702ca3,
            "burst_shot_delay": self.burst_shot_delay,
            "unknown_0xaf28dc00": self.unknown_0xaf28dc00,
            "sound_shot": self.sound_shot,
            "unknown_0x55d9abef": self.unknown_0x55d9abef,
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x395B81EF: ("aiming_prediction", structs.decode_BIG_f),
    0x44E01377: ("scanning_range_min", structs.decode_BIG_f),
    0xA280BC96: ("scanning_range_max", structs.decode_BIG_f),
    0xF71C6DD7: ("scanning_speed", structs.decode_BIG_f),
    0x679028BA: ("max_detection_angle", structs.decode_BIG_f),
    0x494BE648: ("unknown_0x494be648", structs.decode_BIG_f),
    0xF11F7384: ("max_attack_angle", structs.decode_BIG_f),
    0x50EEB9E3: ("max_rotation_speed", structs.decode_BIG_f),
    0x7721DEEA: ("max_rotation", structs.decode_BIG_f),
    0x26D865B7: ("min_rotation", structs.decode_BIG_f),
    0x9597A329: ("max_pitch_speed", structs.decode_BIG_f),
    0xCD8C8763: ("max_pitch", structs.decode_BIG_f),
    0x8DC3FF15: ("min_pitch", structs.decode_BIG_f),
    0xEF485DB9: ("projectile", structs.decode_BIG_Q),
    0x337F9524: ("damage", _decode_damage),
    0xEB903473: ("burst_delay", structs.decode_BIG_f),
    0xB5702CA3: ("unknown_0xb5702ca3", structs.decode_BIG_l),
    0xE8F29E1E: ("burst_shot_delay", structs.decode_BIG_f),
    0xAF28DC00: ("unknown_0xaf28dc00", structs.decode_BIG_l),
    0xC23A1955: ("sound_shot", structs.decode_BIG_Q),
    0x55D9ABEF: ("unknown_0x55d9abef", structs.decode_BIG_bool_),
}
