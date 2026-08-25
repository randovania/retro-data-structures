# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.GrappleBlock import GrappleBlock
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class JetPackJson(typing_extensions.TypedDict):
        unknown: float
        grapple_stunned_time: float
        stunned_hover_height: float
        stunned_hover_speed: float
        part_0x2c79052c: int
        part_0x016b65a9: int
        part_0xd8a92aaa: int
        spin_death_damage: json_util.JsonObject
        stunned_grapple_block: json_util.JsonObject


@dataclasses.dataclass()
class JetPack(BaseProperty):
    unknown: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6E9D30E, original_name="Unknown"),
        },
    )
    grapple_stunned_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9E9D2BD6, original_name="GrappleStunnedTime"),
        },
    )
    stunned_hover_height: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF3A72AF9, original_name="StunnedHoverHeight"),
        },
    )
    stunned_hover_speed: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14355BE0, original_name="StunnedHoverSpeed"),
        },
    )
    part_0x2c79052c: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2C79052C, original_name="PART"),
        },
    )
    part_0x016b65a9: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x016B65A9, original_name="PART"),
        },
    )
    part_0xd8a92aaa: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD8A92AAA, original_name="PART"),
        },
    )
    spin_death_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x5BF6F8E4,
                original_name="SpinDeathDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    stunned_grapple_block: GrappleBlock = dataclasses.field(
        default_factory=GrappleBlock,
        metadata={
            "reflection": FieldReflection[GrappleBlock](
                GrappleBlock,
                id=0x85543E4E,
                original_name="StunnedGrappleBlock",
                from_json=GrappleBlock.from_json,
                to_json=GrappleBlock.to_json,
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
        assert property_id == 0xC6E9D30E
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9E9D2BD6
        grapple_stunned_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3A72AF9
        stunned_hover_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14355BE0
        stunned_hover_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C79052C
        part_0x2c79052c = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x016B65A9
        part_0x016b65a9 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8A92AAA
        part_0xd8a92aaa = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BF6F8E4
        spin_death_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85543E4E
        stunned_grapple_block = GrappleBlock.from_stream(data, game, property_size)

        return cls(
            unknown,
            grapple_stunned_time,
            stunned_hover_height,
            stunned_hover_speed,
            part_0x2c79052c,
            part_0x016b65a9,
            part_0xd8a92aaa,
            spin_death_damage,
            stunned_grapple_block,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"\xc6\xe9\xd3\x0e")  # 0xc6e9d30e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x9e\x9d+\xd6")  # 0x9e9d2bd6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_stunned_time))

        data.write(b"\xf3\xa7*\xf9")  # 0xf3a72af9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stunned_hover_height))

        data.write(b"\x145[\xe0")  # 0x14355be0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stunned_hover_speed))

        data.write(b",y\x05,")  # 0x2c79052c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x2c79052c))

        data.write(b"\x01ke\xa9")  # 0x16b65a9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x016b65a9))

        data.write(b"\xd8\xa9*\xaa")  # 0xd8a92aaa
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xd8a92aaa))

        data.write(b"[\xf6\xf8\xe4")  # 0x5bf6f8e4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spin_death_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x85T>N")  # 0x85543e4e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stunned_grapple_block.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("JetPackJson", data)
        return cls(
            unknown=json_data["unknown"],
            grapple_stunned_time=json_data["grapple_stunned_time"],
            stunned_hover_height=json_data["stunned_hover_height"],
            stunned_hover_speed=json_data["stunned_hover_speed"],
            part_0x2c79052c=json_data["part_0x2c79052c"],
            part_0x016b65a9=json_data["part_0x016b65a9"],
            part_0xd8a92aaa=json_data["part_0xd8a92aaa"],
            spin_death_damage=DamageInfo.from_json(json_data["spin_death_damage"]),
            stunned_grapple_block=GrappleBlock.from_json(json_data["stunned_grapple_block"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown": self.unknown,
            "grapple_stunned_time": self.grapple_stunned_time,
            "stunned_hover_height": self.stunned_hover_height,
            "stunned_hover_speed": self.stunned_hover_speed,
            "part_0x2c79052c": self.part_0x2c79052c,
            "part_0x016b65a9": self.part_0x016b65a9,
            "part_0xd8a92aaa": self.part_0xd8a92aaa,
            "spin_death_damage": self.spin_death_damage.to_json(),
            "stunned_grapple_block": self.stunned_grapple_block.to_json(),
        }


def _decode_spin_death_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_stunned_grapple_block(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC6E9D30E: ("unknown", structs.decode_BIG_f),
    0x9E9D2BD6: ("grapple_stunned_time", structs.decode_BIG_f),
    0xF3A72AF9: ("stunned_hover_height", structs.decode_BIG_f),
    0x14355BE0: ("stunned_hover_speed", structs.decode_BIG_f),
    0x2C79052C: ("part_0x2c79052c", structs.decode_BIG_Q),
    0x016B65A9: ("part_0x016b65a9", structs.decode_BIG_Q),
    0xD8A92AAA: ("part_0xd8a92aaa", structs.decode_BIG_Q),
    0x5BF6F8E4: ("spin_death_damage", _decode_spin_death_damage),
    0x85543E4E: ("stunned_grapple_block", _decode_stunned_grapple_block),
}
