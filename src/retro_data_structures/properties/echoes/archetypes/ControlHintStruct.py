# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.ControllerActionStruct import ControllerActionStruct
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ControlHintStructJson(typing_extensions.TypedDict):
        command: json_util.JsonObject
        state: int


@dataclasses.dataclass()
class ControlHintStruct(BaseProperty):
    command: ControllerActionStruct = dataclasses.field(
        default_factory=ControllerActionStruct,
        metadata={
            "reflection": FieldReflection[ControllerActionStruct](
                ControllerActionStruct,
                id=0x359C7AAF,
                original_name="Command",
                from_json=ControllerActionStruct.from_json,
                to_json=ControllerActionStruct.to_json,
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
        if property_count != 2:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x359C7AAF
        command = ControllerActionStruct.from_stream(
            data, game, property_size, default_override={"command": enums.ControllerActionCommandEnum._None}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4063422A
        state = structs.BIG_l.unpack(data.read(4))[0]

        return cls(command, state)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"5\x9cz\xaf")  # 0x359c7aaf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.command.to_stream(data, game, default_override={"command": enums.ControllerActionCommandEnum._None})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"@cB*")  # 0x4063422a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.state))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ControlHintStructJson", data)
        return cls(
            command=ControllerActionStruct.from_json(json_data["command"]),
            state=json_data["state"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "command": self.command.to_json(),
            "state": self.state,
        }


def _decode_command(data: typing.BinaryIO, game: Game, property_size: int) -> ControllerActionStruct:
    return ControllerActionStruct.from_stream(
        data, game, property_size, default_override={"command": enums.ControllerActionCommandEnum._None}
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x359C7AAF: ("command", _decode_command),
    0x4063422A: ("state", structs.decode_BIG_l),
}
