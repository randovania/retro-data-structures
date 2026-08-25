# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.LightParameters import LightParameters
from retro_data_structures.properties.echoes.archetypes.ScannableParameters import ScannableParameters
from retro_data_structures.properties.echoes.archetypes.VisorParameters import VisorParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ActorParametersJson(typing_extensions.TypedDict):
        lighting: json_util.JsonObject
        scannable: json_util.JsonObject
        dark_model: int
        dark_skin: int
        echo_model: int
        echo_skin: int
        use_global_render_time: bool
        fade_in_time: float
        fade_out_time: float
        visor: json_util.JsonObject
        unknown_0xcd4c81a1: bool
        force_render_unsorted: bool
        takes_projected_shadow: bool
        unknown_0xf07981e8: bool
        unknown_0x6df33845: bool
        max_volume: int
        max_echo_volume: int


@dataclasses.dataclass()
class ActorParameters(BaseProperty):
    lighting: LightParameters = dataclasses.field(
        default_factory=LightParameters,
        metadata={
            "reflection": FieldReflection[LightParameters](
                LightParameters,
                id=0xB028DB0E,
                original_name="Lighting",
                from_json=LightParameters.from_json,
                to_json=LightParameters.to_json,
            ),
        },
    )
    scannable: ScannableParameters = dataclasses.field(
        default_factory=ScannableParameters,
        metadata={
            "reflection": FieldReflection[ScannableParameters](
                ScannableParameters,
                id=0x375BFD7C,
                original_name="Scannable",
                from_json=ScannableParameters.from_json,
                to_json=ScannableParameters.to_json,
            ),
        },
    )
    dark_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC0BA9E18, original_name="DarkModel"),
        },
    )
    dark_skin: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9F027D91, original_name="DarkSkin"),
        },
    )
    echo_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6B1FBC3A, original_name="EchoModel"),
        },
    )
    echo_skin: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEB1D06BE, original_name="EchoSkin"),
        },
    )
    use_global_render_time: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1499803C, original_name="UseGlobalRenderTime"),
        },
    )
    fade_in_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90AA341F, original_name="FadeInTime"),
        },
    )
    fade_out_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7C269EBC, original_name="FadeOutTime"),
        },
    )
    visor: VisorParameters = dataclasses.field(
        default_factory=VisorParameters,
        metadata={
            "reflection": FieldReflection[VisorParameters](
                VisorParameters,
                id=0x05AD250E,
                original_name="Visor",
                from_json=VisorParameters.from_json,
                to_json=VisorParameters.to_json,
            ),
        },
    )
    unknown_0xcd4c81a1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCD4C81A1, original_name="Unknown"),
        },
    )
    force_render_unsorted: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x799263F1, original_name="ForceRenderUnsorted"),
        },
    )
    takes_projected_shadow: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xED3A6E87, original_name="TakesProjectedShadow"),
        },
    )
    unknown_0xf07981e8: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF07981E8, original_name="Unknown"),
        },
    )
    unknown_0x6df33845: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6DF33845, original_name="Unknown"),
        },
    )
    max_volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC712847C, original_name="MaxVolume"),
        },
    )
    max_echo_volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBA2600D7, original_name="MaxEchoVolume"),
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
        if property_count != 17:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB028DB0E
        lighting = LightParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x375BFD7C
        scannable = ScannableParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC0BA9E18
        dark_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F027D91
        dark_skin = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6B1FBC3A
        echo_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB1D06BE
        echo_skin = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1499803C
        use_global_render_time = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90AA341F
        fade_in_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C269EBC
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05AD250E
        visor = VisorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD4C81A1
        unknown_0xcd4c81a1 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x799263F1
        force_render_unsorted = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED3A6E87
        takes_projected_shadow = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF07981E8
        unknown_0xf07981e8 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DF33845
        unknown_0x6df33845 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC712847C
        max_volume = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA2600D7
        max_echo_volume = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            lighting,
            scannable,
            dark_model,
            dark_skin,
            echo_model,
            echo_skin,
            use_global_render_time,
            fade_in_time,
            fade_out_time,
            visor,
            unknown_0xcd4c81a1,
            force_render_unsorted,
            takes_projected_shadow,
            unknown_0xf07981e8,
            unknown_0x6df33845,
            max_volume,
            max_echo_volume,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x11")  # 17 properties

        data.write(b"\xb0(\xdb\x0e")  # 0xb028db0e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.lighting.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"7[\xfd|")  # 0x375bfd7c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.scannable.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc0\xba\x9e\x18")  # 0xc0ba9e18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dark_model))

        data.write(b"\x9f\x02}\x91")  # 0x9f027d91
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dark_skin))

        data.write(b"k\x1f\xbc:")  # 0x6b1fbc3a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.echo_model))

        data.write(b"\xeb\x1d\x06\xbe")  # 0xeb1d06be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.echo_skin))

        data.write(b"\x14\x99\x80<")  # 0x1499803c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_global_render_time))

        data.write(b"\x90\xaa4\x1f")  # 0x90aa341f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_in_time))

        data.write(b"|&\x9e\xbc")  # 0x7c269ebc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

        data.write(b"\x05\xad%\x0e")  # 0x5ad250e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcdL\x81\xa1")  # 0xcd4c81a1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xcd4c81a1))

        data.write(b"y\x92c\xf1")  # 0x799263f1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.force_render_unsorted))

        data.write(b"\xed:n\x87")  # 0xed3a6e87
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.takes_projected_shadow))

        data.write(b"\xf0y\x81\xe8")  # 0xf07981e8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf07981e8))

        data.write(b"m\xf38E")  # 0x6df33845
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x6df33845))

        data.write(b"\xc7\x12\x84|")  # 0xc712847c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_volume))

        data.write(b"\xba&\x00\xd7")  # 0xba2600d7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_echo_volume))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorParametersJson", data)
        return cls(
            lighting=LightParameters.from_json(json_data["lighting"]),
            scannable=ScannableParameters.from_json(json_data["scannable"]),
            dark_model=json_data["dark_model"],
            dark_skin=json_data["dark_skin"],
            echo_model=json_data["echo_model"],
            echo_skin=json_data["echo_skin"],
            use_global_render_time=json_data["use_global_render_time"],
            fade_in_time=json_data["fade_in_time"],
            fade_out_time=json_data["fade_out_time"],
            visor=VisorParameters.from_json(json_data["visor"]),
            unknown_0xcd4c81a1=json_data["unknown_0xcd4c81a1"],
            force_render_unsorted=json_data["force_render_unsorted"],
            takes_projected_shadow=json_data["takes_projected_shadow"],
            unknown_0xf07981e8=json_data["unknown_0xf07981e8"],
            unknown_0x6df33845=json_data["unknown_0x6df33845"],
            max_volume=json_data["max_volume"],
            max_echo_volume=json_data["max_echo_volume"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "lighting": self.lighting.to_json(),
            "scannable": self.scannable.to_json(),
            "dark_model": self.dark_model,
            "dark_skin": self.dark_skin,
            "echo_model": self.echo_model,
            "echo_skin": self.echo_skin,
            "use_global_render_time": self.use_global_render_time,
            "fade_in_time": self.fade_in_time,
            "fade_out_time": self.fade_out_time,
            "visor": self.visor.to_json(),
            "unknown_0xcd4c81a1": self.unknown_0xcd4c81a1,
            "force_render_unsorted": self.force_render_unsorted,
            "takes_projected_shadow": self.takes_projected_shadow,
            "unknown_0xf07981e8": self.unknown_0xf07981e8,
            "unknown_0x6df33845": self.unknown_0x6df33845,
            "max_volume": self.max_volume,
            "max_echo_volume": self.max_echo_volume,
        }

    def _dependencies_for_dark_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_model)

    def _dependencies_for_dark_skin(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_skin)

    def _dependencies_for_echo_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_model)

    def _dependencies_for_echo_skin(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_skin)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.scannable.dependencies_for, "scannable", "ScannableParameters"),
            (self._dependencies_for_dark_model, "dark_model", "AssetId"),
            (self._dependencies_for_dark_skin, "dark_skin", "AssetId"),
            (self._dependencies_for_echo_model, "echo_model", "AssetId"),
            (self._dependencies_for_echo_skin, "echo_skin", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ActorParameters.{field_name} ({field_type}): {e}")


def _decode_lighting(data: typing.BinaryIO, game: Game, property_size: int) -> LightParameters:
    return LightParameters.from_stream(data, game, property_size)


def _decode_scannable(data: typing.BinaryIO, game: Game, property_size: int) -> ScannableParameters:
    return ScannableParameters.from_stream(data, game, property_size)


def _decode_visor(data: typing.BinaryIO, game: Game, property_size: int) -> VisorParameters:
    return VisorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB028DB0E: ("lighting", _decode_lighting),
    0x375BFD7C: ("scannable", _decode_scannable),
    0xC0BA9E18: ("dark_model", structs.decode_BIG_L),
    0x9F027D91: ("dark_skin", structs.decode_BIG_L),
    0x6B1FBC3A: ("echo_model", structs.decode_BIG_L),
    0xEB1D06BE: ("echo_skin", structs.decode_BIG_L),
    0x1499803C: ("use_global_render_time", structs.decode_BIG_bool_),
    0x90AA341F: ("fade_in_time", structs.decode_BIG_f),
    0x7C269EBC: ("fade_out_time", structs.decode_BIG_f),
    0x05AD250E: ("visor", _decode_visor),
    0xCD4C81A1: ("unknown_0xcd4c81a1", structs.decode_BIG_bool_),
    0x799263F1: ("force_render_unsorted", structs.decode_BIG_bool_),
    0xED3A6E87: ("takes_projected_shadow", structs.decode_BIG_bool_),
    0xF07981E8: ("unknown_0xf07981e8", structs.decode_BIG_bool_),
    0x6DF33845: ("unknown_0x6df33845", structs.decode_BIG_bool_),
    0xC712847C: ("max_volume", structs.decode_BIG_l),
    0xBA2600D7: ("max_echo_volume", structs.decode_BIG_l),
}
