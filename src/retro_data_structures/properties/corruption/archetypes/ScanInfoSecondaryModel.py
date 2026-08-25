# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ScanInfoSecondaryModelJson(typing_extensions.TypedDict):
        static_model: int
        animated_model: json_util.JsonObject
        model_locator: str


@dataclasses.dataclass()
class ScanInfoSecondaryModel(BaseProperty):
    static_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB7ADC418, original_name="StaticModel"),
        },
    )
    animated_model: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xC4AD00A7,
                original_name="AnimatedModel",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    model_locator: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x24A97916, original_name="ModelLocator"),
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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7ADC418
        static_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4AD00A7
        animated_model = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24A97916
        model_locator = data.read(property_size)[:-1].decode("utf-8")

        return cls(static_model, animated_model, model_locator)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\xb7\xad\xc4\x18")  # 0xb7adc418
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.static_model))

        data.write(b"\xc4\xad\x00\xa7")  # 0xc4ad00a7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animated_model.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"$\xa9y\x16")  # 0x24a97916
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.model_locator.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ScanInfoSecondaryModelJson", data)
        return cls(
            static_model=json_data["static_model"],
            animated_model=AnimationParameters.from_json(json_data["animated_model"]),
            model_locator=json_data["model_locator"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "static_model": self.static_model,
            "animated_model": self.animated_model.to_json(),
            "model_locator": self.model_locator,
        }


def _decode_animated_model(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_model_locator(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB7ADC418: ("static_model", structs.decode_BIG_Q),
    0xC4AD00A7: ("animated_model", _decode_animated_model),
    0x24A97916: ("model_locator", _decode_model_locator),
}
