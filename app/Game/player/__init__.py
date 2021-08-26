from discord import Embed


from ..stats import Stats
from ..entity import Entity
from ..invetory import Inventory
from ..items import Consumable
from .equipped import Equipped
from .progress import Progress

# 100 * math.exp( lvl / 10 )) -> exp es el número euler a la x
# print(math.exp(1)**(1/3))


class Player(Entity):
    def __init__(self, id: int, name: str = "", stats: Stats = None, inventory: Inventory = None, progress: Progress = None, equiped: Equipped = None) -> None:
        self.id = id
        self.inventory = inventory or Inventory(
            consumables=[Consumable("Life Potion", {"amount": 100, "stat": "hp"})])
        self.equipped = equiped or Equipped()
        self.progress = progress or Progress(24, 0, 1)

        # Call to calculate_current_stats method and pass the list of equipped
        super().__init__(name, stats or Stats(100, 0, 10, 100, 1))
        self.stats.calculate_current_stats(self.equipped.get_equipped())

    def catch_damage(self, attack: int):
        total_attack = attack - self.stats.armor
        super().catch_damage(total_attack)

    def attack(self):
        return super().attack()

    def use(self, name_consumable: str):
        if len(self.inventory.consumables) == 0:
            raise Exception("The Player don't have items in their inventory")
        try:
            consumable = self.inventory.get_consumbale(name_consumable)
            stat, amount = consumable.use()
            self.inventory.consumables.remove(consumable)
            setattr(self.stats.current, stat,
                    getattr(self.stats.current, stat) + amount)
            return (stat, getattr(self.stats.current, stat))
        except Exception as e:
            raise e

    def get_profile_embed(self, avatar: str = None):
        embed = Embed(title=f"Player {self.name}")
        stats = self.stats
        current = self.stats.current

        embed.add_field(name="Progress",
                        value=self.progress.get_progress_text(), inline=False)
        embed.add_field(
            name="Stats", value=f"**HP**: {current.hp}/{stats.hp} \n **ARMOR**: {current.armor}/{stats.armor} \n **ATTACK**: {current.attack}/{stats.attack}", inline=False)

        if avatar:
            embed.set_thumbnail(url=avatar)
        return embed
