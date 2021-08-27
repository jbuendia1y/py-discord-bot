from config.db import conn
from random import choice


def random_enemy(floor: int):
    data = conn.enemys.find_one({"floor": floor}, {"_id": 0})
    enemys: list = data["enemys"]
    return choice(enemys)
