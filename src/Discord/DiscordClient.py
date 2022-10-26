from abc import abstractclassmethod
from typing import Dict
import discord
from asyncio import Queue

from discord.ext import tasks

from src.Discord.Container import Container, Logger
from src.WebhookServer.WebServer import web_server


class DiscordClient(discord.Client):
    def __init__(self, logger: Logger = Container.logger) -> None:
        self.on_messages: Dict[str, OnMessageComponent] = {}
        self.on_notification: Dict[str, OnNotificationComponent] = {}
        self.tasks = []
        self.logger = logger
        intents = discord.Intents.all()
        super().__init__(intents=intents)

    async def on_ready(self):
        self.logger.log(f'Client {self.user} ready.')
        self.__create_tasks()

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        prefix, _, content = message.content.partition(' ')
        self.logger.log(f"Processed message | {prefix} | {content}")

        if prefix in self.on_messages:
            await self.on_messages[prefix].process(message, content)

    def __create_tasks(self):
        taskQueue = Queue()
        self.loop.create_task(web_server(taskQueue))
        self.loop.create_task(self._test(taskQueue))

    @tasks.loop()
    async def _test(self, queue: Queue):
        while True:
            event = await queue.get()
            event_type = event["event_name"]
            if event_type in self.on_notification:
                await self.on_notification[event_type].process(event)


class DiscordComponent:
    def __init__(self, client: DiscordClient) -> None:
        self.client: DiscordClient = client


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
