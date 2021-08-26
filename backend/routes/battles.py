from fastapi import APIRouter
from config.db import conn

from models.battles import Pvp
from models.player import Player

battlesRouter = APIRouter(prefix="/battles")


@battlesRouter.post("/pvp")
async def pvp(pvp: Pvp):
    id1 = pvp.player1_id
    id2 = pvp.player2_id
    player1_dict = conn.players.find_one({"id": id1})
    player2_dict = conn.players.find_one({"id": id2})

    player1 = Player(**player1_dict)
    player2 = Player(**player2_dict)
    print(player1)
    print(player2)
    return [player1, player2]
