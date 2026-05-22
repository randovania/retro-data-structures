from __future__ import annotations

import os
from typing import TYPE_CHECKING

import nod

from retro_data_structures.asset_manager import (
    AssetManager,
    MemoryFileWriter,
    PakExportStrategy,
    PakExportStrategyAppend,
    PakExportStrategyCreate,
)
from retro_data_structures.file_provider import IsoFileProvider, PathFileProvider
from retro_data_structures.formats import Pak
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


def _pak_strategy_factory(manager: AssetManager, pak_name: str) -> PakExportStrategy:
    if pak_name == "LogBook.pak":
        return PakExportStrategyCreate(manager, pak_name)
    else:
        return PakExportStrategyAppend(manager, pak_name)


def test_strategy_create(prime2_iso_provider, tmp_path):
    asset_manager = AssetManager(
        prime2_iso_provider,
        target_game=Game.ECHOES,
        pak_strategy_factory=_pak_strategy_factory,
    )

    writer = MemoryFileWriter()
    asset_manager._pak_strategy["LogBook.pak"].export(writer)

    pak = Pak.parse(writer.get_data("LogBook.pak"), target_game=asset_manager.target_game)
    file_count = len(pak._raw.files)
    assert file_count == 1995
