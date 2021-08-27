from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from config.db import conn

from models.store import Store, Store_item, List

storeRouter = APIRouter(prefix="/store")


@storeRouter.get("/", response_model=List[Store])
async def get_store() -> List[Store]:
    store = [item for item in conn.store.find({}, {"_id": 0})]
    return store


@storeRouter.get("/{lvl}", response_model=List[Store_item])
async def get_by_lvl(lvl: str) -> List[Store_item]:
    type_lvl = lvl.lower()
    if type_lvl != "basic" and type_lvl != "intermediate" and type_lvl != "advanced":
        raise HTTPException(status_code=422, detail="Wrong parameter")
    store = conn.store.find_one({"type": type_lvl}, {"_id": 0})

    return store["items"]
