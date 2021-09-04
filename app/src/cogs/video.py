from discord import Message
from discord.ext import commands

from src.modules.video import get_youtube_video


class Video_cmds(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="search")
    async def search_video(self, ctx: commands.Context, *video_name):
        message: Message = ctx.message
        if len(video_name) == 0:
            return await message.channel.send("Command need a parametre")

        await message.channel.send(get_youtube_video(" ".join(video_name)))


def setup(bot: commands.Bot):
    bot.add_cog(Video_cmds(bot))
