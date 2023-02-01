import discord
from DiscordBot.Discord.DiscordClient import OnMessageComponent


class ApplicationStatus(OnMessageComponent):
    """ Check aplication working status
    """

    async def process(self, msg: discord.Message, content: str) -> None:
        await self.current_channel(msg).send("It's working...")
