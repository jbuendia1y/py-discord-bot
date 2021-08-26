from .news import news_cmds
from .help import help_cmds
from .graphic import graphic_cmds
from .quotes import quotes_cmds

from .audio import Audio_cmds
from .video import Video_cmds
from .server import Server_cmds
from .anime import Anime_cmds

from .game import battle, profile, hunt, inventory, use

_audio = Audio_cmds()
_video = Video_cmds()
_server = Server_cmds()
_anime = Anime_cmds()

commands = {
    "$help": help_cmds,
    "$news": news_cmds,
    "$graph": graphic_cmds,
    "$connect": _audio.connect,
    "$leave": _audio.disconnect,
    "$search": _video.search,
    "$quote": quotes_cmds,
    "$clear": _server.delete_messages,
    "$profile": profile,
    "$battle": battle,
    "$hunt": hunt,
    "$inventory": inventory,
    "$anime": _anime.get_anime,
    "$use": use
}
