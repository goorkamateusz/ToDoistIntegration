import discord
from src.Discord.DiscordClient import DiscordClient
from src.LanguageProcessor.Processor import Result
from src.ToDoist.ApiClient import ApiClient
from src.Discord.Reactions import managed_msg_reaction, error_reaction
from src.Database.Entities import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent


class Help(OnMessageComponent):
    """ Send message with help manual
    """
    
    async def process(self, msg: discord.Message, content: str) -> None:
        client: DiscordClient = self.client

        message = ""
        for key, component in client.on_messages.items():
            message += f"{key}: {component.__doc__}\n"

        await msg.reply(message)

    async def process_command(self, msg: discord.Message, command: Result):
        await self.process(msg, None)
