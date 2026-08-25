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
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class EyeballJson(typing_extensions.TypedDict):
        name: str
        flavor: int
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000005: json_util.JsonObject
        unnamed_0x00000006: json_util.JsonObject
        attack_delay: float
        attack_start_time: float
        wpsc: int
        unnamed_0x0000000a: json_util.JsonObject
        beam_contact_fxid: int
        beam_pulse_fxid: int
        beam_texture_id: int
        beam_glow_texture_id: int
        anim0: int
        anim1: int
        anim2: int
        anim3: int
        beam_sfx: int
        attack_disabled: bool


@dataclasses.dataclass()
class Eyeball(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    flavor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Flavor"),
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
    attack_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="AttackDelay"),
        },
    )
    attack_start_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="AttackStartTime"),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="WPSC"),
        },
    )
    unnamed_0x0000000a: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000A,
                original_name="10",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    beam_contact_fxid: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="BeamContactFXID"),
        },
    )
    beam_pulse_fxid: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="BeamPulseFXID"),
        },
    )
    beam_texture_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="BeamTextureID"),
        },
    )
    beam_glow_texture_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000E, original_name="BeamGlowTextureID"),
        },
    )
    anim0: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000F, original_name="Anim0"),
        },
    )
    anim1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000010, original_name="Anim1"),
        },
    )
    anim2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000011, original_name="Anim2"),
        },
    )
    anim3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000012, original_name="Anim3"),
        },
    )
    beam_sfx: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000013, original_name="BeamSFX"),
        },
    )
    attack_disabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000014, original_name="AttackDisabled"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x67

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        flavor = structs.BIG_l.unpack(data.read(4))[0]
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000005 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000006 = ActorParameters.from_stream(data, game, property_size)
        attack_delay = structs.BIG_f.unpack(data.read(4))[0]
        attack_start_time = structs.BIG_f.unpack(data.read(4))[0]
        wpsc = structs.BIG_L.unpack(data.read(4))[0]
        unnamed_0x0000000a = DamageInfo.from_stream(data, game, property_size)
        beam_contact_fxid = structs.BIG_L.unpack(data.read(4))[0]
        beam_pulse_fxid = structs.BIG_L.unpack(data.read(4))[0]
        beam_texture_id = structs.BIG_L.unpack(data.read(4))[0]
        beam_glow_texture_id = structs.BIG_L.unpack(data.read(4))[0]
        anim0 = structs.BIG_l.unpack(data.read(4))[0]
        anim1 = structs.BIG_l.unpack(data.read(4))[0]
        anim2 = structs.BIG_l.unpack(data.read(4))[0]
        anim3 = structs.BIG_l.unpack(data.read(4))[0]
        beam_sfx = structs.BIG_l.unpack(data.read(4))[0]
        attack_disabled = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            flavor,
            position,
            rotation,
            scale,
            unnamed_0x00000005,
            unnamed_0x00000006,
            attack_delay,
            attack_start_time,
            wpsc,
            unnamed_0x0000000a,
            beam_contact_fxid,
            beam_pulse_fxid,
            beam_texture_id,
            beam_glow_texture_id,
            anim0,
            anim1,
            anim2,
            anim3,
            beam_sfx,
            attack_disabled,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x15")  # 21 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.flavor))
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        self.unnamed_0x00000006.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.attack_delay))
        data.write(structs.BIG_f.pack(self.attack_start_time))
        data.write(structs.BIG_L.pack(self.wpsc))
        self.unnamed_0x0000000a.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.beam_contact_fxid))
        data.write(structs.BIG_L.pack(self.beam_pulse_fxid))
        data.write(structs.BIG_L.pack(self.beam_texture_id))
        data.write(structs.BIG_L.pack(self.beam_glow_texture_id))
        data.write(structs.BIG_l.pack(self.anim0))
        data.write(structs.BIG_l.pack(self.anim1))
        data.write(structs.BIG_l.pack(self.anim2))
        data.write(structs.BIG_l.pack(self.anim3))
        data.write(structs.BIG_l.pack(self.beam_sfx))
        data.write(structs.BIG_bool_.pack(self.attack_disabled))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EyeballJson", data)
        return cls(
            name=json_data["name"],
            flavor=json_data["flavor"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000005=PatternedAITypedef.from_json(json_data["unnamed_0x00000005"]),
            unnamed_0x00000006=ActorParameters.from_json(json_data["unnamed_0x00000006"]),
            attack_delay=json_data["attack_delay"],
            attack_start_time=json_data["attack_start_time"],
            wpsc=json_data["wpsc"],
            unnamed_0x0000000a=DamageInfo.from_json(json_data["unnamed_0x0000000a"]),
            beam_contact_fxid=json_data["beam_contact_fxid"],
            beam_pulse_fxid=json_data["beam_pulse_fxid"],
            beam_texture_id=json_data["beam_texture_id"],
            beam_glow_texture_id=json_data["beam_glow_texture_id"],
            anim0=json_data["anim0"],
            anim1=json_data["anim1"],
            anim2=json_data["anim2"],
            anim3=json_data["anim3"],
            beam_sfx=json_data["beam_sfx"],
            attack_disabled=json_data["attack_disabled"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "flavor": self.flavor,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "unnamed_0x00000006": self.unnamed_0x00000006.to_json(),
            "attack_delay": self.attack_delay,
            "attack_start_time": self.attack_start_time,
            "wpsc": self.wpsc,
            "unnamed_0x0000000a": self.unnamed_0x0000000a.to_json(),
            "beam_contact_fxid": self.beam_contact_fxid,
            "beam_pulse_fxid": self.beam_pulse_fxid,
            "beam_texture_id": self.beam_texture_id,
            "beam_glow_texture_id": self.beam_glow_texture_id,
            "anim0": self.anim0,
            "anim1": self.anim1,
            "anim2": self.anim2,
            "anim3": self.anim3,
            "beam_sfx": self.beam_sfx,
            "attack_disabled": self.attack_disabled,
        }

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def _dependencies_for_beam_contact_fxid(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.beam_contact_fxid)

    def _dependencies_for_beam_pulse_fxid(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.beam_pulse_fxid)

    def _dependencies_for_beam_texture_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.beam_texture_id)

    def _dependencies_for_beam_glow_texture_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.beam_glow_texture_id)

    def _dependencies_for_beam_sfx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.beam_sfx)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "PatternedAITypedef"),
            (self.unnamed_0x00000006.dependencies_for, "unnamed_0x00000006", "ActorParameters"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self._dependencies_for_beam_contact_fxid, "beam_contact_fxid", "AssetId"),
            (self._dependencies_for_beam_pulse_fxid, "beam_pulse_fxid", "AssetId"),
            (self._dependencies_for_beam_texture_id, "beam_texture_id", "AssetId"),
            (self._dependencies_for_beam_glow_texture_id, "beam_glow_texture_id", "AssetId"),
            (self._dependencies_for_beam_sfx, "beam_sfx", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Eyeball.{field_name} ({field_type}): {e}")
