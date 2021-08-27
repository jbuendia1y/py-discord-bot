from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from config.db import conn

from helpers import random_enemy

from models.entities import Enemy
from models.battles import Pvp, Winner, battle_pvp, hunt
from models.player import Player

battlesRouter = APIRouter(prefix="/battles")


@battlesRouter.post("/pvp", response_model=Winner)
async def pvp(pvp: Pvp):
    id1 = pvp.player1_id
    id2 = pvp.player2_id
    player1_dict = conn.players.find_one({"id": id1})
    player2_dict = conn.players.find_one({"id": id2})

    player1 = Player(**player1_dict)
    player2 = Player(**player2_dict)

    return jsonable_encoder(battle_pvp(player1, player2))


@battlesRouter.post("/hunt", response_model=Player)
async def player_hunt(id: int):
    player = Player(**conn.players.find_one({"id": id}, {"_id": 0}))
    hunt(player, Enemy(**random_enemy(player.progress.current.floor)))

    conn.players.update_one(
        {"id": player.id},
        {"$set": {"stats": jsonable_encoder(player.stats)}},
        bypass_document_validation=True)

    return jsonable_encoder(player)
