# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayer_HyperModeJson(typing_extensions.TypedDict):
        hyper_mode_invulnerable_phazon_loss: bool
        hyper_mode_invulnerable_time: float
        unknown_0x1a75c2d0: float
        unknown_0xfb9972fc: bool
        unknown_0x699dff41: json_util.JsonObject
        unknown_0x48cc79f2: float
        unknown_0x128e6ecc: bool
        unknown_0x808ae371: json_util.JsonObject
        unknown_0xfd4c4fee: float
        unknown_0x23c70cb5: float
        hyper_mode_phazon_level: float
        hyper_mode_phazon_capacity: float
        hyper_mode_danger_percentage: float
        unknown_0xa3748fa1: float
        unknown_0x16bc1c24: float
        unknown_0xedff39f1: float
        hyper_mode_phazon_ball_rate: float
        hyper_mode_damage_multiplier: float
        unknown_0xdb1120f2: float
        unknown_0xba8cb0f2: float
        unknown_0x3c18c25c: float
        unknown_0xf74411f9: float
        unknown_0xea412141: float
        unknown_0xb03510b7: float
        unknown_0x3f07961a: float
        hyper_mode_initial_damage: json_util.JsonObject
        hyper_mode_damage: json_util.JsonObject
        hyper_mode_phaaze_damage: json_util.JsonObject
        hyper_mode_critical_time: float
        unknown_0xcd562633: float
        hyper_mode_critical_clear: float
        hyper_mode_venting_control: json_util.JsonObject


@dataclasses.dataclass()
class TweakPlayer_HyperMode(BaseProperty):
    hyper_mode_invulnerable_phazon_loss: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x31FFBFE7, original_name="HyperModeInvulnerablePhazonLoss"),
        },
    )
    hyper_mode_invulnerable_time: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FDFAA62, original_name="HyperModeInvulnerableTime"),
        },
    )
    unknown_0x1a75c2d0: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A75C2D0, original_name="Unknown"),
        },
    )
    unknown_0xfb9972fc: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFB9972FC, original_name="Unknown"),
        },
    )
    unknown_0x699dff41: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x699DFF41, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x48cc79f2: float = dataclasses.field(
        default=14.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x48CC79F2, original_name="Unknown"),
        },
    )
    unknown_0x128e6ecc: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x128E6ECC, original_name="Unknown"),
        },
    )
    unknown_0x808ae371: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x808AE371, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xfd4c4fee: float = dataclasses.field(
        default=14.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFD4C4FEE, original_name="Unknown"),
        },
    )
    unknown_0x23c70cb5: float = dataclasses.field(
        default=14.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23C70CB5, original_name="Unknown"),
        },
    )
    hyper_mode_phazon_level: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAB40BED3, original_name="HyperModePhazonLevel"),
        },
    )
    hyper_mode_phazon_capacity: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8ED2E3FB, original_name="HyperModePhazonCapacity"),
        },
    )
    hyper_mode_danger_percentage: float = dataclasses.field(
        default=70.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA2482028, original_name="HyperModeDangerPercentage"),
        },
    )
    unknown_0xa3748fa1: float = dataclasses.field(
        default=5.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA3748FA1, original_name="Unknown"),
        },
    )
    unknown_0x16bc1c24: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16BC1C24, original_name="Unknown"),
        },
    )
    unknown_0xedff39f1: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEDFF39F1, original_name="Unknown"),
        },
    )
    hyper_mode_phazon_ball_rate: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9CEDEA06, original_name="HyperModePhazonBallRate?"),
        },
    )
    hyper_mode_damage_multiplier: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x56F3C854, original_name="HyperModeDamageMultiplier"),
        },
    )
    unknown_0xdb1120f2: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDB1120F2, original_name="Unknown"),
        },
    )
    unknown_0xba8cb0f2: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA8CB0F2, original_name="Unknown"),
        },
    )
    unknown_0x3c18c25c: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3C18C25C, original_name="Unknown"),
        },
    )
    unknown_0xf74411f9: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF74411F9, original_name="Unknown"),
        },
    )
    unknown_0xea412141: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEA412141, original_name="Unknown"),
        },
    )
    unknown_0xb03510b7: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB03510B7, original_name="Unknown"),
        },
    )
    unknown_0x3f07961a: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3F07961A, original_name="Unknown"),
        },
    )
    hyper_mode_initial_damage: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x711296E2,
                original_name="HyperModeInitialDamage",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    hyper_mode_damage: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xB148913B,
                original_name="HyperModeDamage",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    hyper_mode_phaaze_damage: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xC5F1943D,
                original_name="HyperModePhaazeDamage",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    hyper_mode_critical_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B6624B1, original_name="HyperModeCriticalTime"),
        },
    )
    unknown_0xcd562633: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD562633, original_name="Unknown"),
        },
    )
    hyper_mode_critical_clear: float = dataclasses.field(
        default=75.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBE038CBF, original_name="HyperModeCriticalClear"),
        },
    )
    hyper_mode_venting_control: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x0F35EE69,
                original_name="HyperModeVentingControl",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
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
        if property_count != 32:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31FFBFE7
        hyper_mode_invulnerable_phazon_loss = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FDFAA62
        hyper_mode_invulnerable_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A75C2D0
        unknown_0x1a75c2d0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB9972FC
        unknown_0xfb9972fc = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x699DFF41
        unknown_0x699dff41 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48CC79F2
        unknown_0x48cc79f2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x128E6ECC
        unknown_0x128e6ecc = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x808AE371
        unknown_0x808ae371 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFD4C4FEE
        unknown_0xfd4c4fee = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23C70CB5
        unknown_0x23c70cb5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB40BED3
        hyper_mode_phazon_level = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ED2E3FB
        hyper_mode_phazon_capacity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA2482028
        hyper_mode_danger_percentage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3748FA1
        unknown_0xa3748fa1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16BC1C24
        unknown_0x16bc1c24 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDFF39F1
        unknown_0xedff39f1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9CEDEA06
        hyper_mode_phazon_ball_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56F3C854
        hyper_mode_damage_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDB1120F2
        unknown_0xdb1120f2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA8CB0F2
        unknown_0xba8cb0f2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3C18C25C
        unknown_0x3c18c25c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF74411F9
        unknown_0xf74411f9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA412141
        unknown_0xea412141 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB03510B7
        unknown_0xb03510b7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3F07961A
        unknown_0x3f07961a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x711296E2
        hyper_mode_initial_damage = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB148913B
        hyper_mode_damage = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5F1943D
        hyper_mode_phaaze_damage = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B6624B1
        hyper_mode_critical_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD562633
        unknown_0xcd562633 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE038CBF
        hyper_mode_critical_clear = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F35EE69
        hyper_mode_venting_control = Spline.from_stream(data, game, property_size)

        return cls(
            hyper_mode_invulnerable_phazon_loss,
            hyper_mode_invulnerable_time,
            unknown_0x1a75c2d0,
            unknown_0xfb9972fc,
            unknown_0x699dff41,
            unknown_0x48cc79f2,
            unknown_0x128e6ecc,
            unknown_0x808ae371,
            unknown_0xfd4c4fee,
            unknown_0x23c70cb5,
            hyper_mode_phazon_level,
            hyper_mode_phazon_capacity,
            hyper_mode_danger_percentage,
            unknown_0xa3748fa1,
            unknown_0x16bc1c24,
            unknown_0xedff39f1,
            hyper_mode_phazon_ball_rate,
            hyper_mode_damage_multiplier,
            unknown_0xdb1120f2,
            unknown_0xba8cb0f2,
            unknown_0x3c18c25c,
            unknown_0xf74411f9,
            unknown_0xea412141,
            unknown_0xb03510b7,
            unknown_0x3f07961a,
            hyper_mode_initial_damage,
            hyper_mode_damage,
            hyper_mode_phaaze_damage,
            hyper_mode_critical_time,
            unknown_0xcd562633,
            hyper_mode_critical_clear,
            hyper_mode_venting_control,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00 ")  # 32 properties

        data.write(b"1\xff\xbf\xe7")  # 0x31ffbfe7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_invulnerable_phazon_loss))

        data.write(b"\x7f\xdf\xaab")  # 0x7fdfaa62
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_invulnerable_time))

        data.write(b"\x1au\xc2\xd0")  # 0x1a75c2d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1a75c2d0))

        data.write(b"\xfb\x99r\xfc")  # 0xfb9972fc
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xfb9972fc))

        data.write(b"i\x9d\xffA")  # 0x699dff41
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x699dff41.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"H\xccy\xf2")  # 0x48cc79f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x48cc79f2))

        data.write(b"\x12\x8en\xcc")  # 0x128e6ecc
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x128e6ecc))

        data.write(b"\x80\x8a\xe3q")  # 0x808ae371
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x808ae371.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfdLO\xee")  # 0xfd4c4fee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfd4c4fee))

        data.write(b"#\xc7\x0c\xb5")  # 0x23c70cb5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x23c70cb5))

        data.write(b"\xab@\xbe\xd3")  # 0xab40bed3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phazon_level))

        data.write(b"\x8e\xd2\xe3\xfb")  # 0x8ed2e3fb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phazon_capacity))

        data.write(b"\xa2H (")  # 0xa2482028
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_danger_percentage))

        data.write(b"\xa3t\x8f\xa1")  # 0xa3748fa1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa3748fa1))

        data.write(b"\x16\xbc\x1c$")  # 0x16bc1c24
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x16bc1c24))

        data.write(b"\xed\xff9\xf1")  # 0xedff39f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xedff39f1))

        data.write(b"\x9c\xed\xea\x06")  # 0x9cedea06
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phazon_ball_rate))

        data.write(b"V\xf3\xc8T")  # 0x56f3c854
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_damage_multiplier))

        data.write(b"\xdb\x11 \xf2")  # 0xdb1120f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdb1120f2))

        data.write(b"\xba\x8c\xb0\xf2")  # 0xba8cb0f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xba8cb0f2))

        data.write(b"<\x18\xc2\\")  # 0x3c18c25c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3c18c25c))

        data.write(b"\xf7D\x11\xf9")  # 0xf74411f9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf74411f9))

        data.write(b"\xeaA!A")  # 0xea412141
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xea412141))

        data.write(b"\xb05\x10\xb7")  # 0xb03510b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb03510b7))

        data.write(b"?\x07\x96\x1a")  # 0x3f07961a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3f07961a))

        data.write(b"q\x12\x96\xe2")  # 0x711296e2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode_initial_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb1H\x91;")  # 0xb148913b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc5\xf1\x94=")  # 0xc5f1943d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode_phaaze_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+f$\xb1")  # 0x2b6624b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_critical_time))

        data.write(b"\xcdV&3")  # 0xcd562633
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd562633))

        data.write(b"\xbe\x03\x8c\xbf")  # 0xbe038cbf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_critical_clear))

        data.write(b"\x0f5\xeei")  # 0xf35ee69
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode_venting_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_HyperModeJson", data)
        return cls(
            hyper_mode_invulnerable_phazon_loss=json_data["hyper_mode_invulnerable_phazon_loss"],
            hyper_mode_invulnerable_time=json_data["hyper_mode_invulnerable_time"],
            unknown_0x1a75c2d0=json_data["unknown_0x1a75c2d0"],
            unknown_0xfb9972fc=json_data["unknown_0xfb9972fc"],
            unknown_0x699dff41=Spline.from_json(json_data["unknown_0x699dff41"]),
            unknown_0x48cc79f2=json_data["unknown_0x48cc79f2"],
            unknown_0x128e6ecc=json_data["unknown_0x128e6ecc"],
            unknown_0x808ae371=Spline.from_json(json_data["unknown_0x808ae371"]),
            unknown_0xfd4c4fee=json_data["unknown_0xfd4c4fee"],
            unknown_0x23c70cb5=json_data["unknown_0x23c70cb5"],
            hyper_mode_phazon_level=json_data["hyper_mode_phazon_level"],
            hyper_mode_phazon_capacity=json_data["hyper_mode_phazon_capacity"],
            hyper_mode_danger_percentage=json_data["hyper_mode_danger_percentage"],
            unknown_0xa3748fa1=json_data["unknown_0xa3748fa1"],
            unknown_0x16bc1c24=json_data["unknown_0x16bc1c24"],
            unknown_0xedff39f1=json_data["unknown_0xedff39f1"],
            hyper_mode_phazon_ball_rate=json_data["hyper_mode_phazon_ball_rate"],
            hyper_mode_damage_multiplier=json_data["hyper_mode_damage_multiplier"],
            unknown_0xdb1120f2=json_data["unknown_0xdb1120f2"],
            unknown_0xba8cb0f2=json_data["unknown_0xba8cb0f2"],
            unknown_0x3c18c25c=json_data["unknown_0x3c18c25c"],
            unknown_0xf74411f9=json_data["unknown_0xf74411f9"],
            unknown_0xea412141=json_data["unknown_0xea412141"],
            unknown_0xb03510b7=json_data["unknown_0xb03510b7"],
            unknown_0x3f07961a=json_data["unknown_0x3f07961a"],
            hyper_mode_initial_damage=DamageVulnerability.from_json(json_data["hyper_mode_initial_damage"]),
            hyper_mode_damage=DamageVulnerability.from_json(json_data["hyper_mode_damage"]),
            hyper_mode_phaaze_damage=DamageVulnerability.from_json(json_data["hyper_mode_phaaze_damage"]),
            hyper_mode_critical_time=json_data["hyper_mode_critical_time"],
            unknown_0xcd562633=json_data["unknown_0xcd562633"],
            hyper_mode_critical_clear=json_data["hyper_mode_critical_clear"],
            hyper_mode_venting_control=Spline.from_json(json_data["hyper_mode_venting_control"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hyper_mode_invulnerable_phazon_loss": self.hyper_mode_invulnerable_phazon_loss,
            "hyper_mode_invulnerable_time": self.hyper_mode_invulnerable_time,
            "unknown_0x1a75c2d0": self.unknown_0x1a75c2d0,
            "unknown_0xfb9972fc": self.unknown_0xfb9972fc,
            "unknown_0x699dff41": self.unknown_0x699dff41.to_json(),
            "unknown_0x48cc79f2": self.unknown_0x48cc79f2,
            "unknown_0x128e6ecc": self.unknown_0x128e6ecc,
            "unknown_0x808ae371": self.unknown_0x808ae371.to_json(),
            "unknown_0xfd4c4fee": self.unknown_0xfd4c4fee,
            "unknown_0x23c70cb5": self.unknown_0x23c70cb5,
            "hyper_mode_phazon_level": self.hyper_mode_phazon_level,
            "hyper_mode_phazon_capacity": self.hyper_mode_phazon_capacity,
            "hyper_mode_danger_percentage": self.hyper_mode_danger_percentage,
            "unknown_0xa3748fa1": self.unknown_0xa3748fa1,
            "unknown_0x16bc1c24": self.unknown_0x16bc1c24,
            "unknown_0xedff39f1": self.unknown_0xedff39f1,
            "hyper_mode_phazon_ball_rate": self.hyper_mode_phazon_ball_rate,
            "hyper_mode_damage_multiplier": self.hyper_mode_damage_multiplier,
            "unknown_0xdb1120f2": self.unknown_0xdb1120f2,
            "unknown_0xba8cb0f2": self.unknown_0xba8cb0f2,
            "unknown_0x3c18c25c": self.unknown_0x3c18c25c,
            "unknown_0xf74411f9": self.unknown_0xf74411f9,
            "unknown_0xea412141": self.unknown_0xea412141,
            "unknown_0xb03510b7": self.unknown_0xb03510b7,
            "unknown_0x3f07961a": self.unknown_0x3f07961a,
            "hyper_mode_initial_damage": self.hyper_mode_initial_damage.to_json(),
            "hyper_mode_damage": self.hyper_mode_damage.to_json(),
            "hyper_mode_phaaze_damage": self.hyper_mode_phaaze_damage.to_json(),
            "hyper_mode_critical_time": self.hyper_mode_critical_time,
            "unknown_0xcd562633": self.unknown_0xcd562633,
            "hyper_mode_critical_clear": self.hyper_mode_critical_clear,
            "hyper_mode_venting_control": self.hyper_mode_venting_control.to_json(),
        }


def _decode_unknown_0x699dff41(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x808ae371(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hyper_mode_initial_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hyper_mode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hyper_mode_phaaze_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hyper_mode_venting_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x31FFBFE7: ("hyper_mode_invulnerable_phazon_loss", structs.decode_BIG_bool_),
    0x7FDFAA62: ("hyper_mode_invulnerable_time", structs.decode_BIG_f),
    0x1A75C2D0: ("unknown_0x1a75c2d0", structs.decode_BIG_f),
    0xFB9972FC: ("unknown_0xfb9972fc", structs.decode_BIG_bool_),
    0x699DFF41: ("unknown_0x699dff41", _decode_unknown_0x699dff41),
    0x48CC79F2: ("unknown_0x48cc79f2", structs.decode_BIG_f),
    0x128E6ECC: ("unknown_0x128e6ecc", structs.decode_BIG_bool_),
    0x808AE371: ("unknown_0x808ae371", _decode_unknown_0x808ae371),
    0xFD4C4FEE: ("unknown_0xfd4c4fee", structs.decode_BIG_f),
    0x23C70CB5: ("unknown_0x23c70cb5", structs.decode_BIG_f),
    0xAB40BED3: ("hyper_mode_phazon_level", structs.decode_BIG_f),
    0x8ED2E3FB: ("hyper_mode_phazon_capacity", structs.decode_BIG_f),
    0xA2482028: ("hyper_mode_danger_percentage", structs.decode_BIG_f),
    0xA3748FA1: ("unknown_0xa3748fa1", structs.decode_BIG_f),
    0x16BC1C24: ("unknown_0x16bc1c24", structs.decode_BIG_f),
    0xEDFF39F1: ("unknown_0xedff39f1", structs.decode_BIG_f),
    0x9CEDEA06: ("hyper_mode_phazon_ball_rate", structs.decode_BIG_f),
    0x56F3C854: ("hyper_mode_damage_multiplier", structs.decode_BIG_f),
    0xDB1120F2: ("unknown_0xdb1120f2", structs.decode_BIG_f),
    0xBA8CB0F2: ("unknown_0xba8cb0f2", structs.decode_BIG_f),
    0x3C18C25C: ("unknown_0x3c18c25c", structs.decode_BIG_f),
    0xF74411F9: ("unknown_0xf74411f9", structs.decode_BIG_f),
    0xEA412141: ("unknown_0xea412141", structs.decode_BIG_f),
    0xB03510B7: ("unknown_0xb03510b7", structs.decode_BIG_f),
    0x3F07961A: ("unknown_0x3f07961a", structs.decode_BIG_f),
    0x711296E2: ("hyper_mode_initial_damage", _decode_hyper_mode_initial_damage),
    0xB148913B: ("hyper_mode_damage", _decode_hyper_mode_damage),
    0xC5F1943D: ("hyper_mode_phaaze_damage", _decode_hyper_mode_phaaze_damage),
    0x2B6624B1: ("hyper_mode_critical_time", structs.decode_BIG_f),
    0xCD562633: ("unknown_0xcd562633", structs.decode_BIG_f),
    0xBE038CBF: ("hyper_mode_critical_clear", structs.decode_BIG_f),
    0x0F35EE69: ("hyper_mode_venting_control", _decode_hyper_mode_venting_control),
}
