from re import M
from fastapi import APIRouter
from typing import List
from helpers import random_enemy

from config.db import conn
from models.entities import Enemy

enemysRouter = APIRouter(prefix="/enemys")


@enemysRouter.get("/{floor}", response_model=List[Enemy])
async def enemys_by_floor(floor: int):
    data = conn.enemys.find_one({"floor": floor}, {"_id": 0})
    return data["enemys"]


@enemysRouter.get("/{floor}/random", response_model=Enemy)
async def enemys_by_floor(floor: int):
    return random_enemy(floor)
