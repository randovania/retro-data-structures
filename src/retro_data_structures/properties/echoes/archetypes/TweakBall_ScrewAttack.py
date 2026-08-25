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

    class TweakBall_ScrewAttackJson(typing_extensions.TypedDict):
        screw_attack_gravity: float
        unknown_0xcb77fb28: float
        unknown_0x3fdeb046: float
        unknown_0x691b244d: int
        screw_attack_vertical_jump_velocity: float
        screw_attack_horizontal_jump_velocity: float
        unknown_0x3d03d8a6: float
        unknown_0xf1f2498f: float
        unknown_0x4b0aba1c: float
        screw_attack_wall_jump_max_time: float
        screw_attack_wall_jump_vertical_velocity: float
        screw_attack_wall_jump_horizontal_velocity: float
        screw_attack_wall_jump_gravity: float
        screw_attack_damage: json_util.JsonObject


@dataclasses.dataclass()
class TweakBall_ScrewAttack(BaseProperty):
    screw_attack_gravity: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7EAB4BAB, original_name="ScrewAttackGravity"),
        },
    )
    unknown_0xcb77fb28: float = dataclasses.field(
        default=4.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCB77FB28, original_name="Unknown"),
        },
    )
    unknown_0x3fdeb046: float = dataclasses.field(
        default=4.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3FDEB046, original_name="Unknown"),
        },
    )
    unknown_0x691b244d: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x691B244D, original_name="Unknown"),
        },
    )
    screw_attack_vertical_jump_velocity: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x591DA5B4, original_name="ScrewAttackVerticalJumpVelocity"),
        },
    )
    screw_attack_horizontal_jump_velocity: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0xE428F231, original_name="ScrewAttackHorizontalJumpVelocity"
            ),
        },
    )
    unknown_0x3d03d8a6: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3D03D8A6, original_name="Unknown"),
        },
    )
    unknown_0xf1f2498f: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF1F2498F, original_name="Unknown"),
        },
    )
    unknown_0x4b0aba1c: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B0ABA1C, original_name="Unknown"),
        },
    )
    screw_attack_wall_jump_max_time: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14351140, original_name="ScrewAttackWallJumpMaxTime"),
        },
    )
    screw_attack_wall_jump_vertical_velocity: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0x5DEC33C5, original_name="ScrewAttackWallJumpVerticalVelocity"
            ),
        },
    )
    screw_attack_wall_jump_horizontal_velocity: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0xB8431384, original_name="ScrewAttackWallJumpHorizontalVelocity"
            ),
        },
    )
    screw_attack_wall_jump_gravity: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x38F84011, original_name="ScrewAttackWallJumpGravity"),
        },
    )
    screw_attack_damage: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0xB372ECAB,
                original_name="ScrewAttackDamage",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
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
        assert property_id == 0x7EAB4BAB
        screw_attack_gravity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB77FB28
        unknown_0xcb77fb28 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FDEB046
        unknown_0x3fdeb046 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x691B244D
        unknown_0x691b244d = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x591DA5B4
        screw_attack_vertical_jump_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE428F231
        screw_attack_horizontal_jump_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D03D8A6
        unknown_0x3d03d8a6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1F2498F
        unknown_0xf1f2498f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B0ABA1C
        unknown_0x4b0aba1c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14351140
        screw_attack_wall_jump_max_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5DEC33C5
        screw_attack_wall_jump_vertical_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB8431384
        screw_attack_wall_jump_horizontal_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38F84011
        screw_attack_wall_jump_gravity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB372ECAB
        screw_attack_damage = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 7,
                "damage_amount": 50.0,
                "radius_damage_amount": 50.0,
                "damage_radius": 2.0,
            },
        )

        return cls(
            screw_attack_gravity,
            unknown_0xcb77fb28,
            unknown_0x3fdeb046,
            unknown_0x691b244d,
            screw_attack_vertical_jump_velocity,
            screw_attack_horizontal_jump_velocity,
            unknown_0x3d03d8a6,
            unknown_0xf1f2498f,
            unknown_0x4b0aba1c,
            screw_attack_wall_jump_max_time,
            screw_attack_wall_jump_vertical_velocity,
            screw_attack_wall_jump_horizontal_velocity,
            screw_attack_wall_jump_gravity,
            screw_attack_damage,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"~\xabK\xab")  # 0x7eab4bab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screw_attack_gravity))

        data.write(b"\xcbw\xfb(")  # 0xcb77fb28
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcb77fb28))

        data.write(b"?\xde\xb0F")  # 0x3fdeb046
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3fdeb046))

        data.write(b"i\x1b$M")  # 0x691b244d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x691b244d))

        data.write(b"Y\x1d\xa5\xb4")  # 0x591da5b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screw_attack_vertical_jump_velocity))

        data.write(b"\xe4(\xf21")  # 0xe428f231
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screw_attack_horizontal_jump_velocity))

        data.write(b"=\x03\xd8\xa6")  # 0x3d03d8a6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3d03d8a6))

        data.write(b"\xf1\xf2I\x8f")  # 0xf1f2498f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf1f2498f))

        data.write(b"K\n\xba\x1c")  # 0x4b0aba1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4b0aba1c))

        data.write(b"\x145\x11@")  # 0x14351140
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screw_attack_wall_jump_max_time))

        data.write(b"]\xec3\xc5")  # 0x5dec33c5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screw_attack_wall_jump_vertical_velocity))

        data.write(b"\xb8C\x13\x84")  # 0xb8431384
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screw_attack_wall_jump_horizontal_velocity))

        data.write(b"8\xf8@\x11")  # 0x38f84011
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screw_attack_wall_jump_gravity))

        data.write(b"\xb3r\xec\xab")  # 0xb372ecab
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.screw_attack_damage.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 7,
                "damage_amount": 50.0,
                "radius_damage_amount": 50.0,
                "damage_radius": 2.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakBall_ScrewAttackJson", data)
        return cls(
            screw_attack_gravity=json_data["screw_attack_gravity"],
            unknown_0xcb77fb28=json_data["unknown_0xcb77fb28"],
            unknown_0x3fdeb046=json_data["unknown_0x3fdeb046"],
            unknown_0x691b244d=json_data["unknown_0x691b244d"],
            screw_attack_vertical_jump_velocity=json_data["screw_attack_vertical_jump_velocity"],
            screw_attack_horizontal_jump_velocity=json_data["screw_attack_horizontal_jump_velocity"],
            unknown_0x3d03d8a6=json_data["unknown_0x3d03d8a6"],
            unknown_0xf1f2498f=json_data["unknown_0xf1f2498f"],
            unknown_0x4b0aba1c=json_data["unknown_0x4b0aba1c"],
            screw_attack_wall_jump_max_time=json_data["screw_attack_wall_jump_max_time"],
            screw_attack_wall_jump_vertical_velocity=json_data["screw_attack_wall_jump_vertical_velocity"],
            screw_attack_wall_jump_horizontal_velocity=json_data["screw_attack_wall_jump_horizontal_velocity"],
            screw_attack_wall_jump_gravity=json_data["screw_attack_wall_jump_gravity"],
            screw_attack_damage=TDamageInfo.from_json(json_data["screw_attack_damage"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "screw_attack_gravity": self.screw_attack_gravity,
            "unknown_0xcb77fb28": self.unknown_0xcb77fb28,
            "unknown_0x3fdeb046": self.unknown_0x3fdeb046,
            "unknown_0x691b244d": self.unknown_0x691b244d,
            "screw_attack_vertical_jump_velocity": self.screw_attack_vertical_jump_velocity,
            "screw_attack_horizontal_jump_velocity": self.screw_attack_horizontal_jump_velocity,
            "unknown_0x3d03d8a6": self.unknown_0x3d03d8a6,
            "unknown_0xf1f2498f": self.unknown_0xf1f2498f,
            "unknown_0x4b0aba1c": self.unknown_0x4b0aba1c,
            "screw_attack_wall_jump_max_time": self.screw_attack_wall_jump_max_time,
            "screw_attack_wall_jump_vertical_velocity": self.screw_attack_wall_jump_vertical_velocity,
            "screw_attack_wall_jump_horizontal_velocity": self.screw_attack_wall_jump_horizontal_velocity,
            "screw_attack_wall_jump_gravity": self.screw_attack_wall_jump_gravity,
            "screw_attack_damage": self.screw_attack_damage.to_json(),
        }


def _decode_screw_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"weapon_type": 7, "damage_amount": 50.0, "radius_damage_amount": 50.0, "damage_radius": 2.0},
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7EAB4BAB: ("screw_attack_gravity", structs.decode_BIG_f),
    0xCB77FB28: ("unknown_0xcb77fb28", structs.decode_BIG_f),
    0x3FDEB046: ("unknown_0x3fdeb046", structs.decode_BIG_f),
    0x691B244D: ("unknown_0x691b244d", structs.decode_BIG_l),
    0x591DA5B4: ("screw_attack_vertical_jump_velocity", structs.decode_BIG_f),
    0xE428F231: ("screw_attack_horizontal_jump_velocity", structs.decode_BIG_f),
    0x3D03D8A6: ("unknown_0x3d03d8a6", structs.decode_BIG_f),
    0xF1F2498F: ("unknown_0xf1f2498f", structs.decode_BIG_f),
    0x4B0ABA1C: ("unknown_0x4b0aba1c", structs.decode_BIG_f),
    0x14351140: ("screw_attack_wall_jump_max_time", structs.decode_BIG_f),
    0x5DEC33C5: ("screw_attack_wall_jump_vertical_velocity", structs.decode_BIG_f),
    0xB8431384: ("screw_attack_wall_jump_horizontal_velocity", structs.decode_BIG_f),
    0x38F84011: ("screw_attack_wall_jump_gravity", structs.decode_BIG_f),
    0xB372ECAB: ("screw_attack_damage", _decode_screw_attack_damage),
}
