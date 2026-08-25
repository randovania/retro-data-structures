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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.EchoParameters import EchoParameters
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PickupJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_size: json_util.JsonValue
        collision_offset: json_util.JsonValue
        item_to_give: int
        capacity_increase: int
        item_percentage_increase: int
        amount: int
        respawn_time: float
        pickup_effect_lifetime: float
        lifetime: float
        fadetime: float
        model: int
        animation_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        echo_information: json_util.JsonObject
        activation_delay: float
        pickup_effect: int
        absolute_value: bool
        calculate_visibility: bool
        unknown: bool
        auto_home_range: float
        delay_until_home: float
        homing_speed: float
        auto_spin: bool
        blink_out: bool
        orbit_offset: json_util.JsonValue


@dataclasses.dataclass()
class Pickup(BaseObjectType):
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
    collision_size: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x3A3E03BA, original_name="CollisionSize", from_json=Vector.from_json, to_json=Vector.to_json
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
    item_to_give: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0xA02EF0C4,
                original_name="ItemToGive",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    capacity_increase: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x28C71B54, original_name="CapacityIncrease"),
        },
    )
    item_percentage_increase: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x165AB069, original_name="ItemPercentageIncrease"),
        },
    )
    amount: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x94AF1445, original_name="Amount"),
        },
    )
    respawn_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF7FBAAA5, original_name="RespawnTime"),
        },
    )
    pickup_effect_lifetime: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC80FC827, original_name="PickupEffectLifetime"),
        },
    )
    lifetime: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x32DC67F6, original_name="Lifetime"),
        },
    )
    fadetime: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x56E3CEEF, original_name="Fadetime"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC27FFA8F, original_name="Model"),
        },
    )
    animation_information: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xE25FB08C,
                original_name="AnimationInformation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
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
    echo_information: EchoParameters = dataclasses.field(
        default_factory=EchoParameters,
        metadata={
            "reflection": FieldReflection[EchoParameters](
                EchoParameters,
                id=0x192B0E70,
                original_name="EchoInformation",
                from_json=EchoParameters.from_json,
                to_json=EchoParameters.to_json,
            ),
        },
    )
    activation_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE585F166, original_name="ActivationDelay"),
        },
    )
    pickup_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA9FE872A, original_name="PickupEffect"),
        },
    )
    absolute_value: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE10BCB96, original_name="AbsoluteValue"),
        },
    )
    calculate_visibility: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCE33239F, original_name="CalculateVisibility"),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2DE4A294, original_name="Unknown"),
        },
    )
    auto_home_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA6EA280D, original_name="AutoHomeRange"),
        },
    )
    delay_until_home: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC2B11CFD, original_name="DelayUntilHome"),
        },
    )
    homing_speed: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DB59FCF, original_name="HomingSpeed"),
        },
    )
    auto_spin: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x961C0D17, original_name="AutoSpin"),
        },
    )
    blink_out: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA755EB02, original_name="BlinkOut"),
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

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PCKP"

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
        if property_count != 26:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A3E03BA
        collision_size = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E686C2A
        collision_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA02EF0C4
        item_to_give = enums.PlayerItemEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28C71B54
        capacity_increase = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x165AB069
        item_percentage_increase = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94AF1445
        amount = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF7FBAAA5
        respawn_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC80FC827
        pickup_effect_lifetime = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32DC67F6
        lifetime = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56E3CEEF
        fadetime = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x192B0E70
        echo_information = EchoParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE585F166
        activation_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9FE872A
        pickup_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE10BCB96
        absolute_value = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE33239F
        calculate_visibility = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DE4A294
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6EA280D
        auto_home_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2B11CFD
        delay_until_home = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DB59FCF
        homing_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x961C0D17
        auto_spin = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA755EB02
        blink_out = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x850115E4
        orbit_offset = Vector.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            collision_size,
            collision_offset,
            item_to_give,
            capacity_increase,
            item_percentage_increase,
            amount,
            respawn_time,
            pickup_effect_lifetime,
            lifetime,
            fadetime,
            model,
            animation_information,
            actor_information,
            echo_information,
            activation_delay,
            pickup_effect,
            absolute_value,
            calculate_visibility,
            unknown,
            auto_home_range,
            delay_until_home,
            homing_speed,
            auto_spin,
            blink_out,
            orbit_offset,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x1a")  # 26 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b":>\x03\xba")  # 0x3a3e03ba
        data.write(b"\x00\x0c")  # size
        self.collision_size.to_stream(data, game)

        data.write(b".hl*")  # 0x2e686c2a
        data.write(b"\x00\x0c")  # size
        self.collision_offset.to_stream(data, game)

        data.write(b"\xa0.\xf0\xc4")  # 0xa02ef0c4
        data.write(b"\x00\x04")  # size
        self.item_to_give.to_stream(data, game)

        data.write(b"(\xc7\x1bT")  # 0x28c71b54
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.capacity_increase))

        data.write(b"\x16Z\xb0i")  # 0x165ab069
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.item_percentage_increase))

        data.write(b"\x94\xaf\x14E")  # 0x94af1445
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.amount))

        data.write(b"\xf7\xfb\xaa\xa5")  # 0xf7fbaaa5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.respawn_time))

        data.write(b"\xc8\x0f\xc8'")  # 0xc80fc827
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pickup_effect_lifetime))

        data.write(b"2\xdcg\xf6")  # 0x32dc67f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lifetime))

        data.write(b"V\xe3\xce\xef")  # 0x56e3ceef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fadetime))

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.model))

        data.write(b"\xe2_\xb0\x8c")  # 0xe25fb08c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation_information.to_stream(data, game)
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

        data.write(b"\x19+\x0ep")  # 0x192b0e70
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.echo_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe5\x85\xf1f")  # 0xe585f166
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.activation_delay))

        data.write(b"\xa9\xfe\x87*")  # 0xa9fe872a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.pickup_effect))

        data.write(b"\xe1\x0b\xcb\x96")  # 0xe10bcb96
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.absolute_value))

        data.write(b"\xce3#\x9f")  # 0xce33239f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.calculate_visibility))

        data.write(b"-\xe4\xa2\x94")  # 0x2de4a294
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b"\xa6\xea(\r")  # 0xa6ea280d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.auto_home_range))

        data.write(b"\xc2\xb1\x1c\xfd")  # 0xc2b11cfd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.delay_until_home))

        data.write(b"-\xb5\x9f\xcf")  # 0x2db59fcf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.homing_speed))

        data.write(b"\x96\x1c\r\x17")  # 0x961c0d17
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_spin))

        data.write(b"\xa7U\xeb\x02")  # 0xa755eb02
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.blink_out))

        data.write(b"\x85\x01\x15\xe4")  # 0x850115e4
        data.write(b"\x00\x0c")  # size
        self.orbit_offset.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PickupJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            collision_size=Vector.from_json(json_data["collision_size"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            item_to_give=enums.PlayerItemEnum.from_json(json_data["item_to_give"]),
            capacity_increase=json_data["capacity_increase"],
            item_percentage_increase=json_data["item_percentage_increase"],
            amount=json_data["amount"],
            respawn_time=json_data["respawn_time"],
            pickup_effect_lifetime=json_data["pickup_effect_lifetime"],
            lifetime=json_data["lifetime"],
            fadetime=json_data["fadetime"],
            model=json_data["model"],
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            echo_information=EchoParameters.from_json(json_data["echo_information"]),
            activation_delay=json_data["activation_delay"],
            pickup_effect=json_data["pickup_effect"],
            absolute_value=json_data["absolute_value"],
            calculate_visibility=json_data["calculate_visibility"],
            unknown=json_data["unknown"],
            auto_home_range=json_data["auto_home_range"],
            delay_until_home=json_data["delay_until_home"],
            homing_speed=json_data["homing_speed"],
            auto_spin=json_data["auto_spin"],
            blink_out=json_data["blink_out"],
            orbit_offset=Vector.from_json(json_data["orbit_offset"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "collision_size": self.collision_size.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "item_to_give": self.item_to_give.to_json(),
            "capacity_increase": self.capacity_increase,
            "item_percentage_increase": self.item_percentage_increase,
            "amount": self.amount,
            "respawn_time": self.respawn_time,
            "pickup_effect_lifetime": self.pickup_effect_lifetime,
            "lifetime": self.lifetime,
            "fadetime": self.fadetime,
            "model": self.model,
            "animation_information": self.animation_information.to_json(),
            "actor_information": self.actor_information.to_json(),
            "echo_information": self.echo_information.to_json(),
            "activation_delay": self.activation_delay,
            "pickup_effect": self.pickup_effect,
            "absolute_value": self.absolute_value,
            "calculate_visibility": self.calculate_visibility,
            "unknown": self.unknown,
            "auto_home_range": self.auto_home_range,
            "delay_until_home": self.delay_until_home,
            "homing_speed": self.homing_speed,
            "auto_spin": self.auto_spin,
            "blink_out": self.blink_out,
            "orbit_offset": self.orbit_offset.to_json(),
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_pickup_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pickup_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_pickup_effect, "pickup_effect", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Pickup.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_item_to_give(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PlayerItemEnum:
    return enums.PlayerItemEnum.from_stream(data, game)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_echo_information(data: typing.BinaryIO, game: Game, property_size: int) -> EchoParameters:
    return EchoParameters.from_stream(data, game, property_size)


def _decode_orbit_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x3A3E03BA: ("collision_size", _decode_collision_size),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0xA02EF0C4: ("item_to_give", _decode_item_to_give),
    0x28C71B54: ("capacity_increase", structs.decode_BIG_l),
    0x165AB069: ("item_percentage_increase", structs.decode_BIG_l),
    0x94AF1445: ("amount", structs.decode_BIG_l),
    0xF7FBAAA5: ("respawn_time", structs.decode_BIG_f),
    0xC80FC827: ("pickup_effect_lifetime", structs.decode_BIG_f),
    0x32DC67F6: ("lifetime", structs.decode_BIG_f),
    0x56E3CEEF: ("fadetime", structs.decode_BIG_f),
    0xC27FFA8F: ("model", structs.decode_BIG_L),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x192B0E70: ("echo_information", _decode_echo_information),
    0xE585F166: ("activation_delay", structs.decode_BIG_f),
    0xA9FE872A: ("pickup_effect", structs.decode_BIG_L),
    0xE10BCB96: ("absolute_value", structs.decode_BIG_bool_),
    0xCE33239F: ("calculate_visibility", structs.decode_BIG_bool_),
    0x2DE4A294: ("unknown", structs.decode_BIG_bool_),
    0xA6EA280D: ("auto_home_range", structs.decode_BIG_f),
    0xC2B11CFD: ("delay_until_home", structs.decode_BIG_f),
    0x2DB59FCF: ("homing_speed", structs.decode_BIG_f),
    0x961C0D17: ("auto_spin", structs.decode_BIG_bool_),
    0xA755EB02: ("blink_out", structs.decode_BIG_bool_),
    0x850115E4: ("orbit_offset", _decode_orbit_offset),
}
