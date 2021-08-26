from discord import Message, Embed

from os import path
import discord
import requests
import matplotlib.pyplot as plt
import pandas as pd


def saveGraphic(*config, url: str):
    plt.plot(config["x"], config["y"])
    plt.xlabel(config["xlabel"])
    plt.ylabel(config["ylabel"])
    plt.savefig(url)
    plt.close()


def parse_data(code: str = "PER"):
    data = requests.get(
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

    saveGraphic(config, "assets/images/" + code + ".png")


async def graphic_cmds(message: Message, _):
    content: str = message.content
    command = content.split(" ")
    if len(command) == 1:
        return await message.channel.send("COUNTRY CODE IS REQUIRED \n $graphic PER")

    code = command[1].upper()
    if len(code) != 3:
        return await message.channel.send("COUNTRY CODE IS INVALID")

    invalid_code = requests.get(
        "https://restcountries.eu/rest/v2/alpha/" + code).status_code == 404
    if invalid_code:
        return await message.channel.send("COUNTRY CODE IS INVALID")
    workdir = "assets/images/" + code + ".png"
    if not path.exists(workdir):
        parse_data(code)

    image = discord.File(workdir)
    embed = Embed(title=f"Covid19 - {code} | TOTAL CASES")
    embed.set_image(
        url=f"attachment://{code}.png"
    )
    await message.channel.send(embed=embed, file=image)
