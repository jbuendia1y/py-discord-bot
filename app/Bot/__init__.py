from discord.ext import commands
from os import listdir

cogs = []

for item in listdir("Bot/commands/"):
    if not item.__contains__("__"):
        cogs.append(item.replace(".py", ""))

bot = commands.Bot(command_prefix="$")
for file in cogs:
    bot.load_extension("Bot.commands." + file)


@bot.add_listener
async def on_ready():
    print("BOT READY")
