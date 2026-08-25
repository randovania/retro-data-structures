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

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TeamAIJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        max_team_size: int
        max_melee_attackers: int
        max_ranged_attackers: int
        unknown_0x9fa9c457: int
        unknown_0x54cd2755: int
        unknown_0xc36ed15c: int
        team_formation: int
        unknown_0xd3ad55b6: float
        unknown_0x8d00b839: float


@dataclasses.dataclass()
class TeamAI(BaseObjectType):
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
    max_team_size: int = dataclasses.field(
        default=20,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBF37E518, original_name="MaxTeamSize"),
        },
    )
    max_melee_attackers: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCEBEE4AB, original_name="MaxMeleeAttackers"),
        },
    )
    max_ranged_attackers: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7555C1EA, original_name="MaxRangedAttackers"),
        },
    )
    unknown_0x9fa9c457: int = dataclasses.field(
        default=30,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9FA9C457, original_name="Unknown"),
        },
    )
    unknown_0x54cd2755: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x54CD2755, original_name="Unknown"),
        },
    )
    unknown_0xc36ed15c: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC36ED15C, original_name="Unknown"),
        },
    )
    team_formation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x37A20376, original_name="TeamFormation"),
        },
    )
    unknown_0xd3ad55b6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD3AD55B6, original_name="Unknown"),
        },
    )
    unknown_0x8d00b839: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D00B839, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "TMAI"

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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF37E518
        max_team_size = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCEBEE4AB
        max_melee_attackers = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7555C1EA
        max_ranged_attackers = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9FA9C457
        unknown_0x9fa9c457 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54CD2755
        unknown_0x54cd2755 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC36ED15C
        unknown_0xc36ed15c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37A20376
        team_formation = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3AD55B6
        unknown_0xd3ad55b6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D00B839
        unknown_0x8d00b839 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            max_team_size,
            max_melee_attackers,
            max_ranged_attackers,
            unknown_0x9fa9c457,
            unknown_0x54cd2755,
            unknown_0xc36ed15c,
            team_formation,
            unknown_0xd3ad55b6,
            unknown_0x8d00b839,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\n")  # 10 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbf7\xe5\x18")  # 0xbf37e518
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_team_size))

        data.write(b"\xce\xbe\xe4\xab")  # 0xcebee4ab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_melee_attackers))

        data.write(b"uU\xc1\xea")  # 0x7555c1ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_ranged_attackers))

        data.write(b"\x9f\xa9\xc4W")  # 0x9fa9c457
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9fa9c457))

        data.write(b"T\xcd'U")  # 0x54cd2755
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x54cd2755))

        data.write(b"\xc3n\xd1\\")  # 0xc36ed15c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc36ed15c))

        data.write(b"7\xa2\x03v")  # 0x37a20376
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.team_formation))

        data.write(b"\xd3\xadU\xb6")  # 0xd3ad55b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd3ad55b6))

        data.write(b"\x8d\x00\xb89")  # 0x8d00b839
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8d00b839))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TeamAIJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            max_team_size=json_data["max_team_size"],
            max_melee_attackers=json_data["max_melee_attackers"],
            max_ranged_attackers=json_data["max_ranged_attackers"],
            unknown_0x9fa9c457=json_data["unknown_0x9fa9c457"],
            unknown_0x54cd2755=json_data["unknown_0x54cd2755"],
            unknown_0xc36ed15c=json_data["unknown_0xc36ed15c"],
            team_formation=json_data["team_formation"],
            unknown_0xd3ad55b6=json_data["unknown_0xd3ad55b6"],
            unknown_0x8d00b839=json_data["unknown_0x8d00b839"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "max_team_size": self.max_team_size,
            "max_melee_attackers": self.max_melee_attackers,
            "max_ranged_attackers": self.max_ranged_attackers,
            "unknown_0x9fa9c457": self.unknown_0x9fa9c457,
            "unknown_0x54cd2755": self.unknown_0x54cd2755,
            "unknown_0xc36ed15c": self.unknown_0xc36ed15c,
            "team_formation": self.team_formation,
            "unknown_0xd3ad55b6": self.unknown_0xd3ad55b6,
            "unknown_0x8d00b839": self.unknown_0x8d00b839,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xBF37E518: ("max_team_size", structs.decode_BIG_l),
    0xCEBEE4AB: ("max_melee_attackers", structs.decode_BIG_l),
    0x7555C1EA: ("max_ranged_attackers", structs.decode_BIG_l),
    0x9FA9C457: ("unknown_0x9fa9c457", structs.decode_BIG_l),
    0x54CD2755: ("unknown_0x54cd2755", structs.decode_BIG_l),
    0xC36ED15C: ("unknown_0xc36ed15c", structs.decode_BIG_l),
    0x37A20376: ("team_formation", structs.decode_BIG_l),
    0xD3AD55B6: ("unknown_0xd3ad55b6", structs.decode_BIG_f),
    0x8D00B839: ("unknown_0x8d00b839", structs.decode_BIG_f),
}
