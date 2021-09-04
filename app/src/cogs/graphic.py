from discord import Message, Embed, File
from discord.ext import commands
from discord.ext.commands import Context

from helpers import api

from os import path
import matplotlib.pyplot as plt
import pandas as pd


class Graphics(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def __saveGraphic(self, *config, url: str):
        plt.plot(config["x"], config["y"])
        plt.xlabel(config["xlabel"])
        plt.ylabel(config["ylabel"])
        plt.savefig(url)
        plt.close()

    def __parse_data(self, code: str = "PER"):
        data = api.get(
            "https://covid.ourworldindata.org/data/owid-covid-data.json").json()

        dataFrame = pd.DataFrame.from_dict(data[code]["data"])
        total_cases = dataFrame["total_cases"].tail(15)
        dates = dataFrame["date"].tail(15)
        config = {
            "x": dates,
            "y": total_cases,
            "xlabel": "dates",
            "ylabel": "Total Cases"
        }

        self.__saveGraphic(config, "assets/images/" + code + ".png")

    @commands.command(name="graphic")
    async def get_graphic(self, ctx: Context):
        message: Message = ctx.message
        content: str = message.content
        command = content.split(" ")
        if len(command) == 1:
            return await message.channel.send("COUNTRY CODE IS REQUIRED \n $graphic PER")

        code = command[1].upper()
        if len(code) != 3:
            return await message.channel.send("COUNTRY CODE IS INVALID")

        invalid_code = api.get(
            "https://restcountries.eu/rest/v2/alpha/" + code).status_code == 404
        if invalid_code:
            return await message.channel.send("COUNTRY CODE IS INVALID")
        workdir = "assets/images/" + code + ".png"
        if not path.exists(workdir):
            self.__parse_data(code)

        image = File(workdir)
        embed = Embed(title=f"Covid19 - {code} | TOTAL CASES")
        embed.set_image(
            url=f"attachment://{code}.png"
        )
        await message.channel.send(embed=embed, file=image)


def setup(bot: commands.Bot):
    bot.add_cog(Graphics(bot))
