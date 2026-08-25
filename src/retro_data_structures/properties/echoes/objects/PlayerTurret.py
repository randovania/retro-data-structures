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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PlayerTurretJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flags_player_turret: int
        unknown_0x17cd8b2a: float
        unknown_0x1473dad2: float
        unknown_0x3650ce75: float
        unknown_0x78520e6e: float
        damage_angle: float
        horiz_speed: float
        vert_speed: float
        fire_rate: float
        weapon_damage: json_util.JsonObject
        weapon_effect: int
        wpsc: int
        unknown_0xe7234f72: int
        unknown_0x3e2f7afb: int
        unknown_0x7cabd1f1: int
        unknown_0x7ef976eb: int
        unknown_0x035459fd: int


@dataclasses.dataclass()
class PlayerTurret(BaseObjectType):
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
    flags_player_turret: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEEADEFA6, original_name="FlagsPlayerTurret"),
        },
    )
    unknown_0x17cd8b2a: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x17CD8B2A, original_name="Unknown"),
        },
    )
    unknown_0x1473dad2: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1473DAD2, original_name="Unknown"),
        },
    )
    unknown_0x3650ce75: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3650CE75, original_name="Unknown"),
        },
    )
    unknown_0x78520e6e: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78520E6E, original_name="Unknown"),
        },
    )
    damage_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA39A5D72, original_name="DamageAngle"),
        },
    )
    horiz_speed: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB2E32DB, original_name="HorizSpeed"),
        },
    )
    vert_speed: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B3C8683, original_name="VertSpeed"),
        },
    )
    fire_rate: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6E48F18, original_name="FireRate"),
        },
    )
    weapon_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8E5F7E96,
                original_name="WeaponDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    weapon_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC43360A7, original_name="WeaponEffect"),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA99D3DBE, original_name="WPSC"),
        },
    )
    unknown_0xe7234f72: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE7234F72, original_name="Unknown"),
        },
    )
    unknown_0x3e2f7afb: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x3E2F7AFB, original_name="Unknown"),
        },
    )
    unknown_0x7cabd1f1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x7CABD1F1, original_name="Unknown"),
        },
    )
    unknown_0x7ef976eb: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x7EF976EB, original_name="Unknown"),
        },
    )
    unknown_0x035459fd: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x035459FD, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PLRT"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ScriptPlayerTurret.rel"]

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
        if property_count != 18:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEEADEFA6
        flags_player_turret = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17CD8B2A
        unknown_0x17cd8b2a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1473DAD2
        unknown_0x1473dad2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3650CE75
        unknown_0x3650ce75 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78520E6E
        unknown_0x78520e6e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA39A5D72
        damage_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB2E32DB
        horiz_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B3C8683
        vert_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6E48F18
        fire_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E5F7E96
        weapon_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC43360A7
        weapon_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA99D3DBE
        wpsc = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7234F72
        unknown_0xe7234f72 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3E2F7AFB
        unknown_0x3e2f7afb = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CABD1F1
        unknown_0x7cabd1f1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7EF976EB
        unknown_0x7ef976eb = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x035459FD
        unknown_0x035459fd = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            flags_player_turret,
            unknown_0x17cd8b2a,
            unknown_0x1473dad2,
            unknown_0x3650ce75,
            unknown_0x78520e6e,
            damage_angle,
            horiz_speed,
            vert_speed,
            fire_rate,
            weapon_damage,
            weapon_effect,
            wpsc,
            unknown_0xe7234f72,
            unknown_0x3e2f7afb,
            unknown_0x7cabd1f1,
            unknown_0x7ef976eb,
            unknown_0x035459fd,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x12")  # 18 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xee\xad\xef\xa6")  # 0xeeadefa6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.flags_player_turret))

        data.write(b"\x17\xcd\x8b*")  # 0x17cd8b2a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x17cd8b2a))

        data.write(b"\x14s\xda\xd2")  # 0x1473dad2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1473dad2))

        data.write(b"6P\xceu")  # 0x3650ce75
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3650ce75))

        data.write(b"xR\x0en")  # 0x78520e6e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x78520e6e))

        data.write(b"\xa3\x9a]r")  # 0xa39a5d72
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damage_angle))

        data.write(b"\xfb.2\xdb")  # 0xfb2e32db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.horiz_speed))

        data.write(b"\x1b<\x86\x83")  # 0x1b3c8683
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.vert_speed))

        data.write(b"\xc6\xe4\x8f\x18")  # 0xc6e48f18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fire_rate))

        data.write(b"\x8e_~\x96")  # 0x8e5f7e96
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapon_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc43`\xa7")  # 0xc43360a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.weapon_effect))

        data.write(b"\xa9\x9d=\xbe")  # 0xa99d3dbe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.wpsc))

        data.write(b"\xe7#Or")  # 0xe7234f72
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe7234f72))

        data.write(b">/z\xfb")  # 0x3e2f7afb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x3e2f7afb))

        data.write(b"|\xab\xd1\xf1")  # 0x7cabd1f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7cabd1f1))

        data.write(b"~\xf9v\xeb")  # 0x7ef976eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7ef976eb))

        data.write(b"\x03TY\xfd")  # 0x35459fd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x035459fd))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerTurretJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            flags_player_turret=json_data["flags_player_turret"],
            unknown_0x17cd8b2a=json_data["unknown_0x17cd8b2a"],
            unknown_0x1473dad2=json_data["unknown_0x1473dad2"],
            unknown_0x3650ce75=json_data["unknown_0x3650ce75"],
            unknown_0x78520e6e=json_data["unknown_0x78520e6e"],
            damage_angle=json_data["damage_angle"],
            horiz_speed=json_data["horiz_speed"],
            vert_speed=json_data["vert_speed"],
            fire_rate=json_data["fire_rate"],
            weapon_damage=DamageInfo.from_json(json_data["weapon_damage"]),
            weapon_effect=json_data["weapon_effect"],
            wpsc=json_data["wpsc"],
            unknown_0xe7234f72=json_data["unknown_0xe7234f72"],
            unknown_0x3e2f7afb=json_data["unknown_0x3e2f7afb"],
            unknown_0x7cabd1f1=json_data["unknown_0x7cabd1f1"],
            unknown_0x7ef976eb=json_data["unknown_0x7ef976eb"],
            unknown_0x035459fd=json_data["unknown_0x035459fd"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "flags_player_turret": self.flags_player_turret,
            "unknown_0x17cd8b2a": self.unknown_0x17cd8b2a,
            "unknown_0x1473dad2": self.unknown_0x1473dad2,
            "unknown_0x3650ce75": self.unknown_0x3650ce75,
            "unknown_0x78520e6e": self.unknown_0x78520e6e,
            "damage_angle": self.damage_angle,
            "horiz_speed": self.horiz_speed,
            "vert_speed": self.vert_speed,
            "fire_rate": self.fire_rate,
            "weapon_damage": self.weapon_damage.to_json(),
            "weapon_effect": self.weapon_effect,
            "wpsc": self.wpsc,
            "unknown_0xe7234f72": self.unknown_0xe7234f72,
            "unknown_0x3e2f7afb": self.unknown_0x3e2f7afb,
            "unknown_0x7cabd1f1": self.unknown_0x7cabd1f1,
            "unknown_0x7ef976eb": self.unknown_0x7ef976eb,
            "unknown_0x035459fd": self.unknown_0x035459fd,
        }

    def _dependencies_for_weapon_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon_effect)

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def _dependencies_for_unknown_0xe7234f72(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_0xe7234f72)

    def _dependencies_for_unknown_0x3e2f7afb(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_0x3e2f7afb)

    def _dependencies_for_unknown_0x7cabd1f1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_0x7cabd1f1)

    def _dependencies_for_unknown_0x7ef976eb(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_0x7ef976eb)

    def _dependencies_for_unknown_0x035459fd(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_0x035459fd)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_weapon_effect, "weapon_effect", "AssetId"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self._dependencies_for_unknown_0xe7234f72, "unknown_0xe7234f72", "int"),
            (self._dependencies_for_unknown_0x3e2f7afb, "unknown_0x3e2f7afb", "int"),
            (self._dependencies_for_unknown_0x7cabd1f1, "unknown_0x7cabd1f1", "int"),
            (self._dependencies_for_unknown_0x7ef976eb, "unknown_0x7ef976eb", "int"),
            (self._dependencies_for_unknown_0x035459fd, "unknown_0x035459fd", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PlayerTurret.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_weapon_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xEEADEFA6: ("flags_player_turret", structs.decode_BIG_l),
    0x17CD8B2A: ("unknown_0x17cd8b2a", structs.decode_BIG_f),
    0x1473DAD2: ("unknown_0x1473dad2", structs.decode_BIG_f),
    0x3650CE75: ("unknown_0x3650ce75", structs.decode_BIG_f),
    0x78520E6E: ("unknown_0x78520e6e", structs.decode_BIG_f),
    0xA39A5D72: ("damage_angle", structs.decode_BIG_f),
    0xFB2E32DB: ("horiz_speed", structs.decode_BIG_f),
    0x1B3C8683: ("vert_speed", structs.decode_BIG_f),
    0xC6E48F18: ("fire_rate", structs.decode_BIG_f),
    0x8E5F7E96: ("weapon_damage", _decode_weapon_damage),
    0xC43360A7: ("weapon_effect", structs.decode_BIG_L),
    0xA99D3DBE: ("wpsc", structs.decode_BIG_L),
    0xE7234F72: ("unknown_0xe7234f72", structs.decode_BIG_l),
    0x3E2F7AFB: ("unknown_0x3e2f7afb", structs.decode_BIG_l),
    0x7CABD1F1: ("unknown_0x7cabd1f1", structs.decode_BIG_l),
    0x7EF976EB: ("unknown_0x7ef976eb", structs.decode_BIG_l),
    0x035459FD: ("unknown_0x035459fd", structs.decode_BIG_l),
}
