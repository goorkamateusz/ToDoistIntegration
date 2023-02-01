import discord
from DiscordBot.Discord.DiscordClient import DiscordClient
from Common.LanguageProcessor.Processor import Result
from Common.ToDoist.ApiClient import ApiClient
from DiscordBot.Discord.Reactions import managed_msg_reaction, error_reaction
from DiscordBot.Database.Entities import TaskEntity
from DiscordBot.Discord.DiscordClient import OnMessageComponent


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
