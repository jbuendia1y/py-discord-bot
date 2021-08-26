from models.entities import Enemy
from models.player import Player
from pydantic import BaseModel


class Winner(BaseModel):
    id: int
    name: str = "Winner name"


class Pvp(BaseModel):
    player1_id: int
    player2_id: int


def battle_pvp(player1: Player, player2: Player):
    while player1.stats.current.hp > 0 and player2.stats.current.hp > 0:
        player1.catch_damage(player2.dispatch_damage())
        if player1.stats.current.hp <= 0 and player2.stats.current.hp <= 0:
            break
        player2.catch_damage(player1.dispatch_damage())
    if player1.stats.current.hp > player2.stats.current.hp:
        return player1
    else:
        return player2


def hunt(player1: Player, enemy: Enemy):
    while player1.stats.current.hp > 0 and enemy.stats.current.hp > 0:
        enemy.catch_damage(player1.dispatch_damage())
        if enemy.stats.current.hp <= 0 and player1.stats.current.hp <= 0:
            break
        player1.catch_damage(enemy.dispatch_damage())
    if player1.stats.current.hp > enemy.stats.current.hp:
        return player1
    else:
        return enemy
