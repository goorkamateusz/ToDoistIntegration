import discord
from src.Discord.Reactions import managed_msg_reaction
from src.Database.Entities import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent
from src.ToDoist.ApiClient import ApiClient
from src.config import thread_archive_time


class AddingTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        todoist: ApiClient = self.todoist.get_client(msg.channel.id)
        task = todoist.add_task(content)

        thread = await msg.channel.create_thread(
            name=content,
            auto_archive_duration=thread_archive_time,
            message=msg)

        entity = TaskEntity(discord_channel_id=msg.channel.id,
                            discord_msg_id=msg.id,
                            discord_thread_id=thread.id,
                            todoist_task_id=task.id)

        self.db.insert(entity)

        await self.report(entity, reaction=managed_msg_reaction)
