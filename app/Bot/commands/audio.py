from discord import Message, VoiceClient, VoiceState, VoiceChannel, FFmpegPCMAudio, VoiceProtocol
from discord.ext import commands
from discord.ext.commands import Context


class Audio_cmds(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command
    async def connect(self, ctx: Context):
        message: Message = ctx.message
        voice: VoiceState = message.author.voice
        voice_channel: VoiceChannel = voice.channel
        if voice == None:
            return await message.channel.send("should enter to a channel voice")

        protocol: VoiceClient = await voice_channel.connect()
        try:
            protocol.play(FFmpegPCMAudio("audio.mp3"),
                          after=lambda: print("done"))
        except:
            await message.channel.send("Cannot play audio")

    async def disconnect(self, ctx: Context):
        message: Message = ctx.message
        voice: VoiceState = message.author.voice
        if voice == None:
            return await message.channel.send("should enter to a channel voice")

        voice_client: VoiceProtocol
        for voice_client in ctx.bot.voice_clients:
            if voice.channel.id == voice_client.channel.id:
                await message.channel.send(":hand_splayed: Leave")
                return await voice_client.disconnect()


def setup(bot: commands.Bot):
    bot.add_cog(Audio_cmds(bot))
