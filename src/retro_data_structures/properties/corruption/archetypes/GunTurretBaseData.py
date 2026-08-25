# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GunTurretBaseDataJson(typing_extensions.TypedDict):
        is_pirate_turret: bool
        shoots_at_player: bool
        unknown: bool
        gun_respawns: bool
        gun_respawn_delay: float
        deploy_height: float
        deploy_time: float
        attack_range: float
        hearing_range: float
        retarget_time: float
        gun_connector_effect: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x701D65CD,
    0xA7846EC,
    0x8A12367,
    0x32D6D325,
    0x35D61966,
    0x3D942150,
    0x63CC234D,
    0x39DAC81E,
    0x25474550,
    0x73570173,
    0xB09ED686,
)


@dataclasses.dataclass()
class GunTurretBaseData(BaseProperty):
    is_pirate_turret: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x701D65CD, original_name="IsPirateTurret"),
        },
    )
    shoots_at_player: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0A7846EC, original_name="ShootsAtPlayer"),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x08A12367, original_name="Unknown"),
        },
    )
    gun_respawns: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x32D6D325, original_name="GunRespawns"),
        },
    )
    gun_respawn_delay: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x35D61966, original_name="GunRespawnDelay"),
        },
    )
    deploy_height: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3D942150, original_name="DeployHeight"),
        },
    )
    deploy_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x63CC234D, original_name="DeployTime"),
        },
    )
    attack_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39DAC81E, original_name="AttackRange"),
        },
    )
    hearing_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x25474550, original_name="HearingRange"),
        },
    )
    retarget_time: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x73570173, original_name="RetargetTime"),
        },
    )
    gun_connector_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB09ED686, original_name="GunConnectorEffect"),
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
        if property_count != 11:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LH?LH?LH?LHfLHfLHfLHfLHfLHfLHQ")

        dec = _FAST_FORMAT.unpack(data.read(102))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"p\x1de\xcd")  # 0x701d65cd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_pirate_turret))

        data.write(b"\nxF\xec")  # 0xa7846ec
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.shoots_at_player))

        data.write(b"\x08\xa1#g")  # 0x8a12367
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b"2\xd6\xd3%")  # 0x32d6d325
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.gun_respawns))

        data.write(b"5\xd6\x19f")  # 0x35d61966
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gun_respawn_delay))

        data.write(b"=\x94!P")  # 0x3d942150
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.deploy_height))

        data.write(b"c\xcc#M")  # 0x63cc234d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.deploy_time))

        data.write(b"9\xda\xc8\x1e")  # 0x39dac81e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_range))

        data.write(b"%GEP")  # 0x25474550
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hearing_range))

        data.write(b"sW\x01s")  # 0x73570173
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.retarget_time))

        data.write(b"\xb0\x9e\xd6\x86")  # 0xb09ed686
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.gun_connector_effect))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GunTurretBaseDataJson", data)
        return cls(
            is_pirate_turret=json_data["is_pirate_turret"],
            shoots_at_player=json_data["shoots_at_player"],
            unknown=json_data["unknown"],
            gun_respawns=json_data["gun_respawns"],
            gun_respawn_delay=json_data["gun_respawn_delay"],
            deploy_height=json_data["deploy_height"],
            deploy_time=json_data["deploy_time"],
            attack_range=json_data["attack_range"],
            hearing_range=json_data["hearing_range"],
            retarget_time=json_data["retarget_time"],
            gun_connector_effect=json_data["gun_connector_effect"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "is_pirate_turret": self.is_pirate_turret,
            "shoots_at_player": self.shoots_at_player,
            "unknown": self.unknown,
            "gun_respawns": self.gun_respawns,
            "gun_respawn_delay": self.gun_respawn_delay,
            "deploy_height": self.deploy_height,
            "deploy_time": self.deploy_time,
            "attack_range": self.attack_range,
            "hearing_range": self.hearing_range,
            "retarget_time": self.retarget_time,
            "gun_connector_effect": self.gun_connector_effect,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x701D65CD: ("is_pirate_turret", structs.decode_BIG_bool_),
    0x0A7846EC: ("shoots_at_player", structs.decode_BIG_bool_),
    0x08A12367: ("unknown", structs.decode_BIG_bool_),
    0x32D6D325: ("gun_respawns", structs.decode_BIG_bool_),
    0x35D61966: ("gun_respawn_delay", structs.decode_BIG_f),
    0x3D942150: ("deploy_height", structs.decode_BIG_f),
    0x63CC234D: ("deploy_time", structs.decode_BIG_f),
    0x39DAC81E: ("attack_range", structs.decode_BIG_f),
    0x25474550: ("hearing_range", structs.decode_BIG_f),
    0x73570173: ("retarget_time", structs.decode_BIG_f),
    0xB09ED686: ("gun_connector_effect", structs.decode_BIG_Q),
}
