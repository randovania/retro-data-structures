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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class IngSnatchingSwarmJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        state_machine: int
        swarm_particle_system: int
        unknown_0x7cae2ed5: float
        part_0x35a88fa1: int
        unknown_0xf65e7ec5: float
        lifetime: float
        max_linear_speed: float
        max_linear_acceleration: float
        max_turn_speed: float
        unknown_0xdffdf5a2: bool
        ignore_player: bool
        unknown_0xe6b57a25: float
        exit_portal_distance: float
        unknown_0x2de5a19a: float
        unknown_0x4e79f717: float
        unknown_0xe8e0b5a6: float
        begin_snatching_range: float
        part_0x2d2afc26: int
        impact_damage: json_util.JsonObject
        sound_impact: int
        sound_idle: int
        sound_move: int
        health: float
        swarm_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class IngSnatchingSwarm(BaseObjectType):
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
    state_machine: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["AFSM", "FSM2"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x55744160, original_name="StateMachine"),
        },
    )
    swarm_particle_system: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART", "SRSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x83CF6509, original_name="SwarmParticleSystem"),
        },
    )
    unknown_0x7cae2ed5: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7CAE2ED5, original_name="Unknown"),
        },
    )
    part_0x35a88fa1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x35A88FA1, original_name="PART"),
        },
    )
    unknown_0xf65e7ec5: float = dataclasses.field(
        default=0.3499999940395355,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF65E7EC5, original_name="Unknown"),
        },
    )
    lifetime: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x32DC67F6, original_name="Lifetime"),
        },
    )
    max_linear_speed: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x563D6D13, original_name="MaxLinearSpeed"),
        },
    )
    max_linear_acceleration: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF549E733, original_name="MaxLinearAcceleration"),
        },
    )
    max_turn_speed: float = dataclasses.field(
        default=2000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0B5C3C1A, original_name="MaxTurnSpeed"),
        },
    )
    unknown_0xdffdf5a2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xDFFDF5A2, original_name="Unknown"),
        },
    )
    ignore_player: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7755F349, original_name="IgnorePlayer"),
        },
    )
    unknown_0xe6b57a25: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE6B57A25, original_name="Unknown"),
        },
    )
    exit_portal_distance: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x830966D5, original_name="ExitPortalDistance"),
        },
    )
    unknown_0x2de5a19a: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DE5A19A, original_name="Unknown"),
        },
    )
    unknown_0x4e79f717: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4E79F717, original_name="Unknown"),
        },
    )
    unknown_0xe8e0b5a6: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8E0B5A6, original_name="Unknown"),
        },
    )
    begin_snatching_range: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFCD8057B, original_name="BeginSnatchingRange"),
        },
    )
    part_0x2d2afc26: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2D2AFC26, original_name="PART"),
        },
    )
    impact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xB16D553E,
                original_name="ImpactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_impact: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x1BB16EA5, original_name="Sound_Impact"),
        },
    )
    sound_idle: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xAF38968E, original_name="Sound_Idle"),
        },
    )
    sound_move: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x6C101854, original_name="Sound_Move"),
        },
    )
    health: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0668919, original_name="Health"),
        },
    )
    swarm_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x8792A2B0,
                original_name="SwarmVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "ISSW"

    @classmethod
    def modules(cls) -> list[str]:
        return ["IngSnatchingSwarm.rel"]

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
        if property_count != 25:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55744160
        state_machine = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83CF6509
        swarm_particle_system = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CAE2ED5
        unknown_0x7cae2ed5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35A88FA1
        part_0x35a88fa1 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF65E7EC5
        unknown_0xf65e7ec5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32DC67F6
        lifetime = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x563D6D13
        max_linear_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF549E733
        max_linear_acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B5C3C1A
        max_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFFDF5A2
        unknown_0xdffdf5a2 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7755F349
        ignore_player = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE6B57A25
        unknown_0xe6b57a25 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x830966D5
        exit_portal_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DE5A19A
        unknown_0x2de5a19a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4E79F717
        unknown_0x4e79f717 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8E0B5A6
        unknown_0xe8e0b5a6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFCD8057B
        begin_snatching_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D2AFC26
        part_0x2d2afc26 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB16D553E
        impact_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1BB16EA5
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF38968E
        sound_idle = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C101854
        sound_move = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0668919
        health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8792A2B0
        swarm_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            state_machine,
            swarm_particle_system,
            unknown_0x7cae2ed5,
            part_0x35a88fa1,
            unknown_0xf65e7ec5,
            lifetime,
            max_linear_speed,
            max_linear_acceleration,
            max_turn_speed,
            unknown_0xdffdf5a2,
            ignore_player,
            unknown_0xe6b57a25,
            exit_portal_distance,
            unknown_0x2de5a19a,
            unknown_0x4e79f717,
            unknown_0xe8e0b5a6,
            begin_snatching_range,
            part_0x2d2afc26,
            impact_damage,
            sound_impact,
            sound_idle,
            sound_move,
            health,
            swarm_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x19")  # 25 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"UtA`")  # 0x55744160
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.state_machine))

        data.write(b"\x83\xcfe\t")  # 0x83cf6509
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.swarm_particle_system))

        data.write(b"|\xae.\xd5")  # 0x7cae2ed5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7cae2ed5))

        data.write(b"5\xa8\x8f\xa1")  # 0x35a88fa1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x35a88fa1))

        data.write(b"\xf6^~\xc5")  # 0xf65e7ec5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf65e7ec5))

        data.write(b"2\xdcg\xf6")  # 0x32dc67f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lifetime))

        data.write(b"V=m\x13")  # 0x563d6d13
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_linear_speed))

        data.write(b"\xf5I\xe73")  # 0xf549e733
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_linear_acceleration))

        data.write(b"\x0b\\<\x1a")  # 0xb5c3c1a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed))

        data.write(b"\xdf\xfd\xf5\xa2")  # 0xdffdf5a2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xdffdf5a2))

        data.write(b"wU\xf3I")  # 0x7755f349
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ignore_player))

        data.write(b"\xe6\xb5z%")  # 0xe6b57a25
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe6b57a25))

        data.write(b"\x83\tf\xd5")  # 0x830966d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.exit_portal_distance))

        data.write(b"-\xe5\xa1\x9a")  # 0x2de5a19a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2de5a19a))

        data.write(b"Ny\xf7\x17")  # 0x4e79f717
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4e79f717))

        data.write(b"\xe8\xe0\xb5\xa6")  # 0xe8e0b5a6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe8e0b5a6))

        data.write(b"\xfc\xd8\x05{")  # 0xfcd8057b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.begin_snatching_range))

        data.write(b"-*\xfc&")  # 0x2d2afc26
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x2d2afc26))

        data.write(b"\xb1mU>")  # 0xb16d553e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.impact_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1b\xb1n\xa5")  # 0x1bb16ea5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_impact))

        data.write(b"\xaf8\x96\x8e")  # 0xaf38968e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_idle))

        data.write(b"l\x10\x18T")  # 0x6c101854
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_move))

        data.write(b"\xf0f\x89\x19")  # 0xf0668919
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.health))

        data.write(b"\x87\x92\xa2\xb0")  # 0x8792a2b0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_vulnerability.to_stream(data, game)
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
        json_data = typing.cast("IngSnatchingSwarmJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            state_machine=json_data["state_machine"],
            swarm_particle_system=json_data["swarm_particle_system"],
            unknown_0x7cae2ed5=json_data["unknown_0x7cae2ed5"],
            part_0x35a88fa1=json_data["part_0x35a88fa1"],
            unknown_0xf65e7ec5=json_data["unknown_0xf65e7ec5"],
            lifetime=json_data["lifetime"],
            max_linear_speed=json_data["max_linear_speed"],
            max_linear_acceleration=json_data["max_linear_acceleration"],
            max_turn_speed=json_data["max_turn_speed"],
            unknown_0xdffdf5a2=json_data["unknown_0xdffdf5a2"],
            ignore_player=json_data["ignore_player"],
            unknown_0xe6b57a25=json_data["unknown_0xe6b57a25"],
            exit_portal_distance=json_data["exit_portal_distance"],
            unknown_0x2de5a19a=json_data["unknown_0x2de5a19a"],
            unknown_0x4e79f717=json_data["unknown_0x4e79f717"],
            unknown_0xe8e0b5a6=json_data["unknown_0xe8e0b5a6"],
            begin_snatching_range=json_data["begin_snatching_range"],
            part_0x2d2afc26=json_data["part_0x2d2afc26"],
            impact_damage=DamageInfo.from_json(json_data["impact_damage"]),
            sound_impact=json_data["sound_impact"],
            sound_idle=json_data["sound_idle"],
            sound_move=json_data["sound_move"],
            health=json_data["health"],
            swarm_vulnerability=DamageVulnerability.from_json(json_data["swarm_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "state_machine": self.state_machine,
            "swarm_particle_system": self.swarm_particle_system,
            "unknown_0x7cae2ed5": self.unknown_0x7cae2ed5,
            "part_0x35a88fa1": self.part_0x35a88fa1,
            "unknown_0xf65e7ec5": self.unknown_0xf65e7ec5,
            "lifetime": self.lifetime,
            "max_linear_speed": self.max_linear_speed,
            "max_linear_acceleration": self.max_linear_acceleration,
            "max_turn_speed": self.max_turn_speed,
            "unknown_0xdffdf5a2": self.unknown_0xdffdf5a2,
            "ignore_player": self.ignore_player,
            "unknown_0xe6b57a25": self.unknown_0xe6b57a25,
            "exit_portal_distance": self.exit_portal_distance,
            "unknown_0x2de5a19a": self.unknown_0x2de5a19a,
            "unknown_0x4e79f717": self.unknown_0x4e79f717,
            "unknown_0xe8e0b5a6": self.unknown_0xe8e0b5a6,
            "begin_snatching_range": self.begin_snatching_range,
            "part_0x2d2afc26": self.part_0x2d2afc26,
            "impact_damage": self.impact_damage.to_json(),
            "sound_impact": self.sound_impact,
            "sound_idle": self.sound_idle,
            "sound_move": self.sound_move,
            "health": self.health,
            "swarm_vulnerability": self.swarm_vulnerability.to_json(),
        }

    def _dependencies_for_state_machine(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.state_machine)

    def _dependencies_for_swarm_particle_system(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.swarm_particle_system)

    def _dependencies_for_part_0x35a88fa1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x35a88fa1)

    def _dependencies_for_part_0x2d2afc26(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x2d2afc26)

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_sound_idle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_idle)

    def _dependencies_for_sound_move(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_move)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_state_machine, "state_machine", "AssetId"),
            (self._dependencies_for_swarm_particle_system, "swarm_particle_system", "AssetId"),
            (self._dependencies_for_part_0x35a88fa1, "part_0x35a88fa1", "AssetId"),
            (self._dependencies_for_part_0x2d2afc26, "part_0x2d2afc26", "AssetId"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_sound_idle, "sound_idle", "int"),
            (self._dependencies_for_sound_move, "sound_move", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for IngSnatchingSwarm.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_impact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
    )


def _decode_swarm_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x55744160: ("state_machine", structs.decode_BIG_L),
    0x83CF6509: ("swarm_particle_system", structs.decode_BIG_L),
    0x7CAE2ED5: ("unknown_0x7cae2ed5", structs.decode_BIG_f),
    0x35A88FA1: ("part_0x35a88fa1", structs.decode_BIG_L),
    0xF65E7EC5: ("unknown_0xf65e7ec5", structs.decode_BIG_f),
    0x32DC67F6: ("lifetime", structs.decode_BIG_f),
    0x563D6D13: ("max_linear_speed", structs.decode_BIG_f),
    0xF549E733: ("max_linear_acceleration", structs.decode_BIG_f),
    0x0B5C3C1A: ("max_turn_speed", structs.decode_BIG_f),
    0xDFFDF5A2: ("unknown_0xdffdf5a2", structs.decode_BIG_bool_),
    0x7755F349: ("ignore_player", structs.decode_BIG_bool_),
    0xE6B57A25: ("unknown_0xe6b57a25", structs.decode_BIG_f),
    0x830966D5: ("exit_portal_distance", structs.decode_BIG_f),
    0x2DE5A19A: ("unknown_0x2de5a19a", structs.decode_BIG_f),
    0x4E79F717: ("unknown_0x4e79f717", structs.decode_BIG_f),
    0xE8E0B5A6: ("unknown_0xe8e0b5a6", structs.decode_BIG_f),
    0xFCD8057B: ("begin_snatching_range", structs.decode_BIG_f),
    0x2D2AFC26: ("part_0x2d2afc26", structs.decode_BIG_L),
    0xB16D553E: ("impact_damage", _decode_impact_damage),
    0x1BB16EA5: ("sound_impact", structs.decode_BIG_l),
    0xAF38968E: ("sound_idle", structs.decode_BIG_l),
    0x6C101854: ("sound_move", structs.decode_BIG_l),
    0xF0668919: ("health", structs.decode_BIG_f),
    0x8792A2B0: ("swarm_vulnerability", _decode_swarm_vulnerability),
}
