# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class HyperModeDataJson(typing_extensions.TypedDict):
        initial_time_max: float
        initial_time_min: float
        duration_max: float
        duration_min: float
        check_delay_max: float
        check_delay_min: float
        check_chance: float
        shot: json_util.JsonObject
        vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class HyperModeData(BaseProperty):
    initial_time_max: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB12FDA2B, original_name="InitialTimeMax"),
        },
    )
    initial_time_min: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x574F75CA, original_name="InitialTimeMin"),
        },
    )
    duration_max: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCB83BF77, original_name="DurationMax"),
        },
    )
    duration_min: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DE31096, original_name="DurationMin"),
        },
    )
    check_delay_max: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0C2506BC, original_name="CheckDelayMax"),
        },
    )
    check_delay_min: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEA45A95D, original_name="CheckDelayMin"),
        },
    )
    check_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95C19D09, original_name="CheckChance"),
        },
    )
    shot: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x55D89AB7,
                original_name="Shot",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
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
        if property_count != 9:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB12FDA2B
        initial_time_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x574F75CA
        initial_time_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB83BF77
        duration_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DE31096
        duration_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C2506BC
        check_delay_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA45A95D
        check_delay_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95C19D09
        check_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55D89AB7
        shot = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            initial_time_max,
            initial_time_min,
            duration_max,
            duration_min,
            check_delay_max,
            check_delay_min,
            check_chance,
            shot,
            vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"\xb1/\xda+")  # 0xb12fda2b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_time_max))

        data.write(b"WOu\xca")  # 0x574f75ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_time_min))

        data.write(b"\xcb\x83\xbfw")  # 0xcb83bf77
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration_max))

        data.write(b"-\xe3\x10\x96")  # 0x2de31096
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration_min))

        data.write(b"\x0c%\x06\xbc")  # 0xc2506bc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.check_delay_max))

        data.write(b"\xeaE\xa9]")  # 0xea45a95d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.check_delay_min))

        data.write(b"\x95\xc1\x9d\t")  # 0x95c19d09
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.check_chance))

        data.write(b"U\xd8\x9a\xb7")  # 0x55d89ab7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shot.to_stream(data, game)
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

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("HyperModeDataJson", data)
        return cls(
            initial_time_max=json_data["initial_time_max"],
            initial_time_min=json_data["initial_time_min"],
            duration_max=json_data["duration_max"],
            duration_min=json_data["duration_min"],
            check_delay_max=json_data["check_delay_max"],
            check_delay_min=json_data["check_delay_min"],
            check_chance=json_data["check_chance"],
            shot=LaunchProjectileData.from_json(json_data["shot"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "initial_time_max": self.initial_time_max,
            "initial_time_min": self.initial_time_min,
            "duration_max": self.duration_max,
            "duration_min": self.duration_min,
            "check_delay_max": self.check_delay_max,
            "check_delay_min": self.check_delay_min,
            "check_chance": self.check_chance,
            "shot": self.shot.to_json(),
            "vulnerability": self.vulnerability.to_json(),
        }


def _decode_shot(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB12FDA2B: ("initial_time_max", structs.decode_BIG_f),
    0x574F75CA: ("initial_time_min", structs.decode_BIG_f),
    0xCB83BF77: ("duration_max", structs.decode_BIG_f),
    0x2DE31096: ("duration_min", structs.decode_BIG_f),
    0x0C2506BC: ("check_delay_max", structs.decode_BIG_f),
    0xEA45A95D: ("check_delay_min", structs.decode_BIG_f),
    0x95C19D09: ("check_chance", structs.decode_BIG_f),
    0x55D89AB7: ("shot", _decode_shot),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
}
