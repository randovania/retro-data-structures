"""Orchestrates parsing, merging and writing."""

from __future__ import annotations

import logging
import shutil
import typing
from pathlib import Path
from xml.etree import ElementTree

from pwe_generator.emit import (
    HEADER,
    collect_modules,
    enum_file,
    module_source,
    object_tables_source,
    resolve_names,
)
from pwe_generator.merge import merge
from pwe_generator.model import GAME_IDS
from pwe_generator.parse import GameParser, find_assured, read_property_names
from pwe_generator.report import build_report

if typing.TYPE_CHECKING:
    from pwe_generator.model import GameData
    from retro_data_structures.game_check import Game

# Files and directories of the generator before the classes were merged
OLD_GENERATED = [
    "properties/prime",
    "properties/echoes",
    "properties/corruption",
    "properties/common",
    "properties/shared_archetypes.py",
    "properties/shared_objects.py",
    "properties/structs.py",
    "enums/prime.py",
    "enums/echoes.py",
    "enums/corruption.py",
    "enums/shared_enums.py",
]


def parse_game_list(templates_path: Path) -> dict[str, Path]:
    root = ElementTree.parse(templates_path / "GameList.xml").getroot()
    return {
        game.attrib["ID"]: Path(template.text)
        for game in root
        if (template := find_assured(game, "GameTemplate")).text is not None
    }


def generate(rds_root: Path, templates_path: Path, report_path: Path | None = None) -> None:
    logging.info("Parsing the templates")
    names = read_property_names(templates_path / "PropertyMap.xml")
    game_list = parse_game_list(templates_path)
    games: dict[Game, GameData] = {}
    for game_id, game in GAME_IDS.items():
        logging.info("Parsing %s", game_id)
        games[game] = GameParser(game, templates_path, game_list[game_id], names).parse()

    logging.info("Merging")
    merged = merge(games)
    name_map = resolve_names(merged)

    logging.info("Writing")
    properties = rds_root / "properties"
    for old in OLD_GENERATED:
        path = rds_root / old
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
    for package in ("objects", "archetypes"):
        shutil.rmtree(properties / package, ignore_errors=True)
        (properties / package).mkdir(parents=True)

    (properties / "archetypes" / "__init__.py").write_text(HEADER)
    (properties / "objects" / "__init__.py").write_text(object_tables_source(merged, name_map))

    for (package, name), classes in collect_modules(merged).items():
        module = f"retro_data_structures.properties.{package}.{name}"
        (properties / package / f"{name}.py").write_text(module_source(merged, name_map, module, classes))

    shared = sorted((e for e in merged.enums.values() if e.owner is None), key=lambda e: e.final_name)
    (rds_root / "enums" / "__init__.py").write_text(enum_file(shared))
    if report_path is not None:
        report_path.write_text(build_report(merged), encoding="utf-8", newline="\n")
