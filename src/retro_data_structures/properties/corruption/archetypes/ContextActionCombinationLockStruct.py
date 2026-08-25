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

    class ContextActionCombinationLockStructJson(typing_extensions.TypedDict):
        initial_angle: float
        unlock_angle: float
        min_angle: float
        max_angle: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x90AC8041, 0x89C4CC5F, 0x992C2DF5, 0xD9635583)


@dataclasses.dataclass()
class ContextActionCombinationLockStruct(BaseProperty):
    initial_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90AC8041, original_name="InitialAngle"),
        },
    )
    unlock_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x89C4CC5F, original_name="UnlockAngle"),
        },
    )
    min_angle: float = dataclasses.field(
        default=-90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x992C2DF5, original_name="MinAngle"),
        },
    )
    max_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD9635583, original_name="MaxAngle"),
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

        data.write(b"\x90\xac\x80A")  # 0x90ac8041
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_angle))

        data.write(b"\x89\xc4\xcc_")  # 0x89c4cc5f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unlock_angle))

        data.write(b"\x99,-\xf5")  # 0x992c2df5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_angle))

        data.write(b"\xd9cU\x83")  # 0xd9635583
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_angle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ContextActionCombinationLockStructJson", data)
        return cls(
            initial_angle=json_data["initial_angle"],
            unlock_angle=json_data["unlock_angle"],
            min_angle=json_data["min_angle"],
            max_angle=json_data["max_angle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "initial_angle": self.initial_angle,
            "unlock_angle": self.unlock_angle,
            "min_angle": self.min_angle,
            "max_angle": self.max_angle,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x90AC8041: ("initial_angle", structs.decode_BIG_f),
    0x89C4CC5F: ("unlock_angle", structs.decode_BIG_f),
    0x992C2DF5: ("min_angle", structs.decode_BIG_f),
    0xD9635583: ("max_angle", structs.decode_BIG_f),
}
