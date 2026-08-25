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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct38Json(typing_extensions.TypedDict):
        range: float
        turn_rate: float
        sound_effect: int
        warp_scale: float
        repel_offset: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x3642A398, 0xE34DC703, 0x8D3BA8AE, 0xB99098D9, 0xB3252324)


@dataclasses.dataclass()
class UnknownStruct38(BaseProperty):
    range: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3642A398, original_name="Range"),
        },
    )
    turn_rate: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE34DC703, original_name="TurnRate"),
        },
    )
    sound_effect: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x8D3BA8AE, original_name="SoundEffect"),
        },
    )
    warp_scale: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB99098D9, original_name="WarpScale"),
        },
    )
    repel_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=1.0, z=5.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xB3252324, original_name="RepelOffset", from_json=Vector.from_json, to_json=Vector.to_json
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
        if property_count != 5:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHlLHfLHfff")

        dec = _FAST_FORMAT.unpack(data.read(58))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            Vector(*dec[14:17]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"6B\xa3\x98")  # 0x3642a398
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.range))

        data.write(b"\xe3M\xc7\x03")  # 0xe34dc703
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_rate))

        data.write(b"\x8d;\xa8\xae")  # 0x8d3ba8ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_effect))

        data.write(b"\xb9\x90\x98\xd9")  # 0xb99098d9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.warp_scale))

        data.write(b"\xb3%#$")  # 0xb3252324
        data.write(b"\x00\x0c")  # size
        self.repel_offset.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct38Json", data)
        return cls(
            range=json_data["range"],
            turn_rate=json_data["turn_rate"],
            sound_effect=json_data["sound_effect"],
            warp_scale=json_data["warp_scale"],
            repel_offset=Vector.from_json(json_data["repel_offset"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "range": self.range,
            "turn_rate": self.turn_rate,
            "sound_effect": self.sound_effect,
            "warp_scale": self.warp_scale,
            "repel_offset": self.repel_offset.to_json(),
        }

    def _dependencies_for_sound_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_sound_effect(asset_manager)


def _decode_repel_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x3642A398: ("range", structs.decode_BIG_f),
    0xE34DC703: ("turn_rate", structs.decode_BIG_f),
    0x8D3BA8AE: ("sound_effect", structs.decode_BIG_l),
    0xB99098D9: ("warp_scale", structs.decode_BIG_f),
    0xB3252324: ("repel_offset", _decode_repel_offset),
}
