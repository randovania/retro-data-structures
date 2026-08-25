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
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class MetroidAlphaJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        frozen_vulnerability: json_util.JsonObject
        energy_drain_vulnerability: json_util.JsonObject
        damage_vulnerability: json_util.JsonObject
        unknown_0x72439b39: float
        unknown_0x3af75fcc: float
        telegraph_attack_time: float
        baby_metroid_scale: float
        unknown_0x03362858: float
        unknown_0x852d3bb0: float
        unknown_0x1c783744: float
        part: int
        unknown_0x2fe164c4: float
        unknown_0x4c1f78f3: float
        unknown_0x5f3f294c: float
        unknown_0x06b460f4: float
        chance_to_dodge: float
        unknown_0xfa51d735: int
        ing_possession_data: json_util.JsonObject


@dataclasses.dataclass()
class MetroidAlpha(BaseObjectType):
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
    patterned: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0xB3774750,
                original_name="Patterned",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    actor_information: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x7E397FED,
                original_name="ActorInformation",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    frozen_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x411938AA,
                original_name="FrozenVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    energy_drain_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xD86EE93F,
                original_name="EnergyDrainVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    damage_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x39D63082,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0x72439b39: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x72439B39, original_name="Unknown"),
        },
    )
    unknown_0x3af75fcc: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3AF75FCC, original_name="Unknown"),
        },
    )
    telegraph_attack_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA97EDC02, original_name="TelegraphAttackTime"),
        },
    )
    baby_metroid_scale: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D7E7E2C, original_name="BabyMetroidScale"),
        },
    )
    unknown_0x03362858: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x03362858, original_name="Unknown"),
        },
    )
    unknown_0x852d3bb0: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x852D3BB0, original_name="Unknown"),
        },
    )
    unknown_0x1c783744: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1C783744, original_name="Unknown"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x71A21B50, original_name="PART"),
        },
    )
    unknown_0x2fe164c4: float = dataclasses.field(
        default=1.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2FE164C4, original_name="Unknown"),
        },
    )
    unknown_0x4c1f78f3: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4C1F78F3, original_name="Unknown"),
        },
    )
    unknown_0x5f3f294c: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5F3F294C, original_name="Unknown"),
        },
    )
    unknown_0x06b460f4: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x06B460F4, original_name="Unknown"),
        },
    )
    chance_to_dodge: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23CA0676, original_name="ChanceToDodge"),
        },
    )
    unknown_0xfa51d735: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFA51D735, original_name="Unknown"),
        },
    )
    ing_possession_data: IngPossessionData = dataclasses.field(
        default_factory=IngPossessionData,
        metadata={
            "reflection": FieldReflection[IngPossessionData](
                IngPossessionData,
                id=0xE61748ED,
                original_name="IngPossessionData",
                from_json=IngPossessionData.from_json,
                to_json=IngPossessionData.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "MTDA"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Metroid.rel"]

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
        if property_count != 21:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "turn_speed": 180.0,
                "detection_range": 60.0,
                "max_attack_range": 10.0,
                "average_attack_time": 6.0,
                "attack_time_variation": 5.0,
                "creature_size": 1,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x411938AA
        frozen_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD86EE93F
        energy_drain_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39D63082
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72439B39
        unknown_0x72439b39 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3AF75FCC
        unknown_0x3af75fcc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA97EDC02
        telegraph_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D7E7E2C
        baby_metroid_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03362858
        unknown_0x03362858 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x852D3BB0
        unknown_0x852d3bb0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C783744
        unknown_0x1c783744 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71A21B50
        part = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2FE164C4
        unknown_0x2fe164c4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C1F78F3
        unknown_0x4c1f78f3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F3F294C
        unknown_0x5f3f294c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06B460F4
        unknown_0x06b460f4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23CA0676
        chance_to_dodge = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFA51D735
        unknown_0xfa51d735 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE61748ED
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            patterned,
            actor_information,
            frozen_vulnerability,
            energy_drain_vulnerability,
            damage_vulnerability,
            unknown_0x72439b39,
            unknown_0x3af75fcc,
            telegraph_attack_time,
            baby_metroid_scale,
            unknown_0x03362858,
            unknown_0x852d3bb0,
            unknown_0x1c783744,
            part,
            unknown_0x2fe164c4,
            unknown_0x4c1f78f3,
            unknown_0x5f3f294c,
            unknown_0x06b460f4,
            chance_to_dodge,
            unknown_0xfa51d735,
            ing_possession_data,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(
            data,
            game,
            default_override={
                "turn_speed": 180.0,
                "detection_range": 60.0,
                "max_attack_range": 10.0,
                "average_attack_time": 6.0,
                "attack_time_variation": 5.0,
                "creature_size": 1,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"A\x198\xaa")  # 0x411938aa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.frozen_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd8n\xe9?")  # 0xd86ee93f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.energy_drain_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"9\xd60\x82")  # 0x39d63082
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"rC\x9b9")  # 0x72439b39
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x72439b39))

        data.write(b":\xf7_\xcc")  # 0x3af75fcc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3af75fcc))

        data.write(b"\xa9~\xdc\x02")  # 0xa97edc02
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.telegraph_attack_time))

        data.write(b"\r~~,")  # 0xd7e7e2c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.baby_metroid_scale))

        data.write(b"\x036(X")  # 0x3362858
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x03362858))

        data.write(b"\x85-;\xb0")  # 0x852d3bb0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x852d3bb0))

        data.write(b"\x1cx7D")  # 0x1c783744
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1c783744))

        data.write(b"q\xa2\x1bP")  # 0x71a21b50
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b"/\xe1d\xc4")  # 0x2fe164c4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2fe164c4))

        data.write(b"L\x1fx\xf3")  # 0x4c1f78f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4c1f78f3))

        data.write(b"_?)L")  # 0x5f3f294c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5f3f294c))

        data.write(b"\x06\xb4`\xf4")  # 0x6b460f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x06b460f4))

        data.write(b"#\xca\x06v")  # 0x23ca0676
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.chance_to_dodge))

        data.write(b"\xfaQ\xd75")  # 0xfa51d735
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xfa51d735))

        data.write(b"\xe6\x17H\xed")  # 0xe61748ed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidAlphaJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            frozen_vulnerability=DamageVulnerability.from_json(json_data["frozen_vulnerability"]),
            energy_drain_vulnerability=DamageVulnerability.from_json(json_data["energy_drain_vulnerability"]),
            damage_vulnerability=DamageVulnerability.from_json(json_data["damage_vulnerability"]),
            unknown_0x72439b39=json_data["unknown_0x72439b39"],
            unknown_0x3af75fcc=json_data["unknown_0x3af75fcc"],
            telegraph_attack_time=json_data["telegraph_attack_time"],
            baby_metroid_scale=json_data["baby_metroid_scale"],
            unknown_0x03362858=json_data["unknown_0x03362858"],
            unknown_0x852d3bb0=json_data["unknown_0x852d3bb0"],
            unknown_0x1c783744=json_data["unknown_0x1c783744"],
            part=json_data["part"],
            unknown_0x2fe164c4=json_data["unknown_0x2fe164c4"],
            unknown_0x4c1f78f3=json_data["unknown_0x4c1f78f3"],
            unknown_0x5f3f294c=json_data["unknown_0x5f3f294c"],
            unknown_0x06b460f4=json_data["unknown_0x06b460f4"],
            chance_to_dodge=json_data["chance_to_dodge"],
            unknown_0xfa51d735=json_data["unknown_0xfa51d735"],
            ing_possession_data=IngPossessionData.from_json(json_data["ing_possession_data"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "frozen_vulnerability": self.frozen_vulnerability.to_json(),
            "energy_drain_vulnerability": self.energy_drain_vulnerability.to_json(),
            "damage_vulnerability": self.damage_vulnerability.to_json(),
            "unknown_0x72439b39": self.unknown_0x72439b39,
            "unknown_0x3af75fcc": self.unknown_0x3af75fcc,
            "telegraph_attack_time": self.telegraph_attack_time,
            "baby_metroid_scale": self.baby_metroid_scale,
            "unknown_0x03362858": self.unknown_0x03362858,
            "unknown_0x852d3bb0": self.unknown_0x852d3bb0,
            "unknown_0x1c783744": self.unknown_0x1c783744,
            "part": self.part,
            "unknown_0x2fe164c4": self.unknown_0x2fe164c4,
            "unknown_0x4c1f78f3": self.unknown_0x4c1f78f3,
            "unknown_0x5f3f294c": self.unknown_0x5f3f294c,
            "unknown_0x06b460f4": self.unknown_0x06b460f4,
            "chance_to_dodge": self.chance_to_dodge,
            "unknown_0xfa51d735": self.unknown_0xfa51d735,
            "ing_possession_data": self.ing_possession_data.to_json(),
        }

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for MetroidAlpha.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "turn_speed": 180.0,
            "detection_range": 60.0,
            "max_attack_range": 10.0,
            "average_attack_time": 6.0,
            "attack_time_variation": 5.0,
            "creature_size": 1,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_frozen_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_energy_drain_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x411938AA: ("frozen_vulnerability", _decode_frozen_vulnerability),
    0xD86EE93F: ("energy_drain_vulnerability", _decode_energy_drain_vulnerability),
    0x39D63082: ("damage_vulnerability", _decode_damage_vulnerability),
    0x72439B39: ("unknown_0x72439b39", structs.decode_BIG_f),
    0x3AF75FCC: ("unknown_0x3af75fcc", structs.decode_BIG_f),
    0xA97EDC02: ("telegraph_attack_time", structs.decode_BIG_f),
    0x0D7E7E2C: ("baby_metroid_scale", structs.decode_BIG_f),
    0x03362858: ("unknown_0x03362858", structs.decode_BIG_f),
    0x852D3BB0: ("unknown_0x852d3bb0", structs.decode_BIG_f),
    0x1C783744: ("unknown_0x1c783744", structs.decode_BIG_f),
    0x71A21B50: ("part", structs.decode_BIG_L),
    0x2FE164C4: ("unknown_0x2fe164c4", structs.decode_BIG_f),
    0x4C1F78F3: ("unknown_0x4c1f78f3", structs.decode_BIG_f),
    0x5F3F294C: ("unknown_0x5f3f294c", structs.decode_BIG_f),
    0x06B460F4: ("unknown_0x06b460f4", structs.decode_BIG_f),
    0x23CA0676: ("chance_to_dodge", structs.decode_BIG_f),
    0xFA51D735: ("unknown_0xfa51d735", structs.decode_BIG_l),
    0xE61748ED: ("ing_possession_data", _decode_ing_possession_data),
}
