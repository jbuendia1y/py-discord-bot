from src.modules.game import player_hunt, get_player, init_pvp
from discord import Message, Embed
from discord.ext import commands
from discord.ext.commands import Context


class GameCmds(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="profile")
    async def profile(self, ctx: Context):
        player = get_player(ctx.message.author.id)
        await ctx.message.channel.send(embed=player.get_profile_embed(ctx.message.author.avatar_url))

    @commands.command(name="inventory")
    async def inventory(self, ctx: Context):
        player = get_player(ctx.message.author.id)

        await ctx.message.channel.send("Not available")

    @commands.command(name="battle")
    async def battle(self, ctx: Context):
        message: Message = ctx.message
        embed = Embed()
        embed.title = "Preparing Battle"
        embed.description = "Waiting a player 1/2 ... \n Time for wait 60s"
        emoji_battle = "⚔️"

        msg: Message = await message.channel.send(embed=embed)
        await msg.add_reaction(emoji_battle)

        try:
            reaction, user = await ctx.bot.wait_for("reaction_add", timeout=60.0, check=lambda reaction, user: str(reaction) == emoji_battle and msg.author.id != user.id and message.author.id != user.id)
            if str(reaction) == emoji_battle and msg.author.id != user.id and message.author.id != user.id:
                winner = init_pvp(ctx.message.author.id, user.id)
                return await message.channel.send(f"{emoji_battle} {winner} WIN {emoji_battle}")
        except TimeoutError:
            await msg.delete()

    @commands.command(name="hunt")
    async def hunt(self, ctx: Context):
        player = player_hunt(ctx.message.author.id)

        if player.stats.current.hp <= 0:
            await ctx.message.channel.send("You lose")
        else:
            await ctx.message.channel.send("You Win!!")


def setup(bot: commands.Bot):
    bot.add_cog(GameCmds(bot))
