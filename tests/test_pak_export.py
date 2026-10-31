from __future__ import annotations

import collections
import difflib
import math
import struct
from typing import TYPE_CHECKING

from retro_data_structures import pak_compression, pak_layout
from retro_data_structures.asset_manager import (
    AssetManager,
    MemoryFileWriter,
    PakExportStrategy,
    PakExportStrategyAppend,
    PakExportStrategyCreate,
)
from retro_data_structures.formats.mlvl import Mlvl
from retro_data_structures.formats.pak import Pak
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures.base_resource import AssetId
    from retro_data_structures.file_provider import FileProvider
    from retro_data_structures.formats.pak_common import PakFile

# Bits per pixel of each GX texture format
_TXTR_BITS_PER_PIXEL = {
    0x0: 4,  # I4
    0x1: 8,  # I8
    0x2: 8,  # IA4
    0x3: 16,  # IA8
    0x4: 4,  # C4
    0x5: 8,  # C8
    0x6: 16,  # C14X2
    0x7: 16,  # RGB565
    0x8: 16,  # RGB5A3
    0x9: 32,  # RGBA8
    0xA: 4,  # CMPR
}


_TXTR_TILE_SIZE = {
    0x0: (8, 8),
    0x1: (8, 4),
    0x2: (8, 4),
    0x3: (4, 4),
    0x4: (8, 8),
    0x5: (8, 4),
    0x6: (4, 4),
    0x7: (4, 4),
    0x8: (4, 4),
    0x9: (4, 4),
    0xA: (8, 8),
}


def _txtr_size(data: bytes) -> int:
    image_format, width, height, mipmap_count = struct.unpack_from(">LHHL", data)
    size = 12
    if image_format in {0x4, 0x5, 0x6}:
        _, palette_width, palette_height = struct.unpack_from(">LHH", data, size)
        size += 8 + palette_width * palette_height * 2

    tile_width, tile_height = _TXTR_TILE_SIZE[image_format]
    for mip in range(mipmap_count):
        if mip == 0:
            mip_width = math.ceil(width / tile_width) * tile_width
            mip_height = math.ceil(height / tile_height) * tile_height
        else:
            mip_width, mip_height = width, height
        size += max(32, mip_width * mip_height * _TXTR_BITS_PER_PIXEL[image_format] // 8)
        width = max(width // 2, 1)
        height = max(height // 2, 1)
    return size


def _uncompressed_data(game: Game, file: PakFile) -> bytes:
    """
    The uncompressed data of the given pak entry. When the entry isn't compressed, the data has the padding
    of the pak, so remove it when it's possible to know the real size.
    """
    data = file.get_decompressed(game)
    if file.should_compress:
        return data
    if file.asset_type == "TXTR":
        return data[: _txtr_size(data)]
    if file.asset_type in pak_compression.EFFECT_TYPES:
        # Effects are text that end with _END
        return data.rstrip(b"\xff")
    return data


def _vanilla_files(manager: AssetManager) -> Iterator[tuple[str, PakFile]]:
    for pak_name in manager.all_paks:
        pak = manager.pak_group.get_pak(pak_name)
        for file in pak._raw.files:
            yield pak_name, file
        manager.pak_group.release_in_memory_paks()


def _compression_mismatches(manager: AssetManager) -> dict[tuple[str, AssetId], PakFile]:
    game = manager.target_game
    result = {}
    for pak_name, file in _vanilla_files(manager):
        if file.asset_type not in pak_compression.COMPRESSIBLE_TYPES:
            assert not file.should_compress
            continue

        if pak_compression.should_compress(game, file.asset_type, _uncompressed_data(game, file)) != bool(
            file.should_compress
        ):
            result[(pak_name, file.asset_id)] = file
    return result


def test_txtr_size(prime2_asset_manager: AssetManager) -> None:
    # The size calculation must be right for every texture we know the size of
    game = prime2_asset_manager.target_game
    checked = 0
    for _, file in _vanilla_files(prime2_asset_manager):
        if file.asset_type == "TXTR" and file.should_compress:
            assert _txtr_size(file.get_decompressed(game)) == len(file.get_decompressed(game))
            checked += 1
    assert checked > 5000


def test_compression_rules_prime(prime1_asset_manager: AssetManager) -> None:
    mismatches = _compression_mismatches(prime1_asset_manager)

    # The only exception: the suit models at the start of NoARAM.pak and their textures
    layout = prime1_asset_manager.get_pak_layout_builder().pak_layout(
        "NoARAM.pak",
        prime1_asset_manager.pak_group.get_named_resources_of_pak("NoARAM.pak").items(),
        lambda mlvl, mrea: False,
    )
    assert set(mismatches) == {("NoARAM.pak", asset_id) for asset_id in layout.uncompressed}
    assert len(mismatches) == 115


def test_compression_rules_echoes(prime2_asset_manager: AssetManager) -> None:
    mismatches = _compression_mismatches(prime2_asset_manager)

    # Vanilla resources that don't follow the rule. Exporting keeps their original flag.
    by_asset = {asset_id: (file.asset_type, file.should_compress) for (_, asset_id), file in mismatches.items()}
    counts = collections.Counter(by_asset.values())
    assert counts == {
        # Uncompressed in vanilla, but smaller when compressed
        ("TXTR", False): 103,
        ("ANIM", False): 58,
        ("CRSC", False): 15,
        # Compressed in vanilla, but lzokay makes them 1 or 2 bytes bigger
        ("TXTR", True): 3,
    }


def _layout_score(vanilla: list[AssetId], ours: list[AssetId]) -> float:
    matcher = difflib.SequenceMatcher(None, vanilla, ours, autojunk=False)
    return sum(block.size for block in matcher.get_matching_blocks()) / len(vanilla)


def _create_factory(manager: AssetManager, pak_name: str) -> PakExportStrategy:
    return PakExportStrategyCreate(manager, pak_name)


def _export_and_compare(
    provider: FileProvider, game: Game, pak_name: str, min_score: float
) -> tuple[list[AssetId], list[AssetId]]:
    manager = AssetManager(provider, game, pak_strategy_factory=_create_factory, ignore_low_paks=False)
    manager._pak_strategy = {pak_name: manager._pak_strategy[pak_name]}

    writer = MemoryFileWriter()
    manager._export_paks(writer, lambda message, progress: None)

    original = manager.pak_group.get_pak(pak_name)
    created = Pak.parse(writer.get_data(pak_name), target_game=game)

    vanilla_ids = [file.asset_id for file in original._raw.files]
    created_ids = [file.asset_id for file in created._raw.files]

    assert created._raw.named_resources == original._raw.named_resources
    assert set(created_ids) == set(vanilla_ids)
    assert _layout_score(vanilla_ids, created_ids) >= min_score

    for file in created._raw.files:
        vanilla = original.get_pak_file_with_id(file.asset_id)
        assert file.should_compress == vanilla.should_compress
        assert file.get_decompressed(game) == vanilla.get_decompressed(game)

    return vanilla_ids, created_ids


def test_create_prime_noaram(prime1_iso_provider: FileProvider) -> None:
    vanilla_ids, created_ids = _export_and_compare(prime1_iso_provider, Game.PRIME, "NoARAM.pak", 1.0)
    assert created_ids == vanilla_ids


def test_create_prime_gguisys(prime1_iso_provider: FileProvider) -> None:
    # Mostly FRMEs, which have no dependency list
    vanilla_ids, created_ids = _export_and_compare(prime1_iso_provider, Game.PRIME, "GGuiSys.pak", 1.0)
    assert created_ids == vanilla_ids


def test_create_prime_world(prime1_iso_provider: FileProvider) -> None:
    _export_and_compare(prime1_iso_provider, Game.PRIME, "Metroid7.pak", 0.97)


def test_create_echoes_logbook(prime2_iso_provider: FileProvider) -> None:
    _export_and_compare(prime2_iso_provider, Game.ECHOES, "LogBook.pak", 0.97)


def test_create_echoes_world(prime2_iso_provider: FileProvider) -> None:
    vanilla_ids, created_ids = _export_and_compare(prime2_iso_provider, Game.ECHOES, "Metroid6.pak", 1.0)
    assert created_ids == vanilla_ids


def test_create_echoes_modified_area(prime2_iso_provider: FileProvider) -> None:
    pak_name = "Metroid6.pak"

    def factory(manager: AssetManager, name: str) -> PakExportStrategy:
        if name == pak_name:
            return PakExportStrategyCreate(manager, name)
        return PakExportStrategyAppend(manager, name)

    manager = AssetManager(prime2_iso_provider, Game.ECHOES, pak_strategy_factory=factory, ignore_low_paks=False)

    # A model that this pak doesn't have
    model_id = next(
        asset_id
        for asset_type, asset_id in manager.pak_group.get_resources_of_pak("Metroid3.pak")
        if asset_type == "CMDL" and not manager.pak_group.does_pak_contains_id(pak_name, asset_id)
    )

    mlvl_id = manager.pak_group.get_named_resources_of_pak(pak_name)["M04_Pipeline"]
    mlvl = manager.get_file(mlvl_id, type_hint=Mlvl)
    area = next(iter(mlvl.areas))

    from retro_data_structures.properties.echoes.objects.Actor import Actor

    area.get_layer("Default").add_instance_with(Actor(model=model_id))
    area.build_mlvl_dependencies(only_modified=True)
    mrea_id = area.mrea_asset_id
    textures = [dep.id for dep in manager.get_dependencies_for_asset(model_id) if dep.type == "TXTR"]
    assert textures

    manager.build_modified_files()
    writer = MemoryFileWriter()
    manager.save_modifications(writer)

    created = Pak.parse(writer.get_data(pak_name), target_game=Game.ECHOES)
    ids = [file.asset_id for file in created._raw.files]

    # The model and its textures are in the area, before its MREA
    area_end = ids.index(mrea_id)
    assert model_id in ids[:area_end]
    for texture in textures:
        assert texture in ids[: ids.index(model_id)]

    # And the MREA is the modified one
    original_mrea = manager.pak_group.get_pak(pak_name).get_pak_file_with_id(mrea_id)
    created_mrea = created.get_pak_file_with_id(mrea_id)
    assert created_mrea.get_decompressed(Game.ECHOES) != original_mrea.get_decompressed(Game.ECHOES)


def test_prime_areas_with_unknown_object_order(prime1_asset_manager: AssetManager) -> None:
    # Checks how `_PRIME_AREAS_WITH_UNKNOWN_OBJECT_ORDER` was found, for one world pak
    manager = prime1_asset_manager
    pak_name = "Metroid1.pak"

    vanilla_areas: dict[AssetId, dict[AssetId, int]] = {}
    position: dict[AssetId, int] = {}
    for file in manager.pak_group.get_pak(pak_name)._raw.files:
        position.setdefault(file.asset_id, len(position))
        if file.asset_type == "MREA":
            vanilla_areas[file.asset_id] = position
            position = {}

    off_order = set()
    layers_off_order = []

    class Builder(pak_layout.PakLayoutBuilder):
        def _merge_layers(self, area, ids_per_layer, segments):  # type: ignore[no-untyped-def]
            merged = super()._merge_layers(area, ids_per_layer, segments)
            vanilla = vanilla_areas[area.mrea_asset_id]

            # Where vanilla has the first resource that only this object needs, not counting textures
            first_object = {}
            for key in merged:
                for asset_id in segments[key]:
                    first_object.setdefault(asset_id, key)
            object_position = {}
            for key in merged:
                positions = [
                    vanilla[asset_id]
                    for asset_id in segments[key]
                    if first_object[asset_id] == key
                    and asset_id in vanilla
                    and manager.get_asset_type(asset_id) != "TXTR"
                ]
                if positions:
                    object_position[key] = min(positions)

            placed = [key for key in merged if key in object_position]
            vanilla_order = sorted(placed, key=object_position.__getitem__)
            if vanilla_order != placed:
                off_order.add(area.mrea_asset_id)
            for layer_index in range(len(ids_per_layer)):
                layer = [object_index for li, object_index in vanilla_order if li == layer_index]
                if layer != sorted(layer):
                    layers_off_order.append(area.mrea_asset_id)
            return merged

    pak_layout_builder = Builder(manager)
    pak_layout_builder.pak_layout(
        pak_name,
        manager.pak_group.get_named_resources_of_pak(pak_name).items(),
        lambda mlvl, mrea: False,
    )

    assert len(vanilla_areas) == 28
    assert off_order == pak_layout._PRIME_AREAS_WITH_UNKNOWN_OBJECT_ORDER & vanilla_areas.keys()
    assert len(off_order) == 3

    # Vanilla keeps the order inside each layer, only the layers are interleaved differently.
    # Except for one layer, in one of these areas.
    assert len(layers_off_order) == 1
    assert set(layers_off_order) <= off_order
