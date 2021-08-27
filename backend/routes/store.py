from fastapi import APIRouter
from config.db import conn

from models.store import Store, Store_item, List

storeRouter = APIRouter(prefix="/store")


@storeRouter.get("/")
async def get_store() -> Store:
    store = conn.store.find_one({}, {"_id": 0})
    return store


@storeRouter.get("/{lvl}")
async def get_by_lvl(lvl: str) -> List[Store_item]:
    type_lvl = lvl.lower()
    if type_lvl != "basic" and type_lvl != "intermediate" and type_lvl != "advanced":
        return "Wrong parameter"
    store = conn.store.find_one({"type": type_lvl}, {"_id": 0})

    return store
