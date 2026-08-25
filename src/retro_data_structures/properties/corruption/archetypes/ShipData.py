# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo, DI_WeaponType
from retro_data_structures.properties.corruption.archetypes.Vector2f import Vector2f
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ShipDataJson(typing_extensions.TypedDict):
        samus_ship: bool
        shot_projectile: int
        shot_damage: json_util.JsonObject
        sound_shot: int
        unknown_0xd5039d33: float
        speed: float
        unknown_0x04c4e40b: bool
        vector2f: json_util.JsonObject
        thruster_effect: int
        part_0x7ebd51de: int
        swhc_0x25bd3372: int
        swhc_0xa32941dc: int
        part_0x2f335270: int
        grapple_claw_effect: int
        sound_thrust: int
        unknown_0x497c0d5e: bool
        unknown_0xb6eacc28: float
        command_visor_animation: json_util.JsonObject


@dataclasses.dataclass()
class ShipData(BaseProperty):
    samus_ship: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x742E0922, original_name="SamusShip"),
        },
    )
    shot_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x51253BA3, original_name="ShotProjectile"),
        },
    )
    shot_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xCEA30138,
                original_name="ShotDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_shot: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC23A1955, original_name="Sound_Shot"),
        },
    )
    unknown_0xd5039d33: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5039D33, original_name="Unknown"),
        },
    )
    speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6392404E, original_name="Speed"),
        },
    )
    unknown_0x04c4e40b: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x04C4E40B, original_name="Unknown"),
        },
    )
    vector2f: Vector2f = dataclasses.field(
        default_factory=Vector2f,
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0x4ABADE16,
                original_name="Vector2f",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
            ),
        },
    )
    thruster_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6A43639F, original_name="ThrusterEffect"),
        },
    )
    part_0x7ebd51de: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7EBD51DE, original_name="PART"),
        },
    )
    swhc_0x25bd3372: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SWHC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x25BD3372, original_name="SWHC"),
        },
    )
    swhc_0xa32941dc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SWHC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA32941DC, original_name="SWHC"),
        },
    )
    part_0x2f335270: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2F335270, original_name="PART"),
        },
    )
    grapple_claw_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB685FEEE, original_name="GrappleClawEffect"),
        },
    )
    sound_thrust: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD3023E6C, original_name="Sound_Thrust"),
        },
    )
    unknown_0x497c0d5e: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x497C0D5E, original_name="Unknown"),
        },
    )
    unknown_0xb6eacc28: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB6EACC28, original_name="Unknown"),
        },
    )
    command_visor_animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x7D38C0BE,
                original_name="CommandVisorAnimation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
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
        if property_count != 18:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x742E0922
        samus_ship = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51253BA3
        shot_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCEA30138
        shot_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "di_weapon_type": DI_WeaponType.Friendly,
                "di_damage": 50.0,
                "di_radius": 20.0,
                "di_knock_back_power": 5.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC23A1955
        sound_shot = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5039D33
        unknown_0xd5039d33 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404E
        speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04C4E40B
        unknown_0x04c4e40b = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ABADE16
        vector2f = Vector2f.from_stream(data, game, property_size, default_override={"x": 90.0, "y": 90.0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A43639F
        thruster_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7EBD51DE
        part_0x7ebd51de = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25BD3372
        swhc_0x25bd3372 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA32941DC
        swhc_0xa32941dc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F335270
        part_0x2f335270 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB685FEEE
        grapple_claw_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3023E6C
        sound_thrust = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x497C0D5E
        unknown_0x497c0d5e = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6EACC28
        unknown_0xb6eacc28 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D38C0BE
        command_visor_animation = AnimationParameters.from_stream(data, game, property_size)

        return cls(
            samus_ship,
            shot_projectile,
            shot_damage,
            sound_shot,
            unknown_0xd5039d33,
            speed,
            unknown_0x04c4e40b,
            vector2f,
            thruster_effect,
            part_0x7ebd51de,
            swhc_0x25bd3372,
            swhc_0xa32941dc,
            part_0x2f335270,
            grapple_claw_effect,
            sound_thrust,
            unknown_0x497c0d5e,
            unknown_0xb6eacc28,
            command_visor_animation,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x12")  # 18 properties

        data.write(b't.\t"')  # 0x742e0922
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.samus_ship))

        data.write(b"Q%;\xa3")  # 0x51253ba3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.shot_projectile))

        data.write(b"\xce\xa3\x018")  # 0xcea30138
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shot_damage.to_stream(
            data,
            game,
            default_override={
                "di_weapon_type": DI_WeaponType.Friendly,
                "di_damage": 50.0,
                "di_radius": 20.0,
                "di_knock_back_power": 5.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc2:\x19U")  # 0xc23a1955
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_shot))

        data.write(b"\xd5\x03\x9d3")  # 0xd5039d33
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd5039d33))

        data.write(b"c\x92@N")  # 0x6392404e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b"\x04\xc4\xe4\x0b")  # 0x4c4e40b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x04c4e40b))

        data.write(b"J\xba\xde\x16")  # 0x4abade16
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vector2f.to_stream(data, game, default_override={"x": 90.0, "y": 90.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"jCc\x9f")  # 0x6a43639f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.thruster_effect))

        data.write(b"~\xbdQ\xde")  # 0x7ebd51de
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x7ebd51de))

        data.write(b"%\xbd3r")  # 0x25bd3372
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.swhc_0x25bd3372))

        data.write(b"\xa3)A\xdc")  # 0xa32941dc
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.swhc_0xa32941dc))

        data.write(b"/3Rp")  # 0x2f335270
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x2f335270))

        data.write(b"\xb6\x85\xfe\xee")  # 0xb685feee
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.grapple_claw_effect))

        data.write(b"\xd3\x02>l")  # 0xd3023e6c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_thrust))

        data.write(b"I|\r^")  # 0x497c0d5e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x497c0d5e))

        data.write(b"\xb6\xea\xcc(")  # 0xb6eacc28
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb6eacc28))

        data.write(b"}8\xc0\xbe")  # 0x7d38c0be
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.command_visor_animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShipDataJson", data)
        return cls(
            samus_ship=json_data["samus_ship"],
            shot_projectile=json_data["shot_projectile"],
            shot_damage=DamageInfo.from_json(json_data["shot_damage"]),
            sound_shot=json_data["sound_shot"],
            unknown_0xd5039d33=json_data["unknown_0xd5039d33"],
            speed=json_data["speed"],
            unknown_0x04c4e40b=json_data["unknown_0x04c4e40b"],
            vector2f=Vector2f.from_json(json_data["vector2f"]),
            thruster_effect=json_data["thruster_effect"],
            part_0x7ebd51de=json_data["part_0x7ebd51de"],
            swhc_0x25bd3372=json_data["swhc_0x25bd3372"],
            swhc_0xa32941dc=json_data["swhc_0xa32941dc"],
            part_0x2f335270=json_data["part_0x2f335270"],
            grapple_claw_effect=json_data["grapple_claw_effect"],
            sound_thrust=json_data["sound_thrust"],
            unknown_0x497c0d5e=json_data["unknown_0x497c0d5e"],
            unknown_0xb6eacc28=json_data["unknown_0xb6eacc28"],
            command_visor_animation=AnimationParameters.from_json(json_data["command_visor_animation"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "samus_ship": self.samus_ship,
            "shot_projectile": self.shot_projectile,
            "shot_damage": self.shot_damage.to_json(),
            "sound_shot": self.sound_shot,
            "unknown_0xd5039d33": self.unknown_0xd5039d33,
            "speed": self.speed,
            "unknown_0x04c4e40b": self.unknown_0x04c4e40b,
            "vector2f": self.vector2f.to_json(),
            "thruster_effect": self.thruster_effect,
            "part_0x7ebd51de": self.part_0x7ebd51de,
            "swhc_0x25bd3372": self.swhc_0x25bd3372,
            "swhc_0xa32941dc": self.swhc_0xa32941dc,
            "part_0x2f335270": self.part_0x2f335270,
            "grapple_claw_effect": self.grapple_claw_effect,
            "sound_thrust": self.sound_thrust,
            "unknown_0x497c0d5e": self.unknown_0x497c0d5e,
            "unknown_0xb6eacc28": self.unknown_0xb6eacc28,
            "command_visor_animation": self.command_visor_animation.to_json(),
        }


def _decode_shot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "di_weapon_type": DI_WeaponType.Friendly,
            "di_damage": 50.0,
            "di_radius": 20.0,
            "di_knock_back_power": 5.0,
        },
    )


def _decode_vector2f(data: typing.BinaryIO, game: Game, property_size: int) -> Vector2f:
    return Vector2f.from_stream(data, game, property_size, default_override={"x": 90.0, "y": 90.0})


def _decode_command_visor_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x742E0922: ("samus_ship", structs.decode_BIG_bool_),
    0x51253BA3: ("shot_projectile", structs.decode_BIG_Q),
    0xCEA30138: ("shot_damage", _decode_shot_damage),
    0xC23A1955: ("sound_shot", structs.decode_BIG_Q),
    0xD5039D33: ("unknown_0xd5039d33", structs.decode_BIG_f),
    0x6392404E: ("speed", structs.decode_BIG_f),
    0x04C4E40B: ("unknown_0x04c4e40b", structs.decode_BIG_bool_),
    0x4ABADE16: ("vector2f", _decode_vector2f),
    0x6A43639F: ("thruster_effect", structs.decode_BIG_Q),
    0x7EBD51DE: ("part_0x7ebd51de", structs.decode_BIG_Q),
    0x25BD3372: ("swhc_0x25bd3372", structs.decode_BIG_Q),
    0xA32941DC: ("swhc_0xa32941dc", structs.decode_BIG_Q),
    0x2F335270: ("part_0x2f335270", structs.decode_BIG_Q),
    0xB685FEEE: ("grapple_claw_effect", structs.decode_BIG_Q),
    0xD3023E6C: ("sound_thrust", structs.decode_BIG_Q),
    0x497C0D5E: ("unknown_0x497c0d5e", structs.decode_BIG_bool_),
    0xB6EACC28: ("unknown_0xb6eacc28", structs.decode_BIG_f),
    0x7D38C0BE: ("command_visor_animation", _decode_command_visor_animation),
}
