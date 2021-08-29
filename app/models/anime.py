from dataclasses import dataclass
from discord import Embed


@dataclass
class AnimeModel:
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
