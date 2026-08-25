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
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class IceZoomerJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        advance_wp_radius: float
        unknown_2: float
        align_angle_vel: float
        unknown_4: float
        player_obstruction_min_dist: float
        move_foward_weight_: float
        model_res: int
        skin_res: int
        unnamed_0x0000000e: json_util.JsonObject
        ice_zoomer_joint_hp: float


@dataclasses.dataclass()
class IceZoomer(BaseObjectType):
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
    advance_wp_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="AdvanceWpRadius"),
        },
    )
    unknown_2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Unknown 2"),
        },
    )
    align_angle_vel: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="AlignAngleVel"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unknown 4"),
        },
    )
    player_obstruction_min_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="PlayerObstructionMinDist"),
        },
    )
    move_foward_weight_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="MoveFowardWeight "),
        },
    )
    model_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="ModelRes"),
        },
    )
    skin_res: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="SkinRes"),
        },
    )
    unnamed_0x0000000e: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000E,
                original_name="14",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    ice_zoomer_joint_hp: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="IceZoomerJointHP"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x78

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
        advance_wp_radius = structs.BIG_f.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        align_angle_vel = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        player_obstruction_min_dist = structs.BIG_f.unpack(data.read(4))[0]
        move_foward_weight_ = structs.BIG_f.unpack(data.read(4))[0]
        model_res = structs.BIG_L.unpack(data.read(4))[0]
        skin_res = structs.BIG_L.unpack(data.read(4))[0]
        unnamed_0x0000000e = DamageVulnerability.from_stream(data, game, property_size)
        ice_zoomer_joint_hp = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            advance_wp_radius,
            unknown_2,
            align_angle_vel,
            unknown_4,
            player_obstruction_min_dist,
            move_foward_weight_,
            model_res,
            skin_res,
            unnamed_0x0000000e,
            ice_zoomer_joint_hp,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x10")  # 16 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.advance_wp_radius))
        data.write(structs.BIG_f.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.align_angle_vel))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.player_obstruction_min_dist))
        data.write(structs.BIG_f.pack(self.move_foward_weight_))
        data.write(structs.BIG_L.pack(self.model_res))
        data.write(structs.BIG_L.pack(self.skin_res))
        self.unnamed_0x0000000e.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.ice_zoomer_joint_hp))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("IceZoomerJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            advance_wp_radius=json_data["advance_wp_radius"],
            unknown_2=json_data["unknown_2"],
            align_angle_vel=json_data["align_angle_vel"],
            unknown_4=json_data["unknown_4"],
            player_obstruction_min_dist=json_data["player_obstruction_min_dist"],
            move_foward_weight_=json_data["move_foward_weight_"],
            model_res=json_data["model_res"],
            skin_res=json_data["skin_res"],
            unnamed_0x0000000e=DamageVulnerability.from_json(json_data["unnamed_0x0000000e"]),
            ice_zoomer_joint_hp=json_data["ice_zoomer_joint_hp"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "advance_wp_radius": self.advance_wp_radius,
            "unknown_2": self.unknown_2,
            "align_angle_vel": self.align_angle_vel,
            "unknown_4": self.unknown_4,
            "player_obstruction_min_dist": self.player_obstruction_min_dist,
            "move_foward_weight_": self.move_foward_weight_,
            "model_res": self.model_res,
            "skin_res": self.skin_res,
            "unnamed_0x0000000e": self.unnamed_0x0000000e.to_json(),
            "ice_zoomer_joint_hp": self.ice_zoomer_joint_hp,
        }

    def _dependencies_for_model_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model_res)

    def _dependencies_for_skin_res(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.skin_res)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_model_res, "model_res", "AssetId"),
            (self._dependencies_for_skin_res, "skin_res", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for IceZoomer.{field_name} ({field_type}): {e}")
