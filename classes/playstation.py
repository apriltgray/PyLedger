from classes.game import Game


class Playstation(Game):
    consoles = ("PlayStation 1", "PlayStation 2",
                "PlayStation 3", "PlayStation 4", "PlayStation 5")

    def get_logo(self) -> str:
        return "https://photobucket.com/share/6488a891-4537-4f7e-9104-974244e90135"
