from urllib import parse
from helpers import api


def get_anime_by_name(anime: str = None) -> list:
    if anime == None:
        return []
    if len(anime.strip()) == 0:
        return []
    query = parse.urlencode({"filter[text]": anime})
    url = "https://kitsu.io/api/edge/anime?" + query + "&page[limit]=1"
    data = api.get(url).json()["data"]
    return data
