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

    class UnknownStruct30Json(typing_extensions.TypedDict):
        weapon_system: int
        damage: json_util.JsonObject
        visor_effect: int
        visor_impact_sound: int
        unknown_0x2f79b3d0: float
        unknown_0x11cc7b58: float


@dataclasses.dataclass()
class UnknownStruct30(BaseProperty):
    weapon_system: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x459AE4A8, original_name="WeaponSystem"),
        },
    )
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
    visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART", "ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE9C8E2BD, original_name="VisorEffect"),
        },
    )
    visor_impact_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x86FFB3F6, original_name="VisorImpactSound"),
        },
    )
    unknown_0x2f79b3d0: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2F79B3D0, original_name="Unknown"),
        },
    )
    unknown_0x11cc7b58: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x11CC7B58, original_name="Unknown"),
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
        assert property_id == 0x459AE4A8
        weapon_system = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9C8E2BD
        visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86FFB3F6
        visor_impact_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F79B3D0
        unknown_0x2f79b3d0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11CC7B58
        unknown_0x11cc7b58 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(weapon_system, damage, visor_effect, visor_impact_sound, unknown_0x2f79b3d0, unknown_0x11cc7b58)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"E\x9a\xe4\xa8")  # 0x459ae4a8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.weapon_system))

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe9\xc8\xe2\xbd")  # 0xe9c8e2bd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_effect))

        data.write(b"\x86\xff\xb3\xf6")  # 0x86ffb3f6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_impact_sound))

        data.write(b"/y\xb3\xd0")  # 0x2f79b3d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2f79b3d0))

        data.write(b"\x11\xcc{X")  # 0x11cc7b58
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x11cc7b58))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct30Json", data)
        return cls(
            weapon_system=json_data["weapon_system"],
            damage=DamageInfo.from_json(json_data["damage"]),
            visor_effect=json_data["visor_effect"],
            visor_impact_sound=json_data["visor_impact_sound"],
            unknown_0x2f79b3d0=json_data["unknown_0x2f79b3d0"],
            unknown_0x11cc7b58=json_data["unknown_0x11cc7b58"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "weapon_system": self.weapon_system,
            "damage": self.damage.to_json(),
            "visor_effect": self.visor_effect,
            "visor_impact_sound": self.visor_impact_sound,
            "unknown_0x2f79b3d0": self.unknown_0x2f79b3d0,
            "unknown_0x11cc7b58": self.unknown_0x11cc7b58,
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x459AE4A8: ("weapon_system", structs.decode_BIG_Q),
    0x337F9524: ("damage", _decode_damage),
    0xE9C8E2BD: ("visor_effect", structs.decode_BIG_Q),
    0x86FFB3F6: ("visor_impact_sound", structs.decode_BIG_Q),
    0x2F79B3D0: ("unknown_0x2f79b3d0", structs.decode_BIG_f),
    0x11CC7B58: ("unknown_0x11cc7b58", structs.decode_BIG_f),
}
