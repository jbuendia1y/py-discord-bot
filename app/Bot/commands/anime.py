from discord import Message, Client, Embed
from urllib import parse
import requests
from dataclasses import dataclass

from models import CommandModel


@dataclass
class Anime:
    title: str
    synopsis: str
    favorites: int
    emission: str
    end_emission: str
    image: str

    def __init__(self, data) -> None:
        self.title = data["canonicalTitle"]
        self.synopsis = data["synopsis"]
        self.synopsis = self.synopsis[0:500] + "..."

        self.favorites = data["favoritesCount"]
        self.emission = data["startDate"]
        self.end_emission = data["endDate"]
        self.image = data["posterImage"]["original"]

    def get_embed(self) -> Embed:
        embed = Embed(title=self.title)
        embed.set_image(url=self.image)
        embed.description = self.synopsis
        embed.add_field(name="Emission and Ending",
                        value=f"{self.emission} **/** {self.end_emission}")
        embed.add_field(name="Favorites", value=":star: " +
                        str(self.favorites))
        return embed


class Anime_cmds:
    base_url: str

    def __init__(self) -> None:
        self.base_url = "https://kitsu.io/api/edge/anime?"

    async def get_anime(self, message: Message, _):
        params: list = message.content.split(" ")
        if len(params) == 1:
            return await message.channel.send("The command need a param")
        params.pop(0)
        query = parse.urlencode({"filter[text]": " ".join(params)})
        url = self.base_url + query + "&page[limit]=1"

        data = requests.get(url).json()["data"]
        if len(data) == 0:
            return await message.channel.send("Anime not Found :face_with_monocle:")
        anime = Anime(data[0]["attributes"])

        await message.channel.send(embed=anime.get_embed())

    async def get_character(self, message: Message, client: Client):
        pass
