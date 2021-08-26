from discord import Message, Embed
NAME = "name"
VALUE = "value"
INLINE = "inline"

fields = [
    {
        NAME: "$news",
        VALUE: "Lastet news \n source : 'elcomercio.pe'",
    },
    {
        NAME: "$graph",
        VALUE: "Versatile graphic of the Covid-19",
    },
    {
        NAME: "$search",
        VALUE: "Search video in youtube and get a link",
    },
    {
        NAME: "$quote",
        VALUE: "Get a quote . \n Optional values : --today--"
    },
    {
        NAME: "$anime",
        VALUE: "Search a anime by name. \n command -> $anime name_anime"
    },
    {
        NAME: "$battle",
        VALUE: "Battle PvP"
    },
    {
        NAME: "$hunt",
        VALUE: "Hunt Monsters and get XP"
    },
    {
        NAME: "$profile",
        VALUE: "View you profile of the game"
    }
]


async def help_cmds(message: Message, _):
    embedMSG = Embed()
    embedMSG.title = "Commands"
    [embedMSG.add_field(**field, inline=False) for field in fields]
    embedMSG.set_footer(text="For more information .... \n idk",
                        icon_url="https://avatars.githubusercontent.com/u/71197875?v=4")
    await message.channel.send(embed=embedMSG)
