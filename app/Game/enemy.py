from .stats import Stats
from .entity import Entity


class Enemy(Entity):

    def __init__(self, name: str = "", stats: Stats = None) -> None:
        super().__init__(name, stats or Stats(70, 0, 10, 100))
