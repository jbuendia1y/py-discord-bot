from pydantic import BaseModel
from typing import Optional, List

from .entities import Entity, Common_stats, Entity_stats
from .items import Consumable, Item


class Progress_stats(BaseModel):
    xp: int = 0
    floor: int = 1


class Progress(BaseModel):
    current: Progress_stats
    max: Progress_stats
    lvl: int


class Inventory(BaseModel):
    consumables: List[Consumable] = []
    items: List[Item] = []


class Stats(Entity_stats):
    base: Common_stats


class Player(Entity):
    id: Optional[str]
    name: str
    stats: Stats
    inventory: Inventory
    equipped: dict
    progress: Progress

    def compute_damage(self):
        return self.stats.current.attack

    def dispatch_damage(self):
        return self.compute_damage()

    def catch_damage(self, damage: int):
        self.stats.current.hp -= damage

# Inventory dict -> {items,consumables}
# Equipped dict -> {sword, armor}
# stats dict -> {hp,armor,attack}
# progress dict -> {lvl,current_xp,max_xp,floor,current_floor}
