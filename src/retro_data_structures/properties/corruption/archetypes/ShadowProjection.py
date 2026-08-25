# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ShadowProjectionJson(typing_extensions.TypedDict):
        shadow_projection: int


class ShadowProjectionEnum(enum.IntEnum):
    Unknown1 = 2220656430
    Unknown2 = 2690336603
    Unknown3 = 1214374227
    Unknown4 = 4117616162
    Unknown5 = 3804557437
    Unknown6 = 193846629

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = 0x4B424A39


@dataclasses.dataclass()
class ShadowProjection(BaseProperty):
    shadow_projection: ShadowProjectionEnum = dataclasses.field(
        default=ShadowProjectionEnum.Unknown1,
        metadata={
            "reflection": FieldReflection[ShadowProjectionEnum](
                ShadowProjectionEnum,
                id=0x4B424A39,
                original_name="ShadowProjection",
                from_json=ShadowProjectionEnum.from_json,
                to_json=ShadowProjectionEnum.to_json,
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
        if property_count != 1:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHL")

        dec = _FAST_FORMAT.unpack(data.read(10))
        assert (dec[0]) == _FAST_IDS
        return cls(
            ShadowProjectionEnum(dec[2]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b"KBJ9")  # 0x4b424a39
        data.write(b"\x00\x04")  # size
        self.shadow_projection.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShadowProjectionJson", data)
        return cls(
            shadow_projection=ShadowProjectionEnum.from_json(json_data["shadow_projection"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "shadow_projection": self.shadow_projection.to_json(),
        }


def _decode_shadow_projection(data: typing.BinaryIO, game: Game, property_size: int) -> ShadowProjectionEnum:
    return ShadowProjectionEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4B424A39: ("shadow_projection", _decode_shadow_projection),
}
