# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.echoes.archetypes.ScanInfoSecondaryModel import ScanInfoSecondaryModel
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ScannableObjectInfoJson(typing_extensions.TypedDict):
        string: int
        scan_speed: int
        critical: bool
        unknown_0x1733b1ec: bool
        unknown_0x53336141: int
        model_initial_pitch: float
        model_initial_yaw: float
        model_scale: float
        static_model: int
        animated_model: json_util.JsonObject
        unknown_0x58f9fe99: json_util.JsonObject
        secondary_model0: json_util.JsonObject
        secondary_model1: json_util.JsonObject
        secondary_model2: json_util.JsonObject
        secondary_model3: json_util.JsonObject
        secondary_model4: json_util.JsonObject
        secondary_model5: json_util.JsonObject
        secondary_model6: json_util.JsonObject
        secondary_model7: json_util.JsonObject
        secondary_model8: json_util.JsonObject


@dataclasses.dataclass()
class ScannableObjectInfo(BaseObjectType):
    string: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["STRG"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2F5B6423, original_name="String"),
        },
    )
    scan_speed: enums.ScanSpeedEnum = dataclasses.field(
        default=enums.ScanSpeedEnum.Normal,
        metadata={
            "reflection": FieldReflection[enums.ScanSpeedEnum](
                enums.ScanSpeedEnum,
                id=0xC308A322,
                original_name="ScanSpeed",
                from_json=enums.ScanSpeedEnum.from_json,
                to_json=enums.ScanSpeedEnum.to_json,
            ),
        },
    )
    critical: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7B714814, original_name="Critical"),
        },
    )
    unknown_0x1733b1ec: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1733B1EC, original_name="Unknown"),
        },
    )
    unknown_0x53336141: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x53336141, original_name="Unknown"),
        },
    )
    model_initial_pitch: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3DE0BA64, original_name="ModelInitialPitch"),
        },
    )
    model_initial_yaw: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2ADD6628, original_name="ModelInitialYaw"),
        },
    )
    model_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD0C15066, original_name="ModelScale"),
        },
    )
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
                id=0x15694EE1,
                original_name="AnimatedModel",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unknown_0x58f9fe99: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x58F9FE99,
                original_name="Unknown",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    secondary_model0: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0x1C5B4A3A,
                original_name="SecondaryModel0",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model1: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0x8728A0EE,
                original_name="SecondaryModel1",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model2: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0xF1CD99D3,
                original_name="SecondaryModel2",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model3: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0x6ABE7307,
                original_name="SecondaryModel3",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model4: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0x1C07EBA9,
                original_name="SecondaryModel4",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model5: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0x8774017D,
                original_name="SecondaryModel5",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model6: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0xF1913840,
                original_name="SecondaryModel6",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model7: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0x6AE2D294,
                original_name="SecondaryModel7",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )
    secondary_model8: ScanInfoSecondaryModel = dataclasses.field(
        default_factory=ScanInfoSecondaryModel,
        metadata={
            "reflection": FieldReflection[ScanInfoSecondaryModel](
                ScanInfoSecondaryModel,
                id=0x1CE2091C,
                original_name="SecondaryModel8",
                from_json=ScanInfoSecondaryModel.from_json,
                to_json=ScanInfoSecondaryModel.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return "SNFO"

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
        if property_count != 20:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F5B6423
        string = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC308A322
        scan_speed = enums.ScanSpeedEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B714814
        critical = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1733B1EC
        unknown_0x1733b1ec = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53336141
        unknown_0x53336141 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DE0BA64
        model_initial_pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ADD6628
        model_initial_yaw = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD0C15066
        model_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7ADC418
        static_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15694EE1
        animated_model = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58F9FE99
        unknown_0x58f9fe99 = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C5B4A3A
        secondary_model0 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8728A0EE
        secondary_model1 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1CD99D3
        secondary_model2 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ABE7307
        secondary_model3 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C07EBA9
        secondary_model4 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8774017D
        secondary_model5 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1913840
        secondary_model6 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6AE2D294
        secondary_model7 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CE2091C
        secondary_model8 = ScanInfoSecondaryModel.from_stream(data, game, property_size)

        return cls(
            string,
            scan_speed,
            critical,
            unknown_0x1733b1ec,
            unknown_0x53336141,
            model_initial_pitch,
            model_initial_yaw,
            model_scale,
            static_model,
            animated_model,
            unknown_0x58f9fe99,
            secondary_model0,
            secondary_model1,
            secondary_model2,
            secondary_model3,
            secondary_model4,
            secondary_model5,
            secondary_model6,
            secondary_model7,
            secondary_model8,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x14")  # 20 properties

        data.write(b"/[d#")  # 0x2f5b6423
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.string))

        data.write(b'\xc3\x08\xa3"')  # 0xc308a322
        data.write(b"\x00\x04")  # size
        self.scan_speed.to_stream(data, game)

        data.write(b"{qH\x14")  # 0x7b714814
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.critical))

        data.write(b"\x173\xb1\xec")  # 0x1733b1ec
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x1733b1ec))

        data.write(b"S3aA")  # 0x53336141
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x53336141))

        data.write(b"=\xe0\xbad")  # 0x3de0ba64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.model_initial_pitch))

        data.write(b"*\xddf(")  # 0x2add6628
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.model_initial_yaw))

        data.write(b"\xd0\xc1Pf")  # 0xd0c15066
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.model_scale))

        data.write(b"\xb7\xad\xc4\x18")  # 0xb7adc418
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.static_model))

        data.write(b"\x15iN\xe1")  # 0x15694ee1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animated_model.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X\xf9\xfe\x99")  # 0x58f9fe99
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x58f9fe99.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1c[J:")  # 0x1c5b4a3a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x87(\xa0\xee")  # 0x8728a0ee
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf1\xcd\x99\xd3")  # 0xf1cd99d3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"j\xbes\x07")  # 0x6abe7307
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1c\x07\xeb\xa9")  # 0x1c07eba9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x87t\x01}")  # 0x8774017d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf1\x918@")  # 0xf1913840
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"j\xe2\xd2\x94")  # 0x6ae2d294
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1c\xe2\t\x1c")  # 0x1ce2091c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.secondary_model8.to_stream(data, game)
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
        json_data = typing.cast("ScannableObjectInfoJson", data)
        return cls(
            string=json_data["string"],
            scan_speed=enums.ScanSpeedEnum.from_json(json_data["scan_speed"]),
            critical=json_data["critical"],
            unknown_0x1733b1ec=json_data["unknown_0x1733b1ec"],
            unknown_0x53336141=json_data["unknown_0x53336141"],
            model_initial_pitch=json_data["model_initial_pitch"],
            model_initial_yaw=json_data["model_initial_yaw"],
            model_scale=json_data["model_scale"],
            static_model=json_data["static_model"],
            animated_model=AnimationParameters.from_json(json_data["animated_model"]),
            unknown_0x58f9fe99=AnimationParameters.from_json(json_data["unknown_0x58f9fe99"]),
            secondary_model0=ScanInfoSecondaryModel.from_json(json_data["secondary_model0"]),
            secondary_model1=ScanInfoSecondaryModel.from_json(json_data["secondary_model1"]),
            secondary_model2=ScanInfoSecondaryModel.from_json(json_data["secondary_model2"]),
            secondary_model3=ScanInfoSecondaryModel.from_json(json_data["secondary_model3"]),
            secondary_model4=ScanInfoSecondaryModel.from_json(json_data["secondary_model4"]),
            secondary_model5=ScanInfoSecondaryModel.from_json(json_data["secondary_model5"]),
            secondary_model6=ScanInfoSecondaryModel.from_json(json_data["secondary_model6"]),
            secondary_model7=ScanInfoSecondaryModel.from_json(json_data["secondary_model7"]),
            secondary_model8=ScanInfoSecondaryModel.from_json(json_data["secondary_model8"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "string": self.string,
            "scan_speed": self.scan_speed.to_json(),
            "critical": self.critical,
            "unknown_0x1733b1ec": self.unknown_0x1733b1ec,
            "unknown_0x53336141": self.unknown_0x53336141,
            "model_initial_pitch": self.model_initial_pitch,
            "model_initial_yaw": self.model_initial_yaw,
            "model_scale": self.model_scale,
            "static_model": self.static_model,
            "animated_model": self.animated_model.to_json(),
            "unknown_0x58f9fe99": self.unknown_0x58f9fe99.to_json(),
            "secondary_model0": self.secondary_model0.to_json(),
            "secondary_model1": self.secondary_model1.to_json(),
            "secondary_model2": self.secondary_model2.to_json(),
            "secondary_model3": self.secondary_model3.to_json(),
            "secondary_model4": self.secondary_model4.to_json(),
            "secondary_model5": self.secondary_model5.to_json(),
            "secondary_model6": self.secondary_model6.to_json(),
            "secondary_model7": self.secondary_model7.to_json(),
            "secondary_model8": self.secondary_model8.to_json(),
        }

    def _dependencies_for_string(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.string)

    def _dependencies_for_unknown_0x53336141(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x53336141)

    def _dependencies_for_static_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.static_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_string, "string", "AssetId"),
            (self._dependencies_for_unknown_0x53336141, "unknown_0x53336141", "AssetId"),
            (self._dependencies_for_static_model, "static_model", "AssetId"),
            (self.animated_model.dependencies_for, "animated_model", "AnimationParameters"),
            (self.unknown_0x58f9fe99.dependencies_for, "unknown_0x58f9fe99", "AnimationParameters"),
            (self.secondary_model0.dependencies_for, "secondary_model0", "ScanInfoSecondaryModel"),
            (self.secondary_model1.dependencies_for, "secondary_model1", "ScanInfoSecondaryModel"),
            (self.secondary_model2.dependencies_for, "secondary_model2", "ScanInfoSecondaryModel"),
            (self.secondary_model3.dependencies_for, "secondary_model3", "ScanInfoSecondaryModel"),
            (self.secondary_model4.dependencies_for, "secondary_model4", "ScanInfoSecondaryModel"),
            (self.secondary_model5.dependencies_for, "secondary_model5", "ScanInfoSecondaryModel"),
            (self.secondary_model6.dependencies_for, "secondary_model6", "ScanInfoSecondaryModel"),
            (self.secondary_model7.dependencies_for, "secondary_model7", "ScanInfoSecondaryModel"),
            (self.secondary_model8.dependencies_for, "secondary_model8", "ScanInfoSecondaryModel"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ScannableObjectInfo.{field_name} ({field_type}): {e}")


def _decode_scan_speed(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ScanSpeedEnum:
    return enums.ScanSpeedEnum.from_stream(data, game)


def _decode_animated_model(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_unknown_0x58f9fe99(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_secondary_model0(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model1(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model2(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model3(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model4(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model5(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model6(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model7(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


def _decode_secondary_model8(data: typing.BinaryIO, game: Game, property_size: int) -> ScanInfoSecondaryModel:
    return ScanInfoSecondaryModel.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2F5B6423: ("string", structs.decode_BIG_L),
    0xC308A322: ("scan_speed", _decode_scan_speed),
    0x7B714814: ("critical", structs.decode_BIG_bool_),
    0x1733B1EC: ("unknown_0x1733b1ec", structs.decode_BIG_bool_),
    0x53336141: ("unknown_0x53336141", structs.decode_BIG_L),
    0x3DE0BA64: ("model_initial_pitch", structs.decode_BIG_f),
    0x2ADD6628: ("model_initial_yaw", structs.decode_BIG_f),
    0xD0C15066: ("model_scale", structs.decode_BIG_f),
    0xB7ADC418: ("static_model", structs.decode_BIG_L),
    0x15694EE1: ("animated_model", _decode_animated_model),
    0x58F9FE99: ("unknown_0x58f9fe99", _decode_unknown_0x58f9fe99),
    0x1C5B4A3A: ("secondary_model0", _decode_secondary_model0),
    0x8728A0EE: ("secondary_model1", _decode_secondary_model1),
    0xF1CD99D3: ("secondary_model2", _decode_secondary_model2),
    0x6ABE7307: ("secondary_model3", _decode_secondary_model3),
    0x1C07EBA9: ("secondary_model4", _decode_secondary_model4),
    0x8774017D: ("secondary_model5", _decode_secondary_model5),
    0xF1913840: ("secondary_model6", _decode_secondary_model6),
    0x6AE2D294: ("secondary_model7", _decode_secondary_model7),
    0x1CE2091C: ("secondary_model8", _decode_secondary_model8),
}
