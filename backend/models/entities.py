from pydantic import BaseModel


class Common_stats(BaseModel):
    hp: int = 100
    armor: int = 0
    attack: int = 10


class Entity_stats(BaseModel):
    max: Common_stats
    current: Common_stats


class Entity(BaseModel):
    name: str
    stats: Entity_stats

    def dispatch_damage(self) -> int:
        return self.stats.current.attack

    def catch_damage(self, damage: int):
        self.stats.current.hp -= damage


class Enemy(Entity):
    pass
