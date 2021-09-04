from helpers import api
from Game import Player


def get_player(id) -> Player:
    player_data = api.get(f"/player/{str(id)}").json()
    return Player(**player_data)


def player_hunt(id) -> Player:
    player_data = api.post(f"/battles/hunt?id={str(id)}").json()
    return Player(**player_data)


def init_pvp(id1, id2) -> str:
    data_to_send = {"player1_id": id1,
                    "player2_id": id2}
    return api.post("/battles/pvp", data_to_send).json()["name"]
