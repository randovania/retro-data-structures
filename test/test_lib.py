import dataclasses
import json
from pathlib import Path
from typing import Tuple, Type, List
import construct

from construct.lib.containers import Container

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.base_resource import AssetId, AssetType, BaseResource, RawResource
from retro_data_structures.game_check import Game


@dataclasses.dataclass(frozen=True)
class TypedAsset:
    id: AssetId
    type: AssetType


def _parse_assets_file(name: str) -> List[TypedAsset]:
    with Path(__file__).parent.joinpath("test_files", name).open() as f:
        data = json.load(f)

    return [
        TypedAsset(item["id"], item["type"])
        for item in data
    ]


PRIME_ASSET_IDS = _parse_assets_file("assets_prime.json")
ECHOES_ASSET_IDS = _parse_assets_file("assets_echoes.json")


def _parse_and_build_compare(module, game: Game, file_path: Path, print_data=False, save_file=None):
    raw = file_path.read_bytes()
    construct.lib.setGlobalPrintFullStrings(True)

    data: Container = module.parse(raw, target_game=game)
    if print_data:
        print(data)
    encoded = module.build(data, target_game=game)

    if save_file:
        file_path.with_stem(file_path.stem+"_COPY").write_bytes(encoded)
        file_path.with_suffix(file_path.suffix+".construct").write_text(str(data))
        
    construct.lib.setGlobalPrintFullStrings(False)
    return (raw, encoded, data)


def parse_and_build_compare(module, game: Game, file_path: Path, print_data=False, save_file=None):
    raw, encoded, _ = _parse_and_build_compare(module, game, file_path, print_data, save_file)
    assert encoded == raw


def parse_and_build_compare_parsed(module, game: Game, file_path: Path, print_data=False, save_file=None):
    _, encoded, data = _parse_and_build_compare(module, game, file_path, print_data, save_file)

    data2 = module.parse(encoded, target_game=game)
    if print_data:
        print(data2)

    assert purge_hidden(data) == purge_hidden(data2)


def purge_hidden(data: Container) -> Container:
    data = {k: v for k, v in data.items() if not k.startswith("_")}
    return {k: purge_hidden(v) if isinstance(v, Container) else v for k, v in data.items()}


def parse_and_build_compare_from_manager(
        asset_manager: AssetManager, asset_id: AssetId, resource_class: Type[BaseResource],
        print_data=False) -> Tuple[RawResource, BaseResource, bytes]:
    resource = asset_manager.get_raw_asset(asset_id)
    assert resource.type == resource_class.resource_type()

    decoded = resource_class.parse(resource.data, target_game=asset_manager.target_game)
    if print_data:
        print(decoded)

    encoded = decoded.build()
    decoded2 = resource_class.parse(encoded, target_game=asset_manager.target_game)

    assert purge_hidden(decoded2.raw) == purge_hidden(decoded.raw)

    return resource, decoded, encoded
