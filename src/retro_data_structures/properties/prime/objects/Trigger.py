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
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TriggerJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed: json_util.JsonObject
        force: json_util.JsonValue
        flags: int
        active: bool
        deactivate_on_entered: bool
        deactivate_on_exited: bool


class Flags(enum.IntFlag):
    PendingAmbush = 1
    CeilingAmbush = 2
    NonAggressive = 4
    Melee = 8
    NoShuffleCloseCheck = 16
    OnlyAttackInRange = 32
    Unknown = 64
    NoKnockbackImpulseReset = 128
    NoMeleeAttack = 512
    BreakAttack = 1024
    Seated = 4096
    ShadowPirate = 8192
    AlertBeforeCloak = 16384
    NoBreakDamage = 32768
    FloatingCorpse = 65536
    RagdollNoAiCollision = 131072
    Trooper = 262144

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
class Trigger(BaseObjectType):
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
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unnamed: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo, id=0x00000003, original_name="3", from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
            ),
        },
    )
    force: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="Force", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    flags: Flags = dataclasses.field(
        default=Flags(0),
        metadata={
            "reflection": FieldReflection[Flags](
                Flags, id=0x00000005, original_name="Flags", from_json=Flags.from_json, to_json=Flags.to_json
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="Active"),
        },
    )
    deactivate_on_entered: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="DeactivateOnEntered"),
        },
    )
    deactivate_on_exited: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="DeactivateOnExited"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x4

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed = DamageInfo.from_stream(data, game, property_size)
        force = Vector.from_stream(data, game, property_size)
        flags = Flags.from_stream(data, game)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        deactivate_on_entered = structs.BIG_bool_.unpack(data.read(1))[0]
        deactivate_on_exited = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, position, scale, unnamed, force, flags, active, deactivate_on_entered, deactivate_on_exited)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\t")  # 9 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed.to_stream(data, game)
        self.force.to_stream(data, game)
        self.flags.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_bool_.pack(self.deactivate_on_entered))
        data.write(structs.BIG_bool_.pack(self.deactivate_on_exited))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TriggerJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed=DamageInfo.from_json(json_data["unnamed"]),
            force=Vector.from_json(json_data["force"]),
            flags=Flags.from_json(json_data["flags"]),
            active=json_data["active"],
            deactivate_on_entered=json_data["deactivate_on_entered"],
            deactivate_on_exited=json_data["deactivate_on_exited"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "scale": self.scale.to_json(),
            "unnamed": self.unnamed.to_json(),
            "force": self.force.to_json(),
            "flags": self.flags.to_json(),
            "active": self.active,
            "deactivate_on_entered": self.deactivate_on_entered,
            "deactivate_on_exited": self.deactivate_on_exited,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
