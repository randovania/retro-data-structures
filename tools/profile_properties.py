import argparse
import dataclasses
import io
import time
from pathlib import Path

import construct

from retro_data_structures import properties
from retro_data_structures.asset_manager import AssetManager, IsoFileProvider
from retro_data_structures.formats import Mrea
from retro_data_structures.game_check import Game
from retro_data_structures.properties.prime import objects as prime_objects

@dataclasses.dataclass()
class Object:
    identifier: str
    instance_id: int
    type: str
    properties: bytes


SerializedData = construct.Struct(
    game=construct.VarInt,
    header=construct.PrefixedArray(construct.VarInt, construct.Struct(
        identifier=construct.PascalString(construct.VarInt, "utf-8"),
        instance_id=construct.Int32ub,
        size=construct.VarInt,
    )),
    data=construct.GreedyBytes,
).compile()


def do_dump_properties(game: Game, args):
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
                header.append(dict(
                    identifier=f"{instance.name} of mrea 0x{asset_id:08x}",
                    instance_id=instance.id,
                    size=len(instance.raw_properties),
                ))
                if game == Game.PRIME:
                    name = prime_objects.get_object(instance.type_name).__name__
                else:
                    name = instance.type_name
                data.append(name.encode("ascii"))
                data.append(instance.raw_properties)

        print(f"Wrote properties for {asset_id:08x}")

    data_to_dump = dict(
        game=game.value,
        header=header,
        data=b"".join(data),
    )
    path = Path(__file__).parent.joinpath(f"properties_{game.name}.bin")
    SerializedData.build_file(
        data_to_dump,
        path,
    )


def _parse_properties(game: Game, property_data: construct.Container, build: bool, compare: bool):
    start_time = time.time()
    data = io.BytesIO(property_data.data)
    for instance in property_data.header:
        property_type = data.read(4).decode("ascii")
        property_class = properties.get_game_object(game, property_type)
        type_name = property_class.__name__

        before = data.tell()
        try:
            the_property = property_class.from_stream(data)
        except Exception as e:
            data.seek(before)
            data.read(instance.size)
            print(f"Unable to decode instance {instance.identifier} of type {type_name}: {type(e)} - {e}")
            continue

        after = data.tell()
        if after - before != instance.size:
            print(f"Instance {instance.identifier} of type {type_name} read {after - before} bytes, "
                  f"expected {instance.size}")

        if build:
            new_encoded = the_property.to_bytes()

            if compare:
                data.seek(before)
                original = data.read(after - before)
                if new_encoded != original:
                    re_decode = the_property.from_bytes(new_encoded)
                    if re_decode != the_property:
                        print(f"Comparing instance {instance.identifier} of type {type_name} failed")
                    elif len(new_encoded) > len(original):
                        print(f"Instance {instance.identifier} of type {type_name} is longer than the original")

    print("Processed properties in {:0.4f} seconds".format(time.time() - start_time))


def do_parse_properties(game: Game, args):
    path = Path(__file__).parent.joinpath(f"properties_{game.name}.bin")

    property_data = SerializedData.parse_file(path)

    for repeat in range(args.repeat):
        _parse_properties(game, property_data, args.build or args.compare, args.compare)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", required=True, choices=[g.name for g in Game])

    sub_parser = parser.add_subparsers(dest="tool", required=True)
    dump_properties = sub_parser.add_parser("dump-properties")
    dump_properties.add_argument("iso", type=Path)
    parse_properties = sub_parser.add_parser("parse-properties")
    parse_properties.add_argument("--repeat", default=1, type=int, help="Perform the decoding this many times")
    parse_properties.add_argument("--build", action="store_true", help="re-build and discard the result")
    parse_properties.add_argument("--compare", action="store_true", help="re-build and compare with original")

    args = parser.parse_args()
    game: Game = getattr(Game, args.game)

    if args.tool == "dump-properties":
        do_dump_properties(game, args)
    elif args.tool == "parse-properties":
        do_parse_properties(game, args)


if __name__ == '__main__':
    main()
