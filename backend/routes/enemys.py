from fastapi import APIRouter
from typing import List, Dict
from random import choice

from config.db import conn
from models.entities import Enemy

enemysRouter = APIRouter(prefix="/enemys")


@enemysRouter.get("/{floor}", response_model=List[Enemy])
async def enemys_by_floor(floor: int):
    data = conn.enemys.find_one({"floor": floor}, {"_id": 0})
    return data["enemys"]


@enemysRouter.get("/{floor}/random", response_model=Enemy)
async def enemys_by_floor(floor: int):
    data = conn.enemys.find_one({"floor": floor}, {"_id": 0})
    enemys: list = data["enemys"]
    return choice(enemys)
