from __future__ import annotations

import os
from typing import TYPE_CHECKING

import nod

from retro_data_structures.asset_manager import IsoFileProvider, PathFileProvider

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
