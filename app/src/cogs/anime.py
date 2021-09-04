from discord import Embed
from discord.ext import commands
from discord.message import Message

from src.models.anime import AnimeModel
from src.modules.anime import get_anime_by_name


class Anime(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.base_url = "https://kitsu.io/api/edge/anime?"

    def __get_anime_embed(self, anime: AnimeModel) -> Embed:
        embed = Embed(title=anime.title)
        embed.set_image(url=anime.image)
        embed.description = anime.synopsis
        embed.add_field(name="Emission and Ending",
                        value=f"{anime.emission} **/** {anime.end_emission}")
        embed.add_field(name="Favorites", value=":star: " +
                        str(anime.favorites))
        return embed

    @commands.command(name="anime")
    async def get_anime(self, ctx: commands.Context, *anime_name):
        message: Message = ctx.message
        if len(anime_name) == 0:
            return await message.channel.send("The command need a param")
        data = get_anime_by_name(" ".join(anime_name).strip())
        if len(data) == 0:
            return await message.channel.send("Anime not Found :face_with_monocle:")
        await message.channel.send(embed=self.__get_anime_embed(AnimeModel(data[0]["attributes"])))


def setup(bot: commands.Bot):
    bot.add_cog(Anime(bot))
