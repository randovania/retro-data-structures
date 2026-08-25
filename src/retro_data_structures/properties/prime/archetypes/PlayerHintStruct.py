# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PlayerHintStructJson(typing_extensions.TypedDict):
        unknown_1: bool
        unknown_2: bool
        unknown_3: bool
        unknown_4: bool
        unknown_5: bool
        disable_unmorph: bool
        disable_morph: bool
        disable_controls: bool
        disable_boost: bool
        activate_combat_visor: bool
        activate_scan_visor: bool
        activate_thermal_visor: bool
        activate_x_ray_visor: bool
        unknown_6: bool
        face_object_on_unmorph: bool


@dataclasses.dataclass()
class PlayerHintStruct(BaseProperty):
    unknown_1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="Unknown 1"),
        },
    )
    unknown_2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="Unknown 2"),
        },
    )
    unknown_3: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="Unknown 3"),
        },
    )
    unknown_4: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Unknown 4"),
        },
    )
    unknown_5: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Unknown 5"),
        },
    )
    disable_unmorph: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000005, original_name="Disable Unmorph"),
        },
    )
    disable_morph: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="Disable Morph"),
        },
    )
    disable_controls: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="Disable Controls"),
        },
    )
    disable_boost: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="Disable Boost"),
        },
    )
    activate_combat_visor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000009, original_name="Activate Combat Visor"),
        },
    )
    activate_scan_visor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="Activate Scan Visor"),
        },
    )
    activate_thermal_visor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="Activate Thermal Visor"),
        },
    )
    activate_x_ray_visor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000C, original_name="Activate X-Ray Visor"),
        },
    )
    unknown_6: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="Unknown 6"),
        },
    )
    face_object_on_unmorph: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="Face Object On Unmorph"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unknown_1 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_2 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_3 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_4 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_5 = structs.BIG_bool_.unpack(data.read(1))[0]
        disable_unmorph = structs.BIG_bool_.unpack(data.read(1))[0]
        disable_morph = structs.BIG_bool_.unpack(data.read(1))[0]
        disable_controls = structs.BIG_bool_.unpack(data.read(1))[0]
        disable_boost = structs.BIG_bool_.unpack(data.read(1))[0]
        activate_combat_visor = structs.BIG_bool_.unpack(data.read(1))[0]
        activate_scan_visor = structs.BIG_bool_.unpack(data.read(1))[0]
        activate_thermal_visor = structs.BIG_bool_.unpack(data.read(1))[0]
        activate_x_ray_visor = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_6 = structs.BIG_bool_.unpack(data.read(1))[0]
        face_object_on_unmorph = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            unknown_1,
            unknown_2,
            unknown_3,
            unknown_4,
            unknown_5,
            disable_unmorph,
            disable_morph,
            disable_controls,
            disable_boost,
            activate_combat_visor,
            activate_scan_visor,
            activate_thermal_visor,
            activate_x_ray_visor,
            unknown_6,
            face_object_on_unmorph,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_bool_.pack(self.unknown_1))
        data.write(structs.BIG_bool_.pack(self.unknown_2))
        data.write(structs.BIG_bool_.pack(self.unknown_3))
        data.write(structs.BIG_bool_.pack(self.unknown_4))
        data.write(structs.BIG_bool_.pack(self.unknown_5))
        data.write(structs.BIG_bool_.pack(self.disable_unmorph))
        data.write(structs.BIG_bool_.pack(self.disable_morph))
        data.write(structs.BIG_bool_.pack(self.disable_controls))
        data.write(structs.BIG_bool_.pack(self.disable_boost))
        data.write(structs.BIG_bool_.pack(self.activate_combat_visor))
        data.write(structs.BIG_bool_.pack(self.activate_scan_visor))
        data.write(structs.BIG_bool_.pack(self.activate_thermal_visor))
        data.write(structs.BIG_bool_.pack(self.activate_x_ray_visor))
        data.write(structs.BIG_bool_.pack(self.unknown_6))
        data.write(structs.BIG_bool_.pack(self.face_object_on_unmorph))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerHintStructJson", data)
        return cls(
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            disable_unmorph=json_data["disable_unmorph"],
            disable_morph=json_data["disable_morph"],
            disable_controls=json_data["disable_controls"],
            disable_boost=json_data["disable_boost"],
            activate_combat_visor=json_data["activate_combat_visor"],
            activate_scan_visor=json_data["activate_scan_visor"],
            activate_thermal_visor=json_data["activate_thermal_visor"],
            activate_x_ray_visor=json_data["activate_x_ray_visor"],
            unknown_6=json_data["unknown_6"],
            face_object_on_unmorph=json_data["face_object_on_unmorph"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "disable_unmorph": self.disable_unmorph,
            "disable_morph": self.disable_morph,
            "disable_controls": self.disable_controls,
            "disable_boost": self.disable_boost,
            "activate_combat_visor": self.activate_combat_visor,
            "activate_scan_visor": self.activate_scan_visor,
            "activate_thermal_visor": self.activate_thermal_visor,
            "activate_x_ray_visor": self.activate_x_ray_visor,
            "unknown_6": self.unknown_6,
            "face_object_on_unmorph": self.face_object_on_unmorph,
        }
