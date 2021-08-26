from discord import Message, Client
from discord.channel import TextChannel


class Server_cmds:
    def __init__(self) -> None:
        pass

    async def delete_messages(self, message: Message, client: Client):
        channel = message.channel
        if isinstance(channel, TextChannel):
            msgs = client.cached_messages
            await channel.delete_messages(msgs)
