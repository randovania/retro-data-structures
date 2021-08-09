import argparse
import asyncio
import itertools
import json
import logging
import typing
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Optional, List

from retro_data_structures import construct_extensions, dependencies, formats
from retro_data_structures.asset_provider import AssetProvider
from retro_data_structures.conversion import conversions
from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.formats import mlvl, AssetId
from retro_data_structures.game_check import Game

types_per_game = {
    "metroid_prime_1": {
        "mlvl": mlvl.Prime1MLVL,
    },
    "metroid_prime_2": {
        "mlvl": mlvl.Prime2MLVL,
    },
    "metroid_prime_3": {
        "mlvl": mlvl.Prime3MLVL,
    },
}


def game_argument_type(s: str) -> Game:
    try:
        return Game(int(s))
    except ValueError:
        # not a number, look by name
        for g in Game:
            g = typing.cast(Game, g)
            if g.name.lower() == s.lower():
                return g
        raise ValueError(f"No enum named {s} found")


def add_game_argument(parser: argparse.ArgumentParser, name="--game"):
    choices = []
    for g in Game:
        g = typing.cast(Game, g)
        choices.append(g.value)
        choices.append(g.name)

    parser.add_argument(name, help="The game of the file", type=game_argument_type, choices=list(Game), required=True)


def create_parser():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command", required=True)

    ksy_export = subparser.add_parser("ksy-export")
    ksy_export.add_argument("output_path", type=Path)

    decode = subparser.add_parser("decode")
    add_game_argument(decode)
    decode.add_argument("--format", help="Hint the format of the file. Defaults to extension.")
    decode.add_argument("--re-encode", help="Re-encode afterwards and compares to the original.", action="store_true")
    decode.add_argument("input_path", type=Path, help="Path to the file")

    compare = subparser.add_parser("compare-files")
    add_game_argument(compare)
    compare.add_argument("--format", help="Hint the format of the file", required=True)
    compare.add_argument("--limit", help="Limit the number of files to test", type=int)
    compare.add_argument("input_path", type=Path, help="Path to the directory to glob")

    decode_from_paks = subparser.add_parser("decode-from-pak")
    add_game_argument(decode_from_paks)
    decode_from_paks.add_argument("paks_path", type=Path, help="Path to where to find pak files")
    decode_from_paks.add_argument("asset_id", type=lambda x: int(x, 0), help="Asset id to print")

    deps = subparser.add_parser("list-dependencies")
    add_game_argument(deps)
    deps.add_argument("paks_path", type=Path, help="Path to where to find pak files")
    g = deps.add_mutually_exclusive_group()
    g.add_argument("--asset-ids", type=lambda x: int(x, 0), nargs='+', help="Asset id to list dependencies for")
    g.add_argument("--asset-type", type=str, help="List dependencies for all assets of the given type.")

    convert = subparser.add_parser("convert")
    add_game_argument(convert, "--source-game")
    add_game_argument(convert, "--target-game")
    convert.add_argument("paks_path", type=Path, help="Path to where to find source pak files")
    convert.add_argument("asset_ids", type=lambda x: int(x, 0), nargs='+', help="Asset id to list dependencies for")

    return parser


def do_ksy_export(args):
    output_path: Path = args.output_path
    output_path.mkdir(parents=True, exist_ok=True)

    for game, game_formats in types_per_game.items():
        for format_name, cls in game_formats.items():
            print(f"Exporting {game} / {format_name}")
            cls.export_ksy(f"{game}_{format_name}", output_path.joinpath(f"{game}_{format_name}.ksy"))


def dump_to(path: Path, decoded):
    def default(o):
        if callable(o):
            o = o()
        if isinstance(o, bytes):
            return len(o)

        raise TypeError(f'Object of type {o.__class__.__name__} '
                        f'is not JSON serializable')

    with path.open("w") as f:
        x = construct_extensions.convert_to_raw_python(decoded)
        f.write(json.JSONEncoder(indent=4, default=default).encode(x))


def do_decode(args):
    input_path: Path = args.input_path
    file_format = args.format
    game: Game = args.game
    re_encode = args.re_encode

    if file_format is None:
        file_format = input_path.suffix[1:]

    construct_class = formats.format_for(file_format)

    raw = input_path.read_bytes()
    decoded_from_raw = construct_class.parse(raw, target_game=game)
    print(decoded_from_raw)

    if re_encode:
        encoded = construct_class.build(decoded_from_raw, target_game=game)
        if raw != encoded:
            print(f"{input_path}: Results differ (len(raw): {len(raw)}; len(encoded): {len(encoded)})")


def do_decode_from_pak(args):
    game: Game = args.game
    paks_path: Path = args.paks_path
    asset_id: int = args.asset_id

    with AssetProvider(game, list(paks_path.glob("*.pak"))) as asset_provider:
        print(asset_provider.get_asset(asset_id))


def list_dependencies(args):
    game: Game = args.game
    paks_path: Path = args.paks_path
    asset_ids: List[int]

    with AssetProvider(game, list(paks_path.glob("*.pak"))) as asset_provider:
        if args.asset_ids is not None:
            asset_ids = args.asset_ids
        else:
            asset_ids = [
                resource.asset.id
                for resource in asset_provider.all_resource_headers
                if resource.asset.type == args.asset_type.upper()
            ]

        for asset_type, asset_id in dependencies.recursive_dependencies_for(asset_provider, asset_ids):
            print("{}: {}".format(asset_type, hex(asset_id)))


def do_convert(args):
    source_game: Game = args.source_game
    target_game: Game = args.target_game
    paks_path: Path = args.paks_path
    asset_ids: List[int] = args.asset_ids

    with AssetProvider(source_game, list(paks_path.glob("*.pak"))) as asset_provider:
        next_id = 0xFFFF0000

        def id_generator(asset_type):
            nonlocal next_id
            result = next_id
            while asset_provider.asset_id_exists(result):
                result += 1

            next_id = result + 1
            return result

        converter = AssetConverter(
            target_game=target_game,
            asset_providers={source_game: asset_provider},
            id_generator=id_generator,
            converters=conversions.converter_for,
        )

        for asset_id in asset_ids:
            converted = converter.convert_asset_by_id(asset_id, source_game)

            print(
                "\n========================="
                "\n* Original Id: {:08x}"
                "\n* Target Id: {:08x}"
                "\n* Asset Type: {}"
                "\n\n{}".format(
                    asset_id,
                    converted.id,
                    converted.type,
                    converted.resource,
                ))

            for dependency in dependencies.direct_dependencies_for(converted.resource, converted.type, target_game):
                print(f"* Dependency: {dependency[1]:08x} ({dependency[0]})")

        print("==================\n>> All converted assets")
        reverse_converted_ids: typing.Dict[AssetId, typing.Tuple[Game, AssetId]] = {
            v: k
            for k, v in converter.converted_ids.items()
        }

        for converted_asset in converter.converted_assets.values():
            print(" {}: {:08x} from {:08x} ({})".format(
                converted_asset.type,
                converted_asset.id,
                reverse_converted_ids[converted_asset.id][1],
                reverse_converted_ids[converted_asset.id][0].name,
            ))


_ITEM_ID_TO_NAME = {
    85: "AbsorbAttack",
    94: "ActivateMorphballBoost",
    32: "AgonKey1",
    33: "AgonKey2",
    34: "AgonKey3",
    98: "AmberTranslator",
    3: "AnnihilatorBeam",
    21: "AnnihilatorBomb",
    66: "ArchenemyCount",
    89: "BeamWeaponsDisabled",
    16: "BoostBall",
    96: "CannonBall",
    22: "ChargeBeam",
    108: "ChargeCombo",
    100: "CobaltTranslator",
    79: "CoinAmplifier",
    80: "CoinCounter",
    8: "CombatVisor",
    45: "DarkAmmo",
    1: "DarkBeam",
    19: "DarkBomb",
    83: "DarkShield",
    13: "DarkSuit",
    10: "DarkVisor",
    5: "Darkburst",
    86: "DeathBall",
    65: "DiedCount",
    92: "DisableBall",
    93: "DisableSpaceJump",
    58: "DoubleDamage",
    11: "EchoVisor",
    99: "EmeraldTranslator",
    42: "EnergyTank",
    107: "EnergyTransferModule",
    64: "FragCount",
    23: "GrappleBeam",
    25: "GravityBoost",
    95: "HackedEffect",
    41: "HealthRefill",
    38: "HiveKey1",
    39: "HiveKey2",
    40: "HiveKey3",
    59: "Invincibility",
    57: "Invisibility",
    47: "ItemPercentage",
    46: "LightAmmo",
    2: "LightBeam",
    20: "LightBomb",
    84: "LightShield",
    14: "LightSuit",
    50: "MiscCounter3",
    44: "Missile",
    90: "MissileWeaponsDisabled",
    15: "MorphBall",
    18: "MorphBallBombs",
    56: "MultiChargeUpgrade",
    51: "Multiplayer_Archenemy",
    49: "Multiplayer_NumPlayersInOptionsMenu",
    48: "Multiplayer_NumPlayersJoined",
    67: "PersistentCounter1",
    68: "PersistentCounter2",
    69: "PersistentCounter3",
    70: "PersistentCounter4",
    71: "PersistentCounter5",
    72: "PersistentCounter6",
    73: "PersistentCounter7",
    74: "PersistentCounter8",
    0: "PowerBeam",
    43: "Powerbomb",
    87: "ScanVirus",
    9: "ScanVisor",
    27: "ScrewAttack",
    26: "SeekerLauncher",
    7: "SonicBoom",
    24: "SpaceJumpBoots",
    17: "SpiderBall",
    6: "Sunburst",
    4: "SuperMissile",
    75: "SwitchVisorCombat",
    77: "SwitchVisorDark",
    78: "SwitchVisorEcho",
    76: "SwitchVisorScan",
    55: "SwitchWeaponAnnihilator",
    53: "SwitchWeaponDark",
    54: "SwitchWeaponLight",
    52: "SwitchWeaponPower",
    29: "TempleKey1",
    30: "TempleKey2",
    31: "TempleKey3",
    101: "TempleKey4",
    102: "TempleKey5",
    103: "TempleKey6",
    104: "TempleKey7",
    105: "TempleKey8",
    106: "TempleKey9",
    35: "TorvusKey1",
    36: "TorvusKey2",
    37: "TorvusKey3",
    28: "TranslatorUpgrade_TempETM",
    60: "Unknown_60",
    61: "Unknown_61",
    62: "Unknown_62",
    63: "Unknown_63",
    91: "Unknown_91",
    82: "UnlimitedBeamAmmo",
    81: "UnlimitedMissiles",
    12: "VariaSuit",
    97: "VioletTranslator",
    88: "VisorStatic",
}


def decode_encode_compare_file(file_path: Path, game: Game, file_format: str):
    construct_class = formats.format_for(file_format)

    try:
        raw = file_path.read_bytes()
        decoded_from_raw = construct_class.parse(raw, target_game=game)

        sections = []
        for group in decoded_from_raw.section_groups:
            sections.extend(group.sections)

        conditionals = [0xCEC16932, 0xE709DDC0, 0x49614C51, 0xB498B424]
        condition_name = ["Equal To", "Not Equal To", "Greater Than", "Less Than", "Greater Than or Equal To",
                          "Less Than or Equal To", "Greater Than All Other Players", "Less Than All Other Players"]

        from retro_data_structures.formats.scly import SCLY
        for i in range(decoded_from_raw.script_layers_section, decoded_from_raw.generated_script_objects_section):
            scly = SCLY.parse(sections[i].data, target_game=game)
            for instance in scly.script_instances:
                name = None
                arg = None
                func = None

                if instance.type in {"SPFN", "CRLY"}:
                    for prop in instance.properties.data:
                        if prop.id == 0x255A4580:
                            name = prop.data[0].data
                        if prop.id == 0xB581574B:
                            arg = prop.data
                        if prop.id == 0x95F8D644:
                            func = prop.data

                        if prop.id == 0x3FA164BC and prop.data != 0:
                            print(f"{name}: func {func}, {_ITEM_ID_TO_NAME[prop.data]}, quantity {arg}")

                        if prop.id in conditionals:
                            if prop.data[0].data != 0:
                                index = conditionals.index(prop.id)
                                item = _ITEM_ID_TO_NAME[prop.data[1].data]
                                field = "Capacity" if prop.data[2].data else "Amount"
                                criteria = condition_name[prop.data[3].data]
                                value = prop.data[4].data
                                print(f"{name}: conditional {index}, {item} {field} {criteria} {value}")

        # encoded = construct_class.build(decoded_from_raw, target_game=game)

        # if raw != encoded and raw.rstrip(b"\xFF") != encoded:
        #     return f"{file_path}: Results differ (len(raw): {len(raw)}; len(encoded): {len(encoded)})"
        return None

    except Exception as e:
        return f"{file_path}: Received error - {e}"


async def compare_all_files_in_path(args):
    input_path: Path = args.input_path
    file_format: str = args.format
    game: Game = args.game
    limit: Optional[int] = args.limit

    def apply_limit(it):
        if limit is None:
            return it
        else:
            return itertools.islice(it, limit)

    loop = asyncio.get_running_loop()

    try:
        import tqdm
    except ImportError:
        tqdm = None

    errors = []

    with ProcessPoolExecutor(max_workers=1) as executor:
        files = apply_limit(input_path.rglob(f"*.{file_format.upper()}"))
        # if tqdm is not None:
        #     files = tqdm.tqdm(files, unit=" file")

        for f in files:
            print(f)
            decode_encode_compare_file(f, game, file_format)

        raise SystemExit(0)

        results = [loop.run_in_executor(executor, decode_encode_compare_file, f, game, file_format)
                   for f in files]
        as_completed = asyncio.as_completed(results)
        if tqdm is not None:
            as_completed = tqdm.tqdm(as_completed, total=len(results), unit=" file")

        for c in as_completed:
            message = await c
            if message:
                if tqdm is not None:
                    errors.append(message)
                    as_completed.set_postfix_str(f"{len(errors)} errors")
                else:
                    print(message)
            raise SystemExit

    if errors:
        print(f"{len(errors)} errors:")
        for m in errors:
            print(m)


def main():
    logging.basicConfig(level=logging.INFO)
    args = create_parser().parse_args()

    if args.command == "ksy-export":
        do_ksy_export(args)
    elif args.command == "decode":
        do_decode(args)
    elif args.command == "decode-from-pak":
        do_decode_from_pak(args)
    elif args.command == "list-dependencies":
        list_dependencies(args)
    elif args.command == "convert":
        do_convert(args)
    elif args.command == "compare-files":
        asyncio.run(compare_all_files_in_path(args))
    else:
        raise ValueError(f"Unknown command: {args.command}")
