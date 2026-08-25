# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ModIncaDataJson(typing_extensions.TypedDict):
        mod_inca_color: json_util.JsonValue
        mod_inca_amount: json_util.JsonObject


@dataclasses.dataclass()
class ModIncaData(BaseProperty):
    mod_inca_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF8DF6CD2, original_name="ModIncaColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    mod_inca_amount: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xC23011D9, original_name="ModIncaAmount", from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 2:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8DF6CD2
        mod_inca_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC23011D9
        mod_inca_amount = Spline.from_stream(data, game, property_size)

        return cls(mod_inca_color, mod_inca_amount)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\xf8\xdfl\xd2")  # 0xf8df6cd2
        data.write(b"\x00\x10")  # size
        self.mod_inca_color.to_stream(data, game)

        data.write(b"\xc20\x11\xd9")  # 0xc23011d9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.mod_inca_amount.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ModIncaDataJson", data)
        return cls(
            mod_inca_color=Color.from_json(json_data["mod_inca_color"]),
            mod_inca_amount=Spline.from_json(json_data["mod_inca_amount"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "mod_inca_color": self.mod_inca_color.to_json(),
            "mod_inca_amount": self.mod_inca_amount.to_json(),
        }


def _decode_mod_inca_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_mod_inca_amount(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF8DF6CD2: ("mod_inca_color", _decode_mod_inca_color),
    0xC23011D9: ("mod_inca_amount", _decode_mod_inca_amount),
}
