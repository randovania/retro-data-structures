# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakTargeting_LockFireJson(typing_extensions.TypedDict):
        lock_fire_reticle_scale: float
        lock_fire_anim_time: float
        lock_fire_color: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xD4E59E59, 0xB79DE7E8, 0xF5E9899F)


@dataclasses.dataclass()
class TweakTargeting_LockFire(BaseProperty):
    lock_fire_reticle_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4E59E59, original_name="LockFireReticleScale"),
        },
    )
    lock_fire_anim_time: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB79DE7E8, original_name="LockFireAnimTime"),
        },
    )
    lock_fire_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF5E9899F, original_name="LockFireColor", from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 3:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHffff")

        dec = _FAST_FORMAT.unpack(data.read(42))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            Color(*dec[8:12]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\xd4\xe5\x9eY")  # 0xd4e59e59
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lock_fire_reticle_scale))

        data.write(b"\xb7\x9d\xe7\xe8")  # 0xb79de7e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lock_fire_anim_time))

        data.write(b"\xf5\xe9\x89\x9f")  # 0xf5e9899f
        data.write(b"\x00\x10")  # size
        self.lock_fire_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_LockFireJson", data)
        return cls(
            lock_fire_reticle_scale=json_data["lock_fire_reticle_scale"],
            lock_fire_anim_time=json_data["lock_fire_anim_time"],
            lock_fire_color=Color.from_json(json_data["lock_fire_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "lock_fire_reticle_scale": self.lock_fire_reticle_scale,
            "lock_fire_anim_time": self.lock_fire_anim_time,
            "lock_fire_color": self.lock_fire_color.to_json(),
        }


def _decode_lock_fire_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD4E59E59: ("lock_fire_reticle_scale", structs.decode_BIG_f),
    0xB79DE7E8: ("lock_fire_anim_time", structs.decode_BIG_f),
    0xF5E9899F: ("lock_fire_color", _decode_lock_fire_color),
}
