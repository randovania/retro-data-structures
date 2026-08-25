# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.CircleLineMode import CircleLineMode
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.GhorStructB import GhorStructB
from retro_data_structures.properties.corruption.archetypes.GhorStructC import GhorStructC
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.UnknownStruct38 import UnknownStruct38
from retro_data_structures.properties.corruption.archetypes.UnknownStruct39 import UnknownStruct39
from retro_data_structures.properties.corruption.archetypes.UnknownStruct40 import UnknownStruct40
from retro_data_structures.properties.corruption.archetypes.UnknownStruct41 import UnknownStruct41
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct42Json(typing_extensions.TypedDict):
        is_gandrayda: bool
        unknown_struct38: json_util.JsonObject
        unknown_struct39: json_util.JsonObject
        circle_line_mode: json_util.JsonObject
        ghor_struct_c_0xd345f07f: json_util.JsonObject
        face_effect: str
        ghor_struct_c_0x391a32ae: json_util.JsonObject
        ghor_struct_c_0xafb9313a: json_util.JsonObject
        damage_vulnerability: json_util.JsonObject
        unknown_struct40: json_util.JsonObject
        ghor_struct_c_0x810ec49a: json_util.JsonObject
        unknown_struct41: json_util.JsonObject
        ghor_struct_b_0x0e07b299: json_util.JsonObject
        ghor_struct_b_0x73e98b8f: json_util.JsonObject
        rotate_body_sound: int
        lock_on_locator: str
        energy_bar_string: str
        health_info_0x3d43820c: json_util.JsonObject
        health_info_0x6ed9d988: json_util.JsonObject
        health_info_0xe97f12cb: json_util.JsonObject
        unknown_0xd16b54f9: float
        unknown_0xb40c6fbf: float
        unknown_0x2443e8ec: json_util.JsonValue
        unknown_0x888049bd: json_util.JsonValue


@dataclasses.dataclass()
class UnknownStruct42(BaseProperty):
    is_gandrayda: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x531A8C85, original_name="IsGandrayda"),
        },
    )
    unknown_struct38: UnknownStruct38 = dataclasses.field(
        default_factory=UnknownStruct38,
        metadata={
            "reflection": FieldReflection[UnknownStruct38](
                UnknownStruct38,
                id=0x832C442E,
                original_name="UnknownStruct38",
                from_json=UnknownStruct38.from_json,
                to_json=UnknownStruct38.to_json,
            ),
        },
    )
    unknown_struct39: UnknownStruct39 = dataclasses.field(
        default_factory=UnknownStruct39,
        metadata={
            "reflection": FieldReflection[UnknownStruct39](
                UnknownStruct39,
                id=0xA0D0963B,
                original_name="UnknownStruct39",
                from_json=UnknownStruct39.from_json,
                to_json=UnknownStruct39.to_json,
            ),
        },
    )
    circle_line_mode: CircleLineMode = dataclasses.field(
        default_factory=CircleLineMode,
        metadata={
            "reflection": FieldReflection[CircleLineMode](
                CircleLineMode,
                id=0x81CC0D22,
                original_name="CircleLineMode",
                from_json=CircleLineMode.from_json,
                to_json=CircleLineMode.to_json,
            ),
        },
    )
    ghor_struct_c_0xd345f07f: GhorStructC = dataclasses.field(
        default_factory=GhorStructC,
        metadata={
            "reflection": FieldReflection[GhorStructC](
                GhorStructC,
                id=0xD345F07F,
                original_name="GhorStructC",
                from_json=GhorStructC.from_json,
                to_json=GhorStructC.to_json,
            ),
        },
    )
    face_effect: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xC59D1A2D, original_name="FaceEffect"),
        },
    )
    ghor_struct_c_0x391a32ae: GhorStructC = dataclasses.field(
        default_factory=GhorStructC,
        metadata={
            "reflection": FieldReflection[GhorStructC](
                GhorStructC,
                id=0x391A32AE,
                original_name="GhorStructC",
                from_json=GhorStructC.from_json,
                to_json=GhorStructC.to_json,
            ),
        },
    )
    ghor_struct_c_0xafb9313a: GhorStructC = dataclasses.field(
        default_factory=GhorStructC,
        metadata={
            "reflection": FieldReflection[GhorStructC](
                GhorStructC,
                id=0xAFB9313A,
                original_name="GhorStructC",
                from_json=GhorStructC.from_json,
                to_json=GhorStructC.to_json,
            ),
        },
    )
    damage_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xBA4AD147,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_struct40: UnknownStruct40 = dataclasses.field(
        default_factory=UnknownStruct40,
        metadata={
            "reflection": FieldReflection[UnknownStruct40](
                UnknownStruct40,
                id=0x305CDAD2,
                original_name="UnknownStruct40",
                from_json=UnknownStruct40.from_json,
                to_json=UnknownStruct40.to_json,
            ),
        },
    )
    ghor_struct_c_0x810ec49a: GhorStructC = dataclasses.field(
        default_factory=GhorStructC,
        metadata={
            "reflection": FieldReflection[GhorStructC](
                GhorStructC,
                id=0x810EC49A,
                original_name="GhorStructC",
                from_json=GhorStructC.from_json,
                to_json=GhorStructC.to_json,
            ),
        },
    )
    unknown_struct41: UnknownStruct41 = dataclasses.field(
        default_factory=UnknownStruct41,
        metadata={
            "reflection": FieldReflection[UnknownStruct41](
                UnknownStruct41,
                id=0x5B772F6D,
                original_name="UnknownStruct41",
                from_json=UnknownStruct41.from_json,
                to_json=UnknownStruct41.to_json,
            ),
        },
    )
    ghor_struct_b_0x0e07b299: GhorStructB = dataclasses.field(
        default_factory=GhorStructB,
        metadata={
            "reflection": FieldReflection[GhorStructB](
                GhorStructB,
                id=0x0E07B299,
                original_name="GhorStructB",
                from_json=GhorStructB.from_json,
                to_json=GhorStructB.to_json,
            ),
        },
    )
    ghor_struct_b_0x73e98b8f: GhorStructB = dataclasses.field(
        default_factory=GhorStructB,
        metadata={
            "reflection": FieldReflection[GhorStructB](
                GhorStructB,
                id=0x73E98B8F,
                original_name="GhorStructB",
                from_json=GhorStructB.from_json,
                to_json=GhorStructB.to_json,
            ),
        },
    )
    rotate_body_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x15E3F283, original_name="RotateBodySound"),
        },
    )
    lock_on_locator: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x79BFD886, original_name="LockOnLocator"),
        },
    )
    energy_bar_string: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x337C4056, original_name="EnergyBarString"),
        },
    )
    health_info_0x3d43820c: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0x3D43820C,
                original_name="HealthInfo",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    health_info_0x6ed9d988: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0x6ED9D988,
                original_name="HealthInfo",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    health_info_0xe97f12cb: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xE97F12CB,
                original_name="HealthInfo",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    unknown_0xd16b54f9: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD16B54F9, original_name="Unknown"),
        },
    )
    unknown_0xb40c6fbf: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB40C6FBF, original_name="Unknown"),
        },
    )
    unknown_0x2443e8ec: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x2443E8EC, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x888049bd: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x888049BD, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 24:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531A8C85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x832C442E
        unknown_struct38 = UnknownStruct38.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA0D0963B
        unknown_struct39 = UnknownStruct39.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81CC0D22
        circle_line_mode = CircleLineMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD345F07F
        ghor_struct_c_0xd345f07f = GhorStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC59D1A2D
        face_effect = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x391A32AE
        ghor_struct_c_0x391a32ae = GhorStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAFB9313A
        ghor_struct_c_0xafb9313a = GhorStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA4AD147
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x305CDAD2
        unknown_struct40 = UnknownStruct40.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x810EC49A
        ghor_struct_c_0x810ec49a = GhorStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B772F6D
        unknown_struct41 = UnknownStruct41.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0E07B299
        ghor_struct_b_0x0e07b299 = GhorStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73E98B8F
        ghor_struct_b_0x73e98b8f = GhorStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15E3F283
        rotate_body_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79BFD886
        lock_on_locator = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337C4056
        energy_bar_string = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D43820C
        health_info_0x3d43820c = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ED9D988
        health_info_0x6ed9d988 = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE97F12CB
        health_info_0xe97f12cb = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD16B54F9
        unknown_0xd16b54f9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB40C6FBF
        unknown_0xb40c6fbf = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2443E8EC
        unknown_0x2443e8ec = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x888049BD
        unknown_0x888049bd = Color.from_stream(data, game, property_size)

        return cls(
            is_gandrayda,
            unknown_struct38,
            unknown_struct39,
            circle_line_mode,
            ghor_struct_c_0xd345f07f,
            face_effect,
            ghor_struct_c_0x391a32ae,
            ghor_struct_c_0xafb9313a,
            damage_vulnerability,
            unknown_struct40,
            ghor_struct_c_0x810ec49a,
            unknown_struct41,
            ghor_struct_b_0x0e07b299,
            ghor_struct_b_0x73e98b8f,
            rotate_body_sound,
            lock_on_locator,
            energy_bar_string,
            health_info_0x3d43820c,
            health_info_0x6ed9d988,
            health_info_0xe97f12cb,
            unknown_0xd16b54f9,
            unknown_0xb40c6fbf,
            unknown_0x2443e8ec,
            unknown_0x888049bd,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x18")  # 24 properties

        data.write(b"S\x1a\x8c\x85")  # 0x531a8c85
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b"\x83,D.")  # 0x832c442e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct38.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa0\xd0\x96;")  # 0xa0d0963b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct39.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x81\xcc\r"')  # 0x81cc0d22
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.circle_line_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd3E\xf0\x7f")  # 0xd345f07f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_c_0xd345f07f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc5\x9d\x1a-")  # 0xc59d1a2d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.face_effect.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"9\x1a2\xae")  # 0x391a32ae
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_c_0x391a32ae.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaf\xb91:")  # 0xafb9313a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_c_0xafb9313a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbaJ\xd1G")  # 0xba4ad147
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"0\\\xda\xd2")  # 0x305cdad2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct40.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x81\x0e\xc4\x9a")  # 0x810ec49a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_c_0x810ec49a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"[w/m")  # 0x5b772f6d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct41.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0e\x07\xb2\x99")  # 0xe07b299
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_b_0x0e07b299.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"s\xe9\x8b\x8f")  # 0x73e98b8f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_b_0x73e98b8f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x15\xe3\xf2\x83")  # 0x15e3f283
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.rotate_body_sound))

        data.write(b"y\xbf\xd8\x86")  # 0x79bfd886
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.lock_on_locator.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3|@V")  # 0x337c4056
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.energy_bar_string.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"=C\x82\x0c")  # 0x3d43820c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health_info_0x3d43820c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"n\xd9\xd9\x88")  # 0x6ed9d988
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health_info_0x6ed9d988.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe9\x7f\x12\xcb")  # 0xe97f12cb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health_info_0xe97f12cb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd1kT\xf9")  # 0xd16b54f9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd16b54f9))

        data.write(b"\xb4\x0co\xbf")  # 0xb40c6fbf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb40c6fbf))

        data.write(b"$C\xe8\xec")  # 0x2443e8ec
        data.write(b"\x00\x10")  # size
        self.unknown_0x2443e8ec.to_stream(data, game)

        data.write(b"\x88\x80I\xbd")  # 0x888049bd
        data.write(b"\x00\x10")  # size
        self.unknown_0x888049bd.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct42Json", data)
        return cls(
            is_gandrayda=json_data["is_gandrayda"],
            unknown_struct38=UnknownStruct38.from_json(json_data["unknown_struct38"]),
            unknown_struct39=UnknownStruct39.from_json(json_data["unknown_struct39"]),
            circle_line_mode=CircleLineMode.from_json(json_data["circle_line_mode"]),
            ghor_struct_c_0xd345f07f=GhorStructC.from_json(json_data["ghor_struct_c_0xd345f07f"]),
            face_effect=json_data["face_effect"],
            ghor_struct_c_0x391a32ae=GhorStructC.from_json(json_data["ghor_struct_c_0x391a32ae"]),
            ghor_struct_c_0xafb9313a=GhorStructC.from_json(json_data["ghor_struct_c_0xafb9313a"]),
            damage_vulnerability=DamageVulnerability.from_json(json_data["damage_vulnerability"]),
            unknown_struct40=UnknownStruct40.from_json(json_data["unknown_struct40"]),
            ghor_struct_c_0x810ec49a=GhorStructC.from_json(json_data["ghor_struct_c_0x810ec49a"]),
            unknown_struct41=UnknownStruct41.from_json(json_data["unknown_struct41"]),
            ghor_struct_b_0x0e07b299=GhorStructB.from_json(json_data["ghor_struct_b_0x0e07b299"]),
            ghor_struct_b_0x73e98b8f=GhorStructB.from_json(json_data["ghor_struct_b_0x73e98b8f"]),
            rotate_body_sound=json_data["rotate_body_sound"],
            lock_on_locator=json_data["lock_on_locator"],
            energy_bar_string=json_data["energy_bar_string"],
            health_info_0x3d43820c=HealthInfo.from_json(json_data["health_info_0x3d43820c"]),
            health_info_0x6ed9d988=HealthInfo.from_json(json_data["health_info_0x6ed9d988"]),
            health_info_0xe97f12cb=HealthInfo.from_json(json_data["health_info_0xe97f12cb"]),
            unknown_0xd16b54f9=json_data["unknown_0xd16b54f9"],
            unknown_0xb40c6fbf=json_data["unknown_0xb40c6fbf"],
            unknown_0x2443e8ec=Color.from_json(json_data["unknown_0x2443e8ec"]),
            unknown_0x888049bd=Color.from_json(json_data["unknown_0x888049bd"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "is_gandrayda": self.is_gandrayda,
            "unknown_struct38": self.unknown_struct38.to_json(),
            "unknown_struct39": self.unknown_struct39.to_json(),
            "circle_line_mode": self.circle_line_mode.to_json(),
            "ghor_struct_c_0xd345f07f": self.ghor_struct_c_0xd345f07f.to_json(),
            "face_effect": self.face_effect,
            "ghor_struct_c_0x391a32ae": self.ghor_struct_c_0x391a32ae.to_json(),
            "ghor_struct_c_0xafb9313a": self.ghor_struct_c_0xafb9313a.to_json(),
            "damage_vulnerability": self.damage_vulnerability.to_json(),
            "unknown_struct40": self.unknown_struct40.to_json(),
            "ghor_struct_c_0x810ec49a": self.ghor_struct_c_0x810ec49a.to_json(),
            "unknown_struct41": self.unknown_struct41.to_json(),
            "ghor_struct_b_0x0e07b299": self.ghor_struct_b_0x0e07b299.to_json(),
            "ghor_struct_b_0x73e98b8f": self.ghor_struct_b_0x73e98b8f.to_json(),
            "rotate_body_sound": self.rotate_body_sound,
            "lock_on_locator": self.lock_on_locator,
            "energy_bar_string": self.energy_bar_string,
            "health_info_0x3d43820c": self.health_info_0x3d43820c.to_json(),
            "health_info_0x6ed9d988": self.health_info_0x6ed9d988.to_json(),
            "health_info_0xe97f12cb": self.health_info_0xe97f12cb.to_json(),
            "unknown_0xd16b54f9": self.unknown_0xd16b54f9,
            "unknown_0xb40c6fbf": self.unknown_0xb40c6fbf,
            "unknown_0x2443e8ec": self.unknown_0x2443e8ec.to_json(),
            "unknown_0x888049bd": self.unknown_0x888049bd.to_json(),
        }


def _decode_unknown_struct38(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct38:
    return UnknownStruct38.from_stream(data, game, property_size)


def _decode_unknown_struct39(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct39:
    return UnknownStruct39.from_stream(data, game, property_size)


def _decode_circle_line_mode(data: typing.BinaryIO, game: Game, property_size: int) -> CircleLineMode:
    return CircleLineMode.from_stream(data, game, property_size)


def _decode_ghor_struct_c_0xd345f07f(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructC:
    return GhorStructC.from_stream(data, game, property_size)


def _decode_face_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_ghor_struct_c_0x391a32ae(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructC:
    return GhorStructC.from_stream(data, game, property_size)


def _decode_ghor_struct_c_0xafb9313a(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructC:
    return GhorStructC.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_unknown_struct40(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct40:
    return UnknownStruct40.from_stream(data, game, property_size)


def _decode_ghor_struct_c_0x810ec49a(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructC:
    return GhorStructC.from_stream(data, game, property_size)


def _decode_unknown_struct41(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct41:
    return UnknownStruct41.from_stream(data, game, property_size)


def _decode_ghor_struct_b_0x0e07b299(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructB:
    return GhorStructB.from_stream(data, game, property_size)


def _decode_ghor_struct_b_0x73e98b8f(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructB:
    return GhorStructB.from_stream(data, game, property_size)


def _decode_lock_on_locator(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_energy_bar_string(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_health_info_0x3d43820c(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_health_info_0x6ed9d988(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_health_info_0xe97f12cb(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_unknown_0x2443e8ec(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x888049bd(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x531A8C85: ("is_gandrayda", structs.decode_BIG_bool_),
    0x832C442E: ("unknown_struct38", _decode_unknown_struct38),
    0xA0D0963B: ("unknown_struct39", _decode_unknown_struct39),
    0x81CC0D22: ("circle_line_mode", _decode_circle_line_mode),
    0xD345F07F: ("ghor_struct_c_0xd345f07f", _decode_ghor_struct_c_0xd345f07f),
    0xC59D1A2D: ("face_effect", _decode_face_effect),
    0x391A32AE: ("ghor_struct_c_0x391a32ae", _decode_ghor_struct_c_0x391a32ae),
    0xAFB9313A: ("ghor_struct_c_0xafb9313a", _decode_ghor_struct_c_0xafb9313a),
    0xBA4AD147: ("damage_vulnerability", _decode_damage_vulnerability),
    0x305CDAD2: ("unknown_struct40", _decode_unknown_struct40),
    0x810EC49A: ("ghor_struct_c_0x810ec49a", _decode_ghor_struct_c_0x810ec49a),
    0x5B772F6D: ("unknown_struct41", _decode_unknown_struct41),
    0x0E07B299: ("ghor_struct_b_0x0e07b299", _decode_ghor_struct_b_0x0e07b299),
    0x73E98B8F: ("ghor_struct_b_0x73e98b8f", _decode_ghor_struct_b_0x73e98b8f),
    0x15E3F283: ("rotate_body_sound", structs.decode_BIG_Q),
    0x79BFD886: ("lock_on_locator", _decode_lock_on_locator),
    0x337C4056: ("energy_bar_string", _decode_energy_bar_string),
    0x3D43820C: ("health_info_0x3d43820c", _decode_health_info_0x3d43820c),
    0x6ED9D988: ("health_info_0x6ed9d988", _decode_health_info_0x6ed9d988),
    0xE97F12CB: ("health_info_0xe97f12cb", _decode_health_info_0xe97f12cb),
    0xD16B54F9: ("unknown_0xd16b54f9", structs.decode_BIG_f),
    0xB40C6FBF: ("unknown_0xb40c6fbf", structs.decode_BIG_f),
    0x2443E8EC: ("unknown_0x2443e8ec", _decode_unknown_0x2443e8ec),
    0x888049BD: ("unknown_0x888049bd", _decode_unknown_0x888049bd),
}
