# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TranslationSplinesJson(typing_extensions.TypedDict):
        x_translation: json_util.JsonObject
        y_translation: json_util.JsonObject
        z_translation: json_util.JsonObject


@dataclasses.dataclass()
class TranslationSplines(BaseProperty):
    x_translation: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x24E9A09B, original_name="XTranslation", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    y_translation: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xCBBB167A, original_name="YTranslation", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    z_translation: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x213DCB18, original_name="ZTranslation", from_json=Spline.from_json, to_json=Spline.to_json
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24E9A09B
        x_translation = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCBBB167A
        y_translation = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x213DCB18
        z_translation = Spline.from_stream(data, game, property_size)

        return cls(x_translation, y_translation, z_translation)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"$\xe9\xa0\x9b")  # 0x24e9a09b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.x_translation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcb\xbb\x16z")  # 0xcbbb167a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.y_translation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"!=\xcb\x18")  # 0x213dcb18
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.z_translation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TranslationSplinesJson", data)
        return cls(
            x_translation=Spline.from_json(json_data["x_translation"]),
            y_translation=Spline.from_json(json_data["y_translation"]),
            z_translation=Spline.from_json(json_data["z_translation"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "x_translation": self.x_translation.to_json(),
            "y_translation": self.y_translation.to_json(),
            "z_translation": self.z_translation.to_json(),
        }


def _decode_x_translation(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_y_translation(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_z_translation(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x24E9A09B: ("x_translation", _decode_x_translation),
    0xCBBB167A: ("y_translation", _decode_y_translation),
    0x213DCB18: ("z_translation", _decode_z_translation),
}
