from typing import Tuple

from mautrix.types import MessageType
from maubot import Plugin, MessageEvent
from maubot.handlers import command


class MediaBot(Plugin):
    @command.passive("^mxc://.+/.+$", field=lambda evt: evt.content.url if evt.content.url else evt.content.file.url,
                     msgtypes=(MessageType.IMAGE, MessageType.FILE, MessageType.AUDIO,
                               MessageType.STICKER))
    async def handler(self, evt: MessageEvent, url: Tuple[str]) -> None:
        await evt.respond(f"MXC URI: `{url[0]}`")
