from typing import Dict
from asyncio import Queue
from discord.ext import tasks
import discord
import logging
from src.Discord.DiscordComponent import OnMessageComponent, OnNotificationComponent

from src.WebhookServer.WebServer import web_server


class DiscordClient(discord.Client):
    def __init__(self) -> None:
        self.on_messages: Dict[str, OnMessageComponent] = {}
        self.on_notification: Dict[str, OnNotificationComponent] = {}
        self.tasks = []
        intents = discord.Intents.all()
        super().__init__(intents=intents)

    async def on_ready(self):
        logging.info(f'Client {self.user} ready.')
        self.__create_tasks()

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        prefix, _, content = message.content.partition(' ')
        logging.info(f"Processed message | {prefix} | {content}")

        if prefix in self.on_messages:
            await self.on_messages[prefix].process(message, content)

    def __create_tasks(self):
        taskQueue = Queue()
        self.loop.create_task(web_server(taskQueue))
        self.loop.create_task(self._process_events(taskQueue))

    @tasks.loop()
    async def _process_events(self, queue: Queue):
        while True:
            event = await queue.get()
            event_type = event["event_name"]
            logging.info(f"Processed notification | {event_type}")
            if event_type in self.on_notification:
                await self.on_notification[event_type].process(event)
