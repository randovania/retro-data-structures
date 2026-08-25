# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayerControls_UnknownStruct2Json(typing_extensions.TypedDict):
        unknown_0xff1b0413: bool
        unknown_0xe0c1d958: bool
        toggle_aim_position: bool
        unknown_0x1f99c6ba: bool
        unknown_0x18eb3ab5: bool
        unknown_0xbdc01c71: bool
        fixed_vertical_aim: bool
        unknown_0xda97bbcd: bool
        orbit_around_enemies: bool
        unknown_0xc224d966: bool
        add_grenade_alert: bool
        unknown_0x3fb16819: bool
        unknown_0x4fcf4b70: bool
        unknown_0x07bb06a6: bool
        unknown_0x04d8d57b: bool
        unknown_0x5282c47e: bool
        falling_double_jump: bool
        impulse_double_jump: bool
        unknown_0xa796a8b9: bool
        unknown_0x7c0599c8: bool
        unknown_0x522ab1ac: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xFF1B0413,
    0xE0C1D958,
    0x55C20D58,
    0x1F99C6BA,
    0x18EB3AB5,
    0xBDC01C71,
    0x1C30F1A6,
    0xDA97BBCD,
    0x83583ABD,
    0xC224D966,
    0x1FCFAF3F,
    0x3FB16819,
    0x4FCF4B70,
    0x7BB06A6,
    0x4D8D57B,
    0x5282C47E,
    0x7304DAFA,
    0x7A49267D,
    0xA796A8B9,
    0x7C0599C8,
    0x522AB1AC,
)


@dataclasses.dataclass()
class TweakPlayerControls_UnknownStruct2(BaseProperty):
    unknown_0xff1b0413: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFF1B0413, original_name="Unknown"),
        },
    )
    unknown_0xe0c1d958: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE0C1D958, original_name="Unknown"),
        },
    )
    toggle_aim_position: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x55C20D58, original_name="ToggleAimPosition"),
        },
    )
    unknown_0x1f99c6ba: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1F99C6BA, original_name="Unknown"),
        },
    )
    unknown_0x18eb3ab5: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x18EB3AB5, original_name="Unknown"),
        },
    )
    unknown_0xbdc01c71: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBDC01C71, original_name="Unknown"),
        },
    )
    fixed_vertical_aim: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1C30F1A6, original_name="FixedVerticalAim"),
        },
    )
    unknown_0xda97bbcd: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xDA97BBCD, original_name="Unknown"),
        },
    )
    orbit_around_enemies: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x83583ABD, original_name="OrbitAroundEnemies?"),
        },
    )
    unknown_0xc224d966: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC224D966, original_name="Unknown"),
        },
    )
    add_grenade_alert: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1FCFAF3F, original_name="AddGrenadeAlert?"),
        },
    )
    unknown_0x3fb16819: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3FB16819, original_name="Unknown"),
        },
    )
    unknown_0x4fcf4b70: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4FCF4B70, original_name="Unknown"),
        },
    )
    unknown_0x07bb06a6: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x07BB06A6, original_name="Unknown"),
        },
    )
    unknown_0x04d8d57b: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x04D8D57B, original_name="Unknown"),
        },
    )
    unknown_0x5282c47e: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5282C47E, original_name="Unknown"),
        },
    )
    falling_double_jump: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7304DAFA, original_name="FallingDoubleJump"),
        },
    )
    impulse_double_jump: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7A49267D, original_name="ImpulseDoubleJump"),
        },
    )
    unknown_0xa796a8b9: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA796A8B9, original_name="Unknown"),
        },
    )
    unknown_0x7c0599c8: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7C0599C8, original_name="Unknown"),
        },
    )
    unknown_0x522ab1ac: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x522AB1AC, original_name="Unknown"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?")

        dec = _FAST_FORMAT.unpack(data.read(147))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
            dec[48],
            dec[51],
            dec[54],
            dec[57],
            dec[60],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            dec[59],
            dec[62],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"\xff\x1b\x04\x13")  # 0xff1b0413
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xff1b0413))

        data.write(b"\xe0\xc1\xd9X")  # 0xe0c1d958
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xe0c1d958))

        data.write(b"U\xc2\rX")  # 0x55c20d58
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.toggle_aim_position))

        data.write(b"\x1f\x99\xc6\xba")  # 0x1f99c6ba
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x1f99c6ba))

        data.write(b"\x18\xeb:\xb5")  # 0x18eb3ab5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x18eb3ab5))

        data.write(b"\xbd\xc0\x1cq")  # 0xbdc01c71
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbdc01c71))

        data.write(b"\x1c0\xf1\xa6")  # 0x1c30f1a6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.fixed_vertical_aim))

        data.write(b"\xda\x97\xbb\xcd")  # 0xda97bbcd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xda97bbcd))

        data.write(b"\x83X:\xbd")  # 0x83583abd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.orbit_around_enemies))

        data.write(b"\xc2$\xd9f")  # 0xc224d966
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xc224d966))

        data.write(b"\x1f\xcf\xaf?")  # 0x1fcfaf3f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.add_grenade_alert))

        data.write(b"?\xb1h\x19")  # 0x3fb16819
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x3fb16819))

        data.write(b"O\xcfKp")  # 0x4fcf4b70
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4fcf4b70))

        data.write(b"\x07\xbb\x06\xa6")  # 0x7bb06a6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x07bb06a6))

        data.write(b"\x04\xd8\xd5{")  # 0x4d8d57b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x04d8d57b))

        data.write(b"R\x82\xc4~")  # 0x5282c47e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x5282c47e))

        data.write(b"s\x04\xda\xfa")  # 0x7304dafa
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.falling_double_jump))

        data.write(b"zI&}")  # 0x7a49267d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.impulse_double_jump))

        data.write(b"\xa7\x96\xa8\xb9")  # 0xa796a8b9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa796a8b9))

        data.write(b"|\x05\x99\xc8")  # 0x7c0599c8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7c0599c8))

        data.write(b"R*\xb1\xac")  # 0x522ab1ac
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x522ab1ac))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerControls_UnknownStruct2Json", data)
        return cls(
            unknown_0xff1b0413=json_data["unknown_0xff1b0413"],
            unknown_0xe0c1d958=json_data["unknown_0xe0c1d958"],
            toggle_aim_position=json_data["toggle_aim_position"],
            unknown_0x1f99c6ba=json_data["unknown_0x1f99c6ba"],
            unknown_0x18eb3ab5=json_data["unknown_0x18eb3ab5"],
            unknown_0xbdc01c71=json_data["unknown_0xbdc01c71"],
            fixed_vertical_aim=json_data["fixed_vertical_aim"],
            unknown_0xda97bbcd=json_data["unknown_0xda97bbcd"],
            orbit_around_enemies=json_data["orbit_around_enemies"],
            unknown_0xc224d966=json_data["unknown_0xc224d966"],
            add_grenade_alert=json_data["add_grenade_alert"],
            unknown_0x3fb16819=json_data["unknown_0x3fb16819"],
            unknown_0x4fcf4b70=json_data["unknown_0x4fcf4b70"],
            unknown_0x07bb06a6=json_data["unknown_0x07bb06a6"],
            unknown_0x04d8d57b=json_data["unknown_0x04d8d57b"],
            unknown_0x5282c47e=json_data["unknown_0x5282c47e"],
            falling_double_jump=json_data["falling_double_jump"],
            impulse_double_jump=json_data["impulse_double_jump"],
            unknown_0xa796a8b9=json_data["unknown_0xa796a8b9"],
            unknown_0x7c0599c8=json_data["unknown_0x7c0599c8"],
            unknown_0x522ab1ac=json_data["unknown_0x522ab1ac"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xff1b0413": self.unknown_0xff1b0413,
            "unknown_0xe0c1d958": self.unknown_0xe0c1d958,
            "toggle_aim_position": self.toggle_aim_position,
            "unknown_0x1f99c6ba": self.unknown_0x1f99c6ba,
            "unknown_0x18eb3ab5": self.unknown_0x18eb3ab5,
            "unknown_0xbdc01c71": self.unknown_0xbdc01c71,
            "fixed_vertical_aim": self.fixed_vertical_aim,
            "unknown_0xda97bbcd": self.unknown_0xda97bbcd,
            "orbit_around_enemies": self.orbit_around_enemies,
            "unknown_0xc224d966": self.unknown_0xc224d966,
            "add_grenade_alert": self.add_grenade_alert,
            "unknown_0x3fb16819": self.unknown_0x3fb16819,
            "unknown_0x4fcf4b70": self.unknown_0x4fcf4b70,
            "unknown_0x07bb06a6": self.unknown_0x07bb06a6,
            "unknown_0x04d8d57b": self.unknown_0x04d8d57b,
            "unknown_0x5282c47e": self.unknown_0x5282c47e,
            "falling_double_jump": self.falling_double_jump,
            "impulse_double_jump": self.impulse_double_jump,
            "unknown_0xa796a8b9": self.unknown_0xa796a8b9,
            "unknown_0x7c0599c8": self.unknown_0x7c0599c8,
            "unknown_0x522ab1ac": self.unknown_0x522ab1ac,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFF1B0413: ("unknown_0xff1b0413", structs.decode_BIG_bool_),
    0xE0C1D958: ("unknown_0xe0c1d958", structs.decode_BIG_bool_),
    0x55C20D58: ("toggle_aim_position", structs.decode_BIG_bool_),
    0x1F99C6BA: ("unknown_0x1f99c6ba", structs.decode_BIG_bool_),
    0x18EB3AB5: ("unknown_0x18eb3ab5", structs.decode_BIG_bool_),
    0xBDC01C71: ("unknown_0xbdc01c71", structs.decode_BIG_bool_),
    0x1C30F1A6: ("fixed_vertical_aim", structs.decode_BIG_bool_),
    0xDA97BBCD: ("unknown_0xda97bbcd", structs.decode_BIG_bool_),
    0x83583ABD: ("orbit_around_enemies", structs.decode_BIG_bool_),
    0xC224D966: ("unknown_0xc224d966", structs.decode_BIG_bool_),
    0x1FCFAF3F: ("add_grenade_alert", structs.decode_BIG_bool_),
    0x3FB16819: ("unknown_0x3fb16819", structs.decode_BIG_bool_),
    0x4FCF4B70: ("unknown_0x4fcf4b70", structs.decode_BIG_bool_),
    0x07BB06A6: ("unknown_0x07bb06a6", structs.decode_BIG_bool_),
    0x04D8D57B: ("unknown_0x04d8d57b", structs.decode_BIG_bool_),
    0x5282C47E: ("unknown_0x5282c47e", structs.decode_BIG_bool_),
    0x7304DAFA: ("falling_double_jump", structs.decode_BIG_bool_),
    0x7A49267D: ("impulse_double_jump", structs.decode_BIG_bool_),
    0xA796A8B9: ("unknown_0xa796a8b9", structs.decode_BIG_bool_),
    0x7C0599C8: ("unknown_0x7c0599c8", structs.decode_BIG_bool_),
    0x522AB1AC: ("unknown_0x522ab1ac", structs.decode_BIG_bool_),
}
