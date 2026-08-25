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
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.PlayerActorStruct import PlayerActorStruct
from retro_data_structures.properties.corruption.archetypes.ShadowProjection import ShadowProjection
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PlayerActorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        mass: float
        gravity: float
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        no_model: int
        animation: json_util.JsonObject
        actor_information: json_util.JsonObject
        is_loop: bool
        immovable: bool
        is_solid: bool
        empty_suit_model: int
        empty_suit_skin_rule: int
        varia_suit_model: int
        varia_suit_skin_rule: int
        varia_suit_grapple_model: int
        varia_suit_grapple_skin_rule: int
        stage01_suit_model: int
        stage01_skin_rule: int
        stage02_suit_model: int
        stage02_skin_rule: int
        stage03_suit_model: int
        stage03_skin_rule: int
        stage03_acid_model: int
        stage03_acid_rule: int
        stage04_suit_model: int
        stage04_skin_rule: int
        player_actor_struct_0x1098d091: json_util.JsonObject
        player_actor_struct_0xc7385390: json_util.JsonObject
        flags_player_actor: int
        render_gun_override: int
        unknown_struct510: json_util.JsonObject


@dataclasses.dataclass()
class PlayerActor(BaseObjectType):
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
    collision_box: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xF344C0B0, original_name="CollisionBox", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x2E686C2A,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    mass: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75DBB375, original_name="Mass"),
        },
    )
    gravity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2F2AE3E5, original_name="Gravity"),
        },
    )
    health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xCF90D15E,
                original_name="Health",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x7B71AE90,
                original_name="Vulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    no_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x405E5286, original_name="NoModel"),
        },
    )
    animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xA3D63F44,
                original_name="Animation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
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
    is_loop: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC08D1B93, original_name="IsLoop"),
        },
    )
    immovable: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1E32523E, original_name="Immovable"),
        },
    )
    is_solid: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1D8DD846, original_name="IsSolid"),
        },
    )
    empty_suit_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x846397A8, original_name="EmptySuitModel"),
        },
    )
    empty_suit_skin_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x685A4C01, original_name="EmptySuitSkinRule"),
        },
    )
    varia_suit_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9834ECC9, original_name="VariaSuitModel"),
        },
    )
    varia_suit_skin_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x188B8960, original_name="VariaSuitSkinRule"),
        },
    )
    varia_suit_grapple_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x134A81E3, original_name="VariaSuitGrappleModel"),
        },
    )
    varia_suit_grapple_skin_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4ABF030C, original_name="VariaSuitGrappleSkinRule"),
        },
    )
    stage01_suit_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9BF030DC, original_name="Stage01SuitModel"),
        },
    )
    stage01_skin_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x981263D3, original_name="Stage01SkinRule"),
        },
    )
    stage02_suit_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8A8D5AA5, original_name="Stage02SuitModel"),
        },
    )
    stage02_skin_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE4734608, original_name="Stage02SkinRule"),
        },
    )
    stage03_suit_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3376814D, original_name="Stage03SuitModel"),
        },
    )
    stage03_skin_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x797CA77E, original_name="Stage03SkinRule"),
        },
    )
    stage03_acid_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0EBEC440, original_name="Stage03AcidModel"),
        },
    )
    stage03_acid_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBC0952D8, original_name="Stage03AcidRule"),
        },
    )
    stage04_suit_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA8778E57, original_name="Stage04SuitModel"),
        },
    )
    stage04_skin_rule: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1CB10DBE, original_name="Stage04SkinRule"),
        },
    )
    player_actor_struct_0x1098d091: PlayerActorStruct = dataclasses.field(
        default_factory=PlayerActorStruct,
        metadata={
            "reflection": FieldReflection[PlayerActorStruct](
                PlayerActorStruct,
                id=0x1098D091,
                original_name="PlayerActorStruct",
                from_json=PlayerActorStruct.from_json,
                to_json=PlayerActorStruct.to_json,
            ),
        },
    )
    player_actor_struct_0xc7385390: PlayerActorStruct = dataclasses.field(
        default_factory=PlayerActorStruct,
        metadata={
            "reflection": FieldReflection[PlayerActorStruct](
                PlayerActorStruct,
                id=0xC7385390,
                original_name="PlayerActorStruct",
                from_json=PlayerActorStruct.from_json,
                to_json=PlayerActorStruct.to_json,
            ),
        },
    )
    flags_player_actor: int = dataclasses.field(
        default=16388,
        metadata={
            "reflection": FieldReflection[int](int, id=0x33507998, original_name="FlagsPlayerActor"),
        },
    )  # Flagset
    render_gun_override: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB6832840, original_name="RenderGunOverride"),
        },
    )
    unknown_struct510: ShadowProjection = dataclasses.field(
        default_factory=ShadowProjection,
        metadata={
            "reflection": FieldReflection[ShadowProjection](
                ShadowProjection,
                id=0xA21B515A,
                original_name="UnknownStruct510",
                from_json=ShadowProjection.from_json,
                to_json=ShadowProjection.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PLAC"

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
        if property_count != 34:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF344C0B0
        collision_box = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E686C2A
        collision_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75DBB375
        mass = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F2AE3E5
        gravity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x405E5286
        no_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3D63F44
        animation = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC08D1B93
        is_loop = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E32523E
        immovable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D8DD846
        is_solid = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x846397A8
        empty_suit_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x685A4C01
        empty_suit_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9834ECC9
        varia_suit_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x188B8960
        varia_suit_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x134A81E3
        varia_suit_grapple_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ABF030C
        varia_suit_grapple_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9BF030DC
        stage01_suit_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x981263D3
        stage01_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A8D5AA5
        stage02_suit_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE4734608
        stage02_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3376814D
        stage03_suit_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x797CA77E
        stage03_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0EBEC440
        stage03_acid_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC0952D8
        stage03_acid_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA8778E57
        stage04_suit_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CB10DBE
        stage04_skin_rule = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1098D091
        player_actor_struct_0x1098d091 = PlayerActorStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7385390
        player_actor_struct_0xc7385390 = PlayerActorStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33507998
        flags_player_actor = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6832840
        render_gun_override = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA21B515A
        unknown_struct510 = ShadowProjection.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            collision_box,
            collision_offset,
            mass,
            gravity,
            health,
            vulnerability,
            no_model,
            animation,
            actor_information,
            is_loop,
            immovable,
            is_solid,
            empty_suit_model,
            empty_suit_skin_rule,
            varia_suit_model,
            varia_suit_skin_rule,
            varia_suit_grapple_model,
            varia_suit_grapple_skin_rule,
            stage01_suit_model,
            stage01_skin_rule,
            stage02_suit_model,
            stage02_skin_rule,
            stage03_suit_model,
            stage03_skin_rule,
            stage03_acid_model,
            stage03_acid_rule,
            stage04_suit_model,
            stage04_skin_rule,
            player_actor_struct_0x1098d091,
            player_actor_struct_0xc7385390,
            flags_player_actor,
            render_gun_override,
            unknown_struct510,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b'\x00"')  # 34 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3D\xc0\xb0")  # 0xf344c0b0
        data.write(b"\x00\x0c")  # size
        self.collision_box.to_stream(data, game)

        data.write(b".hl*")  # 0x2e686c2a
        data.write(b"\x00\x0c")  # size
        self.collision_offset.to_stream(data, game)

        data.write(b"u\xdb\xb3u")  # 0x75dbb375
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mass))

        data.write(b"/*\xe3\xe5")  # 0x2f2ae3e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity))

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{q\xae\x90")  # 0x7b71ae90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"@^R\x86")  # 0x405e5286
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.no_model))

        data.write(b"\xa3\xd6?D")  # 0xa3d63f44
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation.to_stream(data, game)
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

        data.write(b"\xc0\x8d\x1b\x93")  # 0xc08d1b93
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_loop))

        data.write(b"\x1e2R>")  # 0x1e32523e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.immovable))

        data.write(b"\x1d\x8d\xd8F")  # 0x1d8dd846
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_solid))

        data.write(b"\x84c\x97\xa8")  # 0x846397a8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.empty_suit_model))

        data.write(b"hZL\x01")  # 0x685a4c01
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.empty_suit_skin_rule))

        data.write(b"\x984\xec\xc9")  # 0x9834ecc9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_model))

        data.write(b"\x18\x8b\x89`")  # 0x188b8960
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_skin_rule))

        data.write(b"\x13J\x81\xe3")  # 0x134a81e3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_grapple_model))

        data.write(b"J\xbf\x03\x0c")  # 0x4abf030c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.varia_suit_grapple_skin_rule))

        data.write(b"\x9b\xf00\xdc")  # 0x9bf030dc
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage01_suit_model))

        data.write(b"\x98\x12c\xd3")  # 0x981263d3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage01_skin_rule))

        data.write(b"\x8a\x8dZ\xa5")  # 0x8a8d5aa5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage02_suit_model))

        data.write(b"\xe4sF\x08")  # 0xe4734608
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage02_skin_rule))

        data.write(b"3v\x81M")  # 0x3376814d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage03_suit_model))

        data.write(b"y|\xa7~")  # 0x797ca77e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage03_skin_rule))

        data.write(b"\x0e\xbe\xc4@")  # 0xebec440
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage03_acid_model))

        data.write(b"\xbc\tR\xd8")  # 0xbc0952d8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage03_acid_rule))

        data.write(b"\xa8w\x8eW")  # 0xa8778e57
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage04_suit_model))

        data.write(b"\x1c\xb1\r\xbe")  # 0x1cb10dbe
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stage04_skin_rule))

        data.write(b"\x10\x98\xd0\x91")  # 0x1098d091
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.player_actor_struct_0x1098d091.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc78S\x90")  # 0xc7385390
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.player_actor_struct_0xc7385390.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3Py\x98")  # 0x33507998
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_player_actor))

        data.write(b"\xb6\x83(@")  # 0xb6832840
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.render_gun_override))

        data.write(b"\xa2\x1bQZ")  # 0xa21b515a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct510.to_stream(data, game)
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
        json_data = typing.cast("PlayerActorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            mass=json_data["mass"],
            gravity=json_data["gravity"],
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            no_model=json_data["no_model"],
            animation=AnimationParameters.from_json(json_data["animation"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            is_loop=json_data["is_loop"],
            immovable=json_data["immovable"],
            is_solid=json_data["is_solid"],
            empty_suit_model=json_data["empty_suit_model"],
            empty_suit_skin_rule=json_data["empty_suit_skin_rule"],
            varia_suit_model=json_data["varia_suit_model"],
            varia_suit_skin_rule=json_data["varia_suit_skin_rule"],
            varia_suit_grapple_model=json_data["varia_suit_grapple_model"],
            varia_suit_grapple_skin_rule=json_data["varia_suit_grapple_skin_rule"],
            stage01_suit_model=json_data["stage01_suit_model"],
            stage01_skin_rule=json_data["stage01_skin_rule"],
            stage02_suit_model=json_data["stage02_suit_model"],
            stage02_skin_rule=json_data["stage02_skin_rule"],
            stage03_suit_model=json_data["stage03_suit_model"],
            stage03_skin_rule=json_data["stage03_skin_rule"],
            stage03_acid_model=json_data["stage03_acid_model"],
            stage03_acid_rule=json_data["stage03_acid_rule"],
            stage04_suit_model=json_data["stage04_suit_model"],
            stage04_skin_rule=json_data["stage04_skin_rule"],
            player_actor_struct_0x1098d091=PlayerActorStruct.from_json(json_data["player_actor_struct_0x1098d091"]),
            player_actor_struct_0xc7385390=PlayerActorStruct.from_json(json_data["player_actor_struct_0xc7385390"]),
            flags_player_actor=json_data["flags_player_actor"],
            render_gun_override=json_data["render_gun_override"],
            unknown_struct510=ShadowProjection.from_json(json_data["unknown_struct510"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "mass": self.mass,
            "gravity": self.gravity,
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "no_model": self.no_model,
            "animation": self.animation.to_json(),
            "actor_information": self.actor_information.to_json(),
            "is_loop": self.is_loop,
            "immovable": self.immovable,
            "is_solid": self.is_solid,
            "empty_suit_model": self.empty_suit_model,
            "empty_suit_skin_rule": self.empty_suit_skin_rule,
            "varia_suit_model": self.varia_suit_model,
            "varia_suit_skin_rule": self.varia_suit_skin_rule,
            "varia_suit_grapple_model": self.varia_suit_grapple_model,
            "varia_suit_grapple_skin_rule": self.varia_suit_grapple_skin_rule,
            "stage01_suit_model": self.stage01_suit_model,
            "stage01_skin_rule": self.stage01_skin_rule,
            "stage02_suit_model": self.stage02_suit_model,
            "stage02_skin_rule": self.stage02_skin_rule,
            "stage03_suit_model": self.stage03_suit_model,
            "stage03_skin_rule": self.stage03_skin_rule,
            "stage03_acid_model": self.stage03_acid_model,
            "stage03_acid_rule": self.stage03_acid_rule,
            "stage04_suit_model": self.stage04_suit_model,
            "stage04_skin_rule": self.stage04_skin_rule,
            "player_actor_struct_0x1098d091": self.player_actor_struct_0x1098d091.to_json(),
            "player_actor_struct_0xc7385390": self.player_actor_struct_0xc7385390.to_json(),
            "flags_player_actor": self.flags_player_actor,
            "render_gun_override": self.render_gun_override,
            "unknown_struct510": self.unknown_struct510.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_player_actor_struct_0x1098d091(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerActorStruct:
    return PlayerActorStruct.from_stream(data, game, property_size)


def _decode_player_actor_struct_0xc7385390(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerActorStruct:
    return PlayerActorStruct.from_stream(data, game, property_size)


def _decode_unknown_struct510(data: typing.BinaryIO, game: Game, property_size: int) -> ShadowProjection:
    return ShadowProjection.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xF344C0B0: ("collision_box", _decode_collision_box),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0x75DBB375: ("mass", structs.decode_BIG_f),
    0x2F2AE3E5: ("gravity", structs.decode_BIG_f),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0x405E5286: ("no_model", structs.decode_BIG_Q),
    0xA3D63F44: ("animation", _decode_animation),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xC08D1B93: ("is_loop", structs.decode_BIG_bool_),
    0x1E32523E: ("immovable", structs.decode_BIG_bool_),
    0x1D8DD846: ("is_solid", structs.decode_BIG_bool_),
    0x846397A8: ("empty_suit_model", structs.decode_BIG_Q),
    0x685A4C01: ("empty_suit_skin_rule", structs.decode_BIG_Q),
    0x9834ECC9: ("varia_suit_model", structs.decode_BIG_Q),
    0x188B8960: ("varia_suit_skin_rule", structs.decode_BIG_Q),
    0x134A81E3: ("varia_suit_grapple_model", structs.decode_BIG_Q),
    0x4ABF030C: ("varia_suit_grapple_skin_rule", structs.decode_BIG_Q),
    0x9BF030DC: ("stage01_suit_model", structs.decode_BIG_Q),
    0x981263D3: ("stage01_skin_rule", structs.decode_BIG_Q),
    0x8A8D5AA5: ("stage02_suit_model", structs.decode_BIG_Q),
    0xE4734608: ("stage02_skin_rule", structs.decode_BIG_Q),
    0x3376814D: ("stage03_suit_model", structs.decode_BIG_Q),
    0x797CA77E: ("stage03_skin_rule", structs.decode_BIG_Q),
    0x0EBEC440: ("stage03_acid_model", structs.decode_BIG_Q),
    0xBC0952D8: ("stage03_acid_rule", structs.decode_BIG_Q),
    0xA8778E57: ("stage04_suit_model", structs.decode_BIG_Q),
    0x1CB10DBE: ("stage04_skin_rule", structs.decode_BIG_Q),
    0x1098D091: ("player_actor_struct_0x1098d091", _decode_player_actor_struct_0x1098d091),
    0xC7385390: ("player_actor_struct_0xc7385390", _decode_player_actor_struct_0xc7385390),
    0x33507998: ("flags_player_actor", structs.decode_BIG_L),
    0xB6832840: ("render_gun_override", structs.decode_BIG_l),
    0xA21B515A: ("unknown_struct510", _decode_unknown_struct510),
}
