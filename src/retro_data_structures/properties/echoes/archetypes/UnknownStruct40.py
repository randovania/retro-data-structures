# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct40Json(typing_extensions.TypedDict):
        unknown_0xbed8a4ba: float
        unknown_0xc2b98161: float
        unknown_0x5fb66017: float
        unknown_0xbab42316: float
        part_0x8f06342a: int
        sound_0xd8b11129: int
        sound_0xe99e5316: int
        damage_info: json_util.JsonObject
        part_0x686489fd: int


@dataclasses.dataclass()
class UnknownStruct40(BaseProperty):
    unknown_0xbed8a4ba: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBED8A4BA, original_name="Unknown"),
        },
    )
    unknown_0xc2b98161: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC2B98161, original_name="Unknown"),
        },
    )
    unknown_0x5fb66017: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5FB66017, original_name="Unknown"),
        },
    )
    unknown_0xbab42316: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBAB42316, original_name="Unknown"),
        },
    )
    part_0x8f06342a: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8F06342A, original_name="PART"),
        },
    )
    sound_0xd8b11129: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xD8B11129, original_name="Sound"),
        },
    )
    sound_0xe99e5316: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE99E5316, original_name="Sound"),
        },
    )
    damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x1440D152,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    part_0x686489fd: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x686489FD, original_name="PART"),
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
        if property_count != 9:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBED8A4BA
        unknown_0xbed8a4ba = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2B98161
        unknown_0xc2b98161 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5FB66017
        unknown_0x5fb66017 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBAB42316
        unknown_0xbab42316 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F06342A
        part_0x8f06342a = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8B11129
        sound_0xd8b11129 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE99E5316
        sound_0xe99e5316 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1440D152
        damage_info = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_radius": 13.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x686489FD
        part_0x686489fd = structs.BIG_L.unpack(data.read(4))[0]

        return cls(
            unknown_0xbed8a4ba,
            unknown_0xc2b98161,
            unknown_0x5fb66017,
            unknown_0xbab42316,
            part_0x8f06342a,
            sound_0xd8b11129,
            sound_0xe99e5316,
            damage_info,
            part_0x686489fd,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"\xbe\xd8\xa4\xba")  # 0xbed8a4ba
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbed8a4ba))

        data.write(b"\xc2\xb9\x81a")  # 0xc2b98161
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc2b98161))

        data.write(b"_\xb6`\x17")  # 0x5fb66017
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5fb66017))

        data.write(b"\xba\xb4#\x16")  # 0xbab42316
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbab42316))

        data.write(b"\x8f\x064*")  # 0x8f06342a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x8f06342a))

        data.write(b"\xd8\xb1\x11)")  # 0xd8b11129
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0xd8b11129))

        data.write(b"\xe9\x9eS\x16")  # 0xe99e5316
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0xe99e5316))

        data.write(b"\x14@\xd1R")  # 0x1440d152
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info.to_stream(
            data,
            game,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_radius": 13.0, "di_knock_back_power": 10.0},
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"hd\x89\xfd")  # 0x686489fd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x686489fd))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct40Json", data)
        return cls(
            unknown_0xbed8a4ba=json_data["unknown_0xbed8a4ba"],
            unknown_0xc2b98161=json_data["unknown_0xc2b98161"],
            unknown_0x5fb66017=json_data["unknown_0x5fb66017"],
            unknown_0xbab42316=json_data["unknown_0xbab42316"],
            part_0x8f06342a=json_data["part_0x8f06342a"],
            sound_0xd8b11129=json_data["sound_0xd8b11129"],
            sound_0xe99e5316=json_data["sound_0xe99e5316"],
            damage_info=DamageInfo.from_json(json_data["damage_info"]),
            part_0x686489fd=json_data["part_0x686489fd"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xbed8a4ba": self.unknown_0xbed8a4ba,
            "unknown_0xc2b98161": self.unknown_0xc2b98161,
            "unknown_0x5fb66017": self.unknown_0x5fb66017,
            "unknown_0xbab42316": self.unknown_0xbab42316,
            "part_0x8f06342a": self.part_0x8f06342a,
            "sound_0xd8b11129": self.sound_0xd8b11129,
            "sound_0xe99e5316": self.sound_0xe99e5316,
            "damage_info": self.damage_info.to_json(),
            "part_0x686489fd": self.part_0x686489fd,
        }

    def _dependencies_for_part_0x8f06342a(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x8f06342a)

    def _dependencies_for_sound_0xd8b11129(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0xd8b11129)

    def _dependencies_for_sound_0xe99e5316(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0xe99e5316)

    def _dependencies_for_part_0x686489fd(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x686489fd)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_part_0x8f06342a, "part_0x8f06342a", "AssetId"),
            (self._dependencies_for_sound_0xd8b11129, "sound_0xd8b11129", "int"),
            (self._dependencies_for_sound_0xe99e5316, "sound_0xe99e5316", "int"),
            (self._dependencies_for_part_0x686489fd, "part_0x686489fd", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct40.{field_name} ({field_type}): {e}")


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_radius": 13.0, "di_knock_back_power": 10.0},
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xBED8A4BA: ("unknown_0xbed8a4ba", structs.decode_BIG_f),
    0xC2B98161: ("unknown_0xc2b98161", structs.decode_BIG_f),
    0x5FB66017: ("unknown_0x5fb66017", structs.decode_BIG_f),
    0xBAB42316: ("unknown_0xbab42316", structs.decode_BIG_f),
    0x8F06342A: ("part_0x8f06342a", structs.decode_BIG_L),
    0xD8B11129: ("sound_0xd8b11129", structs.decode_BIG_l),
    0xE99E5316: ("sound_0xe99e5316", structs.decode_BIG_l),
    0x1440D152: ("damage_info", _decode_damage_info),
    0x686489FD: ("part_0x686489fd", structs.decode_BIG_L),
}
