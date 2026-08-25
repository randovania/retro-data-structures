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

    class GrappleInfoJson(typing_extensions.TypedDict):
        skeleton_landing: float
        unknown_0x7a5e41e1: float
        unknown_0x76104d9e: float
        visible_through_geometry: bool
        unknown_0x11b6a17a: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x2BA7FABC, 0x7A5E41E1, 0x76104D9E, 0xBAA8A527, 0x11B6A17A)


@dataclasses.dataclass()
class GrappleInfo(BaseProperty):
    skeleton_landing: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2BA7FABC, original_name="SkeletonLanding"),
        },
    )
    unknown_0x7a5e41e1: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7A5E41E1, original_name="Unknown"),
        },
    )
    unknown_0x76104d9e: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76104D9E, original_name="Unknown"),
        },
    )
    visible_through_geometry: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBAA8A527, original_name="VisibleThroughGeometry"),
        },
    )
    unknown_0x11b6a17a: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x11B6A17A, original_name="Unknown"),
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
        if property_count != 5:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLH?LH?")

        dec = _FAST_FORMAT.unpack(data.read(44))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"+\xa7\xfa\xbc")  # 0x2ba7fabc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.skeleton_landing))

        data.write(b"z^A\xe1")  # 0x7a5e41e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7a5e41e1))

        data.write(b"v\x10M\x9e")  # 0x76104d9e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76104d9e))

        data.write(b"\xba\xa8\xa5'")  # 0xbaa8a527
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.visible_through_geometry))

        data.write(b"\x11\xb6\xa1z")  # 0x11b6a17a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x11b6a17a))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GrappleInfoJson", data)
        return cls(
            skeleton_landing=json_data["skeleton_landing"],
            unknown_0x7a5e41e1=json_data["unknown_0x7a5e41e1"],
            unknown_0x76104d9e=json_data["unknown_0x76104d9e"],
            visible_through_geometry=json_data["visible_through_geometry"],
            unknown_0x11b6a17a=json_data["unknown_0x11b6a17a"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "skeleton_landing": self.skeleton_landing,
            "unknown_0x7a5e41e1": self.unknown_0x7a5e41e1,
            "unknown_0x76104d9e": self.unknown_0x76104d9e,
            "visible_through_geometry": self.visible_through_geometry,
            "unknown_0x11b6a17a": self.unknown_0x11b6a17a,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2BA7FABC: ("skeleton_landing", structs.decode_BIG_f),
    0x7A5E41E1: ("unknown_0x7a5e41e1", structs.decode_BIG_f),
    0x76104D9E: ("unknown_0x76104d9e", structs.decode_BIG_f),
    0xBAA8A527: ("visible_through_geometry", structs.decode_BIG_bool_),
    0x11B6A17A: ("unknown_0x11b6a17a", structs.decode_BIG_bool_),
}
