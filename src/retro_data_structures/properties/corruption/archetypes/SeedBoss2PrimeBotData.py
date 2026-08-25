# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SeedBoss2PrimeBotDataJson(typing_extensions.TypedDict):
        unknown_0x313d0133: float
        unknown_0xecb65675: float
        unknown_0x80a300a5: float
        unknown_0x8fe03c41: float
        unknown_0x4bc36eee: float
        shock_wave_info: json_util.JsonObject
        giant_electric_ball_damage: json_util.JsonObject
        ring_projectile_damage: json_util.JsonObject
        ring_vulnerability: json_util.JsonObject
        ring_health: float
        wheel_energy_beam_damage: json_util.JsonObject
        damage_info_0x3e1b90ff: json_util.JsonObject
        giant_contact_damage: json_util.JsonObject
        sphere_contact_damage: json_util.JsonObject
        damage_info_0x8461ab52: json_util.JsonObject
        damage_info_0x2872762b: json_util.JsonObject
        damage_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class SeedBoss2PrimeBotData(BaseProperty):
    unknown_0x313d0133: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x313D0133, original_name="Unknown"),
        },
    )
    unknown_0xecb65675: float = dataclasses.field(
        default=500.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xECB65675, original_name="Unknown"),
        },
    )
    unknown_0x80a300a5: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x80A300A5, original_name="Unknown"),
        },
    )
    unknown_0x8fe03c41: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8FE03C41, original_name="Unknown"),
        },
    )
    unknown_0x4bc36eee: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4BC36EEE, original_name="Unknown"),
        },
    )
    shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0xA40F65C2,
                original_name="ShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    giant_electric_ball_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x7651EC00,
                original_name="GiantElectricBallDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    ring_projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x18F91880,
                original_name="RingProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    ring_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x9562E522,
                original_name="RingVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    ring_health: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE0794DB1, original_name="RingHealth"),
        },
    )
    wheel_energy_beam_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x231D0FC4,
                original_name="WheelEnergyBeamDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x3e1b90ff: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x3E1B90FF,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    giant_contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xD0122838,
                original_name="GiantContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sphere_contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x1259AACD,
                original_name="SphereContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x8461ab52: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8461AB52,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x2872762b: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x2872762B,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0C6B7FA9,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
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
        if property_count != 17:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x313D0133
        unknown_0x313d0133 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xECB65675
        unknown_0xecb65675 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80A300A5
        unknown_0x80a300a5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8FE03C41
        unknown_0x8fe03c41 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4BC36EEE
        unknown_0x4bc36eee = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA40F65C2
        shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7651EC00
        giant_electric_ball_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18F91880
        ring_projectile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9562E522
        ring_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0794DB1
        ring_health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x231D0FC4
        wheel_energy_beam_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3E1B90FF
        damage_info_0x3e1b90ff = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD0122838
        giant_contact_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1259AACD
        sphere_contact_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8461AB52
        damage_info_0x8461ab52 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2872762B
        damage_info_0x2872762b = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C6B7FA9
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            unknown_0x313d0133,
            unknown_0xecb65675,
            unknown_0x80a300a5,
            unknown_0x8fe03c41,
            unknown_0x4bc36eee,
            shock_wave_info,
            giant_electric_ball_damage,
            ring_projectile_damage,
            ring_vulnerability,
            ring_health,
            wheel_energy_beam_damage,
            damage_info_0x3e1b90ff,
            giant_contact_damage,
            sphere_contact_damage,
            damage_info_0x8461ab52,
            damage_info_0x2872762b,
            damage_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x11")  # 17 properties

        data.write(b"1=\x013")  # 0x313d0133
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x313d0133))

        data.write(b"\xec\xb6Vu")  # 0xecb65675
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xecb65675))

        data.write(b"\x80\xa3\x00\xa5")  # 0x80a300a5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x80a300a5))

        data.write(b"\x8f\xe0<A")  # 0x8fe03c41
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8fe03c41))

        data.write(b"K\xc3n\xee")  # 0x4bc36eee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4bc36eee))

        data.write(b"\xa4\x0fe\xc2")  # 0xa40f65c2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"vQ\xec\x00")  # 0x7651ec00
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.giant_electric_ball_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x18\xf9\x18\x80")  # 0x18f91880
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ring_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x95b\xe5"')  # 0x9562e522
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ring_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe0yM\xb1")  # 0xe0794db1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ring_health))

        data.write(b"#\x1d\x0f\xc4")  # 0x231d0fc4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.wheel_energy_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b">\x1b\x90\xff")  # 0x3e1b90ff
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x3e1b90ff.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd0\x12(8")  # 0xd0122838
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.giant_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x12Y\xaa\xcd")  # 0x1259aacd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sphere_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x84a\xabR")  # 0x8461ab52
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x8461ab52.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"(rv+")  # 0x2872762b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x2872762b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0ck\x7f\xa9")  # 0xc6b7fa9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss2PrimeBotDataJson", data)
        return cls(
            unknown_0x313d0133=json_data["unknown_0x313d0133"],
            unknown_0xecb65675=json_data["unknown_0xecb65675"],
            unknown_0x80a300a5=json_data["unknown_0x80a300a5"],
            unknown_0x8fe03c41=json_data["unknown_0x8fe03c41"],
            unknown_0x4bc36eee=json_data["unknown_0x4bc36eee"],
            shock_wave_info=ShockWaveInfo.from_json(json_data["shock_wave_info"]),
            giant_electric_ball_damage=DamageInfo.from_json(json_data["giant_electric_ball_damage"]),
            ring_projectile_damage=DamageInfo.from_json(json_data["ring_projectile_damage"]),
            ring_vulnerability=DamageVulnerability.from_json(json_data["ring_vulnerability"]),
            ring_health=json_data["ring_health"],
            wheel_energy_beam_damage=DamageInfo.from_json(json_data["wheel_energy_beam_damage"]),
            damage_info_0x3e1b90ff=DamageInfo.from_json(json_data["damage_info_0x3e1b90ff"]),
            giant_contact_damage=DamageInfo.from_json(json_data["giant_contact_damage"]),
            sphere_contact_damage=DamageInfo.from_json(json_data["sphere_contact_damage"]),
            damage_info_0x8461ab52=DamageInfo.from_json(json_data["damage_info_0x8461ab52"]),
            damage_info_0x2872762b=DamageInfo.from_json(json_data["damage_info_0x2872762b"]),
            damage_vulnerability=DamageVulnerability.from_json(json_data["damage_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x313d0133": self.unknown_0x313d0133,
            "unknown_0xecb65675": self.unknown_0xecb65675,
            "unknown_0x80a300a5": self.unknown_0x80a300a5,
            "unknown_0x8fe03c41": self.unknown_0x8fe03c41,
            "unknown_0x4bc36eee": self.unknown_0x4bc36eee,
            "shock_wave_info": self.shock_wave_info.to_json(),
            "giant_electric_ball_damage": self.giant_electric_ball_damage.to_json(),
            "ring_projectile_damage": self.ring_projectile_damage.to_json(),
            "ring_vulnerability": self.ring_vulnerability.to_json(),
            "ring_health": self.ring_health,
            "wheel_energy_beam_damage": self.wheel_energy_beam_damage.to_json(),
            "damage_info_0x3e1b90ff": self.damage_info_0x3e1b90ff.to_json(),
            "giant_contact_damage": self.giant_contact_damage.to_json(),
            "sphere_contact_damage": self.sphere_contact_damage.to_json(),
            "damage_info_0x8461ab52": self.damage_info_0x8461ab52.to_json(),
            "damage_info_0x2872762b": self.damage_info_0x2872762b.to_json(),
            "damage_vulnerability": self.damage_vulnerability.to_json(),
        }


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_giant_electric_ball_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ring_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ring_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_wheel_energy_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x3e1b90ff(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_giant_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_sphere_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x8461ab52(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x2872762b(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x313D0133: ("unknown_0x313d0133", structs.decode_BIG_f),
    0xECB65675: ("unknown_0xecb65675", structs.decode_BIG_f),
    0x80A300A5: ("unknown_0x80a300a5", structs.decode_BIG_f),
    0x8FE03C41: ("unknown_0x8fe03c41", structs.decode_BIG_f),
    0x4BC36EEE: ("unknown_0x4bc36eee", structs.decode_BIG_f),
    0xA40F65C2: ("shock_wave_info", _decode_shock_wave_info),
    0x7651EC00: ("giant_electric_ball_damage", _decode_giant_electric_ball_damage),
    0x18F91880: ("ring_projectile_damage", _decode_ring_projectile_damage),
    0x9562E522: ("ring_vulnerability", _decode_ring_vulnerability),
    0xE0794DB1: ("ring_health", structs.decode_BIG_f),
    0x231D0FC4: ("wheel_energy_beam_damage", _decode_wheel_energy_beam_damage),
    0x3E1B90FF: ("damage_info_0x3e1b90ff", _decode_damage_info_0x3e1b90ff),
    0xD0122838: ("giant_contact_damage", _decode_giant_contact_damage),
    0x1259AACD: ("sphere_contact_damage", _decode_sphere_contact_damage),
    0x8461AB52: ("damage_info_0x8461ab52", _decode_damage_info_0x8461ab52),
    0x2872762B: ("damage_info_0x2872762b", _decode_damage_info_0x2872762b),
    0x0C6B7FA9: ("damage_vulnerability", _decode_damage_vulnerability),
}
