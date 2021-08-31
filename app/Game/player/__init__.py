from discord import Embed

from models.game.entities import PlayerModel

# 100 * math.exp( lvl / 10 )) -> exp es el número euler a la x
# print(math.exp(1)**(1/3))


class Player(PlayerModel):

    def get_profile_embed(self, avatar: str = None):
        embed = Embed(title=f"Player {self.name}")
        stats = self.stats
        current = self.stats.current

        embed.add_field(name="Progress",
                        value=self.progress.get_progress_text(), inline=False)
        embed.add_field(
            name="Stats", value=f"**HP**: {current.hp}/{stats.max.hp} \n **ARMOR**: {current.armor}/{stats.armor} \n **ATTACK**: {current.attack}/{stats.max.attack}", inline=False)

        if avatar:
            embed.set_thumbnail(url=avatar)
        return embed


""" def use(self, name_consumable: str):
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
            raise e """
