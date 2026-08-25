# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TweakCameraBobJson(typing_extensions.TypedDict):
        instance_name: str
        camera_bob_extent_x: float
        camera_bob_extent_y: float
        camera_bob_period: float
        unknown_0xa27bb5a7: float
        unknown_0xe3580b2b: float
        slow_speed_period_scale: float
        target_magnitude_tracking_rate: float
        landing_bob_spring_constant: float
        view_wander_radius: float
        view_wander_speed_min: float
        view_wander_speed_max: float
        view_wander_roll_variation: float
        gun_bob_magnitude: float
        helmet_bob_magnitude: float


@dataclasses.dataclass()
class TweakCameraBob(BaseObjectType):
    instance_name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x7FDA1466, original_name="InstanceName"),
        },
    )
    camera_bob_extent_x: float = dataclasses.field(
        default=0.07000000029802322,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE2A0B6F1, original_name="CameraBobExtentX"),
        },
    )
    camera_bob_extent_y: float = dataclasses.field(
        default=0.14000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x29FC6554, original_name="CameraBobExtentY"),
        },
    )
    camera_bob_period: float = dataclasses.field(
        default=0.38999998569488525,
        metadata={
            "reflection": FieldReflection[float](float, id=0x149D7339, original_name="CameraBobPeriod"),
        },
    )
    unknown_0xa27bb5a7: float = dataclasses.field(
        default=0.7699999809265137,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA27BB5A7, original_name="Unknown"),
        },
    )
    unknown_0xe3580b2b: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE3580B2B, original_name="Unknown"),
        },
    )
    slow_speed_period_scale: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB05DADE7, original_name="SlowSpeedPeriodScale"),
        },
    )
    target_magnitude_tracking_rate: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6DC5D440, original_name="TargetMagnitudeTrackingRate"),
        },
    )
    landing_bob_spring_constant: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD16539A7, original_name="LandingBobSpringConstant"),
        },
    )
    view_wander_radius: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xADBB0A42, original_name="ViewWanderRadius"),
        },
    )
    view_wander_speed_min: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7F8F11B, original_name="ViewWanderSpeedMin"),
        },
    )
    view_wander_speed_max: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x01985EFA, original_name="ViewWanderSpeedMax"),
        },
    )
    view_wander_roll_variation: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEF19BA33, original_name="ViewWanderRollVariation"),
        },
    )
    gun_bob_magnitude: float = dataclasses.field(
        default=0.2199999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7F59BE96, original_name="GunBobMagnitude"),
        },
    )
    helmet_bob_magnitude: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x38A82AC1, original_name="HelmetBobMagnitude"),
        },
    )

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return "TWCB"

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
        if property_count != 15:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FDA1466
        instance_name = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2A0B6F1
        camera_bob_extent_x = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29FC6554
        camera_bob_extent_y = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x149D7339
        camera_bob_period = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA27BB5A7
        unknown_0xa27bb5a7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE3580B2B
        unknown_0xe3580b2b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB05DADE7
        slow_speed_period_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DC5D440
        target_magnitude_tracking_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD16539A7
        landing_bob_spring_constant = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xADBB0A42
        view_wander_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7F8F11B
        view_wander_speed_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01985EFA
        view_wander_speed_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF19BA33
        view_wander_roll_variation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F59BE96
        gun_bob_magnitude = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38A82AC1
        helmet_bob_magnitude = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            instance_name,
            camera_bob_extent_x,
            camera_bob_extent_y,
            camera_bob_period,
            unknown_0xa27bb5a7,
            unknown_0xe3580b2b,
            slow_speed_period_scale,
            target_magnitude_tracking_rate,
            landing_bob_spring_constant,
            view_wander_radius,
            view_wander_speed_min,
            view_wander_speed_max,
            view_wander_roll_variation,
            gun_bob_magnitude,
            helmet_bob_magnitude,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"\x7f\xda\x14f")  # 0x7fda1466
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.instance_name.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe2\xa0\xb6\xf1")  # 0xe2a0b6f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.camera_bob_extent_x))

        data.write(b")\xfceT")  # 0x29fc6554
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.camera_bob_extent_y))

        data.write(b"\x14\x9ds9")  # 0x149d7339
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.camera_bob_period))

        data.write(b"\xa2{\xb5\xa7")  # 0xa27bb5a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa27bb5a7))

        data.write(b"\xe3X\x0b+")  # 0xe3580b2b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe3580b2b))

        data.write(b"\xb0]\xad\xe7")  # 0xb05dade7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.slow_speed_period_scale))

        data.write(b"m\xc5\xd4@")  # 0x6dc5d440
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.target_magnitude_tracking_rate))

        data.write(b"\xd1e9\xa7")  # 0xd16539a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.landing_bob_spring_constant))

        data.write(b"\xad\xbb\nB")  # 0xadbb0a42
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.view_wander_radius))

        data.write(b"\xe7\xf8\xf1\x1b")  # 0xe7f8f11b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.view_wander_speed_min))

        data.write(b"\x01\x98^\xfa")  # 0x1985efa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.view_wander_speed_max))

        data.write(b"\xef\x19\xba3")  # 0xef19ba33
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.view_wander_roll_variation))

        data.write(b"\x7fY\xbe\x96")  # 0x7f59be96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gun_bob_magnitude))

        data.write(b"8\xa8*\xc1")  # 0x38a82ac1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.helmet_bob_magnitude))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakCameraBobJson", data)
        return cls(
            instance_name=json_data["instance_name"],
            camera_bob_extent_x=json_data["camera_bob_extent_x"],
            camera_bob_extent_y=json_data["camera_bob_extent_y"],
            camera_bob_period=json_data["camera_bob_period"],
            unknown_0xa27bb5a7=json_data["unknown_0xa27bb5a7"],
            unknown_0xe3580b2b=json_data["unknown_0xe3580b2b"],
            slow_speed_period_scale=json_data["slow_speed_period_scale"],
            target_magnitude_tracking_rate=json_data["target_magnitude_tracking_rate"],
            landing_bob_spring_constant=json_data["landing_bob_spring_constant"],
            view_wander_radius=json_data["view_wander_radius"],
            view_wander_speed_min=json_data["view_wander_speed_min"],
            view_wander_speed_max=json_data["view_wander_speed_max"],
            view_wander_roll_variation=json_data["view_wander_roll_variation"],
            gun_bob_magnitude=json_data["gun_bob_magnitude"],
            helmet_bob_magnitude=json_data["helmet_bob_magnitude"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "instance_name": self.instance_name,
            "camera_bob_extent_x": self.camera_bob_extent_x,
            "camera_bob_extent_y": self.camera_bob_extent_y,
            "camera_bob_period": self.camera_bob_period,
            "unknown_0xa27bb5a7": self.unknown_0xa27bb5a7,
            "unknown_0xe3580b2b": self.unknown_0xe3580b2b,
            "slow_speed_period_scale": self.slow_speed_period_scale,
            "target_magnitude_tracking_rate": self.target_magnitude_tracking_rate,
            "landing_bob_spring_constant": self.landing_bob_spring_constant,
            "view_wander_radius": self.view_wander_radius,
            "view_wander_speed_min": self.view_wander_speed_min,
            "view_wander_speed_max": self.view_wander_speed_max,
            "view_wander_roll_variation": self.view_wander_roll_variation,
            "gun_bob_magnitude": self.gun_bob_magnitude,
            "helmet_bob_magnitude": self.helmet_bob_magnitude,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FDA1466: ("instance_name", _decode_instance_name),
    0xE2A0B6F1: ("camera_bob_extent_x", structs.decode_BIG_f),
    0x29FC6554: ("camera_bob_extent_y", structs.decode_BIG_f),
    0x149D7339: ("camera_bob_period", structs.decode_BIG_f),
    0xA27BB5A7: ("unknown_0xa27bb5a7", structs.decode_BIG_f),
    0xE3580B2B: ("unknown_0xe3580b2b", structs.decode_BIG_f),
    0xB05DADE7: ("slow_speed_period_scale", structs.decode_BIG_f),
    0x6DC5D440: ("target_magnitude_tracking_rate", structs.decode_BIG_f),
    0xD16539A7: ("landing_bob_spring_constant", structs.decode_BIG_f),
    0xADBB0A42: ("view_wander_radius", structs.decode_BIG_f),
    0xE7F8F11B: ("view_wander_speed_min", structs.decode_BIG_f),
    0x01985EFA: ("view_wander_speed_max", structs.decode_BIG_f),
    0xEF19BA33: ("view_wander_roll_variation", structs.decode_BIG_f),
    0x7F59BE96: ("gun_bob_magnitude", structs.decode_BIG_f),
    0x38A82AC1: ("helmet_bob_magnitude", structs.decode_BIG_f),
}
