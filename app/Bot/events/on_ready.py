from discord import Client


def on_ready(client: Client):
    @client.event
    async def on_ready():
        print("BOT READY")
