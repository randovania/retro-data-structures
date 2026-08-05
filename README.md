# Retro-data-structures
Construct type definitions for Retro Studios game

| Format | Prime 1 (Read) | Prime 1 (Write) | Prime 2 (Read) | Prime 2 (Write) | Prime 3 (Read) | Prime 3 (Write) |
|--------| -------------- | --------------- | -------------- | --------------- | -------------- | --------------- |
| PAK    | &check;        | &check;         | &check;        | &check;         | &cross;        | &cross;         |
| MLVL   | &check;        | &cross;         | &check;        | &cross;         | &check;        | &cross;         |
| MREA   | &cross;        | &cross;         | &check;        | &cross; [2]     | &cross;        | &cross;         |
| MAPA   | &check;        | &cross;         | &check;        | &cross;         | &cross;        | &cross;         |
| CMDL   | &check;        | &check;         | &check;        | &check;         | &cross;        | &cross;         |
| ANCS   | &check;        | &check;         | &check;        | &check;         | &cross;        | &cross;         |
| ANIM   | &check;        | &check;         | &check;        | &check;         | &cross;        | &cross;         |
| CSKR   | &check;        | &check;         | &check;        | &check;         | &cross;        | &cross;         |
| CINF   | &check;        | &check;         | &check;        | &check;         | &cross;        | &cross;         |
| PART   | &check;        | &check;         | &check;        | &check;         | &check; [1]    | &check; [1]     |
| HIER   | -              | -               | &check;        | &check;         | -              | -               |
| STRG   | &check;        | &check;         | &check;        | &check;         | &check;        | &check;         |
| SAVW   | &check;        | &check;         | &cross;        | &cross;         | &cross;        | &cross;         |

* [1] All existing files parse, but not checked if exhaustive for what the game supports.
* [2] Missing re-calculation of how sections are split between blocks.


## Example Usage

```python
from retro_data_structures.formats.pak_gc import PAK_GC


def read_file(path):
    with open(path, "rb") as f:
        return f.read()


PAK_GC.build_file({
    'named_resources': [
        {"asset": {"type": 'TXTR', "id": 201335801}, "name": 'TXTR_ElevatorIcon_1'},
        {"asset": {"type": 'TXTR', "id": 239414538}, "name": 'TXTR_ElevatorIcon'},
        {"asset": {"type": 'TXTR', "id": 564256465}, "name": 'TXTR_QuaterCurve'},
        {"asset": {"type": 'TXTR', "id": 568030977}, "name": 'TXTR_SaveStationIcon_1'},
    ],
    'resources': [
        {
            "asset": {"type": 'TXTR', "id": 201335801},
            "compressed": 1,
            "contents": {"value": read_file("ElevatorIcon_1.TXTR")},
        },
        {
            "asset": {"type": 'TXTR', "id": 201335801},
            "compressed": 1,
            "contents": {"value": read_file("ElevatorIcon.TXTR")},
        },
        {
            "asset": {"type": 'TXTR', "id": 201335801},
            "compressed": 1,
            "contents": {"value": read_file("QuaterCurve.TXTR")},
        },
        {
            "asset": {"type": 'TXTR', "id": 201335801},
            "compressed": 1,
            "contents": {"value": read_file("SaveStationIcon_1.TXTR")},
        },
    ]
}, "Game.pak")

```

## Setup

Make sure to clone this repository using the `--recursive` option (or running `git submodule update --init` if already cloned),
as the project needs those files to build

Once this has been done, the project and its extras can be installed

```
uv sync --all-groups --all-extras
```

Use `python -m retro_data_structures -h` to see available arguments

### Testing

Tests rely on user-provided ISO files for Metroid Prime, Metroid Prime 2: Echoes, and Metroid Prime 3: Corruption. Create a `.env` file in 
the repository root:

```
PRIME1_ISO = /path/to/prime1.iso
PRIME2_ISO = /path/to/prime2_ntsc.iso
PRIME2_PAL_ISO = /path/to/prime2_pal.iso
PRIME3_ISO = /path/to/prime3.iso
```

Tests can be run locally using 

```
uv run pytest -n 2
```