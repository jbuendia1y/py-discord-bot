from helpers import api
from src.models.quote import QuoteModel


def get_quote(type_quote: str = "random") -> QuoteModel:
    if type_quote == None:
        raise Exception("Missing parametre")
    type_quote = type_quote.strip().lower()
    if type_quote != "today" and type_quote != "random":
        raise Exception("Wrong parametre")
    url = "https://zenquotes.io/api/" + type_quote
    data = api.get(url).json()[0]

    return QuoteModel(data["q"], data["a"])
