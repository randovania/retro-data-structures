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
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ThardusJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        unknown_1: bool
        unknown_2: bool
        rock_weak_point_1_model: int
        rock_weak_point_2_model: int
        rock_weak_point_3_model: int
        rock_weak_point_4_model: int
        rock_weak_point_5_model: int
        rock_weak_point_6_model: int
        rock_weak_point_7_model: int
        phazon_weak_point_1_model: int
        phazon_weak_point_2_model: int
        phazon_weak_point_3_model: int
        phazon_weak_point_4_model: int
        phazon_weak_point_5_model: int
        phazon_weak_point_6_model: int
        phazon_weak_point_7_model: int
        particle_1: int
        particle_2: int
        particle_3: int
        state_machine: int
        particle_4: int
        particle_5: int
        particle_6: int
        particle_7: int
        particle_8: int
        particle_9: int
        roll_speed: float
        unknown_4: float
        unknown_5: float
        phazon_weak_point_health: float
        rock_weak_point_health: float
        ice_spikes_speed: float
        texture: int
        unknown_9: int
        particle_10: int
        unknown_10: int
        unknown_11: int
        unknown_12: int


@dataclasses.dataclass()
class Thardus(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000001, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000003, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unnamed_0x00000004: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x00000004,
                original_name="4",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    unnamed_0x00000005: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000005,
                original_name="5",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unknown_1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="Unknown 1"),
        },
    )
    unknown_2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="Unknown 2"),
        },
    )
    rock_weak_point_1_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="Rock Weak Point 1 Model"),
        },
    )
    rock_weak_point_2_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="Rock Weak Point 2 Model"),
        },
    )
    rock_weak_point_3_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="Rock Weak Point 3 Model"),
        },
    )
    rock_weak_point_4_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="Rock Weak Point 4 Model"),
        },
    )
    rock_weak_point_5_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="Rock Weak Point 5 Model"),
        },
    )
    rock_weak_point_6_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="Rock Weak Point 6 Model"),
        },
    )
    rock_weak_point_7_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000E, original_name="Rock Weak Point 7 Model"),
        },
    )
    phazon_weak_point_1_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000F, original_name="Phazon Weak Point 1 Model"),
        },
    )
    phazon_weak_point_2_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000010, original_name="Phazon Weak Point 2 Model"),
        },
    )
    phazon_weak_point_3_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000011, original_name="Phazon Weak Point 3 Model"),
        },
    )
    phazon_weak_point_4_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000012, original_name="Phazon Weak Point 4 Model"),
        },
    )
    phazon_weak_point_5_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000013, original_name="Phazon Weak Point 5 Model"),
        },
    )
    phazon_weak_point_6_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000014, original_name="Phazon Weak Point 6 Model"),
        },
    )
    phazon_weak_point_7_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000015, original_name="Phazon Weak Point 7 Model"),
        },
    )
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000016, original_name="Particle 1"),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000017, original_name="Particle 2"),
        },
    )
    particle_3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000018, original_name="Particle 3"),
        },
    )
    state_machine: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["AFSM"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000019, original_name="State Machine"),
        },
    )
    particle_4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001A, original_name="Particle 4"),
        },
    )
    particle_5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001B, original_name="Particle 5"),
        },
    )
    particle_6: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001C, original_name="Particle 6"),
        },
    )
    particle_7: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001D, original_name="Particle 7"),
        },
    )
    particle_8: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001E, original_name="Particle 8"),
        },
    )
    particle_9: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001F, original_name="Particle 9"),
        },
    )
    roll_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000020, original_name="Roll Speed"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000021, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000022, original_name="Unknown 5"),
        },
    )
    phazon_weak_point_health: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000023, original_name="Phazon Weak Point Health"),
        },
    )
    rock_weak_point_health: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000024, original_name="Rock Weak Point Health"),
        },
    )
    ice_spikes_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000025, original_name="Ice Spikes Speed"),
        },
    )
    texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000026, original_name="Texture"),
        },
    )
    unknown_9: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000027, original_name="Unknown 9"),
        },
    )
    particle_10: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000028, original_name="Particle 10"),
        },
    )
    unknown_10: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000029, original_name="Unknown 10"),
        },
    )
    unknown_11: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000002A, original_name="Unknown 11"),
        },
    )
    unknown_12: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000002B, original_name="Unknown 12"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x58

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000004 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000005 = ActorParameters.from_stream(data, game, property_size)
        unknown_1 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_2 = structs.BIG_bool_.unpack(data.read(1))[0]
        rock_weak_point_1_model = structs.BIG_L.unpack(data.read(4))[0]
        rock_weak_point_2_model = structs.BIG_L.unpack(data.read(4))[0]
        rock_weak_point_3_model = structs.BIG_L.unpack(data.read(4))[0]
        rock_weak_point_4_model = structs.BIG_L.unpack(data.read(4))[0]
        rock_weak_point_5_model = structs.BIG_L.unpack(data.read(4))[0]
        rock_weak_point_6_model = structs.BIG_L.unpack(data.read(4))[0]
        rock_weak_point_7_model = structs.BIG_L.unpack(data.read(4))[0]
        phazon_weak_point_1_model = structs.BIG_L.unpack(data.read(4))[0]
        phazon_weak_point_2_model = structs.BIG_L.unpack(data.read(4))[0]
        phazon_weak_point_3_model = structs.BIG_L.unpack(data.read(4))[0]
        phazon_weak_point_4_model = structs.BIG_L.unpack(data.read(4))[0]
        phazon_weak_point_5_model = structs.BIG_L.unpack(data.read(4))[0]
        phazon_weak_point_6_model = structs.BIG_L.unpack(data.read(4))[0]
        phazon_weak_point_7_model = structs.BIG_L.unpack(data.read(4))[0]
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        particle_3 = structs.BIG_L.unpack(data.read(4))[0]
        state_machine = structs.BIG_L.unpack(data.read(4))[0]
        particle_4 = structs.BIG_L.unpack(data.read(4))[0]
        particle_5 = structs.BIG_L.unpack(data.read(4))[0]
        particle_6 = structs.BIG_L.unpack(data.read(4))[0]
        particle_7 = structs.BIG_L.unpack(data.read(4))[0]
        particle_8 = structs.BIG_L.unpack(data.read(4))[0]
        particle_9 = structs.BIG_L.unpack(data.read(4))[0]
        roll_speed = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        phazon_weak_point_health = structs.BIG_f.unpack(data.read(4))[0]
        rock_weak_point_health = structs.BIG_f.unpack(data.read(4))[0]
        ice_spikes_speed = structs.BIG_f.unpack(data.read(4))[0]
        texture = structs.BIG_L.unpack(data.read(4))[0]
        unknown_9 = structs.BIG_l.unpack(data.read(4))[0]
        particle_10 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_11 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_12 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            unknown_1,
            unknown_2,
            rock_weak_point_1_model,
            rock_weak_point_2_model,
            rock_weak_point_3_model,
            rock_weak_point_4_model,
            rock_weak_point_5_model,
            rock_weak_point_6_model,
            rock_weak_point_7_model,
            phazon_weak_point_1_model,
            phazon_weak_point_2_model,
            phazon_weak_point_3_model,
            phazon_weak_point_4_model,
            phazon_weak_point_5_model,
            phazon_weak_point_6_model,
            phazon_weak_point_7_model,
            particle_1,
            particle_2,
            particle_3,
            state_machine,
            particle_4,
            particle_5,
            particle_6,
            particle_7,
            particle_8,
            particle_9,
            roll_speed,
            unknown_4,
            unknown_5,
            phazon_weak_point_health,
            rock_weak_point_health,
            ice_spikes_speed,
            texture,
            unknown_9,
            particle_10,
            unknown_10,
            unknown_11,
            unknown_12,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00,")  # 44 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.unknown_1))
        data.write(structs.BIG_bool_.pack(self.unknown_2))
        data.write(structs.BIG_L.pack(self.rock_weak_point_1_model))
        data.write(structs.BIG_L.pack(self.rock_weak_point_2_model))
        data.write(structs.BIG_L.pack(self.rock_weak_point_3_model))
        data.write(structs.BIG_L.pack(self.rock_weak_point_4_model))
        data.write(structs.BIG_L.pack(self.rock_weak_point_5_model))
        data.write(structs.BIG_L.pack(self.rock_weak_point_6_model))
        data.write(structs.BIG_L.pack(self.rock_weak_point_7_model))
        data.write(structs.BIG_L.pack(self.phazon_weak_point_1_model))
        data.write(structs.BIG_L.pack(self.phazon_weak_point_2_model))
        data.write(structs.BIG_L.pack(self.phazon_weak_point_3_model))
        data.write(structs.BIG_L.pack(self.phazon_weak_point_4_model))
        data.write(structs.BIG_L.pack(self.phazon_weak_point_5_model))
        data.write(structs.BIG_L.pack(self.phazon_weak_point_6_model))
        data.write(structs.BIG_L.pack(self.phazon_weak_point_7_model))
        data.write(structs.BIG_L.pack(self.particle_1))
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_L.pack(self.particle_3))
        data.write(structs.BIG_L.pack(self.state_machine))
        data.write(structs.BIG_L.pack(self.particle_4))
        data.write(structs.BIG_L.pack(self.particle_5))
        data.write(structs.BIG_L.pack(self.particle_6))
        data.write(structs.BIG_L.pack(self.particle_7))
        data.write(structs.BIG_L.pack(self.particle_8))
        data.write(structs.BIG_L.pack(self.particle_9))
        data.write(structs.BIG_f.pack(self.roll_speed))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.phazon_weak_point_health))
        data.write(structs.BIG_f.pack(self.rock_weak_point_health))
        data.write(structs.BIG_f.pack(self.ice_spikes_speed))
        data.write(structs.BIG_L.pack(self.texture))
        data.write(structs.BIG_l.pack(self.unknown_9))
        data.write(structs.BIG_L.pack(self.particle_10))
        data.write(structs.BIG_l.pack(self.unknown_10))
        data.write(structs.BIG_l.pack(self.unknown_11))
        data.write(structs.BIG_l.pack(self.unknown_12))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ThardusJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            rock_weak_point_1_model=json_data["rock_weak_point_1_model"],
            rock_weak_point_2_model=json_data["rock_weak_point_2_model"],
            rock_weak_point_3_model=json_data["rock_weak_point_3_model"],
            rock_weak_point_4_model=json_data["rock_weak_point_4_model"],
            rock_weak_point_5_model=json_data["rock_weak_point_5_model"],
            rock_weak_point_6_model=json_data["rock_weak_point_6_model"],
            rock_weak_point_7_model=json_data["rock_weak_point_7_model"],
            phazon_weak_point_1_model=json_data["phazon_weak_point_1_model"],
            phazon_weak_point_2_model=json_data["phazon_weak_point_2_model"],
            phazon_weak_point_3_model=json_data["phazon_weak_point_3_model"],
            phazon_weak_point_4_model=json_data["phazon_weak_point_4_model"],
            phazon_weak_point_5_model=json_data["phazon_weak_point_5_model"],
            phazon_weak_point_6_model=json_data["phazon_weak_point_6_model"],
            phazon_weak_point_7_model=json_data["phazon_weak_point_7_model"],
            particle_1=json_data["particle_1"],
            particle_2=json_data["particle_2"],
            particle_3=json_data["particle_3"],
            state_machine=json_data["state_machine"],
            particle_4=json_data["particle_4"],
            particle_5=json_data["particle_5"],
            particle_6=json_data["particle_6"],
            particle_7=json_data["particle_7"],
            particle_8=json_data["particle_8"],
            particle_9=json_data["particle_9"],
            roll_speed=json_data["roll_speed"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            phazon_weak_point_health=json_data["phazon_weak_point_health"],
            rock_weak_point_health=json_data["rock_weak_point_health"],
            ice_spikes_speed=json_data["ice_spikes_speed"],
            texture=json_data["texture"],
            unknown_9=json_data["unknown_9"],
            particle_10=json_data["particle_10"],
            unknown_10=json_data["unknown_10"],
            unknown_11=json_data["unknown_11"],
            unknown_12=json_data["unknown_12"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "rock_weak_point_1_model": self.rock_weak_point_1_model,
            "rock_weak_point_2_model": self.rock_weak_point_2_model,
            "rock_weak_point_3_model": self.rock_weak_point_3_model,
            "rock_weak_point_4_model": self.rock_weak_point_4_model,
            "rock_weak_point_5_model": self.rock_weak_point_5_model,
            "rock_weak_point_6_model": self.rock_weak_point_6_model,
            "rock_weak_point_7_model": self.rock_weak_point_7_model,
            "phazon_weak_point_1_model": self.phazon_weak_point_1_model,
            "phazon_weak_point_2_model": self.phazon_weak_point_2_model,
            "phazon_weak_point_3_model": self.phazon_weak_point_3_model,
            "phazon_weak_point_4_model": self.phazon_weak_point_4_model,
            "phazon_weak_point_5_model": self.phazon_weak_point_5_model,
            "phazon_weak_point_6_model": self.phazon_weak_point_6_model,
            "phazon_weak_point_7_model": self.phazon_weak_point_7_model,
            "particle_1": self.particle_1,
            "particle_2": self.particle_2,
            "particle_3": self.particle_3,
            "state_machine": self.state_machine,
            "particle_4": self.particle_4,
            "particle_5": self.particle_5,
            "particle_6": self.particle_6,
            "particle_7": self.particle_7,
            "particle_8": self.particle_8,
            "particle_9": self.particle_9,
            "roll_speed": self.roll_speed,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "phazon_weak_point_health": self.phazon_weak_point_health,
            "rock_weak_point_health": self.rock_weak_point_health,
            "ice_spikes_speed": self.ice_spikes_speed,
            "texture": self.texture,
            "unknown_9": self.unknown_9,
            "particle_10": self.particle_10,
            "unknown_10": self.unknown_10,
            "unknown_11": self.unknown_11,
            "unknown_12": self.unknown_12,
        }

    def _dependencies_for_rock_weak_point_1_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rock_weak_point_1_model)

    def _dependencies_for_rock_weak_point_2_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rock_weak_point_2_model)

    def _dependencies_for_rock_weak_point_3_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rock_weak_point_3_model)

    def _dependencies_for_rock_weak_point_4_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rock_weak_point_4_model)

    def _dependencies_for_rock_weak_point_5_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rock_weak_point_5_model)

    def _dependencies_for_rock_weak_point_6_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rock_weak_point_6_model)

    def _dependencies_for_rock_weak_point_7_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rock_weak_point_7_model)

    def _dependencies_for_phazon_weak_point_1_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_weak_point_1_model)

    def _dependencies_for_phazon_weak_point_2_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_weak_point_2_model)

    def _dependencies_for_phazon_weak_point_3_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_weak_point_3_model)

    def _dependencies_for_phazon_weak_point_4_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_weak_point_4_model)

    def _dependencies_for_phazon_weak_point_5_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_weak_point_5_model)

    def _dependencies_for_phazon_weak_point_6_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_weak_point_6_model)

    def _dependencies_for_phazon_weak_point_7_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_weak_point_7_model)

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def _dependencies_for_particle_3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_3)

    def _dependencies_for_state_machine(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.state_machine)

    def _dependencies_for_particle_4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_4)

    def _dependencies_for_particle_5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_5)

    def _dependencies_for_particle_6(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_6)

    def _dependencies_for_particle_7(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_7)

    def _dependencies_for_particle_8(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_8)

    def _dependencies_for_particle_9(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_9)

    def _dependencies_for_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture)

    def _dependencies_for_unknown_9(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_9)

    def _dependencies_for_particle_10(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_10)

    def _dependencies_for_unknown_10(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_10)

    def _dependencies_for_unknown_11(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_11)

    def _dependencies_for_unknown_12(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_12)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_rock_weak_point_1_model, "rock_weak_point_1_model", "AssetId"),
            (self._dependencies_for_rock_weak_point_2_model, "rock_weak_point_2_model", "AssetId"),
            (self._dependencies_for_rock_weak_point_3_model, "rock_weak_point_3_model", "AssetId"),
            (self._dependencies_for_rock_weak_point_4_model, "rock_weak_point_4_model", "AssetId"),
            (self._dependencies_for_rock_weak_point_5_model, "rock_weak_point_5_model", "AssetId"),
            (self._dependencies_for_rock_weak_point_6_model, "rock_weak_point_6_model", "AssetId"),
            (self._dependencies_for_rock_weak_point_7_model, "rock_weak_point_7_model", "AssetId"),
            (self._dependencies_for_phazon_weak_point_1_model, "phazon_weak_point_1_model", "AssetId"),
            (self._dependencies_for_phazon_weak_point_2_model, "phazon_weak_point_2_model", "AssetId"),
            (self._dependencies_for_phazon_weak_point_3_model, "phazon_weak_point_3_model", "AssetId"),
            (self._dependencies_for_phazon_weak_point_4_model, "phazon_weak_point_4_model", "AssetId"),
            (self._dependencies_for_phazon_weak_point_5_model, "phazon_weak_point_5_model", "AssetId"),
            (self._dependencies_for_phazon_weak_point_6_model, "phazon_weak_point_6_model", "AssetId"),
            (self._dependencies_for_phazon_weak_point_7_model, "phazon_weak_point_7_model", "AssetId"),
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
            (self._dependencies_for_particle_3, "particle_3", "AssetId"),
            (self._dependencies_for_state_machine, "state_machine", "AssetId"),
            (self._dependencies_for_particle_4, "particle_4", "AssetId"),
            (self._dependencies_for_particle_5, "particle_5", "AssetId"),
            (self._dependencies_for_particle_6, "particle_6", "AssetId"),
            (self._dependencies_for_particle_7, "particle_7", "AssetId"),
            (self._dependencies_for_particle_8, "particle_8", "AssetId"),
            (self._dependencies_for_particle_9, "particle_9", "AssetId"),
            (self._dependencies_for_texture, "texture", "AssetId"),
            (self._dependencies_for_unknown_9, "unknown_9", "int"),
            (self._dependencies_for_particle_10, "particle_10", "AssetId"),
            (self._dependencies_for_unknown_10, "unknown_10", "int"),
            (self._dependencies_for_unknown_11, "unknown_11", "int"),
            (self._dependencies_for_unknown_12, "unknown_12", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Thardus.{field_name} ({field_type}): {e}")
