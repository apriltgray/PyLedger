from classes.game import Game


class PC(Game):
    consoles = ("PC",)

    def get_logo(self) -> str:
        return "https://github.com/apriltgray/PyLedger/blob/main/assets/pc.png?raw=true"
