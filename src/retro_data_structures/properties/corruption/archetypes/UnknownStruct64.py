# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.archetypes.SpriteStruct import SpriteStruct
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct64Json(typing_extensions.TypedDict):
        patrol: json_util.JsonObject
        sprite_struct_0x2cbb438b: json_util.JsonObject
        sprite_struct_0xa80227e6: json_util.JsonObject
        sprite_struct_0x34799811: json_util.JsonObject
        flash_range: float
        flash_range_max: float
        flash_intensity: float
        flash_duration: float
        unknown: float
        flash_delay: float
        scan_delay: float


@dataclasses.dataclass()
class UnknownStruct64(BaseProperty):
    patrol: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xCCDD3ACA,
                original_name="Patrol",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    sprite_struct_0x2cbb438b: SpriteStruct = dataclasses.field(
        default_factory=SpriteStruct,
        metadata={
            "reflection": FieldReflection[SpriteStruct](
                SpriteStruct,
                id=0x2CBB438B,
                original_name="SpriteStruct",
                from_json=SpriteStruct.from_json,
                to_json=SpriteStruct.to_json,
            ),
        },
    )
    sprite_struct_0xa80227e6: SpriteStruct = dataclasses.field(
        default_factory=SpriteStruct,
        metadata={
            "reflection": FieldReflection[SpriteStruct](
                SpriteStruct,
                id=0xA80227E6,
                original_name="SpriteStruct",
                from_json=SpriteStruct.from_json,
                to_json=SpriteStruct.to_json,
            ),
        },
    )
    sprite_struct_0x34799811: SpriteStruct = dataclasses.field(
        default_factory=SpriteStruct,
        metadata={
            "reflection": FieldReflection[SpriteStruct](
                SpriteStruct,
                id=0x34799811,
                original_name="SpriteStruct",
                from_json=SpriteStruct.from_json,
                to_json=SpriteStruct.to_json,
            ),
        },
    )
    flash_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x26945E20, original_name="FlashRange"),
        },
    )
    flash_range_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7F878C1C, original_name="FlashRangeMax"),
        },
    )
    flash_intensity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6E575D67, original_name="FlashIntensity"),
        },
    )
    flash_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8EBEA596, original_name="FlashDuration"),
        },
    )
    unknown: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x429C66D3, original_name="Unknown"),
        },
    )
    flash_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x04290E24, original_name="FlashDelay"),
        },
    )
    scan_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FC827A2, original_name="ScanDelay"),
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCDD3ACA
        patrol = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={"speed": 1.0, "acceleration": 0.5, "facing_turn_rate": 10.0, "turn_threshold": 180.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CBB438B
        sprite_struct_0x2cbb438b = SpriteStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA80227E6
        sprite_struct_0xa80227e6 = SpriteStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34799811
        sprite_struct_0x34799811 = SpriteStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26945E20
        flash_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F878C1C
        flash_range_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E575D67
        flash_intensity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8EBEA596
        flash_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x429C66D3
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04290E24
        flash_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FC827A2
        scan_delay = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            patrol,
            sprite_struct_0x2cbb438b,
            sprite_struct_0xa80227e6,
            sprite_struct_0x34799811,
            flash_range,
            flash_range_max,
            flash_intensity,
            flash_duration,
            unknown,
            flash_delay,
            scan_delay,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"\xcc\xdd:\xca")  # 0xccdd3aca
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patrol.to_stream(
            data,
            game,
            default_override={"speed": 1.0, "acceleration": 0.5, "facing_turn_rate": 10.0, "turn_threshold": 180.0},
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b",\xbbC\x8b")  # 0x2cbb438b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sprite_struct_0x2cbb438b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa8\x02'\xe6")  # 0xa80227e6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sprite_struct_0xa80227e6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"4y\x98\x11")  # 0x34799811
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sprite_struct_0x34799811.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"&\x94^ ")  # 0x26945e20
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flash_range))

        data.write(b"\x7f\x87\x8c\x1c")  # 0x7f878c1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flash_range_max))

        data.write(b"nW]g")  # 0x6e575d67
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flash_intensity))

        data.write(b"\x8e\xbe\xa5\x96")  # 0x8ebea596
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flash_duration))

        data.write(b"B\x9cf\xd3")  # 0x429c66d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x04)\x0e$")  # 0x4290e24
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flash_delay))

        data.write(b"\x7f\xc8'\xa2")  # 0x7fc827a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_delay))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct64Json", data)
        return cls(
            patrol=FlyerMovementMode.from_json(json_data["patrol"]),
            sprite_struct_0x2cbb438b=SpriteStruct.from_json(json_data["sprite_struct_0x2cbb438b"]),
            sprite_struct_0xa80227e6=SpriteStruct.from_json(json_data["sprite_struct_0xa80227e6"]),
            sprite_struct_0x34799811=SpriteStruct.from_json(json_data["sprite_struct_0x34799811"]),
            flash_range=json_data["flash_range"],
            flash_range_max=json_data["flash_range_max"],
            flash_intensity=json_data["flash_intensity"],
            flash_duration=json_data["flash_duration"],
            unknown=json_data["unknown"],
            flash_delay=json_data["flash_delay"],
            scan_delay=json_data["scan_delay"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "patrol": self.patrol.to_json(),
            "sprite_struct_0x2cbb438b": self.sprite_struct_0x2cbb438b.to_json(),
            "sprite_struct_0xa80227e6": self.sprite_struct_0xa80227e6.to_json(),
            "sprite_struct_0x34799811": self.sprite_struct_0x34799811.to_json(),
            "flash_range": self.flash_range,
            "flash_range_max": self.flash_range_max,
            "flash_intensity": self.flash_intensity,
            "flash_duration": self.flash_duration,
            "unknown": self.unknown,
            "flash_delay": self.flash_delay,
            "scan_delay": self.scan_delay,
        }


def _decode_patrol(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={"speed": 1.0, "acceleration": 0.5, "facing_turn_rate": 10.0, "turn_threshold": 180.0},
    )


def _decode_sprite_struct_0x2cbb438b(data: typing.BinaryIO, game: Game, property_size: int) -> SpriteStruct:
    return SpriteStruct.from_stream(data, game, property_size)


def _decode_sprite_struct_0xa80227e6(data: typing.BinaryIO, game: Game, property_size: int) -> SpriteStruct:
    return SpriteStruct.from_stream(data, game, property_size)


def _decode_sprite_struct_0x34799811(data: typing.BinaryIO, game: Game, property_size: int) -> SpriteStruct:
    return SpriteStruct.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCCDD3ACA: ("patrol", _decode_patrol),
    0x2CBB438B: ("sprite_struct_0x2cbb438b", _decode_sprite_struct_0x2cbb438b),
    0xA80227E6: ("sprite_struct_0xa80227e6", _decode_sprite_struct_0xa80227e6),
    0x34799811: ("sprite_struct_0x34799811", _decode_sprite_struct_0x34799811),
    0x26945E20: ("flash_range", structs.decode_BIG_f),
    0x7F878C1C: ("flash_range_max", structs.decode_BIG_f),
    0x6E575D67: ("flash_intensity", structs.decode_BIG_f),
    0x8EBEA596: ("flash_duration", structs.decode_BIG_f),
    0x429C66D3: ("unknown", structs.decode_BIG_f),
    0x04290E24: ("flash_delay", structs.decode_BIG_f),
    0x7FC827A2: ("scan_delay", structs.decode_BIG_f),
}
