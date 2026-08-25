# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.VisorParameters import VisorParameters
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class DamageableTriggerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        orbitable: bool
        enable_seeker_lock_on: bool
        invulnerable: bool
        show_on_radar: bool
        visor: json_util.JsonObject
        damage_originator: int
        only_take_damage_from_inhabitants: bool
        is_hostile: bool


@dataclasses.dataclass()
class DamageableTrigger(BaseObjectType):
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
    health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xCF90D15E,
                original_name="Health",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x7B71AE90,
                original_name="Vulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    orbitable: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x704B5369, original_name="Orbitable"),
        },
    )
    enable_seeker_lock_on: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5DFD7820, original_name="Enable Seeker Lock-On"),
        },
    )
    invulnerable: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6652BDD7, original_name="Invulnerable"),
        },
    )
    show_on_radar: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF0E07A4B, original_name="ShowOnRadar"),
        },
    )
    visor: VisorParameters = dataclasses.field(
        default_factory=VisorParameters,
        metadata={
            "reflection": FieldReflection[VisorParameters](
                VisorParameters,
                id=0x05AD250E,
                original_name="Visor",
                from_json=VisorParameters.from_json,
                to_json=VisorParameters.to_json,
            ),
        },
    )
    damage_originator: enums.DamageableTriggerEnumEnum = dataclasses.field(
        default=enums.DamageableTriggerEnumEnum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.DamageableTriggerEnumEnum](
                enums.DamageableTriggerEnumEnum,
                id=0x8B9D2123,
                original_name="DamageOriginator",
                from_json=enums.DamageableTriggerEnumEnum.from_json,
                to_json=enums.DamageableTriggerEnumEnum.to_json,
            ),
        },
    )
    only_take_damage_from_inhabitants: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCE2CF510, original_name="OnlyTakeDamageFromInhabitants"),
        },
    )
    is_hostile: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x701B61B3, original_name="IsHostile"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DTRG"

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
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x704B5369
        orbitable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5DFD7820
        enable_seeker_lock_on = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6652BDD7
        invulnerable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0E07A4B
        show_on_radar = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05AD250E
        visor = VisorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B9D2123
        damage_originator = enums.DamageableTriggerEnumEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE2CF510
        only_take_damage_from_inhabitants = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x701B61B3
        is_hostile = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            health,
            vulnerability,
            orbitable,
            enable_seeker_lock_on,
            invulnerable,
            show_on_radar,
            visor,
            damage_originator,
            only_take_damage_from_inhabitants,
            is_hostile,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{q\xae\x90")  # 0x7b71ae90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"pKSi")  # 0x704b5369
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.orbitable))

        data.write(b"]\xfdx ")  # 0x5dfd7820
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.enable_seeker_lock_on))

        data.write(b"fR\xbd\xd7")  # 0x6652bdd7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.invulnerable))

        data.write(b"\xf0\xe0zK")  # 0xf0e07a4b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.show_on_radar))

        data.write(b"\x05\xad%\x0e")  # 0x5ad250e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8b\x9d!#")  # 0x8b9d2123
        data.write(b"\x00\x04")  # size
        self.damage_originator.to_stream(data, game)

        data.write(b"\xce,\xf5\x10")  # 0xce2cf510
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.only_take_damage_from_inhabitants))

        data.write(b"p\x1ba\xb3")  # 0x701b61b3
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_hostile))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DamageableTriggerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            orbitable=json_data["orbitable"],
            enable_seeker_lock_on=json_data["enable_seeker_lock_on"],
            invulnerable=json_data["invulnerable"],
            show_on_radar=json_data["show_on_radar"],
            visor=VisorParameters.from_json(json_data["visor"]),
            damage_originator=enums.DamageableTriggerEnumEnum.from_json(json_data["damage_originator"]),
            only_take_damage_from_inhabitants=json_data["only_take_damage_from_inhabitants"],
            is_hostile=json_data["is_hostile"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "orbitable": self.orbitable,
            "enable_seeker_lock_on": self.enable_seeker_lock_on,
            "invulnerable": self.invulnerable,
            "show_on_radar": self.show_on_radar,
            "visor": self.visor.to_json(),
            "damage_originator": self.damage_originator.to_json(),
            "only_take_damage_from_inhabitants": self.only_take_damage_from_inhabitants,
            "is_hostile": self.is_hostile,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_visor(data: typing.BinaryIO, game: Game, property_size: int) -> VisorParameters:
    return VisorParameters.from_stream(data, game, property_size)


def _decode_damage_originator(data: typing.BinaryIO, game: Game, property_size: int) -> enums.DamageableTriggerEnumEnum:
    return enums.DamageableTriggerEnumEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0x704B5369: ("orbitable", structs.decode_BIG_bool_),
    0x5DFD7820: ("enable_seeker_lock_on", structs.decode_BIG_bool_),
    0x6652BDD7: ("invulnerable", structs.decode_BIG_bool_),
    0xF0E07A4B: ("show_on_radar", structs.decode_BIG_bool_),
    0x05AD250E: ("visor", _decode_visor),
    0x8B9D2123: ("damage_originator", _decode_damage_originator),
    0xCE2CF510: ("only_take_damage_from_inhabitants", structs.decode_BIG_bool_),
    0x701B61B3: ("is_hostile", structs.decode_BIG_bool_),
}
