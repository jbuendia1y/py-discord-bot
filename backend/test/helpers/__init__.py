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
        },
        "lvl": 1
    }
}

players_for_test = [
    {
        "name": "Joaquín",
        "id": "123456",
        **player_attributes
    },
    {
        "name": "testing_player",
        "id": "234567",
        **player_attributes
    }
]

store_for_test = [
    {
        "type": "basic",
        "items": [
            {
                "name": "Basic Armor",
                "boost": {
                    "amount": 0.1,
                    "stat": "armor"
                },
                "cost": 100
            },
            {
                "name": "Basic Sword",
                "boost": {
                    "amount": 0.05,
                    "stat": "attack"
                },
                "cost": 75
            },
            {
                "name": "Basic Horse",
                "boost": {
                    "amount": 0.15,
                    "stat": "hp"
                },
                "cost": 1000
            }
        ]
    }, {
        "type": "intermediate",
        "items": [
            {
                "name": "Intermediate Armor",
                "boost": {
                    "amount": 0.2,
                    "stat": "armor"
                },
                "cost": 250
            },
            {
                "name": "Intermediate Sword",
                "boost": {
                    "amount": 0.08,
                    "stat": "attack"
                },
                "cost": 225
            },
            {
                "name": "Intermediate Horse",
                "boost": {
                    "amount": 0.25,
                    "stat": "hp"
                },
                "cost": 10000
            }
        ]
    },
    {
        "type": "advanced",
        "items": [
            {
                "name": "Advanced Armor",
                "boost": {
                    "amount": 0.5,
                    "stat": "armor"
                },
                "cost": 500
            },
            {
                "name": "Advanced Sword",
                "boost": {
                    "amount": 0.15,
                    "stat": "attack"
                },
                "cost": 445
            },
            {
                "name": "Advanced Horse",
                "boost": {
                    "amount": 0.5,
                    "stat": "hp"
                },
                "cost": 100000
            }
        ]
    }
]

enemys_for_test = [
    {
        "floor": 1,
        "enemys": [
            {
                "name": "Goblin",
                "stats": {
                    "current": {
                        "hp": 60,
                        "armor": 1,
                        "attack": 10
                    },
                    "max": {
                        "armor": 1,
                        "attack": 10,
                        "hp": 60
                    }
                }
            },
            {
                "name": "Slime",
                "stats": {
                    "current": {
                        "hp": 15,
                        "armor": 1,
                        "attack": 5,
                    },
                    "max": {
                        "hp": 15,
                        "armor": 1,
                        "attack": 5,
                    }
                }
            },
            {
                "name": "Skeleton",
                "stats": {
                    "current": {
                        "hp": 45,
                        "armor": 10,
                        "attack": 15,
                    },
                    "max": {
                        "hp": 45,
                        "armor": 10,
                        "attack": 15,
                    }
                }
            },
            {
                "name": "Wolf",
                "stats": {
                    "current": {
                        "hp": 70,
                        "armor": 15,
                        "attack": 15,
                    },
                    "max": {
                        "hp": 70,
                        "armor": 15,
                        "attack": 15,
                    }
                }
            },
            {
                "name": "Wild Pig",
                "stats": {
                    "current": {
                        "hp": 25,
                        "armor": 12,
                        "attack": 15,
                    },
                    "max": {
                        "hp": 25,
                        "armor": 12,
                        "attack": 15,
                    }
                }
            },
        ]
    }, {
        "floor": 2,
        "enemys": [
            {
                "name": "Orc",
                "stats": {
                    "current": {
                        "hp": 85,
                        "armor": 12,
                        "attack": 13,
                    },
                    "max": {
                        "hp": 85,
                        "armor": 12,
                        "attack": 13,
                    }
                }
            },
            {
                "name": "Troll",
                "stats": {
                    "current": {
                        "hp": 50,
                        "armor": 15,
                        "attack": 20,
                    },
                    "max": {
                        "hp": 50,
                        "armor": 15,
                        "attack": 20,
                    }
                }
            }
        ]
    }
]


def reset_players():
    # player 1 == id 1 -- player 2 == id 2
    conn.players.delete_many({})
    conn.players.insert_many(players_for_test)


def reset_store():
    conn.store.delete_many({})
    conn.store.insert_many(store_for_test)


def reset_enemys():
    conn.enemys.delete_many({})
    conn.enemys.insert_many(enemys_for_test)


def reset_db_for_testing():
    reset_players()
    reset_store()
    reset_enemys()
