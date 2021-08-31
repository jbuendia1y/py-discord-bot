from discord import Embed
from discord.ext import commands
from discord.message import Message

from urllib import parse
import requests

from models.anime import AnimeModel


class Anime(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.base_url = "https://kitsu.io/api/edge/anime?"

    def get_anime_embed(self, anime: AnimeModel) -> Embed:
        embed = Embed(title=anime.title)
        embed.set_image(url=anime.image)
        embed.description = anime.synopsis
        embed.add_field(name="Emission and Ending",
                        value=f"{anime.emission} **/** {anime.end_emission}")
        embed.add_field(name="Favorites", value=":star: " +
                        str(anime.favorites))
        return embed

    @commands.command(name="anime")
    async def get_anime(self, ctx: commands.Context):
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
        print(message.author.id)
        await message.channel.send(embed=self.get_anime_embed(AnimeModel(data[0]["attributes"])))


def setup(bot: commands.Bot):
    bot.add_cog(Anime(bot))
