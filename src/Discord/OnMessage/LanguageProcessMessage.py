import discord
from src.Discord.DiscordComponent import DiscordClient
from src.Discord.Container import Container
from src.Discord.DiscordClient import OnMessageComponent
from src.LanguageProcessor.Processor import LanguageProcessor


class LanguageProcessMessage(OnMessageComponent):

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
            discord: DiscordClient = self.client

            new_var = f"!{first_command.command}"
            if new_var in discord.on_messages:
                await discord.on_messages[new_var].process(
                    msg, first_command.dict["content"])
