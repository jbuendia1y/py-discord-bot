from discord.ext import commands

from urllib import parse, request
import re


class Video_cmds(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="search")
    async def search_video(self, ctx: commands.Context):
        message = ctx.message
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


def setup(bot: commands.Bot):
    bot.add_cog(Video_cmds(bot))
