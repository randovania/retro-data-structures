# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DestructibleBarrierJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_0xcd4f7e71: int
        unknown_0xa7f551f7: int
        unknown_0x609c6240: int
        chunk_size: json_util.JsonValue
        left_model: int
        center_model: int
        right_model: int
        unknown_0x396660b4: int
        unknown_0x48e25884: int
        base_model: int
        unknown_0x1eb90d06: int
        unknown_0x9d852dfe: int
        unknown_0x982d7fa8: int
        unknown_0x2e11003d: int
        unknown_0x5371ac0d: int
        unknown_0x409d1b7c: int
        unknown_0x4e749cb5: int
        unknown_0x92485dfa: int
        unknown_0x6e4a9d27: int
        unknown_0xbc2381a6: int
        unknown_0x6575a3d5: int
        unknown_0xc91b0946: int
        unknown_0x4b2d5a37: int
        unknown_0x605847b9: float
        unknown_0xcd9c67fe: float
        unknown_0x0af428b4: float
        unknown_0x4d3109e3: bool
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        actor_information: json_util.JsonObject


@dataclasses.dataclass()
class DestructibleBarrier(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    unknown_0xcd4f7e71: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCD4F7E71, original_name="Unknown"),
        },
    )
    unknown_0xa7f551f7: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA7F551F7, original_name="Unknown"),
        },
    )
    unknown_0x609c6240: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x609C6240, original_name="Unknown"),
        },
    )
    chunk_size: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.5, y=0.20000000298023224, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xB29E159E, original_name="ChunkSize", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    left_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x014A0C36, original_name="LeftModel"),
        },
    )
    center_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x90F55C5D, original_name="CenterModel"),
        },
    )
    right_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE1975355, original_name="RightModel"),
        },
    )
    unknown_0x396660b4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x396660B4, original_name="Unknown"),
        },
    )
    unknown_0x48e25884: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x48E25884, original_name="Unknown"),
        },
    )
    base_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF1ABB2C7, original_name="BaseModel"),
        },
    )
    unknown_0x1eb90d06: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1EB90D06, original_name="Unknown"),
        },
    )
    unknown_0x9d852dfe: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9D852DFE, original_name="Unknown"),
        },
    )
    unknown_0x982d7fa8: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x982D7FA8, original_name="Unknown"),
        },
    )
    unknown_0x2e11003d: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2E11003D, original_name="Unknown"),
        },
    )
    unknown_0x5371ac0d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5371AC0D, original_name="Unknown"),
        },
    )
    unknown_0x409d1b7c: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x409D1B7C, original_name="Unknown"),
        },
    )
    unknown_0x4e749cb5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4E749CB5, original_name="Unknown"),
        },
    )
    unknown_0x92485dfa: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x92485DFA, original_name="Unknown"),
        },
    )
    unknown_0x6e4a9d27: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6E4A9D27, original_name="Unknown"),
        },
    )
    unknown_0xbc2381a6: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBC2381A6, original_name="Unknown"),
        },
    )
    unknown_0x6575a3d5: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6575A3D5, original_name="Unknown"),
        },
    )
    unknown_0xc91b0946: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC91B0946, original_name="Unknown"),
        },
    )
    unknown_0x4b2d5a37: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x4B2D5A37, original_name="Unknown"),
        },
    )
    unknown_0x605847b9: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x605847B9, original_name="Unknown"),
        },
    )
    unknown_0xcd9c67fe: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD9C67FE, original_name="Unknown"),
        },
    )
    unknown_0x0af428b4: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0AF428B4, original_name="Unknown"),
        },
    )
    unknown_0x4d3109e3: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4D3109E3, original_name="Unknown"),
        },
    )
    health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xCF90D15E,
                original_name="Health",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
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
    actor_information: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x7E397FED,
                original_name="ActorInformation",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DBAR"

    @classmethod
    def modules(cls) -> list[str]:
        return ["DestructibleBarrier.rel"]

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
        if property_count != 31:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD4F7E71
        unknown_0xcd4f7e71 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA7F551F7
        unknown_0xa7f551f7 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x609C6240
        unknown_0x609c6240 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB29E159E
        chunk_size = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x014A0C36
        left_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90F55C5D
        center_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1975355
        right_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x396660B4
        unknown_0x396660b4 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48E25884
        unknown_0x48e25884 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1ABB2C7
        base_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1EB90D06
        unknown_0x1eb90d06 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9D852DFE
        unknown_0x9d852dfe = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x982D7FA8
        unknown_0x982d7fa8 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E11003D
        unknown_0x2e11003d = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5371AC0D
        unknown_0x5371ac0d = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x409D1B7C
        unknown_0x409d1b7c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4E749CB5
        unknown_0x4e749cb5 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92485DFA
        unknown_0x92485dfa = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E4A9D27
        unknown_0x6e4a9d27 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC2381A6
        unknown_0xbc2381a6 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6575A3D5
        unknown_0x6575a3d5 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC91B0946
        unknown_0xc91b0946 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B2D5A37
        unknown_0x4b2d5a37 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x605847B9
        unknown_0x605847b9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD9C67FE
        unknown_0xcd9c67fe = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0AF428B4
        unknown_0x0af428b4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D3109E3
        unknown_0x4d3109e3 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            unknown_0xcd4f7e71,
            unknown_0xa7f551f7,
            unknown_0x609c6240,
            chunk_size,
            left_model,
            center_model,
            right_model,
            unknown_0x396660b4,
            unknown_0x48e25884,
            base_model,
            unknown_0x1eb90d06,
            unknown_0x9d852dfe,
            unknown_0x982d7fa8,
            unknown_0x2e11003d,
            unknown_0x5371ac0d,
            unknown_0x409d1b7c,
            unknown_0x4e749cb5,
            unknown_0x92485dfa,
            unknown_0x6e4a9d27,
            unknown_0xbc2381a6,
            unknown_0x6575a3d5,
            unknown_0xc91b0946,
            unknown_0x4b2d5a37,
            unknown_0x605847b9,
            unknown_0xcd9c67fe,
            unknown_0x0af428b4,
            unknown_0x4d3109e3,
            health,
            vulnerability,
            actor_information,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x1f")  # 31 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcdO~q")  # 0xcd4f7e71
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xcd4f7e71))

        data.write(b"\xa7\xf5Q\xf7")  # 0xa7f551f7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa7f551f7))

        data.write(b"`\x9cb@")  # 0x609c6240
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x609c6240))

        data.write(b"\xb2\x9e\x15\x9e")  # 0xb29e159e
        data.write(b"\x00\x0c")  # size
        self.chunk_size.to_stream(data, game)

        data.write(b"\x01J\x0c6")  # 0x14a0c36
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.left_model))

        data.write(b"\x90\xf5\\]")  # 0x90f55c5d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.center_model))

        data.write(b"\xe1\x97SU")  # 0xe1975355
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.right_model))

        data.write(b"9f`\xb4")  # 0x396660b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x396660b4))

        data.write(b"H\xe2X\x84")  # 0x48e25884
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x48e25884))

        data.write(b"\xf1\xab\xb2\xc7")  # 0xf1abb2c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.base_model))

        data.write(b"\x1e\xb9\r\x06")  # 0x1eb90d06
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x1eb90d06))

        data.write(b"\x9d\x85-\xfe")  # 0x9d852dfe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9d852dfe))

        data.write(b"\x98-\x7f\xa8")  # 0x982d7fa8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x982d7fa8))

        data.write(b".\x11\x00=")  # 0x2e11003d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x2e11003d))

        data.write(b"Sq\xac\r")  # 0x5371ac0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x5371ac0d))

        data.write(b"@\x9d\x1b|")  # 0x409d1b7c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x409d1b7c))

        data.write(b"Nt\x9c\xb5")  # 0x4e749cb5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x4e749cb5))

        data.write(b"\x92H]\xfa")  # 0x92485dfa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x92485dfa))

        data.write(b"nJ\x9d'")  # 0x6e4a9d27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6e4a9d27))

        data.write(b"\xbc#\x81\xa6")  # 0xbc2381a6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xbc2381a6))

        data.write(b"eu\xa3\xd5")  # 0x6575a3d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6575a3d5))

        data.write(b"\xc9\x1b\tF")  # 0xc91b0946
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc91b0946))

        data.write(b"K-Z7")  # 0x4b2d5a37
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x4b2d5a37))

        data.write(b"`XG\xb9")  # 0x605847b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x605847b9))

        data.write(b"\xcd\x9cg\xfe")  # 0xcd9c67fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd9c67fe))

        data.write(b"\n\xf4(\xb4")  # 0xaf428b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0af428b4))

        data.write(b"M1\t\xe3")  # 0x4d3109e3
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4d3109e3))

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
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

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DestructibleBarrierJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            unknown_0xcd4f7e71=json_data["unknown_0xcd4f7e71"],
            unknown_0xa7f551f7=json_data["unknown_0xa7f551f7"],
            unknown_0x609c6240=json_data["unknown_0x609c6240"],
            chunk_size=Vector.from_json(json_data["chunk_size"]),
            left_model=json_data["left_model"],
            center_model=json_data["center_model"],
            right_model=json_data["right_model"],
            unknown_0x396660b4=json_data["unknown_0x396660b4"],
            unknown_0x48e25884=json_data["unknown_0x48e25884"],
            base_model=json_data["base_model"],
            unknown_0x1eb90d06=json_data["unknown_0x1eb90d06"],
            unknown_0x9d852dfe=json_data["unknown_0x9d852dfe"],
            unknown_0x982d7fa8=json_data["unknown_0x982d7fa8"],
            unknown_0x2e11003d=json_data["unknown_0x2e11003d"],
            unknown_0x5371ac0d=json_data["unknown_0x5371ac0d"],
            unknown_0x409d1b7c=json_data["unknown_0x409d1b7c"],
            unknown_0x4e749cb5=json_data["unknown_0x4e749cb5"],
            unknown_0x92485dfa=json_data["unknown_0x92485dfa"],
            unknown_0x6e4a9d27=json_data["unknown_0x6e4a9d27"],
            unknown_0xbc2381a6=json_data["unknown_0xbc2381a6"],
            unknown_0x6575a3d5=json_data["unknown_0x6575a3d5"],
            unknown_0xc91b0946=json_data["unknown_0xc91b0946"],
            unknown_0x4b2d5a37=json_data["unknown_0x4b2d5a37"],
            unknown_0x605847b9=json_data["unknown_0x605847b9"],
            unknown_0xcd9c67fe=json_data["unknown_0xcd9c67fe"],
            unknown_0x0af428b4=json_data["unknown_0x0af428b4"],
            unknown_0x4d3109e3=json_data["unknown_0x4d3109e3"],
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "unknown_0xcd4f7e71": self.unknown_0xcd4f7e71,
            "unknown_0xa7f551f7": self.unknown_0xa7f551f7,
            "unknown_0x609c6240": self.unknown_0x609c6240,
            "chunk_size": self.chunk_size.to_json(),
            "left_model": self.left_model,
            "center_model": self.center_model,
            "right_model": self.right_model,
            "unknown_0x396660b4": self.unknown_0x396660b4,
            "unknown_0x48e25884": self.unknown_0x48e25884,
            "base_model": self.base_model,
            "unknown_0x1eb90d06": self.unknown_0x1eb90d06,
            "unknown_0x9d852dfe": self.unknown_0x9d852dfe,
            "unknown_0x982d7fa8": self.unknown_0x982d7fa8,
            "unknown_0x2e11003d": self.unknown_0x2e11003d,
            "unknown_0x5371ac0d": self.unknown_0x5371ac0d,
            "unknown_0x409d1b7c": self.unknown_0x409d1b7c,
            "unknown_0x4e749cb5": self.unknown_0x4e749cb5,
            "unknown_0x92485dfa": self.unknown_0x92485dfa,
            "unknown_0x6e4a9d27": self.unknown_0x6e4a9d27,
            "unknown_0xbc2381a6": self.unknown_0xbc2381a6,
            "unknown_0x6575a3d5": self.unknown_0x6575a3d5,
            "unknown_0xc91b0946": self.unknown_0xc91b0946,
            "unknown_0x4b2d5a37": self.unknown_0x4b2d5a37,
            "unknown_0x605847b9": self.unknown_0x605847b9,
            "unknown_0xcd9c67fe": self.unknown_0xcd9c67fe,
            "unknown_0x0af428b4": self.unknown_0x0af428b4,
            "unknown_0x4d3109e3": self.unknown_0x4d3109e3,
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "actor_information": self.actor_information.to_json(),
        }

    def _dependencies_for_left_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_model)

    def _dependencies_for_center_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.center_model)

    def _dependencies_for_right_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_model)

    def _dependencies_for_unknown_0x396660b4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x396660b4)

    def _dependencies_for_unknown_0x48e25884(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x48e25884)

    def _dependencies_for_base_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.base_model)

    def _dependencies_for_unknown_0x1eb90d06(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x1eb90d06)

    def _dependencies_for_unknown_0x982d7fa8(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x982d7fa8)

    def _dependencies_for_unknown_0x5371ac0d(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x5371ac0d)

    def _dependencies_for_unknown_0x4e749cb5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x4e749cb5)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_left_model, "left_model", "AssetId"),
            (self._dependencies_for_center_model, "center_model", "AssetId"),
            (self._dependencies_for_right_model, "right_model", "AssetId"),
            (self._dependencies_for_unknown_0x396660b4, "unknown_0x396660b4", "AssetId"),
            (self._dependencies_for_unknown_0x48e25884, "unknown_0x48e25884", "AssetId"),
            (self._dependencies_for_base_model, "base_model", "AssetId"),
            (self._dependencies_for_unknown_0x1eb90d06, "unknown_0x1eb90d06", "AssetId"),
            (self._dependencies_for_unknown_0x982d7fa8, "unknown_0x982d7fa8", "AssetId"),
            (self._dependencies_for_unknown_0x5371ac0d, "unknown_0x5371ac0d", "AssetId"),
            (self._dependencies_for_unknown_0x4e749cb5, "unknown_0x4e749cb5", "AssetId"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for DestructibleBarrier.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_chunk_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xCD4F7E71: ("unknown_0xcd4f7e71", structs.decode_BIG_l),
    0xA7F551F7: ("unknown_0xa7f551f7", structs.decode_BIG_l),
    0x609C6240: ("unknown_0x609c6240", structs.decode_BIG_l),
    0xB29E159E: ("chunk_size", _decode_chunk_size),
    0x014A0C36: ("left_model", structs.decode_BIG_L),
    0x90F55C5D: ("center_model", structs.decode_BIG_L),
    0xE1975355: ("right_model", structs.decode_BIG_L),
    0x396660B4: ("unknown_0x396660b4", structs.decode_BIG_L),
    0x48E25884: ("unknown_0x48e25884", structs.decode_BIG_L),
    0xF1ABB2C7: ("base_model", structs.decode_BIG_L),
    0x1EB90D06: ("unknown_0x1eb90d06", structs.decode_BIG_L),
    0x9D852DFE: ("unknown_0x9d852dfe", structs.decode_BIG_l),
    0x982D7FA8: ("unknown_0x982d7fa8", structs.decode_BIG_L),
    0x2E11003D: ("unknown_0x2e11003d", structs.decode_BIG_l),
    0x5371AC0D: ("unknown_0x5371ac0d", structs.decode_BIG_L),
    0x409D1B7C: ("unknown_0x409d1b7c", structs.decode_BIG_l),
    0x4E749CB5: ("unknown_0x4e749cb5", structs.decode_BIG_L),
    0x92485DFA: ("unknown_0x92485dfa", structs.decode_BIG_l),
    0x6E4A9D27: ("unknown_0x6e4a9d27", structs.decode_BIG_l),
    0xBC2381A6: ("unknown_0xbc2381a6", structs.decode_BIG_l),
    0x6575A3D5: ("unknown_0x6575a3d5", structs.decode_BIG_l),
    0xC91B0946: ("unknown_0xc91b0946", structs.decode_BIG_l),
    0x4B2D5A37: ("unknown_0x4b2d5a37", structs.decode_BIG_l),
    0x605847B9: ("unknown_0x605847b9", structs.decode_BIG_f),
    0xCD9C67FE: ("unknown_0xcd9c67fe", structs.decode_BIG_f),
    0x0AF428B4: ("unknown_0x0af428b4", structs.decode_BIG_f),
    0x4D3109E3: ("unknown_0x4d3109e3", structs.decode_BIG_bool_),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0x7E397FED: ("actor_information", _decode_actor_information),
}
