from construct.lib import ListContainer, Container

from retro_data_structures.conversion.asset_converter import AssetConverter, AssetDetails, Resource
from retro_data_structures.conversion.errors import UnsupportedTargetGame, UnsupportedSourceGame
from retro_data_structures.formats.meta_animation import MetaAnimationType
from retro_data_structures.game_check import Game


# ANCS Conversion
# For MP2->MP1 AnimID needs parsed and passed in here, EvntId needs to be created new/unique and passed in as well.
# For MP1->MP2 - Pass in EVNT file path to build proper event_sets


def _convert_meta_animation(animation, converter: AssetConverter, source_game: Game):
    if animation["type"] == MetaAnimationType.Play:
        animation["body"]["asset_id"] = converter.convert_id(animation["body"]["asset_id"], source_game)

    elif animation["type"] in (MetaAnimationType.Blend, MetaAnimationType.PhaseBlend):
        animation["body"]["anim_a"] = converter.convert_id(animation["body"]["anim_a"], source_game)
        animation["body"]["anim_b"] = converter.convert_id(animation["body"]["anim_b"], source_game)

    elif animation["type"] == MetaAnimationType.Random:
        for item in animation["body"]:
            _convert_meta_animation(item["animation"], converter, source_game)

    elif animation["type"] == MetaAnimationType.Sequence:
        for item in animation["body"]:
            _convert_meta_animation(item, converter, source_game)

    else:
        raise ValueError(f"Unknown animation type: {animation['type']}")


def _convert_meta_animations(data, converter: AssetConverter, source_game: Game):
    for named_animation in data["animation_set"]["animations"]:
        _convert_meta_animation(named_animation["meta"], converter, source_game)


def _convert_character(data, converter: AssetConverter, source_game: Game):
    for field in ["model_id", "skin_id", "skeleton_id", "frozen_model", "frozen_skin"]:
        data[field] = converter.convert_id(data[field], source_game)

    if converter.target_game == Game.PRIME:
        data["spatial_primitives_id"] = None
    elif source_game == Game.PRIME:
        data["spatial_primitives_id"] = converter.invalid_asset_id
    else:
        raise NotImplementedError("spatial_primitives_id from not-prime to not-prime")

    for field in ["generic_particles", "swoosh_particles", "electric_particles"]:
        data["particle_resource_data"][field] = [
            converter.convert_id(particle, source_game) for particle in data["particle_resource_data"][field]
        ]

    if converter.target_game == Game.PRIME:
        data["particle_resource_data"]["spawn_particles"] = None
    elif source_game == Game.PRIME:
        data["particle_resource_data"]["spawn_particles"] = []
    else:
        raise NotImplementedError("spawn_particles from not-prime to not-prime")


def get_animation_ids(animation):
    if animation["type"] == MetaAnimationType.Play:
        yield animation["body"]["asset_id"]

    elif animation["type"] in (MetaAnimationType.Blend, MetaAnimationType.PhaseBlend):
        yield from get_animation_ids(animation["body"]["anim_a"])
        yield from get_animation_ids(animation["body"]["anim_b"])

    elif animation["type"] == MetaAnimationType.Random:
        for item in animation["body"]:
            yield from get_animation_ids(item["animation"])

    elif animation["type"] == MetaAnimationType.Sequence:
        for item in animation["body"]:
            yield from get_animation_ids(item)

    else:
        raise ValueError(f"Unknown animation type: {animation['type']}")


def convert_from_prime(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.ECHOES:
        raise UnsupportedTargetGame(Game.PRIME, converter.target_game)

    for character in data["character_set"]["characters"]:
        character["version"] = 10
        character["unknown_1"] = 0
        character["unknown_2"] = 0
        character["unknown_3"] = 0
        _convert_character(character, converter, Game.PRIME)
        if character["frozen_model"] == 0:
            character["frozen_model"] = 0xFFFFFFFF
        if character["frozen_skin"] == 0:
            character["frozen_skin"] = 0xFFFFFFFF
        character["indexed_animation_aabb_array"] = ListContainer(character["animation_aabb_array"])
        for i, aabb_array in enumerate(character["indexed_animation_aabb_array"]):
            aabb_array["id"] = i
        for animation_name in character["animation_names"]:
            animation_name["unknown"] = None

    anim_to_event = {
        animation_resource["anim_id"]: animation_resource["event_id"]
        for animation_resource in data["animation_set"]["animation_resources"]
    }
    data["animation_set"]["animation_resources"] = None

    event_sets = ListContainer()
    for animation in data["animation_set"]["animations"]:
        anim_ids = list(get_animation_ids(animation["meta"]))
        event_sets.append(converter.convert_asset_by_id(anim_to_event[anim_ids[0]], Game.PRIME).resource)
    data["animation_set"]["event_sets"] = event_sets

    # Convert the animations after the event sets, so the asset id conversion doesn't break us
    _convert_meta_animations(data, converter, Game.PRIME)

    return data


def convert_from_echoes(data: Resource, details: AssetDetails, converter: AssetConverter):
    if converter.target_game != Game.PRIME:
        raise UnsupportedTargetGame(Game.ECHOES, converter.target_game)

    for character in data["character_set"]["characters"]:
        character["version"] = 6
        for animation_name in character["animation_names"]:
            animation_name["unknown"] = ""
        character["unknown_1"] = 1
        _convert_character(character, converter, Game.ECHOES)
        if character["frozen_model"] == 0xFFFFFFFF:
            character["frozen_model"] = 0
        if character["frozen_skin"] == 0xFFFFFFFF:
            character["frozen_skin"] = 0

    if details.asset_id == 0x41C2513F:
        del data["animation_set"]["event_sets"][1]

    _convert_meta_animations(data, converter, Game.ECHOES)

    data["animation_set"]["animation_resources"] = []
    seen_ids = set()

    for animation, event_set in zip(data["animation_set"]["animations"], data["animation_set"]["event_sets"]):
        details = AssetDetails(asset_id=None, asset_type="EVNT", original_game=Game.ECHOES)
        evnt_id = converter.convert_asset(event_set, details).id
        for anim_id in get_animation_ids(animation["meta"]):
            if anim_id not in seen_ids and anim_id != Game.ECHOES.invalid_asset_id:
                seen_ids.add(anim_id)
                data["animation_set"]["animation_resources"].append(
                    Container(
                        {
                            "anim_id": anim_id,
                            "event_id": evnt_id,
                        }
                    )
                )

    data["animation_set"]["event_sets"] = None

    return data


def convert_from_corruption(data: Resource, details: AssetDetails, converter: AssetConverter):
    raise UnsupportedSourceGame(Game.CORRUPTION)


CONVERTERS = {
    Game.PRIME: convert_from_prime,
    Game.ECHOES: convert_from_echoes,
    Game.CORRUPTION: convert_from_corruption,
}
