from discord import Client
from .events import init_events
from os import getenv


class Bot:
    def __init__(self, client: Client) -> None:
        self.client = client
        init_events(self.client)

    def run_bot(self):
        self.client.run(getenv("BOT_TOKEN"))
