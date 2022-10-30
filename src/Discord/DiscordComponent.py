import discord
from abc import abstractclassmethod
from src.Discord.Container import Container
from src.ToDoist.ApiClient import ApiClient
from src.Discord.Container import Container
from src.Database.Database import Database


class DiscordClient:
    pass


class DiscordComponent:
    def __init__(self, client: DiscordClient, todoist=Container.apiClient, db=Container.database):
        self.client = client
        self.todoist = todoist
        self.db = db.discord


class OnMessageComponent(DiscordComponent):
    @abstractclassmethod
    async def process(self, msg: discord.Message, content: str) -> None:
        raise NotImplemented()

    def current_channel(self, msg: discord.Message):
        return self.client.get_channel(msg.channel.id)


class OnNotificationComponent(DiscordComponent):
    @abstractclassmethod
    async def process(self, event) -> None:
        raise NotImplemented()
