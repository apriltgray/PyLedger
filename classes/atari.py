from classes.game import Game


class Atari(Game):
    consoles = ("Atari", "Atari 2600")

    def get_logo(self) -> str:
        return "https://github.com/apriltgray/PyLedger/blob/main/assets/atari.png?raw=true"
