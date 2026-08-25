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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FlareDefJson(typing_extensions.TypedDict):
        texture: int
        position: float
        scale: float
        color: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xD1F65872, 0xCB99B4DA, 0x2C51A676, 0x37C7D09D)


@dataclasses.dataclass()
class FlareDef(BaseProperty):
    texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD1F65872, original_name="Texture"),
        },
    )
    position: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCB99B4DA, original_name="Position"),
        },
    )
    scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C51A676, original_name="Scale"),
        },
    )
    color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x37C7D09D, original_name="Color", from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 4:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHQLHfLHfLHffff")

        dec = _FAST_FORMAT.unpack(data.read(56))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            Color(*dec[11:15]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\xd1\xf6Xr")  # 0xd1f65872
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.texture))

        data.write(b"\xcb\x99\xb4\xda")  # 0xcb99b4da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.position))

        data.write(b",Q\xa6v")  # 0x2c51a676
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scale))

        data.write(b"7\xc7\xd0\x9d")  # 0x37c7d09d
        data.write(b"\x00\x10")  # size
        self.color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlareDefJson", data)
        return cls(
            texture=json_data["texture"],
            position=json_data["position"],
            scale=json_data["scale"],
            color=Color.from_json(json_data["color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "texture": self.texture,
            "position": self.position,
            "scale": self.scale,
            "color": self.color.to_json(),
        }


def _decode_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD1F65872: ("texture", structs.decode_BIG_Q),
    0xCB99B4DA: ("position", structs.decode_BIG_f),
    0x2C51A676: ("scale", structs.decode_BIG_f),
    0x37C7D09D: ("color", _decode_color),
}
