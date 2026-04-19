from __future__ import annotations

import os
from typing import TYPE_CHECKING

import nod

from retro_data_structures.asset_manager import AssetManager, IsoFileProvider, PathFileProvider
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from pathlib import Path


def extract_iso(iso: Path, out: Path) -> None:
    context = nod.ExtractionContext()
    disc, is_wii = nod.open_disc_from_image(iso)
    data_partition = disc.get_data_partition()
    data_partition.extract_to_directory(os.fspath(out), context)


def test_identical_provider_prime2(prime2_iso: Path, tmp_path: Path) -> None:
    extract_path = tmp_path.joinpath("extract")
    extract_iso(prime2_iso, extract_path)

    iso_provider = IsoFileProvider(prime2_iso)
    path_provider = PathFileProvider(extract_path)

    assert sorted(iso_provider.rglob("*")) == sorted(path_provider.rglob("*"))


def test_get_custom_name(prime2_iso_provider):
    asset_manager = AssetManager(prime2_iso_provider, target_game=Game.ECHOES)

    assert asset_manager.get_custom_asset("MyFancyAsset") is None
    assert asset_manager.get_custom_name_for(0xFFFF0000) is None

    asset_manager.register_custom_asset_name("MyFancyAsset", 0xFFFF0000)

    assert asset_manager.get_custom_asset("MyFancyAsset") == 0xFFFF0000
    assert asset_manager.get_custom_name_for(0xFFFF0000) == "MyFancyAsset"

    assert asset_manager.get_custom_asset("MyUglyAsset") is None
    assert asset_manager.get_custom_name_for(0xFFFFF000) is None
