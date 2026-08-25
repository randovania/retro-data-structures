# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.SpindlePositionInterpolant import SpindlePositionInterpolant
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct23Json(typing_extensions.TypedDict):
        look_at_position: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct23(BaseProperty):
    look_at_position: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x43A6DED6,
                original_name="LookAtPosition",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43A6DED6
        look_at_position = SpindlePositionInterpolant.from_stream(data, game, property_size)

        return cls(look_at_position)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b"C\xa6\xde\xd6")  # 0x43a6ded6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_at_position.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct23Json", data)
        return cls(
            look_at_position=SpindlePositionInterpolant.from_json(json_data["look_at_position"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "look_at_position": self.look_at_position.to_json(),
        }


def _decode_look_at_position(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x43A6DED6: ("look_at_position", _decode_look_at_position),
}
