import logging
import time
from pathlib import Path
from unittest.mock import MagicMock

from retro_data_structures.asset_manager import AssetManager, PathFileProvider
from retro_data_structures.base_resource import Dependency
from retro_data_structures.game_check import Game


def test_rebuild_paks(prime2_asset_manager: AssetManager, mocker):
    manager = prime2_asset_manager
    mock_get_modified_paks: MagicMock = mocker.patch(
        "retro_data_structures.asset_manager.AssetManager._get_modified_paks",
        autospec=True
    )
    paks = [
        pak for pak in manager.all_paks
        # if not pak.startswith("Metroid")
    ]
    # paks = ["GGuiSys.pak"]
    mock_get_modified_paks.return_value = set(paks)

    out_path = Path(__file__).parent.joinpath("test_files", "pak_output")
    # prime2_asset_manager.provider.extract_to_directory(out_path)

    start_time = time.time()
    manager.save_modifications(out_path)

    logging.info("Total time: %fs", time.time() - start_time)

    new_manager = AssetManager(PathFileProvider(out_path), Game.ECHOES)

#     if nod.DiscBuilderGCN.calculate_total_size_required(out_path) is None:
#         raise Exception("Image built with given directory would pass the maximum size.")

#     def fprogress_callback(progress: float, name: str, bytes: int):
#         print("\r" + " " * 100, end="")
#         print(f"\r{progress:.0%} {name} {bytes} B", flush=True)

#     logging.info("hi")
#     disc_builder = nod.DiscBuilderGCN(out_path.parent.joinpath("game.iso"), fprogress_callback)
#     logging.info("bye")
#     try:
#         disc_builder.build_from_directory(out_path)
#     except RuntimeError as e:
#         raise Exception(f"Failure building the image: {e}")

# if __name__ == "__main__":
#     test_rebuild_paks(None, None)
    old_paks = {}
    new_paks = {}
    for pak in paks:
        logging.info("Comparing %s", pak)
        old_pak = manager.get_pak(pak)
        new_pak = new_manager.get_pak(pak)

        old_paks[pak] = {Dependency(f.asset_type, f.asset_id) for f in old_pak._raw.files}
        new_paks[pak] = {Dependency(f.asset_type, f.asset_id) for f in new_pak._raw.files}

    for f in out_path.rglob("*.*"):
        f.unlink()

    missing = {
        pak: old_paks[pak].difference(new_paks[pak])
        for pak in paks
    }
    extra = {
        pak: new_paks[pak].difference(old_paks[pak])
        for pak in paks
    }
    missing = {n: miss for n, miss in missing.items() if miss}
    extra = {n: ext for n, ext in extra.items() if ext}
    assert missing == {}
    assert extra == {}
    # assert accuracy == {pak: True for pak in paks}
    assert old_paks == new_paks

