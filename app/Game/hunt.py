from helpers import api

from .enemy import Enemy
from .player import Player


def fetch_random_enemy(floor: int):
    data = api.get("/enemys/"+str(floor)+"/random").json()
    return Enemy(**data)


class Hunt:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.enemy = fetch_random_enemy(player.progress.current.floor)

    def start_hunt(self):
        while self.player.stats.current.hp > 0 or self.enemy.stats.current.hp > 0:
            self.enemy.catch_damage(self.player.attack())

            if self.player.stats.current.hp <= 0 or self.enemy.stats.current.hp <= 0:
                break
            self.player.catch_damage(self.enemy.attack())
        return self.get_winner()

    def get_winner(self):
        player_hp = self.player.stats.current.hp
        enemy_hp = self.enemy.stats.current.hp
        if player_hp < enemy_hp:
            return self.enemy
        else:
            return self.player
