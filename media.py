from maubot import Plugin, CommandSpec, PassiveCommand, MessageEvent

COMMAND_MEDIA = "xyz.maubot.media"


class MediaBot(Plugin):
    async def start(self) -> None:
        self.set_command_spec(CommandSpec(
            passive_commands=[PassiveCommand(
                name=COMMAND_MEDIA,
                matches="mxc://.+/.+",
                match_against="url",
            )],
        ))
        self.client.add_command_handler(COMMAND_MEDIA, self.handler)

    async def stop(self) -> None:
        self.client.remove_command_handler(COMMAND_MEDIA, self.handler)

    @staticmethod
    async def handler(evt: MessageEvent) -> None:
        await evt.respond(f"MXC URI: `{evt.content.url}`")
