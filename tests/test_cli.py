from __future__ import annotations

import os
from typing import TYPE_CHECKING
from unittest.mock import call, patch

from retro_data_structures import cli

if TYPE_CHECKING:
    from pathlib import Path


def test_list_docks(prime2_iso: Path) -> None:
    with patch("builtins.print") as mock_print:
        cli.handle_args(
            cli.create_parser().parse_args(
                [
                    "areas",
                    "--game",
                    "ECHOES",
                    "--input-iso",
                    os.fspath(prime2_iso),
                    "list-docks",
                    "0x1baa96c2",
                    "0x65B801CE",
                ]
            )
        )
    mock_print.assert_has_calls(
        [
            call("1 docks found"),
            call("Dock 0. 1 connections, 4 coordinates."),
            call("> Connections:"),
            call(" 0: area  5, dock index: 0"),
            call("> Coordinates:"),
            call("0: [2.5, -8.162336349487305, -2.4206600189208984]"),
            call("1: [-2.5, -8.162336349487305, -2.4206600189208984]"),
            call("2: [-2.5, -8.162335395812988, -7.420660018920898]"),
            call("3: [2.5, -8.162335395812988, -7.420660018920898]"),
        ]
    )
