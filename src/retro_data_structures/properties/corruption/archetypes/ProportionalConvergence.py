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

    class ProportionalConvergenceJson(typing_extensions.TypedDict):
        velocity: float
        dampening_control: json_util.JsonObject


@dataclasses.dataclass()
class ProportionalConvergence(BaseProperty):
    velocity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x02F01683, original_name="Velocity"),
        },
    )
    dampening_control: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xF7FBA2BF,
                original_name="DampeningControl",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
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
        assert property_id == 0x02F01683
        velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF7FBA2BF
        dampening_control = Spline.from_stream(data, game, property_size)

        return cls(velocity, dampening_control)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\x02\xf0\x16\x83")  # 0x2f01683
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.velocity))

        data.write(b"\xf7\xfb\xa2\xbf")  # 0xf7fba2bf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dampening_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ProportionalConvergenceJson", data)
        return cls(
            velocity=json_data["velocity"],
            dampening_control=Spline.from_json(json_data["dampening_control"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "velocity": self.velocity,
            "dampening_control": self.dampening_control.to_json(),
        }


def _decode_dampening_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x02F01683: ("velocity", structs.decode_BIG_f),
    0xF7FBA2BF: ("dampening_control", _decode_dampening_control),
}
