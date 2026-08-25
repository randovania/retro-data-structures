# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing
import uuid

import typing_extensions

import retro_data_structures.enums.prime_remastered as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime_remastered.archetypes.ActorInformationMP1 import ActorInformationMP1
from retro_data_structures.properties.prime_remastered.archetypes.AnimSetMP1 import AnimSetMP1
from retro_data_structures.properties.prime_remastered.archetypes.MapInfoMP1 import MapInfoMP1
from retro_data_structures.properties.prime_remastered.archetypes.VectorMP1 import VectorMP1
from retro_data_structures.properties.prime_remastered.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PickupMP1Json(typing_extensions.TypedDict):
        collision_scale: json_util.JsonObject
        scan_collision_offset: json_util.JsonObject
        item: int
        capacity: int
        amount: int
        drop_rate: float
        life_time: float
        fade_length: float
        guid_1: str
        animation_parameters: json_util.JsonObject
        spawn_delay: float
        guid_2: str
        unk_vec_3: json_util.JsonObject
        map_info: json_util.JsonObject
        actor_info: json_util.JsonObject
        unk_bool_1: bool
        unk_bool_2: bool


def _from_json_guid_1(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_guid_2(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _to_json_guid_1(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_guid_2(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


@dataclasses.dataclass()
class PickupMP1(BaseProperty):
    collision_scale: VectorMP1 = dataclasses.field(
        default_factory=VectorMP1,
        metadata={
            "reflection": FieldReflection[VectorMP1](
                VectorMP1,
                id=0x70E39EC6,
                original_name="Collision Scale",
                from_json=VectorMP1.from_json,
                to_json=VectorMP1.to_json,
            ),
        },
    )
    scan_collision_offset: VectorMP1 = dataclasses.field(
        default_factory=VectorMP1,
        metadata={
            "reflection": FieldReflection[VectorMP1](
                VectorMP1,
                id=0x2D644844,
                original_name="Scan/Collision Offset",
                from_json=VectorMP1.from_json,
                to_json=VectorMP1.to_json,
            ),
        },
    )
    item: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0xC79794EE,
                original_name="Item",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    capacity: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x76BE91D5, original_name="Capacity"),
        },
    )
    amount: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9FDBD2F6, original_name="Amount"),
        },
    )
    drop_rate: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFCF349D2, original_name="Drop Rate"),
        },
    )
    life_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7F2AAF7D, original_name="Life Time"),
        },
    )
    fade_length: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEF930F2B, original_name="Fade Length"),
        },
    )
    guid_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId, id=0xBCE29CB3, original_name="GUID 1", from_json=_from_json_guid_1, to_json=_to_json_guid_1
            ),
        },
    )
    animation_parameters: AnimSetMP1 = dataclasses.field(
        default_factory=AnimSetMP1,
        metadata={
            "reflection": FieldReflection[AnimSetMP1](
                AnimSetMP1,
                id=0x19D911B1,
                original_name="AnimationParameters",
                from_json=AnimSetMP1.from_json,
                to_json=AnimSetMP1.to_json,
            ),
        },
    )
    spawn_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3E9F5EFF, original_name="Spawn Delay"),
        },
    )
    guid_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId, id=0xE2A07D8E, original_name="GUID 2", from_json=_from_json_guid_2, to_json=_to_json_guid_2
            ),
        },
    )
    unk_vec_3: VectorMP1 = dataclasses.field(
        default_factory=VectorMP1,
        metadata={
            "reflection": FieldReflection[VectorMP1](
                VectorMP1,
                id=0x853F438A,
                original_name="Unk Vec 3",
                from_json=VectorMP1.from_json,
                to_json=VectorMP1.to_json,
            ),
        },
    )
    map_info: MapInfoMP1 = dataclasses.field(
        default_factory=MapInfoMP1,
        metadata={
            "reflection": FieldReflection[MapInfoMP1](
                MapInfoMP1,
                id=0xBA38A80B,
                original_name="Map Info",
                from_json=MapInfoMP1.from_json,
                to_json=MapInfoMP1.to_json,
            ),
        },
    )
    actor_info: ActorInformationMP1 = dataclasses.field(
        default_factory=ActorInformationMP1,
        metadata={
            "reflection": FieldReflection[ActorInformationMP1](
                ActorInformationMP1,
                id=0x68F9D4B6,
                original_name="Actor Info",
                from_json=ActorInformationMP1.from_json,
                to_json=ActorInformationMP1.to_json,
            ),
        },
    )
    unk_bool_1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBD71E2F2, original_name="Unk Bool 1"),
        },
    )
    unk_bool_2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF2165C6E, original_name="Unk Bool 2"),
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
        if property_count != 17:
            return None

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x70E39EC6
        collision_scale = VectorMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x2D644844
        scan_collision_offset = VectorMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xC79794EE
        item = enums.PlayerItemEnum.from_stream(data, game)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x76BE91D5
        capacity = structs.LITTLE_l.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x9FDBD2F6
        amount = structs.LITTLE_l.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xFCF349D2
        drop_rate = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x7F2AAF7D
        life_time = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xEF930F2B
        fade_length = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xBCE29CB3
        guid_1 = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x19D911B1
        animation_parameters = AnimSetMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x3E9F5EFF
        spawn_delay = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xE2A07D8E
        guid_2 = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x853F438A
        unk_vec_3 = VectorMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xBA38A80B
        map_info = MapInfoMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x68F9D4B6
        actor_info = ActorInformationMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xBD71E2F2
        unk_bool_1 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xF2165C6E
        unk_bool_2 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        return cls(
            collision_scale,
            scan_collision_offset,
            item,
            capacity,
            amount,
            drop_rate,
            life_time,
            fade_length,
            guid_1,
            animation_parameters,
            spawn_delay,
            guid_2,
            unk_vec_3,
            map_info,
            actor_info,
            unk_bool_1,
            unk_bool_2,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x08\x00")  # 8 properties
        num_properties_written = 8

        data.write(b"\xc6\x9e\xe3p")  # 0x70e39ec6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.collision_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"DHd-")  # 0x2d644844
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.scan_collision_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xee\x94\x97\xc7")  # 0xc79794ee
        data.write(b"\x04\x00")  # size
        self.item.to_stream(data, game)

        if self.capacity != default_override.get("capacity", 1):
            num_properties_written += 1
            data.write(b"\xd5\x91\xbev")  # 0x76be91d5
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_l.pack(self.capacity))

        if self.amount != default_override.get("amount", 1):
            num_properties_written += 1
            data.write(b"\xf6\xd2\xdb\x9f")  # 0x9fdbd2f6
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_l.pack(self.amount))

        if self.drop_rate != default_override.get("drop_rate", 100.0):
            num_properties_written += 1
            data.write(b"\xd2I\xf3\xfc")  # 0xfcf349d2
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.drop_rate))

        if self.life_time != default_override.get("life_time", 0.0):
            num_properties_written += 1
            data.write(b"}\xaf*\x7f")  # 0x7f2aaf7d
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.life_time))

        if self.fade_length != default_override.get("fade_length", 0.0):
            num_properties_written += 1
            data.write(b"+\x0f\x93\xef")  # 0xef930f2b
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.fade_length))

        if self.guid_1 != default_override.get("guid_1", default_asset_id):
            num_properties_written += 1
            data.write(b"\xb3\x9c\xe2\xbc")  # 0xbce29cb3
            data.write(b"\x10\x00")  # size
            data.write(self.guid_1.bytes_le)

        data.write(b"\xb1\x11\xd9\x19")  # 0x19d911b1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation_parameters.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        if self.spawn_delay != default_override.get("spawn_delay", 0.0):
            num_properties_written += 1
            data.write(b"\xff^\x9f>")  # 0x3e9f5eff
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.spawn_delay))

        data.write(b"\x8e}\xa0\xe2")  # 0xe2a07d8e
        data.write(b"\x10\x00")  # size
        data.write(self.guid_2.bytes_le)

        data.write(b"\x8aC?\x85")  # 0x853f438a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unk_vec_3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0b\xa88\xba")  # 0xba38a80b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.map_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb6\xd4\xf9h")  # 0x68f9d4b6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        if self.unk_bool_1 != default_override.get("unk_bool_1", False):
            num_properties_written += 1
            data.write(b"\xf2\xe2q\xbd")  # 0xbd71e2f2
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_1))

        if self.unk_bool_2 != default_override.get("unk_bool_2", False):
            num_properties_written += 1
            data.write(b"n\\\x16\xf2")  # 0xf2165c6e
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool_2))

        if num_properties_written != 8:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack("<H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PickupMP1Json", data)
        return cls(
            collision_scale=VectorMP1.from_json(json_data["collision_scale"]),
            scan_collision_offset=VectorMP1.from_json(json_data["scan_collision_offset"]),
            item=enums.PlayerItemEnum.from_json(json_data["item"]),
            capacity=json_data["capacity"],
            amount=json_data["amount"],
            drop_rate=json_data["drop_rate"],
            life_time=json_data["life_time"],
            fade_length=json_data["fade_length"],
            guid_1=uuid.UUID(json_data["guid_1"]),
            animation_parameters=AnimSetMP1.from_json(json_data["animation_parameters"]),
            spawn_delay=json_data["spawn_delay"],
            guid_2=uuid.UUID(json_data["guid_2"]),
            unk_vec_3=VectorMP1.from_json(json_data["unk_vec_3"]),
            map_info=MapInfoMP1.from_json(json_data["map_info"]),
            actor_info=ActorInformationMP1.from_json(json_data["actor_info"]),
            unk_bool_1=json_data["unk_bool_1"],
            unk_bool_2=json_data["unk_bool_2"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "collision_scale": self.collision_scale.to_json(),
            "scan_collision_offset": self.scan_collision_offset.to_json(),
            "item": self.item.to_json(),
            "capacity": self.capacity,
            "amount": self.amount,
            "drop_rate": self.drop_rate,
            "life_time": self.life_time,
            "fade_length": self.fade_length,
            "guid_1": str(self.guid_1),
            "animation_parameters": self.animation_parameters.to_json(),
            "spawn_delay": self.spawn_delay,
            "guid_2": str(self.guid_2),
            "unk_vec_3": self.unk_vec_3.to_json(),
            "map_info": self.map_info.to_json(),
            "actor_info": self.actor_info.to_json(),
            "unk_bool_1": self.unk_bool_1,
            "unk_bool_2": self.unk_bool_2,
        }


def _decode_collision_scale(data: typing.BinaryIO, game: Game, property_size: int) -> VectorMP1:
    return VectorMP1.from_stream(data, game, property_size)


def _decode_scan_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> VectorMP1:
    return VectorMP1.from_stream(data, game, property_size)


def _decode_item(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PlayerItemEnum:
    return enums.PlayerItemEnum.from_stream(data, game)


def _decode_guid_1(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_animation_parameters(data: typing.BinaryIO, game: Game, property_size: int) -> AnimSetMP1:
    return AnimSetMP1.from_stream(data, game, property_size)


def _decode_guid_2(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_unk_vec_3(data: typing.BinaryIO, game: Game, property_size: int) -> VectorMP1:
    return VectorMP1.from_stream(data, game, property_size)


def _decode_map_info(data: typing.BinaryIO, game: Game, property_size: int) -> MapInfoMP1:
    return MapInfoMP1.from_stream(data, game, property_size)


def _decode_actor_info(data: typing.BinaryIO, game: Game, property_size: int) -> ActorInformationMP1:
    return ActorInformationMP1.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x70E39EC6: ("collision_scale", _decode_collision_scale),
    0x2D644844: ("scan_collision_offset", _decode_scan_collision_offset),
    0xC79794EE: ("item", _decode_item),
    0x76BE91D5: ("capacity", structs.decode_LITTLE_l),
    0x9FDBD2F6: ("amount", structs.decode_LITTLE_l),
    0xFCF349D2: ("drop_rate", structs.decode_LITTLE_f),
    0x7F2AAF7D: ("life_time", structs.decode_LITTLE_f),
    0xEF930F2B: ("fade_length", structs.decode_LITTLE_f),
    0xBCE29CB3: ("guid_1", _decode_guid_1),
    0x19D911B1: ("animation_parameters", _decode_animation_parameters),
    0x3E9F5EFF: ("spawn_delay", structs.decode_LITTLE_f),
    0xE2A07D8E: ("guid_2", _decode_guid_2),
    0x853F438A: ("unk_vec_3", _decode_unk_vec_3),
    0xBA38A80B: ("map_info", _decode_map_info),
    0x68F9D4B6: ("actor_info", _decode_actor_info),
    0xBD71E2F2: ("unk_bool_1", structs.decode_LITTLE_bool_),
    0xF2165C6E: ("unk_bool_2", structs.decode_LITTLE_bool_),
}
