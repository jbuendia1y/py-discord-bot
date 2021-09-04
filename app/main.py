from os import getenv

from src import bot

if __name__ == "__main__":
    bot.run(getenv("BOT_TOKEN"))
