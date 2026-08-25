# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.echoes.archetypes.TweakGame_CoinLimitChoices import TweakGame_CoinLimitChoices
from retro_data_structures.properties.echoes.archetypes.TweakGame_FragLimitChoices import TweakGame_FragLimitChoices
from retro_data_structures.properties.echoes.archetypes.TweakGame_TimeLimitChoices import TweakGame_TimeLimitChoices
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TweakGameJson(typing_extensions.TypedDict):
        instance_name: str
        pak_file: str
        asset: str
        fieldof_view: float
        fieldof_view2_player: float
        disable_debug_menu: bool
        unknown_0x7262d27b: bool
        development_mode: bool
        unknown_0xa3dcf42a: float
        unknown_0xb35c72be: float
        unknown_0x4a02103c: float
        unknown_0xe1fca71b: float
        unknown_0xfbce966a: float
        unknown_0x09c6ca10: float
        hard_mode_damage_multiplier: float
        hard_mode_weapon_multiplier: float
        unknown_0x5ab5812c: float
        unknown_0x53401390: float
        total_percentage: int
        unknown_0x1d627808: json_util.JsonObject
        unknown_0xb2e8828d: json_util.JsonObject
        unknown_0x06af87bd: json_util.JsonObject
        unknown_0x1533ea4e: json_util.JsonObject
        unknown_0x40818220: json_util.JsonObject


@dataclasses.dataclass()
class TweakGame(BaseObjectType):
    instance_name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x7FDA1466, original_name="InstanceName"),
        },
    )
    pak_file: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x2BD13AB3, original_name="PakFile"),
        },
    )
    asset: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xF8BE005A, original_name="Asset"),
        },
    )
    fieldof_view: float = dataclasses.field(
        default=55.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFC93CEB8, original_name="FieldofView"),
        },
    )
    fieldof_view2_player: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9FB2FAA6, original_name="FieldofView2Player"),
        },
    )
    disable_debug_menu: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA9096914, original_name="DisableDebugMenu"),
        },
    )
    unknown_0x7262d27b: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7262D27B, original_name="Unknown"),
        },
    )
    development_mode: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE943BA12, original_name="DevelopmentMode"),
        },
    )
    unknown_0xa3dcf42a: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA3DCF42A, original_name="Unknown"),
        },
    )
    unknown_0xb35c72be: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB35C72BE, original_name="Unknown"),
        },
    )
    unknown_0x4a02103c: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4A02103C, original_name="Unknown"),
        },
    )
    unknown_0xe1fca71b: float = dataclasses.field(
        default=125.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE1FCA71B, original_name="Unknown"),
        },
    )
    unknown_0xfbce966a: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFBCE966A, original_name="Unknown"),
        },
    )
    unknown_0x09c6ca10: float = dataclasses.field(
        default=300.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x09C6CA10, original_name="Unknown"),
        },
    )
    hard_mode_damage_multiplier: float = dataclasses.field(
        default=1.5299999713897705,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4DFCD432, original_name="HardModeDamageMultiplier"),
        },
    )
    hard_mode_weapon_multiplier: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAE1831D9, original_name="HardModeWeaponMultiplier"),
        },
    )
    unknown_0x5ab5812c: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5AB5812C, original_name="Unknown"),
        },
    )
    unknown_0x53401390: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x53401390, original_name="Unknown"),
        },
    )
    total_percentage: int = dataclasses.field(
        default=102,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD09F373B, original_name="TotalPercentage"),
        },
    )
    unknown_0x1d627808: TweakGame_FragLimitChoices = dataclasses.field(
        default_factory=TweakGame_FragLimitChoices,
        metadata={
            "reflection": FieldReflection[TweakGame_FragLimitChoices](
                TweakGame_FragLimitChoices,
                id=0x1D627808,
                original_name="Unknown",
                from_json=TweakGame_FragLimitChoices.from_json,
                to_json=TweakGame_FragLimitChoices.to_json,
            ),
        },
    )
    unknown_0xb2e8828d: TweakGame_TimeLimitChoices = dataclasses.field(
        default_factory=TweakGame_TimeLimitChoices,
        metadata={
            "reflection": FieldReflection[TweakGame_TimeLimitChoices](
                TweakGame_TimeLimitChoices,
                id=0xB2E8828D,
                original_name="Unknown",
                from_json=TweakGame_TimeLimitChoices.from_json,
                to_json=TweakGame_TimeLimitChoices.to_json,
            ),
        },
    )
    unknown_0x06af87bd: TweakGame_CoinLimitChoices = dataclasses.field(
        default_factory=TweakGame_CoinLimitChoices,
        metadata={
            "reflection": FieldReflection[TweakGame_CoinLimitChoices](
                TweakGame_CoinLimitChoices,
                id=0x06AF87BD,
                original_name="Unknown",
                from_json=TweakGame_CoinLimitChoices.from_json,
                to_json=TweakGame_CoinLimitChoices.to_json,
            ),
        },
    )
    unknown_0x1533ea4e: TweakGame_TimeLimitChoices = dataclasses.field(
        default_factory=TweakGame_TimeLimitChoices,
        metadata={
            "reflection": FieldReflection[TweakGame_TimeLimitChoices](
                TweakGame_TimeLimitChoices,
                id=0x1533EA4E,
                original_name="Unknown",
                from_json=TweakGame_TimeLimitChoices.from_json,
                to_json=TweakGame_TimeLimitChoices.to_json,
            ),
        },
    )
    unknown_0x40818220: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x40818220, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return "TWGM"

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
        if property_count != 24:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FDA1466
        instance_name = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BD13AB3
        pak_file = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8BE005A
        asset = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC93CEB8
        fieldof_view = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9FB2FAA6
        fieldof_view2_player = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9096914
        disable_debug_menu = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7262D27B
        unknown_0x7262d27b = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE943BA12
        development_mode = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3DCF42A
        unknown_0xa3dcf42a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB35C72BE
        unknown_0xb35c72be = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A02103C
        unknown_0x4a02103c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1FCA71B
        unknown_0xe1fca71b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBCE966A
        unknown_0xfbce966a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09C6CA10
        unknown_0x09c6ca10 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4DFCD432
        hard_mode_damage_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE1831D9
        hard_mode_weapon_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5AB5812C
        unknown_0x5ab5812c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53401390
        unknown_0x53401390 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD09F373B
        total_percentage = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D627808
        unknown_0x1d627808 = TweakGame_FragLimitChoices.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2E8828D
        unknown_0xb2e8828d = TweakGame_TimeLimitChoices.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06AF87BD
        unknown_0x06af87bd = TweakGame_CoinLimitChoices.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1533EA4E
        unknown_0x1533ea4e = TweakGame_TimeLimitChoices.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40818220
        unknown_0x40818220 = Spline.from_stream(data, game, property_size)

        return cls(
            instance_name,
            pak_file,
            asset,
            fieldof_view,
            fieldof_view2_player,
            disable_debug_menu,
            unknown_0x7262d27b,
            development_mode,
            unknown_0xa3dcf42a,
            unknown_0xb35c72be,
            unknown_0x4a02103c,
            unknown_0xe1fca71b,
            unknown_0xfbce966a,
            unknown_0x09c6ca10,
            hard_mode_damage_multiplier,
            hard_mode_weapon_multiplier,
            unknown_0x5ab5812c,
            unknown_0x53401390,
            total_percentage,
            unknown_0x1d627808,
            unknown_0xb2e8828d,
            unknown_0x06af87bd,
            unknown_0x1533ea4e,
            unknown_0x40818220,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x18")  # 24 properties

        data.write(b"\x7f\xda\x14f")  # 0x7fda1466
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.instance_name.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+\xd1:\xb3")  # 0x2bd13ab3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.pak_file.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf8\xbe\x00Z")  # 0xf8be005a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.asset.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfc\x93\xce\xb8")  # 0xfc93ceb8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fieldof_view))

        data.write(b"\x9f\xb2\xfa\xa6")  # 0x9fb2faa6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fieldof_view2_player))

        data.write(b"\xa9\ti\x14")  # 0xa9096914
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.disable_debug_menu))

        data.write(b"rb\xd2{")  # 0x7262d27b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7262d27b))

        data.write(b"\xe9C\xba\x12")  # 0xe943ba12
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.development_mode))

        data.write(b"\xa3\xdc\xf4*")  # 0xa3dcf42a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa3dcf42a))

        data.write(b"\xb3\\r\xbe")  # 0xb35c72be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb35c72be))

        data.write(b"J\x02\x10<")  # 0x4a02103c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4a02103c))

        data.write(b"\xe1\xfc\xa7\x1b")  # 0xe1fca71b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe1fca71b))

        data.write(b"\xfb\xce\x96j")  # 0xfbce966a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfbce966a))

        data.write(b"\t\xc6\xca\x10")  # 0x9c6ca10
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x09c6ca10))

        data.write(b"M\xfc\xd42")  # 0x4dfcd432
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hard_mode_damage_multiplier))

        data.write(b"\xae\x181\xd9")  # 0xae1831d9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hard_mode_weapon_multiplier))

        data.write(b"Z\xb5\x81,")  # 0x5ab5812c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5ab5812c))

        data.write(b"S@\x13\x90")  # 0x53401390
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x53401390))

        data.write(b"\xd0\x9f7;")  # 0xd09f373b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.total_percentage))

        data.write(b"\x1dbx\x08")  # 0x1d627808
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x1d627808.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb2\xe8\x82\x8d")  # 0xb2e8828d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xb2e8828d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x06\xaf\x87\xbd")  # 0x6af87bd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x06af87bd.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x153\xeaN")  # 0x1533ea4e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x1533ea4e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"@\x81\x82 ")  # 0x40818220
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x40818220.to_stream(data, game)
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
        json_data = typing.cast("TweakGameJson", data)
        return cls(
            instance_name=json_data["instance_name"],
            pak_file=json_data["pak_file"],
            asset=json_data["asset"],
            fieldof_view=json_data["fieldof_view"],
            fieldof_view2_player=json_data["fieldof_view2_player"],
            disable_debug_menu=json_data["disable_debug_menu"],
            unknown_0x7262d27b=json_data["unknown_0x7262d27b"],
            development_mode=json_data["development_mode"],
            unknown_0xa3dcf42a=json_data["unknown_0xa3dcf42a"],
            unknown_0xb35c72be=json_data["unknown_0xb35c72be"],
            unknown_0x4a02103c=json_data["unknown_0x4a02103c"],
            unknown_0xe1fca71b=json_data["unknown_0xe1fca71b"],
            unknown_0xfbce966a=json_data["unknown_0xfbce966a"],
            unknown_0x09c6ca10=json_data["unknown_0x09c6ca10"],
            hard_mode_damage_multiplier=json_data["hard_mode_damage_multiplier"],
            hard_mode_weapon_multiplier=json_data["hard_mode_weapon_multiplier"],
            unknown_0x5ab5812c=json_data["unknown_0x5ab5812c"],
            unknown_0x53401390=json_data["unknown_0x53401390"],
            total_percentage=json_data["total_percentage"],
            unknown_0x1d627808=TweakGame_FragLimitChoices.from_json(json_data["unknown_0x1d627808"]),
            unknown_0xb2e8828d=TweakGame_TimeLimitChoices.from_json(json_data["unknown_0xb2e8828d"]),
            unknown_0x06af87bd=TweakGame_CoinLimitChoices.from_json(json_data["unknown_0x06af87bd"]),
            unknown_0x1533ea4e=TweakGame_TimeLimitChoices.from_json(json_data["unknown_0x1533ea4e"]),
            unknown_0x40818220=Spline.from_json(json_data["unknown_0x40818220"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "instance_name": self.instance_name,
            "pak_file": self.pak_file,
            "asset": self.asset,
            "fieldof_view": self.fieldof_view,
            "fieldof_view2_player": self.fieldof_view2_player,
            "disable_debug_menu": self.disable_debug_menu,
            "unknown_0x7262d27b": self.unknown_0x7262d27b,
            "development_mode": self.development_mode,
            "unknown_0xa3dcf42a": self.unknown_0xa3dcf42a,
            "unknown_0xb35c72be": self.unknown_0xb35c72be,
            "unknown_0x4a02103c": self.unknown_0x4a02103c,
            "unknown_0xe1fca71b": self.unknown_0xe1fca71b,
            "unknown_0xfbce966a": self.unknown_0xfbce966a,
            "unknown_0x09c6ca10": self.unknown_0x09c6ca10,
            "hard_mode_damage_multiplier": self.hard_mode_damage_multiplier,
            "hard_mode_weapon_multiplier": self.hard_mode_weapon_multiplier,
            "unknown_0x5ab5812c": self.unknown_0x5ab5812c,
            "unknown_0x53401390": self.unknown_0x53401390,
            "total_percentage": self.total_percentage,
            "unknown_0x1d627808": self.unknown_0x1d627808.to_json(),
            "unknown_0xb2e8828d": self.unknown_0xb2e8828d.to_json(),
            "unknown_0x06af87bd": self.unknown_0x06af87bd.to_json(),
            "unknown_0x1533ea4e": self.unknown_0x1533ea4e.to_json(),
            "unknown_0x40818220": self.unknown_0x40818220.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_pak_file(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_asset(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x1d627808(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGame_FragLimitChoices:
    return TweakGame_FragLimitChoices.from_stream(data, game, property_size)


def _decode_unknown_0xb2e8828d(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGame_TimeLimitChoices:
    return TweakGame_TimeLimitChoices.from_stream(data, game, property_size)


def _decode_unknown_0x06af87bd(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGame_CoinLimitChoices:
    return TweakGame_CoinLimitChoices.from_stream(data, game, property_size)


def _decode_unknown_0x1533ea4e(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGame_TimeLimitChoices:
    return TweakGame_TimeLimitChoices.from_stream(data, game, property_size)


def _decode_unknown_0x40818220(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FDA1466: ("instance_name", _decode_instance_name),
    0x2BD13AB3: ("pak_file", _decode_pak_file),
    0xF8BE005A: ("asset", _decode_asset),
    0xFC93CEB8: ("fieldof_view", structs.decode_BIG_f),
    0x9FB2FAA6: ("fieldof_view2_player", structs.decode_BIG_f),
    0xA9096914: ("disable_debug_menu", structs.decode_BIG_bool_),
    0x7262D27B: ("unknown_0x7262d27b", structs.decode_BIG_bool_),
    0xE943BA12: ("development_mode", structs.decode_BIG_bool_),
    0xA3DCF42A: ("unknown_0xa3dcf42a", structs.decode_BIG_f),
    0xB35C72BE: ("unknown_0xb35c72be", structs.decode_BIG_f),
    0x4A02103C: ("unknown_0x4a02103c", structs.decode_BIG_f),
    0xE1FCA71B: ("unknown_0xe1fca71b", structs.decode_BIG_f),
    0xFBCE966A: ("unknown_0xfbce966a", structs.decode_BIG_f),
    0x09C6CA10: ("unknown_0x09c6ca10", structs.decode_BIG_f),
    0x4DFCD432: ("hard_mode_damage_multiplier", structs.decode_BIG_f),
    0xAE1831D9: ("hard_mode_weapon_multiplier", structs.decode_BIG_f),
    0x5AB5812C: ("unknown_0x5ab5812c", structs.decode_BIG_f),
    0x53401390: ("unknown_0x53401390", structs.decode_BIG_f),
    0xD09F373B: ("total_percentage", structs.decode_BIG_l),
    0x1D627808: ("unknown_0x1d627808", _decode_unknown_0x1d627808),
    0xB2E8828D: ("unknown_0xb2e8828d", _decode_unknown_0xb2e8828d),
    0x06AF87BD: ("unknown_0x06af87bd", _decode_unknown_0x06af87bd),
    0x1533EA4E: ("unknown_0x1533ea4e", _decode_unknown_0x1533ea4e),
    0x40818220: ("unknown_0x40818220", _decode_unknown_0x40818220),
}
