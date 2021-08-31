from helpers import api
from discord import Message, Embed
from discord.ext import commands
from discord.ext.commands import Context

from Game import Player, Battle, Hunt


class Game_cmds(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="profile")
    async def profile(self, ctx: Context):
        message: Message = ctx.message
        id = message.author.id
        name = message.author.display_name
        player = Player(id=id, name=name)

        await message.channel.send(embed=player.get_profile_embed(message.author.avatar_url))

    @commands.command(name="inventory")
    async def inventory(self, ctx: Context):
        message: Message = ctx.message
        id = message.author.id
        name = message.author.display_name
        player = Player(id=id, name="Player " + name)

        await message.channel.send(embed=player.inventory.get_embed())

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
                player1 = Player(id=message.author.id,
                                 name=message.author.name)
                player2 = Player(id=user.id, name=user.name)
                winner = Battle(player1, player2).start_battle()
                return await message.channel.send(f"{emoji_battle} {winner.name} WIN {emoji_battle}")
        except TimeoutError:
            await msg.delete()

    @commands.command(name="hunt")
    async def hunt(self, ctx: Context):
        url = "/player/"+str(ctx.message.author.id)
        player = Player(**api.get(url).json())
        winner = Hunt(player).start_hunt()

        if winner.name != player.name:
            await ctx.message.channel.send("You lose")
        else:
            await ctx.message.channel.send("You get 5px")

    @commands.command(name="use")
    async def use(self, ctx: Context):
        message: Message = ctx.message
        content: list[str] = message.content.split(" ")
        if len(content) == 1:
            return await message.channel.send("The command '$use' need a param")
        content.pop(0)
        player = Player(message.author.id, message.author.name)
        try:
            stat, amount = player.use(" ".join(content))
            await message.channel.send(f"{stat} +{amount}")
        except Exception as e:
            await message.channel.send(e.args[0])


def setup(bot: commands.Bot):
    bot.add_cog(Game_cmds(bot))
