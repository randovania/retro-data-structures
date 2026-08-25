# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class FishCloudJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        active: bool
        fish_model: int
        animation_information: json_util.JsonObject
        fish_count: float
        speed: float
        influence_distance: float
        unknown_0x61959f0d: float
        alignment_priority: float
        separation_priority: float
        projectile_priority: float
        player_priority: float
        containment_priority: float
        wander_priority: float
        wander_amount: float
        player_ball_priority: float
        player_ball_distance: float
        projectile_decay_rate: float
        player_decay_rate: float
        look_ahead_time: float
        update_frame: int
        material_color: json_util.JsonValue
        can_be_killed: bool
        collision_radius: float
        death_effect0: int
        death_effect0_count: int
        death_effect1: int
        death_effect1_count: int
        death_effect2: int
        death_effect2_count: int
        death_effect3: int
        death_effect3_count: int
        death_sound: int
        unknown_0xc320a050: bool
        unknown_0xcd4c81a1: bool


@dataclasses.dataclass()
class FishCloud(BaseObjectType):
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
    active: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC6BB2F45, original_name="Active"),
        },
    )
    fish_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7990A3B6, original_name="FishModel"),
        },
    )
    animation_information: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xE25FB08C,
                original_name="AnimationInformation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    fish_count: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF1C07275, original_name="FishCount"),
        },
    )
    speed: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6392404E, original_name="Speed"),
        },
    )
    influence_distance: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7864AD0E, original_name="InfluenceDistance"),
        },
    )
    unknown_0x61959f0d: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x61959F0D, original_name="Unknown"),
        },
    )
    alignment_priority: float = dataclasses.field(
        default=0.8999999761581421,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4841F1DE, original_name="AlignmentPriority"),
        },
    )
    separation_priority: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD293EBC4, original_name="SeparationPriority"),
        },
    )
    projectile_priority: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5F362A14, original_name="ProjectilePriority"),
        },
    )
    player_priority: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC9B73C2, original_name="PlayerPriority"),
        },
    )
    containment_priority: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FF1469E, original_name="ContainmentPriority"),
        },
    )
    wander_priority: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7CE17870, original_name="WanderPriority"),
        },
    )
    wander_amount: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3A25F09D, original_name="WanderAmount"),
        },
    )
    player_ball_priority: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23A160F3, original_name="PlayerBallPriority"),
        },
    )
    player_ball_distance: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0671410, original_name="PlayerBallDistance"),
        },
    )
    projectile_decay_rate: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA1747268, original_name="ProjectileDecayRate"),
        },
    )
    player_decay_rate: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCE77A8D0, original_name="PlayerDecayRate"),
        },
    )
    look_ahead_time: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8CB20C53, original_name="LookAheadTime"),
        },
    )
    update_frame: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x21B3D07C, original_name="UpdateFrame"),
        },
    )
    material_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1F83D350, original_name="MaterialColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    can_be_killed: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF630B89F, original_name="CanBeKilled"),
        },
    )
    collision_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A6AB139, original_name="CollisionRadius"),
        },
    )
    death_effect0: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5BA86245, original_name="DeathEffect0"),
        },
    )
    death_effect0_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA8232FB1, original_name="DeathEffect0Count"),
        },
    )
    death_effect1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x90F4B1E0, original_name="DeathEffect1"),
        },
    )
    death_effect1_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBF583BF2, original_name="DeathEffect1Count"),
        },
    )
    death_effect2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1660C34E, original_name="DeathEffect2"),
        },
    )
    death_effect2_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x86D50737, original_name="DeathEffect2Count"),
        },
    )
    death_effect3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDD3C10EB, original_name="DeathEffect3"),
        },
    )
    death_effect3_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x91AE1374, original_name="DeathEffect3Count"),
        },
    )
    death_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x3DE26FC8, original_name="DeathSound"),
        },
    )
    unknown_0xc320a050: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC320A050, original_name="Unknown"),
        },
    )
    unknown_0xcd4c81a1: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCD4C81A1, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "FISH"

    @classmethod
    def modules(cls) -> list[str]:
        return ["FishCloud.rel"]

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
        if property_count != 35:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6BB2F45
        active = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7990A3B6
        fish_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1C07275
        fish_count = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404E
        speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7864AD0E
        influence_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61959F0D
        unknown_0x61959f0d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4841F1DE
        alignment_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD293EBC4
        separation_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F362A14
        projectile_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC9B73C2
        player_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FF1469E
        containment_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CE17870
        wander_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A25F09D
        wander_amount = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23A160F3
        player_ball_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0671410
        player_ball_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1747268
        projectile_decay_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE77A8D0
        player_decay_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8CB20C53
        look_ahead_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21B3D07C
        update_frame = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F83D350
        material_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF630B89F
        can_be_killed = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A6AB139
        collision_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BA86245
        death_effect0 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA8232FB1
        death_effect0_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90F4B1E0
        death_effect1 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF583BF2
        death_effect1_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1660C34E
        death_effect2 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86D50737
        death_effect2_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD3C10EB
        death_effect3 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91AE1374
        death_effect3_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DE26FC8
        death_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC320A050
        unknown_0xc320a050 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD4C81A1
        unknown_0xcd4c81a1 = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            active,
            fish_model,
            animation_information,
            fish_count,
            speed,
            influence_distance,
            unknown_0x61959f0d,
            alignment_priority,
            separation_priority,
            projectile_priority,
            player_priority,
            containment_priority,
            wander_priority,
            wander_amount,
            player_ball_priority,
            player_ball_distance,
            projectile_decay_rate,
            player_decay_rate,
            look_ahead_time,
            update_frame,
            material_color,
            can_be_killed,
            collision_radius,
            death_effect0,
            death_effect0_count,
            death_effect1,
            death_effect1_count,
            death_effect2,
            death_effect2_count,
            death_effect3,
            death_effect3_count,
            death_sound,
            unknown_0xc320a050,
            unknown_0xcd4c81a1,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00#")  # 35 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\xbb/E")  # 0xc6bb2f45
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.active))

        data.write(b"y\x90\xa3\xb6")  # 0x7990a3b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.fish_model))

        data.write(b"\xe2_\xb0\x8c")  # 0xe25fb08c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf1\xc0ru")  # 0xf1c07275
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fish_count))

        data.write(b"c\x92@N")  # 0x6392404e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b"xd\xad\x0e")  # 0x7864ad0e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.influence_distance))

        data.write(b"a\x95\x9f\r")  # 0x61959f0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x61959f0d))

        data.write(b"HA\xf1\xde")  # 0x4841f1de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alignment_priority))

        data.write(b"\xd2\x93\xeb\xc4")  # 0xd293ebc4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.separation_priority))

        data.write(b"_6*\x14")  # 0x5f362a14
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_priority))

        data.write(b"\xec\x9bs\xc2")  # 0xec9b73c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_priority))

        data.write(b"\x7f\xf1F\x9e")  # 0x7ff1469e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.containment_priority))

        data.write(b"|\xe1xp")  # 0x7ce17870
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.wander_priority))

        data.write(b":%\xf0\x9d")  # 0x3a25f09d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.wander_amount))

        data.write(b"#\xa1`\xf3")  # 0x23a160f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_ball_priority))

        data.write(b"\xf0g\x14\x10")  # 0xf0671410
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_ball_distance))

        data.write(b"\xa1trh")  # 0xa1747268
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_decay_rate))

        data.write(b"\xcew\xa8\xd0")  # 0xce77a8d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_decay_rate))

        data.write(b"\x8c\xb2\x0cS")  # 0x8cb20c53
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.look_ahead_time))

        data.write(b"!\xb3\xd0|")  # 0x21b3d07c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.update_frame))

        data.write(b"\x1f\x83\xd3P")  # 0x1f83d350
        data.write(b"\x00\x10")  # size
        self.material_color.to_stream(data, game)

        data.write(b"\xf60\xb8\x9f")  # 0xf630b89f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.can_be_killed))

        data.write(b"\x8aj\xb19")  # 0x8a6ab139
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.collision_radius))

        data.write(b"[\xa8bE")  # 0x5ba86245
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.death_effect0))

        data.write(b"\xa8#/\xb1")  # 0xa8232fb1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.death_effect0_count))

        data.write(b"\x90\xf4\xb1\xe0")  # 0x90f4b1e0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.death_effect1))

        data.write(b"\xbfX;\xf2")  # 0xbf583bf2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.death_effect1_count))

        data.write(b"\x16`\xc3N")  # 0x1660c34e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.death_effect2))

        data.write(b"\x86\xd5\x077")  # 0x86d50737
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.death_effect2_count))

        data.write(b"\xdd<\x10\xeb")  # 0xdd3c10eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.death_effect3))

        data.write(b"\x91\xae\x13t")  # 0x91ae1374
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.death_effect3_count))

        data.write(b"=\xe2o\xc8")  # 0x3de26fc8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.death_sound))

        data.write(b"\xc3 \xa0P")  # 0xc320a050
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xc320a050))

        data.write(b"\xcdL\x81\xa1")  # 0xcd4c81a1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xcd4c81a1))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FishCloudJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            active=json_data["active"],
            fish_model=json_data["fish_model"],
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            fish_count=json_data["fish_count"],
            speed=json_data["speed"],
            influence_distance=json_data["influence_distance"],
            unknown_0x61959f0d=json_data["unknown_0x61959f0d"],
            alignment_priority=json_data["alignment_priority"],
            separation_priority=json_data["separation_priority"],
            projectile_priority=json_data["projectile_priority"],
            player_priority=json_data["player_priority"],
            containment_priority=json_data["containment_priority"],
            wander_priority=json_data["wander_priority"],
            wander_amount=json_data["wander_amount"],
            player_ball_priority=json_data["player_ball_priority"],
            player_ball_distance=json_data["player_ball_distance"],
            projectile_decay_rate=json_data["projectile_decay_rate"],
            player_decay_rate=json_data["player_decay_rate"],
            look_ahead_time=json_data["look_ahead_time"],
            update_frame=json_data["update_frame"],
            material_color=Color.from_json(json_data["material_color"]),
            can_be_killed=json_data["can_be_killed"],
            collision_radius=json_data["collision_radius"],
            death_effect0=json_data["death_effect0"],
            death_effect0_count=json_data["death_effect0_count"],
            death_effect1=json_data["death_effect1"],
            death_effect1_count=json_data["death_effect1_count"],
            death_effect2=json_data["death_effect2"],
            death_effect2_count=json_data["death_effect2_count"],
            death_effect3=json_data["death_effect3"],
            death_effect3_count=json_data["death_effect3_count"],
            death_sound=json_data["death_sound"],
            unknown_0xc320a050=json_data["unknown_0xc320a050"],
            unknown_0xcd4c81a1=json_data["unknown_0xcd4c81a1"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "active": self.active,
            "fish_model": self.fish_model,
            "animation_information": self.animation_information.to_json(),
            "fish_count": self.fish_count,
            "speed": self.speed,
            "influence_distance": self.influence_distance,
            "unknown_0x61959f0d": self.unknown_0x61959f0d,
            "alignment_priority": self.alignment_priority,
            "separation_priority": self.separation_priority,
            "projectile_priority": self.projectile_priority,
            "player_priority": self.player_priority,
            "containment_priority": self.containment_priority,
            "wander_priority": self.wander_priority,
            "wander_amount": self.wander_amount,
            "player_ball_priority": self.player_ball_priority,
            "player_ball_distance": self.player_ball_distance,
            "projectile_decay_rate": self.projectile_decay_rate,
            "player_decay_rate": self.player_decay_rate,
            "look_ahead_time": self.look_ahead_time,
            "update_frame": self.update_frame,
            "material_color": self.material_color.to_json(),
            "can_be_killed": self.can_be_killed,
            "collision_radius": self.collision_radius,
            "death_effect0": self.death_effect0,
            "death_effect0_count": self.death_effect0_count,
            "death_effect1": self.death_effect1,
            "death_effect1_count": self.death_effect1_count,
            "death_effect2": self.death_effect2,
            "death_effect2_count": self.death_effect2_count,
            "death_effect3": self.death_effect3,
            "death_effect3_count": self.death_effect3_count,
            "death_sound": self.death_sound,
            "unknown_0xc320a050": self.unknown_0xc320a050,
            "unknown_0xcd4c81a1": self.unknown_0xcd4c81a1,
        }

    def _dependencies_for_fish_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.fish_model)

    def _dependencies_for_death_effect0(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_effect0)

    def _dependencies_for_death_effect1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_effect1)

    def _dependencies_for_death_effect2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_effect2)

    def _dependencies_for_death_effect3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_effect3)

    def _dependencies_for_death_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.death_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_fish_model, "fish_model", "AssetId"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self._dependencies_for_death_effect0, "death_effect0", "AssetId"),
            (self._dependencies_for_death_effect1, "death_effect1", "AssetId"),
            (self._dependencies_for_death_effect2, "death_effect2", "AssetId"),
            (self._dependencies_for_death_effect3, "death_effect3", "AssetId"),
            (self._dependencies_for_death_sound, "death_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for FishCloud.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_material_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xC6BB2F45: ("active", structs.decode_BIG_bool_),
    0x7990A3B6: ("fish_model", structs.decode_BIG_L),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0xF1C07275: ("fish_count", structs.decode_BIG_f),
    0x6392404E: ("speed", structs.decode_BIG_f),
    0x7864AD0E: ("influence_distance", structs.decode_BIG_f),
    0x61959F0D: ("unknown_0x61959f0d", structs.decode_BIG_f),
    0x4841F1DE: ("alignment_priority", structs.decode_BIG_f),
    0xD293EBC4: ("separation_priority", structs.decode_BIG_f),
    0x5F362A14: ("projectile_priority", structs.decode_BIG_f),
    0xEC9B73C2: ("player_priority", structs.decode_BIG_f),
    0x7FF1469E: ("containment_priority", structs.decode_BIG_f),
    0x7CE17870: ("wander_priority", structs.decode_BIG_f),
    0x3A25F09D: ("wander_amount", structs.decode_BIG_f),
    0x23A160F3: ("player_ball_priority", structs.decode_BIG_f),
    0xF0671410: ("player_ball_distance", structs.decode_BIG_f),
    0xA1747268: ("projectile_decay_rate", structs.decode_BIG_f),
    0xCE77A8D0: ("player_decay_rate", structs.decode_BIG_f),
    0x8CB20C53: ("look_ahead_time", structs.decode_BIG_f),
    0x21B3D07C: ("update_frame", structs.decode_BIG_l),
    0x1F83D350: ("material_color", _decode_material_color),
    0xF630B89F: ("can_be_killed", structs.decode_BIG_bool_),
    0x8A6AB139: ("collision_radius", structs.decode_BIG_f),
    0x5BA86245: ("death_effect0", structs.decode_BIG_L),
    0xA8232FB1: ("death_effect0_count", structs.decode_BIG_l),
    0x90F4B1E0: ("death_effect1", structs.decode_BIG_L),
    0xBF583BF2: ("death_effect1_count", structs.decode_BIG_l),
    0x1660C34E: ("death_effect2", structs.decode_BIG_L),
    0x86D50737: ("death_effect2_count", structs.decode_BIG_l),
    0xDD3C10EB: ("death_effect3", structs.decode_BIG_L),
    0x91AE1374: ("death_effect3_count", structs.decode_BIG_l),
    0x3DE26FC8: ("death_sound", structs.decode_BIG_l),
    0xC320A050: ("unknown_0xc320a050", structs.decode_BIG_bool_),
    0xCD4C81A1: ("unknown_0xcd4c81a1", structs.decode_BIG_bool_),
}
