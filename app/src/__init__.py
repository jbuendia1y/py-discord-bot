from discord.ext import commands
import re
from os import listdir

cogsList = []

for item in listdir("src/cogs/"):
    if len(re.findall("__", item)) == 0:
        cogsList.append(item.replace(".py", ""))


bot = commands.Bot(command_prefix="$")
for file in cogsList:
    bot.load_extension("src.cogs." + file)


@bot.command()
async def reload(ctx):
    for file in cogsList:
        bot.reload_extension("src.cogs." + file)


@bot.add_listener
async def on_ready():
    print("BOT READY")
