from __future__ import annotations
import typing

from construct import Construct, Container

from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.dependencies import MlvlDependencies

AssetType = str
AssetId = int
NameOrAssetId = typing.Union[str, AssetId]


class Dependency(typing.NamedTuple):
    type: AssetType
    id: AssetId


class BaseResource:
    _raw: Container
    target_game: Game
    asset_manager: AssetManager

    def __init__(self, raw: Container, target_game: Game, asset_manager: typing.Optional[AssetManager] = None):
        self._raw = raw
        self.target_game = target_game
        self.asset_manager = asset_manager

    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        raise NotImplementedError()

    @classmethod
    def resource_type(cls) -> AssetType:
        raise NotImplementedError()

    @classmethod
    def parse(cls, data: bytes, target_game: Game, asset_manager: typing.Optional[AssetManager] = None) -> "BaseResource":
        if asset_manager is not None:
            print(asset_manager)
        return cls(cls.construct_class(target_game).parse(data, target_game=target_game),
                   target_game, asset_manager)

    def build(self) -> bytes:
        return self.construct_class(self.target_game).build(self._raw, target_game=self.target_game)

    @classmethod
    def has_dependencies(cls, target_game: Game = None) -> bool:
        test = cls(Container(), target_game)
        try:
            deps = list(test.dependencies_for())
        except:
            return True
        return bool(deps)

    def dependencies_for(self) -> typing.Iterator[AssetId]:
        raise NotImplementedError()
    
    def mlvl_dependencies_for(self, dep_manager: MlvlDependencies) -> typing.Iterator[AssetId]:
        yield from self.dependencies_for()
    
    @staticmethod
    def dependencies_to_asset_ids(dependencies: typing.Iterable[Dependency]) -> typing.Iterator[AssetId]:
        for _, asset_id in dependencies:
            yield asset_id

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
