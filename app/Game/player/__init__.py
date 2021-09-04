from discord import Embed

from models.game.entities import PlayerModel


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
