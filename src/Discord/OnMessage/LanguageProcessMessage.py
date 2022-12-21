import discord
from src.Discord.Container import Container
from src.Discord.DiscordComponent import OnMessageComponent
from src.Discord.DiscordClient import DiscordClient
from src.LanguageProcessor.Processor import LanguageProcessor, Result


class LanguageProcessMessage(OnMessageComponent):
    """ Process natural language command
    """

    def __init__(self,
                 client,
                 todoist=Container.apiClientProvider,
                 db=Container.database,
                 language=Container.languageProcessor):
        super().__init__(client, todoist, db)
        self.language: LanguageProcessor = language

    async def process(self, msg: discord.Message, content: str) -> None:
        commands = self.language.process(content)

        txt = ''
        for c in commands:
            txt += f"{c}\r\n"

        if txt == '':
            txt = "No result"

        await msg.reply(txt)

        if len(commands) > 0:
            first_command = commands[0]
            await self.process_command(msg, first_command)

    async def process_command(self, msg, command: Result):
        discord: DiscordClient = self.client
        command_id = f"!{command.command}"

        if command_id in discord.on_messages:
            component: OnMessageComponent = discord.on_messages[command_id]
            await component.process_command(msg, command)
        if command_id == "selected":
            await msg.reply("Wybierania zadań nie jest obsłużone tekstowo")
