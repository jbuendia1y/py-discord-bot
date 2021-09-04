from discord.ext import commands
from discord import Embed
from discord.message import Message

from src.modules.quotes import get_quote
from src.models.quote import QuoteModel


class Quotes_cmd(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def make_embed_quote(self, data: QuoteModel):
        embed = Embed()
        embed.title = "Quote"
        embed.description = data.text
        embed.set_author(name=data.author, url="", icon_url="")

    @commands.command(name="quote")
    async def quote(self, ctx: commands.Context, type_quote: str):
        message: Message = ctx.message
        type_quote = type_quote.strip().lower()

        if len(type_quote) == 0:
            return await message.channel.send(embed=self.make_embed_quote(get_quote()))

        if type_quote != "today" or type_quote != "random":
            return await message.channel.send("Wrong parametre")

        await message.channel.send(embed=self.make_embed_quote(get_quote(type_quote)))


def setup(bot: commands.Bot):
    bot.add_cog(Quotes_cmd(bot))
