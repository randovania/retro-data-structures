# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ElectroMagneticPulseJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        active: bool
        initial_radius: float
        final_radius: float
        duration: float
        interference_dur: float
        unknown_0x00000008: float
        interference_mag: float
        unknown_0x0000000a: float
        particle: int


@dataclasses.dataclass()
class ElectroMagneticPulse(BaseObjectType):
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
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Active"),
        },
    )
    initial_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="InitialRadius"),
        },
    )
    final_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="FinalRadius"),
        },
    )
    duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Duration"),
        },
    )
    interference_dur: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="InterferenceDur"),
        },
    )
    unknown_0x00000008: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Unknown"),
        },
    )
    interference_mag: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="InterferenceMag"),
        },
    )
    unknown_0x0000000a: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="Unknown"),
        },
    )
    particle: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="Particle"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x4A

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        initial_radius = structs.BIG_f.unpack(data.read(4))[0]
        final_radius = structs.BIG_f.unpack(data.read(4))[0]
        duration = structs.BIG_f.unpack(data.read(4))[0]
        interference_dur = structs.BIG_f.unpack(data.read(4))[0]
        unknown_0x00000008 = structs.BIG_f.unpack(data.read(4))[0]
        interference_mag = structs.BIG_f.unpack(data.read(4))[0]
        unknown_0x0000000a = structs.BIG_f.unpack(data.read(4))[0]
        particle = structs.BIG_L.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            active,
            initial_radius,
            final_radius,
            duration,
            interference_dur,
            unknown_0x00000008,
            interference_mag,
            unknown_0x0000000a,
            particle,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0c")  # 12 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.initial_radius))
        data.write(structs.BIG_f.pack(self.final_radius))
        data.write(structs.BIG_f.pack(self.duration))
        data.write(structs.BIG_f.pack(self.interference_dur))
        data.write(structs.BIG_f.pack(self.unknown_0x00000008))
        data.write(structs.BIG_f.pack(self.interference_mag))
        data.write(structs.BIG_f.pack(self.unknown_0x0000000a))
        data.write(structs.BIG_L.pack(self.particle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ElectroMagneticPulseJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            active=json_data["active"],
            initial_radius=json_data["initial_radius"],
            final_radius=json_data["final_radius"],
            duration=json_data["duration"],
            interference_dur=json_data["interference_dur"],
            unknown_0x00000008=json_data["unknown_0x00000008"],
            interference_mag=json_data["interference_mag"],
            unknown_0x0000000a=json_data["unknown_0x0000000a"],
            particle=json_data["particle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "active": self.active,
            "initial_radius": self.initial_radius,
            "final_radius": self.final_radius,
            "duration": self.duration,
            "interference_dur": self.interference_dur,
            "unknown_0x00000008": self.unknown_0x00000008,
            "interference_mag": self.interference_mag,
            "unknown_0x0000000a": self.unknown_0x0000000a,
            "particle": self.particle,
        }

    def _dependencies_for_particle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_particle(asset_manager)
