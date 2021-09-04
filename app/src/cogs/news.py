from discord.ext import commands
from helpers import parser


class News(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="news")
    async def get_news(self, ctx: commands.Context):
        soup = parser("https://elcomercio.pe/")

        main_article = soup.find("div", {"role": "main"}).find("article")
        link = main_article.findAll("a")[1]
        await ctx.message.channel.send("https://elcomercio.pe" + link.get("href"))


def setup(bot: commands.Bot):
    bot.add_cog(News(bot))
