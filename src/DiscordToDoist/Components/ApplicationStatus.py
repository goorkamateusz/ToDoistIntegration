import discord

from src.DiscordToDoist.DiscordClient import DiscordComponent


class ApplicationStatus(DiscordComponent):
    async def process(self, msg: discord.Message, content: str) -> None:
        await self.current_channel(msg).send("It's working...")
