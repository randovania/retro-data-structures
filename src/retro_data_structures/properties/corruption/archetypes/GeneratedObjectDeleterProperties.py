# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GeneratedObjectDeleterPropertiesJson(typing_extensions.TypedDict):
        delete_all_on_attached_object_deletion: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = 0xC6164AFF


@dataclasses.dataclass()
class GeneratedObjectDeleterProperties(BaseProperty):
    delete_all_on_attached_object_deletion: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC6164AFF, original_name="DeleteAllOnAttachedObjectDeletion"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?")

        dec = _FAST_FORMAT.unpack(data.read(7))
        assert (dec[0]) == _FAST_IDS
        return cls(
            dec[2],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b"\xc6\x16J\xff")  # 0xc6164aff
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.delete_all_on_attached_object_deletion))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GeneratedObjectDeleterPropertiesJson", data)
        return cls(
            delete_all_on_attached_object_deletion=json_data["delete_all_on_attached_object_deletion"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "delete_all_on_attached_object_deletion": self.delete_all_on_attached_object_deletion,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC6164AFF: ("delete_all_on_attached_object_deletion", structs.decode_BIG_bool_),
}
