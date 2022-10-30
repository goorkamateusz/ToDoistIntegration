from asyncio import Task
import discord
from abc import abstractclassmethod
from src.Discord.Container import Container
from src.ToDoist.ApiClient import ApiClient


class DiscordClient:
    pass


class DiscordComponent:
    def __init__(self,
                 client,
                 todoist=Container.apiClient,
                 db=Container.database):
        self.client: discord.Client = client
        self.todoist: ApiClient = todoist
        self.db_tasks = db.tasks

    def current_channel(self, msg: discord.Message):
        return self.client.get_channel(msg.channel.id)

    async def report(self, entity, communicate=None, reaction=None) -> Task:
        if reaction:
            channel = self.client.get_channel(entity.discord_channel_id)
            msg = channel.get_partial_message(entity.discord_msg_id)
            await msg.add_reaction(reaction)

        if communicate:
            thread = self.client.get_channel(entity.discord_thread_id)
            await thread.send(f"{reaction} {communicate}")


class OnMessageComponent(DiscordComponent):
    @abstractclassmethod
    async def process(self, msg: discord.Message, content: str) -> None:
        raise NotImplementedError()


class OnNotificationComponent(DiscordComponent):
    @abstractclassmethod
    async def process(self, event) -> None:
        raise NotImplementedError()
