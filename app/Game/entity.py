from .stats import Stats


class Entity:
    name: str
    stats: Stats

    def __init__(self, name: str = "", stats: Stats = None) -> None:
        self.name = name
        self.stats = stats or Stats(100, 0, 10, 100)

    def catch_damage(self, attack: int):
        hp = self.stats.hp
        self.stats.hp = hp - attack

    def attack(self):
        return self.stats.attack
