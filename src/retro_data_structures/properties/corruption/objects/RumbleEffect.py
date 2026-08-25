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
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class RumbleEffectJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        radius: float
        effect: int
        flags_rumble: int
        unknown: json_util.JsonObject


@dataclasses.dataclass()
class RumbleEffect(BaseObjectType):
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
    radius: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78C507EB, original_name="Radius"),
        },
    )
    effect: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x68ACBD86, original_name="Effect"),
        },
    )  # Choice
    flags_rumble: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x4F7FEC39, original_name="FlagsRumble"),
        },
    )  # Flagset
    unknown: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x05A451ED, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "RUMB"

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
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78C507EB
        radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68ACBD86
        effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F7FEC39
        flags_rumble = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05A451ED
        unknown = Spline.from_stream(data, game, property_size)

        return cls(editor_properties, radius, effect, flags_rumble, unknown)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x04")  # 4 properties
        num_properties_written = 4

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"x\xc5\x07\xeb")  # 0x78c507eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.radius))

        data.write(b"h\xac\xbd\x86")  # 0x68acbd86
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.effect))

        data.write(b"O\x7f\xec9")  # 0x4f7fec39
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_rumble))

        if self.unknown != default_override.get("unknown", Spline()):
            num_properties_written += 1
            data.write(b"\x05\xa4Q\xed")  # 0x5a451ed
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.unknown.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RumbleEffectJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            radius=json_data["radius"],
            effect=json_data["effect"],
            flags_rumble=json_data["flags_rumble"],
            unknown=Spline.from_json(json_data["unknown"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "radius": self.radius,
            "effect": self.effect,
            "flags_rumble": self.flags_rumble,
            "unknown": self.unknown.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_unknown(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x78C507EB: ("radius", structs.decode_BIG_f),
    0x68ACBD86: ("effect", structs.decode_BIG_L),
    0x4F7FEC39: ("flags_rumble", structs.decode_BIG_L),
    0x05A451ED: ("unknown", _decode_unknown),
}
