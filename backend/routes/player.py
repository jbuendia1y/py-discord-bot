from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from models import Player
from config.db import conn

player = APIRouter(prefix="/player")


@player.get("/{id}", response_model=Player)
async def get_player(id: int):
    return conn.players.find_one({"id": id}, {"_id": 0})


@player.post("/", response_model=Player)
async def create_player(player: Player):
    id = conn.players.insert_one(jsonable_encoder(dict(player))).inserted_id
    player_added = conn.players.find_one({"_id": id}, {"_id": 0})
    return player_added


@player.put("/{id}", response_model=int)
async def update_player(id: int):
    conn.players.update_one({"id": id})
    return id
