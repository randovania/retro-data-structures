# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.MultiModelInformation import MultiModelInformation
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MultiModelActorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        collision_model: int
        model: int
        multi_model_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        unknown: bool
        use_mod_inca: bool
        mod_inca_color: json_util.JsonValue
        mod_inca_amount: json_util.JsonObject
        orbit_offset: json_util.JsonValue
        orbit_offset_local: bool
        is_solid: bool
        immovable: bool


@dataclasses.dataclass()
class MultiModelActor(BaseObjectType):
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
    collision_box: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xF344C0B0, original_name="CollisionBox", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x2E686C2A,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    collision_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["DCLN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0FC966DC, original_name="CollisionModel"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC27FFA8F, original_name="Model"),
        },
    )
    multi_model_information: MultiModelInformation = dataclasses.field(
        default_factory=MultiModelInformation,
        metadata={
            "reflection": FieldReflection[MultiModelInformation](
                MultiModelInformation,
                id=0x1960932D,
                original_name="MultiModelInformation",
                from_json=MultiModelInformation.from_json,
                to_json=MultiModelInformation.to_json,
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
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA09D4A1F, original_name="Unknown"),
        },
    )
    use_mod_inca: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB530D7DE, original_name="UseModInca"),
        },
    )
    mod_inca_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF8DF6CD2, original_name="ModIncaColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    mod_inca_amount: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xC23011D9, original_name="ModIncaAmount", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    orbit_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x850115E4, original_name="OrbitOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    orbit_offset_local: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE73F123D, original_name="OrbitOffsetLocal"),
        },
    )
    is_solid: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1D8DD846, original_name="IsSolid"),
        },
    )
    immovable: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1E32523E, original_name="Immovable"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "MMDL"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_ScriptMultiModelActor.rso"]

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
        if property_count != 15:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF344C0B0
        collision_box = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E686C2A
        collision_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FC966DC
        collision_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1960932D
        multi_model_information = MultiModelInformation.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA09D4A1F
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB530D7DE
        use_mod_inca = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8DF6CD2
        mod_inca_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC23011D9
        mod_inca_amount = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x850115E4
        orbit_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE73F123D
        orbit_offset_local = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D8DD846
        is_solid = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E32523E
        immovable = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            collision_box,
            collision_offset,
            collision_model,
            model,
            multi_model_information,
            actor_information,
            unknown,
            use_mod_inca,
            mod_inca_color,
            mod_inca_amount,
            orbit_offset,
            orbit_offset_local,
            is_solid,
            immovable,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3D\xc0\xb0")  # 0xf344c0b0
        data.write(b"\x00\x0c")  # size
        self.collision_box.to_stream(data, game)

        data.write(b".hl*")  # 0x2e686c2a
        data.write(b"\x00\x0c")  # size
        self.collision_offset.to_stream(data, game)

        data.write(b"\x0f\xc9f\xdc")  # 0xfc966dc
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.collision_model))

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model))

        data.write(b"\x19`\x93-")  # 0x1960932d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.multi_model_information.to_stream(data, game)
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

        data.write(b"\xa0\x9dJ\x1f")  # 0xa09d4a1f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b"\xb50\xd7\xde")  # 0xb530d7de
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_mod_inca))

        data.write(b"\xf8\xdfl\xd2")  # 0xf8df6cd2
        data.write(b"\x00\x10")  # size
        self.mod_inca_color.to_stream(data, game)

        data.write(b"\xc20\x11\xd9")  # 0xc23011d9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.mod_inca_amount.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x85\x01\x15\xe4")  # 0x850115e4
        data.write(b"\x00\x0c")  # size
        self.orbit_offset.to_stream(data, game)

        data.write(b"\xe7?\x12=")  # 0xe73f123d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.orbit_offset_local))

        data.write(b"\x1d\x8d\xd8F")  # 0x1d8dd846
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_solid))

        data.write(b"\x1e2R>")  # 0x1e32523e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.immovable))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MultiModelActorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            collision_model=json_data["collision_model"],
            model=json_data["model"],
            multi_model_information=MultiModelInformation.from_json(json_data["multi_model_information"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            unknown=json_data["unknown"],
            use_mod_inca=json_data["use_mod_inca"],
            mod_inca_color=Color.from_json(json_data["mod_inca_color"]),
            mod_inca_amount=Spline.from_json(json_data["mod_inca_amount"]),
            orbit_offset=Vector.from_json(json_data["orbit_offset"]),
            orbit_offset_local=json_data["orbit_offset_local"],
            is_solid=json_data["is_solid"],
            immovable=json_data["immovable"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "collision_model": self.collision_model,
            "model": self.model,
            "multi_model_information": self.multi_model_information.to_json(),
            "actor_information": self.actor_information.to_json(),
            "unknown": self.unknown,
            "use_mod_inca": self.use_mod_inca,
            "mod_inca_color": self.mod_inca_color.to_json(),
            "mod_inca_amount": self.mod_inca_amount.to_json(),
            "orbit_offset": self.orbit_offset.to_json(),
            "orbit_offset_local": self.orbit_offset_local,
            "is_solid": self.is_solid,
            "immovable": self.immovable,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_multi_model_information(data: typing.BinaryIO, game: Game, property_size: int) -> MultiModelInformation:
    return MultiModelInformation.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_mod_inca_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_mod_inca_amount(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_orbit_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xF344C0B0: ("collision_box", _decode_collision_box),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0x0FC966DC: ("collision_model", structs.decode_BIG_Q),
    0xC27FFA8F: ("model", structs.decode_BIG_Q),
    0x1960932D: ("multi_model_information", _decode_multi_model_information),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xA09D4A1F: ("unknown", structs.decode_BIG_bool_),
    0xB530D7DE: ("use_mod_inca", structs.decode_BIG_bool_),
    0xF8DF6CD2: ("mod_inca_color", _decode_mod_inca_color),
    0xC23011D9: ("mod_inca_amount", _decode_mod_inca_amount),
    0x850115E4: ("orbit_offset", _decode_orbit_offset),
    0xE73F123D: ("orbit_offset_local", structs.decode_BIG_bool_),
    0x1D8DD846: ("is_solid", structs.decode_BIG_bool_),
    0x1E32523E: ("immovable", structs.decode_BIG_bool_),
}
