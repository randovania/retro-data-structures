from __future__ import annotations

import argparse
import hashlib
import io
import json
import time
from pathlib import Path

import construct

from retro_data_structures import properties
from retro_data_structures.asset_manager import AssetManager, IsoFileProvider, PathFileProvider
from retro_data_structures.formats import Mrea, Room
from retro_data_structures.game_check import Game
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.prime import objects as prime_objects

SerializedData = construct.Struct(
    game=construct.VarInt,
    header=construct.PrefixedArray(
        construct.VarInt,
        construct.Struct(
            identifier=construct.PascalString(construct.VarInt, "utf-8"),
            instance_id=construct.VarInt,
            size=construct.VarInt,
        ),
    ),
    data=construct.GreedyBytes,
)


def do_dump_properties_mrea(game: Game, args):
    manager = AssetManager(IsoFileProvider(args.iso), target_game=game)

    header = []
    data = []

    for asset_id in manager.all_asset_ids():
        if manager.get_asset_type(asset_id) != Mrea.resource_type():
            continue

        try:
            mrea = manager.get_parsed_asset(asset_id, type_hint=Mrea)
        except construct.ConstructError as e:
            print(f"Unable to parse {asset_id:08x}: {e}")
            continue

        for layer in mrea.script_layers:
            for instance in layer.instances:
                header.append(
                    {
                        "identifier": f"{instance.name} of mrea 0x{asset_id:08x}",
                        "instance_id": instance.id,
                        "size": len(instance.raw_properties),
                    }
                )
                if game == Game.PRIME:
                    name = prime_objects.get_object(instance.type_name).__name__
                else:
                    name = instance.type_name
                data.append(name.encode("ascii"))
                data.append(instance.raw_properties)

        print(f"Wrote properties for {asset_id:08x}")

    data_to_dump = {
        "game": game.value,
        "header": header,
        "data": b"".join(data),
    }
    path = Path(__file__).parent.joinpath(f"properties_{game.name}.bin")
    SerializedData.build_file(
        data_to_dump,
        path,
    )


def do_dump_properties_room(game: Game, args):
    manager = AssetManager(PathFileProvider(args.root), target_game=game)

    header = []
    data = []

    for asset_id in manager.all_asset_ids():
        if manager.get_asset_type(asset_id) != Room.resource_type():
            continue

        try:
            room = manager.get_parsed_asset(asset_id, type_hint=Room)
        except construct.ConstructError as e:
            print(f"Unable to parse {asset_id}: {e}")
            continue

        for i, instance in enumerate(room.raw.script_data.properties):
            if not isinstance(instance.data, BaseProperty):
                continue

            body = instance.data.to_bytes()
            header.append(
                {
                    "identifier": f"{i} property of room {asset_id} ({instance.data.__class__.__name__})",
                    "instance_id": instance.type_id,
                    "size": len(body),
                }
            )
            data.append(body)

        print(f"Wrote properties for {asset_id}")

    data_to_dump = {
        "game": game.value,
        "header": header,
        "data": b"".join(data),
    }
    path = Path(__file__).parent.joinpath(f"properties_{game.name}.bin")
    SerializedData.build_file(
        data_to_dump,
        path,
    )


def _parse_properties(  # noqa: PLR0912 Too many branches
    game: Game,
    property_data: construct.Container,
    build: bool,
    compare: bool,
    report: bool,
) -> list[dict]:
    decoded_results = []

    start_time = time.time()
    data = io.BytesIO(property_data.data)
    for instance in property_data.header:
        try:
            if game == Game.PRIME_REMASTER:
                property_class = properties.get_game_object(game, instance.instance_id)
            else:
                property_class = properties.get_game_object(game, data.read(4).decode("ascii"))
        except KeyError:
            data.read(instance.size)
            continue
        type_name = property_class.__name__

        before = data.tell()
        try:
            the_property = property_class.from_stream(data)
        except Exception as e:
            data.seek(before)
            data.read(instance.size)
            print(f"Unable to decode instance {instance.identifier} of type {type_name}: {type(e)} - {e}")
            if report:
                decoded_results.append(
                    {
                        "identifier": instance.identifier,
                        "error": str(e),
                    }
                )
            continue

        after = data.tell()
        if after - before != instance.size:
            print(
                f"Instance {instance.identifier} of type {type_name} read {after - before} bytes, "
                f"expected {instance.size}"
            )

        if build:
            new_encoded = the_property.to_bytes()
            if report:
                decoded_results.append(
                    {
                        "identifier": instance.identifier,
                        "value": the_property.to_json(),
                        "rebuild_sha256": hashlib.sha256(new_encoded).hexdigest(),
                    }
                )

            if compare:
                data.seek(before)
                original = data.read(after - before)
                if new_encoded != original:
                    re_decode = the_property.from_bytes(new_encoded)
                    if re_decode != the_property:
                        print(f"Comparing instance {instance.identifier} of type {type_name} failed")
                    elif len(new_encoded) > len(original):
                        print(f"Instance {instance.identifier} of type {type_name} is longer than the original")

    print(f"Processed properties in {time.time() - start_time:0.4f} seconds")
    return decoded_results


def do_parse_properties(game: Game, args):
    path = Path(__file__).parent.joinpath(f"properties_{game.name}.bin")

    property_data = SerializedData.parse_file(path)
    decoded_result = None

    for repeat in range(args.repeat):
        decoded_result = _parse_properties(game, property_data, args.build or args.compare, args.compare, args.report)

    if args.report:
        assert decoded_result is not None
        encoded_results = json.dumps(decoded_result, indent=4)
        encoded_results_path = path.with_suffix(".json")

        if encoded_results_path.exists():
            if encoded_results_path.read_text() != encoded_results:
                print("Results differ from last run!")
        else:
            encoded_results_path.write_text(encoded_results)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", required=True, choices=[g.name for g in Game])

    sub_parser = parser.add_subparsers(dest="tool", required=True)
    dump_properties = sub_parser.add_parser("dump-properties-mrea")
    dump_properties.add_argument("iso", type=Path)
    dump_properties = sub_parser.add_parser("dump-properties-room")
    dump_properties.add_argument("root", type=Path)
    parse_properties = sub_parser.add_parser("parse-properties")
    parse_properties.add_argument("--repeat", default=1, type=int, help="Perform the decoding this many times")
    parse_properties.add_argument("--build", action="store_true", help="re-build and discard the result")
    parse_properties.add_argument("--compare", action="store_true", help="re-build and compare with original")
    parse_properties.add_argument("--report", action="store_true", help="creates a json report of the decoded values")

    args = parser.parse_args()
    game: Game = getattr(Game, args.game)

    if args.tool == "dump-properties-mrea":
        do_dump_properties_mrea(game, args)
    elif args.tool == "dump-properties-room":
        do_dump_properties_room(game, args)
    elif args.tool == "parse-properties":
        do_parse_properties(game, args)


if __name__ == "__main__":
    main()
