# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.ControlCommands import ControlCommands
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CommandDataJson(typing_extensions.TypedDict):
        used: bool
        control_command: json_util.JsonObject
        state: int


@dataclasses.dataclass()
class CommandData(BaseProperty):
    used: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1AD5B168, original_name="Used"),
        },
    )
    control_command: ControlCommands = dataclasses.field(
        default_factory=ControlCommands,
        metadata={
            "reflection": FieldReflection[ControlCommands](
                ControlCommands,
                id=0x07527B3A,
                original_name="ControlCommand",
                from_json=ControlCommands.from_json,
                to_json=ControlCommands.to_json,
            ),
        },
    )
    state: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x4063422A, original_name="State"),
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
        assert property_id == 0x1AD5B168
        used = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07527B3A
        control_command = ControlCommands.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4063422A
        state = structs.BIG_l.unpack(data.read(4))[0]

        return cls(used, control_command, state)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\x1a\xd5\xb1h")  # 0x1ad5b168
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.used))

        data.write(b"\x07R{:")  # 0x7527b3a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.control_command.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"@cB*")  # 0x4063422a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.state))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CommandDataJson", data)
        return cls(
            used=json_data["used"],
            control_command=ControlCommands.from_json(json_data["control_command"]),
            state=json_data["state"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "used": self.used,
            "control_command": self.control_command.to_json(),
            "state": self.state,
        }


def _decode_control_command(data: typing.BinaryIO, game: Game, property_size: int) -> ControlCommands:
    return ControlCommands.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1AD5B168: ("used", structs.decode_BIG_bool_),
    0x07527B3A: ("control_command", _decode_control_command),
    0x4063422A: ("state", structs.decode_BIG_l),
}
