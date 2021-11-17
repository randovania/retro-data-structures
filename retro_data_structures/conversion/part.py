import copy

from retro_data_structures.conversion.asset_converter import AssetConverter, Resource, AssetDetails
from retro_data_structures.game_check import Game


def upgrade(data, converter: AssetConverter, source_game: Game):
    if source_game < Game.ECHOES <= converter.target_game:
        for element in data["elements"]:
            if element["type"] == "KSSM" and element["body"]["magic"] != "NONE":
                for spawn in element["body"]["value"]["spawns"]:
                    for t in spawn["v2"]:
                        t["type"] = "PART"


def downgrade(data, converter: AssetConverter, source_game: Game):
    if converter.target_game <= Game.PRIME < source_game:
        for element in data["elements"][:]:
            if element["type"] == "KSSM" and element["body"]["magic"] != "NONE":
                for spawn in element["body"]["value"]["spawns"]:
                    for t in spawn["v2"]:
                        t["type"] = 0

            if element["type"] == "RDOP":
                data["elements"].remove(element)

            if element["type"] == "XTAD":
                data["elements"].remove(element)

            if element["type"] == "INDM":
                data["elements"].remove(element)

            if element["type"] == "VMPC":
                data["elements"].remove(element)
                
            if element["type"] == "EMTR":
                if element["body"]["type"] == "SEMR":
                    if (
                        element["body"]["body"]["a"]["type"] == "RNDV"
                        and element["body"]["body"]["b"]["type"] == "RNDV"
                    ):
                        element["body"]["type"] = "SPHE"
                        element["body"]["body"] = {
                            "a": {
                                "type": "RTOV",
                                "body" : {
                                    "type": "CNST",
                                    "body": 0,
                                },
                            },
                            "b": element["body"]["body"]["a"]["body"],
                            "c": {
                                "type": "RAND",
                                "body": {
                                    "a": {
                                        "type": "CNST",
                                        "body": 0,
                                    },
                                    "b": element["body"]["body"]["b"]["body"],
                                },
                            },
                        }
                    if (
                        element["body"]["body"]["a"]["type"] == "RNDV"
                        and element["body"]["body"]["b"]["type"] == "CNST"
                    ):
                        element["body"]["type"] = "SPHE"
                        element["body"]["body"] = {
                            "a": {
                                "type": "RTOV",
                                "body": {
                                    "type": "CNST",
                                    "body": 0
                                }
                            },
                            "b": element["body"]["body"]["a"]["body"],
                            "c": {
                                "type": "RAND",
                                "body": {
                                    "a": {
                                        "type": "CNST",
                                        "body": 0
                                    },
                                    "b": element["body"]["body"]["b"]["body"]["a"]
                                }
                            }
                        }
                if element["body"]["type"] == "ELPS":
                    element["body"]["type"] = "SPHE"
                    element["body"]["body"]["b"] = element["body"]["body"]["b"]["body"]["a"]
                    element["body"]["body"]["c"] = element["body"]["body"]["d"].copy()
                    del element["body"]["body"]["d"]
                    del element["body"]["body"]["e"]

            if element["type"] == "COLR":
                if element["body"]["type"] == "MDAO":
                    if (
                        element["body"]["body"]["a"]["type"] == "KEYE"
                        and element["body"]["body"]["b"]["type"] == "KEYP"
                    ):
                        org_colr_mado_a_keye = element["body"]["body"]["a"]["body"]["keys"]
                        new_colr_cnst_a_keyp_a = copy.deepcopy(element["body"]["body"]["a"])
                        new_colr_cnst_a_keyp_b = copy.deepcopy(element["body"]["body"]["a"])
                        new_colr_cnst_a_keyp_c = copy.deepcopy(element["body"]["body"]["a"])
                        new_colr_cnst_a_keyp_d = copy.deepcopy(element["body"]["body"]["a"])
                        new_colr_cnst_a_keyp_a["body"]["keys"] = [None] * len(element["body"]["body"]["a"]["body"]["keys"])
                        new_colr_cnst_a_keyp_b["body"]["keys"] = [None] * len(element["body"]["body"]["a"]["body"]["keys"])
                        new_colr_cnst_a_keyp_c["body"]["keys"] = [None] * len(element["body"]["body"]["a"]["body"]["keys"])
                        new_colr_cnst_a_keyp_d["body"]["keys"] = [None] * len(element["body"]["body"]["a"]["body"]["keys"])
                        element["body"]["body"]["a"]["type"] = "CNST"
                        for i,key in enumerate(org_colr_mado_a_keye):
                            new_colr_cnst_a_keyp_a["body"]["keys"][i] = key[0]
                            new_colr_cnst_a_keyp_b["body"]["keys"][i] = key[1]
                            new_colr_cnst_a_keyp_c["body"]["keys"][i] = key[2]
                            new_colr_cnst_a_keyp_d["body"]["keys"][i] = key[3]
                        element["body"]["body"]["a"]["body"] = {
                            "a": new_colr_cnst_a_keyp_a,
                            "b": new_colr_cnst_a_keyp_b,
                            "c": new_colr_cnst_a_keyp_c,
                            "d": {
                                "type": "MULT",
                                "body": {
                                    "a": new_colr_cnst_a_keyp_d,
                                    "b": element["body"]["body"]["b"],
                                },
                            },
                        }
                    element["body"] = element["body"]["body"]["a"]

                if element["body"]["type"] == "MULT":
                    if (
                        element["body"]["body"]["a"]["type"] == "PULS"
                        and element["body"]["body"]["b"]["type"] == "KEYP"
                    ):
                        org_colr_mult_b_keyp = element["body"]["body"]["b"]["body"]["keys"]
                        new_colr_a_c_mult_b_keyp_a = copy.deepcopy(element["body"]["body"]["b"])
                        new_colr_a_c_mult_b_keyp_b = copy.deepcopy(element["body"]["body"]["b"])
                        new_colr_a_c_mult_b_keyp_c = copy.deepcopy(element["body"]["body"]["b"])
                        new_colr_a_c_mult_b_keyp_d = copy.deepcopy(element["body"]["body"]["b"])
                        num_keys = len(element["body"]["body"]["b"]["body"]["keys"])
                        new_colr_a_c_mult_b_keyp_a["body"]["keys"] = [None] * num_keys
                        new_colr_a_c_mult_b_keyp_b["body"]["keys"] = [None] * num_keys
                        new_colr_a_c_mult_b_keyp_c["body"]["keys"] = [None] * num_keys
                        new_colr_a_c_mult_b_keyp_d["body"]["keys"] = [None] * num_keys
                        for i, key in enumerate(org_colr_mult_b_keyp):
                            new_colr_a_c_mult_b_keyp_a["body"]["keys"][i] = key[0]
                            new_colr_a_c_mult_b_keyp_b["body"]["keys"][i] = key[1]
                            new_colr_a_c_mult_b_keyp_c["body"]["keys"][i] = key[2]
                            new_colr_a_c_mult_b_keyp_d["body"]["keys"][i] = key[3]

                        if (
                            element["body"]["body"]["a"]["body"]["c"]["type"] == "KEYP"
                            and element["body"]["body"]["a"]["body"]["d"]["type"] == "KEYP"
                        ):
                            org_colr_mult_a_c_keyp = element["body"]["body"]["a"]["body"]["c"]["body"]["keys"]
                            new_colr_a_c_mult_a_keyp_c_a = copy.deepcopy(element["body"]["body"]["a"]["body"]["c"])
                            new_colr_a_c_mult_a_keyp_c_b = copy.deepcopy(element["body"]["body"]["a"]["body"]["c"])
                            new_colr_a_c_mult_a_keyp_c_c = copy.deepcopy(element["body"]["body"]["a"]["body"]["c"])
                            new_colr_a_c_mult_a_keyp_c_d = copy.deepcopy(element["body"]["body"]["a"]["body"]["c"])
                            new_colr_a_c_mult_a_keyp_c_a["body"]["keys"] = [None] * len(org_colr_mult_a_c_keyp)
                            new_colr_a_c_mult_a_keyp_c_b["body"]["keys"] = [None] * len(org_colr_mult_a_c_keyp)
                            new_colr_a_c_mult_a_keyp_c_c["body"]["keys"] = [None] * len(org_colr_mult_a_c_keyp)
                            new_colr_a_c_mult_a_keyp_c_d["body"]["keys"] = [None] * len(org_colr_mult_a_c_keyp)
                            element["body"]["body"]["a"]["body"]["c"]["type"] = "CNST"
                            for i, key in enumerate(org_colr_mult_a_c_keyp):
                                new_colr_a_c_mult_a_keyp_c_a["body"]["keys"][i] = key[0]
                                new_colr_a_c_mult_a_keyp_c_b["body"]["keys"][i] = key[1]
                                new_colr_a_c_mult_a_keyp_c_c["body"]["keys"][i] = key[2]
                                new_colr_a_c_mult_a_keyp_c_d["body"]["keys"][i] = key[3]

                            element["body"]["body"]["a"]["body"]["c"]["body"] = {
                                "a": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_c_a,
                                        "b": new_colr_a_c_mult_b_keyp_a,
                                    },
                                },
                                "b": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_c_b,
                                        "b": new_colr_a_c_mult_b_keyp_b,
                                    },
                                },
                                "c": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_c_c,
                                        "b": new_colr_a_c_mult_b_keyp_c,
                                    },
                                },
                                "d": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_c_d,
                                        "b": new_colr_a_c_mult_b_keyp_d,
                                    },
                                },
                            }

                            # ================================================
                            org_colr_mult_a_d_keyp = element["body"]["body"]["a"]["body"]["d"]["body"]["keys"]
                            new_colr_a_c_mult_a_keyp_d_a = copy.deepcopy(element["body"]["body"]["a"]["body"]["d"])
                            new_colr_a_c_mult_a_keyp_d_b = copy.deepcopy(element["body"]["body"]["a"]["body"]["d"])
                            new_colr_a_c_mult_a_keyp_d_c = copy.deepcopy(element["body"]["body"]["a"]["body"]["d"])
                            new_colr_a_c_mult_a_keyp_d_d = copy.deepcopy(element["body"]["body"]["a"]["body"]["d"])
                            new_colr_a_c_mult_a_keyp_d_a["body"]["keys"] = [None] * len(org_colr_mult_a_d_keyp)
                            new_colr_a_c_mult_a_keyp_d_b["body"]["keys"] = [None] * len(org_colr_mult_a_d_keyp)
                            new_colr_a_c_mult_a_keyp_d_c["body"]["keys"] = [None] * len(org_colr_mult_a_d_keyp)
                            new_colr_a_c_mult_a_keyp_d_d["body"]["keys"] = [None] * len(org_colr_mult_a_d_keyp)
                            element["body"]["body"]["a"]["body"]["d"]["type"] = "CNST"
                            for i, key in enumerate(org_colr_mult_a_d_keyp):
                                new_colr_a_c_mult_a_keyp_d_a["body"]["keys"][i] = key[0]
                                new_colr_a_c_mult_a_keyp_d_b["body"]["keys"][i] = key[1]
                                new_colr_a_c_mult_a_keyp_d_c["body"]["keys"][i] = key[2]
                                new_colr_a_c_mult_a_keyp_d_d["body"]["keys"][i] = key[3]

                            element["body"]["body"]["a"]["body"]["d"]["body"] = {
                                "a": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_d_a,
                                        "b": new_colr_a_c_mult_b_keyp_a,
                                    },
                                },
                                "b": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_d_b,
                                        "b": new_colr_a_c_mult_b_keyp_b,
                                    },
                                },
                                "c": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_d_c,
                                        "b": new_colr_a_c_mult_b_keyp_c,
                                    },
                                },
                                "d": {
                                    "type": "MULT",
                                    "body": {
                                        "a": new_colr_a_c_mult_a_keyp_d_d,
                                        "b": new_colr_a_c_mult_b_keyp_d,
                                    },
                                },
                            }
                        else:
                            element["body"]["body"]["a"]["body"]["c"]["type"] = "CNST"
                            element["body"]["body"]["a"]["body"]["c"]["body"] = {
                                "a": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["c"]["body"]["a"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_a,
                                    },
                                },
                                "b": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["c"]["body"]["b"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_b,
                                    },
                                },
                                "c": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["c"]["body"]["c"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_c,
                                    },
                                },
                                "d": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["c"]["body"]["d"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_d,
                                    },
                                },
                            }
                            element["body"]["body"]["a"]["body"]["d"]["type"] = "CNST"
                            element["body"]["body"]["a"]["body"]["d"]["body"] = {
                                "a": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["d"]["body"]["a"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_a,
                                    },
                                },
                                "b": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["d"]["body"]["b"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_b,
                                    },
                                },
                                "c": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["d"]["body"]["c"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_c,
                                    },
                                },
                                "d": {
                                    "type": "MULT",
                                    "body": {
                                        "a": {
                                            "type": "CNST",
                                            "body": element["body"]["body"]["a"]["body"]["d"]["body"]["d"]["body"],
                                        },
                                        "b": new_colr_a_c_mult_b_keyp_d,
                                    },
                                },
                            }

                    element["body"] = element["body"]["body"]["a"]

            if element["type"] == "ADV1":
                if element["body"]["type"] == "KPIN":
                    element["body"] = element["body"]["body"]
    return data


def convert(data: Resource, details: AssetDetails, converter: AssetConverter):
    source_game = details.original_game

    if source_game.value < converter.target_game.value:
        upgrade(data, converter, source_game)
    elif source_game.value > converter.target_game.value:
        downgrade(data, converter, source_game)

    # convert asset references
    for element in data["elements"]:
        if element["type"] in ("TEXR", "TIND"):
            body = element["body"]["body"]
            if body is not None:
                if body["id"] is not None:
                    body["id"] = converter.convert_id(body["id"], source_game)

        if element["type"] == "KSSM" and element["body"]["magic"] != "NONE":
            for spawn in element["body"]["value"]["spawns"]:
                for t in spawn["v2"]:
                    t["id"] = converter.convert_id(t["id"], source_game)

        if element["type"] in ("SSWH", "PMDL", "SELC", "IDTS", "ICTS", "IITS"):
            body = element["body"]
            if body["body"] is not None and source_game.is_valid_asset_id(body["body"]):
                body["body"] = converter.convert_id(body["body"], source_game)

    return data


class PARTConverter(dict):
    def __missing__(self, key: Game):
        if isinstance(key, Game):
            return convert
        else:
            raise KeyError(key)


CONVERTERS = PARTConverter()
