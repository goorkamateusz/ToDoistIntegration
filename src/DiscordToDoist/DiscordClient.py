from abc import abstractclassmethod
from typing import Dict
import discord

from src.DiscordToDoist.Container import Container, Logger


class DiscordClient(discord.Client):
    def __init__(self, logger: Logger = Container.logger) -> None:
        self.components: Dict[str, DiscordComponent] = {}
        self.logger = logger
        intents = discord.Intents.all()
        super().__init__(intents=intents)

    async def on_ready(self):
        self.logger.log(f'Client {self.user} ready.')

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        prefix, _, content = message.content.partition(' ')
        self.logger.log(f"Processed message | {prefix} | {content}")

        if prefix in self.components:
            await self.components[prefix].process(message, content)


class DiscordComponent:
    def __init__(self, client: DiscordClient) -> None:
        self.client: DiscordClient = client

    @abstractclassmethod
    async def process(self, msg: discord.Message, content: str) -> None:
        raise NotImplemented()

    def current_channel(self, msg: discord.Message):
        return self.client.get_channel(msg.channel.id)
