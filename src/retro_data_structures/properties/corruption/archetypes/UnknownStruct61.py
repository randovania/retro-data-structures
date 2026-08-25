# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct61Json(typing_extensions.TypedDict):
        patrol: json_util.JsonObject
        attack: json_util.JsonObject
        part: int
        missile_deflection_radius: float
        missile_deflection_rate: float
        unknown_0x8ac503de: int
        shot_prediction: float
        close_enough_distance: float
        minimum_firing_distance: float
        maximum_firing_distance: float
        recheck_path_distance: float
        update_path_time: float
        unknown_0x271e49b4: float
        projectile_left: json_util.JsonObject
        projectile_right: json_util.JsonObject
        reload_delay: float
        shot_delay: float
        unknown_0x04d03b18: float
        grapple_data: json_util.JsonObject
        dodge_chance_after_fire: int
        dodge_chance_after_reload: int
        unknown_0xd88ecc2f: int
        unknown_0x50b47d78: int
        dodge_chance_after_taunt: int
        unknown_0xd7c5c618: float
        unknown_0x0c7a95ff: float
        char: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct61(BaseProperty):
    patrol: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xCCDD3ACA,
                original_name="Patrol",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    attack: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xFA2A173F,
                original_name="Attack",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x635B60AA, original_name="PART"),
        },
    )
    missile_deflection_radius: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x88FA2ACF, original_name="MissileDeflectionRadius"),
        },
    )
    missile_deflection_rate: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1D159832, original_name="MissileDeflectionRate"),
        },
    )
    unknown_0x8ac503de: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8AC503DE, original_name="Unknown"),
        },
    )
    shot_prediction: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1874F2CB, original_name="ShotPrediction"),
        },
    )
    close_enough_distance: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x24937085, original_name="CloseEnoughDistance"),
        },
    )
    minimum_firing_distance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCA5238BF, original_name="MinimumFiringDistance"),
        },
    )
    maximum_firing_distance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x290F8665, original_name="MaximumFiringDistance"),
        },
    )
    recheck_path_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7626EC89, original_name="RecheckPathDistance"),
        },
    )
    update_path_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4B60951, original_name="UpdatePathTime"),
        },
    )
    unknown_0x271e49b4: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x271E49B4, original_name="Unknown"),
        },
    )
    projectile_left: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x72989547,
                original_name="ProjectileLeft",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    projectile_right: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x53EAC4BA,
                original_name="ProjectileRight",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    reload_delay: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF9DF1262, original_name="ReloadDelay"),
        },
    )
    shot_delay: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3D69D750, original_name="ShotDelay"),
        },
    )
    unknown_0x04d03b18: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x04D03B18, original_name="Unknown"),
        },
    )
    grapple_data: GrappleData = dataclasses.field(
        default_factory=GrappleData,
        metadata={
            "reflection": FieldReflection[GrappleData](
                GrappleData,
                id=0xF609C637,
                original_name="GrappleData",
                from_json=GrappleData.from_json,
                to_json=GrappleData.to_json,
            ),
        },
    )
    dodge_chance_after_fire: int = dataclasses.field(
        default=25,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9AB0A987, original_name="DodgeChanceAfterFire"),
        },
    )
    dodge_chance_after_reload: int = dataclasses.field(
        default=25,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0C14253D, original_name="DodgeChanceAfterReload"),
        },
    )
    unknown_0xd88ecc2f: int = dataclasses.field(
        default=25,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD88ECC2F, original_name="Unknown"),
        },
    )
    unknown_0x50b47d78: int = dataclasses.field(
        default=25,
        metadata={
            "reflection": FieldReflection[int](int, id=0x50B47D78, original_name="Unknown"),
        },
    )
    dodge_chance_after_taunt: int = dataclasses.field(
        default=25,
        metadata={
            "reflection": FieldReflection[int](int, id=0x549B098B, original_name="DodgeChanceAfterTaunt"),
        },
    )
    unknown_0xd7c5c618: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD7C5C618, original_name="Unknown"),
        },
    )
    unknown_0x0c7a95ff: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0C7A95FF, original_name="Unknown"),
        },
    )
    char: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xD83B8302,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
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
        if property_count != 27:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCDD3ACA
        patrol = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFA2A173F
        attack = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x635B60AA
        part = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88FA2ACF
        missile_deflection_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D159832
        missile_deflection_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8AC503DE
        unknown_0x8ac503de = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1874F2CB
        shot_prediction = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24937085
        close_enough_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCA5238BF
        minimum_firing_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x290F8665
        maximum_firing_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626EC89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4B60951
        update_path_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x271E49B4
        unknown_0x271e49b4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72989547
        projectile_left = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53EAC4BA
        projectile_right = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9DF1262
        reload_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D69D750
        shot_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04D03B18
        unknown_0x04d03b18 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF609C637
        grapple_data = GrappleData.from_stream(data, game, property_size, default_override={"grapple_type": 1})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AB0A987
        dodge_chance_after_fire = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C14253D
        dodge_chance_after_reload = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD88ECC2F
        unknown_0xd88ecc2f = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50B47D78
        unknown_0x50b47d78 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x549B098B
        dodge_chance_after_taunt = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD7C5C618
        unknown_0xd7c5c618 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C7A95FF
        unknown_0x0c7a95ff = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD83B8302
        char = AnimationParameters.from_stream(data, game, property_size)

        return cls(
            patrol,
            attack,
            part,
            missile_deflection_radius,
            missile_deflection_rate,
            unknown_0x8ac503de,
            shot_prediction,
            close_enough_distance,
            minimum_firing_distance,
            maximum_firing_distance,
            recheck_path_distance,
            update_path_time,
            unknown_0x271e49b4,
            projectile_left,
            projectile_right,
            reload_delay,
            shot_delay,
            unknown_0x04d03b18,
            grapple_data,
            dodge_chance_after_fire,
            dodge_chance_after_reload,
            unknown_0xd88ecc2f,
            unknown_0x50b47d78,
            dodge_chance_after_taunt,
            unknown_0xd7c5c618,
            unknown_0x0c7a95ff,
            char,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1b")  # 27 properties

        data.write(b"\xcc\xdd:\xca")  # 0xccdd3aca
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patrol.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfa*\x17?")  # 0xfa2a173f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"c[`\xaa")  # 0x635b60aa
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part))

        data.write(b"\x88\xfa*\xcf")  # 0x88fa2acf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.missile_deflection_radius))

        data.write(b"\x1d\x15\x982")  # 0x1d159832
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.missile_deflection_rate))

        data.write(b"\x8a\xc5\x03\xde")  # 0x8ac503de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x8ac503de))

        data.write(b"\x18t\xf2\xcb")  # 0x1874f2cb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shot_prediction))

        data.write(b"$\x93p\x85")  # 0x24937085
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.close_enough_distance))

        data.write(b"\xcaR8\xbf")  # 0xca5238bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.minimum_firing_distance))

        data.write(b")\x0f\x86e")  # 0x290f8665
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maximum_firing_distance))

        data.write(b"v&\xec\x89")  # 0x7626ec89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b"\xf4\xb6\tQ")  # 0xf4b60951
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.update_path_time))

        data.write(b"'\x1eI\xb4")  # 0x271e49b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x271e49b4))

        data.write(b"r\x98\x95G")  # 0x72989547
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"S\xea\xc4\xba")  # 0x53eac4ba
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf9\xdf\x12b")  # 0xf9df1262
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reload_delay))

        data.write(b"=i\xd7P")  # 0x3d69d750
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shot_delay))

        data.write(b"\x04\xd0;\x18")  # 0x4d03b18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x04d03b18))

        data.write(b"\xf6\t\xc67")  # 0xf609c637
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_data.to_stream(data, game, default_override={"grapple_type": 1})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9a\xb0\xa9\x87")  # 0x9ab0a987
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dodge_chance_after_fire))

        data.write(b"\x0c\x14%=")  # 0xc14253d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dodge_chance_after_reload))

        data.write(b"\xd8\x8e\xcc/")  # 0xd88ecc2f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd88ecc2f))

        data.write(b"P\xb4}x")  # 0x50b47d78
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x50b47d78))

        data.write(b"T\x9b\t\x8b")  # 0x549b098b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dodge_chance_after_taunt))

        data.write(b"\xd7\xc5\xc6\x18")  # 0xd7c5c618
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd7c5c618))

        data.write(b"\x0cz\x95\xff")  # 0xc7a95ff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0c7a95ff))

        data.write(b"\xd8;\x83\x02")  # 0xd83b8302
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct61Json", data)
        return cls(
            patrol=FlyerMovementMode.from_json(json_data["patrol"]),
            attack=FlyerMovementMode.from_json(json_data["attack"]),
            part=json_data["part"],
            missile_deflection_radius=json_data["missile_deflection_radius"],
            missile_deflection_rate=json_data["missile_deflection_rate"],
            unknown_0x8ac503de=json_data["unknown_0x8ac503de"],
            shot_prediction=json_data["shot_prediction"],
            close_enough_distance=json_data["close_enough_distance"],
            minimum_firing_distance=json_data["minimum_firing_distance"],
            maximum_firing_distance=json_data["maximum_firing_distance"],
            recheck_path_distance=json_data["recheck_path_distance"],
            update_path_time=json_data["update_path_time"],
            unknown_0x271e49b4=json_data["unknown_0x271e49b4"],
            projectile_left=LaunchProjectileData.from_json(json_data["projectile_left"]),
            projectile_right=LaunchProjectileData.from_json(json_data["projectile_right"]),
            reload_delay=json_data["reload_delay"],
            shot_delay=json_data["shot_delay"],
            unknown_0x04d03b18=json_data["unknown_0x04d03b18"],
            grapple_data=GrappleData.from_json(json_data["grapple_data"]),
            dodge_chance_after_fire=json_data["dodge_chance_after_fire"],
            dodge_chance_after_reload=json_data["dodge_chance_after_reload"],
            unknown_0xd88ecc2f=json_data["unknown_0xd88ecc2f"],
            unknown_0x50b47d78=json_data["unknown_0x50b47d78"],
            dodge_chance_after_taunt=json_data["dodge_chance_after_taunt"],
            unknown_0xd7c5c618=json_data["unknown_0xd7c5c618"],
            unknown_0x0c7a95ff=json_data["unknown_0x0c7a95ff"],
            char=AnimationParameters.from_json(json_data["char"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "patrol": self.patrol.to_json(),
            "attack": self.attack.to_json(),
            "part": self.part,
            "missile_deflection_radius": self.missile_deflection_radius,
            "missile_deflection_rate": self.missile_deflection_rate,
            "unknown_0x8ac503de": self.unknown_0x8ac503de,
            "shot_prediction": self.shot_prediction,
            "close_enough_distance": self.close_enough_distance,
            "minimum_firing_distance": self.minimum_firing_distance,
            "maximum_firing_distance": self.maximum_firing_distance,
            "recheck_path_distance": self.recheck_path_distance,
            "update_path_time": self.update_path_time,
            "unknown_0x271e49b4": self.unknown_0x271e49b4,
            "projectile_left": self.projectile_left.to_json(),
            "projectile_right": self.projectile_right.to_json(),
            "reload_delay": self.reload_delay,
            "shot_delay": self.shot_delay,
            "unknown_0x04d03b18": self.unknown_0x04d03b18,
            "grapple_data": self.grapple_data.to_json(),
            "dodge_chance_after_fire": self.dodge_chance_after_fire,
            "dodge_chance_after_reload": self.dodge_chance_after_reload,
            "unknown_0xd88ecc2f": self.unknown_0xd88ecc2f,
            "unknown_0x50b47d78": self.unknown_0x50b47d78,
            "dodge_chance_after_taunt": self.dodge_chance_after_taunt,
            "unknown_0xd7c5c618": self.unknown_0xd7c5c618,
            "unknown_0x0c7a95ff": self.unknown_0x0c7a95ff,
            "char": self.char.to_json(),
        }


def _decode_patrol(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_attack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_projectile_left(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_projectile_right(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size, default_override={"grapple_type": 1})


def _decode_char(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCCDD3ACA: ("patrol", _decode_patrol),
    0xFA2A173F: ("attack", _decode_attack),
    0x635B60AA: ("part", structs.decode_BIG_Q),
    0x88FA2ACF: ("missile_deflection_radius", structs.decode_BIG_f),
    0x1D159832: ("missile_deflection_rate", structs.decode_BIG_f),
    0x8AC503DE: ("unknown_0x8ac503de", structs.decode_BIG_l),
    0x1874F2CB: ("shot_prediction", structs.decode_BIG_f),
    0x24937085: ("close_enough_distance", structs.decode_BIG_f),
    0xCA5238BF: ("minimum_firing_distance", structs.decode_BIG_f),
    0x290F8665: ("maximum_firing_distance", structs.decode_BIG_f),
    0x7626EC89: ("recheck_path_distance", structs.decode_BIG_f),
    0xF4B60951: ("update_path_time", structs.decode_BIG_f),
    0x271E49B4: ("unknown_0x271e49b4", structs.decode_BIG_f),
    0x72989547: ("projectile_left", _decode_projectile_left),
    0x53EAC4BA: ("projectile_right", _decode_projectile_right),
    0xF9DF1262: ("reload_delay", structs.decode_BIG_f),
    0x3D69D750: ("shot_delay", structs.decode_BIG_f),
    0x04D03B18: ("unknown_0x04d03b18", structs.decode_BIG_f),
    0xF609C637: ("grapple_data", _decode_grapple_data),
    0x9AB0A987: ("dodge_chance_after_fire", structs.decode_BIG_l),
    0x0C14253D: ("dodge_chance_after_reload", structs.decode_BIG_l),
    0xD88ECC2F: ("unknown_0xd88ecc2f", structs.decode_BIG_l),
    0x50B47D78: ("unknown_0x50b47d78", structs.decode_BIG_l),
    0x549B098B: ("dodge_chance_after_taunt", structs.decode_BIG_l),
    0xD7C5C618: ("unknown_0xd7c5c618", structs.decode_BIG_f),
    0x0C7A95FF: ("unknown_0x0c7a95ff", structs.decode_BIG_f),
    0xD83B8302: ("char", _decode_char),
}
