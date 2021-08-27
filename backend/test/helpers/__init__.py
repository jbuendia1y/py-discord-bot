from config.db import conn

player_attributes = {
    "stats": {
        "max": {
            "hp": 100,
            "armor": 0,
            "attack": 10
        },
        "current": {
            "hp": 25,
            "armor": 0,
            "attack": 10
        },
        "base": {
            "hp": 100,
            "armor": 0,
            "attack": 10
        }
    },
    "inventory": {
        "consumables": [],
        "items": []
    },
    "equipped": {},
    "progress": {
        "current": {
            "xp": 0,
            "floor": 1
        },
        "max": {
            "xp": 0,
            "floor": 1
        }
    }
}

players_for_test = [
    {
        "name": "Joaquín",
        "id": 1,
        **player_attributes
    },
    {
        "name": "testing_player",
        "id": 2,
        **player_attributes
    }
]


def reset_players():
    # player 1 == id 1 -- player 2 == id 2
    conn.players.delete_many({})
    conn.players.insert_many(players_for_test)
