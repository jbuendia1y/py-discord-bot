from discord import Message, Embed
import requests


class Quote:
    def __init__(self, text: str, author: str) -> None:
        self.text = text
        self.author = author


def get_quote(type_quote: str = "random"):
    url = "https://zenquotes.io/api/" + type_quote
    data = requests.get(url).json()[0]

    quote = Quote(data["q"], data["a"])
    embed = Embed()
    embed.title = "Quote " + type_quote
    embed.description = quote.text
    embed.set_author(name=quote.author, url="", icon_url="")

    return embed


async def quotes_cmds(message: Message, _):
    content: str = message.content
    text_message = content.split(" ")

    quote_embed = None
    if len(text_message) == 2:
        if text_message[1] == "today":
            quote_embed = get_quote("today")
    if quote_embed != None:
        return await message.channel.send(embed=quote_embed)
    await message.channel.send(embed=get_quote())
