# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct33Json(typing_extensions.TypedDict):
        damage: json_util.JsonObject
        bomb_stun_duration: float
        unknown_0x46aaced3: float
        max_speed: float
        max_wall_speed: float
        ball_pursuit_speed: float
        speed_modifier: float
        turn_speed: float
        blob_effect: int
        hit_normal_damage: int
        hit_heavy_damage: int
        death: int
        sound_idle: int
        sound_move: int
        sound_0xb392943a: int
        sound_0x24ecc1e9: int
        sound_death: int
        unknown_0x7569fdba: float
        unknown_0xd55938d2: float
        vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct33(BaseProperty):
    damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x337F9524,
                original_name="Damage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    bomb_stun_duration: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5860E24B, original_name="BombStunDuration"),
        },
    )
    unknown_0x46aaced3: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x46AACED3, original_name="Unknown"),
        },
    )
    max_speed: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x82DB0CBE, original_name="MaxSpeed"),
        },
    )
    max_wall_speed: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBEC652AE, original_name="MaxWallSpeed"),
        },
    )
    ball_pursuit_speed: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x600A863F, original_name="BallPursuitSpeed"),
        },
    )
    speed_modifier: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x388E4902, original_name="SpeedModifier"),
        },
    )
    turn_speed: float = dataclasses.field(
        default=360.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x020C78BB, original_name="TurnSpeed"),
        },
    )
    blob_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2367F689, original_name="BlobEffect"),
        },
    )
    hit_normal_damage: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD473158D, original_name="HitNormalDamage"),
        },
    )
    hit_heavy_damage: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCCA298B4, original_name="HitHeavyDamage"),
        },
    )
    death: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB99C80D3, original_name="Death"),
        },
    )
    sound_idle: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xAF38968E, original_name="Sound_Idle"),
        },
    )
    sound_move: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x6C101854, original_name="Sound_Move"),
        },
    )
    sound_0xb392943a: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xB392943A, original_name="Sound"),
        },
    )
    sound_0x24ecc1e9: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x24ECC1E9, original_name="Sound"),
        },
    )
    sound_death: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE160B593, original_name="Sound_Death"),
        },
    )
    unknown_0x7569fdba: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7569FDBA, original_name="Unknown"),
        },
    )
    unknown_0xd55938d2: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD55938D2, original_name="Unknown"),
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
        if property_count != 20:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 4.5, "di_knock_back_power": 4.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5860E24B
        bomb_stun_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46AACED3
        unknown_0x46aaced3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82DB0CBE
        max_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBEC652AE
        max_wall_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x600A863F
        ball_pursuit_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388E4902
        speed_modifier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x020C78BB
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2367F689
        blob_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD473158D
        hit_normal_damage = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCA298B4
        hit_heavy_damage = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB99C80D3
        death = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF38968E
        sound_idle = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C101854
        sound_move = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB392943A
        sound_0xb392943a = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24ECC1E9
        sound_0x24ecc1e9 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE160B593
        sound_death = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7569FDBA
        unknown_0x7569fdba = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD55938D2
        unknown_0xd55938d2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            damage,
            bomb_stun_duration,
            unknown_0x46aaced3,
            max_speed,
            max_wall_speed,
            ball_pursuit_speed,
            speed_modifier,
            turn_speed,
            blob_effect,
            hit_normal_damage,
            hit_heavy_damage,
            death,
            sound_idle,
            sound_move,
            sound_0xb392943a,
            sound_0x24ecc1e9,
            sound_death,
            unknown_0x7569fdba,
            unknown_0xd55938d2,
            vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x14")  # 20 properties

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(
            data,
            game,
            default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 4.5, "di_knock_back_power": 4.0},
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X`\xe2K")  # 0x5860e24b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bomb_stun_duration))

        data.write(b"F\xaa\xce\xd3")  # 0x46aaced3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x46aaced3))

        data.write(b"\x82\xdb\x0c\xbe")  # 0x82db0cbe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_speed))

        data.write(b"\xbe\xc6R\xae")  # 0xbec652ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_wall_speed))

        data.write(b"`\n\x86?")  # 0x600a863f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_pursuit_speed))

        data.write(b"8\x8eI\x02")  # 0x388e4902
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.speed_modifier))

        data.write(b"\x02\x0cx\xbb")  # 0x20c78bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_speed))

        data.write(b"#g\xf6\x89")  # 0x2367f689
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.blob_effect))

        data.write(b"\xd4s\x15\x8d")  # 0xd473158d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.hit_normal_damage))

        data.write(b"\xcc\xa2\x98\xb4")  # 0xcca298b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.hit_heavy_damage))

        data.write(b"\xb9\x9c\x80\xd3")  # 0xb99c80d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.death))

        data.write(b"\xaf8\x96\x8e")  # 0xaf38968e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_idle))

        data.write(b"l\x10\x18T")  # 0x6c101854
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_move))

        data.write(b"\xb3\x92\x94:")  # 0xb392943a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0xb392943a))

        data.write(b"$\xec\xc1\xe9")  # 0x24ecc1e9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0x24ecc1e9))

        data.write(b"\xe1`\xb5\x93")  # 0xe160b593
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_death))

        data.write(b"ui\xfd\xba")  # 0x7569fdba
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7569fdba))

        data.write(b"\xd5Y8\xd2")  # 0xd55938d2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd55938d2))

        data.write(b"{q\xae\x90")  # 0x7b71ae90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct33Json", data)
        return cls(
            damage=DamageInfo.from_json(json_data["damage"]),
            bomb_stun_duration=json_data["bomb_stun_duration"],
            unknown_0x46aaced3=json_data["unknown_0x46aaced3"],
            max_speed=json_data["max_speed"],
            max_wall_speed=json_data["max_wall_speed"],
            ball_pursuit_speed=json_data["ball_pursuit_speed"],
            speed_modifier=json_data["speed_modifier"],
            turn_speed=json_data["turn_speed"],
            blob_effect=json_data["blob_effect"],
            hit_normal_damage=json_data["hit_normal_damage"],
            hit_heavy_damage=json_data["hit_heavy_damage"],
            death=json_data["death"],
            sound_idle=json_data["sound_idle"],
            sound_move=json_data["sound_move"],
            sound_0xb392943a=json_data["sound_0xb392943a"],
            sound_0x24ecc1e9=json_data["sound_0x24ecc1e9"],
            sound_death=json_data["sound_death"],
            unknown_0x7569fdba=json_data["unknown_0x7569fdba"],
            unknown_0xd55938d2=json_data["unknown_0xd55938d2"],
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "damage": self.damage.to_json(),
            "bomb_stun_duration": self.bomb_stun_duration,
            "unknown_0x46aaced3": self.unknown_0x46aaced3,
            "max_speed": self.max_speed,
            "max_wall_speed": self.max_wall_speed,
            "ball_pursuit_speed": self.ball_pursuit_speed,
            "speed_modifier": self.speed_modifier,
            "turn_speed": self.turn_speed,
            "blob_effect": self.blob_effect,
            "hit_normal_damage": self.hit_normal_damage,
            "hit_heavy_damage": self.hit_heavy_damage,
            "death": self.death,
            "sound_idle": self.sound_idle,
            "sound_move": self.sound_move,
            "sound_0xb392943a": self.sound_0xb392943a,
            "sound_0x24ecc1e9": self.sound_0x24ecc1e9,
            "sound_death": self.sound_death,
            "unknown_0x7569fdba": self.unknown_0x7569fdba,
            "unknown_0xd55938d2": self.unknown_0xd55938d2,
            "vulnerability": self.vulnerability.to_json(),
        }

    def _dependencies_for_blob_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.blob_effect)

    def _dependencies_for_hit_normal_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hit_normal_damage)

    def _dependencies_for_hit_heavy_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hit_heavy_damage)

    def _dependencies_for_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death)

    def _dependencies_for_sound_idle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_idle)

    def _dependencies_for_sound_move(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_move)

    def _dependencies_for_sound_0xb392943a(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0xb392943a)

    def _dependencies_for_sound_0x24ecc1e9(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0x24ecc1e9)

    def _dependencies_for_sound_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_death)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_blob_effect, "blob_effect", "AssetId"),
            (self._dependencies_for_hit_normal_damage, "hit_normal_damage", "AssetId"),
            (self._dependencies_for_hit_heavy_damage, "hit_heavy_damage", "AssetId"),
            (self._dependencies_for_death, "death", "AssetId"),
            (self._dependencies_for_sound_idle, "sound_idle", "int"),
            (self._dependencies_for_sound_move, "sound_move", "int"),
            (self._dependencies_for_sound_0xb392943a, "sound_0xb392943a", "int"),
            (self._dependencies_for_sound_0x24ecc1e9, "sound_0x24ecc1e9", "int"),
            (self._dependencies_for_sound_death, "sound_death", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct33.{field_name} ({field_type}): {e}")


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 4.5, "di_knock_back_power": 4.0},
    )


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x337F9524: ("damage", _decode_damage),
    0x5860E24B: ("bomb_stun_duration", structs.decode_BIG_f),
    0x46AACED3: ("unknown_0x46aaced3", structs.decode_BIG_f),
    0x82DB0CBE: ("max_speed", structs.decode_BIG_f),
    0xBEC652AE: ("max_wall_speed", structs.decode_BIG_f),
    0x600A863F: ("ball_pursuit_speed", structs.decode_BIG_f),
    0x388E4902: ("speed_modifier", structs.decode_BIG_f),
    0x020C78BB: ("turn_speed", structs.decode_BIG_f),
    0x2367F689: ("blob_effect", structs.decode_BIG_L),
    0xD473158D: ("hit_normal_damage", structs.decode_BIG_L),
    0xCCA298B4: ("hit_heavy_damage", structs.decode_BIG_L),
    0xB99C80D3: ("death", structs.decode_BIG_L),
    0xAF38968E: ("sound_idle", structs.decode_BIG_l),
    0x6C101854: ("sound_move", structs.decode_BIG_l),
    0xB392943A: ("sound_0xb392943a", structs.decode_BIG_l),
    0x24ECC1E9: ("sound_0x24ecc1e9", structs.decode_BIG_l),
    0xE160B593: ("sound_death", structs.decode_BIG_l),
    0x7569FDBA: ("unknown_0x7569fdba", structs.decode_BIG_f),
    0xD55938D2: ("unknown_0xd55938d2", structs.decode_BIG_f),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
}
