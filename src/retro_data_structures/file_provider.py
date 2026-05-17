from __future__ import annotations

import fnmatch
import typing

from retro_data_structures.disc.game_disc import GameDisc

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from pathlib import Path


class FileProvider:
    def is_file(self, name: str) -> bool:
        raise NotImplementedError

    def rglob(self, pattern: str) -> Iterator[str]:
        raise NotImplementedError

    def open_binary(self, name: str) -> typing.BinaryIO:
        raise NotImplementedError

    def read_binary(self, name: str) -> bytes:
        raise NotImplementedError

    def get_dol(self) -> bytes:
        raise NotImplementedError

    def get_file_list(self) -> list[str]:
        raise NotImplementedError


class PathFileProvider(FileProvider):
    def __init__(self, root: Path):
        if not root.is_dir():
            raise FileNotFoundError(f"{root} is not a directory")
        self.root = root
        self.file_root = root.joinpath("files")

    def __repr__(self) -> str:
        return f"<PathFileProvider {self.root}>"

    def is_file(self, name: str) -> bool:
        return self.file_root.joinpath(name).is_file()

    def rglob(self, name: str) -> Iterator[str]:
        for it in self.file_root.rglob(name):
            if it.is_file():
                yield it.relative_to(self.file_root).as_posix()

    def open_binary(self, name: str) -> typing.BinaryIO:
        return self.file_root.joinpath(name).open("rb")

    def read_binary(self, name: str) -> bytes:
        with self.open_binary(name) as f:
            return f.read()

    def get_dol(self) -> bytes:
        return self.root.joinpath("sys/main.dol").read_bytes()

    def get_file_list(self) -> list[str]:
        return list(self.rglob("*"))


class IsoFileProvider(FileProvider):
    game_disc: GameDisc

    def __init__(self, iso_path: Path):
        self.iso_path = iso_path

        self.game_disc = GameDisc.parse(iso_path)
        self.all_files = self.game_disc.files()

    def __repr__(self) -> str:
        return f"<IsoFileProvider {self.iso_path}>"

    def is_file(self, name: str) -> bool:
        return name in self.all_files

    def rglob(self, pattern: str) -> Iterator[str]:
        for it in self.all_files:
            if fnmatch.fnmatch(it, pattern):
                yield it

    def open_binary(self, name: str) -> typing.BinaryIO:
        return self.game_disc.open_binary(name)

    def read_binary(self, name: str) -> bytes:
        return self.game_disc.read_binary(name)

    def get_dol(self) -> bytes:
        return self.game_disc.get_dol()

    def get_file_list(self) -> list[str]:
        return list(self.all_files)
