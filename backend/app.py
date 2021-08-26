from fastapi import FastAPI, Request

from routes.player import player
from routes.store import storeRouter
from routes.battles import battlesRouter

app = FastAPI()

app.include_router(player)
app.include_router(storeRouter)
app.include_router(battlesRouter)
