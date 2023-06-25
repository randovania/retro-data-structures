class UnsupportedTargetGame(Exception):
    def __init__(self, source_game, target_game):
        super().__init__(f"Unable to convert to {target_game} with {source_game} as source")


class UnsupportedSourceGame(Exception):
    def __init__(self, source_game):
        super().__init__(f"Game {source_game} is unsupported for conversion")
