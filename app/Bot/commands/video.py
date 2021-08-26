from discord import Message

from urllib import parse, request
import re


class Video_cmds:
    def __init__(self) -> None:
        pass

    async def search(self, message: Message, _):
        params: list = message.content.split(" ")
        if len(params) == 1:
            return await message.channel.send("PLEASE INSERT QUERY")

        params.pop(0)
        query = parse.urlencode({"search_query": " ".join(params)})
        url = "https://www.youtube.com/results?" + query

        html_content = request.urlopen(url)
        regex = 'url":"/watch\?v=(.{11})'
        # Links in tag(script) on Html_Content
        video_id_list = re.findall(regex, html_content.read().decode())
        await message.channel.send("https://youtube.com/watch?v=" + video_id_list[0])
