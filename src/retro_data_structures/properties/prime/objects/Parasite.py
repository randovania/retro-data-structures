# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ParasiteJson(typing_extensions.TypedDict):
        name: str
        flavor_type: int
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000005: json_util.JsonObject
        unnamed_0x00000006: json_util.JsonObject
        max_telegraph_react_dist: float
        advance_wp_radius: float
        unknown_1: float
        align_ang_vel: float
        unknown_2: float
        stuck_time_threshold: float
        collision_close_margin: float
        parasite_search_radius: float
        parasite_separation_dist: float
        parasite_separation_weight: float
        parasite_alignment_weight: float
        parasite_cohesion_weight: float
        destination_seek_weight: float
        forward_move_weight: float
        player_separation_dist: float
        player_separation_weight: float
        player_obstruction_min_dist: float
        disable_move: bool


class FlavorType(enum.IntEnum):
    Zero = 0
    One = 1
    Two = 2

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class Parasite(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    flavor_type: FlavorType = dataclasses.field(
        default=FlavorType.Zero,
        metadata={
            "reflection": FieldReflection[FlavorType](
                FlavorType,
                id=0x00000001,
                original_name="FlavorType",
                from_json=FlavorType.from_json,
                to_json=FlavorType.to_json,
            ),
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
    unnamed_0x00000005: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x00000005,
                original_name="5",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    unnamed_0x00000006: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000006,
                original_name="6",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    max_telegraph_react_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="MaxTelegraphReactDist"),
        },
    )
    advance_wp_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="AdvanceWpRadius"),
        },
    )
    unknown_1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unknown 1"),
        },
    )
    align_ang_vel: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="AlignAngVel"),
        },
    )
    unknown_2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="Unknown 2"),
        },
    )
    stuck_time_threshold: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="StuckTimeThreshold"),
        },
    )
    collision_close_margin: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="CollisionCloseMargin"),
        },
    )
    parasite_search_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="ParasiteSearchRadius"),
        },
    )
    parasite_separation_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="ParasiteSeparationDist"),
        },
    )
    parasite_separation_weight: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="ParasiteSeparationWeight"),
        },
    )
    parasite_alignment_weight: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="ParasiteAlignmentWeight"),
        },
    )
    parasite_cohesion_weight: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="ParasiteCohesionWeight"),
        },
    )
    destination_seek_weight: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="DestinationSeekWeight"),
        },
    )
    forward_move_weight: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="ForwardMoveWeight"),
        },
    )
    player_separation_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="PlayerSeparationDist"),
        },
    )
    player_separation_weight: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="PlayerSeparationWeight"),
        },
    )
    player_obstruction_min_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000017, original_name="PlayerObstructionMinDist"),
        },
    )
    disable_move: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000018, original_name="DisableMove"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x3D

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        flavor_type = FlavorType.from_stream(data, game)
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000005 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000006 = ActorParameters.from_stream(data, game, property_size)
        max_telegraph_react_dist = structs.BIG_f.unpack(data.read(4))[0]
        advance_wp_radius = structs.BIG_f.unpack(data.read(4))[0]
        unknown_1 = structs.BIG_f.unpack(data.read(4))[0]
        align_ang_vel = structs.BIG_f.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        stuck_time_threshold = structs.BIG_f.unpack(data.read(4))[0]
        collision_close_margin = structs.BIG_f.unpack(data.read(4))[0]
        parasite_search_radius = structs.BIG_f.unpack(data.read(4))[0]
        parasite_separation_dist = structs.BIG_f.unpack(data.read(4))[0]
        parasite_separation_weight = structs.BIG_f.unpack(data.read(4))[0]
        parasite_alignment_weight = structs.BIG_f.unpack(data.read(4))[0]
        parasite_cohesion_weight = structs.BIG_f.unpack(data.read(4))[0]
        destination_seek_weight = structs.BIG_f.unpack(data.read(4))[0]
        forward_move_weight = structs.BIG_f.unpack(data.read(4))[0]
        player_separation_dist = structs.BIG_f.unpack(data.read(4))[0]
        player_separation_weight = structs.BIG_f.unpack(data.read(4))[0]
        player_obstruction_min_dist = structs.BIG_f.unpack(data.read(4))[0]
        disable_move = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            flavor_type,
            position,
            rotation,
            scale,
            unnamed_0x00000005,
            unnamed_0x00000006,
            max_telegraph_react_dist,
            advance_wp_radius,
            unknown_1,
            align_ang_vel,
            unknown_2,
            stuck_time_threshold,
            collision_close_margin,
            parasite_search_radius,
            parasite_separation_dist,
            parasite_separation_weight,
            parasite_alignment_weight,
            parasite_cohesion_weight,
            destination_seek_weight,
            forward_move_weight,
            player_separation_dist,
            player_separation_weight,
            player_obstruction_min_dist,
            disable_move,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x19")  # 25 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.flavor_type.to_stream(data, game)
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        self.unnamed_0x00000006.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.max_telegraph_react_dist))
        data.write(structs.BIG_f.pack(self.advance_wp_radius))
        data.write(structs.BIG_f.pack(self.unknown_1))
        data.write(structs.BIG_f.pack(self.align_ang_vel))
        data.write(structs.BIG_f.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.stuck_time_threshold))
        data.write(structs.BIG_f.pack(self.collision_close_margin))
        data.write(structs.BIG_f.pack(self.parasite_search_radius))
        data.write(structs.BIG_f.pack(self.parasite_separation_dist))
        data.write(structs.BIG_f.pack(self.parasite_separation_weight))
        data.write(structs.BIG_f.pack(self.parasite_alignment_weight))
        data.write(structs.BIG_f.pack(self.parasite_cohesion_weight))
        data.write(structs.BIG_f.pack(self.destination_seek_weight))
        data.write(structs.BIG_f.pack(self.forward_move_weight))
        data.write(structs.BIG_f.pack(self.player_separation_dist))
        data.write(structs.BIG_f.pack(self.player_separation_weight))
        data.write(structs.BIG_f.pack(self.player_obstruction_min_dist))
        data.write(structs.BIG_bool_.pack(self.disable_move))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ParasiteJson", data)
        return cls(
            name=json_data["name"],
            flavor_type=FlavorType.from_json(json_data["flavor_type"]),
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000005=PatternedAITypedef.from_json(json_data["unnamed_0x00000005"]),
            unnamed_0x00000006=ActorParameters.from_json(json_data["unnamed_0x00000006"]),
            max_telegraph_react_dist=json_data["max_telegraph_react_dist"],
            advance_wp_radius=json_data["advance_wp_radius"],
            unknown_1=json_data["unknown_1"],
            align_ang_vel=json_data["align_ang_vel"],
            unknown_2=json_data["unknown_2"],
            stuck_time_threshold=json_data["stuck_time_threshold"],
            collision_close_margin=json_data["collision_close_margin"],
            parasite_search_radius=json_data["parasite_search_radius"],
            parasite_separation_dist=json_data["parasite_separation_dist"],
            parasite_separation_weight=json_data["parasite_separation_weight"],
            parasite_alignment_weight=json_data["parasite_alignment_weight"],
            parasite_cohesion_weight=json_data["parasite_cohesion_weight"],
            destination_seek_weight=json_data["destination_seek_weight"],
            forward_move_weight=json_data["forward_move_weight"],
            player_separation_dist=json_data["player_separation_dist"],
            player_separation_weight=json_data["player_separation_weight"],
            player_obstruction_min_dist=json_data["player_obstruction_min_dist"],
            disable_move=json_data["disable_move"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "flavor_type": self.flavor_type.to_json(),
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "unnamed_0x00000006": self.unnamed_0x00000006.to_json(),
            "max_telegraph_react_dist": self.max_telegraph_react_dist,
            "advance_wp_radius": self.advance_wp_radius,
            "unknown_1": self.unknown_1,
            "align_ang_vel": self.align_ang_vel,
            "unknown_2": self.unknown_2,
            "stuck_time_threshold": self.stuck_time_threshold,
            "collision_close_margin": self.collision_close_margin,
            "parasite_search_radius": self.parasite_search_radius,
            "parasite_separation_dist": self.parasite_separation_dist,
            "parasite_separation_weight": self.parasite_separation_weight,
            "parasite_alignment_weight": self.parasite_alignment_weight,
            "parasite_cohesion_weight": self.parasite_cohesion_weight,
            "destination_seek_weight": self.destination_seek_weight,
            "forward_move_weight": self.forward_move_weight,
            "player_separation_dist": self.player_separation_dist,
            "player_separation_weight": self.player_separation_weight,
            "player_obstruction_min_dist": self.player_obstruction_min_dist,
            "disable_move": self.disable_move,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "PatternedAITypedef"),
            (self.unnamed_0x00000006.dependencies_for, "unnamed_0x00000006", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Parasite.{field_name} ({field_type}): {e}")
