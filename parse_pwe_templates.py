"""
Generates the property classes in `src/retro_data_structures/properties/{objects,archetypes}` and the enums in
`src/retro_data_structures/enums/__init__.py` from `retro-script-object-templates`.
Run manually after changing the templates. The output is committed, and CI checks that it is up to date.

`--report PATH` also writes a report of how the games' templates were merged: split fields, fields only in one game,
structs and enums that differ, and optional Prime properties.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pwe_generator.generate import generate  # noqa: E402

rds_root = Path(__file__).parent.joinpath("src", "retro_data_structures")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report", type=Path, help="Also write the merge report to this path.")
    args = parser.parse_args()
    generate(rds_root, Path(__file__).parent.joinpath("retro-script-object-templates"), args.report)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
