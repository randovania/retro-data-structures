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
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class VenomWeedJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        vulnerability: json_util.JsonObject
        actor_information: json_util.JsonObject
        character_animation_information: json_util.JsonObject
        density: float
        max_depth: float
        location_variance: float
        detection_radius: float
        grab_radius: float
        unknown_0xd50d757d: float
        unknown_0xcc689024: float
        unknown_0x723737bc: float
        unknown_0x57452dd9: float
        retreat_depth: float
        move_speed: float
        unknown_0x11f854e2: float
        max_slope: float
        min_size: float
        max_size: float
        height_offset: float
        contact_damage: json_util.JsonObject
        sound_looped: int
        sound_into_ground: int
        unknown_0xff90b1e5: int
        unknown_0x4473fec0: int
        retreat_particle_system: int
        unknown_0x534c2bbf: int
        unknown_0x8e30f547: int
        unknown_0x12289828: float


@dataclasses.dataclass()
class VenomWeed(BaseObjectType):
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
    character_animation_information: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xA244C9D8,
                original_name="CharacterAnimationInformation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    density: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x64E5FE9F, original_name="Density"),
        },
    )
    max_depth: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23CEF95F, original_name="MaxDepth"),
        },
    )
    location_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBE02E456, original_name="LocationVariance"),
        },
    )
    detection_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x21CDCF21, original_name="DetectionRadius"),
        },
    )
    grab_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x89664723, original_name="GrabRadius"),
        },
    )
    unknown_0xd50d757d: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD50D757D, original_name="Unknown"),
        },
    )
    unknown_0xcc689024: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCC689024, original_name="Unknown"),
        },
    )
    unknown_0x723737bc: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x723737BC, original_name="Unknown"),
        },
    )
    unknown_0x57452dd9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x57452DD9, original_name="Unknown"),
        },
    )
    retreat_depth: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5C20B0C7, original_name="RetreatDepth"),
        },
    )
    move_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6497C750, original_name="MoveSpeed"),
        },
    )
    unknown_0x11f854e2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x11F854E2, original_name="Unknown"),
        },
    )
    max_slope: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA755C1DF, original_name="MaxSlope"),
        },
    )
    min_size: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x558C6DD7, original_name="MinSize"),
        },
    )
    max_size: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC5FF7D3D, original_name="MaxSize"),
        },
    )
    height_offset: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB2EBC23A, original_name="HeightOffset"),
        },
    )
    contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xD756416E,
                original_name="ContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_looped: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x08BC9A8C, original_name="SoundLooped"),
        },
    )
    sound_into_ground: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6D0DB963, original_name="SoundIntoGround"),
        },
    )
    unknown_0xff90b1e5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xFF90B1E5, original_name="Unknown"),
        },
    )
    unknown_0x4473fec0: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4473FEC0, original_name="Unknown"),
        },
    )
    retreat_particle_system: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x81D5AE6B, original_name="RetreatParticleSystem"),
        },
    )
    unknown_0x534c2bbf: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x534C2BBF, original_name="Unknown"),
        },
    )
    unknown_0x8e30f547: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8E30F547, original_name="Unknown"),
        },
    )
    unknown_0x12289828: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x12289828, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "WEED"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_VenomWeed.rso"]

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
        if property_count != 29:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA244C9D8
        character_animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64E5FE9F
        density = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23CEF95F
        max_depth = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE02E456
        location_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21CDCF21
        detection_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89664723
        grab_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD50D757D
        unknown_0xd50d757d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC689024
        unknown_0xcc689024 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723737BC
        unknown_0x723737bc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57452DD9
        unknown_0x57452dd9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C20B0C7
        retreat_depth = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6497C750
        move_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11F854E2
        unknown_0x11f854e2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA755C1DF
        max_slope = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x558C6DD7
        min_size = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5FF7D3D
        max_size = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2EBC23A
        height_offset = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD756416E
        contact_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08BC9A8C
        sound_looped = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D0DB963
        sound_into_ground = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF90B1E5
        unknown_0xff90b1e5 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4473FEC0
        unknown_0x4473fec0 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81D5AE6B
        retreat_particle_system = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x534C2BBF
        unknown_0x534c2bbf = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E30F547
        unknown_0x8e30f547 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12289828
        unknown_0x12289828 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            vulnerability,
            actor_information,
            character_animation_information,
            density,
            max_depth,
            location_variance,
            detection_radius,
            grab_radius,
            unknown_0xd50d757d,
            unknown_0xcc689024,
            unknown_0x723737bc,
            unknown_0x57452dd9,
            retreat_depth,
            move_speed,
            unknown_0x11f854e2,
            max_slope,
            min_size,
            max_size,
            height_offset,
            contact_damage,
            sound_looped,
            sound_into_ground,
            unknown_0xff90b1e5,
            unknown_0x4473fec0,
            retreat_particle_system,
            unknown_0x534c2bbf,
            unknown_0x8e30f547,
            unknown_0x12289828,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x1d")  # 29 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
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

        data.write(b"\xa2D\xc9\xd8")  # 0xa244c9d8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.character_animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"d\xe5\xfe\x9f")  # 0x64e5fe9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.density))

        data.write(b"#\xce\xf9_")  # 0x23cef95f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_depth))

        data.write(b"\xbe\x02\xe4V")  # 0xbe02e456
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.location_variance))

        data.write(b"!\xcd\xcf!")  # 0x21cdcf21
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.detection_radius))

        data.write(b"\x89fG#")  # 0x89664723
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grab_radius))

        data.write(b"\xd5\ru}")  # 0xd50d757d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd50d757d))

        data.write(b"\xcch\x90$")  # 0xcc689024
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcc689024))

        data.write(b"r77\xbc")  # 0x723737bc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x723737bc))

        data.write(b"WE-\xd9")  # 0x57452dd9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x57452dd9))

        data.write(b"\\ \xb0\xc7")  # 0x5c20b0c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.retreat_depth))

        data.write(b"d\x97\xc7P")  # 0x6497c750
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_speed))

        data.write(b"\x11\xf8T\xe2")  # 0x11f854e2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x11f854e2))

        data.write(b"\xa7U\xc1\xdf")  # 0xa755c1df
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_slope))

        data.write(b"U\x8cm\xd7")  # 0x558c6dd7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_size))

        data.write(b"\xc5\xff}=")  # 0xc5ff7d3d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_size))

        data.write(b"\xb2\xeb\xc2:")  # 0xb2ebc23a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.height_offset))

        data.write(b"\xd7VAn")  # 0xd756416e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x08\xbc\x9a\x8c")  # 0x8bc9a8c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_looped))

        data.write(b"m\r\xb9c")  # 0x6d0db963
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_into_ground))

        data.write(b"\xff\x90\xb1\xe5")  # 0xff90b1e5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xff90b1e5))

        data.write(b"Ds\xfe\xc0")  # 0x4473fec0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x4473fec0))

        data.write(b"\x81\xd5\xaek")  # 0x81d5ae6b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.retreat_particle_system))

        data.write(b"SL+\xbf")  # 0x534c2bbf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x534c2bbf))

        data.write(b"\x8e0\xf5G")  # 0x8e30f547
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x8e30f547))

        data.write(b"\x12(\x98(")  # 0x12289828
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x12289828))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VenomWeedJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            character_animation_information=AnimationParameters.from_json(json_data["character_animation_information"]),
            density=json_data["density"],
            max_depth=json_data["max_depth"],
            location_variance=json_data["location_variance"],
            detection_radius=json_data["detection_radius"],
            grab_radius=json_data["grab_radius"],
            unknown_0xd50d757d=json_data["unknown_0xd50d757d"],
            unknown_0xcc689024=json_data["unknown_0xcc689024"],
            unknown_0x723737bc=json_data["unknown_0x723737bc"],
            unknown_0x57452dd9=json_data["unknown_0x57452dd9"],
            retreat_depth=json_data["retreat_depth"],
            move_speed=json_data["move_speed"],
            unknown_0x11f854e2=json_data["unknown_0x11f854e2"],
            max_slope=json_data["max_slope"],
            min_size=json_data["min_size"],
            max_size=json_data["max_size"],
            height_offset=json_data["height_offset"],
            contact_damage=DamageInfo.from_json(json_data["contact_damage"]),
            sound_looped=json_data["sound_looped"],
            sound_into_ground=json_data["sound_into_ground"],
            unknown_0xff90b1e5=json_data["unknown_0xff90b1e5"],
            unknown_0x4473fec0=json_data["unknown_0x4473fec0"],
            retreat_particle_system=json_data["retreat_particle_system"],
            unknown_0x534c2bbf=json_data["unknown_0x534c2bbf"],
            unknown_0x8e30f547=json_data["unknown_0x8e30f547"],
            unknown_0x12289828=json_data["unknown_0x12289828"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "actor_information": self.actor_information.to_json(),
            "character_animation_information": self.character_animation_information.to_json(),
            "density": self.density,
            "max_depth": self.max_depth,
            "location_variance": self.location_variance,
            "detection_radius": self.detection_radius,
            "grab_radius": self.grab_radius,
            "unknown_0xd50d757d": self.unknown_0xd50d757d,
            "unknown_0xcc689024": self.unknown_0xcc689024,
            "unknown_0x723737bc": self.unknown_0x723737bc,
            "unknown_0x57452dd9": self.unknown_0x57452dd9,
            "retreat_depth": self.retreat_depth,
            "move_speed": self.move_speed,
            "unknown_0x11f854e2": self.unknown_0x11f854e2,
            "max_slope": self.max_slope,
            "min_size": self.min_size,
            "max_size": self.max_size,
            "height_offset": self.height_offset,
            "contact_damage": self.contact_damage.to_json(),
            "sound_looped": self.sound_looped,
            "sound_into_ground": self.sound_into_ground,
            "unknown_0xff90b1e5": self.unknown_0xff90b1e5,
            "unknown_0x4473fec0": self.unknown_0x4473fec0,
            "retreat_particle_system": self.retreat_particle_system,
            "unknown_0x534c2bbf": self.unknown_0x534c2bbf,
            "unknown_0x8e30f547": self.unknown_0x8e30f547,
            "unknown_0x12289828": self.unknown_0x12289828,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_character_animation_information(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xA244C9D8: ("character_animation_information", _decode_character_animation_information),
    0x64E5FE9F: ("density", structs.decode_BIG_f),
    0x23CEF95F: ("max_depth", structs.decode_BIG_f),
    0xBE02E456: ("location_variance", structs.decode_BIG_f),
    0x21CDCF21: ("detection_radius", structs.decode_BIG_f),
    0x89664723: ("grab_radius", structs.decode_BIG_f),
    0xD50D757D: ("unknown_0xd50d757d", structs.decode_BIG_f),
    0xCC689024: ("unknown_0xcc689024", structs.decode_BIG_f),
    0x723737BC: ("unknown_0x723737bc", structs.decode_BIG_f),
    0x57452DD9: ("unknown_0x57452dd9", structs.decode_BIG_f),
    0x5C20B0C7: ("retreat_depth", structs.decode_BIG_f),
    0x6497C750: ("move_speed", structs.decode_BIG_f),
    0x11F854E2: ("unknown_0x11f854e2", structs.decode_BIG_f),
    0xA755C1DF: ("max_slope", structs.decode_BIG_f),
    0x558C6DD7: ("min_size", structs.decode_BIG_f),
    0xC5FF7D3D: ("max_size", structs.decode_BIG_f),
    0xB2EBC23A: ("height_offset", structs.decode_BIG_f),
    0xD756416E: ("contact_damage", _decode_contact_damage),
    0x08BC9A8C: ("sound_looped", structs.decode_BIG_Q),
    0x6D0DB963: ("sound_into_ground", structs.decode_BIG_Q),
    0xFF90B1E5: ("unknown_0xff90b1e5", structs.decode_BIG_Q),
    0x4473FEC0: ("unknown_0x4473fec0", structs.decode_BIG_Q),
    0x81D5AE6B: ("retreat_particle_system", structs.decode_BIG_Q),
    0x534C2BBF: ("unknown_0x534c2bbf", structs.decode_BIG_l),
    0x8E30F547: ("unknown_0x8e30f547", structs.decode_BIG_Q),
    0x12289828: ("unknown_0x12289828", structs.decode_BIG_f),
}
