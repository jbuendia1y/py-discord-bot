from discord.ext import commands
from discord import Embed

import requests

from models.quote import QuoteModel


class Quotes_cmd(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def get_quote(self, type_quote: str = "random"):
        url = "https://zenquotes.io/api/" + type_quote
        data = requests.get(url).json()[0]

        quote = QuoteModel(data["q"], data["a"])
        embed = Embed()
        embed.title = "Quote " + type_quote
        embed.description = quote.text
        embed.set_author(name=quote.author, url="", icon_url="")

        return embed

    @commands.command(name="quote")
    async def quote(self, ctx: commands.Context):
        message = ctx.message
        content: str = message.content
        text_message = content.split(" ")

        quote_embed = None
        if len(text_message) == 2:
            if text_message[1] == "today":
                quote_embed = self.get_quote("today")
        if quote_embed != None:
            return await message.channel.send(embed=quote_embed)
        await message.channel.send(embed=self.get_quote())


def setup(bot: commands.Bot):
    bot.add_cog(Quotes_cmd(bot))
