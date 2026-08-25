# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct10Json(typing_extensions.TypedDict):
        attract: bool
        unknown_0x73c0f1ae: bool
        rotate: bool
        power: float
        radius: float
        alpha_target: float
        alpha_delta: float
        x_ray_alpha_target: float
        x_ray_alpha_delta: float
        unknown_0xf66ca675: float
        unknown_0x8fd14aa3: float
        unknown_0x0a17fbf7: float
        unknown_0x4d04b4f8: float
        flash: bool
        explode: bool
        die: bool
        flash_damage: json_util.JsonObject
        explode_damage: json_util.JsonObject
        sound: int
        auto_transition: bool
        duration: float
        duration_variance: float


@dataclasses.dataclass()
class UnknownStruct10(BaseProperty):
    attract: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE4103CCE, original_name="Attract"),
        },
    )
    unknown_0x73c0f1ae: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x73C0F1AE, original_name="Unknown"),
        },
    )
    rotate: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x923109D6, original_name="Rotate"),
        },
    )
    power: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x10CDA13D, original_name="Power"),
        },
    )
    radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78C507EB, original_name="Radius"),
        },
    )
    alpha_target: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2D72A3D3, original_name="AlphaTarget"),
        },
    )
    alpha_delta: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2A1D3A89, original_name="AlphaDelta"),
        },
    )
    x_ray_alpha_target: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA19C4B46, original_name="XRayAlphaTarget"),
        },
    )
    x_ray_alpha_delta: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x17895CD7, original_name="XRayAlphaDelta"),
        },
    )
    unknown_0xf66ca675: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF66CA675, original_name="Unknown"),
        },
    )
    unknown_0x8fd14aa3: float = dataclasses.field(
        default=0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8FD14AA3, original_name="Unknown"),
        },
    )
    unknown_0x0a17fbf7: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0A17FBF7, original_name="Unknown"),
        },
    )
    unknown_0x4d04b4f8: float = dataclasses.field(
        default=0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4D04B4F8, original_name="Unknown"),
        },
    )
    flash: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4ECAC914, original_name="Flash"),
        },
    )
    explode: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6A922800, original_name="Explode"),
        },
    )
    die: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xD83B3ECA, original_name="Die"),
        },
    )
    flash_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x6A5BD5E5,
                original_name="FlashDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    explode_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xF6206A12,
                original_name="ExplodeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA55DACF6, original_name="Sound"),
        },
    )
    auto_transition: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6575BF29, original_name="AutoTransition"),
        },
    )
    duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B51E23F, original_name="Duration"),
        },
    )
    duration_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8835D69, original_name="DurationVariance"),
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
        if property_count != 22:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE4103CCE
        attract = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73C0F1AE
        unknown_0x73c0f1ae = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x923109D6
        rotate = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10CDA13D
        power = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78C507EB
        radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D72A3D3
        alpha_target = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2A1D3A89
        alpha_delta = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA19C4B46
        x_ray_alpha_target = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17895CD7
        x_ray_alpha_delta = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF66CA675
        unknown_0xf66ca675 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8FD14AA3
        unknown_0x8fd14aa3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A17FBF7
        unknown_0x0a17fbf7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D04B4F8
        unknown_0x4d04b4f8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ECAC914
        flash = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A922800
        explode = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD83B3ECA
        die = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A5BD5E5
        flash_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF6206A12
        explode_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA55DACF6
        sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6575BF29
        auto_transition = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B51E23F
        duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8835D69
        duration_variance = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            attract,
            unknown_0x73c0f1ae,
            rotate,
            power,
            radius,
            alpha_target,
            alpha_delta,
            x_ray_alpha_target,
            x_ray_alpha_delta,
            unknown_0xf66ca675,
            unknown_0x8fd14aa3,
            unknown_0x0a17fbf7,
            unknown_0x4d04b4f8,
            flash,
            explode,
            die,
            flash_damage,
            explode_damage,
            sound,
            auto_transition,
            duration,
            duration_variance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x16")  # 22 properties

        data.write(b"\xe4\x10<\xce")  # 0xe4103cce
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.attract))

        data.write(b"s\xc0\xf1\xae")  # 0x73c0f1ae
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x73c0f1ae))

        data.write(b"\x921\t\xd6")  # 0x923109d6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.rotate))

        data.write(b"\x10\xcd\xa1=")  # 0x10cda13d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.power))

        data.write(b"x\xc5\x07\xeb")  # 0x78c507eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.radius))

        data.write(b"-r\xa3\xd3")  # 0x2d72a3d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alpha_target))

        data.write(b"*\x1d:\x89")  # 0x2a1d3a89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alpha_delta))

        data.write(b"\xa1\x9cKF")  # 0xa19c4b46
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.x_ray_alpha_target))

        data.write(b"\x17\x89\\\xd7")  # 0x17895cd7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.x_ray_alpha_delta))

        data.write(b"\xf6l\xa6u")  # 0xf66ca675
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf66ca675))

        data.write(b"\x8f\xd1J\xa3")  # 0x8fd14aa3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8fd14aa3))

        data.write(b"\n\x17\xfb\xf7")  # 0xa17fbf7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0a17fbf7))

        data.write(b"M\x04\xb4\xf8")  # 0x4d04b4f8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4d04b4f8))

        data.write(b"N\xca\xc9\x14")  # 0x4ecac914
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.flash))

        data.write(b"j\x92(\x00")  # 0x6a922800
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.explode))

        data.write(b"\xd8;>\xca")  # 0xd83b3eca
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.die))

        data.write(b"j[\xd5\xe5")  # 0x6a5bd5e5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flash_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf6 j\x12")  # 0xf6206a12
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.explode_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa5]\xac\xf6")  # 0xa55dacf6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound))

        data.write(b"eu\xbf)")  # 0x6575bf29
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_transition))

        data.write(b"\x8bQ\xe2?")  # 0x8b51e23f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b"\xe8\x83]i")  # 0xe8835d69
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration_variance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct10Json", data)
        return cls(
            attract=json_data["attract"],
            unknown_0x73c0f1ae=json_data["unknown_0x73c0f1ae"],
            rotate=json_data["rotate"],
            power=json_data["power"],
            radius=json_data["radius"],
            alpha_target=json_data["alpha_target"],
            alpha_delta=json_data["alpha_delta"],
            x_ray_alpha_target=json_data["x_ray_alpha_target"],
            x_ray_alpha_delta=json_data["x_ray_alpha_delta"],
            unknown_0xf66ca675=json_data["unknown_0xf66ca675"],
            unknown_0x8fd14aa3=json_data["unknown_0x8fd14aa3"],
            unknown_0x0a17fbf7=json_data["unknown_0x0a17fbf7"],
            unknown_0x4d04b4f8=json_data["unknown_0x4d04b4f8"],
            flash=json_data["flash"],
            explode=json_data["explode"],
            die=json_data["die"],
            flash_damage=DamageInfo.from_json(json_data["flash_damage"]),
            explode_damage=DamageInfo.from_json(json_data["explode_damage"]),
            sound=json_data["sound"],
            auto_transition=json_data["auto_transition"],
            duration=json_data["duration"],
            duration_variance=json_data["duration_variance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "attract": self.attract,
            "unknown_0x73c0f1ae": self.unknown_0x73c0f1ae,
            "rotate": self.rotate,
            "power": self.power,
            "radius": self.radius,
            "alpha_target": self.alpha_target,
            "alpha_delta": self.alpha_delta,
            "x_ray_alpha_target": self.x_ray_alpha_target,
            "x_ray_alpha_delta": self.x_ray_alpha_delta,
            "unknown_0xf66ca675": self.unknown_0xf66ca675,
            "unknown_0x8fd14aa3": self.unknown_0x8fd14aa3,
            "unknown_0x0a17fbf7": self.unknown_0x0a17fbf7,
            "unknown_0x4d04b4f8": self.unknown_0x4d04b4f8,
            "flash": self.flash,
            "explode": self.explode,
            "die": self.die,
            "flash_damage": self.flash_damage.to_json(),
            "explode_damage": self.explode_damage.to_json(),
            "sound": self.sound,
            "auto_transition": self.auto_transition,
            "duration": self.duration,
            "duration_variance": self.duration_variance,
        }


def _decode_flash_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_explode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xE4103CCE: ("attract", structs.decode_BIG_bool_),
    0x73C0F1AE: ("unknown_0x73c0f1ae", structs.decode_BIG_bool_),
    0x923109D6: ("rotate", structs.decode_BIG_bool_),
    0x10CDA13D: ("power", structs.decode_BIG_f),
    0x78C507EB: ("radius", structs.decode_BIG_f),
    0x2D72A3D3: ("alpha_target", structs.decode_BIG_f),
    0x2A1D3A89: ("alpha_delta", structs.decode_BIG_f),
    0xA19C4B46: ("x_ray_alpha_target", structs.decode_BIG_f),
    0x17895CD7: ("x_ray_alpha_delta", structs.decode_BIG_f),
    0xF66CA675: ("unknown_0xf66ca675", structs.decode_BIG_f),
    0x8FD14AA3: ("unknown_0x8fd14aa3", structs.decode_BIG_f),
    0x0A17FBF7: ("unknown_0x0a17fbf7", structs.decode_BIG_f),
    0x4D04B4F8: ("unknown_0x4d04b4f8", structs.decode_BIG_f),
    0x4ECAC914: ("flash", structs.decode_BIG_bool_),
    0x6A922800: ("explode", structs.decode_BIG_bool_),
    0xD83B3ECA: ("die", structs.decode_BIG_bool_),
    0x6A5BD5E5: ("flash_damage", _decode_flash_damage),
    0xF6206A12: ("explode_damage", _decode_explode_damage),
    0xA55DACF6: ("sound", structs.decode_BIG_Q),
    0x6575BF29: ("auto_transition", structs.decode_BIG_bool_),
    0x8B51E23F: ("duration", structs.decode_BIG_f),
    0xE8835D69: ("duration_variance", structs.decode_BIG_f),
}
