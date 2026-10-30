from __future__ import annotations

import dataclasses
import struct
import typing

from retro_data_structures.properties.base_property import BaseProperty

if typing.TYPE_CHECKING:
    import typing_extensions

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

INVALID_ASSET_32 = 0xFFFFFFFF
INVALID_ASSET_64 = 0xFFFFFFFFFFFFFFFF


@dataclasses.dataclass()
class AnimationParameters(BaseProperty):
    """
    An ANCS asset, the index of a character in it and the initial animation. It's stored as an asset id (32 bits in
    Prime and Echoes, 64 in Corruption) and two u32. Corruption only has the asset and the character index, so
    `initial_anim` is not stored there.

    The class has no game, so `ancs` defaults to the 32-bit invalid id. It's written as the invalid id of the game.
    """

    ancs: int = dataclasses.field(default=INVALID_ASSET_32, metadata={"asset_types": ["ANCS"]})
    character_index: int = 0
    initial_anim: int = 0

    def __post_init__(self) -> None:
        # The class has no game, so every invalid id is the 32-bit one. It's written as the invalid id of the game.
        if self.ancs == INVALID_ASSET_64:
            self.ancs = INVALID_ASSET_32

    @staticmethod
    def encode_ancs(ancs: int, game: Game) -> int:
        """Replace the invalid asset id of the other asset id width with the invalid asset id of the game."""
        if ancs in (INVALID_ASSET_32, INVALID_ASSET_64):
            return game.invalid_asset_id  # type: ignore[return-value]
        return ancs

    @classmethod
    def _format(cls, game: Game) -> str:
        return game.struct_endianness + ("LLL" if game.uses_asset_id_32 else "QL")

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        fmt = cls._format(game)
        return cls(*struct.unpack(fmt, data.read(struct.calcsize(fmt))))

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        values = (self.encode_ancs(self.ancs, game), self.character_index, self.initial_anim)
        data.write(struct.pack(self._format(game), *values[: 3 if game.uses_asset_id_32 else 2]))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        data_json = typing.cast("dict[str, int]", data)
        return cls(data_json["ancs"], data_json["character_index"], data_json["initial_anim"])

    def to_json(self) -> json_util.JsonObject:
        return {
            "ancs": self.ancs,
            "character_index": self.character_index,
            "initial_anim": self.initial_anim,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> typing.Iterator[Dependency]:
        yield from asset_manager.get_dependencies_for_ancs(self.ancs, self.character_index)
