from discord import Message
from helpers import parser

PE = "PE"
US = "US"

pages = {
    PE: "https://elcomercio.pe/",
    US: ""
}


async def news_cmds(message: Message,_):
    soup = parser("https://elcomercio.pe/")

    main_article = soup.find("div", {"role": "main"}).find("article")
    link = main_article.findAll("a")[1]
    await message.channel.send("https://elcomercio.pe" + link.get("href"))
