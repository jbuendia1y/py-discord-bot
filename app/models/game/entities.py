from pydantic import BaseModel
# Entity


class StatItemModel(BaseModel):
    hp: int
    armor: int
    attack: int


class StatModel(BaseModel):
    current: StatItemModel
    max: StatItemModel


class EntityModel(BaseModel):
    name: str
    stats: StatModel

    def catch_damage(self, attack: int):
        tota_attack = attack - self.stats.current.armor
        self.stats.current.hp -= tota_attack

    def attack(self):
        return self.stats.current.attack
# Player


class PlayerStatsModel(StatModel):
    base: StatItemModel


class ProgressItem(BaseModel):
    xp: int
    floor: int


class ProgressModel(BaseModel):
    current: ProgressItem
    max: ProgressItem
    lvl: int

    def get_progress_text(self):
        return f"**Level**: {self.lvl}\n**XP**: {self.current.xp} / {self.max.xp}\n**Floor**: {self.current.floor}/{self.max.floor}"


class PlayerModel(EntityModel):
    id: str
    stats: PlayerStatsModel
    progress: ProgressModel
    inventory: dict
    equipped: dict
