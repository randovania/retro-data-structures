import typing

from construct import Construct, Container

from retro_data_structures.game_check import Game

AssetType = str
AssetId = int
NameOrAssetId = typing.Union[str, AssetId]


class BaseResource:
    _raw: Container
    target_game: Game

    def __init__(self, raw: Container, target_game: Game):
        self._raw = raw
        self.target_game = target_game

    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        raise NotImplementedError()

    @classmethod
    def resource_type(cls) -> AssetType:
        raise NotImplementedError()

    @classmethod
    def parse(cls, data: bytes, target_game: Game) -> "BaseResource":
        return cls(cls.construct_class(target_game).parse(data, target_game=target_game),
                   target_game)

    def build(self) -> bytes:
        return self.construct_class(self.target_game).build(self._raw, target_game=self.target_game)

    @property
    def raw(self) -> Container:
        return self._raw


def resolve_asset_id(game: Game, value: NameOrAssetId) -> AssetId:
    if isinstance(value, str):
        return game.hash_asset_id(value)
    return value


class RawResource(typing.NamedTuple):
    type: AssetType
    data: bytes
