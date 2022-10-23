import discord
from src.DiscordToDoist.Reactions import managed_msg_reaction
from src.Database.TaskMsg import TaskMsg
from src.DiscordToDoist.Container import Container
from src.Database.Database import Database
from src.DiscordToDoist.DiscordClient import DiscordComponent


class AddingTask(DiscordComponent):
    async def process(self, msg: discord.Message, content: str) -> None:
        # todo make dependency injection
        todoist = Container.apiClient
        db = Database().discord

        task = todoist.add_task(content)

        thread = await msg.channel.create_thread(name=content, auto_archive_duration=(60 * 24), message=msg)

        await msg.add_reaction(managed_msg_reaction)

        entity = TaskMsg(msg.channel.id, msg.id, thread.id, task.id)
        db.insert_one(entity.to_dict())
