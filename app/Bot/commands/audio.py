from discord import Message, VoiceState, VoiceClient, FFmpegPCMAudio, Client
from discord.channel import VoiceChannel
from discord.voice_client import VoiceProtocol


class Audio_cmds:
    def __init__(self) -> None:
        pass

    async def connect(self, message: Message, _):
        voice: VoiceState = message.author.voice
        voice_channel: VoiceChannel = voice.channel
        if voice == None:
            return await message.channel.send("should enter to a channel voice")

        protocol: VoiceClient = await voice_channel.connect()
        try:
            protocol.play(FFmpegPCMAudio("gaaa.mp3"),
                          after=lambda: print("done"))
        except:
            await message.channel.send("Cannot play audio")

    async def disconnect(self, message: Message, client: Client):
        voice: VoiceState = message.author.voice
        if voice == None:
            return await message.channel.send("should enter to a channel voice")

        voice_client: VoiceProtocol
        for voice_client in client.voice_clients:
            if voice.channel.id == voice_client.channel.id:
                await message.channel.send(":hand_splayed: Leave")
                return await voice_client.disconnect()
