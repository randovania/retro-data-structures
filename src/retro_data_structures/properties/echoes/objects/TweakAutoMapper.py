# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.echoes.archetypes.TweakAutoMapper_Base import TweakAutoMapper_Base
from retro_data_structures.properties.echoes.archetypes.TweakAutoMapper_DoorColors import TweakAutoMapper_DoorColors
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TweakAutoMapperJson(typing_extensions.TypedDict):
        instance_name: str
        base: json_util.JsonObject
        door_colors: json_util.JsonObject


@dataclasses.dataclass()
class TweakAutoMapper(BaseObjectType):
    instance_name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x7FDA1466, original_name="InstanceName"),
        },
    )
    base: TweakAutoMapper_Base = dataclasses.field(
        default_factory=TweakAutoMapper_Base,
        metadata={
            "reflection": FieldReflection[TweakAutoMapper_Base](
                TweakAutoMapper_Base,
                id=0x18B2F423,
                original_name="Base",
                from_json=TweakAutoMapper_Base.from_json,
                to_json=TweakAutoMapper_Base.to_json,
            ),
        },
    )
    door_colors: TweakAutoMapper_DoorColors = dataclasses.field(
        default_factory=TweakAutoMapper_DoorColors,
        metadata={
            "reflection": FieldReflection[TweakAutoMapper_DoorColors](
                TweakAutoMapper_DoorColors,
                id=0xC5368863,
                original_name="DoorColors",
                from_json=TweakAutoMapper_DoorColors.from_json,
                to_json=TweakAutoMapper_DoorColors.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return "TWAM"

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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FDA1466
        instance_name = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18B2F423
        base = TweakAutoMapper_Base.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5368863
        door_colors = TweakAutoMapper_DoorColors.from_stream(data, game, property_size)

        return cls(instance_name, base, door_colors)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\x7f\xda\x14f")  # 0x7fda1466
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.instance_name.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x18\xb2\xf4#")  # 0x18b2f423
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.base.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc56\x88c")  # 0xc5368863
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.door_colors.to_stream(data, game)
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
        json_data = typing.cast("TweakAutoMapperJson", data)
        return cls(
            instance_name=json_data["instance_name"],
            base=TweakAutoMapper_Base.from_json(json_data["base"]),
            door_colors=TweakAutoMapper_DoorColors.from_json(json_data["door_colors"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "instance_name": self.instance_name,
            "base": self.base.to_json(),
            "door_colors": self.door_colors.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_base(data: typing.BinaryIO, game: Game, property_size: int) -> TweakAutoMapper_Base:
    return TweakAutoMapper_Base.from_stream(data, game, property_size)


def _decode_door_colors(data: typing.BinaryIO, game: Game, property_size: int) -> TweakAutoMapper_DoorColors:
    return TweakAutoMapper_DoorColors.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FDA1466: ("instance_name", _decode_instance_name),
    0x18B2F423: ("base", _decode_base),
    0xC5368863: ("door_colors", _decode_door_colors),
}
