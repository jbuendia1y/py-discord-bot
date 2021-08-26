from discord import Client, Message
from ..commands import commands


def on_message(client: Client):
    @client.event
    async def on_message(message: Message):
        if message.author == client.user:
            return

        content: str = message.content
        if type(content) != str:
            return
        for command in commands:
            if content.startswith(command):
                await commands[command](message, client)
