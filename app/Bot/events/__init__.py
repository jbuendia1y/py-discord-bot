from discord import Client

from .on_message import on_message
from .on_ready import on_ready


def init_events(client: Client):
    on_message(client)
    on_ready(client)
