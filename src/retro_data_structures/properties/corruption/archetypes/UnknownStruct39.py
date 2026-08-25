# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.GhorStructC import GhorStructC
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct39Json(typing_extensions.TypedDict):
        ghor_struct_c: json_util.JsonObject
        reset_time: float
        reset_damage: float
        activate_spline: json_util.JsonObject
        deactivate_spline: json_util.JsonObject
        active_effect: str
        hit_effect: str
        inactive_effect: str
        caud: int
        shield_off_sound: int


@dataclasses.dataclass()
class UnknownStruct39(BaseProperty):
    ghor_struct_c: GhorStructC = dataclasses.field(
        default_factory=GhorStructC,
        metadata={
            "reflection": FieldReflection[GhorStructC](
                GhorStructC,
                id=0xFDEA5D06,
                original_name="GhorStructC",
                from_json=GhorStructC.from_json,
                to_json=GhorStructC.to_json,
            ),
        },
    )
    reset_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2BCD1D77, original_name="ResetTime"),
        },
    )
    reset_damage: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FEC6162, original_name="ResetDamage"),
        },
    )
    activate_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x39D64E40,
                original_name="ActivateSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    deactivate_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xFC336BED,
                original_name="DeactivateSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    active_effect: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x60BDAA38, original_name="ActiveEffect"),
        },
    )
    hit_effect: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xC60B41B4, original_name="HitEffect"),
        },
    )
    inactive_effect: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x67808780, original_name="InactiveEffect"),
        },
    )
    caud: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x62771F66, original_name="CAUD"),
        },
    )
    shield_off_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB75B8442, original_name="ShieldOffSound"),
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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFDEA5D06
        ghor_struct_c = GhorStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BCD1D77
        reset_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FEC6162
        reset_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39D64E40
        activate_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC336BED
        deactivate_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60BDAA38
        active_effect = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC60B41B4
        hit_effect = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67808780
        inactive_effect = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62771F66
        caud = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB75B8442
        shield_off_sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            ghor_struct_c,
            reset_time,
            reset_damage,
            activate_spline,
            deactivate_spline,
            active_effect,
            hit_effect,
            inactive_effect,
            caud,
            shield_off_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"\xfd\xea]\x06")  # 0xfdea5d06
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+\xcd\x1dw")  # 0x2bcd1d77
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reset_time))

        data.write(b"\x7f\xecab")  # 0x7fec6162
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reset_damage))

        data.write(b"9\xd6N@")  # 0x39d64e40
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.activate_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfc3k\xed")  # 0xfc336bed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.deactivate_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"`\xbd\xaa8")  # 0x60bdaa38
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.active_effect.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\x0bA\xb4")  # 0xc60b41b4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.hit_effect.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"g\x80\x87\x80")  # 0x67808780
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.inactive_effect.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"bw\x1ff")  # 0x62771f66
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud))

        data.write(b"\xb7[\x84B")  # 0xb75b8442
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.shield_off_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct39Json", data)
        return cls(
            ghor_struct_c=GhorStructC.from_json(json_data["ghor_struct_c"]),
            reset_time=json_data["reset_time"],
            reset_damage=json_data["reset_damage"],
            activate_spline=Spline.from_json(json_data["activate_spline"]),
            deactivate_spline=Spline.from_json(json_data["deactivate_spline"]),
            active_effect=json_data["active_effect"],
            hit_effect=json_data["hit_effect"],
            inactive_effect=json_data["inactive_effect"],
            caud=json_data["caud"],
            shield_off_sound=json_data["shield_off_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "ghor_struct_c": self.ghor_struct_c.to_json(),
            "reset_time": self.reset_time,
            "reset_damage": self.reset_damage,
            "activate_spline": self.activate_spline.to_json(),
            "deactivate_spline": self.deactivate_spline.to_json(),
            "active_effect": self.active_effect,
            "hit_effect": self.hit_effect,
            "inactive_effect": self.inactive_effect,
            "caud": self.caud,
            "shield_off_sound": self.shield_off_sound,
        }


def _decode_ghor_struct_c(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructC:
    return GhorStructC.from_stream(data, game, property_size)


def _decode_activate_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_deactivate_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_active_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_hit_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_inactive_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFDEA5D06: ("ghor_struct_c", _decode_ghor_struct_c),
    0x2BCD1D77: ("reset_time", structs.decode_BIG_f),
    0x7FEC6162: ("reset_damage", structs.decode_BIG_f),
    0x39D64E40: ("activate_spline", _decode_activate_spline),
    0xFC336BED: ("deactivate_spline", _decode_deactivate_spline),
    0x60BDAA38: ("active_effect", _decode_active_effect),
    0xC60B41B4: ("hit_effect", _decode_hit_effect),
    0x67808780: ("inactive_effect", _decode_inactive_effect),
    0x62771F66: ("caud", structs.decode_BIG_Q),
    0xB75B8442: ("shield_off_sound", structs.decode_BIG_Q),
}
