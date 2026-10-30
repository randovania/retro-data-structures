"""
Decodes every script instance of every MREA of Prime, Echoes and Corruption with the generated property classes,
re-encodes it and compares with the original bytes. Also times decode and encode separately.

Uses the same env vars as the tests: PRIME1_ISO, PRIME2_ISO, PRIME3_ISO (or PRIME3_EXTRACTED_ISO).

    uv run python tools/script_roundtrip_baseline.py --output docs/baseline-roundtrip.md
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import hashlib
import json
import os
import time
import typing
from pathlib import Path

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.file_provider import FileProvider, IsoFileProvider, PathFileProvider
from retro_data_structures.formats.mlvl import Mlvl
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from retro_data_structures.properties.base_property import BaseObjectType


@dataclasses.dataclass
class Failure:
    type_name: str
    instance_id: int
    mrea_id: int
    reason: str


@dataclasses.dataclass
class GameResult:
    game: Game
    total: int = 0
    identical: int = 0
    decode_seconds: float = 0.0
    encode_seconds: float = 0.0
    areas: int = 0
    failures: list[Failure] = dataclasses.field(default_factory=list)
    # stable instance key -> [type name, sha1 of original, sha1 of re-encoded or "error: ..."]
    records: dict[str, list[str]] = dataclasses.field(default_factory=dict)


def _provider(game: Game) -> FileProvider | None:
    if game == Game.PRIME:
        env = "PRIME1_ISO"
    elif game == Game.ECHOES:
        env = "PRIME2_ISO"
    else:
        if "PRIME3_EXTRACTED_ISO" in os.environ:
            return PathFileProvider(Path(os.environ["PRIME3_EXTRACTED_ISO"]))
        env = "PRIME3_ISO"

    if env not in os.environ:
        return None
    return IsoFileProvider(Path(os.environ[env]))


def _describe_mismatch(original: bytes, encoded: bytes) -> str:
    offset = next((i for i, (a, b) in enumerate(zip(original, encoded, strict=False)) if a != b), None)
    if len(original) != len(encoded):
        extra = f"first diff at 0x{offset:x}" if offset is not None else "common prefix equal"
        return f"length {len(original)} -> {len(encoded)} ({extra})"
    return f"same length {len(original)}, first diff at 0x{offset:x}"


def _mismatch_category(original: bytes, encoded: bytes) -> str:
    if len(original) == len(encoded):
        return "same length, different content"
    if len(encoded) < len(original):
        return "encoded is shorter"
    return "encoded is longer"


def decode_properties(script_type: type[BaseObjectType], raw: bytes, game: Game) -> BaseObjectType:
    """The only place that decodes: the merged classes bind to the game when decoding."""
    return script_type.from_bytes(raw, game)


def encode_properties(obj: BaseObjectType, game: Game) -> bytes:
    """The only place that encodes."""
    return obj.to_bytes(game)


def _sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()  # noqa: S324


def _iter_instances(mrea: Mrea, game: Game) -> typing.Iterator[tuple[int, typing.Any]]:
    """Yields (layer index, instance). The generated objects layer has index -1."""
    for index, layer in enumerate(mrea.script_layers):
        for inst in layer.instances:
            yield index, inst
    if game >= Game.ECHOES:
        for inst in mrea.generated_objects_layer.instances:
            yield -1, inst


def _mrea_owners(asset_manager: AssetManager) -> dict[int, tuple[int, int]]:
    """MREA asset id -> (MLVL asset id, area index), first MLVL that has it wins. (0, -1) when in no MLVL."""
    owners: dict[int, tuple[int, int]] = {}
    for mlvl_id in sorted(asset_manager.all_asset_ids_of_type("MLVL")):
        try:
            mlvl = asset_manager.get_file(mlvl_id, Mlvl)
            for area in mlvl.areas:
                owners.setdefault(area.mrea_asset_id, (mlvl_id, area.index))
        except Exception as e:  # noqa: BLE001
            print(f"  failed to read MLVL 0x{mlvl_id:x}: {e!r}")
    return owners


def run_game(game: Game, limit_areas: int | None) -> GameResult | None:  # noqa: PLR0912, PLR0915
    provider = _provider(game)
    if provider is None:
        print(f"Skipping {game.name}: no ISO configured")
        return None

    result = GameResult(game)
    kwargs = {"ignore_low_paks": False} if game == Game.ECHOES else {}
    asset_manager = AssetManager(provider, target_game=game, **kwargs)

    mrea_ids = sorted(asset_manager.all_asset_ids_of_type("MREA"))
    if limit_areas is not None:
        mrea_ids = mrea_ids[:limit_areas]

    owners = _mrea_owners(asset_manager)

    # (type_name, instance id, mrea id, class | None, original bytes)
    pending: list[tuple[str, int, int, type[BaseObjectType] | None, bytes]] = []
    keys: list[str] = []
    for mrea_id in mrea_ids:
        try:
            mrea = asset_manager.get_file(mrea_id, Mrea)
            instances = list(_iter_instances(mrea, game))
        except Exception as e:  # noqa: BLE001
            print(f"  {game.name}: failed to load MREA 0x{mrea_id:x}: {e!r}")
            continue
        result.areas += 1
        mlvl_id, area_index = owners.get(mrea_id, (0, -1))
        for layer_index, inst in instances:
            keys.append(
                f"{mlvl_id:x}/{area_index}/{layer_index}/{int(inst.id):x}" + (f"@{mrea_id:x}" if mlvl_id == 0 else "")
            )
            try:
                script_type: type[BaseObjectType] | None = inst.script_type
            except KeyError:
                script_type = None
            type_name = inst.type_name if isinstance(inst.type_name, str) else f"0x{inst.type_name:02X}"
            pending.append((type_name, int(inst.id), mrea_id, script_type, inst.raw_properties))
        # drop the area's data, we only need the raw bytes of the properties
        del mrea, instances

    result.total = len(pending)
    print(f"  {game.name}: {result.areas} areas, {result.total} instances")

    # Decode
    decoded: list[BaseObjectType | None] = []
    decode_errors: dict[int, str] = {}
    start = time.perf_counter()
    for i, (_, _, _, script_type, raw) in enumerate(pending):
        if script_type is None:
            decoded.append(None)
            continue
        try:
            decoded.append(decode_properties(script_type, raw, game))
        except Exception as e:  # noqa: BLE001
            decoded.append(None)
            decode_errors[i] = f"{type(e).__name__}: {str(e)[:80]}"
    result.decode_seconds = time.perf_counter() - start

    # Encode
    encoded: list[bytes | None] = []
    encode_errors: dict[int, str] = {}
    start = time.perf_counter()
    for i, obj in enumerate(decoded):
        if obj is None:
            encoded.append(None)
            continue
        try:
            encoded.append(encode_properties(obj, game))
        except Exception as e:  # noqa: BLE001
            encoded.append(None)
            encode_errors[i] = f"{type(e).__name__}: {str(e)[:80]}"
    result.encode_seconds = time.perf_counter() - start

    # Compare
    for i, (type_name, instance_id, mrea_id, script_type, raw) in enumerate(pending):
        data_i = encoded[i]
        if data_i is not None:
            enc_hash = _sha1(data_i)
        elif script_type is None:
            enc_hash = "error: no class"
        else:
            enc_hash = "error: " + (decode_errors.get(i) or encode_errors.get(i, ""))
        result.records[keys[i]] = [type_name, _sha1(raw), enc_hash]

        if script_type is None:
            reason = "unknown object type (no generated class)"
        elif i in decode_errors:
            reason = f"decode error, {decode_errors[i]}"
        elif i in encode_errors:
            reason = f"encode error, {encode_errors[i]}"
        else:
            data = encoded[i]
            assert data is not None
            if data == raw:
                result.identical += 1
                continue
            reason = f"{_mismatch_category(raw, data)}: {_describe_mismatch(raw, data)}"
        result.failures.append(Failure(type_name, instance_id, mrea_id, reason))

    return result


def _category(reason: str) -> str:
    # the part before the details
    return (
        reason.split(":", 1)[0]
        if not reason.startswith(("decode error", "encode error"))
        else reason.split(",", maxsplit=1)[0]
    )


NOTES = """Round trip of the merged property classes (`properties/objects`), decoding with `from_bytes(raw, game)` and
encoding with `to_bytes(game)` (`CookMode.PRESERVE`: optional properties that were in the data are written back).
Timings are for all instances of the game, one after the other, excluding loading the MREAs.
A mismatch is either a decode error or an encoder that doesn't reproduce the bytes of the game's own cooker.
"""


def render(results: list[GameResult], max_listed: int) -> str:
    out: list[str] = []
    out.append("# Script instance round trip\n")
    out.append(
        "Generated by `tools/script_roundtrip_baseline.py`. For every MREA of each game, every script instance "
        "(all script layers, plus the generated objects layer for Echoes and Corruption) is decoded with its generated "
        "property class, re-encoded, and compared with the original `instance.raw_properties`.\n"
    )
    out.append(NOTES)
    out.append("| Game | Areas | Instances | Byte-identical | % | Decode (s) | Encode (s) |")
    out.append("|---|---:|---:|---:|---:|---:|---:|")
    for r in results:
        pct = 100.0 * r.identical / r.total if r.total else 0.0
        out.append(
            f"| {r.game.name} | {r.areas} | {r.total} | {r.identical} | {pct:.3f} | "
            f"{r.decode_seconds:.2f} | {r.encode_seconds:.2f} |"
        )
    out.append("")

    for r in results:
        out.append(f"## {r.game.name}\n")
        if not r.failures:
            out.append("All instances re-encode byte-identical.\n")
            continue

        categories = collections.Counter(_category(f.reason) for f in r.failures)
        out.append("Failure categories:\n")
        for category, count in categories.most_common():
            out.append(f"- {category}: {count}")
        out.append("")

        by_type_reason: dict[tuple[str, str], list[Failure]] = collections.defaultdict(list)
        for f in r.failures:
            # group the position-dependent details away
            by_type_reason[(f.type_name, _category(f.reason))].append(f)

        out.append("Failures by object type (count, first examples):\n")
        out.append("| Object type | Reason | Count | Example (instance id: detail) |")
        out.append("|---|---|---:|---|")
        for (type_name, category), failures in sorted(by_type_reason.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            example = failures[0]
            out.append(
                f"| {type_name} | {category} | {len(failures)} | 0x{example.instance_id:08x}: {example.reason} |"
            )
        out.append("")

        out.append(f"First {min(max_listed, len(r.failures))} failing instances (type, instance id, reason):\n")
        out.append("```")
        for f in r.failures[:max_listed]:
            out.append(f"{f.type_name} 0x{f.instance_id:08x} (mrea 0x{f.mrea_id:x}): {f.reason}")
        out.append("```\n")

    return "\n".join(out)


def write_snapshot(results: list[GameResult], path: Path) -> None:
    data = {r.game.name: r.records for r in results}
    path.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote snapshot to {path} ({path.stat().st_size} bytes)")


def compare_snapshot(results: list[GameResult], path: Path, max_listed: int = 50) -> bool:
    """Reports how many re-encoded hashes differ from the snapshot. Returns True when everything matches."""
    snapshot = json.loads(path.read_text(encoding="utf-8"))
    all_equal = True
    for r in results:
        old = snapshot.get(r.game.name)
        if old is None:
            print(f"{r.game.name}: not in the snapshot")
            continue
        differing = [k for k, v in r.records.items() if k in old and old[k][2] != v[2]]
        only_new = [k for k in r.records if k not in old]
        only_old = [k for k in old if k not in r.records]
        print(
            f"{r.game.name}: {len(r.records)} instances, {len(differing)} re-encode differently from the snapshot, "
            f"{len(only_new)} not in the snapshot, {len(only_old)} missing now"
        )
        all_equal = all_equal and not (differing or only_new or only_old)
        for k in differing[:max_listed]:
            print(f"  {r.records[k][0]} {k}: {old[k][2][:16]} -> {r.records[k][2][:16]}")
    return all_equal


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--games", nargs="+", default=["prime", "echoes", "corruption"])
    parser.add_argument("--limit-areas", type=int, default=None, help="Only use this many MREAs of each game")
    parser.add_argument("--max-listed", type=int, default=100, help="How many failing instances to list per game")
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--snapshot", type=Path, default=None, help="Write the hashes of all re-encoded instances")
    parser.add_argument("--compare", type=Path, default=None, help="Compare the re-encoded hashes with a snapshot")
    args = parser.parse_args()

    games = {"prime": Game.PRIME, "echoes": Game.ECHOES, "corruption": Game.CORRUPTION}
    results = []
    for name in args.games:
        print(f"Running {name}")
        r = run_game(games[name], args.limit_areas)
        if r is not None:
            results.append(r)

    if args.snapshot is not None:
        write_snapshot(results, args.snapshot)
    if args.compare is not None:
        compare_snapshot(results, args.compare)

    text = render(results, args.max_listed)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
