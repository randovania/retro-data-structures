from retro_data_structures.conversion.asset_converter import AssetConverter, Resource, AssetDetails
from retro_data_structures.conversion.errors import UnsupportedTargetGame, UnsupportedSourceGame
from retro_data_structures.game_check import Game


def convert_from_prime(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.ECHOES:
        raise UnsupportedTargetGame(Game.PRIME, converter.target_game)

    total_vertices = 0
    vertex_sizes = {}
    bones = {}
    for i, vertex_group in enumerate(data["vertex_groups"]):
        vertex_sizes[i] = vertex_group["vertex_count"]
        for weight in vertex_group["weights_array"]:
            bones[i] = weight["bone_id"]
            weight["bone_id"] = weight["bone_id"] - 3
        total_vertices += vertex_group["vertex_count"]

    data["footer"]["pool_to_skin_idx"] = [None] * (-(len(data["vertex_groups"]) // -10) * 10)
    for i in range(-(len(data["vertex_groups"]) // -10) * 10):
        data["footer"]["pool_to_skin_idx"][i] = 0xFFFF
    for i in range(len(list(set(bones.values())))):
        data["footer"]["pool_to_skin_idx"][i] = i
    for i, size in enumerate(vertex_sizes.values()):
        data["footer"]["trailing_bytes"] += i.to_bytes(1, "big") * size

    return data


def convert_from_echoes(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.PRIME:
        raise UnsupportedTargetGame(Game.ECHOES, converter.target_game)

    total_vertices = 0
    for i, vertex_group in enumerate(data["vertex_groups"]):
        for weight in vertex_group["weights_array"]:
            weight["bone_id"] = weight["bone_id"] + 3
        total_vertices += vertex_group["vertex_count"]

    data["footer"] = {
        "unk_a": {"first": 0xFFFFFFFF, "other": total_vertices},
        "unk_b": {"first": 0xFFFFFFFF, "other": total_vertices},
        "trailing_bytes": b"",
    }

    return data


def convert_from_corruption(data: Resource, details: AssetDetails, converter: AssetConverter):
    raise UnsupportedSourceGame(Game.CORRUPTION)


CONVERTERS = {
    Game.PRIME: convert_from_prime,
    Game.ECHOES: convert_from_echoes,
    Game.CORRUPTION: convert_from_corruption,
}
