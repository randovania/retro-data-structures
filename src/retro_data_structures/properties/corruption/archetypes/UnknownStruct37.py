# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct37Json(typing_extensions.TypedDict):
        speed: float
        track_time: float
        track_disable_distance: float
        unknown: float
        contact_damage: json_util.JsonObject
        slam_damage: json_util.JsonObject
        throw_damage: json_util.JsonObject
        launch_ball_speed: float
        contact_effect: int
        cable_segment_effect: int
        claw_model: int
        caud: int
        latch_morphball_sound: int


@dataclasses.dataclass()
class UnknownStruct37(BaseProperty):
    speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6392404E, original_name="Speed"),
        },
    )
    track_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC4489506, original_name="TrackTime"),
        },
    )
    track_disable_distance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x31CA76C8, original_name="TrackDisableDistance"),
        },
    )
    unknown: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x963C1729, original_name="Unknown"),
        },
    )
    contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xD756416E,
                original_name="ContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    slam_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x480103F3,
                original_name="SlamDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    throw_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xD80B1F34,
                original_name="ThrowDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    launch_ball_speed: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5324CBFB, original_name="LaunchBallSpeed"),
        },
    )
    contact_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4F387C49, original_name="ContactEffect"),
        },
    )
    cable_segment_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SWHC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xFFE83B77, original_name="CableSegmentEffect"),
        },
    )
    claw_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3D313DA6, original_name="ClawModel"),
        },
    )
    caud: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5C5BCE53, original_name="CAUD"),
        },
    )
    latch_morphball_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB97C1467, original_name="LatchMorphballSound"),
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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404E
        speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4489506
        track_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31CA76C8
        track_disable_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x963C1729
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD756416E
        contact_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x480103F3
        slam_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD80B1F34
        throw_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5324CBFB
        launch_ball_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F387C49
        contact_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFFE83B77
        cable_segment_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D313DA6
        claw_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C5BCE53
        caud = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB97C1467
        latch_morphball_sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            speed,
            track_time,
            track_disable_distance,
            unknown,
            contact_damage,
            slam_damage,
            throw_damage,
            launch_ball_speed,
            contact_effect,
            cable_segment_effect,
            claw_model,
            caud,
            latch_morphball_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\r")  # 13 properties

        data.write(b"c\x92@N")  # 0x6392404e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b"\xc4H\x95\x06")  # 0xc4489506
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.track_time))

        data.write(b"1\xcav\xc8")  # 0x31ca76c8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.track_disable_distance))

        data.write(b"\x96<\x17)")  # 0x963c1729
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\xd7VAn")  # 0xd756416e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"H\x01\x03\xf3")  # 0x480103f3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.slam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd8\x0b\x1f4")  # 0xd80b1f34
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.throw_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"S$\xcb\xfb")  # 0x5324cbfb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.launch_ball_speed))

        data.write(b"O8|I")  # 0x4f387c49
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.contact_effect))

        data.write(b"\xff\xe8;w")  # 0xffe83b77
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cable_segment_effect))

        data.write(b"=1=\xa6")  # 0x3d313da6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.claw_model))

        data.write(b"\\[\xceS")  # 0x5c5bce53
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud))

        data.write(b"\xb9|\x14g")  # 0xb97c1467
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.latch_morphball_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct37Json", data)
        return cls(
            speed=json_data["speed"],
            track_time=json_data["track_time"],
            track_disable_distance=json_data["track_disable_distance"],
            unknown=json_data["unknown"],
            contact_damage=DamageInfo.from_json(json_data["contact_damage"]),
            slam_damage=DamageInfo.from_json(json_data["slam_damage"]),
            throw_damage=DamageInfo.from_json(json_data["throw_damage"]),
            launch_ball_speed=json_data["launch_ball_speed"],
            contact_effect=json_data["contact_effect"],
            cable_segment_effect=json_data["cable_segment_effect"],
            claw_model=json_data["claw_model"],
            caud=json_data["caud"],
            latch_morphball_sound=json_data["latch_morphball_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "speed": self.speed,
            "track_time": self.track_time,
            "track_disable_distance": self.track_disable_distance,
            "unknown": self.unknown,
            "contact_damage": self.contact_damage.to_json(),
            "slam_damage": self.slam_damage.to_json(),
            "throw_damage": self.throw_damage.to_json(),
            "launch_ball_speed": self.launch_ball_speed,
            "contact_effect": self.contact_effect,
            "cable_segment_effect": self.cable_segment_effect,
            "claw_model": self.claw_model,
            "caud": self.caud,
            "latch_morphball_sound": self.latch_morphball_sound,
        }


def _decode_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_slam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_throw_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6392404E: ("speed", structs.decode_BIG_f),
    0xC4489506: ("track_time", structs.decode_BIG_f),
    0x31CA76C8: ("track_disable_distance", structs.decode_BIG_f),
    0x963C1729: ("unknown", structs.decode_BIG_f),
    0xD756416E: ("contact_damage", _decode_contact_damage),
    0x480103F3: ("slam_damage", _decode_slam_damage),
    0xD80B1F34: ("throw_damage", _decode_throw_damage),
    0x5324CBFB: ("launch_ball_speed", structs.decode_BIG_f),
    0x4F387C49: ("contact_effect", structs.decode_BIG_Q),
    0xFFE83B77: ("cable_segment_effect", structs.decode_BIG_Q),
    0x3D313DA6: ("claw_model", structs.decode_BIG_Q),
    0x5C5BCE53: ("caud", structs.decode_BIG_Q),
    0xB97C1467: ("latch_morphball_sound", structs.decode_BIG_Q),
}
