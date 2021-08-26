from discord import Client
from os import getenv, mkdir

from Bot import Bot
from scripts.reset import reset

if __name__ == "__main__":
    try:
        mkdir("assets")
    except FileExistsError:
        print("File already exist")
    if getenv("PY_ENV") == "production":
        reset()
    bot = Bot(Client())
    bot.run_bot()
