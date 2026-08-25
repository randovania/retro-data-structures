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

    class PuddleControlPhaseDataJson(typing_extensions.TypedDict):
        generation_rate: float
        effect_rate: float
        move_rate: float
        duration: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x23E91E15, 0x82403CBD, 0x7EC9E6D9, 0x8B51E23F)


@dataclasses.dataclass()
class PuddleControlPhaseData(BaseProperty):
    generation_rate: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23E91E15, original_name="GenerationRate"),
        },
    )
    effect_rate: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x82403CBD, original_name="EffectRate"),
        },
    )
    move_rate: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7EC9E6D9, original_name="MoveRate"),
        },
    )
    duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B51E23F, original_name="Duration"),
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
        if property_count != 4:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(40))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"#\xe9\x1e\x15")  # 0x23e91e15
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.generation_rate))

        data.write(b"\x82@<\xbd")  # 0x82403cbd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.effect_rate))

        data.write(b"~\xc9\xe6\xd9")  # 0x7ec9e6d9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_rate))

        data.write(b"\x8bQ\xe2?")  # 0x8b51e23f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PuddleControlPhaseDataJson", data)
        return cls(
            generation_rate=json_data["generation_rate"],
            effect_rate=json_data["effect_rate"],
            move_rate=json_data["move_rate"],
            duration=json_data["duration"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "generation_rate": self.generation_rate,
            "effect_rate": self.effect_rate,
            "move_rate": self.move_rate,
            "duration": self.duration,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x23E91E15: ("generation_rate", structs.decode_BIG_f),
    0x82403CBD: ("effect_rate", structs.decode_BIG_f),
    0x7EC9E6D9: ("move_rate", structs.decode_BIG_f),
    0x8B51E23F: ("duration", structs.decode_BIG_f),
}
