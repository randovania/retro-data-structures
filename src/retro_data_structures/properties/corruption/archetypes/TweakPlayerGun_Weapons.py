# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.common.archetypes.TBeamInfo import TBeamInfo
from retro_data_structures.properties.common.archetypes.TDamageInfo import TDamageInfo
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayerGun_WeaponsJson(typing_extensions.TypedDict):
        bomb: json_util.JsonObject
        unknown_0xe8907530: float
        unknown_0x0a9186cb: float
        unknown_0x519c83e7: float
        unknown_0xea7f3336: float
        unknown_0xba3ef7ea: float
        unknown_0xebdf0b9b: json_util.JsonObject
        unknown_0xf9125d7e: json_util.JsonObject
        missile: json_util.JsonObject
        unknown_0xe58d6c84: json_util.JsonObject
        unknown_0xd26376fd: json_util.JsonObject
        missile_reload_time: float
        power_beam: json_util.JsonObject
        unknown_0x86a941fc: json_util.JsonObject
        unknown_0x25906c03: json_util.JsonObject
        phazon_beam: json_util.JsonObject


@dataclasses.dataclass()
class TweakPlayerGun_Weapons(BaseProperty):
    bomb: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0x6173AD96,
                original_name="Bomb",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    unknown_0xe8907530: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8907530, original_name="Unknown"),
        },
    )
    unknown_0x0a9186cb: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0A9186CB, original_name="Unknown"),
        },
    )
    unknown_0x519c83e7: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x519C83E7, original_name="Unknown"),
        },
    )
    unknown_0xea7f3336: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEA7F3336, original_name="Unknown"),
        },
    )
    unknown_0xba3ef7ea: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA3EF7EA, original_name="Unknown"),
        },
    )
    unknown_0xebdf0b9b: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xEBDF0B9B, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xf9125d7e: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xF9125D7E, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    missile: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0x58F00B0A,
                original_name="Missile",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    unknown_0xe58d6c84: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0xE58D6C84,
                original_name="Unknown",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    unknown_0xd26376fd: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0xD26376FD,
                original_name="Unknown",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    missile_reload_time: float = dataclasses.field(
        default=1.2999999523162842,
        metadata={
            "reflection": FieldReflection[float](float, id=0x43F0A8A0, original_name="MissileReloadTime"),
        },
    )
    power_beam: TBeamInfo = dataclasses.field(
        default_factory=TBeamInfo,
        metadata={
            "reflection": FieldReflection[TBeamInfo](
                TBeamInfo,
                id=0x1F6C1A6B,
                original_name="Power_Beam",
                from_json=TBeamInfo.from_json,
                to_json=TBeamInfo.to_json,
            ),
        },
    )
    unknown_0x86a941fc: TBeamInfo = dataclasses.field(
        default_factory=TBeamInfo,
        metadata={
            "reflection": FieldReflection[TBeamInfo](
                TBeamInfo,
                id=0x86A941FC,
                original_name="Unknown",
                from_json=TBeamInfo.from_json,
                to_json=TBeamInfo.to_json,
            ),
        },
    )
    unknown_0x25906c03: TBeamInfo = dataclasses.field(
        default_factory=TBeamInfo,
        metadata={
            "reflection": FieldReflection[TBeamInfo](
                TBeamInfo,
                id=0x25906C03,
                original_name="Unknown",
                from_json=TBeamInfo.from_json,
                to_json=TBeamInfo.to_json,
            ),
        },
    )
    phazon_beam: TBeamInfo = dataclasses.field(
        default_factory=TBeamInfo,
        metadata={
            "reflection": FieldReflection[TBeamInfo](
                TBeamInfo,
                id=0xDD5F2E3D,
                original_name="Phazon_Beam",
                from_json=TBeamInfo.from_json,
                to_json=TBeamInfo.to_json,
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
        if property_count != 16:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6173AD96
        bomb = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"weapon_type": 7, "radius_damage_amount": 10.0, "damage_radius": 3.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8907530
        unknown_0xe8907530 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A9186CB
        unknown_0x0a9186cb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x519C83E7
        unknown_0x519c83e7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA7F3336
        unknown_0xea7f3336 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA3EF7EA
        unknown_0xba3ef7ea = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBDF0B9B
        unknown_0xebdf0b9b = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9125D7E
        unknown_0xf9125d7e = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58F00B0A
        missile = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 4,
                "damage_amount": 30.0,
                "radius_damage_amount": 15.0,
                "damage_radius": 4.5,
                "knock_back_power": 4.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE58D6C84
        unknown_0xe58d6c84 = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 5,
                "damage_amount": 30.0,
                "radius_damage_amount": 15.0,
                "damage_radius": 4.5,
                "knock_back_power": 4.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD26376FD
        unknown_0xd26376fd = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 5,
                "damage_amount": 30.0,
                "radius_damage_amount": 15.0,
                "damage_radius": 4.5,
                "knock_back_power": 4.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43F0A8A0
        missile_reload_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F6C1A6B
        power_beam = TBeamInfo.from_stream(
            data, game, property_size, default_override={"cooldown": 0.11100000143051147}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86A941FC
        unknown_0x86a941fc = TBeamInfo.from_stream(data, game, property_size, default_override={"cooldown": 0.5})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25906C03
        unknown_0x25906c03 = TBeamInfo.from_stream(
            data, game, property_size, default_override={"cooldown": 0.33000001311302185}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD5F2E3D
        phazon_beam = TBeamInfo.from_stream(
            data, game, property_size, default_override={"cooldown": 0.10000000149011612}
        )

        return cls(
            bomb,
            unknown_0xe8907530,
            unknown_0x0a9186cb,
            unknown_0x519c83e7,
            unknown_0xea7f3336,
            unknown_0xba3ef7ea,
            unknown_0xebdf0b9b,
            unknown_0xf9125d7e,
            missile,
            unknown_0xe58d6c84,
            unknown_0xd26376fd,
            missile_reload_time,
            power_beam,
            unknown_0x86a941fc,
            unknown_0x25906c03,
            phazon_beam,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x10")  # 16 properties

        data.write(b"as\xad\x96")  # 0x6173ad96
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.bomb.to_stream(
            data, game, default_override={"weapon_type": 7, "radius_damage_amount": 10.0, "damage_radius": 3.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe8\x90u0")  # 0xe8907530
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe8907530))

        data.write(b"\n\x91\x86\xcb")  # 0xa9186cb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0a9186cb))

        data.write(b"Q\x9c\x83\xe7")  # 0x519c83e7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x519c83e7))

        data.write(b"\xea\x7f36")  # 0xea7f3336
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xea7f3336))

        data.write(b"\xba>\xf7\xea")  # 0xba3ef7ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xba3ef7ea))

        data.write(b"\xeb\xdf\x0b\x9b")  # 0xebdf0b9b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xebdf0b9b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf9\x12]~")  # 0xf9125d7e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xf9125d7e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X\xf0\x0b\n")  # 0x58f00b0a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.missile.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 4,
                "damage_amount": 30.0,
                "radius_damage_amount": 15.0,
                "damage_radius": 4.5,
                "knock_back_power": 4.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe5\x8dl\x84")  # 0xe58d6c84
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xe58d6c84.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 5,
                "damage_amount": 30.0,
                "radius_damage_amount": 15.0,
                "damage_radius": 4.5,
                "knock_back_power": 4.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd2cv\xfd")  # 0xd26376fd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xd26376fd.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 5,
                "damage_amount": 30.0,
                "radius_damage_amount": 15.0,
                "damage_radius": 4.5,
                "knock_back_power": 4.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"C\xf0\xa8\xa0")  # 0x43f0a8a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.missile_reload_time))

        data.write(b"\x1fl\x1ak")  # 0x1f6c1a6b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.power_beam.to_stream(data, game, default_override={"cooldown": 0.11100000143051147})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x86\xa9A\xfc")  # 0x86a941fc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x86a941fc.to_stream(data, game, default_override={"cooldown": 0.5})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"%\x90l\x03")  # 0x25906c03
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x25906c03.to_stream(data, game, default_override={"cooldown": 0.33000001311302185})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdd_.=")  # 0xdd5f2e3d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.phazon_beam.to_stream(data, game, default_override={"cooldown": 0.10000000149011612})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_WeaponsJson", data)
        return cls(
            bomb=TDamageInfo.from_json(json_data["bomb"]),
            unknown_0xe8907530=json_data["unknown_0xe8907530"],
            unknown_0x0a9186cb=json_data["unknown_0x0a9186cb"],
            unknown_0x519c83e7=json_data["unknown_0x519c83e7"],
            unknown_0xea7f3336=json_data["unknown_0xea7f3336"],
            unknown_0xba3ef7ea=json_data["unknown_0xba3ef7ea"],
            unknown_0xebdf0b9b=Spline.from_json(json_data["unknown_0xebdf0b9b"]),
            unknown_0xf9125d7e=Spline.from_json(json_data["unknown_0xf9125d7e"]),
            missile=TDamageInfo.from_json(json_data["missile"]),
            unknown_0xe58d6c84=TDamageInfo.from_json(json_data["unknown_0xe58d6c84"]),
            unknown_0xd26376fd=TDamageInfo.from_json(json_data["unknown_0xd26376fd"]),
            missile_reload_time=json_data["missile_reload_time"],
            power_beam=TBeamInfo.from_json(json_data["power_beam"]),
            unknown_0x86a941fc=TBeamInfo.from_json(json_data["unknown_0x86a941fc"]),
            unknown_0x25906c03=TBeamInfo.from_json(json_data["unknown_0x25906c03"]),
            phazon_beam=TBeamInfo.from_json(json_data["phazon_beam"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "bomb": self.bomb.to_json(),
            "unknown_0xe8907530": self.unknown_0xe8907530,
            "unknown_0x0a9186cb": self.unknown_0x0a9186cb,
            "unknown_0x519c83e7": self.unknown_0x519c83e7,
            "unknown_0xea7f3336": self.unknown_0xea7f3336,
            "unknown_0xba3ef7ea": self.unknown_0xba3ef7ea,
            "unknown_0xebdf0b9b": self.unknown_0xebdf0b9b.to_json(),
            "unknown_0xf9125d7e": self.unknown_0xf9125d7e.to_json(),
            "missile": self.missile.to_json(),
            "unknown_0xe58d6c84": self.unknown_0xe58d6c84.to_json(),
            "unknown_0xd26376fd": self.unknown_0xd26376fd.to_json(),
            "missile_reload_time": self.missile_reload_time,
            "power_beam": self.power_beam.to_json(),
            "unknown_0x86a941fc": self.unknown_0x86a941fc.to_json(),
            "unknown_0x25906c03": self.unknown_0x25906c03.to_json(),
            "phazon_beam": self.phazon_beam.to_json(),
        }


def _decode_bomb(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"weapon_type": 7, "radius_damage_amount": 10.0, "damage_radius": 3.0},
    )


def _decode_unknown_0xebdf0b9b(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0xf9125d7e(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_missile(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "weapon_type": 4,
            "damage_amount": 30.0,
            "radius_damage_amount": 15.0,
            "damage_radius": 4.5,
            "knock_back_power": 4.0,
        },
    )


def _decode_unknown_0xe58d6c84(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "weapon_type": 5,
            "damage_amount": 30.0,
            "radius_damage_amount": 15.0,
            "damage_radius": 4.5,
            "knock_back_power": 4.0,
        },
    )


def _decode_unknown_0xd26376fd(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "weapon_type": 5,
            "damage_amount": 30.0,
            "radius_damage_amount": 15.0,
            "damage_radius": 4.5,
            "knock_back_power": 4.0,
        },
    )


def _decode_power_beam(data: typing.BinaryIO, game: Game, property_size: int) -> TBeamInfo:
    return TBeamInfo.from_stream(data, game, property_size, default_override={"cooldown": 0.11100000143051147})


def _decode_unknown_0x86a941fc(data: typing.BinaryIO, game: Game, property_size: int) -> TBeamInfo:
    return TBeamInfo.from_stream(data, game, property_size, default_override={"cooldown": 0.5})


def _decode_unknown_0x25906c03(data: typing.BinaryIO, game: Game, property_size: int) -> TBeamInfo:
    return TBeamInfo.from_stream(data, game, property_size, default_override={"cooldown": 0.33000001311302185})


def _decode_phazon_beam(data: typing.BinaryIO, game: Game, property_size: int) -> TBeamInfo:
    return TBeamInfo.from_stream(data, game, property_size, default_override={"cooldown": 0.10000000149011612})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6173AD96: ("bomb", _decode_bomb),
    0xE8907530: ("unknown_0xe8907530", structs.decode_BIG_f),
    0x0A9186CB: ("unknown_0x0a9186cb", structs.decode_BIG_f),
    0x519C83E7: ("unknown_0x519c83e7", structs.decode_BIG_f),
    0xEA7F3336: ("unknown_0xea7f3336", structs.decode_BIG_f),
    0xBA3EF7EA: ("unknown_0xba3ef7ea", structs.decode_BIG_f),
    0xEBDF0B9B: ("unknown_0xebdf0b9b", _decode_unknown_0xebdf0b9b),
    0xF9125D7E: ("unknown_0xf9125d7e", _decode_unknown_0xf9125d7e),
    0x58F00B0A: ("missile", _decode_missile),
    0xE58D6C84: ("unknown_0xe58d6c84", _decode_unknown_0xe58d6c84),
    0xD26376FD: ("unknown_0xd26376fd", _decode_unknown_0xd26376fd),
    0x43F0A8A0: ("missile_reload_time", structs.decode_BIG_f),
    0x1F6C1A6B: ("power_beam", _decode_power_beam),
    0x86A941FC: ("unknown_0x86a941fc", _decode_unknown_0x86a941fc),
    0x25906C03: ("unknown_0x25906c03", _decode_unknown_0x25906c03),
    0xDD5F2E3D: ("phazon_beam", _decode_phazon_beam),
}
