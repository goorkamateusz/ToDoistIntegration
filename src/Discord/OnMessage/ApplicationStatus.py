import discord

from src.Discord.DiscordClient import OnMessageComponent


class ApplicationStatus(OnMessageComponent):
    async def process(self, msg: discord.Message, content: str) -> None:
        await self.current_channel(msg).send("It's working...")
