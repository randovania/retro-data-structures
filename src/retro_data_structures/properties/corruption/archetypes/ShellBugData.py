# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ShellBugDataJson(typing_extensions.TypedDict):
        launch_projectile_data: json_util.JsonObject
        unknown_0xa023555c: float
        unknown_0x4643fabd: float
        ball_range: float
        ball_radius: float
        look_ahead_time: float
        unknown_0x34bbc7a5: bool
        unknown_0xe5839374: float
        unknown_0x03e33c95: float
        weak_spot_vulnerability: json_util.JsonObject
        unknown_0x84e71870: bool
        unknown_0x76264db1: bool
        grapple_data: json_util.JsonObject


@dataclasses.dataclass()
class ShellBugData(BaseProperty):
    launch_projectile_data: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0xABA9A56D,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    unknown_0xa023555c: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA023555C, original_name="Unknown"),
        },
    )
    unknown_0x4643fabd: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4643FABD, original_name="Unknown"),
        },
    )
    ball_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0057A7D8, original_name="BallRange"),
        },
    )
    ball_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0E2F537F, original_name="BallRadius"),
        },
    )
    look_ahead_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8CB20C53, original_name="LookAheadTime"),
        },
    )
    unknown_0x34bbc7a5: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x34BBC7A5, original_name="Unknown"),
        },
    )
    unknown_0xe5839374: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE5839374, original_name="Unknown"),
        },
    )
    unknown_0x03e33c95: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x03E33C95, original_name="Unknown"),
        },
    )
    weak_spot_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x950318F0,
                original_name="WeakSpotVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0x84e71870: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x84E71870, original_name="Unknown"),
        },
    )
    unknown_0x76264db1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x76264DB1, original_name="Unknown"),
        },
    )
    grapple_data: GrappleData = dataclasses.field(
        default_factory=GrappleData,
        metadata={
            "reflection": FieldReflection[GrappleData](
                GrappleData,
                id=0xF609C637,
                original_name="GrappleData",
                from_json=GrappleData.from_json,
                to_json=GrappleData.to_json,
            ),
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
        assert property_id == 0xABA9A56D
        launch_projectile_data = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA023555C
        unknown_0xa023555c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4643FABD
        unknown_0x4643fabd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0057A7D8
        ball_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0E2F537F
        ball_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8CB20C53
        look_ahead_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34BBC7A5
        unknown_0x34bbc7a5 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE5839374
        unknown_0xe5839374 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03E33C95
        unknown_0x03e33c95 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x950318F0
        weak_spot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84E71870
        unknown_0x84e71870 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76264DB1
        unknown_0x76264db1 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF609C637
        grapple_data = GrappleData.from_stream(data, game, property_size)

        return cls(
            launch_projectile_data,
            unknown_0xa023555c,
            unknown_0x4643fabd,
            ball_range,
            ball_radius,
            look_ahead_time,
            unknown_0x34bbc7a5,
            unknown_0xe5839374,
            unknown_0x03e33c95,
            weak_spot_vulnerability,
            unknown_0x84e71870,
            unknown_0x76264db1,
            grapple_data,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\r")  # 13 properties

        data.write(b"\xab\xa9\xa5m")  # 0xaba9a56d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa0#U\\")  # 0xa023555c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa023555c))

        data.write(b"FC\xfa\xbd")  # 0x4643fabd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4643fabd))

        data.write(b"\x00W\xa7\xd8")  # 0x57a7d8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_range))

        data.write(b"\x0e/S\x7f")  # 0xe2f537f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_radius))

        data.write(b"\x8c\xb2\x0cS")  # 0x8cb20c53
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.look_ahead_time))

        data.write(b"4\xbb\xc7\xa5")  # 0x34bbc7a5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x34bbc7a5))

        data.write(b"\xe5\x83\x93t")  # 0xe5839374
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe5839374))

        data.write(b"\x03\xe3<\x95")  # 0x3e33c95
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x03e33c95))

        data.write(b"\x95\x03\x18\xf0")  # 0x950318f0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weak_spot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x84\xe7\x18p")  # 0x84e71870
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x84e71870))

        data.write(b"v&M\xb1")  # 0x76264db1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x76264db1))

        data.write(b"\xf6\t\xc67")  # 0xf609c637
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShellBugDataJson", data)
        return cls(
            launch_projectile_data=LaunchProjectileData.from_json(json_data["launch_projectile_data"]),
            unknown_0xa023555c=json_data["unknown_0xa023555c"],
            unknown_0x4643fabd=json_data["unknown_0x4643fabd"],
            ball_range=json_data["ball_range"],
            ball_radius=json_data["ball_radius"],
            look_ahead_time=json_data["look_ahead_time"],
            unknown_0x34bbc7a5=json_data["unknown_0x34bbc7a5"],
            unknown_0xe5839374=json_data["unknown_0xe5839374"],
            unknown_0x03e33c95=json_data["unknown_0x03e33c95"],
            weak_spot_vulnerability=DamageVulnerability.from_json(json_data["weak_spot_vulnerability"]),
            unknown_0x84e71870=json_data["unknown_0x84e71870"],
            unknown_0x76264db1=json_data["unknown_0x76264db1"],
            grapple_data=GrappleData.from_json(json_data["grapple_data"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "launch_projectile_data": self.launch_projectile_data.to_json(),
            "unknown_0xa023555c": self.unknown_0xa023555c,
            "unknown_0x4643fabd": self.unknown_0x4643fabd,
            "ball_range": self.ball_range,
            "ball_radius": self.ball_radius,
            "look_ahead_time": self.look_ahead_time,
            "unknown_0x34bbc7a5": self.unknown_0x34bbc7a5,
            "unknown_0xe5839374": self.unknown_0xe5839374,
            "unknown_0x03e33c95": self.unknown_0x03e33c95,
            "weak_spot_vulnerability": self.weak_spot_vulnerability.to_json(),
            "unknown_0x84e71870": self.unknown_0x84e71870,
            "unknown_0x76264db1": self.unknown_0x76264db1,
            "grapple_data": self.grapple_data.to_json(),
        }


def _decode_launch_projectile_data(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_weak_spot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xABA9A56D: ("launch_projectile_data", _decode_launch_projectile_data),
    0xA023555C: ("unknown_0xa023555c", structs.decode_BIG_f),
    0x4643FABD: ("unknown_0x4643fabd", structs.decode_BIG_f),
    0x0057A7D8: ("ball_range", structs.decode_BIG_f),
    0x0E2F537F: ("ball_radius", structs.decode_BIG_f),
    0x8CB20C53: ("look_ahead_time", structs.decode_BIG_f),
    0x34BBC7A5: ("unknown_0x34bbc7a5", structs.decode_BIG_bool_),
    0xE5839374: ("unknown_0xe5839374", structs.decode_BIG_f),
    0x03E33C95: ("unknown_0x03e33c95", structs.decode_BIG_f),
    0x950318F0: ("weak_spot_vulnerability", _decode_weak_spot_vulnerability),
    0x84E71870: ("unknown_0x84e71870", structs.decode_BIG_bool_),
    0x76264DB1: ("unknown_0x76264db1", structs.decode_BIG_bool_),
    0xF609C637: ("grapple_data", _decode_grapple_data),
}
