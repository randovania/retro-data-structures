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

    class TweakPlayerGun_HolsteringJson(typing_extensions.TypedDict):
        gun_holster_time: float
        gun_not_firing_time: float
        gun_holstered_angle: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x7EE98EBB, 0xEC515CD5, 0x448573F)


@dataclasses.dataclass()
class TweakPlayerGun_Holstering(BaseProperty):
    gun_holster_time: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7EE98EBB, original_name="GunHolsterTime"),
        },
    )
    gun_not_firing_time: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC515CD5, original_name="GunNotFiringTime"),
        },
    )
    gun_holstered_angle: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0448573F, original_name="GunHolsteredAngle"),
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
        if property_count != 3:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(30))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"~\xe9\x8e\xbb")  # 0x7ee98ebb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gun_holster_time))

        data.write(b"\xecQ\\\xd5")  # 0xec515cd5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gun_not_firing_time))

        data.write(b"\x04HW?")  # 0x448573f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gun_holstered_angle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_HolsteringJson", data)
        return cls(
            gun_holster_time=json_data["gun_holster_time"],
            gun_not_firing_time=json_data["gun_not_firing_time"],
            gun_holstered_angle=json_data["gun_holstered_angle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "gun_holster_time": self.gun_holster_time,
            "gun_not_firing_time": self.gun_not_firing_time,
            "gun_holstered_angle": self.gun_holstered_angle,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7EE98EBB: ("gun_holster_time", structs.decode_BIG_f),
    0xEC515CD5: ("gun_not_firing_time", structs.decode_BIG_f),
    0x0448573F: ("gun_holstered_angle", structs.decode_BIG_f),
}
