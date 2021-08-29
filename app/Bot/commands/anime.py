from discord.ext import commands
from discord.ext.commands.context import Context
from discord.message import Message

from urllib import parse
import requests

from models.anime import AnimeModel


class Anime(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.base_url = "https://kitsu.io/api/edge/anime?"

    @commands.command(name="anime")
    async def get_anime(self, ctx: Context):
        message: Message = ctx.message
        params: list = message.content.split(" ")
        if len(params) == 1:
            return await message.channel.send("The command need a param")
        params.pop(0)
        query = parse.urlencode({"filter[text]": " ".join(params)})
        url = self.base_url + query + "&page[limit]=1"

        data = requests.get(url).json()["data"]
        if len(data) == 0:
            return await message.channel.send("Anime not Found :face_with_monocle:")
        anime = AnimeModel(data[0]["attributes"])

        await message.channel.send(embed=anime.get_embed())


def setup(bot: commands.Bot):
    bot.add_cog(Anime(bot))
