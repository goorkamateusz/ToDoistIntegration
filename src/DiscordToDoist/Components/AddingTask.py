import discord
from src.Database.TaskMsg import TaskMsg
from src.DiscordToDoist.Container import Container
from src.Database.Database import Database
from src.DiscordToDoist.DiscordClient import DiscordComponent


class AddingTask(DiscordComponent):
    async def process(self, msg: discord.Message, content: str) -> None:
        # todo make dependency injection
        todoist = Container.apiClient
        db = Database().db['discord']

        task = todoist.add_task(content)

        channel = msg.channel
        thread = await channel.create_thread(name=content, auto_archive_duration=(60 * 24), message=msg)

        await msg.add_reaction('🔶')

        entity = TaskMsg(channel.id, msg.id, thread.id, task.id)
        db.insert_one(entity.to_dict())
