from abc import abstractclassmethod
from asyncio import Task
from typing import Any, Dict
import discord

from Common.LanguageProcessor.Processor import Result
from DiscordBot.Database.Database import Database
from DiscordBot.Database.Entities import TaskEntity
from DiscordBot.Discord.Container import Container
from Common.ToDoist.ApiClient import ApiClientProvider


class DiscordClient:
    pass


class DiscordComponent:

    def __init__(self,
                 client,
                 todoist=Container.apiClientProvider,
                 db=Container.database):
        self.client: discord.Client = client
        self.todoist: ApiClientProvider = todoist
        self.db: Database = db
        self.db_tasks = db._tasks  # todo obsolete

    def current_channel(self, msg: discord.Message):
        return self.client.get_channel(msg.channel.id)

    async def report(self,
                     entity: TaskEntity,
                     communicate: str = None,
                     reaction: str = None) -> Task:
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

    @abstractclassmethod
    async def process_command(self, msg: discord.Message, command: Result):
        raise NotImplementedError()


class OnNotificationComponent(DiscordComponent):
    @abstractclassmethod
    async def process(self, event: Dict[str, Any]) -> None:
        raise NotImplementedError()
