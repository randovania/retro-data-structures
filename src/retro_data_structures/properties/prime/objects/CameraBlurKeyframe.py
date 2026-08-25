# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CameraBlurKeyframeJson(typing_extensions.TypedDict):
        name: str
        active: bool
        blur_type: int
        amount: float
        filter_index: int
        fade_in_duration: float
        fade_out_duration: float


class BlurType(enum.IntEnum):
    NoBlur = 0
    LowBlur = 1
    HighBlur = 2
    XRay = 3

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class CameraBlurKeyframe(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="Active"),
        },
    )
    blur_type: BlurType = dataclasses.field(
        default=BlurType.NoBlur,
        metadata={
            "reflection": FieldReflection[BlurType](
                BlurType,
                id=0x00000002,
                original_name="BlurType",
                from_json=BlurType.from_json,
                to_json=BlurType.to_json,
            ),
        },
    )
    amount: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Amount"),
        },
    )
    filter_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="FilterIndex"),
        },
    )
    fade_in_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="FadeInDuration"),
        },
    )
    fade_out_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="FadeOutDuration"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x19

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        blur_type = BlurType.from_stream(data, game)
        amount = structs.BIG_f.unpack(data.read(4))[0]
        filter_index = structs.BIG_l.unpack(data.read(4))[0]
        fade_in_duration = structs.BIG_f.unpack(data.read(4))[0]
        fade_out_duration = structs.BIG_f.unpack(data.read(4))[0]
        return cls(name, active, blur_type, amount, filter_index, fade_in_duration, fade_out_duration)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x07")  # 7 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        self.blur_type.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.amount))
        data.write(structs.BIG_l.pack(self.filter_index))
        data.write(structs.BIG_f.pack(self.fade_in_duration))
        data.write(structs.BIG_f.pack(self.fade_out_duration))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraBlurKeyframeJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            blur_type=BlurType.from_json(json_data["blur_type"]),
            amount=json_data["amount"],
            filter_index=json_data["filter_index"],
            fade_in_duration=json_data["fade_in_duration"],
            fade_out_duration=json_data["fade_out_duration"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "blur_type": self.blur_type.to_json(),
            "amount": self.amount,
            "filter_index": self.filter_index,
            "fade_in_duration": self.fade_in_duration,
            "fade_out_duration": self.fade_out_duration,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
