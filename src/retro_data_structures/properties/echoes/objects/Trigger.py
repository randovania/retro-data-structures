# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.TriggerInfo import TriggerInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TriggerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        trigger: json_util.JsonObject
        deactivate_on_enter: bool
        deactivate_on_exit: bool


@dataclasses.dataclass()
class Trigger(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    trigger: TriggerInfo = dataclasses.field(
        default_factory=TriggerInfo,
        metadata={
            "reflection": FieldReflection[TriggerInfo](
                TriggerInfo,
                id=0x77A27411,
                original_name="Trigger",
                from_json=TriggerInfo.from_json,
                to_json=TriggerInfo.to_json,
            ),
        },
    )
    deactivate_on_enter: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8D33465F, original_name="DeactivateOnEnter"),
        },
    )
    deactivate_on_exit: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1C453986, original_name="DeactivateOnExit"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "TRGR"

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 4:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77A27411
        trigger = TriggerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D33465F
        deactivate_on_enter = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C453986
        deactivate_on_exit = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(editor_properties, trigger, deactivate_on_enter, deactivate_on_exit)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w\xa2t\x11")  # 0x77a27411
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.trigger.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8d3F_")  # 0x8d33465f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.deactivate_on_enter))

        data.write(b"\x1cE9\x86")  # 0x1c453986
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.deactivate_on_exit))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TriggerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            trigger=TriggerInfo.from_json(json_data["trigger"]),
            deactivate_on_enter=json_data["deactivate_on_enter"],
            deactivate_on_exit=json_data["deactivate_on_exit"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "trigger": self.trigger.to_json(),
            "deactivate_on_enter": self.deactivate_on_enter,
            "deactivate_on_exit": self.deactivate_on_exit,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_trigger(data: typing.BinaryIO, game: Game, property_size: int) -> TriggerInfo:
    return TriggerInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x77A27411: ("trigger", _decode_trigger),
    0x8D33465F: ("deactivate_on_enter", structs.decode_BIG_bool_),
    0x1C453986: ("deactivate_on_exit", structs.decode_BIG_bool_),
}
