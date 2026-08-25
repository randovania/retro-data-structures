# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.ControlCommands import ControlCommands
from retro_data_structures.properties.corruption.archetypes.RevolutionControl_UnknownStruct1 import (
    RevolutionControl_UnknownStruct1,
)
from retro_data_structures.properties.corruption.archetypes.RevolutionPhysicalControl import RevolutionPhysicalControl
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class RevolutionControlJson(typing_extensions.TypedDict):
        command_enum: json_util.JsonObject
        revolution_control_type: int
        physical_control: json_util.JsonObject
        unknown_0x6e14bc06: int
        unknown_0xf0bf68a4: json_util.JsonObject
        revolution_virtual_control: int
        unknown_0xebaabf01: int
        unknown_0xeda6d736: int
        unknown_0xbf80d594: int
        unknown_0x91b8c18a: json_util.JsonObject


@dataclasses.dataclass()
class RevolutionControl(BaseProperty):
    command_enum: ControlCommands = dataclasses.field(
        default_factory=ControlCommands,
        metadata={
            "reflection": FieldReflection[ControlCommands](
                ControlCommands,
                id=0xB0D17D4D,
                original_name="CommandEnum",
                from_json=ControlCommands.from_json,
                to_json=ControlCommands.to_json,
            ),
        },
    )
    revolution_control_type: enums.RevolutionControlTypeEnum = dataclasses.field(
        default=enums.RevolutionControlTypeEnum.Unknown2,
        metadata={
            "reflection": FieldReflection[enums.RevolutionControlTypeEnum](
                enums.RevolutionControlTypeEnum,
                id=0x81CC3D3E,
                original_name="RevolutionControlType",
                from_json=enums.RevolutionControlTypeEnum.from_json,
                to_json=enums.RevolutionControlTypeEnum.to_json,
            ),
        },
    )
    physical_control: RevolutionPhysicalControl = dataclasses.field(
        default_factory=RevolutionPhysicalControl,
        metadata={
            "reflection": FieldReflection[RevolutionPhysicalControl](
                RevolutionPhysicalControl,
                id=0xE646D3B7,
                original_name="PhysicalControl",
                from_json=RevolutionPhysicalControl.from_json,
                to_json=RevolutionPhysicalControl.to_json,
            ),
        },
    )
    unknown_0x6e14bc06: enums.PhysicalControlBooleanEnum = dataclasses.field(
        default=enums.PhysicalControlBooleanEnum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.PhysicalControlBooleanEnum](
                enums.PhysicalControlBooleanEnum,
                id=0x6E14BC06,
                original_name="Unknown",
                from_json=enums.PhysicalControlBooleanEnum.from_json,
                to_json=enums.PhysicalControlBooleanEnum.to_json,
            ),
        },
    )
    unknown_0xf0bf68a4: RevolutionPhysicalControl = dataclasses.field(
        default_factory=RevolutionPhysicalControl,
        metadata={
            "reflection": FieldReflection[RevolutionPhysicalControl](
                RevolutionPhysicalControl,
                id=0xF0BF68A4,
                original_name="Unknown",
                from_json=RevolutionPhysicalControl.from_json,
                to_json=RevolutionPhysicalControl.to_json,
            ),
        },
    )
    revolution_virtual_control: enums.RevolutionVirtualControlEnum = dataclasses.field(
        default=enums.RevolutionVirtualControlEnum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.RevolutionVirtualControlEnum](
                enums.RevolutionVirtualControlEnum,
                id=0xFE819DDB,
                original_name="RevolutionVirtualControl",
                from_json=enums.RevolutionVirtualControlEnum.from_json,
                to_json=enums.RevolutionVirtualControlEnum.to_json,
            ),
        },
    )
    unknown_0xebaabf01: enums.PhysicalControlBooleanEnum = dataclasses.field(
        default=enums.PhysicalControlBooleanEnum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.PhysicalControlBooleanEnum](
                enums.PhysicalControlBooleanEnum,
                id=0xEBAABF01,
                original_name="Unknown",
                from_json=enums.PhysicalControlBooleanEnum.from_json,
                to_json=enums.PhysicalControlBooleanEnum.to_json,
            ),
        },
    )
    unknown_0xeda6d736: enums.RevolutionVirtualControlEnum = dataclasses.field(
        default=enums.RevolutionVirtualControlEnum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.RevolutionVirtualControlEnum](
                enums.RevolutionVirtualControlEnum,
                id=0xEDA6D736,
                original_name="Unknown",
                from_json=enums.RevolutionVirtualControlEnum.from_json,
                to_json=enums.RevolutionVirtualControlEnum.to_json,
            ),
        },
    )
    unknown_0xbf80d594: enums.RevolutionControl_UnknownEnum1Enum = dataclasses.field(
        default=enums.RevolutionControl_UnknownEnum1Enum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.RevolutionControl_UnknownEnum1Enum](
                enums.RevolutionControl_UnknownEnum1Enum,
                id=0xBF80D594,
                original_name="Unknown",
                from_json=enums.RevolutionControl_UnknownEnum1Enum.from_json,
                to_json=enums.RevolutionControl_UnknownEnum1Enum.to_json,
            ),
        },
    )
    unknown_0x91b8c18a: RevolutionControl_UnknownStruct1 = dataclasses.field(
        default_factory=RevolutionControl_UnknownStruct1,
        metadata={
            "reflection": FieldReflection[RevolutionControl_UnknownStruct1](
                RevolutionControl_UnknownStruct1,
                id=0x91B8C18A,
                original_name="Unknown",
                from_json=RevolutionControl_UnknownStruct1.from_json,
                to_json=RevolutionControl_UnknownStruct1.to_json,
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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB0D17D4D
        command_enum = ControlCommands.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81CC3D3E
        revolution_control_type = enums.RevolutionControlTypeEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE646D3B7
        physical_control = RevolutionPhysicalControl.from_stream(
            data, game, property_size, default_override={"physical_control": enums.PhysicalControlEnum.Unknown3}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E14BC06
        unknown_0x6e14bc06 = enums.PhysicalControlBooleanEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0BF68A4
        unknown_0xf0bf68a4 = RevolutionPhysicalControl.from_stream(
            data, game, property_size, default_override={"physical_control": enums.PhysicalControlEnum.Unknown3}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE819DDB
        revolution_virtual_control = enums.RevolutionVirtualControlEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBAABF01
        unknown_0xebaabf01 = enums.PhysicalControlBooleanEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDA6D736
        unknown_0xeda6d736 = enums.RevolutionVirtualControlEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF80D594
        unknown_0xbf80d594 = enums.RevolutionControl_UnknownEnum1Enum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91B8C18A
        unknown_0x91b8c18a = RevolutionControl_UnknownStruct1.from_stream(data, game, property_size)

        return cls(
            command_enum,
            revolution_control_type,
            physical_control,
            unknown_0x6e14bc06,
            unknown_0xf0bf68a4,
            revolution_virtual_control,
            unknown_0xebaabf01,
            unknown_0xeda6d736,
            unknown_0xbf80d594,
            unknown_0x91b8c18a,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x00\x03")  # 3 properties
        num_properties_written = 3

        data.write(b"\xb0\xd1}M")  # 0xb0d17d4d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.command_enum.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x81\xcc=>")  # 0x81cc3d3e
        data.write(b"\x00\x04")  # size
        self.revolution_control_type.to_stream(data, game)

        data.write(b"\xe6F\xd3\xb7")  # 0xe646d3b7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.physical_control.to_stream(
            data, game, default_override={"physical_control": enums.PhysicalControlEnum.Unknown3}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.unknown_0x6e14bc06 != default_override.get(
            "unknown_0x6e14bc06", enums.PhysicalControlBooleanEnum.Unknown1
        ):
            num_properties_written += 1
            data.write(b"n\x14\xbc\x06")  # 0x6e14bc06
            data.write(b"\x00\x04")  # size
            self.unknown_0x6e14bc06.to_stream(data, game)

        if self.unknown_0xf0bf68a4 != default_override.get("unknown_0xf0bf68a4", RevolutionPhysicalControl()):
            num_properties_written += 1
            data.write(b"\xf0\xbfh\xa4")  # 0xf0bf68a4
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.unknown_0xf0bf68a4.to_stream(
                data, game, default_override={"physical_control": enums.PhysicalControlEnum.Unknown3}
            )
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.revolution_virtual_control != default_override.get(
            "revolution_virtual_control", enums.RevolutionVirtualControlEnum.Unknown1
        ):
            num_properties_written += 1
            data.write(b"\xfe\x81\x9d\xdb")  # 0xfe819ddb
            data.write(b"\x00\x04")  # size
            self.revolution_virtual_control.to_stream(data, game)

        if self.unknown_0xebaabf01 != default_override.get(
            "unknown_0xebaabf01", enums.PhysicalControlBooleanEnum.Unknown1
        ):
            num_properties_written += 1
            data.write(b"\xeb\xaa\xbf\x01")  # 0xebaabf01
            data.write(b"\x00\x04")  # size
            self.unknown_0xebaabf01.to_stream(data, game)

        if self.unknown_0xeda6d736 != default_override.get(
            "unknown_0xeda6d736", enums.RevolutionVirtualControlEnum.Unknown1
        ):
            num_properties_written += 1
            data.write(b"\xed\xa6\xd76")  # 0xeda6d736
            data.write(b"\x00\x04")  # size
            self.unknown_0xeda6d736.to_stream(data, game)

        if self.unknown_0xbf80d594 != default_override.get(
            "unknown_0xbf80d594", enums.RevolutionControl_UnknownEnum1Enum.Unknown1
        ):
            num_properties_written += 1
            data.write(b"\xbf\x80\xd5\x94")  # 0xbf80d594
            data.write(b"\x00\x04")  # size
            self.unknown_0xbf80d594.to_stream(data, game)

        if self.unknown_0x91b8c18a != default_override.get("unknown_0x91b8c18a", RevolutionControl_UnknownStruct1()):
            num_properties_written += 1
            data.write(b"\x91\xb8\xc1\x8a")  # 0x91b8c18a
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.unknown_0x91b8c18a.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if num_properties_written != 3:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack(">H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RevolutionControlJson", data)
        return cls(
            command_enum=ControlCommands.from_json(json_data["command_enum"]),
            revolution_control_type=enums.RevolutionControlTypeEnum.from_json(json_data["revolution_control_type"]),
            physical_control=RevolutionPhysicalControl.from_json(json_data["physical_control"]),
            unknown_0x6e14bc06=enums.PhysicalControlBooleanEnum.from_json(json_data["unknown_0x6e14bc06"]),
            unknown_0xf0bf68a4=RevolutionPhysicalControl.from_json(json_data["unknown_0xf0bf68a4"]),
            revolution_virtual_control=enums.RevolutionVirtualControlEnum.from_json(
                json_data["revolution_virtual_control"]
            ),
            unknown_0xebaabf01=enums.PhysicalControlBooleanEnum.from_json(json_data["unknown_0xebaabf01"]),
            unknown_0xeda6d736=enums.RevolutionVirtualControlEnum.from_json(json_data["unknown_0xeda6d736"]),
            unknown_0xbf80d594=enums.RevolutionControl_UnknownEnum1Enum.from_json(json_data["unknown_0xbf80d594"]),
            unknown_0x91b8c18a=RevolutionControl_UnknownStruct1.from_json(json_data["unknown_0x91b8c18a"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "command_enum": self.command_enum.to_json(),
            "revolution_control_type": self.revolution_control_type.to_json(),
            "physical_control": self.physical_control.to_json(),
            "unknown_0x6e14bc06": self.unknown_0x6e14bc06.to_json(),
            "unknown_0xf0bf68a4": self.unknown_0xf0bf68a4.to_json(),
            "revolution_virtual_control": self.revolution_virtual_control.to_json(),
            "unknown_0xebaabf01": self.unknown_0xebaabf01.to_json(),
            "unknown_0xeda6d736": self.unknown_0xeda6d736.to_json(),
            "unknown_0xbf80d594": self.unknown_0xbf80d594.to_json(),
            "unknown_0x91b8c18a": self.unknown_0x91b8c18a.to_json(),
        }


def _decode_command_enum(data: typing.BinaryIO, game: Game, property_size: int) -> ControlCommands:
    return ControlCommands.from_stream(data, game, property_size)


def _decode_revolution_control_type(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.RevolutionControlTypeEnum:
    return enums.RevolutionControlTypeEnum.from_stream(data, game)


def _decode_physical_control(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionPhysicalControl:
    return RevolutionPhysicalControl.from_stream(
        data, game, property_size, default_override={"physical_control": enums.PhysicalControlEnum.Unknown3}
    )


def _decode_unknown_0x6e14bc06(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.PhysicalControlBooleanEnum:
    return enums.PhysicalControlBooleanEnum.from_stream(data, game)


def _decode_unknown_0xf0bf68a4(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionPhysicalControl:
    return RevolutionPhysicalControl.from_stream(
        data, game, property_size, default_override={"physical_control": enums.PhysicalControlEnum.Unknown3}
    )


def _decode_revolution_virtual_control(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.RevolutionVirtualControlEnum:
    return enums.RevolutionVirtualControlEnum.from_stream(data, game)


def _decode_unknown_0xebaabf01(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.PhysicalControlBooleanEnum:
    return enums.PhysicalControlBooleanEnum.from_stream(data, game)


def _decode_unknown_0xeda6d736(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.RevolutionVirtualControlEnum:
    return enums.RevolutionVirtualControlEnum.from_stream(data, game)


def _decode_unknown_0xbf80d594(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.RevolutionControl_UnknownEnum1Enum:
    return enums.RevolutionControl_UnknownEnum1Enum.from_stream(data, game)


def _decode_unknown_0x91b8c18a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> RevolutionControl_UnknownStruct1:
    return RevolutionControl_UnknownStruct1.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB0D17D4D: ("command_enum", _decode_command_enum),
    0x81CC3D3E: ("revolution_control_type", _decode_revolution_control_type),
    0xE646D3B7: ("physical_control", _decode_physical_control),
    0x6E14BC06: ("unknown_0x6e14bc06", _decode_unknown_0x6e14bc06),
    0xF0BF68A4: ("unknown_0xf0bf68a4", _decode_unknown_0xf0bf68a4),
    0xFE819DDB: ("revolution_virtual_control", _decode_revolution_virtual_control),
    0xEBAABF01: ("unknown_0xebaabf01", _decode_unknown_0xebaabf01),
    0xEDA6D736: ("unknown_0xeda6d736", _decode_unknown_0xeda6d736),
    0xBF80D594: ("unknown_0xbf80d594", _decode_unknown_0xbf80d594),
    0x91B8C18A: ("unknown_0x91b8c18a", _decode_unknown_0x91b8c18a),
}
