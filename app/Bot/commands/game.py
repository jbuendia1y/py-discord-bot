from asyncio import TimeoutError

from discord import Message, Embed, Client
from Game import Player, Battle, Hunt


async def profile(message: Message, _):
    id = message.author.id
    name = message.author.display_name
    player = Player(id=id, name=name)

    await message.channel.send(embed=player.get_profile_embed(message.author.avatar_url))


async def inventory(message: Message, _):
    id = message.author.id
    name = message.author.display_name
    player = Player(id=id, name="Player " + name)

    await message.channel.send(embed=player.inventory.get_embed())


async def battle(message: Message, client: Client):
    embed = Embed()
    embed.title = "Preparing Battle"
    embed.description = "Waiting a player 1/2 ... \n Time for wait 60s"
    emoji_battle = "⚔️"

    msg: Message = await message.channel.send(embed=embed)
    await msg.add_reaction(emoji_battle)

    try:
        reaction, user = await client.wait_for("reaction_add", timeout=60.0, check=lambda reaction, user: str(reaction) == emoji_battle and msg.author.id != user.id and message.author.id != user.id)
        if str(reaction) == emoji_battle and msg.author.id != user.id and message.author.id != user.id:
            player1 = Player(id=message.author.id, name=message.author.name)
            player2 = Player(id=user.id, name=user.name)
            winner = Battle(player1, player2).start_battle()
            return await message.channel.send(f"{emoji_battle} {winner.name} WIN {emoji_battle}")
    except TimeoutError:
        await msg.delete()


async def hunt(message: Message, _):
    player = Player(message.author.id, message.author.name)
    winner = Hunt(player).start_hunt()

    if not winner:
        await message.channel.send("EMPATE !!!")
    else:
        if winner.name != player.name:
            await message.channel.send("You lose")
        else:
            await message.channel.send("You get 5px")


async def use(message: Message, _):
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
