from os import getenv, mkdir

from Bot import bot
from scripts.reset import reset

if __name__ == "__main__":
    try:
        mkdir("assets")
    except FileExistsError:
        print("File already exist")
    if getenv("PY_ENV") == "production":
        reset()
    bot.run(getenv("BOT_TOKEN"))
