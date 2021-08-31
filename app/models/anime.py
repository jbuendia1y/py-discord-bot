from dataclasses import dataclass


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
