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
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.prime.archetypes.VisorParameters import VisorParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DamageableTriggerJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000003: json_util.JsonObject
        unnamed_0x00000004: json_util.JsonObject
        render_side: int
        pattern_tex1: int
        pattern_tex2: int
        color_tex: int
        can_orbit: bool
        active: bool
        unnamed_0x0000000b: json_util.JsonObject


class RenderSide(enum.IntEnum):
    _None = 0
    North = 1
    South = 2
    West = 4
    East = 8
    Top = 16
    Bottom = 32

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
class DamageableTrigger(BaseObjectType):
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
    unnamed_0x00000003: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo, id=0x00000003, original_name="3", from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
            ),
        },
    )
    unnamed_0x00000004: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00000004,
                original_name="4",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    render_side: RenderSide = dataclasses.field(
        default=RenderSide._None,
        metadata={
            "reflection": FieldReflection[RenderSide](
                RenderSide,
                id=0x00000005,
                original_name="Render Side",
                from_json=RenderSide.from_json,
                to_json=RenderSide.to_json,
            ),
        },
    )
    pattern_tex1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000006, original_name="PatternTex1"),
        },
    )
    pattern_tex2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000007, original_name="PatternTex2"),
        },
    )
    color_tex: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="ColorTex"),
        },
    )
    can_orbit: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000009, original_name="CanOrbit"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="Active"),
        },
    )
    unnamed_0x0000000b: VisorParameters = dataclasses.field(
        default_factory=VisorParameters,
        metadata={
            "reflection": FieldReflection[VisorParameters](
                VisorParameters,
                id=0x0000000B,
                original_name="11",
                from_json=VisorParameters.from_json,
                to_json=VisorParameters.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x1A

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000003 = HealthInfo.from_stream(data, game, property_size)
        unnamed_0x00000004 = DamageVulnerability.from_stream(data, game, property_size)
        render_side = RenderSide.from_stream(data, game)
        pattern_tex1 = structs.BIG_L.unpack(data.read(4))[0]
        pattern_tex2 = structs.BIG_L.unpack(data.read(4))[0]
        color_tex = structs.BIG_L.unpack(data.read(4))[0]
        can_orbit = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        unnamed_0x0000000b = VisorParameters.from_stream(data, game, property_size)
        return cls(
            name,
            position,
            scale,
            unnamed_0x00000003,
            unnamed_0x00000004,
            render_side,
            pattern_tex1,
            pattern_tex2,
            color_tex,
            can_orbit,
            active,
            unnamed_0x0000000b,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0c")  # 12 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000003.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.render_side.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.pattern_tex1))
        data.write(structs.BIG_L.pack(self.pattern_tex2))
        data.write(structs.BIG_L.pack(self.color_tex))
        data.write(structs.BIG_bool_.pack(self.can_orbit))
        data.write(structs.BIG_bool_.pack(self.active))
        self.unnamed_0x0000000b.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DamageableTriggerJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000003=HealthInfo.from_json(json_data["unnamed_0x00000003"]),
            unnamed_0x00000004=DamageVulnerability.from_json(json_data["unnamed_0x00000004"]),
            render_side=RenderSide.from_json(json_data["render_side"]),
            pattern_tex1=json_data["pattern_tex1"],
            pattern_tex2=json_data["pattern_tex2"],
            color_tex=json_data["color_tex"],
            can_orbit=json_data["can_orbit"],
            active=json_data["active"],
            unnamed_0x0000000b=VisorParameters.from_json(json_data["unnamed_0x0000000b"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000003": self.unnamed_0x00000003.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "render_side": self.render_side.to_json(),
            "pattern_tex1": self.pattern_tex1,
            "pattern_tex2": self.pattern_tex2,
            "color_tex": self.color_tex,
            "can_orbit": self.can_orbit,
            "active": self.active,
            "unnamed_0x0000000b": self.unnamed_0x0000000b.to_json(),
        }

    def _dependencies_for_pattern_tex1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pattern_tex1)

    def _dependencies_for_pattern_tex2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pattern_tex2)

    def _dependencies_for_color_tex(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_tex)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_pattern_tex1, "pattern_tex1", "AssetId"),
            (self._dependencies_for_pattern_tex2, "pattern_tex2", "AssetId"),
            (self._dependencies_for_color_tex, "color_tex", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for DamageableTrigger.{field_name} ({field_type}): {e}")
