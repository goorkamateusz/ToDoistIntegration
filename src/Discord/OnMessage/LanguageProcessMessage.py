import discord
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
