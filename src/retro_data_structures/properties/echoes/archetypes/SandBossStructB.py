# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SandBossStructBJson(typing_extensions.TypedDict):
        damage: json_util.JsonObject
        duration: float
        change_direction_interval: float
        unknown_0x1b57d422: float
        change_direction_chance: float
        inner_radius: float
        outer_radius: float
        unknown_0x52642b7e: float
        unknown_0xfda3eb4b: float
        turn_speed: float
        unknown_0x47cde539: float
        sound_charge_beam: int
        unknown_0x8d4f3b88: int
        unknown_0xbf88fe4f: float
        unknown_0x74c702b3: float


@dataclasses.dataclass()
class SandBossStructB(BaseProperty):
    damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x337F9524,
                original_name="Damage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    duration: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B51E23F, original_name="Duration"),
        },
    )
    change_direction_interval: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x82BE06BA, original_name="ChangeDirectionInterval"),
        },
    )
    unknown_0x1b57d422: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B57D422, original_name="Unknown"),
        },
    )
    change_direction_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x060B9B84, original_name="ChangeDirectionChance"),
        },
    )
    inner_radius: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3F5AF46F, original_name="InnerRadius"),
        },
    )
    outer_radius: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x42D842CD, original_name="OuterRadius"),
        },
    )
    unknown_0x52642b7e: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x52642B7E, original_name="Unknown"),
        },
    )
    unknown_0xfda3eb4b: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFDA3EB4B, original_name="Unknown"),
        },
    )
    turn_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x020C78BB, original_name="TurnSpeed"),
        },
    )
    unknown_0x47cde539: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47CDE539, original_name="Unknown"),
        },
    )
    sound_charge_beam: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x29D8744A, original_name="Sound_ChargeBeam"),
        },
    )
    unknown_0x8d4f3b88: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8D4F3B88, original_name="Unknown"),
        },
    )
    unknown_0xbf88fe4f: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBF88FE4F, original_name="Unknown"),
        },
    )
    unknown_0x74c702b3: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x74C702B3, original_name="Unknown"),
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
        if property_count != 15:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 0.5, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B51E23F
        duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82BE06BA
        change_direction_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B57D422
        unknown_0x1b57d422 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x060B9B84
        change_direction_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3F5AF46F
        inner_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42D842CD
        outer_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52642B7E
        unknown_0x52642b7e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFDA3EB4B
        unknown_0xfda3eb4b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x020C78BB
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47CDE539
        unknown_0x47cde539 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29D8744A
        sound_charge_beam = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D4F3B88
        unknown_0x8d4f3b88 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF88FE4F
        unknown_0xbf88fe4f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74C702B3
        unknown_0x74c702b3 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            damage,
            duration,
            change_direction_interval,
            unknown_0x1b57d422,
            change_direction_chance,
            inner_radius,
            outer_radius,
            unknown_0x52642b7e,
            unknown_0xfda3eb4b,
            turn_speed,
            unknown_0x47cde539,
            sound_charge_beam,
            unknown_0x8d4f3b88,
            unknown_0xbf88fe4f,
            unknown_0x74c702b3,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 0.5, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8bQ\xe2?")  # 0x8b51e23f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b"\x82\xbe\x06\xba")  # 0x82be06ba
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.change_direction_interval))

        data.write(b'\x1bW\xd4"')  # 0x1b57d422
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1b57d422))

        data.write(b"\x06\x0b\x9b\x84")  # 0x60b9b84
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.change_direction_chance))

        data.write(b"?Z\xf4o")  # 0x3f5af46f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.inner_radius))

        data.write(b"B\xd8B\xcd")  # 0x42d842cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.outer_radius))

        data.write(b"Rd+~")  # 0x52642b7e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x52642b7e))

        data.write(b"\xfd\xa3\xebK")  # 0xfda3eb4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfda3eb4b))

        data.write(b"\x02\x0cx\xbb")  # 0x20c78bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_speed))

        data.write(b"G\xcd\xe59")  # 0x47cde539
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x47cde539))

        data.write(b")\xd8tJ")  # 0x29d8744a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_charge_beam))

        data.write(b"\x8dO;\x88")  # 0x8d4f3b88
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x8d4f3b88))

        data.write(b"\xbf\x88\xfeO")  # 0xbf88fe4f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbf88fe4f))

        data.write(b"t\xc7\x02\xb3")  # 0x74c702b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x74c702b3))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SandBossStructBJson", data)
        return cls(
            damage=DamageInfo.from_json(json_data["damage"]),
            duration=json_data["duration"],
            change_direction_interval=json_data["change_direction_interval"],
            unknown_0x1b57d422=json_data["unknown_0x1b57d422"],
            change_direction_chance=json_data["change_direction_chance"],
            inner_radius=json_data["inner_radius"],
            outer_radius=json_data["outer_radius"],
            unknown_0x52642b7e=json_data["unknown_0x52642b7e"],
            unknown_0xfda3eb4b=json_data["unknown_0xfda3eb4b"],
            turn_speed=json_data["turn_speed"],
            unknown_0x47cde539=json_data["unknown_0x47cde539"],
            sound_charge_beam=json_data["sound_charge_beam"],
            unknown_0x8d4f3b88=json_data["unknown_0x8d4f3b88"],
            unknown_0xbf88fe4f=json_data["unknown_0xbf88fe4f"],
            unknown_0x74c702b3=json_data["unknown_0x74c702b3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "damage": self.damage.to_json(),
            "duration": self.duration,
            "change_direction_interval": self.change_direction_interval,
            "unknown_0x1b57d422": self.unknown_0x1b57d422,
            "change_direction_chance": self.change_direction_chance,
            "inner_radius": self.inner_radius,
            "outer_radius": self.outer_radius,
            "unknown_0x52642b7e": self.unknown_0x52642b7e,
            "unknown_0xfda3eb4b": self.unknown_0xfda3eb4b,
            "turn_speed": self.turn_speed,
            "unknown_0x47cde539": self.unknown_0x47cde539,
            "sound_charge_beam": self.sound_charge_beam,
            "unknown_0x8d4f3b88": self.unknown_0x8d4f3b88,
            "unknown_0xbf88fe4f": self.unknown_0xbf88fe4f,
            "unknown_0x74c702b3": self.unknown_0x74c702b3,
        }

    def _dependencies_for_sound_charge_beam(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_charge_beam)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_sound_charge_beam(asset_manager)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 0.5, "di_knock_back_power": 10.0},
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x337F9524: ("damage", _decode_damage),
    0x8B51E23F: ("duration", structs.decode_BIG_f),
    0x82BE06BA: ("change_direction_interval", structs.decode_BIG_f),
    0x1B57D422: ("unknown_0x1b57d422", structs.decode_BIG_f),
    0x060B9B84: ("change_direction_chance", structs.decode_BIG_f),
    0x3F5AF46F: ("inner_radius", structs.decode_BIG_f),
    0x42D842CD: ("outer_radius", structs.decode_BIG_f),
    0x52642B7E: ("unknown_0x52642b7e", structs.decode_BIG_f),
    0xFDA3EB4B: ("unknown_0xfda3eb4b", structs.decode_BIG_f),
    0x020C78BB: ("turn_speed", structs.decode_BIG_f),
    0x47CDE539: ("unknown_0x47cde539", structs.decode_BIG_f),
    0x29D8744A: ("sound_charge_beam", structs.decode_BIG_l),
    0x8D4F3B88: ("unknown_0x8d4f3b88", structs.decode_BIG_l),
    0xBF88FE4F: ("unknown_0xbf88fe4f", structs.decode_BIG_f),
    0x74C702B3: ("unknown_0x74c702b3", structs.decode_BIG_f),
}
