# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ScriptBeamStructJson(typing_extensions.TypedDict):
        beam_attributes: int
        contact_fx_id: int
        pulse_fx_id: int
        texture_id: int
        glow_texture_id: int
        length: float
        radius: float
        expansion_speed: float
        lifetime: float
        pulse_speed: float
        shutdown_time: float
        contact_fx_scale: float
        pulse_fx_scale: float
        travel_speed: float
        inner_color: json_util.JsonValue
        outer_color: json_util.JsonValue


class BeamAttributes(enum.IntEnum):
    MotionBlur = 0
    PulseEffect = 1
    OneShot = 2
    PhazonDamage = 3

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
class ScriptBeamStruct(BaseProperty):
    beam_attributes: BeamAttributes = dataclasses.field(
        default=BeamAttributes.MotionBlur,
        metadata={
            "reflection": FieldReflection[BeamAttributes](
                BeamAttributes,
                id=0x00000000,
                original_name="BeamAttributes",
                from_json=BeamAttributes.from_json,
                to_json=BeamAttributes.to_json,
            ),
        },
    )
    contact_fx_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000001, original_name="ContactFxID"),
        },
    )
    pulse_fx_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000002, original_name="PulseFxID"),
        },
    )
    texture_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000003, original_name="TextureID"),
        },
    )
    glow_texture_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000004, original_name="GlowTextureID"),
        },
    )
    length: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Length"),
        },
    )
    radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Radius"),
        },
    )
    expansion_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="ExpansionSpeed"),
        },
    )
    lifetime: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Lifetime"),
        },
    )
    pulse_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="PulseSpeed"),
        },
    )
    shutdown_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="ShutdownTime"),
        },
    )
    contact_fx_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="ContactFXScale"),
        },
    )
    pulse_fx_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="PulseFxScale"),
        },
    )
    travel_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="TravelSpeed"),
        },
    )
    inner_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0000000E, original_name="InnerColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    outer_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0000000F, original_name="OuterColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        beam_attributes = BeamAttributes.from_stream(data, game)
        contact_fx_id = structs.BIG_L.unpack(data.read(4))[0]
        pulse_fx_id = structs.BIG_L.unpack(data.read(4))[0]
        texture_id = structs.BIG_L.unpack(data.read(4))[0]
        glow_texture_id = structs.BIG_L.unpack(data.read(4))[0]
        length = structs.BIG_f.unpack(data.read(4))[0]
        radius = structs.BIG_f.unpack(data.read(4))[0]
        expansion_speed = structs.BIG_f.unpack(data.read(4))[0]
        lifetime = structs.BIG_f.unpack(data.read(4))[0]
        pulse_speed = structs.BIG_f.unpack(data.read(4))[0]
        shutdown_time = structs.BIG_f.unpack(data.read(4))[0]
        contact_fx_scale = structs.BIG_f.unpack(data.read(4))[0]
        pulse_fx_scale = structs.BIG_f.unpack(data.read(4))[0]
        travel_speed = structs.BIG_f.unpack(data.read(4))[0]
        inner_color = Color.from_stream(data, game, property_size)
        outer_color = Color.from_stream(data, game, property_size)
        return cls(
            beam_attributes,
            contact_fx_id,
            pulse_fx_id,
            texture_id,
            glow_texture_id,
            length,
            radius,
            expansion_speed,
            lifetime,
            pulse_speed,
            shutdown_time,
            contact_fx_scale,
            pulse_fx_scale,
            travel_speed,
            inner_color,
            outer_color,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        self.beam_attributes.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.contact_fx_id))
        data.write(structs.BIG_L.pack(self.pulse_fx_id))
        data.write(structs.BIG_L.pack(self.texture_id))
        data.write(structs.BIG_L.pack(self.glow_texture_id))
        data.write(structs.BIG_f.pack(self.length))
        data.write(structs.BIG_f.pack(self.radius))
        data.write(structs.BIG_f.pack(self.expansion_speed))
        data.write(structs.BIG_f.pack(self.lifetime))
        data.write(structs.BIG_f.pack(self.pulse_speed))
        data.write(structs.BIG_f.pack(self.shutdown_time))
        data.write(structs.BIG_f.pack(self.contact_fx_scale))
        data.write(structs.BIG_f.pack(self.pulse_fx_scale))
        data.write(structs.BIG_f.pack(self.travel_speed))
        self.inner_color.to_stream(data, game)
        self.outer_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ScriptBeamStructJson", data)
        return cls(
            beam_attributes=BeamAttributes.from_json(json_data["beam_attributes"]),
            contact_fx_id=json_data["contact_fx_id"],
            pulse_fx_id=json_data["pulse_fx_id"],
            texture_id=json_data["texture_id"],
            glow_texture_id=json_data["glow_texture_id"],
            length=json_data["length"],
            radius=json_data["radius"],
            expansion_speed=json_data["expansion_speed"],
            lifetime=json_data["lifetime"],
            pulse_speed=json_data["pulse_speed"],
            shutdown_time=json_data["shutdown_time"],
            contact_fx_scale=json_data["contact_fx_scale"],
            pulse_fx_scale=json_data["pulse_fx_scale"],
            travel_speed=json_data["travel_speed"],
            inner_color=Color.from_json(json_data["inner_color"]),
            outer_color=Color.from_json(json_data["outer_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "beam_attributes": self.beam_attributes.to_json(),
            "contact_fx_id": self.contact_fx_id,
            "pulse_fx_id": self.pulse_fx_id,
            "texture_id": self.texture_id,
            "glow_texture_id": self.glow_texture_id,
            "length": self.length,
            "radius": self.radius,
            "expansion_speed": self.expansion_speed,
            "lifetime": self.lifetime,
            "pulse_speed": self.pulse_speed,
            "shutdown_time": self.shutdown_time,
            "contact_fx_scale": self.contact_fx_scale,
            "pulse_fx_scale": self.pulse_fx_scale,
            "travel_speed": self.travel_speed,
            "inner_color": self.inner_color.to_json(),
            "outer_color": self.outer_color.to_json(),
        }

    def _dependencies_for_contact_fx_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.contact_fx_id)

    def _dependencies_for_pulse_fx_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pulse_fx_id)

    def _dependencies_for_texture_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture_id)

    def _dependencies_for_glow_texture_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.glow_texture_id)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_contact_fx_id, "contact_fx_id", "AssetId"),
            (self._dependencies_for_pulse_fx_id, "pulse_fx_id", "AssetId"),
            (self._dependencies_for_texture_id, "texture_id", "AssetId"),
            (self._dependencies_for_glow_texture_id, "glow_texture_id", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ScriptBeamStruct.{field_name} ({field_type}): {e}")
