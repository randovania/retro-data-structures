# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class IngPossessionDataJson(typing_extensions.TypedDict):
        is_an_encounter: bool
        unknown_0xb68c0aa3: bool
        ing_possessed_model: int
        ing_possessed_skin_rules: int
        dark_scan_info: int
        ing_possessed_health: json_util.JsonObject
        ing_possessed_damage_multiplier: float
        unknown_0x2befc1bf: int
        ing_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class IngPossessionData(BaseProperty):
    is_an_encounter: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x888FA435, original_name="IsAnEncounter"),
        },
    )
    unknown_0xb68c0aa3: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB68C0AA3, original_name="Unknown"),
        },
    )
    ing_possessed_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAD54DA11, original_name="IngPossessedModel"),
        },
    )
    ing_possessed_skin_rules: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF5C66384, original_name="IngPossessedSkinRules"),
        },
    )
    dark_scan_info: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x35A9792E, original_name="DarkScanInfo"),
        },
    )
    ing_possessed_health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0x1D852D4B,
                original_name="IngPossessedHealth",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    ing_possessed_damage_multiplier: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x487E4F9A, original_name="IngPossessedDamageMultiplier"),
        },
    )
    unknown_0x2befc1bf: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2BEFC1BF, original_name="Unknown"),
        },
    )
    ing_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x4AEEC093,
                original_name="IngVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
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
        if property_count != 9:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x888FA435
        is_an_encounter = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB68C0AA3
        unknown_0xb68c0aa3 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD54DA11
        ing_possessed_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5C66384
        ing_possessed_skin_rules = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35A9792E
        dark_scan_info = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D852D4B
        ing_possessed_health = HealthInfo.from_stream(
            data, game, property_size, default_override={"health": 150.0, "hi_knock_back_resistance": 2.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x487E4F9A
        ing_possessed_damage_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BEFC1BF
        unknown_0x2befc1bf = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AEEC093
        ing_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            is_an_encounter,
            unknown_0xb68c0aa3,
            ing_possessed_model,
            ing_possessed_skin_rules,
            dark_scan_info,
            ing_possessed_health,
            ing_possessed_damage_multiplier,
            unknown_0x2befc1bf,
            ing_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"\x88\x8f\xa45")  # 0x888fa435
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_an_encounter))

        data.write(b"\xb6\x8c\n\xa3")  # 0xb68c0aa3
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xb68c0aa3))

        data.write(b"\xadT\xda\x11")  # 0xad54da11
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.ing_possessed_model))

        data.write(b"\xf5\xc6c\x84")  # 0xf5c66384
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.ing_possessed_skin_rules))

        data.write(b"5\xa9y.")  # 0x35a9792e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dark_scan_info))

        data.write(b"\x1d\x85-K")  # 0x1d852d4b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possessed_health.to_stream(
            data, game, default_override={"health": 150.0, "hi_knock_back_resistance": 2.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"H~O\x9a")  # 0x487e4f9a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ing_possessed_damage_multiplier))

        data.write(b"+\xef\xc1\xbf")  # 0x2befc1bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x2befc1bf))

        data.write(b"J\xee\xc0\x93")  # 0x4aeec093
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("IngPossessionDataJson", data)
        return cls(
            is_an_encounter=json_data["is_an_encounter"],
            unknown_0xb68c0aa3=json_data["unknown_0xb68c0aa3"],
            ing_possessed_model=json_data["ing_possessed_model"],
            ing_possessed_skin_rules=json_data["ing_possessed_skin_rules"],
            dark_scan_info=json_data["dark_scan_info"],
            ing_possessed_health=HealthInfo.from_json(json_data["ing_possessed_health"]),
            ing_possessed_damage_multiplier=json_data["ing_possessed_damage_multiplier"],
            unknown_0x2befc1bf=json_data["unknown_0x2befc1bf"],
            ing_vulnerability=DamageVulnerability.from_json(json_data["ing_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "is_an_encounter": self.is_an_encounter,
            "unknown_0xb68c0aa3": self.unknown_0xb68c0aa3,
            "ing_possessed_model": self.ing_possessed_model,
            "ing_possessed_skin_rules": self.ing_possessed_skin_rules,
            "dark_scan_info": self.dark_scan_info,
            "ing_possessed_health": self.ing_possessed_health.to_json(),
            "ing_possessed_damage_multiplier": self.ing_possessed_damage_multiplier,
            "unknown_0x2befc1bf": self.unknown_0x2befc1bf,
            "ing_vulnerability": self.ing_vulnerability.to_json(),
        }

    def _dependencies_for_ing_possessed_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_possessed_model)

    def _dependencies_for_ing_possessed_skin_rules(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_possessed_skin_rules)

    def _dependencies_for_dark_scan_info(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_scan_info)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_ing_possessed_model, "ing_possessed_model", "AssetId"),
            (self._dependencies_for_ing_possessed_skin_rules, "ing_possessed_skin_rules", "AssetId"),
            (self._dependencies_for_dark_scan_info, "dark_scan_info", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for IngPossessionData.{field_name} ({field_type}): {e}")


def _decode_ing_possessed_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(
        data, game, property_size, default_override={"health": 150.0, "hi_knock_back_resistance": 2.0}
    )


def _decode_ing_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x888FA435: ("is_an_encounter", structs.decode_BIG_bool_),
    0xB68C0AA3: ("unknown_0xb68c0aa3", structs.decode_BIG_bool_),
    0xAD54DA11: ("ing_possessed_model", structs.decode_BIG_L),
    0xF5C66384: ("ing_possessed_skin_rules", structs.decode_BIG_L),
    0x35A9792E: ("dark_scan_info", structs.decode_BIG_L),
    0x1D852D4B: ("ing_possessed_health", _decode_ing_possessed_health),
    0x487E4F9A: ("ing_possessed_damage_multiplier", structs.decode_BIG_f),
    0x2BEFC1BF: ("unknown_0x2befc1bf", structs.decode_BIG_l),
    0x4AEEC093: ("ing_vulnerability", _decode_ing_vulnerability),
}
