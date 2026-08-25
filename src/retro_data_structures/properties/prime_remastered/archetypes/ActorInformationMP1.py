# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing
import uuid

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime_remastered.archetypes.LightingMP1 import LightingMP1
from retro_data_structures.properties.prime_remastered.archetypes.ScannableMP1 import ScannableMP1
from retro_data_structures.properties.prime_remastered.archetypes.VisorMP1 import VisorMP1
from retro_data_structures.properties.prime_remastered.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ActorInformationMP1Json(typing_extensions.TypedDict):
        unk_guid_1: str
        unk_guid_2: str
        unk_guid_3: str
        unk_guid_4: str
        unk_guid_5: str
        unk_float_1: float
        unk_bool_4: bool
        lighting: json_util.JsonObject
        scannable: json_util.JsonObject
        visor: json_util.JsonObject
        unk_float_2: float
        unk_float_3: float
        unk_float_4: float
        unk_int: int
        water_sort_type: int
        unk_bool_1: bool
        unk_bool_2: bool
        unk_bool_3: bool
        unk_bool_5: bool
        unk_bool_6: bool
        unk_bool_7: bool
        unk_bool_8: bool
        unk_bool_9: bool
        unk_bool_10: bool


def _from_json_unk_guid_1(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_unk_guid_2(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_unk_guid_3(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_unk_guid_4(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_unk_guid_5(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _to_json_unk_guid_1(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_unk_guid_2(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_unk_guid_3(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_unk_guid_4(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_unk_guid_5(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


@dataclasses.dataclass()
class ActorInformationMP1(BaseProperty):
    unk_guid_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId,
                id=0x0036D778,
                original_name="Unk GUID 1",
                from_json=_from_json_unk_guid_1,
                to_json=_to_json_unk_guid_1,
            ),
        },
    )
    unk_guid_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId,
                id=0xAB68F7A7,
                original_name="Unk GUID 2",
                from_json=_from_json_unk_guid_2,
                to_json=_to_json_unk_guid_2,
            ),
        },
    )
    unk_guid_3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId,
                id=0x802A053A,
                original_name="Unk GUID 3",
                from_json=_from_json_unk_guid_3,
                to_json=_to_json_unk_guid_3,
            ),
        },
    )
    unk_guid_4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId,
                id=0x74822F37,
                original_name="Unk GUID 4",
                from_json=_from_json_unk_guid_4,
                to_json=_to_json_unk_guid_4,
            ),
        },
    )
    unk_guid_5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId,
                id=0x0364A97A,
                original_name="Unk GUID 5",
                from_json=_from_json_unk_guid_5,
                to_json=_to_json_unk_guid_5,
            ),
        },
    )
    unk_float_1: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x36A5A738, original_name="Unk Float 1"),
        },
    )
    unk_bool_4: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6251CCA7, original_name="Unk Bool 4"),
        },
    )
    lighting: LightingMP1 = dataclasses.field(
        default_factory=LightingMP1,
        metadata={
            "reflection": FieldReflection[LightingMP1](
                LightingMP1,
                id=0x149E3CF2,
                original_name="Lighting",
                from_json=LightingMP1.from_json,
                to_json=LightingMP1.to_json,
            ),
        },
    )
    scannable: ScannableMP1 = dataclasses.field(
        default_factory=ScannableMP1,
        metadata={
            "reflection": FieldReflection[ScannableMP1](
                ScannableMP1,
                id=0xE50D083C,
                original_name="Scannable",
                from_json=ScannableMP1.from_json,
                to_json=ScannableMP1.to_json,
            ),
        },
    )
    visor: VisorMP1 = dataclasses.field(
        default_factory=VisorMP1,
        metadata={
            "reflection": FieldReflection[VisorMP1](
                VisorMP1, id=0xAF510B78, original_name="Visor", from_json=VisorMP1.from_json, to_json=VisorMP1.to_json
            ),
        },
    )
    unk_float_2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90075D55, original_name="Unk Float 2"),
        },
    )
    unk_float_3: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A759FFD, original_name="Unk Float 3"),
        },
    )
    unk_float_4: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDE5135DD, original_name="Unk Float 4"),
        },
    )
    unk_int: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBA89B4E8, original_name="Unk Int"),
        },
    )
    water_sort_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB222556A, original_name="Water Sort Type"),
        },
    )
    unk_bool_1: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8A410818, original_name="Unk Bool 1"),
        },
    )
    unk_bool_2: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x77066D1B, original_name="Unk Bool 2"),
        },
    )
    unk_bool_3: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7E405EE2, original_name="Unk Bool 3"),
        },
    )
    unk_bool_5: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x050751FB, original_name="Unk Bool 5"),
        },
    )
    unk_bool_6: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC8BA5DC9, original_name="Unk Bool 6"),
        },
    )
    unk_bool_7: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC7B23A2C, original_name="Unk Bool 7"),
        },
    )
    unk_bool_8: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4ACA4EFA, original_name="Unk Bool 8"),
        },
    )
    unk_bool_9: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6AD8955D, original_name="Unk Bool 9"),
        },
    )
    unk_bool_10: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x61B39963, original_name="Unk Bool 10"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.LITTLE_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
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

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x0036D778
        unk_guid_1 = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xAB68F7A7
        unk_guid_2 = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x802A053A
        unk_guid_3 = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x74822F37
        unk_guid_4 = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x0364A97A
        unk_guid_5 = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x36A5A738
        unk_float_1 = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x6251CCA7
        unk_bool_4 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x149E3CF2
        lighting = LightingMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xE50D083C
        scannable = ScannableMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xAF510B78
        visor = VisorMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x90075D55
        unk_float_2 = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x1A759FFD
        unk_float_3 = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xDE5135DD
        unk_float_4 = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xBA89B4E8
        unk_int = structs.LITTLE_l.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xB222556A
        water_sort_type = structs.LITTLE_l.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x8A410818
        unk_bool_1 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x77066D1B
        unk_bool_2 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x7E405EE2
        unk_bool_3 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x050751FB
        unk_bool_5 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xC8BA5DC9
        unk_bool_6 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xC7B23A2C
        unk_bool_7 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x4ACA4EFA
        unk_bool_8 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x6AD8955D
        unk_bool_9 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x61B39963
        unk_bool_10 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        return cls(
            unk_guid_1,
            unk_guid_2,
            unk_guid_3,
            unk_guid_4,
            unk_guid_5,
            unk_float_1,
            unk_bool_4,
            lighting,
            scannable,
            visor,
            unk_float_2,
            unk_float_3,
            unk_float_4,
            unk_int,
            water_sort_type,
            unk_bool_1,
            unk_bool_2,
            unk_bool_3,
            unk_bool_5,
            unk_bool_6,
            unk_bool_7,
            unk_bool_8,
            unk_bool_9,
            unk_bool_10,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x03\x00")  # 3 properties
        num_properties_written = 3

        if self.unk_guid_1 != default_override.get("unk_guid_1", default_asset_id):
            num_properties_written += 1
            data.write(b"x\xd76\x00")  # 0x36d778
            data.write(b"\x10\x00")  # size
            data.write(self.unk_guid_1.bytes_le)

        if self.unk_guid_2 != default_override.get("unk_guid_2", default_asset_id):
            num_properties_written += 1
            data.write(b"\xa7\xf7h\xab")  # 0xab68f7a7
            data.write(b"\x10\x00")  # size
            data.write(self.unk_guid_2.bytes_le)

        if self.unk_guid_3 != default_override.get("unk_guid_3", default_asset_id):
            num_properties_written += 1
            data.write(b":\x05*\x80")  # 0x802a053a
            data.write(b"\x10\x00")  # size
            data.write(self.unk_guid_3.bytes_le)

        if self.unk_guid_4 != default_override.get("unk_guid_4", default_asset_id):
            num_properties_written += 1
            data.write(b"7/\x82t")  # 0x74822f37
            data.write(b"\x10\x00")  # size
            data.write(self.unk_guid_4.bytes_le)

        if self.unk_guid_5 != default_override.get("unk_guid_5", default_asset_id):
            num_properties_written += 1
            data.write(b"z\xa9d\x03")  # 0x364a97a
            data.write(b"\x10\x00")  # size
            data.write(self.unk_guid_5.bytes_le)

        if self.unk_float_1 != default_override.get("unk_float_1", 1.0):
            num_properties_written += 1
            data.write(b"8\xa7\xa56")  # 0x36a5a738
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.unk_float_1))

        if self.unk_bool_4 != default_override.get("unk_bool_4", False):
            num_properties_written += 1
            data.write(b"\xa7\xccQb")  # 0x6251cca7
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_4))

        data.write(b"\xf2<\x9e\x14")  # 0x149e3cf2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.lighting.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"<\x08\r\xe5")  # 0xe50d083c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.scannable.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"x\x0bQ\xaf")  # 0xaf510b78
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        if self.unk_float_2 != default_override.get("unk_float_2", 1.0):
            num_properties_written += 1
            data.write(b"U]\x07\x90")  # 0x90075d55
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.unk_float_2))

        if self.unk_float_3 != default_override.get("unk_float_3", 1.0):
            num_properties_written += 1
            data.write(b"\xfd\x9fu\x1a")  # 0x1a759ffd
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.unk_float_3))

        if self.unk_float_4 != default_override.get("unk_float_4", 1.0):
            num_properties_written += 1
            data.write(b"\xdd5Q\xde")  # 0xde5135dd
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.unk_float_4))

        if self.unk_int != default_override.get("unk_int", 0):
            num_properties_written += 1
            data.write(b"\xe8\xb4\x89\xba")  # 0xba89b4e8
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_l.pack(self.unk_int))

        if self.water_sort_type != default_override.get("water_sort_type", 0):
            num_properties_written += 1
            data.write(b'jU"\xb2')  # 0xb222556a
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_l.pack(self.water_sort_type))

        if self.unk_bool_1 != default_override.get("unk_bool_1", True):
            num_properties_written += 1
            data.write(b"\x18\x08A\x8a")  # 0x8a410818
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_1))

        if self.unk_bool_2 != default_override.get("unk_bool_2", True):
            num_properties_written += 1
            data.write(b"\x1bm\x06w")  # 0x77066d1b
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_2))

        if self.unk_bool_3 != default_override.get("unk_bool_3", False):
            num_properties_written += 1
            data.write(b"\xe2^@~")  # 0x7e405ee2
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_3))

        if self.unk_bool_5 != default_override.get("unk_bool_5", False):
            num_properties_written += 1
            data.write(b"\xfbQ\x07\x05")  # 0x50751fb
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_5))

        if self.unk_bool_6 != default_override.get("unk_bool_6", False):
            num_properties_written += 1
            data.write(b"\xc9]\xba\xc8")  # 0xc8ba5dc9
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_6))

        if self.unk_bool_7 != default_override.get("unk_bool_7", True):
            num_properties_written += 1
            data.write(b",:\xb2\xc7")  # 0xc7b23a2c
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_7))

        if self.unk_bool_8 != default_override.get("unk_bool_8", False):
            num_properties_written += 1
            data.write(b"\xfaN\xcaJ")  # 0x4aca4efa
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_8))

        if self.unk_bool_9 != default_override.get("unk_bool_9", False):
            num_properties_written += 1
            data.write(b"]\x95\xd8j")  # 0x6ad8955d
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_9))

        if self.unk_bool_10 != default_override.get("unk_bool_10", True):
            num_properties_written += 1
            data.write(b"c\x99\xb3a")  # 0x61b39963
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_10))

        if num_properties_written != 3:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack("<H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorInformationMP1Json", data)
        return cls(
            unk_guid_1=uuid.UUID(json_data["unk_guid_1"]),
            unk_guid_2=uuid.UUID(json_data["unk_guid_2"]),
            unk_guid_3=uuid.UUID(json_data["unk_guid_3"]),
            unk_guid_4=uuid.UUID(json_data["unk_guid_4"]),
            unk_guid_5=uuid.UUID(json_data["unk_guid_5"]),
            unk_float_1=json_data["unk_float_1"],
            unk_bool_4=json_data["unk_bool_4"],
            lighting=LightingMP1.from_json(json_data["lighting"]),
            scannable=ScannableMP1.from_json(json_data["scannable"]),
            visor=VisorMP1.from_json(json_data["visor"]),
            unk_float_2=json_data["unk_float_2"],
            unk_float_3=json_data["unk_float_3"],
            unk_float_4=json_data["unk_float_4"],
            unk_int=json_data["unk_int"],
            water_sort_type=json_data["water_sort_type"],
            unk_bool_1=json_data["unk_bool_1"],
            unk_bool_2=json_data["unk_bool_2"],
            unk_bool_3=json_data["unk_bool_3"],
            unk_bool_5=json_data["unk_bool_5"],
            unk_bool_6=json_data["unk_bool_6"],
            unk_bool_7=json_data["unk_bool_7"],
            unk_bool_8=json_data["unk_bool_8"],
            unk_bool_9=json_data["unk_bool_9"],
            unk_bool_10=json_data["unk_bool_10"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unk_guid_1": str(self.unk_guid_1),
            "unk_guid_2": str(self.unk_guid_2),
            "unk_guid_3": str(self.unk_guid_3),
            "unk_guid_4": str(self.unk_guid_4),
            "unk_guid_5": str(self.unk_guid_5),
            "unk_float_1": self.unk_float_1,
            "unk_bool_4": self.unk_bool_4,
            "lighting": self.lighting.to_json(),
            "scannable": self.scannable.to_json(),
            "visor": self.visor.to_json(),
            "unk_float_2": self.unk_float_2,
            "unk_float_3": self.unk_float_3,
            "unk_float_4": self.unk_float_4,
            "unk_int": self.unk_int,
            "water_sort_type": self.water_sort_type,
            "unk_bool_1": self.unk_bool_1,
            "unk_bool_2": self.unk_bool_2,
            "unk_bool_3": self.unk_bool_3,
            "unk_bool_5": self.unk_bool_5,
            "unk_bool_6": self.unk_bool_6,
            "unk_bool_7": self.unk_bool_7,
            "unk_bool_8": self.unk_bool_8,
            "unk_bool_9": self.unk_bool_9,
            "unk_bool_10": self.unk_bool_10,
        }


def _decode_unk_guid_1(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_unk_guid_2(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_unk_guid_3(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_unk_guid_4(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_unk_guid_5(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_lighting(data: typing.BinaryIO, game: Game, property_size: int) -> LightingMP1:
    return LightingMP1.from_stream(data, game, property_size)


def _decode_scannable(data: typing.BinaryIO, game: Game, property_size: int) -> ScannableMP1:
    return ScannableMP1.from_stream(data, game, property_size)


def _decode_visor(data: typing.BinaryIO, game: Game, property_size: int) -> VisorMP1:
    return VisorMP1.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x0036D778: ("unk_guid_1", _decode_unk_guid_1),
    0xAB68F7A7: ("unk_guid_2", _decode_unk_guid_2),
    0x802A053A: ("unk_guid_3", _decode_unk_guid_3),
    0x74822F37: ("unk_guid_4", _decode_unk_guid_4),
    0x0364A97A: ("unk_guid_5", _decode_unk_guid_5),
    0x36A5A738: ("unk_float_1", structs.decode_LITTLE_f),
    0x6251CCA7: ("unk_bool_4", structs.decode_LITTLE_bool_),
    0x149E3CF2: ("lighting", _decode_lighting),
    0xE50D083C: ("scannable", _decode_scannable),
    0xAF510B78: ("visor", _decode_visor),
    0x90075D55: ("unk_float_2", structs.decode_LITTLE_f),
    0x1A759FFD: ("unk_float_3", structs.decode_LITTLE_f),
    0xDE5135DD: ("unk_float_4", structs.decode_LITTLE_f),
    0xBA89B4E8: ("unk_int", structs.decode_LITTLE_l),
    0xB222556A: ("water_sort_type", structs.decode_LITTLE_l),
    0x8A410818: ("unk_bool_1", structs.decode_LITTLE_bool_),
    0x77066D1B: ("unk_bool_2", structs.decode_LITTLE_bool_),
    0x7E405EE2: ("unk_bool_3", structs.decode_LITTLE_bool_),
    0x050751FB: ("unk_bool_5", structs.decode_LITTLE_bool_),
    0xC8BA5DC9: ("unk_bool_6", structs.decode_LITTLE_bool_),
    0xC7B23A2C: ("unk_bool_7", structs.decode_LITTLE_bool_),
    0x4ACA4EFA: ("unk_bool_8", structs.decode_LITTLE_bool_),
    0x6AD8955D: ("unk_bool_9", structs.decode_LITTLE_bool_),
    0x61B39963: ("unk_bool_10", structs.decode_LITTLE_bool_),
}
