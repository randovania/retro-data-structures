# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.FlareDef import FlareDef
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DroneJson(typing_extensions.TypedDict):
        name: str
        unknown_1: int
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unknown_2: float
        unnamed_0x00000006: json_util.JsonObject
        unnamed_0x00000007: json_util.JsonObject
        damage_info_1: json_util.JsonObject
        unknown_3: int
        damage_info_2: json_util.JsonObject
        particle_1: int
        particle_2: int
        model_1: int
        flare_def_1: json_util.JsonObject
        flare_def_2: json_util.JsonObject
        flare_def_3: json_util.JsonObject
        flare_def_4: json_util.JsonObject
        flare_def_5: json_util.JsonObject
        unknown_7: float
        unknown_8: float
        unknown_9: float
        unknown_10: float
        unknown_11: float
        unknown_12: float
        unknown_13: float
        unknown_14: float
        unknown_15: float
        unknown_16: float
        unknown_17: float
        unknown_18: float
        unknown_19: float
        unknown_20: float
        unknown_21: float
        unknown_22: float
        unknown_23: float
        unknown_24: float
        unknown_25: float
        crsc: int
        unknown_26: float
        unknown_27: float
        unknown_28: float
        unknown_29: float
        sound: int
        unknown_30: bool


@dataclasses.dataclass()
class Drone(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Unknown 1"),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000003, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Unknown 2"),
        },
    )
    unnamed_0x00000006: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x00000006,
                original_name="6",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    unnamed_0x00000007: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000007,
                original_name="7",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    damage_info_1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000008,
                original_name="DamageInfo 1",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Unknown 3"),
        },
    )
    damage_info_2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000A,
                original_name="DamageInfo 2",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="Particle 1"),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="Particle 2"),
        },
    )
    model_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="Model 1"),
        },
    )
    flare_def_1: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x0000000E,
                original_name="FlareDef 1",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_2: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x0000000F,
                original_name="FlareDef 2",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_3: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x00000010,
                original_name="FlareDef 3",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_4: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x00000011,
                original_name="FlareDef 4",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_5: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x00000012,
                original_name="FlareDef 5",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="Unknown 7"),
        },
    )
    unknown_8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="Unknown 8"),
        },
    )
    unknown_9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="Unknown 9"),
        },
    )
    unknown_10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="Unknown 10"),
        },
    )
    unknown_11: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000017, original_name="Unknown 11"),
        },
    )
    unknown_12: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000018, original_name="Unknown 12"),
        },
    )
    unknown_13: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000019, original_name="Unknown 13"),
        },
    )
    unknown_14: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001A, original_name="Unknown 14"),
        },
    )
    unknown_15: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001B, original_name="Unknown 15"),
        },
    )
    unknown_16: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="Unknown 16"),
        },
    )
    unknown_17: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="Unknown 17"),
        },
    )
    unknown_18: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001E, original_name="Unknown 18"),
        },
    )
    unknown_19: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001F, original_name="Unknown 19"),
        },
    )
    unknown_20: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000020, original_name="Unknown 20"),
        },
    )
    unknown_21: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000021, original_name="Unknown 21"),
        },
    )
    unknown_22: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000022, original_name="Unknown 22"),
        },
    )
    unknown_23: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000023, original_name="Unknown 23"),
        },
    )
    unknown_24: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000024, original_name="Unknown 24"),
        },
    )
    unknown_25: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000025, original_name="Unknown 25"),
        },
    )
    crsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CRSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000026, original_name="CRSC"),
        },
    )
    unknown_26: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000027, original_name="Unknown 26"),
        },
    )
    unknown_27: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000028, original_name="Unknown 27"),
        },
    )
    unknown_28: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000029, original_name="Unknown 28"),
        },
    )
    unknown_29: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000002A, original_name="Unknown 29"),
        },
    )
    sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000002B, original_name="Sound"),
        },
    )
    unknown_30: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000002C, original_name="Unknown 30"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x43

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000006 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000007 = ActorParameters.from_stream(data, game, property_size)
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        unknown_3 = structs.BIG_l.unpack(data.read(4))[0]
        damage_info_2 = DamageInfo.from_stream(data, game, property_size)
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        model_1 = structs.BIG_L.unpack(data.read(4))[0]
        flare_def_1 = FlareDef.from_stream(data, game, property_size)
        flare_def_2 = FlareDef.from_stream(data, game, property_size)
        flare_def_3 = FlareDef.from_stream(data, game, property_size)
        flare_def_4 = FlareDef.from_stream(data, game, property_size)
        flare_def_5 = FlareDef.from_stream(data, game, property_size)
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_9 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_11 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_12 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_13 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_14 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_15 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_16 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_17 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_18 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_19 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_20 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_21 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_22 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_23 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_24 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_25 = structs.BIG_f.unpack(data.read(4))[0]
        crsc = structs.BIG_L.unpack(data.read(4))[0]
        unknown_26 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_27 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_28 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_29 = structs.BIG_f.unpack(data.read(4))[0]
        sound = structs.BIG_l.unpack(data.read(4))[0]
        unknown_30 = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            unknown_1,
            position,
            rotation,
            scale,
            unknown_2,
            unnamed_0x00000006,
            unnamed_0x00000007,
            damage_info_1,
            unknown_3,
            damage_info_2,
            particle_1,
            particle_2,
            model_1,
            flare_def_1,
            flare_def_2,
            flare_def_3,
            flare_def_4,
            flare_def_5,
            unknown_7,
            unknown_8,
            unknown_9,
            unknown_10,
            unknown_11,
            unknown_12,
            unknown_13,
            unknown_14,
            unknown_15,
            unknown_16,
            unknown_17,
            unknown_18,
            unknown_19,
            unknown_20,
            unknown_21,
            unknown_22,
            unknown_23,
            unknown_24,
            unknown_25,
            crsc,
            unknown_26,
            unknown_27,
            unknown_28,
            unknown_29,
            sound,
            unknown_30,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00-")  # 45 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.unknown_1))
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_2))
        self.unnamed_0x00000006.to_stream(data, game)
        self.unnamed_0x00000007.to_stream(data, game)
        self.damage_info_1.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.unknown_3))
        self.damage_info_2.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle_1))
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_L.pack(self.model_1))
        self.flare_def_1.to_stream(data, game)
        self.flare_def_2.to_stream(data, game)
        self.flare_def_3.to_stream(data, game)
        self.flare_def_4.to_stream(data, game)
        self.flare_def_5.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_7))
        data.write(structs.BIG_f.pack(self.unknown_8))
        data.write(structs.BIG_f.pack(self.unknown_9))
        data.write(structs.BIG_f.pack(self.unknown_10))
        data.write(structs.BIG_f.pack(self.unknown_11))
        data.write(structs.BIG_f.pack(self.unknown_12))
        data.write(structs.BIG_f.pack(self.unknown_13))
        data.write(structs.BIG_f.pack(self.unknown_14))
        data.write(structs.BIG_f.pack(self.unknown_15))
        data.write(structs.BIG_f.pack(self.unknown_16))
        data.write(structs.BIG_f.pack(self.unknown_17))
        data.write(structs.BIG_f.pack(self.unknown_18))
        data.write(structs.BIG_f.pack(self.unknown_19))
        data.write(structs.BIG_f.pack(self.unknown_20))
        data.write(structs.BIG_f.pack(self.unknown_21))
        data.write(structs.BIG_f.pack(self.unknown_22))
        data.write(structs.BIG_f.pack(self.unknown_23))
        data.write(structs.BIG_f.pack(self.unknown_24))
        data.write(structs.BIG_f.pack(self.unknown_25))
        data.write(structs.BIG_L.pack(self.crsc))
        data.write(structs.BIG_f.pack(self.unknown_26))
        data.write(structs.BIG_f.pack(self.unknown_27))
        data.write(structs.BIG_f.pack(self.unknown_28))
        data.write(structs.BIG_f.pack(self.unknown_29))
        data.write(structs.BIG_l.pack(self.sound))
        data.write(structs.BIG_bool_.pack(self.unknown_30))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DroneJson", data)
        return cls(
            name=json_data["name"],
            unknown_1=json_data["unknown_1"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unknown_2=json_data["unknown_2"],
            unnamed_0x00000006=PatternedAITypedef.from_json(json_data["unnamed_0x00000006"]),
            unnamed_0x00000007=ActorParameters.from_json(json_data["unnamed_0x00000007"]),
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            unknown_3=json_data["unknown_3"],
            damage_info_2=DamageInfo.from_json(json_data["damage_info_2"]),
            particle_1=json_data["particle_1"],
            particle_2=json_data["particle_2"],
            model_1=json_data["model_1"],
            flare_def_1=FlareDef.from_json(json_data["flare_def_1"]),
            flare_def_2=FlareDef.from_json(json_data["flare_def_2"]),
            flare_def_3=FlareDef.from_json(json_data["flare_def_3"]),
            flare_def_4=FlareDef.from_json(json_data["flare_def_4"]),
            flare_def_5=FlareDef.from_json(json_data["flare_def_5"]),
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
            unknown_9=json_data["unknown_9"],
            unknown_10=json_data["unknown_10"],
            unknown_11=json_data["unknown_11"],
            unknown_12=json_data["unknown_12"],
            unknown_13=json_data["unknown_13"],
            unknown_14=json_data["unknown_14"],
            unknown_15=json_data["unknown_15"],
            unknown_16=json_data["unknown_16"],
            unknown_17=json_data["unknown_17"],
            unknown_18=json_data["unknown_18"],
            unknown_19=json_data["unknown_19"],
            unknown_20=json_data["unknown_20"],
            unknown_21=json_data["unknown_21"],
            unknown_22=json_data["unknown_22"],
            unknown_23=json_data["unknown_23"],
            unknown_24=json_data["unknown_24"],
            unknown_25=json_data["unknown_25"],
            crsc=json_data["crsc"],
            unknown_26=json_data["unknown_26"],
            unknown_27=json_data["unknown_27"],
            unknown_28=json_data["unknown_28"],
            unknown_29=json_data["unknown_29"],
            sound=json_data["sound"],
            unknown_30=json_data["unknown_30"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "unknown_1": self.unknown_1,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unknown_2": self.unknown_2,
            "unnamed_0x00000006": self.unnamed_0x00000006.to_json(),
            "unnamed_0x00000007": self.unnamed_0x00000007.to_json(),
            "damage_info_1": self.damage_info_1.to_json(),
            "unknown_3": self.unknown_3,
            "damage_info_2": self.damage_info_2.to_json(),
            "particle_1": self.particle_1,
            "particle_2": self.particle_2,
            "model_1": self.model_1,
            "flare_def_1": self.flare_def_1.to_json(),
            "flare_def_2": self.flare_def_2.to_json(),
            "flare_def_3": self.flare_def_3.to_json(),
            "flare_def_4": self.flare_def_4.to_json(),
            "flare_def_5": self.flare_def_5.to_json(),
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
            "unknown_9": self.unknown_9,
            "unknown_10": self.unknown_10,
            "unknown_11": self.unknown_11,
            "unknown_12": self.unknown_12,
            "unknown_13": self.unknown_13,
            "unknown_14": self.unknown_14,
            "unknown_15": self.unknown_15,
            "unknown_16": self.unknown_16,
            "unknown_17": self.unknown_17,
            "unknown_18": self.unknown_18,
            "unknown_19": self.unknown_19,
            "unknown_20": self.unknown_20,
            "unknown_21": self.unknown_21,
            "unknown_22": self.unknown_22,
            "unknown_23": self.unknown_23,
            "unknown_24": self.unknown_24,
            "unknown_25": self.unknown_25,
            "crsc": self.crsc,
            "unknown_26": self.unknown_26,
            "unknown_27": self.unknown_27,
            "unknown_28": self.unknown_28,
            "unknown_29": self.unknown_29,
            "sound": self.sound,
            "unknown_30": self.unknown_30,
        }

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def _dependencies_for_model_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model_1)

    def _dependencies_for_crsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.crsc)

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000006.dependencies_for, "unnamed_0x00000006", "PatternedAITypedef"),
            (self.unnamed_0x00000007.dependencies_for, "unnamed_0x00000007", "ActorParameters"),
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
            (self._dependencies_for_model_1, "model_1", "AssetId"),
            (self.flare_def_1.dependencies_for, "flare_def_1", "FlareDef"),
            (self.flare_def_2.dependencies_for, "flare_def_2", "FlareDef"),
            (self.flare_def_3.dependencies_for, "flare_def_3", "FlareDef"),
            (self.flare_def_4.dependencies_for, "flare_def_4", "FlareDef"),
            (self.flare_def_5.dependencies_for, "flare_def_5", "FlareDef"),
            (self._dependencies_for_crsc, "crsc", "AssetId"),
            (self._dependencies_for_sound, "sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Drone.{field_name} ({field_type}): {e}")
