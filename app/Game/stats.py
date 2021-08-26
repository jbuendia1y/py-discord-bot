from dataclasses import dataclass
from .items import Equipment


@dataclass
class Current_stats:
    hp: int
    armor: int
    attack: int


class Stats:
    hp: int
    armor: int
    attack: int

    current: Current_stats

    lvl: int
    currently_hp: int = None

    def __init__(self, hp: int, armor: int, attack: int, currently_hp: int, lvl: int = None) -> None:
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.currently_hp = currently_hp
        self.lvl = lvl or 1

        self.current = Current_stats(hp, armor, attack)

    def calculate_current_stats(self, boosts: tuple):
        if len(boosts) == 0:
            return None
        boost: Equipment
        for boost in boosts:
            if not boost:
                continue
            stat, amount = boost.get_stat()
            value = getattr(self.current, stat)
            setattr(self.current, stat, value + (amount * 100))
