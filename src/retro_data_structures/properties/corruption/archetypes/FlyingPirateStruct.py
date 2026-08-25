# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FlyingPirateStructJson(typing_extensions.TypedDict):
        enable_hyper_mode: bool
        initial_hyper_mode_time: float
        hyper_mode_check_time: float
        hyper_mode_check_chance: float
        hyper_mode_duration: float
        hyper_mode_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class FlyingPirateStruct(BaseProperty):
    enable_hyper_mode: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xDD448CC9, original_name="EnableHyperMode"),
        },
    )
    initial_hyper_mode_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A834618, original_name="InitialHyperModeTime"),
        },
    )
    hyper_mode_check_time: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE9FD5A01, original_name="HyperModeCheckTime"),
        },
    )
    hyper_mode_check_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF04452F3, original_name="HyperModeCheckChance"),
        },
    )
    hyper_mode_duration: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA3F3BE5D, original_name="HyperModeDuration"),
        },
    )
    hyper_mode_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xC8A1EAC8,
                original_name="HyperModeVulnerability",
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
        if property_count != 6:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD448CC9
        enable_hyper_mode = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A834618
        initial_hyper_mode_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9FD5A01
        hyper_mode_check_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF04452F3
        hyper_mode_check_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3F3BE5D
        hyper_mode_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC8A1EAC8
        hyper_mode_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            enable_hyper_mode,
            initial_hyper_mode_time,
            hyper_mode_check_time,
            hyper_mode_check_chance,
            hyper_mode_duration,
            hyper_mode_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"\xddD\x8c\xc9")  # 0xdd448cc9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.enable_hyper_mode))

        data.write(b"\x8a\x83F\x18")  # 0x8a834618
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_hyper_mode_time))

        data.write(b"\xe9\xfdZ\x01")  # 0xe9fd5a01
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_check_time))

        data.write(b"\xf0DR\xf3")  # 0xf04452f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_check_chance))

        data.write(b"\xa3\xf3\xbe]")  # 0xa3f3be5d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_duration))

        data.write(b"\xc8\xa1\xea\xc8")  # 0xc8a1eac8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyingPirateStructJson", data)
        return cls(
            enable_hyper_mode=json_data["enable_hyper_mode"],
            initial_hyper_mode_time=json_data["initial_hyper_mode_time"],
            hyper_mode_check_time=json_data["hyper_mode_check_time"],
            hyper_mode_check_chance=json_data["hyper_mode_check_chance"],
            hyper_mode_duration=json_data["hyper_mode_duration"],
            hyper_mode_vulnerability=DamageVulnerability.from_json(json_data["hyper_mode_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "enable_hyper_mode": self.enable_hyper_mode,
            "initial_hyper_mode_time": self.initial_hyper_mode_time,
            "hyper_mode_check_time": self.hyper_mode_check_time,
            "hyper_mode_check_chance": self.hyper_mode_check_chance,
            "hyper_mode_duration": self.hyper_mode_duration,
            "hyper_mode_vulnerability": self.hyper_mode_vulnerability.to_json(),
        }


def _decode_hyper_mode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xDD448CC9: ("enable_hyper_mode", structs.decode_BIG_bool_),
    0x8A834618: ("initial_hyper_mode_time", structs.decode_BIG_f),
    0xE9FD5A01: ("hyper_mode_check_time", structs.decode_BIG_f),
    0xF04452F3: ("hyper_mode_check_chance", structs.decode_BIG_f),
    0xA3F3BE5D: ("hyper_mode_duration", structs.decode_BIG_f),
    0xC8A1EAC8: ("hyper_mode_vulnerability", _decode_hyper_mode_vulnerability),
}
