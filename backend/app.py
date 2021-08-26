from fastapi import FastAPI

from routes.player import player
from routes.store import storeRouter
from routes.battles import battlesRouter
from routes.enemys import enemysRouter

app = FastAPI()

app.include_router(player)
app.include_router(storeRouter)
app.include_router(battlesRouter)
app.include_router(enemysRouter)
