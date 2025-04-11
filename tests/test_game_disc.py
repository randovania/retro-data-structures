from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

from retro_data_structures.disc import game_disc

if TYPE_CHECKING:
    from pathlib import Path


def test_prime1_dol(prime1_iso: Path) -> None:
    disc = game_disc.GameDisc.parse(prime1_iso)
    disc_dol = disc.get_dol()

    assert hashlib.sha256(disc_dol).digest() == (
        b"wz\x83\n8\xa1\xd2\x07\x11i\x85g\xff\x89X\xfbO\xe7$\x1ar?J\x18\xe25YP\xd7\x9f\xc8V"
    )


def test_prime2_dol(prime2_iso: Path) -> None:
    disc = game_disc.GameDisc.parse(prime2_iso)
    disc_dol = disc.get_dol()

    assert hashlib.sha256(disc_dol).digest() == (
        b"v!\xe7W\x1e\x0e\xe4\xe0\x98\xa4\x0b\xc8\xa0\xa3dx\x11\xbd\x94NC\x02R)Bl}\xea\xe1v\x06\x84"
    )


def test_prime3_dol(prime3_iso: Path) -> None:
    disc = game_disc.GameDisc.parse(prime3_iso)
    disc_dol = disc.get_dol()

    assert hashlib.sha256(disc_dol).digest() == (
        b'kU\x0f"\x16\x02\x07GG\xa2\xe6\x1b\n\xa0d ?\xd4\x93\xf6\x86]\xfb;\x1a\x91&\x82\x06^a\x04'
    )
