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

    class UnknownStruct18Json(typing_extensions.TypedDict):
        column_effect: int
        column_trail_effect: int
        elsc: int
        visor_effect_electric: int
        unknown_0x01299e29: int
        unknown_0x442bddab: int
        column_damage: json_util.JsonObject
        cross_bar_damage: json_util.JsonObject
        column_damage_radius: float
        initial_speed: float
        acceleration: float
        apex_shockwave_volume: float
        unknown_0x4032c58a: float
        unknown_0x8b6e162f: float
        unknown_0x966b2697: float


@dataclasses.dataclass()
class UnknownStruct18(BaseProperty):
    column_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4C28CD13, original_name="ColumnEffect"),
        },
    )
    column_trail_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x32A13DFD, original_name="ColumnTrailEffect"),
        },
    )
    elsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x57F7EFF9, original_name="ELSC"),
        },
    )
    visor_effect_electric: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xFD132F70, original_name="VisorEffectElectric"),
        },
    )
    unknown_0x01299e29: int = dataclasses.field(
        default=6,
        metadata={
            "reflection": FieldReflection[int](int, id=0x01299E29, original_name="Unknown"),
        },
    )
    unknown_0x442bddab: int = dataclasses.field(
        default=6,
        metadata={
            "reflection": FieldReflection[int](int, id=0x442BDDAB, original_name="Unknown"),
        },
    )
    column_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x37304F48,
                original_name="ColumnDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    cross_bar_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xC5528A8D,
                original_name="CrossBarDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    column_damage_radius: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B59E590, original_name="ColumnDamageRadius"),
        },
    )
    initial_speed: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCB14D97C, original_name="InitialSpeed"),
        },
    )
    acceleration: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39FB7978, original_name="Acceleration"),
        },
    )
    apex_shockwave_volume: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6A6B724, original_name="ApexShockwaveVolume"),
        },
    )
    unknown_0x4032c58a: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4032C58A, original_name="Unknown"),
        },
    )
    unknown_0x8b6e162f: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B6E162F, original_name="Unknown"),
        },
    )
    unknown_0x966b2697: float = dataclasses.field(
        default=9.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x966B2697, original_name="Unknown"),
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
        assert property_id == 0x4C28CD13
        column_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32A13DFD
        column_trail_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57F7EFF9
        elsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFD132F70
        visor_effect_electric = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01299E29
        unknown_0x01299e29 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x442BDDAB
        unknown_0x442bddab = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37304F48
        column_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_damage": 20.0, "di_knock_back_power": 10.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5528A8D
        cross_bar_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_damage": 20.0, "di_knock_back_power": 10.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B59E590
        column_damage_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB14D97C
        initial_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39FB7978
        acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6A6B724
        apex_shockwave_volume = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4032C58A
        unknown_0x4032c58a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B6E162F
        unknown_0x8b6e162f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x966B2697
        unknown_0x966b2697 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            column_effect,
            column_trail_effect,
            elsc,
            visor_effect_electric,
            unknown_0x01299e29,
            unknown_0x442bddab,
            column_damage,
            cross_bar_damage,
            column_damage_radius,
            initial_speed,
            acceleration,
            apex_shockwave_volume,
            unknown_0x4032c58a,
            unknown_0x8b6e162f,
            unknown_0x966b2697,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"L(\xcd\x13")  # 0x4c28cd13
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.column_effect))

        data.write(b"2\xa1=\xfd")  # 0x32a13dfd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.column_trail_effect))

        data.write(b"W\xf7\xef\xf9")  # 0x57f7eff9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc))

        data.write(b"\xfd\x13/p")  # 0xfd132f70
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_effect_electric))

        data.write(b"\x01)\x9e)")  # 0x1299e29
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x01299e29))

        data.write(b"D+\xdd\xab")  # 0x442bddab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x442bddab))

        data.write(b"70OH")  # 0x37304f48
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.column_damage.to_stream(data, game, default_override={"di_damage": 20.0, "di_knock_back_power": 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc5R\x8a\x8d")  # 0xc5528a8d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.cross_bar_damage.to_stream(data, game, default_override={"di_damage": 20.0, "di_knock_back_power": 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"KY\xe5\x90")  # 0x4b59e590
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.column_damage_radius))

        data.write(b"\xcb\x14\xd9|")  # 0xcb14d97c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_speed))

        data.write(b"9\xfbyx")  # 0x39fb7978
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.acceleration))

        data.write(b"\xc6\xa6\xb7$")  # 0xc6a6b724
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.apex_shockwave_volume))

        data.write(b"@2\xc5\x8a")  # 0x4032c58a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4032c58a))

        data.write(b"\x8bn\x16/")  # 0x8b6e162f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8b6e162f))

        data.write(b"\x96k&\x97")  # 0x966b2697
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x966b2697))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct18Json", data)
        return cls(
            column_effect=json_data["column_effect"],
            column_trail_effect=json_data["column_trail_effect"],
            elsc=json_data["elsc"],
            visor_effect_electric=json_data["visor_effect_electric"],
            unknown_0x01299e29=json_data["unknown_0x01299e29"],
            unknown_0x442bddab=json_data["unknown_0x442bddab"],
            column_damage=DamageInfo.from_json(json_data["column_damage"]),
            cross_bar_damage=DamageInfo.from_json(json_data["cross_bar_damage"]),
            column_damage_radius=json_data["column_damage_radius"],
            initial_speed=json_data["initial_speed"],
            acceleration=json_data["acceleration"],
            apex_shockwave_volume=json_data["apex_shockwave_volume"],
            unknown_0x4032c58a=json_data["unknown_0x4032c58a"],
            unknown_0x8b6e162f=json_data["unknown_0x8b6e162f"],
            unknown_0x966b2697=json_data["unknown_0x966b2697"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "column_effect": self.column_effect,
            "column_trail_effect": self.column_trail_effect,
            "elsc": self.elsc,
            "visor_effect_electric": self.visor_effect_electric,
            "unknown_0x01299e29": self.unknown_0x01299e29,
            "unknown_0x442bddab": self.unknown_0x442bddab,
            "column_damage": self.column_damage.to_json(),
            "cross_bar_damage": self.cross_bar_damage.to_json(),
            "column_damage_radius": self.column_damage_radius,
            "initial_speed": self.initial_speed,
            "acceleration": self.acceleration,
            "apex_shockwave_volume": self.apex_shockwave_volume,
            "unknown_0x4032c58a": self.unknown_0x4032c58a,
            "unknown_0x8b6e162f": self.unknown_0x8b6e162f,
            "unknown_0x966b2697": self.unknown_0x966b2697,
        }


def _decode_column_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_damage": 20.0, "di_knock_back_power": 10.0}
    )


def _decode_cross_bar_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_damage": 20.0, "di_knock_back_power": 10.0}
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4C28CD13: ("column_effect", structs.decode_BIG_Q),
    0x32A13DFD: ("column_trail_effect", structs.decode_BIG_Q),
    0x57F7EFF9: ("elsc", structs.decode_BIG_Q),
    0xFD132F70: ("visor_effect_electric", structs.decode_BIG_Q),
    0x01299E29: ("unknown_0x01299e29", structs.decode_BIG_l),
    0x442BDDAB: ("unknown_0x442bddab", structs.decode_BIG_l),
    0x37304F48: ("column_damage", _decode_column_damage),
    0xC5528A8D: ("cross_bar_damage", _decode_cross_bar_damage),
    0x4B59E590: ("column_damage_radius", structs.decode_BIG_f),
    0xCB14D97C: ("initial_speed", structs.decode_BIG_f),
    0x39FB7978: ("acceleration", structs.decode_BIG_f),
    0xC6A6B724: ("apex_shockwave_volume", structs.decode_BIG_f),
    0x4032C58A: ("unknown_0x4032c58a", structs.decode_BIG_f),
    0x8B6E162F: ("unknown_0x8b6e162f", structs.decode_BIG_f),
    0x966B2697: ("unknown_0x966b2697", structs.decode_BIG_f),
}
