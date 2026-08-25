# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.UnknownStruct18 import UnknownStruct18
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct19Json(typing_extensions.TypedDict):
        health: float
        animation_speed: float
        body_vulnerability: json_util.JsonObject
        mouth_vulnerability: json_util.JsonObject
        joint_vulnerability: json_util.JsonObject
        orb_vulnerability: json_util.JsonObject
        stun_threshold: float
        stun_decay: float
        wander_distance: float
        too_far_distance: float
        dash_delay_maximum: float
        dash_delay_minimum: float
        dash_delay_variance: float
        unknown_0x673a2724: float
        unknown_0x815a88c5: float
        stun_delay_max: float
        stun_delay_min: float
        unknown_0x86e154b4: float
        unknown_0x20dc1c96: float
        unknown_0xfba7c57b: float
        unknown_0xba801f2f: float
        unknown_0xe1ee4260: float
        unknown_0x8e080314: float
        unknown_0xd7d24bfa: int
        unknown_struct18: json_util.JsonObject
        unknown_0xa62404dc: float
        unknown_0xbf8b57bf: float
        unknown_0x530ecf07: float
        unknown_0x8482e270: float
        unknown_0x7128f60e: float
        unknown_0xd9c4aa53: str
        left_target_attachment: int
        unknown_0x71c8e644: str
        unknown_0x8cb60fc9: str
        right_target_attachment: int
        unknown_0x967948b7: str
        left_armor_attachment: int
        unknown_0xf5ed7ba0: str
        right_armor_attachment: int
        unknown_0xfc6e8fae: str
        cmdl: int
        unknown_0x448d4f01: str


@dataclasses.dataclass()
class UnknownStruct19(BaseProperty):
    health: float = dataclasses.field(
        default=750.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0668919, original_name="Health"),
        },
    )
    animation_speed: float = dataclasses.field(
        default=1.0499999523162842,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC5407757, original_name="AnimationSpeed"),
        },
    )
    body_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0D9230D1,
                original_name="BodyVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    mouth_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xED7EDCA3,
                original_name="MouthVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    joint_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x295CF609,
                original_name="JointVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    orb_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x23DDBB55,
                original_name="OrbVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    stun_threshold: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5BDD1E4C, original_name="StunThreshold"),
        },
    )
    stun_decay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6082430F, original_name="StunDecay"),
        },
    )
    wander_distance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAF270C93, original_name="WanderDistance"),
        },
    )
    too_far_distance: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8819688D, original_name="TooFarDistance"),
        },
    )
    dash_delay_maximum: float = dataclasses.field(
        default=18.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B37EDA7, original_name="DashDelayMaximum"),
        },
    )
    dash_delay_minimum: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B44FD4D, original_name="DashDelayMinimum"),
        },
    )
    dash_delay_variance: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDAC05EB5, original_name="DashDelayVariance"),
        },
    )
    unknown_0x673a2724: float = dataclasses.field(
        default=24.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x673A2724, original_name="Unknown"),
        },
    )
    unknown_0x815a88c5: float = dataclasses.field(
        default=16.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x815A88C5, original_name="Unknown"),
        },
    )
    stun_delay_max: float = dataclasses.field(
        default=12.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4D6A00C, original_name="StunDelayMax"),
        },
    )
    stun_delay_min: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x32B60FED, original_name="StunDelayMin"),
        },
    )
    unknown_0x86e154b4: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x86E154B4, original_name="Unknown"),
        },
    )
    unknown_0x20dc1c96: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x20DC1C96, original_name="Unknown"),
        },
    )
    unknown_0xfba7c57b: float = dataclasses.field(
        default=0.009999999776482582,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFBA7C57B, original_name="Unknown"),
        },
    )
    unknown_0xba801f2f: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA801F2F, original_name="Unknown"),
        },
    )
    unknown_0xe1ee4260: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE1EE4260, original_name="Unknown"),
        },
    )
    unknown_0x8e080314: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E080314, original_name="Unknown"),
        },
    )
    unknown_0xd7d24bfa: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD7D24BFA, original_name="Unknown"),
        },
    )
    unknown_struct18: UnknownStruct18 = dataclasses.field(
        default_factory=UnknownStruct18,
        metadata={
            "reflection": FieldReflection[UnknownStruct18](
                UnknownStruct18,
                id=0xCCCCA97E,
                original_name="UnknownStruct18",
                from_json=UnknownStruct18.from_json,
                to_json=UnknownStruct18.to_json,
            ),
        },
    )
    unknown_0xa62404dc: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA62404DC, original_name="Unknown"),
        },
    )
    unknown_0xbf8b57bf: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBF8B57BF, original_name="Unknown"),
        },
    )
    unknown_0x530ecf07: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x530ECF07, original_name="Unknown"),
        },
    )
    unknown_0x8482e270: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8482E270, original_name="Unknown"),
        },
    )
    unknown_0x7128f60e: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7128F60E, original_name="Unknown"),
        },
    )
    unknown_0xd9c4aa53: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xD9C4AA53, original_name="Unknown"),
        },
    )
    left_target_attachment: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8E13F1F6, original_name="LeftTargetAttachment"),
        },
    )
    unknown_0x71c8e644: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x71C8E644, original_name="Unknown"),
        },
    )
    unknown_0x8cb60fc9: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x8CB60FC9, original_name="Unknown"),
        },
    )
    right_target_attachment: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x69A25F05, original_name="RightTargetAttachment"),
        },
    )
    unknown_0x967948b7: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x967948B7, original_name="Unknown"),
        },
    )
    left_armor_attachment: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0A366C12, original_name="LeftArmorAttachment"),
        },
    )
    unknown_0xf5ed7ba0: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xF5ED7BA0, original_name="Unknown"),
        },
    )
    right_armor_attachment: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x03B5981C, original_name="RightArmorAttachment"),
        },
    )
    unknown_0xfc6e8fae: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xFC6E8FAE, original_name="Unknown"),
        },
    )
    cmdl: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBB5658B3, original_name="CMDL"),
        },
    )
    unknown_0x448d4f01: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x448D4F01, original_name="Unknown"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 42:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0668919
        health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5407757
        animation_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D9230D1
        body_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED7EDCA3
        mouth_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x295CF609
        joint_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23DDBB55
        orb_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BDD1E4C
        stun_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6082430F
        stun_decay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF270C93
        wander_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8819688D
        too_far_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B37EDA7
        dash_delay_maximum = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B44FD4D
        dash_delay_minimum = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDAC05EB5
        dash_delay_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x673A2724
        unknown_0x673a2724 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x815A88C5
        unknown_0x815a88c5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4D6A00C
        stun_delay_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32B60FED
        stun_delay_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86E154B4
        unknown_0x86e154b4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20DC1C96
        unknown_0x20dc1c96 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBA7C57B
        unknown_0xfba7c57b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA801F2F
        unknown_0xba801f2f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1EE4260
        unknown_0xe1ee4260 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E080314
        unknown_0x8e080314 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD7D24BFA
        unknown_0xd7d24bfa = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCCCA97E
        unknown_struct18 = UnknownStruct18.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA62404DC
        unknown_0xa62404dc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF8B57BF
        unknown_0xbf8b57bf = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x530ECF07
        unknown_0x530ecf07 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8482E270
        unknown_0x8482e270 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7128F60E
        unknown_0x7128f60e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD9C4AA53
        unknown_0xd9c4aa53 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E13F1F6
        left_target_attachment = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71C8E644
        unknown_0x71c8e644 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8CB60FC9
        unknown_0x8cb60fc9 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69A25F05
        right_target_attachment = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x967948B7
        unknown_0x967948b7 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A366C12
        left_armor_attachment = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5ED7BA0
        unknown_0xf5ed7ba0 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03B5981C
        right_armor_attachment = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC6E8FAE
        unknown_0xfc6e8fae = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB5658B3
        cmdl = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x448D4F01
        unknown_0x448d4f01 = data.read(property_size)[:-1].decode("utf-8")

        return cls(
            health,
            animation_speed,
            body_vulnerability,
            mouth_vulnerability,
            joint_vulnerability,
            orb_vulnerability,
            stun_threshold,
            stun_decay,
            wander_distance,
            too_far_distance,
            dash_delay_maximum,
            dash_delay_minimum,
            dash_delay_variance,
            unknown_0x673a2724,
            unknown_0x815a88c5,
            stun_delay_max,
            stun_delay_min,
            unknown_0x86e154b4,
            unknown_0x20dc1c96,
            unknown_0xfba7c57b,
            unknown_0xba801f2f,
            unknown_0xe1ee4260,
            unknown_0x8e080314,
            unknown_0xd7d24bfa,
            unknown_struct18,
            unknown_0xa62404dc,
            unknown_0xbf8b57bf,
            unknown_0x530ecf07,
            unknown_0x8482e270,
            unknown_0x7128f60e,
            unknown_0xd9c4aa53,
            left_target_attachment,
            unknown_0x71c8e644,
            unknown_0x8cb60fc9,
            right_target_attachment,
            unknown_0x967948b7,
            left_armor_attachment,
            unknown_0xf5ed7ba0,
            right_armor_attachment,
            unknown_0xfc6e8fae,
            cmdl,
            unknown_0x448d4f01,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00*")  # 42 properties

        data.write(b"\xf0f\x89\x19")  # 0xf0668919
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.health))

        data.write(b"\xc5@wW")  # 0xc5407757
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.animation_speed))

        data.write(b"\r\x920\xd1")  # 0xd9230d1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.body_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed~\xdc\xa3")  # 0xed7edca3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.mouth_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b")\\\xf6\t")  # 0x295cf609
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.joint_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"#\xdd\xbbU")  # 0x23ddbb55
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.orb_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"[\xdd\x1eL")  # 0x5bdd1e4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_threshold))

        data.write(b"`\x82C\x0f")  # 0x6082430f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_decay))

        data.write(b"\xaf'\x0c\x93")  # 0xaf270c93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.wander_distance))

        data.write(b"\x88\x19h\x8d")  # 0x8819688d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.too_far_distance))

        data.write(b"\x1b7\xed\xa7")  # 0x1b37eda7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dash_delay_maximum))

        data.write(b"\x8bD\xfdM")  # 0x8b44fd4d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dash_delay_minimum))

        data.write(b"\xda\xc0^\xb5")  # 0xdac05eb5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dash_delay_variance))

        data.write(b"g:'$")  # 0x673a2724
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x673a2724))

        data.write(b"\x81Z\x88\xc5")  # 0x815a88c5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x815a88c5))

        data.write(b"\xd4\xd6\xa0\x0c")  # 0xd4d6a00c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_delay_max))

        data.write(b"2\xb6\x0f\xed")  # 0x32b60fed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_delay_min))

        data.write(b"\x86\xe1T\xb4")  # 0x86e154b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x86e154b4))

        data.write(b" \xdc\x1c\x96")  # 0x20dc1c96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x20dc1c96))

        data.write(b"\xfb\xa7\xc5{")  # 0xfba7c57b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfba7c57b))

        data.write(b"\xba\x80\x1f/")  # 0xba801f2f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xba801f2f))

        data.write(b"\xe1\xeeB`")  # 0xe1ee4260
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe1ee4260))

        data.write(b"\x8e\x08\x03\x14")  # 0x8e080314
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8e080314))

        data.write(b"\xd7\xd2K\xfa")  # 0xd7d24bfa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd7d24bfa))

        data.write(b"\xcc\xcc\xa9~")  # 0xcccca97e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct18.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa6$\x04\xdc")  # 0xa62404dc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa62404dc))

        data.write(b"\xbf\x8bW\xbf")  # 0xbf8b57bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbf8b57bf))

        data.write(b"S\x0e\xcf\x07")  # 0x530ecf07
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x530ecf07))

        data.write(b"\x84\x82\xe2p")  # 0x8482e270
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8482e270))

        data.write(b"q(\xf6\x0e")  # 0x7128f60e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7128f60e))

        data.write(b"\xd9\xc4\xaaS")  # 0xd9c4aa53
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xd9c4aa53.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8e\x13\xf1\xf6")  # 0x8e13f1f6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_target_attachment))

        data.write(b"q\xc8\xe6D")  # 0x71c8e644
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x71c8e644.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8c\xb6\x0f\xc9")  # 0x8cb60fc9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x8cb60fc9.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"i\xa2_\x05")  # 0x69a25f05
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_target_attachment))

        data.write(b"\x96yH\xb7")  # 0x967948b7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x967948b7.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\n6l\x12")  # 0xa366c12
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_armor_attachment))

        data.write(b"\xf5\xed{\xa0")  # 0xf5ed7ba0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xf5ed7ba0.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x03\xb5\x98\x1c")  # 0x3b5981c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_armor_attachment))

        data.write(b"\xfcn\x8f\xae")  # 0xfc6e8fae
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xfc6e8fae.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbbVX\xb3")  # 0xbb5658b3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl))

        data.write(b"D\x8dO\x01")  # 0x448d4f01
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x448d4f01.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct19Json", data)
        return cls(
            health=json_data["health"],
            animation_speed=json_data["animation_speed"],
            body_vulnerability=DamageVulnerability.from_json(json_data["body_vulnerability"]),
            mouth_vulnerability=DamageVulnerability.from_json(json_data["mouth_vulnerability"]),
            joint_vulnerability=DamageVulnerability.from_json(json_data["joint_vulnerability"]),
            orb_vulnerability=DamageVulnerability.from_json(json_data["orb_vulnerability"]),
            stun_threshold=json_data["stun_threshold"],
            stun_decay=json_data["stun_decay"],
            wander_distance=json_data["wander_distance"],
            too_far_distance=json_data["too_far_distance"],
            dash_delay_maximum=json_data["dash_delay_maximum"],
            dash_delay_minimum=json_data["dash_delay_minimum"],
            dash_delay_variance=json_data["dash_delay_variance"],
            unknown_0x673a2724=json_data["unknown_0x673a2724"],
            unknown_0x815a88c5=json_data["unknown_0x815a88c5"],
            stun_delay_max=json_data["stun_delay_max"],
            stun_delay_min=json_data["stun_delay_min"],
            unknown_0x86e154b4=json_data["unknown_0x86e154b4"],
            unknown_0x20dc1c96=json_data["unknown_0x20dc1c96"],
            unknown_0xfba7c57b=json_data["unknown_0xfba7c57b"],
            unknown_0xba801f2f=json_data["unknown_0xba801f2f"],
            unknown_0xe1ee4260=json_data["unknown_0xe1ee4260"],
            unknown_0x8e080314=json_data["unknown_0x8e080314"],
            unknown_0xd7d24bfa=json_data["unknown_0xd7d24bfa"],
            unknown_struct18=UnknownStruct18.from_json(json_data["unknown_struct18"]),
            unknown_0xa62404dc=json_data["unknown_0xa62404dc"],
            unknown_0xbf8b57bf=json_data["unknown_0xbf8b57bf"],
            unknown_0x530ecf07=json_data["unknown_0x530ecf07"],
            unknown_0x8482e270=json_data["unknown_0x8482e270"],
            unknown_0x7128f60e=json_data["unknown_0x7128f60e"],
            unknown_0xd9c4aa53=json_data["unknown_0xd9c4aa53"],
            left_target_attachment=json_data["left_target_attachment"],
            unknown_0x71c8e644=json_data["unknown_0x71c8e644"],
            unknown_0x8cb60fc9=json_data["unknown_0x8cb60fc9"],
            right_target_attachment=json_data["right_target_attachment"],
            unknown_0x967948b7=json_data["unknown_0x967948b7"],
            left_armor_attachment=json_data["left_armor_attachment"],
            unknown_0xf5ed7ba0=json_data["unknown_0xf5ed7ba0"],
            right_armor_attachment=json_data["right_armor_attachment"],
            unknown_0xfc6e8fae=json_data["unknown_0xfc6e8fae"],
            cmdl=json_data["cmdl"],
            unknown_0x448d4f01=json_data["unknown_0x448d4f01"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "health": self.health,
            "animation_speed": self.animation_speed,
            "body_vulnerability": self.body_vulnerability.to_json(),
            "mouth_vulnerability": self.mouth_vulnerability.to_json(),
            "joint_vulnerability": self.joint_vulnerability.to_json(),
            "orb_vulnerability": self.orb_vulnerability.to_json(),
            "stun_threshold": self.stun_threshold,
            "stun_decay": self.stun_decay,
            "wander_distance": self.wander_distance,
            "too_far_distance": self.too_far_distance,
            "dash_delay_maximum": self.dash_delay_maximum,
            "dash_delay_minimum": self.dash_delay_minimum,
            "dash_delay_variance": self.dash_delay_variance,
            "unknown_0x673a2724": self.unknown_0x673a2724,
            "unknown_0x815a88c5": self.unknown_0x815a88c5,
            "stun_delay_max": self.stun_delay_max,
            "stun_delay_min": self.stun_delay_min,
            "unknown_0x86e154b4": self.unknown_0x86e154b4,
            "unknown_0x20dc1c96": self.unknown_0x20dc1c96,
            "unknown_0xfba7c57b": self.unknown_0xfba7c57b,
            "unknown_0xba801f2f": self.unknown_0xba801f2f,
            "unknown_0xe1ee4260": self.unknown_0xe1ee4260,
            "unknown_0x8e080314": self.unknown_0x8e080314,
            "unknown_0xd7d24bfa": self.unknown_0xd7d24bfa,
            "unknown_struct18": self.unknown_struct18.to_json(),
            "unknown_0xa62404dc": self.unknown_0xa62404dc,
            "unknown_0xbf8b57bf": self.unknown_0xbf8b57bf,
            "unknown_0x530ecf07": self.unknown_0x530ecf07,
            "unknown_0x8482e270": self.unknown_0x8482e270,
            "unknown_0x7128f60e": self.unknown_0x7128f60e,
            "unknown_0xd9c4aa53": self.unknown_0xd9c4aa53,
            "left_target_attachment": self.left_target_attachment,
            "unknown_0x71c8e644": self.unknown_0x71c8e644,
            "unknown_0x8cb60fc9": self.unknown_0x8cb60fc9,
            "right_target_attachment": self.right_target_attachment,
            "unknown_0x967948b7": self.unknown_0x967948b7,
            "left_armor_attachment": self.left_armor_attachment,
            "unknown_0xf5ed7ba0": self.unknown_0xf5ed7ba0,
            "right_armor_attachment": self.right_armor_attachment,
            "unknown_0xfc6e8fae": self.unknown_0xfc6e8fae,
            "cmdl": self.cmdl,
            "unknown_0x448d4f01": self.unknown_0x448d4f01,
        }


def _decode_body_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_mouth_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_joint_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_orb_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_unknown_struct18(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct18:
    return UnknownStruct18.from_stream(data, game, property_size)


def _decode_unknown_0xd9c4aa53(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x71c8e644(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x8cb60fc9(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x967948b7(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xf5ed7ba0(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xfc6e8fae(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x448d4f01(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF0668919: ("health", structs.decode_BIG_f),
    0xC5407757: ("animation_speed", structs.decode_BIG_f),
    0x0D9230D1: ("body_vulnerability", _decode_body_vulnerability),
    0xED7EDCA3: ("mouth_vulnerability", _decode_mouth_vulnerability),
    0x295CF609: ("joint_vulnerability", _decode_joint_vulnerability),
    0x23DDBB55: ("orb_vulnerability", _decode_orb_vulnerability),
    0x5BDD1E4C: ("stun_threshold", structs.decode_BIG_f),
    0x6082430F: ("stun_decay", structs.decode_BIG_f),
    0xAF270C93: ("wander_distance", structs.decode_BIG_f),
    0x8819688D: ("too_far_distance", structs.decode_BIG_f),
    0x1B37EDA7: ("dash_delay_maximum", structs.decode_BIG_f),
    0x8B44FD4D: ("dash_delay_minimum", structs.decode_BIG_f),
    0xDAC05EB5: ("dash_delay_variance", structs.decode_BIG_f),
    0x673A2724: ("unknown_0x673a2724", structs.decode_BIG_f),
    0x815A88C5: ("unknown_0x815a88c5", structs.decode_BIG_f),
    0xD4D6A00C: ("stun_delay_max", structs.decode_BIG_f),
    0x32B60FED: ("stun_delay_min", structs.decode_BIG_f),
    0x86E154B4: ("unknown_0x86e154b4", structs.decode_BIG_f),
    0x20DC1C96: ("unknown_0x20dc1c96", structs.decode_BIG_f),
    0xFBA7C57B: ("unknown_0xfba7c57b", structs.decode_BIG_f),
    0xBA801F2F: ("unknown_0xba801f2f", structs.decode_BIG_f),
    0xE1EE4260: ("unknown_0xe1ee4260", structs.decode_BIG_f),
    0x8E080314: ("unknown_0x8e080314", structs.decode_BIG_f),
    0xD7D24BFA: ("unknown_0xd7d24bfa", structs.decode_BIG_l),
    0xCCCCA97E: ("unknown_struct18", _decode_unknown_struct18),
    0xA62404DC: ("unknown_0xa62404dc", structs.decode_BIG_f),
    0xBF8B57BF: ("unknown_0xbf8b57bf", structs.decode_BIG_f),
    0x530ECF07: ("unknown_0x530ecf07", structs.decode_BIG_f),
    0x8482E270: ("unknown_0x8482e270", structs.decode_BIG_f),
    0x7128F60E: ("unknown_0x7128f60e", structs.decode_BIG_f),
    0xD9C4AA53: ("unknown_0xd9c4aa53", _decode_unknown_0xd9c4aa53),
    0x8E13F1F6: ("left_target_attachment", structs.decode_BIG_Q),
    0x71C8E644: ("unknown_0x71c8e644", _decode_unknown_0x71c8e644),
    0x8CB60FC9: ("unknown_0x8cb60fc9", _decode_unknown_0x8cb60fc9),
    0x69A25F05: ("right_target_attachment", structs.decode_BIG_Q),
    0x967948B7: ("unknown_0x967948b7", _decode_unknown_0x967948b7),
    0x0A366C12: ("left_armor_attachment", structs.decode_BIG_Q),
    0xF5ED7BA0: ("unknown_0xf5ed7ba0", _decode_unknown_0xf5ed7ba0),
    0x03B5981C: ("right_armor_attachment", structs.decode_BIG_Q),
    0xFC6E8FAE: ("unknown_0xfc6e8fae", _decode_unknown_0xfc6e8fae),
    0xBB5658B3: ("cmdl", structs.decode_BIG_Q),
    0x448D4F01: ("unknown_0x448d4f01", _decode_unknown_0x448d4f01),
}
