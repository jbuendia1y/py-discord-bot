from helpers.api import Api

from .enemy import Enemy
from .stats import Stats
from .player import Player

import math
from random import choice


def fetch_enemys():
    data: list = Api().get("/enemys")
    enemys: list[Enemy] = []

    [enemys.append(Enemy(item["name"], Stats(**item["stats"])))
     for item in data]

    return enemys


class Hunt:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.enemy = choice(fetch_enemys())

    def get_drops(self):
        floor = self.player.progress.floor
        e = math.exp(floor)
        xp = round(e / (floor**2) * 10)
        # fetch items of enemy
        # Should return items and xp
        return (xp)

    def start_hunt(self):
        while self.player.stats.hp >= 0 or self.enemy.stats.hp >= 0:
            attack = self.player.attack()
            self.enemy.catch_damage(attack)
            ok1 = self.verify_hp()

            if ok1:
                return ok1

            attack = self.enemy.attack()
            self.player.catch_damage(attack)
        return self.verify_hp()

    def verify_hp(self):
        player_hp = self.player.stats.hp
        enemy_hp = self.enemy.stats.hp
        if player_hp <= 0 or enemy_hp <= 0:
            if player_hp < enemy_hp:
                return self.enemy
            elif player_hp > enemy_hp:
                return self.player
        return None
